// const : une valeur fixe
const ville = "Paris";
document.getElementById("r-const").textContent = ville;

// let : une valeur qui change
let score = 0;
score = score + 10;
document.getElementById("r-let").textContent = score;

// console.log : visible dans la console (F12)
console.log("Bonjour");

// les nombres
document.getElementById("r-addition").textContent = 2 + 2;

// les chaînes : le + colle les textes
document.getElementById("r-concat").textContent = "2" + "2";

// les booléens
const majeur = true;
document.getElementById("r-bool").textContent = majeur;

// la condition if
const age = 20;
if (age >= 18) {
  document.getElementById("r-if").textContent = "age vaut " + age + " : tu es majeur.";
} else {
  document.getElementById("r-if").textContent = "age vaut " + age + " : tu es mineur.";
}

// la boucle for
let suite = "";
for (let i = 1; i <= 5; i++) {
  suite = suite + i + " ";
}
document.getElementById("r-for").textContent = suite;

// le DOM : modifier la page au clic
const titre = document.getElementById("titre-demo");
const bouton = document.getElementById("bouton-demo");
bouton.addEventListener("click", () => {
  titre.textContent = "Texte modifié par le code !";
  titre.style.color = "#4f46e5";
});
