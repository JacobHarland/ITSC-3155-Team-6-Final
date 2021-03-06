from flask import Blueprint, render_template, request, abort
from flask_login import current_user, login_required
from sqlalchemy import func, and_, or_, desc
from petpals import db, socket
from petpals.models import Messages, User

router = Blueprint(
    'message_router',
    __name__,
    url_prefix='/messages',
    template_folder='templates',
    static_folder="static",
)


@router.get('')
@login_required
def render_message_page():

    # This source was very useful: https://stackoverflow.com/a/45779686

    subqry = (
        db.session.query(
            Messages.conversation_id, func.max(Messages.time_sent).label("last_time")
        )
        .outerjoin(
            User,
            or_(
                User.username == Messages.sender_username,
                User.username == Messages.recipient_username,
            ),
        )
        .filter(User.id == current_user.id)
        .group_by(Messages.conversation_id)
        .subquery()
    )

    msg_query = Messages.query.join(
        subqry,
        and_(
            Messages.conversation_id == subqry.c.conversation_id,
            Messages.time_sent == subqry.c.last_time,
        ),
    ).order_by(desc(Messages.time_sent))

    def get_prof_pic(username):
        prof_pic_query = User.query.filter_by(username=username).first()
        return prof_pic_query.image_path

    return render_template(
        'messages.html', recent_messages=msg_query, get_prof_pic=get_prof_pic
    )


@router.get('/new')
@login_required
def render_new_conversation_page():
    usernames = []

    users = User.query.all()
    messages = Messages.query.all()

    for user in users:
        if current_user.username != user.username:
            usernames.append(user.username)

    for message in messages:
        if current_user.username == message.sender_username:
            if message.recipient_username in usernames:
                usernames.remove(message.recipient_username)
        elif current_user.username == message.recipient_username:
            if message.sender_username in usernames:
                usernames.remove(message.sender_username)

    return render_template(
        'new_message.html',
        usernames=sorted(usernames),
    )


@router.post('/new')
@login_required
def create_new_conversation():
    data = request.json
    new_message = Messages()

    next_conversation_id = 0
    conversation_id_query = db.session.query(
        func.max(Messages.conversation_id).label("highest_convo")
    )

    try:
        next_conversation_id = int(conversation_id_query.first()['highest_convo']) + 1
    except Exception:
        next_conversation_id = 1

    new_message.recipient_username = data['recipient']
    new_message.sender_username = data['sender']
    new_message.message = data['message']
    new_message.conversation_id = next_conversation_id

    db.session.add(new_message)
    db.session.commit()
    return {'convo_id': next_conversation_id}


@router.get("/conversation/<conversation_id>")
@login_required
def get_conversation(conversation_id):
    messages = Messages.query.filter_by(conversation_id=conversation_id).all()
    if len(messages) == 0:
        abort(404)
    elif (messages[0].sender_username == current_user.username) or (
        messages[0].recipient_username == current_user.username
    ):
        if messages[0].sender_username == current_user.username:
            recipient = messages[0].recipient_username
        else:
            recipient = messages[0].sender_username
    else:
        abort(403)

    return render_template(
        'conversation.html',
        recipient=recipient,
        messages=messages,
        conversation_id=conversation_id,
    )


@socket.on('message')
def handle_message(message):
    new_message = Messages()
    new_message.conversation_id = message['conversation_id']
    new_message.recipient_username = message['recipient']
    new_message.sender_username = message['sender']
    new_message.message = message['message']

    db.session.add(new_message)
    db.session.commit()

    socket.send(message)
