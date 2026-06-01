# Atelier : reproduire en HTML et CSS

Avant de te lancer dans ton projet, fais ces trois petits exercices pour prendre tes marques. Le principe est toujours le même : modifie le code, clique sur **▶ Exécuter**, et regarde ce qui change. Le bouton ↺ remet le code de départ si tu veux recommencer.

Tu n'as rien à installer, tout se passe dans la page. Il n'y a pas de note ni de bonne réponse unique : l'important est d'essayer des valeurs et de voir leur effet.

## Exercice 1 : une boîte à ton goût

Objectif : composer ta propre boîte et découvrir quatre propriétés CSS très courantes : `background` (la couleur de fond), `padding` (l'espace intérieur), `border-radius` (les coins arrondis) et `font-family` (la police).

Modifie l'exemple ci-dessous, clique sur Exécuter, et fais tes propres choix :

- **La couleur de fond** (`background`) : un code couleur comme `#ffe8d6`, ou un nom de couleur en anglais comme `lavender`, `lightyellow`, `mistyrose`.
- **Les coins** : arrondis avec `border-radius: 16px`, ou bien droits si tu enlèves cette ligne. À toi de voir ce que tu préfères.
- **La police** (`font-family`) : par exemple `font-family: Georgia, serif;` pour un style classique, ou `font-family: 'Trebuchet MS', sans-serif;` pour un style plus moderne.
- Garde un peu de `padding` pour que le texte ne colle pas aux bords.

```htmlrun
<div style="background: lightyellow; padding: 20px; border-radius: 16px; font-family: Georgia, serif; max-width: 320px;">
  <h3 style="margin-top: 0;">Mon titre</h3>
  <p>Change la couleur, les coins et la police, puis observe le résultat.</p>
</div>
```

Il n'y a pas de bonne réponse unique : le but est de voir comment chaque valeur change l'apparence.

## Exercice 2 : une image dans un cadre

Objectif : afficher une image à une taille fixe et comprendre `object-fit`, la propriété qui décide comment l'image remplit son cadre.

Modifie l'exemple, clique sur Exécuter, et fais des essais :

- **Change la largeur et la hauteur** (`width`, `height`) : essaie un grand carré (`240px`), un petit (`100px`), ou un rectangle (`width: 240px; height: 120px`).
- **Change la valeur de `object-fit`** pour voir la différence :
    - `cover` : l'image remplit le cadre et déborde proprement (elle est recadrée),
    - `contain` : l'image entière entre dans le cadre, avec des espaces vides éventuels,
    - `fill` : l'image est étirée pour remplir, quitte à se déformer.
- La bordure (`border`) et les coins arrondis (`border-radius`) sont là pour faire joli, modifie-les aussi si tu veux.

```htmlrun
<img
  src="https://picsum.photos/seed/atelier/500/350"
  alt="photo d'exemple"
  style="width: 160px; height: 160px; object-fit: cover; border: 3px solid #3b82f6; border-radius: 12px;">
```

C'est sur un cadre rectangulaire que la différence entre `cover`, `contain` et `fill` se voit le mieux. Essaie les trois.

## Exercice 3 : ton propre effet au clic

Objectif : comprendre comment un clic modifie la page. Le code ci-dessous fonctionne déjà : à chaque clic, le bouton ajoute ou retire la classe `miroir` sur l'image, et cette classe la retourne comme un miroir. Clique sur Exécuter, puis sur le bouton pour le voir.

À toi maintenant d'inventer ton propre effet :

1. Sous la ligne `.miroir { ... }`, écris une **nouvelle classe** avec l'effet de ton choix. Quelques idées :
    - agrandir : `transform: scale(1.3);`
    - faire pivoter : `transform: rotate(15deg);`
    - passer en noir et blanc : `filter: grayscale(100%);`
    - rendre l'image ronde : `border-radius: 50%;`
2. Dans le bouton, remplace `toggle('miroir')` par le nom de ta nouvelle classe (par exemple `toggle('grossir')` si tu l'as appelée `.grossir`).
3. Clique sur Exécuter, puis sur le bouton : ton effet doit s'appliquer et se retirer à chaque clic.

```htmlrun
<style>
  .miroir { transform: scaleX(-1); }

  /* Écris ta nouvelle classe ici, par exemple :
  .grossir { transform: scale(1.3); } */

  img { width: 200px; border-radius: 12px; display: block; margin-bottom: 10px; }
</style>

<img id="photo" src="https://picsum.photos/seed/atelier/300/200" alt="photo">
<button onclick="document.getElementById('photo').classList.toggle('miroir')">
  Appliquer l'effet
</button>
```

Tu tiens là le principe que tu retrouveras dans ton projet : un clic déclenche un changement visible sur la page.

## Pour aller plus loin

Ces deux derniers exercices ne sont pas obligatoires. Fais-les si tu as le temps et l'envie : ils introduisent deux outils que tu réutiliseras souvent.

## Exercice 4 : un effet au survol

Objectif : déclencher un effet quand la souris passe sur un élément, sans aucun clic ni JavaScript. Cela se fait avec `:hover` en CSS, et `transition` rend le changement progressif.

Modifie l'exemple et passe la souris sur la carte :

- Change ce qui se passe au survol, dans le bloc `.carte:hover { ... }` : une autre couleur de fond (`background`), une légère rotation (`transform: rotate(3deg)`), une ombre…
- Modifie la durée de la transition (`.2s`, `.5s`) pour voir l'effet ralentir ou s'accélérer.

```htmlrun
<style>
  .carte {
    background: lavender;
    padding: 20px;
    border-radius: 12px;
    max-width: 280px;
    transition: transform .2s;
  }
  .carte:hover { transform: scale(1.05); }
</style>

<div class="carte">
  <h3 style="margin-top: 0;">Passe la souris sur moi</h3>
  <p>Je réagis au survol, et tu peux changer ma réaction.</p>
</div>
```

## Exercice 5 : deux éléments côte à côte

Objectif : placer une image et un texte l'un à côté de l'autre, au lieu de l'un sous l'autre. C'est le rôle de `display: flex`, l'outil de base pour la mise en page.

Modifie l'exemple et observe :

- Enlève `display: flex` (ou mets `block`) : l'image et le texte repassent l'un sous l'autre. C'est la preuve de ce que fait `flex`.
- Change l'espace entre les deux avec `gap` (`8px`, `30px`).
- Change l'alignement vertical avec `align-items` (`flex-start`, `center`, `flex-end`).

```htmlrun
<style>
  .ligne { display: flex; gap: 16px; align-items: center; max-width: 440px; }
  .ligne img { width: 100px; height: 100px; object-fit: cover; border-radius: 50%; }
</style>

<div class="ligne">
  <img src="https://picsum.photos/seed/atelier/200/200" alt="photo">
  <p>Grâce à flex, cette image et ce texte se placent côte à côte. Essaie de changer les valeurs.</p>
</div>
```

Avec ces bases (couleurs, cadres, effets au clic et au survol, mise en page), tu es prêt pour le brief 1.
