# Atelier : reproduire en HTML et CSS

Avant de te lancer dans ton projet, entraîne-toi sur trois petits modèles. Pour chacun, la méthode est la même : observe le résultat, lis le code, puis reproduis-le dans l'éditeur du dessous.

Tu n'as rien à installer, tout se passe dans la page. Clique sur **▶ Exécuter** pour afficher le rendu de ton code, et sur ↺ pour repartir de zéro. Prends ton temps, et n'hésite pas à modifier une valeur pour voir ce qu'elle change.

## Exercice 1 : une boîte

Objectif : afficher une boîte colorée qui contient un titre et une phrase. Tu vas utiliser trois propriétés CSS très courantes : `background` (la couleur de fond), `padding` (l'espace intérieur) et `border-radius` (les coins arrondis).

Voici le modèle à obtenir. Clique sur Exécuter pour l'afficher, puis lis le code attentivement.

```htmlrun-frozen
<div style="background: #eaf1ff; padding: 20px; border-radius: 12px; max-width: 320px;">
  <h3 style="margin-top: 0;">Bonjour</h3>
  <p>Je suis une boîte toute simple : un fond, de l'espace autour du texte, des coins arrondis.</p>
</div>
```

À toi de jouer. Le squelette est déjà en place, remplace les `____` par des valeurs, puis clique sur Exécuter.

```htmlrun
<div style="background: ____; padding: ____; border-radius: ____;">
  <h3>Bonjour</h3>
  <p>À moi de remplir les trois valeurs pour retrouver le modèle.</p>
</div>
```

Quand ta boîte ressemble au modèle, l'exercice est réussi.

## Exercice 2 : une image cadrée

Objectif : afficher une image dans un cadre carré, avec une bordure et des coins arrondis. La propriété importante est `object-fit: cover` : elle **recadre** l'image pour qu'elle remplisse le cadre sans se déformer.

Le modèle :

```htmlrun-frozen
<img
  src="https://picsum.photos/seed/atelier/500/350"
  alt="photo d'exemple"
  style="width: 160px; height: 160px; object-fit: cover; border: 3px solid #3b82f6; border-radius: 12px;">
```

À toi. L'image de départ est déjà là, ajoute les styles entre les guillemets de `style`.

```htmlrun
<img
  src="https://picsum.photos/seed/atelier/500/350"
  alt="photo d'exemple"
  style="">
```

Astuce : une fois que ça marche, enlève `object-fit: cover` et regarde. L'image se déforme, et tu comprends à quoi sert cette propriété.

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
