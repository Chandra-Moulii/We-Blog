setTimeout(() => {
  document.querySelector(".Error").innerText = "";
}, 5000);

document.querySelector(".Show").style.display = "none";
var type = document.querySelector("#Password");
type.addEventListener("change", () => {
  if (type.value === "") {
    document.querySelector(".Show").style.display = "none";
  } else {
    document.querySelector(".Show").style.display = "block";
  }
});

function Show(p) {
  if (type.type === "text") {
    document.querySelector("#Password").type = "password";
    // document.querySelector("#Confirmpassword").type = "password";
    p.innerText = "Show password";
  } else {
    document.querySelector("#Password").type = "text";
    // document.querySelector("#Confirmpassword").type = "password";
    p.innerText = "Hide password";
  }
}

const animate = gsap.timeline({ repeat: -1 });
animate
  .to(".moveright", { x: 70, duration: 5 })
  .to(".moveright", { x: 0, duration: 5 });
const anim = gsap.timeline({ repeat: -1 });
anim
  .to(".moveleft", { x: -120, duration: 5 })
  .to(".moveleft", { x: 0, duration: 5 });
const anims = gsap.timeline({ repeat: -1 });
anims
  .to(".movearm", { rotate: -45, y: 20, duration: 5 })
  .to(".movearm", { rotate: 0, y: 0, duration: 5 });
const animss = gsap.timeline({ repeat: -1 });
animss
  .to(".movehand", { rotate: -44, x: 60, y: -13, duration: 5 })
  .to(".movehand", { rotate: 0, x: 0, y: 0, duration: 5 });

const write = document.querySelector(".sub").innerText;
document.querySelector(".sub").innerText = "";
var i = 0;
(function loopIt(i) {
  setTimeout(function () {
    document.querySelector(".sub").textContent += write[i];
    if (i < write.length - 1) loopIt(i + 1);
  }, 50);
})(i);
