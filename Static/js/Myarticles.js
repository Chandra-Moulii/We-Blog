function deleteall() {
  document.querySelector(".delete").classList.add("delactive");
}
function closepop() {
  document.querySelector(".delete").classList.remove("delactive");
}

window.addEventListener("scroll", (event) => {
  let scroll = this.scrollY;
  try {
    if (scroll > 170) {
      document.querySelector(".Totop").style.display = "flex";
    } else {
      document.querySelector(".Totop").style.display = "none";
    }
  } catch (TypeError) {
    console.log("No such thing");
  }
});


function Copy(svg) {
    navigator.clipboard.writeText(svg.id);
    var message = document.createElement("span");
    var actualmessage = document.createTextNode("Link copied");
    message.appendChild(actualmessage);
    var element = document.querySelector("[id=" + svg.parentElement.id + "]");
    if (element.querySelector("span") !== null) {
      console.log("Already copied");
    } else {
      element.appendChild(message);
      setTimeout(() => {
        element.removeChild(element.lastChild);
      }, 2000);
    }
  }


  function createarticle() {
    document
      .querySelector(".createarticle")
      .classList.toggle("createarticleactive");
  }
  function closee() {
    document
      .querySelector(".createarticle")
      .classList.remove("createarticleactive");
  }1