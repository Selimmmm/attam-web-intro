# Brief 1 : ma page de présentation, en ligne (HTML, Tailwind, JS, GitHub Pages, Supabase)

- **Type** : brief par groupe
- **Référentiel** : [2025] Mobiliser les compétences informatiques fondamentales

Aujourd'hui, vous écrivez le code vous-mêmes, ligne par ligne, pour comprendre comment une page web est construite. À la fin, vous aurez une page qui présente une application, publiée en ligne, avec un formulaire de contact dont les messages sont enregistrés dans une base de données.

## Contexte du projet

Une page web, c'est trois langages qui travaillent ensemble : le **HTML** (le contenu et la structure : « voici un titre, voici une image »), le **CSS** (l'apparence : couleurs, polices, mise en page) et le **JavaScript** (le comportement : ce qui bouge quand on clique). On goûte d'abord au CSS « à la main », puis on passe à **Tailwind** (et daisyUI) pour styler vite, sans écrire de feuille de style.

Le but du jour : construire **votre page de présentation**, une mini-page qui met en valeur l'application que vous avez créée avec Google AI Studio (son nom, ce qu'elle fait, une capture, un lien pour l'essayer), la **mettre en ligne** sur une adresse publique, et y ajouter un **formulaire de contact** dont les messages sont enregistrés dans une base de données.

> Si vous préférez un autre sujet, c'est libre : vous pouvez présenter un projet personnel, une association, ou un sujet qui vous tient à cœur, au lieu de l'application AI Studio. Les étapes restent exactement les mêmes.

## Ressources

- MDN, le manuel de référence du web (en français) : <https://developer.mozilla.org/fr/docs/Learn_web_development>
- Toxicode pour s'entraîner de façon ludique : <https://www.toxicode.fr/learn>
- Un éditeur de code (VS Code) avec l'extension Live Server.
- GitHub Pages, démarrage : <https://pages.github.com/>
- Tailwind (classes utilitaires) : <https://tailwindcss.com/docs/styling-with-utility-classes>
- daisyUI (composants) et ses thèmes : <https://daisyui.com/components/> · <https://daisyui.com/docs/themes/>
- Supabase, doc JavaScript : <https://supabase.com/docs/reference/javascript/introduction>
- Antisèche Markdown : <https://www.markdownguide.org/cheat-sheet/>

## Modalités pédagogiques

Travail en groupe, avec démos collectives du formateur entre chaque étape. On code en direct, on casse, on répare. Chaque étape est découpée en petits pas : faites-les **un par un**, et vérifiez le résultat dans le navigateur après chaque pas avant de passer au suivant. Répartissez-vous les rôles dans le groupe, mais avancez sur **une seule page** commune.

### Étape 1 (⭐ principal) : le squelette HTML

Objectif : comprendre qu'une page HTML est une structure d'éléments imbriqués, et savoir nommer les balises de base.

1. Créez un dossier `ma-page` sur votre ordinateur, et dedans un fichier vide nommé `index.html`.
2. Ouvrez ce dossier dans VS Code.
3. Tapez le squelette d'une page : `<!DOCTYPE html>`, puis `<html>`, `<head>` et `<body>`. (Astuce : taper `!` puis Entrée dans VS Code génère le squelette.)
4. Ouvrez `index.html` dans votre navigateur (ou clic droit → « Open with Live Server »). Vous voyez une page blanche : c'est normal.
5. Dans le `<body>`, ajoutez un titre avec le nom de votre appli : `<h1>…</h1>`. Rechargez la page.
6. Ajoutez une capture d'écran de votre appli : `<img src="..." alt="capture de mon appli">`.
7. Ajoutez un paragraphe qui explique ce que fait l'appli : `<p>…</p>`.
8. Ajoutez une liste de 3 fonctionnalités (ce qu'on peut faire avec) : un `<ul>` qui contient trois `<li>`.
9. Ajoutez au moins un lien pour essayer l'appli en ligne : `<a href="...">…</a>`.

À la fin : votre page affiche tout son contenu, sans style. C'est volontaire, on l'habille à l'étape suivante.

### Étape 2 (○ facultatif) : un avant-goût de CSS

Objectif : comprendre qu'on sélectionne des éléments HTML et qu'on leur applique des règles de style. On n'en fait qu'un avant-goût : à l'étape Tailwind, on stylera beaucoup plus vite.

1. Créez un fichier `style.css` dans le même dossier.
2. Reliez-le à votre page : dans le `<head>` de `index.html`, ajoutez `<link rel="stylesheet" href="style.css">`.
3. Vérifiez la liaison : dans `style.css`, écrivez `body { background: lightblue; }` et rechargez. Si le fond change, c'est branché.
4. Changez la couleur du fond et celle du texte, choisissez une police lisible (`font-family`).

À la fin : vous avez vu comment marche une feuille de style. À l'étape 3, Tailwind fera la même chose, mais directement dans les attributs `class`.

### Étape 3 (⭐ principal) : styler avec Tailwind et daisyUI

Objectif : styler vite, sans écrire de CSS, en posant des classes « utilitaires » sur vos balises et en utilisant des composants prêts à l'emploi.

1. Dans le `<head>` de `index.html`, ajoutez ces trois lignes (Tailwind, daisyUI, et ses thèmes) :

```html
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
<link href="https://cdn.jsdelivr.net/npm/daisyui@5/daisyui.css" rel="stylesheet" type="text/css" />
<link href="https://cdn.jsdelivr.net/npm/daisyui@5/themes.css" rel="stylesheet" type="text/css" />
```

2. Choisissez un thème daisyUI sur la balise `<html>` : `<html lang="fr" data-theme="nord">` (essayez aussi `bumblebee`, `dracula`… galerie : <https://daisyui.com/docs/themes/>).
3. Posez quelques classes Tailwind sur vos balises : par exemple `class="text-3xl font-bold"` sur le `<h1>`, `class="rounded-xl shadow-lg"` sur le `<img>`, et un conteneur `class="p-6 max-w-2xl mx-auto"` pour centrer et aérer.
4. Utilisez au moins **un composant daisyUI**, par exemple une carte pour présenter votre appli :

```html
<div class="card w-96 bg-base-100 shadow-sm">
  <div class="card-body">
    <h2 class="card-title">Mon appli</h2>
    <p>Ce qu'elle fait, en deux phrases.</p>
  </div>
</div>
```

5. Rechargez : le style s'applique sans aucun fichier CSS.

À la fin : votre page est habillée avec Tailwind et utilise au moins un composant daisyUI.

### Étape 4 (⭐ principal) : mettre votre page en ligne (GitHub Pages)

Objectif : votre page n'existe que sur votre ordinateur. Là, vous lui donnez une **adresse publique** partageable, et vous apprenez à la mettre à jour. Mettre un site « en ligne », c'est le déposer sur un serveur accessible à tous ; GitHub le fait gratuitement avec **GitHub Pages**.

1. Créez un compte GitHub (gratuit) et confirmez l'adresse e-mail. Un seul compte pour le groupe suffit.
2. Cliquez « New repository », nommez-le comme vous voulez (`ma-page` par exemple : lettres, chiffres et tirets, pas d'espaces) et cochez « Public ».
3. Sur la page du dépôt : « Add file » → « Upload files », glissez-déposez vos fichiers (`index.html`, et `style.css` si vous l'avez fait), puis « Commit changes ».
4. Onglet « Settings » → « Pages » : choisissez la branche `main` comme source et cliquez « Save ».
5. Attendez une minute, rechargez « Settings » → « Pages » : GitHub y affiche l'URL publique, de la forme `https://votre-pseudo.github.io/nom-du-repo/`. Ouvrez-la, votre page doit s'afficher.
6. Gardez des chemins **relatifs** dans votre HTML (`style.css`, `script.js`, pas `/style.css`) pour que tout soit trouvé dans le sous-dossier.

À chaque modification suivante, vous ré-uploaderez vos fichiers de la même façon (« Add file » → « Upload files »), et vous rechargerez l'URL pour voir le changement en ligne.

### Étape 5 (⭐ principal) : un formulaire de contact (Tailwind + JS)

Objectif : construire un formulaire, le styler avec daisyUI, lire la saisie en JavaScript, la valider et réagir à l'envoi.

1. Dans `index.html`, ajoutez un `<form>` avec au moins trois champs, stylés avec les classes daisyUI :
    - un champ **nom** (`<input type="text" class="input" id="nom">`),
    - un champ **e-mail** (`<input type="email" class="input" id="email">`),
    - un champ **message** (`<textarea class="textarea" id="message"></textarea>`),
    - un bouton d'envoi (`<button type="submit" class="btn btn-primary">Envoyer</button>`).
2. Mettez un `<label>` devant chaque champ. Prévoyez une zone de retour vide : `<p id="confirmation"></p>`.
3. Créez `script.js` et reliez-le juste avant `</body>` : `<script src="script.js"></script>`.
4. Dans `script.js`, récupérez le formulaire et les champs avec `document.querySelector(...)`.
5. Branchez l'envoi avec `addEventListener("submit", ...)` et appelez `event.preventDefault()` pour empêcher le rechargement de la page.
6. Vérifiez que les champs ne sont pas vides et que l'e-mail contient bien un `@`. Si quelque chose manque, affichez un message d'erreur ; sinon, affichez une confirmation du type « Merci NOM, ton message a bien été pris en compte ».
7. Testez en local, puis ré-uploadez `index.html` et `script.js` sur GitHub et vérifiez sur l'URL publique.

> Note : GitHub Pages héberge un site statique, sans serveur. Pour l'instant, votre formulaire valide la saisie et affiche un retour, mais le message n'est enregistré nulle part. À l'étape 6, vous le rangez pour de vrai dans une base de données.

### Étape 6 (⭐ principal) : enregistrer le formulaire dans Supabase

Objectif : ranger les messages du formulaire dans une vraie base de données, **directement depuis le JavaScript du navigateur**, sans serveur à coder. C'est ce que permet **Supabase** : dès qu'on crée une table, il génère une API appelable depuis le front.

**Créez votre compte et votre projet**

1. Allez sur <https://supabase.com>, créez un compte (gratuit) et confirmez l'e-mail. Un seul projet pour le groupe suffit.
2. Cliquez « New project », donnez-lui un nom, choisissez un mot de passe pour la base et attendez que le projet soit prêt (une à deux minutes).
3. Dans le menu « SQL Editor », collez ce code et cliquez « Run » pour créer la table :

```sql
create table contacts (
  id bigint generated always as identity primary key,
  created_at timestamptz default now(),
  nom text,
  email text,
  message text
);
```

4. Activez la sécurité au niveau des lignes (RLS) et autorisez **l'envoi** par tout le monde. Toujours dans le SQL Editor :

```sql
alter table contacts enable row level security;

create policy "Tout le monde peut envoyer un message"
  on contacts for insert
  to anon
  with check (true);
```

5. Récupérez vos deux identifiants dans « Project Settings » → « API » : l'**URL du projet** (`https://xxxx.supabase.co`) et la **clé anon** (la clé « anon public »).

**Branchez votre formulaire**

6. Donnez un `id` à votre formulaire : `<form id="contact">`.
7. Dans `index.html`, chargez la librairie Supabase, puis votre `script.js` **juste après**. L'ordre compte : `script.js` utilise `window.supabase`, donc la librairie doit être chargée avant. Placez les deux lignes ensemble, juste avant `</body>` :

```html
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="script.js"></script>
```

(Si vous aviez déjà mis `<script src="script.js"></script>` à l'étape 5, déplacez-le ici, après la ligne Supabase, et ne le laissez qu'une seule fois.)

8. Dans `script.js`, créez le client puis enregistrez la saisie à l'envoi. Remplacez votre ancien code par celui-ci (avec vos propres URL et clé) :

```javascript
const URL_SUPABASE = "https://xxxx.supabase.co"; // votre URL de projet
const CLE_ANON = "eyJhbGciOi..."; // votre clé anon (Project Settings → API)
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
```

9. Testez en local : envoyez un message, puis allez voir dans Supabase « Table Editor » → `contacts`. Votre ligne doit y être.
10. Ré-uploadez `index.html` et `script.js` sur GitHub, et vérifiez que ça marche aussi sur l'URL publique.

> La clé anon est **publique**, c'est normal : elle finit dans le code envoyé au navigateur. Ce qui protège les données, ce sont les règles **RLS** (Row Level Security). Ici on autorise seulement l'**insertion** : personne ne peut lire les messages des autres depuis le front. On pourra creuser ce sujet plus tard (lecture des données, règles d'accès plus fines).

### Étape 7 (○ bonus, si le temps)

À piocher dans l'ordre que vous voulez :

1. Soigner les **messages d'erreur** du formulaire : dire précisément quel champ pose problème.
2. Proposer **plusieurs thèmes** daisyUI au choix (un bouton qui change l'attribut `data-theme`).
3. Rendre la page **responsive** (préfixes Tailwind `sm:`, `md:`…).
4. Ajouter une petite icône d'onglet (favicon).
5. Découvrir **Git en ligne de commande** : installez Git et essayez `git clone`, `git add`, `git commit`, `git push` en suivant <https://github.com/Selimmmm/git_step_by_step>.

## Travail sur le Markdown (⭐ principal, transverse)

Créez un fichier `JOURNAL.md`. C'est un fichier texte écrit en **Markdown**, le langage qui sert à écrire de la doc lisible (c'est ce qui formate les messages sur Discord, les README sur GitHub, etc.). Dedans, expliquez avec vos mots :

- ce qu'est le HTML, le CSS, le JS, en une phrase chacun,
- ce que vous avez construit aujourd'hui,
- une difficulté rencontrée et comment vous l'avez réglée.

Utilisez au moins : un titre (`#`), une liste, un mot en **gras**, et un bloc de code (avec des `` ``` ``). C'est votre premier vrai Markdown, on s'en resservira toute la semaine.

## Modalités d'évaluation

Le formateur ouvre l'URL publique de la page depuis son poste en fin de journée, et le groupe fait la démo du formulaire. Dépôt sur SimplonLine de l'URL publique et des fichiers (`index.html`, `script.js`, `JOURNAL.md`, et `style.css` s'il a été fait).

## Livrables

1. L'**URL publique** de la page (`https://votre-pseudo.github.io/nom-du-repo/`), déposée sur SimplonLine.
2. Les fichiers `index.html` et `script.js` (plus `style.css` si vous avez fait l'étape 2).
3. Le fichier `JOURNAL.md` rempli (rendu Markdown explicatif).

## Critères de performance

- La page est accessible publiquement à son URL et affiche une présentation complète (titre, capture, description, lien).
- La page est habillée avec **Tailwind** et utilise au moins un **composant daisyUI**.
- Le formulaire de contact valide les champs et affiche un message de retour clair, sans erreur dans le navigateur.
- Un message envoyé via le formulaire est bien enregistré dans la table Supabase du groupe.
- Le `JOURNAL.md` est lisible et utilise au moins quatre éléments Markdown différents.

## Situation professionnelle

Découverte du développement web front-end.

## Besoin visé ou problème rencontré

Dans une équipe produit, savoir lire et modifier une page web à la main, sans dépendre entièrement d'un générateur ou d'une IA, est une compétence de base. Comprendre la séparation HTML / CSS / JS permet de dialoguer avec des développeurs, de corriger un détail soi-même et de juger ce que produit un outil de génération de code.

## Compétences visées

**C1. Réaliser des interfaces utilisateur statiques web ou web mobile** (visé : niveau 1 et 2)
niveau 1, imiter · niveau 2, adapter · niveau 3, transposer

**C2. Développer la partie dynamique des interfaces utilisateur web ou web mobile** (visé : niveau 1)
niveau 1, imiter · niveau 2, adapter · niveau 3, transposer

**C3. Mettre en place une base de données relationnelle** (visé : niveau 1)
niveau 1, imiter · niveau 2, adapter · niveau 3, transposer
