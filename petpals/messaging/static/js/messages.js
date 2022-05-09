window.onload = function() {
    messageItems = document.querySelectorAll(".message-card");
    if (messageItems.length == 0) {
        document.querySelector(".forum-main-body").innerHTML += "<h1 class='no-message-cards'> No Messages to Display. Send a New Message and it Will Appear Here! </h1>"  
    }
}