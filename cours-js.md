# Cours : JavaScript et le DOM

Cette page est interactive. Chaque bloc de code a un bouton **▶ Exécuter** : le code s'exécute directement dans la page et le résultat s'affiche dessous. La plupart des blocs sont **modifiables** (change le code, puis relance), certains sont en lecture seule. Le bouton ↺ remet le code d'origine.

- Lis l'explication, exécute le bloc, puis modifie-le pour vérifier que tu as compris.
- Le contenu va du plus simple au plus utile : rappel HTML, variables, types, hasard, conditions, listes, objets, requêtes `fetch`, et enfin la modification de la page (le DOM).

## D'abord, un rappel HTML

Une page web est faite de **balises**. Une balise ouvre (`<p>`) et ferme (`</p>`), et ce qu'il y a entre les deux est le contenu. Quelques balises de base :

- `<h1>` à `<h3>` : des titres, du plus gros au plus petit.
- `<p>` : un paragraphe.
- `<ul>` et `<li>` : une liste à puces.
- `<button>` : un bouton.
- `<a href="...">` : un lien.

Chaque balise peut avoir un **identifiant** avec `id="..."`, qui servira plus tard à la retrouver depuis le JavaScript. Voici du HTML, et juste en dessous ce que ça affiche (clique sur Exécuter) :

```domrun-frozen
<h2 id="titre">Ma première page</h2>
<p>Ceci est un paragraphe.</p>
<ul>
  <li>Premier élément</li>
  <li>Deuxième élément</li>
</ul>
<button>Un bouton</button>
===
console.log("Le HTML ci-dessus est affiché dans le cadre blanc.");
```

Le **CSS** sert à habiller ce HTML : couleurs, formes, animations. Clique sur ▶ Exécuter pour afficher la carte, puis passe la souris dessus :

```domrun-frozen
<style>
  .carte {
    padding: 18px 26px;
    border-radius: 14px;
    color: white;
    font-weight: bold;
    font-size: 18px;
    background: linear-gradient(135deg, #6a11cb, #2575fc);
    display: inline-block;
    transition: transform .2s;
    cursor: pointer;
  }
  .carte:hover { transform: scale(1.12) rotate(-2deg); }
</style>
<div class="carte">Passe la souris sur moi</div>
===
console.log("Tout l'effet vient du CSS, sans une ligne de JavaScript.");
```

Retiens ça : le HTML décrit **quoi** afficher, le CSS décide **à quoi ça ressemble**, et le JavaScript, qu'on voit maintenant, sert à **calculer** et à **modifier** ce qui est affiché.

## Les variables

Une variable est une boîte étiquetée où on range une valeur pour la réutiliser. On la crée avec `let` (valeur qui peut changer) ou `const` (valeur fixe). `console.log(...)` affiche une valeur pour vérifier ce qu'on fait.

```jsrun
let pseudo = "Ada";
const niveau = 1;

console.log(pseudo);
console.log("Niveau", niveau);

pseudo = "Ada_la_boss";
console.log("Nouveau pseudo :", pseudo);
```

À toi : change les valeurs, ajoute une variable `score` et affiche-la.

## Les types simples

Une valeur a un **type**. Les trois types de base :

- le texte (`string`), entre guillemets : `"bonjour"`,
- les nombres (`number`) : `42`, `3.14`,
- les booléens (`boolean`) : `true` ou `false`.

`typeof` donne le type d'une valeur. Attention : `+` additionne des nombres mais **colle** des textes.

```jsrun
let texte = "bonjour";
let nombre = 42;
let estMajeur = true;

console.log(typeof texte, typeof nombre, typeof estMajeur);

console.log(nombre + 8);
console.log(texte + " tout le monde");
```

Essaie `"5" + 3` puis `5 + 3` et observe la différence. C'est un piège classique.

## Un peu de hasard et de maths

`Math.random()` donne un nombre au hasard entre 0 et 1. Combiné à `Math.floor()` (qui arrondit vers le bas), on tire un nombre entier au hasard. C'est la base de tous les jeux.

```jsrun
console.log("Un hasard entre 0 et 1 :", Math.random());

let de = Math.floor(Math.random() * 6) + 1;
console.log("Tu as lancé un", de);

console.log("Arrondi de 4.7 :", Math.round(4.7));
console.log("Le plus grand de 3 et 9 :", Math.max(3, 9));
```

Relance plusieurs fois : le dé change à chaque exécution.

## Prendre des décisions : les conditions

`if ... else` exécute un bloc ou un autre selon qu'une condition est vraie ou fausse. On compare avec `>`, `<`, `>=`, `===` (égal).

```jsrun
let age = 20;

if (age >= 18) {
  console.log("Tu es majeur");
} else {
  console.log("Tu es mineur");
}

let piece = Math.random() < 0.5 ? "pile" : "face";
console.log("La pièce tombe sur :", piece);
```

Change `age` à 15 et relance. Le `< 0.5 ? ... : ...` est un raccourci pour un `if/else` court.

## Les listes (tableaux)

Un **tableau** range plusieurs valeurs dans l'ordre, entre crochets. On accède à un élément par sa position (qui commence à 0), on en ajoute avec `push`, et on parcourt avec `forEach`.

```jsrun
let courses = ["pain", "lait", "œufs"];

console.log("J'ai", courses.length, "articles");
console.log("Le premier :", courses[0]);

courses.push("café");
console.log("Après ajout :", courses);

courses.forEach(article => {
  console.log("- " + article);
});
```

## Les dictionnaires (objets)

Quand on veut regrouper plusieurs informations qui vont ensemble (un pseudo, un score, un niveau), on utilise un **objet** : une liste de paires `clé: valeur`. C'est ce qu'on appelle souvent un dictionnaire.

On accède à une valeur avec un point (`joueur.pseudo`) ou des crochets (`joueur["pseudo"]`).

```jsrun
const joueur = {
  pseudo: "Ada",
  score: 1200,
  niveau: 7
};

console.log(joueur.pseudo);
console.log(joueur["score"]);

joueur.score = joueur.score + 100;
console.log(joueur);
```

On peut aussi avoir une **liste d'objets**, et la parcourir :

```jsrun
const equipe = [
  { nom: "Ada", role: "dev" },
  { nom: "Alan", role: "maths" },
  { nom: "Grace", role: "compilateur" }
];

equipe.forEach(membre => {
  console.log(membre.nom + " s'occupe de " + membre.role);
});
```

Retiens bien les objets : c'est exactement la forme sous laquelle les données arrivent quand on interroge une API, juste après.

## Aller chercher des données : `fetch`

Une **API** est un service en ligne qui répond à une question en renvoyant des données, en général sous forme d'objet (comme ceux du dessus). `fetch` envoie la requête. La réponse arrive plus tard : on enchaîne donc avec `.then(...)`, qui veut dire « quand la réponse est là, fais ceci ».

Première API, pour se mettre en jambes : une blague au hasard. Elle renvoie un objet `{ setup, punchline }`.

```jsrun
fetch("https://official-joke-api.appspot.com/random_joke")
  .then(reponse => reponse.json())
  .then(blague => {
    console.log(blague.setup);
    console.log("👉 " + blague.punchline);
  })
  .catch(erreur => console.log("Erreur :", erreur.message));
```

Relance pour une autre blague. Deux étapes à comprendre : `.json()` transforme la réponse en objet JavaScript, puis le `.then` suivant reçoit cet objet et on lit ses clés comme tout à l'heure.

Une deuxième API devine un âge moyen à partir d'un prénom. Change `ada` par le tien :

```jsrun
fetch("https://api.agify.io?name=ada")
  .then(reponse => reponse.json())
  .then(donnees => {
    console.log("Prénom :", donnees.name);
    console.log("Âge estimé :", donnees.age);
  });
```

Et une troisième, qui renvoie des infos sur un pays (la réponse est une liste, on prend le premier élément avec `[0]`) :

```jsrun
fetch("https://restcountries.com/v3.1/name/japan?fields=capital,population")
  .then(reponse => reponse.json())
  .then(donnees => {
    const pays = donnees[0];
    console.log("Capitale :", pays.capital[0]);
    console.log("Population :", pays.population);
  });
```

## Manipuler le DOM

Le **DOM**, c'est la page HTML vue comme des objets que le JavaScript peut lire et modifier. On retrouve un élément avec `document.querySelector("#identifiant")`, puis on change son contenu (`.textContent`) ou son style (`.style`).

Dans les blocs qui suivent, le HTML de départ est affiché, et le JavaScript en dessous le modifie. Clique sur Exécuter pour voir le changement dans le cadre blanc.

### Changer un texte et une couleur

```domrun
<h2 id="titre">Bonjour</h2>
===
const titre = document.querySelector("#titre");
titre.textContent = "Bonjour la promo !";
titre.style.color = "purple";
```

### Réagir à un clic

`addEventListener("click", ...)` exécute du code à chaque clic. Ici on compte les clics.

```domrun
<button id="bouton">Clique-moi</button>
<p id="message">Aucun clic pour l'instant.</p>
===
const bouton = document.querySelector("#bouton");
const message = document.querySelector("#message");
let compteur = 0;

bouton.addEventListener("click", () => {
  compteur = compteur + 1;
  message.textContent = "Nombre de clics : " + compteur;
});
```

### Changer la couleur de fond au hasard

On réutilise le hasard : à chaque clic, on pioche une couleur dans une liste.

```domrun
<button id="changer">Change la couleur</button>
===
const couleurs = ["#ffadad", "#ffd6a5", "#fdffb6", "#caffbf", "#9bf6ff", "#bdb2ff"];

document.querySelector("#changer").addEventListener("click", () => {
  const c = couleurs[Math.floor(Math.random() * couleurs.length)];
  document.body.style.background = c;
});
```

### La boule magique (Magic 8-ball)

Pose une question dans ta tête, clique, et reçois une réponse au hasard. Tout est là : une liste, le hasard, un clic, et la modification du texte.

```domrun
<button id="poser">Pose une question, puis clique</button>
<p id="reponse" style="font-size:22px">🎱</p>
===
const reponses = ["Oui, clairement", "Non", "Peut-être…", "Certainement", "Ça m'étonnerait", "Demande plus tard"];

document.querySelector("#poser").addEventListener("click", () => {
  const i = Math.floor(Math.random() * reponses.length);
  document.querySelector("#reponse").textContent = reponses[i];
});
```

### Lancer un dé

```domrun
<button id="lancer">Lancer le dé</button>
<p id="de" style="font-size:60px">🎲</p>
===
const faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"];

document.querySelector("#lancer").addEventListener("click", () => {
  const n = Math.floor(Math.random() * 6);
  document.querySelector("#de").textContent = faces[n];
});
```

### Compter les caractères en direct

L'événement `input` se déclenche à chaque touche tapée. Pratique pour réagir pendant que l'utilisateur écrit.

```domrun
<input id="champ" placeholder="Écris quelque chose…" style="padding:6px;width:240px">
<p id="compte">0 caractère</p>
===
const champ = document.querySelector("#champ");
const compte = document.querySelector("#compte");

champ.addEventListener("input", () => {
  compte.textContent = champ.value.length + " caractères";
});
```

### Construire une liste à partir d'un tableau

On combine tout : une liste de données, une boucle, et la création d'éléments HTML avec `createElement` et `appendChild`.

```domrun
<ul id="liste"></ul>
===
const fruits = ["pomme", "banane", "cerise"];
const liste = document.querySelector("#liste");

fruits.forEach(fruit => {
  const li = document.createElement("li");
  li.textContent = fruit;
  liste.appendChild(li);
});
```

### Générateur de pseudo

```domrun
<button id="go">Génère mon pseudo</button>
<p id="pseudo" style="font-size:20px;font-weight:bold"></p>
===
const adjectifs = ["Super", "Méga", "Ninja", "Cosmic", "Turbo", "Mystic"];
const animaux = ["Panda", "Tigre", "Renard", "Faucon", "Loutre", "Dragon"];

document.querySelector("#go").addEventListener("click", () => {
  const a = adjectifs[Math.floor(Math.random() * adjectifs.length)];
  const b = animaux[Math.floor(Math.random() * animaux.length)];
  const n = Math.floor(Math.random() * 100);
  document.querySelector("#pseudo").textContent = a + b + n;
});
```

### Le clic qui va chercher une image

On combine `fetch` et le DOM : au clic, on demande une photo de chien au hasard et on l'affiche dans la page.

```domrun
<button id="chien">Montre-moi un chien 🐶</button><br>
<img id="photo" alt="" style="max-width:220px;margin-top:10px;border-radius:10px">
===
document.querySelector("#chien").addEventListener("click", () => {
  fetch("https://dog.ceo/api/breeds/image/random")
    .then(reponse => reponse.json())
    .then(donnees => {
      document.querySelector("#photo").src = donnees.message;
    });
});
```

### Un mini-Pokédex

Le grand final : on tape un nom de Pokémon, on interroge l'API, et on affiche son image et ses stats. C'est exactement le mécanisme qu'on utilisera avec Supabase au brief 3.

Important : l'API ne connaît que les noms **en anglais** (ou le numéro du Pokémon). Donc `charizard` fonctionne, mais `dracaufeu` non.

```domrun
<input id="nom" value="pikachu" placeholder="nom en anglais ou numéro" style="padding:6px">
<button id="chercher">Chercher</button>
<p style="font-size:13px;color:#666;margin:6px 0">Exemples : bulbasaur, charizard, eevee, mewtwo, ou un numéro de 1 à 1000.</p>
<div id="resultat" style="margin-top:10px;display:flex;align-items:center;gap:12px"></div>
===
document.querySelector("#chercher").addEventListener("click", () => {
  const nom = document.querySelector("#nom").value.toLowerCase().trim();
  const res = document.querySelector("#resultat");
  res.textContent = "Recherche…";

  fetch("https://pokeapi.co/api/v2/pokemon/" + nom)
    .then(reponse => {
      if (!reponse.ok) throw new Error("introuvable");
      return reponse.json();
    })
    .then(p => {
      res.innerHTML =
        "<img src='" + p.sprites.front_default + "' alt='' width='72' height='72'>" +
        "<span><strong>" + p.name + "</strong><br>" +
        "Type : " + p.types[0].type.name + "<br>" +
        "Taille : " + p.height + " · Poids : " + p.weight + "</span>";
    })
    .catch(() => {
      res.textContent = "Pas trouvé. Essaie un nom en anglais (bulbasaur, charizard…) ou un numéro.";
    });
});
```

## À toi de jouer

Tu as toutes les briques. Essaie ces petits défis en modifiant les exemples ci-dessus :

1. Dans la **boule magique**, ajoute trois nouvelles réponses.
2. Fais que le **dé** affiche aussi dans la console le numéro tiré.
3. Dans le **générateur de pseudo**, ajoute tes propres adjectifs et animaux.
4. Dans le **mini-Pokédex**, affiche aussi le premier type du Pokémon (indice : `p.types[0].type.name`).

Quand tu es à l'aise avec tout ça, passe aux briefs : tu vas réutiliser exactement ces mécanismes pour construire ta carte web, puis le mur partagé de la promo.
