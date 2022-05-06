var submitButton = document.getElementById('submit');

recipient = document.getElementById("conversation").dataset["recipient"];
sender = document.getElementById("conversation").dataset["sender"];
message = document.getElementById("new_message").value.replaceAll("`", "");
conversation_id = document.getElementById("conversation").dataset["conversation_id"]

document.getElementById("message-container").scrollTop = document.getElementById("message-container").scrollHeight;

submitButton.addEventListener('click', function() {
    recipient = document.getElementById("conversation").dataset["recipient"];
    sender = document.getElementById("conversation").dataset["sender"];
    message = document.getElementById("new_message").value.replaceAll("`", "");
    conversation_id = document.getElementById("conversation").dataset["conversation_id"]

    data = {
        conversation_id: conversation_id,
        sender: sender,
        recipient: recipient,
        message: message
    }

    options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }

    let container = document.createElement("container");
    let header = document.createElement("header");
    let new_message = document.createElement("new_message");
    let time = document.createElement("time");

    container.innerHTML = "<div></div>"

    container.setAttribute("class", "message sender")
    container.setAttribute("id", "sender")

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

    fetch("/messages/conversation/" + conversation_id, options);
})