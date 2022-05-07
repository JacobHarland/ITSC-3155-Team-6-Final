let messageSender = document.getElementById('new_message');



messageSender.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        recipient = document.getElementById("recipient").value.replaceAll("`", "");
        sender = document.getElementById("sender").dataset["name"];
        message = document.getElementById("new_message").value.replaceAll("`", "");
        conversation_id = document.getElementById("sender").dataset["conversation_id"];

    data = {
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

    fetch("/messages/new/" + recipient, options);
    
    window.location = "/messages/" + conversation_id
    }
})