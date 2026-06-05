// On récupère les éléments 'formulaire' et 'confirmation'
const form = document.querySelector("#contact");
const confirmation = document.querySelector("#confirmation");

// On 'écoute' le formulaire 
// (seulement l'event 'submit' = cliquer sur un bouton avec type="submit")
form.addEventListener("submit", (event) => {

  event.preventDefault(); // empêche le rechargement de la page (qui est auto avec type="submit")

  // On sélectionne les valeurs de nom, d'email et de message qui ont été complétées
  const nom = document.querySelector("#nom").value;
  const email = document.querySelector("#email").value;
  const message = document.querySelector("#message").value;

  // Ligne de test : 
  // On vérifie : 
  // - que le nom n'est pas vide
  // - que l'email contient un symbole '@'
  // - que le message n'est pas vide
  if (!nom || !email.includes("@") || !message) {
    // On change le message de confirmation
    confirmation.textContent = "Remplis tous les champs avec un e-mail valide.";
    return;
  }

  // Pas de base de données ici : on se contente de valider et de répondre.
  confirmation.textContent = `Merci ${nom}, ton message a bien été pris en compte.`;
  form.reset();
});
