const elementsArray = document.querySelectorAll(".like");

function updateLikes(elem, liked) {
  const iElem = elem.querySelector("i");
  const spanElem = elem.querySelector("span");
  if (liked) {
    iElem.classList.replace("fa-regular", "fa-solid");
    spanElem.textContent = Number(spanElem.textContent) + 1;
  } else {
    iElem.classList.replace("fa-solid", "fa-regular");
    spanElem.textContent = Number(spanElem.textContent) - 1;
  }
}

async function sendLike(elem, id, URL) {
  await fetch(URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ id: id }),
  })
    .then(async (response) => {
      if (response.ok) {
        return response.json();
      } else {
        const text = await response.text();
        throw new Error(text);
      }
    })
    .then((data) => updateLikes(elem, data.liked));
}

elementsArray.forEach((elem) => {
  elem.addEventListener("click", () => {
    if ("postId" in elem.dataset) {
      sendLike(elem, elem.dataset["postId"], "/forum/post/like");
    } else {
      sendLike(elem, elem.dataset["replyId"], "/forum/post/reply/like");
    }
  });
});
