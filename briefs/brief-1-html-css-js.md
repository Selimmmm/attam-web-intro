# Brief 1 : ma page de présentation (HTML, CSS, puis un peu de JS)

- **Type** : brief individuel
- **Durée visée** : 1 journée (7h)
- **Référentiel** : [2025] Mobiliser les compétences informatiques fondamentales

Aujourd'hui, tu écris le code toi-même, ligne par ligne, pour comprendre comment une page web est construite. À la fin de la journée, tu auras une page qui présente une application, et tu sauras lire et modifier le code d'une page.

## Contexte du projet

Une page web, c'est trois langages qui travaillent ensemble : le **HTML** (le contenu et la structure : « voici un titre, voici une image »), le **CSS** (l'apparence : couleurs, polices, mise en page) et le **JavaScript** (le comportement : ce qui bouge quand on clique). On va les découvrir dans cet ordre, du plus simple au plus vivant.

Le but du jour : construire **ta page de présentation**, une mini-page qui met en valeur l'application que tu as créée avec Google AI Studio (son nom, ce qu'elle fait, une capture, un lien pour l'essayer). C'est la première brique d'un projet qu'on fera grandir toute la semaine : demain on la met en ligne, après-demain on la connecte à une base de données partagée par toute la promo.

> Si tu préfères travailler de ton côté, le sujet est libre : tu peux présenter un projet perso, une asso, un truc qui te tient à cœur, au lieu de l'appli AI Studio. Les étapes restent exactement les mêmes.

## Ressources

- MDN, le manuel de référence du web (en français) : <https://developer.mozilla.org/fr/docs/Learn_web_development>
- Toxicode pour s'entraîner de façon ludique : <https://www.toxicode.fr/learn>
- Un éditeur de code (VS Code) avec l'extension Live Server.
- Tutoriel Git pas à pas : <https://github.com/Selimmmm/git_step_by_step>
- Antisèche Markdown : <https://www.markdownguide.org/cheat-sheet/>

## Modalités pédagogiques

Travail individuel, avec démos collectives du formateur entre chaque étape. On code en direct, on casse, on répare. Chaque étape est découpée en petits pas : fais-les **un par un**, et vérifie le résultat dans le navigateur après chaque pas avant de passer au suivant.

### Étape 1 (⭐ principal) : le squelette HTML

Objectif : comprendre qu'une page HTML est une structure d'éléments imbriqués, et savoir nommer les balises de base.

1. Crée un dossier `ma-page` sur ton ordinateur, et dedans un fichier vide nommé `index.html`.
2. Ouvre ce dossier dans VS Code.
3. Tape le squelette d'une page : `<!DOCTYPE html>`, puis `<html>`, `<head>` et `<body>`. (Astuce : taper `!` puis Entrée dans VS Code génère le squelette.)
4. Ouvre `index.html` dans ton navigateur (ou clic droit → « Open with Live Server »). Tu vois une page blanche : c'est normal.
5. Dans le `<body>`, ajoute un titre avec le nom de ton appli : `<h1>…</h1>`. Recharge la page.
6. Ajoute une capture d'écran de ton appli : `<img src="..." alt="capture de mon appli">`.
7. Ajoute un paragraphe qui explique ce que fait l'appli : `<p>…</p>`.
8. Ajoute une liste de 3 fonctionnalités (ce qu'on peut faire avec) : un `<ul>` qui contient trois `<li>`.
9. Ajoute au moins un lien pour essayer l'appli en ligne : `<a href="...">…</a>`.

À la fin : ta page affiche tout son contenu, sans style. C'est volontaire, on l'habille à l'étape suivante.

### Étape 2 (⭐ principal) : l'habillage CSS

Objectif : comprendre qu'on sélectionne des éléments HTML et qu'on leur applique des règles de style.

1. Crée un fichier `style.css` dans le même dossier.
2. Relie-le à ta page : dans le `<head>` de `index.html`, ajoute `<link rel="stylesheet" href="style.css">`.
3. Vérifie la liaison : dans `style.css`, écris `body { background: lightblue; }` et recharge. Si le fond change, c'est branché.
4. Change la couleur du fond et celle du texte à ton goût.
5. Choisis une police lisible (`font-family`) et une taille de texte agréable.
6. Donne de l'air : ajoute des marges et du `padding` pour que ça respire.
7. Arrondis les coins de la capture avec `border-radius: 12px;` sur le `<img>`.
8. Centre ta page au milieu de la fenêtre.

À la fin : la même page, mais agréable à regarder.

### Étape 3 (⭐ principal) : une première interaction JS

Objectif : comprendre qu'on peut réagir à un clic et modifier la page en direct. Une seule interaction qui marche vaut mieux que trois à moitié faites.

1. Crée un fichier `script.js`. Relie-le juste avant `</body>` : `<script src="script.js"></script>`.
2. Vérifie la liaison : dans `script.js`, écris `console.log("ça marche");`. Ouvre la console du navigateur (F12) et vérifie que le message s'affiche.
3. Ajoute un bouton dans ton HTML : `<button id="bouton">Clique-moi</button>`.
4. Dans le JS, récupère ce bouton : `const bouton = document.querySelector("#bouton");`.
5. Réagis au clic : `bouton.addEventListener("click", () => { ... });`.
6. À l'intérieur, fais une seule chose visible, au choix :
    - passer la page en **mode sombre** (changer `document.body.style.background` et la couleur du texte),
    - afficher une **phrase surprise** (changer le `textContent` d'un paragraphe),
    - **compter les clics** (une variable qui augmente et s'affiche).

À la fin : un clic produit un effet visible sur ta page.

### Étape 4 (⭐ principal) : découverte de Git et GitHub

Objectif : comprendre à quoi servent Git et GitHub, et créer ton compte, pour être prêt à publier ta page demain.

1. Retiens la différence en une phrase :
    - **Git** : un outil qui garde l'historique des versions de ton code (qui a changé quoi, et quand).
    - **GitHub** : le site où on dépose ce code, où on le partage et où on le publie.
2. Crée un compte sur GitHub (gratuit) et confirme ton adresse e-mail.
3. Ouvre le tutoriel pas à pas : <https://github.com/Selimmmm/git_step_by_step>.
4. Parcours-le tranquillement et repère les quatre commandes qui reviennent : `git init`, `git add`, `git commit`, `git push`.
5. Note dans ton `JOURNAL.md`, avec tes mots, à quoi sert chacune de ces commandes.

On ne tape pas encore les commandes aujourd'hui : c'est une première découverte. On s'en sert pour de vrai au brief 2 (la pratique de Git en ligne de commande y est en bonus).

### Étape 5 (○ bonus, si le temps)

À piocher dans l'ordre que tu veux, un seul suffit :

1. Ajouter une **animation CSS** : la capture qui grossit au survol (`:hover` + `transform: scale(...)`).
2. Proposer **plusieurs thèmes** de couleurs au lieu d'un seul mode sombre.
3. Rendre la page **responsive** : jolie aussi sur téléphone.
4. Ajouter une petite icône d'onglet (favicon).
5. Installer Git et **essayer** les commandes du tutoriel sur un dossier de test.

## Travail sur le Markdown (⭐ principal, transverse)

Crée un fichier `JOURNAL.md`. C'est un fichier texte écrit en **Markdown**, le langage qui sert à écrire de la doc lisible (c'est ce qui formate les messages sur Discord, les README sur GitHub, etc.). Dedans, explique avec tes mots :

- ce qu'est le HTML, le CSS, le JS, en une phrase chacun,
- ce que tu as construit aujourd'hui,
- une difficulté rencontrée et comment tu l'as réglée.

Utilise au moins : un titre (`#`), une liste, un mot en **gras**, et un bloc de code (avec des `` ``` ``). C'est ton premier vrai Markdown, on s'en resservira toute la semaine.

## Modalités d'évaluation

Démonstration de la page au formateur en fin de journée, et dépôt des fichiers (`index.html`, `style.css`, `script.js`, `JOURNAL.md`) sur SimplonLine.

## Livrables

1. Les fichiers `index.html`, `style.css`, `script.js` de ta page de présentation.
2. Le fichier `JOURNAL.md` rempli (rendu Markdown explicatif).

## Critères de performance

- La page s'ouvre dans le navigateur et affiche une présentation complète (titre, capture, description, lien).
- Le HTML, le CSS et le JS sont dans **trois fichiers séparés** et reliés correctement.
- Au moins une interaction JS fonctionne (un clic produit un effet visible).
- Le compte GitHub est créé, et l'élève sait dire à quoi servent `git add`, `git commit` et `git push`.
- Le `JOURNAL.md` est lisible et utilise au moins quatre éléments Markdown différents.

## Situation professionnelle

Découverte du développement web front-end.

## Besoin visé ou problème rencontré

Dans une équipe produit, savoir lire et modifier une page web à la main, sans dépendre entièrement d'un générateur ou d'une IA, est une compétence de base. Comprendre la séparation HTML / CSS / JS permet de dialoguer avec des développeurs, de corriger un détail soi-même et de juger ce que produit un outil de génération de code.

## Compétences visées

**C1. Planifier le travail à effectuer individuellement**
niveau 1, imiter · niveau 2, adapter · niveau 3, transposer

**C3. Définir le périmètre d'un problème rencontré en adoptant une démarche inductive**
niveau 1, imiter · niveau 2, adapter · niveau 3, transposer

**C4. Rechercher de façon méthodique une ou des solutions au problème rencontré**
niveau 1, imiter · niveau 2, adapter · niveau 3, transposer
