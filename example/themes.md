# Deux thèmes pour la même page

La page `4-page-vitrine/` est volontairement neutre : on voit la structure, pas le style. Ici, deux façons de l'habiller, sans toucher au HTML. On garde les mêmes classes (`.bouton`, `.carte`, `.hero`, etc.), on change seulement le CSS.

- **Brutaliste** : bordures noires épaisses, pas d'arrondi, ombres dures décalées, couleurs franches. Brut, assumé.
- **Minimaliste** (palette neutre, le « style Tailwind ») : gris doux, coins arrondis, ombres légères et floues, beaucoup d'espace.

Pour tester : copie un des blocs ci-dessous à la fin de `style.css` (il vient écraser le style neutre), ou remplace tout le fichier.

---

## Thème brutaliste

```css
/* Thème brutaliste : noir, jaune, bordures épaisses, ombres dures. */

body {
  font-family: "Courier New", monospace;
  background: #fdfd00;
  color: #000;
}

.navbar {
  border-bottom: 4px solid #000;
  background: #fff;
}

.logo {
  text-transform: uppercase;
  letter-spacing: 1px;
}

.bouton,
.bouton-secondaire {
  border: 3px solid #000;
  border-radius: 0;
  box-shadow: 4px 4px 0 #000;
  text-transform: uppercase;
}

.bouton {
  background: #000;
  color: #fdfd00;
}

.bouton-secondaire {
  background: #fff;
  color: #000;
}

.bouton:hover,
.bouton-secondaire:hover {
  box-shadow: none;
  transform: translate(4px, 4px);
}

.titre {
  font-weight: 900;
  text-transform: uppercase;
}

.hero-image,
.fonctions-image,
.histoire-image {
  border: 4px solid #000;
  border-radius: 0;
}

.carte,
.temoignage {
  border: 3px solid #000;
  border-radius: 0;
  background: #fff;
  box-shadow: 6px 6px 0 #000;
}

.avatar {
  border: 3px solid #000;
  border-radius: 0;
}

.telechargement {
  background: #000;
  color: #fdfd00;
  border: 4px solid #000;
}
```

---

## Thème minimaliste (palette neutre)

```css
/* Thème minimaliste : gris doux, arrondis, ombres légères.
   C'est le rendu « par défaut Tailwind » que tu vois partout. */

body {
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  background: #f9fafb;
  color: #1f2937;
}

.navbar {
  border-bottom: 1px solid #e5e7eb;
  background: #ffffff;
}

.bouton,
.bouton-secondaire {
  border-radius: 10px;
  border: 1px solid transparent;
  transition: background 0.15s;
}

.bouton {
  background: #111827;
  color: #ffffff;
}

.bouton:hover {
  background: #374151;
}

.bouton-secondaire {
  background: #ffffff;
  color: #374151;
  border-color: #d1d5db;
}

.bouton-secondaire:hover {
  background: #f3f4f6;
}

.titre {
  font-weight: 700;
  color: #111827;
}

.sous-titre {
  color: #6b7280;
}

.hero-image,
.fonctions-image,
.histoire-image {
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(17, 24, 39, 0.08);
}

.carte,
.temoignage {
  border: 1px solid #e5e7eb;
  border-radius: 14px;
  background: #ffffff;
  box-shadow: 0 1px 3px rgba(17, 24, 39, 0.06);
}

.avatar {
  border-radius: 50%;
}

.telechargement {
  background: #f3f4f6;
  border-radius: 20px;
}
```
