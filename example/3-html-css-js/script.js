const total = document.querySelector("#total");
const bouton = document.querySelector("#ajouter");

let sessions = 0;

bouton.addEventListener("click", () => {
  sessions = sessions + 1;
  total.textContent = sessions;
});
