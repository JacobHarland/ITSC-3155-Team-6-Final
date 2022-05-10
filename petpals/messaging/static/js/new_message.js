let messageSender = document.getElementById('new_message');
let listSearch = document.getElementById('listSearch');
let list = document.getElementById('myList');
let listItems = list.getElementsByTagName('li');
let recipient = '';

    window.onload = function() {
        for (i = 0; i < listItems.length; i++) {
            listItems[i].textContent = listItems[i].textContent.trim(" ")
            listItems[i].style.display = 'none';
        }
    }

    listSearch.addEventListener("keyup", function(event) {
        var value = listSearch.value.toLowerCase();
        for (i = 0; i < listItems.length; i++) {
            if (listItems[i].textContent.toLowerCase().indexOf(value) > -1) {
                listItems[i].style.display = 'block';
            } 
            if (listItems[i].textContent.toLowerCase().indexOf(value) == -1) {
                listItems[i].style.display = 'none';
            }
            if (value == '') {
                listItems[i].style.display = 'none';
            }
        }
    });


    for (i = 0; i < listItems.length; i++) {
        listItems[i].addEventListener('click', function(event) {
            recipient = this.textContent;
    
            recipientHeader = document.createElement('div');
            recipientHeader.setAttribute('id', 'recipient-header');
            recipientHeader.innerHTML = "<h1 style='color: #f07178;'>" + recipient + "</h1>";
    
            document.querySelector('.user-search').replaceChildren(recipientHeader);
        })
    }
    

messageSender.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        const sender = document.getElementById("sender").dataset["name"];
        const message = document.getElementById("new_message").value.replaceAll("`", "");
        const conversation_id = parseInt(document.getElementById("sender").dataset["conversation_id"]);

        if (recipient != '') {
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

            sendNewMessage(("/messages/new" ), options);

        } else {
            alert("Please enter a recipient!")
        }
    
    
    }
})

async function sendNewMessage(URL, options) {
    await fetch(URL, options, {
        options
    })
    .then (async (response) => response.json())
    .then ((data) => {
        console.log(data)
        window.location = "/messages/conversation/" + data['convo_id'];
    })
        
        
    }