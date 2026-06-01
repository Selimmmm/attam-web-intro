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

## Exercice 3 : une image qui se retourne au clic

Objectif : afficher une image et un bouton. Quand on clique sur le bouton, l'image se retourne comme dans un miroir. Une petite ligne de JavaScript entre en jeu : au clic, on ajoute ou on retire une classe CSS, et c'est cette classe qui retourne l'image.

Le modèle, déjà fonctionnel. Clique sur Exécuter, puis sur le bouton.

```htmlrun-frozen
<style>
  .miroir { transform: scaleX(-1); }
  img { width: 200px; border-radius: 12px; display: block; margin-bottom: 10px; }
</style>

<img id="photo" src="https://picsum.photos/seed/atelier/300/200" alt="photo">
<button onclick="document.getElementById('photo').classList.toggle('miroir')">
  Retourner l'image
</button>
```

À toi. Le bouton et l'image sont en place, mais l'action au clic manque. Complète l'attribut `onclick` du bouton pour ajouter et retirer la classe `miroir`, comme dans le modèle.

```htmlrun
<style>
  .miroir { transform: scaleX(-1); }
  img { width: 200px; border-radius: 12px; display: block; margin-bottom: 10px; }
</style>

<img id="photo" src="https://picsum.photos/seed/atelier/300/200" alt="photo">
<button onclick="">
  Retourner l'image
</button>
```

Quand le clic retourne bien l'image, tu tiens le principe que tu retrouveras dans ton projet : un clic déclenche un changement visible sur la page. Tu es prêt pour le brief 1.
