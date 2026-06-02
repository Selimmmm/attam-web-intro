const questions = [
  {
    question: "Quel mot-clé déclare une variable dont la valeur ne changera plus ?",
    reponses: ["let", "const", "var", "fix"],
    correcte: 1,
    temps: 20,
  },
  {
    question: "Quel mot-clé déclare une variable dont la valeur pourra changer ?",
    reponses: ["const", "final", "let", "lock"],
    correcte: 2,
    temps: 20,
  },
  {
    question: "Que fait console.log(\"Bonjour\") ?",
    reponses: [
      "Crée une page web",
      "Supprime une variable",
      "Enregistre un fichier",
      "Affiche Bonjour dans la console",
    ],
    correcte: 3,
    temps: 20,
  },
  {
    question: "Quel est le résultat de 2 + 2 en JavaScript ?",
    reponses: ["\"22\"", "4", "22", "Erreur"],
    correcte: 1,
    temps: 20,
  },
  {
    question: "Comment écrit-on une chaîne de caractères en JavaScript ?",
    reponses: ["#Bonjour", "0", "\"Bonjour\"", "Bonjour"],
    correcte: 2,
    temps: 20,
  },
  {
    question: "Laquelle de ces valeurs est un booléen ?",
    reponses: ["\"oui\"", "1.5", "true", "[ ]"],
    correcte: 2,
    temps: 20,
  },
  {
    question: "Que teste la condition if (age >= 18) ?",
    reponses: [
      "Si age est une lettre",
      "Si age est supérieur ou égal à 18",
      "Si age vaut exactement 18",
      "Si age est vide",
    ],
    correcte: 1,
    temps: 20,
  },
  {
    question: "À quoi sert une boucle for ?",
    reponses: [
      "Changer la couleur",
      "Créer un bouton",
      "Répéter une action plusieurs fois",
      "Afficher une image",
    ],
    correcte: 2,
    temps: 20,
  },
  {
    question: "En JavaScript, que désigne le DOM ?",
    reponses: [
      "Un type de fichier image",
      "La représentation de la page web que le code peut modifier",
      "Un langage de base de données",
      "Un navigateur web",
    ],
    correcte: 1,
    temps: 30,
  },
  {
    question: "Quelle ligne récupère l'élément HTML ayant l'id \"titre\" ?",
    reponses: [
      "print(\"titre\")",
      "getfile(\"titre\")",
      "document.getElementById(\"titre\")",
      "document.color(\"titre\")",
    ],
    correcte: 2,
    temps: 30,
  },
];

const elProgression = document.querySelector("#progression");
const elMinuteur = document.querySelector("#minuteur");
const elQuestion = document.querySelector("#question");
const elReponses = document.querySelector("#reponses");
const btnSuivant = document.querySelector("#suivant");
const blocFin = document.querySelector("#fin");
const elScoreFinal = document.querySelector("#score-final");
const btnRecommencer = document.querySelector("#recommencer");
const entete = document.querySelector(".entete");

let index = 0;
let score = 0;
let minuteur = null;
let repondu = false;

function afficherQuestion() {
  repondu = false;
  const q = questions[index];
  elProgression.textContent = "Question " + (index + 1) + " / " + questions.length;
  elQuestion.textContent = q.question;
  btnSuivant.hidden = true;
  elReponses.innerHTML = "";

  q.reponses.forEach((texte, i) => {
    const bouton = document.createElement("button");
    bouton.className = "reponse";
    bouton.textContent = texte;
    bouton.addEventListener("click", () => choisir(i));
    elReponses.appendChild(bouton);
  });

  lancerMinuteur(q.temps);
}

function lancerMinuteur(secondes) {
  let restant = secondes;
  elMinuteur.textContent = restant;
  minuteur = setInterval(() => {
    restant = restant - 1;
    elMinuteur.textContent = restant;
    if (restant <= 0) {
      clearInterval(minuteur);
      reveler(-1);
    }
  }, 1000);
}

function choisir(i) {
  if (repondu) return;
  reveler(i);
}

function reveler(choix) {
  repondu = true;
  clearInterval(minuteur);
  const q = questions[index];
  const boutons = elReponses.querySelectorAll(".reponse");

  boutons.forEach((bouton, i) => {
    bouton.disabled = true;
    if (i === q.correcte) {
      bouton.classList.add("correcte");
    } else if (i === choix) {
      bouton.classList.add("fausse");
    }
  });

  if (choix === q.correcte) {
    score = score + 1;
  }

  btnSuivant.hidden = false;
  btnSuivant.textContent =
    index === questions.length - 1 ? "Voir mon score" : "Question suivante";
}

btnSuivant.addEventListener("click", () => {
  index = index + 1;
  if (index < questions.length) {
    afficherQuestion();
  } else {
    terminer();
  }
});

function terminer() {
  entete.hidden = true;
  elQuestion.hidden = true;
  elReponses.hidden = true;
  btnSuivant.hidden = true;
  blocFin.hidden = false;
  elScoreFinal.textContent =
    "Tu as " + score + " bonne(s) réponse(s) sur " + questions.length + ".";
}

btnRecommencer.addEventListener("click", () => {
  index = 0;
  score = 0;
  entete.hidden = false;
  elQuestion.hidden = false;
  elReponses.hidden = false;
  blocFin.hidden = true;
  afficherQuestion();
});

afficherQuestion();
