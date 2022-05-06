let submitButton = document.getElementById('submit');

submitButton.addEventListener('click', function() {
    recipient = document.getElementById("recipient").value.replaceAll("`", "");
    sender = document.getElementById("sender").dataset["name"];
    message = document.getElementById("new_message").value.replaceAll("`", "");

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
    
    window.location = "/messages"
})