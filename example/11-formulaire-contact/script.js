const form = document.querySelector("#contact");
const confirmation = document.querySelector("#confirmation");

form.addEventListener("submit", (event) => {
  event.preventDefault(); // empêche le rechargement de la page

  const nom = document.querySelector("#nom").value;
  const email = document.querySelector("#email").value;
  const message = document.querySelector("#message").value;

  if (!nom || !email.includes("@") || !message) {
    confirmation.textContent = "Remplis tous les champs avec un e-mail valide.";
    return;
  }

  // Pas de base de données ici : on se contente de valider et de répondre.
  confirmation.textContent = `Merci ${nom}, ton message a bien été pris en compte.`;
  form.reset();
});
