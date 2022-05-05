const elementsArray = document.querySelectorAll(".like");

elementsArray.forEach((elem) => {
  elem.addEventListener("click", () => {
    data = fetch("/forum/post/reply/like", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ replyId: elem.dataset["replyId"] }),
    })
      .then((response) => response.json())
      .then((data) => {
        const iTag = elem.querySelector("i");
        const spanTag = elem.querySelector("span");
        if (data.liked) {
          iTag.classList.replace("fa-regular", "fa-solid");
          spanTag.textContent = Number(spanTag.textContent) + 1;
        } else {
          iTag.classList.replace("fa-solid", "fa-regular");
          spanTag.textContent = Number(spanTag.textContent) - 1;
        }
      });
  });
});
