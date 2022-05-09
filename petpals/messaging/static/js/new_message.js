var recipient = null;


let messageSender = document.getElementById('new_message');
let listSearch = document.getElementById('listSearch');
let list = document.getElementById('myList');
let listItems = list.getElementsByTagName('li');

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
        var sender = document.getElementById("sender").dataset["name"];
        var message = document.getElementById("new_message").value.replaceAll("`", "");
        var conversation_id = parseInt(document.getElementById("sender").dataset["conversation_id"]);

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
    
    window.location = "/messages/conversation/" + conversation_id;
    }
})
