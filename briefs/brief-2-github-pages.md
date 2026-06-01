# Brief 2 : en ligne ! (GitHub Pages + une feature JS)

- **Type** : brief individuel
- **Durée visée** : 1 journée (7h)
- **Référentiel** : [2025] Mobiliser les compétences informatiques fondamentales
- **Pré-requis** : avoir fini le cœur du [brief 1](#brief-1).

Ta page n'existe que sur ton ordinateur. Aujourd'hui, tu vas la publier sur internet : à la fin de la journée, elle aura une **adresse publique** que tu pourras partager. Tu lui ajouteras aussi une fonctionnalité en JavaScript.

## Contexte du projet

Mettre un site « en ligne », c'est le déposer sur un serveur accessible à tous. GitHub propose ça gratuitement avec **GitHub Pages** : tu déposes tes fichiers sur GitHub (une plateforme où les développeurs stockent et partagent leur code), et GitHub publie automatiquement ta page sur une URL publique.

Au passage, tu découvres **GitHub**, l'outil que tu retrouveras dans absolument toutes les entreprises tech. On reste sur l'essentiel : déposer des fichiers, les mettre à jour, publier.

## Ressources

- GitHub Pages, démarrage : <https://pages.github.com/>
- Doc GitHub (upload de fichiers via le navigateur) : <https://docs.github.com/fr/repositories>
- Tutoriel Git pas à pas (pour l'étape bonus) : <https://github.com/Selimmmm/git_step_by_step>
- Antisèche Markdown : <https://www.markdownguide.org/cheat-sheet/>
- Galerie d'idées de features JS : <https://developer.mozilla.org/fr/docs/Learn_web_development/Core/Scripting>

## Modalités pédagogiques

Travail individuel. Le formateur fait la première mise en ligne en démo, puis chacun refait avec ses fichiers. Avance pas à pas et vérifie chaque résultat avant de continuer.

### Étape 1 (⭐ principal) : créer son dépôt et publier

Objectif : comprendre la différence entre « le fichier sur mon ordi » et « le site publié », et savoir mettre à jour le site.

1. Crée un compte GitHub (si tu n'en as pas) et confirme ton adresse e-mail.
2. Clique sur « New repository » pour créer un nouveau dépôt.
3. Nomme-le **exactement** `ton-pseudo.github.io` (remplace `ton-pseudo` par ton pseudo GitHub) et coche « Public ».
4. Sur la page du dépôt, clique « Add file » → « Upload files ».
5. Glisse-dépose tes fichiers du brief 1 (`index.html`, `style.css`, `script.js`) puis clique « Commit changes ».
6. Va dans l'onglet « Settings » → « Pages » et vérifie que la source est bien la branche `main`.
7. Attends une minute, puis ouvre `https://ton-pseudo.github.io`. Ta page doit s'afficher.
8. Teste une mise à jour : modifie une couleur dans `style.css` sur ton ordi, ré-uploade le fichier, et recharge l'URL pour voir le changement.

### Étape 2 (⭐ principal) : un vrai README en Markdown

Objectif : voir le Markdown servir « pour de vrai » et comprendre le rôle d'un README.

1. Sur le dépôt, clique « Add file » → « Create new file » et nomme-le `README.md`.
2. Écris un titre (`#`) avec le nom du projet et une phrase de description.
3. Ajoute le lien cliquable vers ton site publié : `[Voir le site](https://ton-pseudo.github.io)`.
4. Ajoute une petite liste de ce que contient ta page.
5. Ajoute une capture d'écran : uploade une image dans le dépôt puis insère-la avec `![ma page](nom-image.png)`.
6. « Commit » et vérifie que le README s'affiche, joliment formaté, en page d'accueil du dépôt.

### Étape 3 (⭐ principal) : une fonctionnalité JS au choix

Objectif : manipuler une liste, le hasard, et réagir à un clic. On approfondit le JS découvert au brief 1 et au cours.

1. Choisis **une seule** fonctionnalité, mais qui marche bien :
   - un **générateur de compliments** (un bouton tire une phrase au hasard dans une liste),
   - un **lanceur de dé** ou une **roue de décision** (« qui ramène le café ? »),
   - une **mini-horloge** ou un compteur de jours avant un événement,
   - un **mini-quiz** de 3 questions avec score,
   - un **fond qui change** de couleur à chaque clic.
2. Ajoute dans le HTML les éléments dont tu as besoin (un bouton, une zone de résultat).
3. Dans `script.js`, récupère ces éléments avec `document.querySelector(...)`.
4. Branche le clic avec `addEventListener` et fais l'effet voulu (inspire-toi des exemples du cours).
5. Teste en local, puis ré-uploade les fichiers modifiés sur GitHub.
6. Vérifie que la fonctionnalité marche sur l'URL publique.

### Étape 4 (○ bonus, si le temps)

1. **Initiation à Git en ligne de commande.** C'est la « vraie » façon de travailler ; ceux qui galèrent restent sur l'upload web. Suis le tutoriel pas à pas : <https://github.com/Selimmmm/git_step_by_step>. Dans l'ordre :
   1. installe Git et configure ton nom / e-mail,
   2. `git clone` ton dépôt sur ton ordi,
   3. modifie un fichier,
   4. `git add` puis `git commit -m "mon message"`,
   5. `git push` et vérifie que le changement apparaît en ligne.
2. Connecter un **nom de domaine** personnalisé (au moins comprendre le principe).
3. Ajouter une **deuxième** fonctionnalité JS.
4. Soigner le **responsive** et l'accessibilité (textes alternatifs des images).

## Modalités d'évaluation

Le formateur ouvre l'URL publique de chaque élève depuis son propre poste pour vérifier que le site est bien en ligne et que la feature fonctionne. Dépôt du lien sur SimplonLine.

## Livrables

1. L'**URL publique** du site (`https://ton-pseudo.github.io`), déposée sur SimplonLine.
2. Le dépôt GitHub contenant les fichiers + un `README.md` formaté.
3. Mise à jour du `JOURNAL.md` : explique ce qu'est GitHub Pages et décris ta feature JS.

## Critères de performance

- Le site est accessible publiquement à son URL, depuis n'importe quel appareil.
- Le `README.md` s'affiche correctement formaté sur la page du dépôt et contient un lien cliquable vers le site.
- La fonctionnalité JS ajoutée fonctionne sans erreur dans le navigateur.
- L'élève sait expliquer comment mettre à jour son site après une modification.

## Situation professionnelle

Hébergement et publication d'un site web statique, découverte de GitHub.

## Besoin visé ou problème rencontré

Toute entreprise tech utilise GitHub pour stocker, partager et publier du code. Savoir déposer un site, le publier et le documenter avec un README est un réflexe attendu dès le premier jour en poste. C'est aussi la base pour collaborer en équipe et montrer son travail à un recruteur (un portfolio en ligne vaut mieux qu'un fichier sur un disque dur).

## Compétences visées

**C1. Planifier le travail à effectuer individuellement**
niveau 1, imiter · niveau 2, adapter · niveau 3, transposer

**C2. Contribuer au pilotage de l'organisation du travail individuel et collectif**
niveau 1, imiter · niveau 2, adapter · niveau 3, transposer

**C4. Rechercher de façon méthodique une ou des solutions au problème rencontré**
niveau 1, imiter · niveau 2, adapter · niveau 3, transposer
