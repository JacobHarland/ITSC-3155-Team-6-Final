var submitButton = document.getElementById('submit');

current_user = document.getElementById("conversation").dataset['current_user']


recipient = document.getElementById("conversation").dataset["recipient"];
sender = document.getElementById("conversation").dataset["sender"];
message = document.getElementById("new_message").value.replaceAll("`", "");
conversation_id = document.getElementById("conversation").dataset["conversation_id"]

document.getElementById("message-container").scrollTop = document.getElementById("message-container").scrollHeight;

// Socket IO
socket = io()
socket.connect('http://127.0.0.1:5000/messages/conversation/' + conversation_id)

socket.on('message', function(message) {
    if (message['recipient'] == current_user && ((message['sender'] == recipient) || (message['recipient'] == recipient))) {
        let container = document.createElement("container");
        let header = document.createElement("header");
        let new_message = document.createElement("new_message");
        let time = document.createElement("time");

        container.innerHTML = "<div></div>"

        container.setAttribute("class", "message recipient")
        container.setAttribute("id", "recipient")

        header.innerHTML = "<h2>" + message['sender'] + "</h2>";
        header.setAttribute("id", "recipient-name");
        container.appendChild(header);

        new_message.innerHTML = "<h4>" + message['message'] + "</h4>";
        container.appendChild(new_message)

        time.innerHTML = "<p>Just now</p>";
        time.setAttribute("id", "time")
        container.appendChild(time);    

        document.getElementById("message-container").append(container)

        document.getElementById("message-container").scrollTop = document.getElementById("message-container").scrollHeight;
    }
})

// Event Listener for 'Enter' Key Press
messageSender = document.getElementById("new_message")

messageSender.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        recipient = document.getElementById("conversation").dataset["recipient"];
        sender = document.getElementById("conversation").dataset["sender"];
        message = document.getElementById("new_message").value.replaceAll("`", "");
        conversation_id = document.getElementById("conversation").dataset["conversation_id"]

        socket.send({
            'conversation_id': conversation_id,
            'sender': sender,
            'message': message,
            'recipient': recipient
        })

        let container = document.createElement("container");
        let header = document.createElement("header");
        let new_message = document.createElement("new_message");
        let time = document.createElement("time");

        container.innerHTML = "<div></div>";

        container.setAttribute("class", "message sender");
        container.setAttribute("id", "sender");

        header.innerHTML = "<h2>" + sender + "</h2>";
        header.setAttribute("id", "sender-name");
        container.appendChild(header);

        new_message.innerHTML = "<h4>" + message + "</h4>";
        container.appendChild(new_message)

        time.innerHTML = "<p>Just now</p>";
        time.setAttribute("id", "time")
        container.appendChild(time);    

        document.getElementById("message-container").append(container)

        document.getElementById("message-container").scrollTop = document.getElementById("message-container").scrollHeight;

        document.getElementById("new_message").value = ''
    }
})