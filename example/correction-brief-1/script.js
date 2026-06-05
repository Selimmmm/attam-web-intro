// À remplir avec tes propres identifiants (Project Settings → API dans Supabase).
const URL_SUPABASE = "https://xxxx.supabase.co"; // ton URL de projet
const CLE_ANON = "eyJhbGciOi..."; // ta clé anon (anon public)

const supabase = window.supabase.createClient(URL_SUPABASE, CLE_ANON);

const form = document.querySelector("#contact");
const confirmation = document.querySelector("#confirmation");

form.addEventListener("submit", async (event) => {
  event.preventDefault(); // empêche le rechargement de la page

  const nom = document.querySelector("#nom").value;
  const email = document.querySelector("#email").value;
  const message = document.querySelector("#message").value;

  if (!nom || !email.includes("@") || !message) {
    confirmation.textContent = "Remplis tous les champs avec un e-mail valide.";
    return;
  }

  const { error } = await supabase
    .from("contacts")
    .insert({ nom: nom, email: email, message: message });

  if (error) {
    confirmation.textContent = "Oups, l'envoi a échoué. Réessaie.";
    console.error(error);
  } else {
    confirmation.textContent = `Merci ${nom}, ton message a bien été enregistré.`;
    form.reset();
  }
});
