# Brief 3 : le mur de la promo (Supabase, sans backend)

**Type** : brief individuel (avec effet collectif)
**Durée visée** : 1 journée (7h), la plus dense
**Référentiel** : [2025] Mobiliser les compétences informatiques fondamentales
**Pré-requis** : avoir un site en ligne ([brief 2](brief-2-github-pages.md)).

Jusqu'ici, ta carte est figée : elle affiche toujours la même chose. Aujourd'hui on la rend **vivante et partagée**. On ajoute un livre d'or : un endroit où n'importe qui peut laisser un message, et ces messages sont stockés dans une base de données commune à toute la promo. Quand tu écris sur ton site, ça apparaît aussi sur celui des autres. Et tout ça **sans écrire le moindre serveur**.

## Contexte du projet

Une base de données, c'est là où une application range ses informations pour les retrouver plus tard (les messages, les comptes, les commandes...). D'habitude, pour y accéder, il faut un **backend** : un programme qui tourne sur un serveur et fait l'intermédiaire entre la page web et la base.

**Supabase** change la donne : dès qu'on crée une table, il génère automatiquement une **API** (un point d'accès standardisé) qu'on peut appeler **directement depuis le JavaScript du navigateur**. Pas de backend à écrire. C'est exactement ce qu'explique cet article : <https://supabase.com/blog/simplify-backend-with-data-api>.

Le point de vigilance, c'est la **sécurité**. La clé qu'on met dans le code (la clé « anon ») est publique, c'est normal. Ce qui protège les données, ce sont les règles **RLS** (Row Level Security) définies dans Supabase : elles disent qui a le droit de lire et d'écrire quoi. Pour notre mur public, la règle est simple (« tout le monde peut lire et ajouter un message »), et on prendra 15 minutes pour comprendre **pourquoi cette règle serait dangereuse** sur des données sensibles (un mot de passe, un dossier médical).

## Ressources

- Article de référence (à lire au début) : <https://supabase.com/blog/simplify-backend-with-data-api>
- Doc Supabase JavaScript : <https://supabase.com/docs/reference/javascript/introduction>
- L'**URL du projet** et la **clé anon** fournies par le formateur (projet Supabase partagé par la promo).

## Modalités pédagogiques

Travail individuel sur un **projet Supabase partagé** (le formateur le crée et distribue l'URL + la clé anon, pour ne pas perdre de temps). Le formateur fait la démo complète une fois, puis chacun branche son propre site.

La table est déjà créée par le formateur, avec ces colonnes : `id`, `created_at`, `auteur` (texte), `message` (texte). RLS activée avec une politique « lecture + insertion pour tous ».

### Étape 1 (⭐ principal) : lire les messages

Objectif : comprendre qu'un appel JS va chercher des données ailleurs et les affiche. Premier « aller-retour » avec une base de données.

1. Dans `index.html`, charge la librairie Supabase avec une ligne de `<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>`.
2. Récupère auprès du formateur l'**URL du projet** et la **clé anon**.
3. Crée le client : `const supabase = window.supabase.createClient(URL, CLE_ANON);`.
4. Ajoute dans la page une zone vide où afficher les messages : `<div id="mur"></div>`.
5. Écris une fonction qui va chercher les messages et vérifie d'abord dans la console :

   ```javascript
   const { data, error } = await supabase
     .from('messages')
     .select('*')
     .order('created_at', { ascending: false });
   console.log(data);
   ```
6. Parcours `data` avec `forEach` et, pour chaque message, ajoute un élément dans `#mur` (auteur + message).

### Étape 2 (⭐ principal) : écrire un message

Objectif : comprendre le **CRUD** (créer / lire), et voir l'effet collectif : ton message apparaît chez tout le monde.

1. Ajoute un petit formulaire : un champ « ton nom », un champ « ton message », un bouton « Envoyer ».
2. Au clic sur le bouton, récupère les valeurs des deux champs.
3. Insère le message dans la table :

   ```javascript
   await supabase
     .from('messages')
     .insert({ auteur: nom, message: texte });
   ```
4. Après l'insertion, rappelle ta fonction d'affichage pour recharger la liste.
5. Teste : ton message apparaît. Demande à un voisin d'en poster un : il apparaît aussi chez toi.

### Étape 3 (⭐ principal) : comprendre la sécurité

Pas de code ici, une **discussion guidée** de 15 à 20 min animée par le formateur. Note tes réponses dans `JOURNAL.md` :

1. Pourquoi la clé anon peut-elle être publique, visible dans le code ?
2. Qu'est-ce que RLS (Row Level Security) empêche exactement ?
3. Pourquoi la règle « tout le monde peut écrire » est ok pour un mur public mais serait catastrophique pour des mots de passe ou un dossier médical ?

### Étape 4 (○ bonus, si le temps)

1. **Tri et filtres** : afficher les plus récents en premier, ou filtrer par auteur.
2. **Suppression** : un bouton « supprimer » (et constater que RLS pourrait l'interdire aux autres : bonne occasion de reparler sécurité).
3. **Anti-spam léger** : empêcher l'envoi d'un message vide.
4. **Ton propre projet** : créer ton projet Supabase, ta table, et configurer la politique RLS toi-même depuis l'interface.
5. **Auth** : découvrir Supabase Auth (connexion par e-mail) et n'autoriser l'écriture qu'aux personnes connectées.

## Modalités d'évaluation

Démonstration en direct : l'élève écrit un message sur son site, le formateur vérifie qu'il apparaît sur le mur partagé (donc sur d'autres sites). Dépôt du lien et du journal sur SimplonLine.

## Livrables

1. Le site mis à jour, en ligne, avec le mur de messages **lecture + écriture** fonctionnel.
2. Le `JOURNAL.md` complété avec la partie **sécurité** (clé anon, RLS, pourquoi c'est ok ici).
3. (Bonus) Une courte note Markdown ou Google Doc « Ce que je ferais différemment pour des données sensibles ».

## Critères de performance

- Le site lit et affiche les messages de la base Supabase.
- Le site permet d'ajouter un nouveau message, qui est bien enregistré dans la base.
- L'élève sait expliquer, à l'oral ou dans son journal, le rôle de la clé anon et de RLS.
- L'effet collectif est constaté : un message écrit sur un site apparaît sur les autres.

## Situation professionnelle

Connexion d'une application front-end à une base de données via une API, sans backend dédié.

## Besoin visé ou problème rencontré

Les entreprises veulent livrer vite des produits qui manipulent des données (formulaires, listes, comptes) sans payer la complexité d'un backend complet. Des solutions comme Supabase répondent à ce besoin en exposant une API directement utilisable depuis le front. Savoir brancher une page web sur une telle API, et comprendre les enjeux de sécurité associés (clé publique, règles d'accès), est une compétence directement employable dans une petite équipe ou une startup.

## Compétences visées

**C1. Planifier le travail à effectuer individuellement**
niveau 1, imiter · niveau 2, adapter · niveau 3, transposer

**C3. Définir le périmètre d'un problème rencontré en adoptant une démarche inductive**
niveau 1, imiter · niveau 2, adapter · niveau 3, transposer

**C4. Rechercher de façon méthodique une ou des solutions au problème rencontré**
niveau 1, imiter · niveau 2, adapter · niveau 3, transposer
