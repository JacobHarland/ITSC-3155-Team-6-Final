from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from sqlalchemy import func
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

active_page = "messages"


@login_required
@router.get('')
def render_message_page():
    unique_conversation_ids = []
    recent_conversations = []
    recent_messages = []
    sender_messages = (
        Messages.query.filter_by(sender_username=current_user.username)
        .order_by(Messages.time_sent.desc())
        .all()
    )
    recipient_messages = (
        Messages.query.filter_by(recipient_username=current_user.username)
        .order_by(Messages.time_sent.desc())
        .all()
    )

    for message in sender_messages:
        recent_conversations.append(message)
        if message.conversation_id not in unique_conversation_ids:
            unique_conversation_ids.append(message.conversation_id)

    for message in recipient_messages:
        recent_conversations.append(message)
        if message.conversation_id not in unique_conversation_ids:
            unique_conversation_ids.append(message.conversation_id)

    for id in unique_conversation_ids:
        for message in recent_conversations:
            if message.conversation_id in unique_conversation_ids:
                recent_messages.append(message)
                unique_conversation_ids.remove(message.conversation_id)

    return render_template(
        'messages.html',
        recent_messages=recent_messages,
        current_user=current_user,
        active_page=active_page,
    )


@login_required
@router.get('/new')
def render_new_conversation_page():
    usernames = []
    next_conversation_id = 0
    conversation_id_query = db.session.query(func.max(Messages.conversation_id)).all()

    if conversation_id_query[0][0] != None:
        next_conversation_id = (
            int(db.session.query(func.max(Messages.conversation_id)).all()[0][0]) + 1
        )
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
        active_page=active_page,
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
