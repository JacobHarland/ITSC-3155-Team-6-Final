from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from sqlalchemy import func, and_
from petpals import db, socket
from petpals.models import Messages, User
from datetime import datetime
import time

router = Blueprint(
    'message_router',
    __name__,
    url_prefix='/messages',
    template_folder='templates',
    static_folder="static",
)


@login_required
@router.get('')
def render_message_page():
    subqry = (
        db.session.query(func.max(Messages.time_sent).label("last_time"))
        .outerjoin(User, User.username == Messages.sender_username)
        .filter(User.id == current_user.id)
        .group_by(Messages.conversation_id)
        .subquery('t2')
    )

    msg_query = Messages.query.join(
        subqry,
        and_(
            Messages.sender_username == current_user.username,
            Messages.time_sent == subqry.c.last_time,
        ),
    )

    return render_template(
        'messages.html',
        recent_messages=msg_query,
        current_user=current_user,
    )


@login_required
@router.get('/new')
def render_new_conversation_page():
    usernames = []
    next_conversation_id = 0
    conversation_id_query = db.session.query(func.max(Messages.conversation_id)).all()

    if conversation_id_query[0][0] != None:
        next_conversation_id = int(conversation_id_query[0][0]) + 1
    else:
        next_conversation_id = 1

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
        conversation_id=next_conversation_id,
    )


@login_required
@router.post('/new/<recipient>')
def create_new_conversation(recipient):
    data = request.json
    next_conversation_id = 0
    new_message = Messages()

    try:
        next_conversation_id = (
            int(db.session.query(func.max(Messages.conversation_id)).all()[0][0]) + 1
        )
    except Exception:
        next_conversation_id = 1

    new_message.recipient_username = data['recipient']
    new_message.sender_username = data['sender']
    new_message.message = data['message']
    new_message.conversation_id = next_conversation_id

    db.session.add(new_message)
    db.session.commit()
    return recipient


@login_required
@router.get("/conversation/<conversation_id>")
def get_conversation(conversation_id):
    time.sleep(1)

    messages = Messages.query.filter_by(conversation_id=conversation_id).all()
    if messages[0].sender_username == current_user.username:
        recipient = messages[0].recipient_username
    else:
        recipient = messages[0].sender_username

    return render_template(
        'conversation.html',
        recipient=recipient,
        messages=messages,
        current_user=current_user,
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
    return message
