function Showprofilepic() {
  document.querySelector(".Profilepicdiv").classList.add("show");
}

function Closeimg() {
  document.querySelector(".Profilepicdiv").classList.remove("show");
}

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
