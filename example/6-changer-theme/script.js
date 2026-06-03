// On récupère deux éléments de la page :
// - le <link> du style, pour changer le fichier CSS
// - le bouton, pour réagir au clic
const lienStyle = document.getElementById("theme");
const bouton = document.getElementById("changer-theme");

// À chaque clic sur le bouton, on bascule d'un thème à l'autre.
bouton.addEventListener("click", function () {
  if (lienStyle.getAttribute("href") === "style-brutaliste.css") {
    lienStyle.setAttribute("href", "style-minimaliste.css");
    bouton.textContent = "Thème brutaliste";
  } else {
    lienStyle.setAttribute("href", "style-brutaliste.css");
    bouton.textContent = "Thème minimaliste";
  }
});
