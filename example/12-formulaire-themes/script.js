// Changer le thème : on écrit l'attribut data-theme sur la balise <html>.
// daisyUI applique alors toutes les couleurs du thème choisi.
const selecteurTheme = document.querySelector("#theme");

selecteurTheme.addEventListener("change", () => {
  document.documentElement.setAttribute("data-theme", selecteurTheme.value);
});

// Le formulaire, comme à l'étape 5 : validation et message de retour, sans base de données.
const form = document.querySelector("#contact");
const confirmation = document.querySelector("#confirmation");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const nom = document.querySelector("#nom").value;
  const email = document.querySelector("#email").value;
  const message = document.querySelector("#message").value;

  if (!nom || !email.includes("@") || !message) {
    confirmation.textContent = "Remplis tous les champs avec un e-mail valide.";
    return;
  }

  confirmation.textContent = `Merci ${nom}, ton message a bien été pris en compte.`;
  form.reset();

  


});
