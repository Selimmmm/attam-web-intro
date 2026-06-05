# Brief 2 : en ligne ! (GitHub Pages + une feature JS)

- **Type** : brief individuel
- **Référentiel** : [2025] Mobiliser les compétences informatiques fondamentales
- **Pré-requis** : avoir fini le cœur du [brief 1](#brief-1).

Ta page n'existe que sur ton ordinateur. Aujourd'hui, tu vas la publier sur internet : à la fin de la journée, elle aura une **adresse publique** que tu pourras partager. Tu lui ajouteras aussi un **formulaire de contact** en JavaScript.

## Contexte du projet

Mettre un site « en ligne », c'est le déposer sur un serveur accessible à tous. GitHub propose ça gratuitement avec **GitHub Pages** : tu déposes tes fichiers sur GitHub (une plateforme où les développeurs stockent et partagent leur code), et GitHub publie automatiquement ta page sur une URL publique.

Au passage, tu découvres **GitHub**, l'outil que tu retrouveras dans absolument toutes les entreprises tech. On reste sur l'essentiel : déposer des fichiers, les mettre à jour, publier.

## Ressources

- GitHub Pages, démarrage : <https://pages.github.com/>
- Doc GitHub (upload de fichiers via le navigateur) : <https://docs.github.com/fr/repositories>
- Antisèche Markdown : <https://www.markdownguide.org/cheat-sheet/>
- Les formulaires HTML : <https://developer.mozilla.org/fr/docs/Learn_web_development/Extensions/Forms>
- Validation de formulaire en JS : <https://developer.mozilla.org/fr/docs/Learn_web_development/Extensions/Forms/Form_validation>

## Modalités pédagogiques

Travail individuel. Le formateur fait la première mise en ligne en démo, puis chacun refait avec ses fichiers. Avance pas à pas et vérifie chaque résultat avant de continuer.

### Étape 1 (⭐ principal) : créer son dépôt et publier

Objectif : comprendre la différence entre « le fichier sur mon ordi » et « le site publié », et savoir mettre à jour le site.

1. Crée un compte GitHub (si tu n'en as pas) et confirme ton adresse e-mail.
2. Clique sur « New repository » pour créer un nouveau dépôt.
3. Nomme-le comme tu veux, par exemple `ma-page` ou `portfolio` (lettres, chiffres et tirets, pas d'espaces) et coche « Public ».
4. Sur la page du dépôt, clique « Add file » → « Upload files ».
5. Glisse-dépose tes fichiers du brief 1 (`index.html`, `style.css`, `script.js`) puis clique « Commit changes ».
6. Va dans l'onglet « Settings » → « Pages », choisis la branche `main` comme source et clique « Save ».
7. Attends une minute, puis recharge la page « Settings » → « Pages » : GitHub y affiche l'URL publique, de la forme `https://ton-pseudo.github.io/nom-du-repo/`. Ouvre-la, ta page doit s'afficher.
8. Teste une mise à jour : modifie une couleur dans `style.css` sur ton ordi, ré-uploade le fichier, et recharge l'URL pour voir le changement.

> Deux façons de nommer le dépôt. Si tu l'appelles **exactement** `ton-pseudo.github.io`, le site est servi à la racine : `https://ton-pseudo.github.io`. Avec **n'importe quel autre nom**, c'est un « site de projet » servi dans un sous-dossier : `https://ton-pseudo.github.io/nom-du-repo/`. Les deux marchent. Pour la suite, garde des chemins **relatifs** dans ton HTML (`style.css`, `script.js`, pas `/style.css`) pour que les fichiers soient trouvés quel que soit le nom du dépôt.

### Étape 2 (⭐ principal) : un vrai README en Markdown

Objectif : voir le Markdown servir « pour de vrai » et comprendre le rôle d'un README.

1. Sur le dépôt, clique « Add file » → « Create new file » et nomme-le `README.md`.
2. Écris un titre (`#`) avec le nom du projet et une phrase de description.
3. Ajoute le lien cliquable vers ton site publié : `[Voir le site](TON-URL)` (l'URL affichée dans « Settings » → « Pages »).
4. Ajoute une petite liste de ce que contient ta page.
5. Ajoute une capture d'écran : uploade une image dans le dépôt puis insère-la avec `![ma page](nom-image.png)`.
6. « Commit » et vérifie que le README s'affiche, joliment formaté, en page d'accueil du dépôt.

### Étape 3 (⭐ principal) : un formulaire de contact

Objectif : construire un formulaire HTML, lire ce que l'utilisateur a saisi, le valider en JavaScript et réagir à l'envoi. On approfondit le JS découvert au brief 1 et au cours.

1. Dans `index.html`, ajoute un `<form>` avec au moins trois champs :
    - un champ **nom** (`<input type="text">`),
    - un champ **e-mail** (`<input type="email">`),
    - un champ **message** (`<textarea>`),
    - un bouton d'envoi (`<button type="submit">`).
2. Mets un `<label>` devant chaque champ et un `id` sur chacun pour pouvoir le récupérer.
3. Prévois une zone de résultat vide (`<p id="confirmation"></p>`) pour afficher le message de retour.
4. Dans `script.js`, récupère le formulaire et les champs avec `document.querySelector(...)`.
5. Branche l'envoi avec `addEventListener('submit', ...)` et appelle `event.preventDefault()` pour empêcher le rechargement de la page.
6. Vérifie que les champs ne sont pas vides et que l'e-mail contient bien un `@`. Si quelque chose manque, affiche un message d'erreur ; sinon, affiche une confirmation du type « Merci NOM, ton message a bien été pris en compte ».
7. Teste en local, puis ré-uploade les fichiers modifiés sur GitHub.
8. Vérifie que le formulaire marche sur l'URL publique.

> Note : GitHub Pages héberge un site statique, sans serveur. Le formulaire ne peut donc pas vraiment envoyer d'e-mail tout seul. Ici on se concentre sur la saisie, la validation et le retour à l'utilisateur. L'envoi réel viendra au [brief 3](#brief-3) avec Supabase.

### Étape 4 (○ bonus, si le temps)

1. Connecter un **nom de domaine** personnalisé (au moins comprendre le principe).
2. Soigner les **messages d'erreur** : afficher précisément quel champ pose problème plutôt qu'un message générique.
3. Soigner le **responsive** et l'accessibilité (labels bien liés aux champs, focus visible, messages d'erreur lisibles).

## Modalités d'évaluation

Le formateur ouvre l'URL publique de chaque élève depuis son propre poste pour vérifier que le site est bien en ligne et que le formulaire de contact fonctionne (validation et message de retour). Dépôt du lien sur SimplonLine.

## Livrables

1. L'**URL publique** du site (`https://ton-pseudo.github.io` ou `https://ton-pseudo.github.io/nom-du-repo/`), déposée sur SimplonLine.
2. Le dépôt GitHub contenant les fichiers + un `README.md` formaté.
3. Mise à jour du `JOURNAL.md` : explique ce qu'est GitHub Pages et décris ton formulaire de contact (champs, validation, message de retour).

## Critères de performance

- Le site est accessible publiquement à son URL, depuis n'importe quel appareil.
- Le `README.md` s'affiche correctement formaté sur la page du dépôt et contient un lien cliquable vers le site.
- Le formulaire de contact valide les champs et affiche un message de retour clair, sans erreur dans le navigateur.
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
