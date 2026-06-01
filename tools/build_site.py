#!/usr/bin/env python3
"""Compile les briefs Markdown en un site statique de présentation.

Usage :
    python3 tools/build_site.py

Lit README.md et briefs/*.md, génère site/index.html (page unique, sidebar de
sélection + panneau central). Le rendu est autonome : aucune dépendance réseau
sauf les polices Google. Les élèves n'ouvrent que site/index.html, jamais ce
script. Reconstruire après chaque modification d'un brief.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

import markdown
from pygments import highlight as pyg_highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site" / "index.html"

# Ordre et libellés courts de la barre latérale. Le titre affiché dans le
# panneau central est le premier titre (#) du fichier.
# README.md est le doc de pilotage interne (formateur) et n'apparaît PAS dans le
# site vu par les apprenants. La page d'accueil du site est accueil.md.
PAGES = [
    {"file": "accueil.md", "slug": "accueil", "nav": "Accueil"},
    {"file": "cours-js.md", "slug": "cours-js", "nav": "Cours · JS et le DOM"},
    {"file": "briefs/brief-1-html-css-js.md", "slug": "brief-1", "nav": "Brief 1 · ma page de présentation"},
    {"file": "briefs/brief-2-github-pages.md", "slug": "brief-2", "nav": "Brief 2 · en ligne"},
    {"file": "briefs/brief-3-supabase.md", "slug": "brief-3", "nav": "Brief 3 · le mur de la promo"},
]

MD_EXTENSIONS = ["extra", "fenced_code", "tables", "sane_lists", "codehilite", "toc"]
MD_CONFIG = {"codehilite": {"guess_lang": False}}


def extract_title(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Sans titre"


def tag_section_headings(rendered: str) -> str:
    """Colore les titres d'étapes selon principal (vert) ou bonus (ambre)."""

    def repl(match: re.Match) -> str:
        level, attrs, inner = match.group(1), match.group(2), match.group(3)
        plain = re.sub(r"<[^>]+>", "", inner).lower()
        cls = None
        if "principal" in plain:
            cls = "is-principal"
        elif "bonus" in plain or "secondaire" in plain:
            cls = "is-bonus"
        if cls and "class=" not in attrs:
            attrs = f' class="{cls}"' + attrs
        return f"<h{level}{attrs}>{inner}</h{level}>"

    return re.sub(r"<h([34])([^>]*)>(.*?)</h\1>", repl, rendered, flags=re.DOTALL)


def highlight_code(code: str, lang: str) -> str:
    lexer = get_lexer_by_name(lang)
    return pyg_highlight(code, lexer, HtmlFormatter(cssclass="codehilite"))


# Blocs interactifs. Syntaxe dans le Markdown :
#   ```jsrun           JS éditable, exécution + console
#   ```jsrun-frozen    idem mais en lecture seule
#   ```domrun          HTML de départ + ligne "===" + JS éditable qui manipule le DOM
#   ```domrun-frozen   idem mais JS en lecture seule
PG_FENCE = re.compile(
    r"(?ms)^```(jsrun-frozen|jsrun|domrun-frozen|domrun)[ \t]*\n(.*?)\n```[ \t]*$"
)


def make_widget(lang: str, content: str) -> str:
    frozen = lang.endswith("-frozen")
    kind = "dom" if lang.startswith("dom") else "js"
    if kind == "dom":
        parts = re.split(r"(?m)^[ \t]*===[ \t]*$", content, maxsplit=1)
        stage_html = parts[0].strip("\n")
        js = (parts[1] if len(parts) > 1 else "").strip("\n")
    else:
        stage_html = ""
        js = content.strip("\n")

    frozen_attr = ' data-frozen="1"' if frozen else ""
    ro = " readonly" if frozen else ""
    rows = max(2, js.count("\n") + 1)
    js_esc = html.escape(js)
    label = "lecture seule" if frozen else "à toi de jouer"

    bits = [f'<div class="pg" data-kind="{kind}"{frozen_attr}>']
    if kind == "dom":
        bits.append('<div class="pg-htmllabel">HTML de départ</div>')
        bits.append(highlight_code(stage_html, "html"))
        bits.append(f'<template class="pg-html">{stage_html}</template>')
    bits.append(
        '<div class="pg-bar"><span class="pg-lang">JavaScript · '
        + label
        + '</span><span class="pg-actions">'
        + '<button class="pg-run" type="button">▶ Exécuter</button>'
        + ("" if frozen else '<button class="pg-reset" type="button" title="Réinitialiser">↺</button>')
        + "</span></div>"
    )
    bits.append(
        '<div class="pg-editor">'
        '<pre class="pg-hl" aria-hidden="true"><code class="language-js"></code></pre>'
        f'<textarea class="pg-code" spellcheck="false" autocapitalize="off" autocomplete="off" autocorrect="off"{ro} rows="{rows}">{js_esc}</textarea>'
        "</div>"
    )
    bits.append(f'<textarea class="pg-initial" hidden>{js_esc}</textarea>')
    stage_cls = "pg-stage" if kind == "dom" else "pg-stage pg-hidden"
    bits.append(f'<iframe class="{stage_cls}" sandbox="allow-scripts allow-modals" title="résultat"></iframe>')
    bits.append('<div class="pg-console" aria-live="polite"></div>')
    bits.append("</div>")
    return "\n".join(bits)


def preprocess_playgrounds(src: str) -> tuple[str, dict[int, str]]:
    widgets: dict[int, str] = {}

    def repl(m: re.Match) -> str:
        idx = len(widgets)
        widgets[idx] = make_widget(m.group(1), m.group(2))
        return f"\n\n@@PG{idx}@@\n\n"

    return PG_FENCE.sub(repl, src), widgets


MERMAID_FENCE = re.compile(r"(?ms)^```mermaid[ \t]*\n(.*?)\n```[ \t]*$")


def preprocess_mermaid(src: str) -> tuple[str, dict[int, str]]:
    blocks: dict[int, str] = {}

    def repl(m: re.Match) -> str:
        idx = len(blocks)
        blocks[idx] = f'<pre class="mermaid">{html.escape(m.group(1))}</pre>'
        return f"\n\n@@MM{idx}@@\n\n"

    return MERMAID_FENCE.sub(repl, src), blocks


def build_page(page: dict) -> tuple[str, str]:
    src = (ROOT / page["file"]).read_text(encoding="utf-8")
    title = extract_title(src)
    raw = html.escape(src)
    pp, widgets = preprocess_playgrounds(src)
    pp, mermaids = preprocess_mermaid(pp)
    md = markdown.Markdown(extensions=MD_EXTENSIONS, extension_configs=MD_CONFIG)
    body = tag_section_headings(md.convert(pp))
    for idx, widget in widgets.items():
        body = body.replace(f"<p>@@PG{idx}@@</p>", widget).replace(f"@@PG{idx}@@", widget)
    for idx, diagram in mermaids.items():
        body = body.replace(f"<p>@@MM{idx}@@</p>", diagram).replace(f"@@MM{idx}@@", diagram)

    nav = f'<button class="nav-item" data-target="{page["slug"]}">{html.escape(page["nav"])}</button>'

    section = f"""<section class="page" id="{page['slug']}" hidden>
  <div class="page-toolbar">
    <button class="src-toggle" data-src="src-{page['slug']}">Voir la source Markdown</button>
  </div>
  <article class="prose">{body}</article>
  <pre class="md-source" id="src-{page['slug']}" hidden><code>{raw}</code></pre>
</section>"""
    return nav, section


def main() -> None:
    navs, sections = [], []
    for page in PAGES:
        nav, section = build_page(page)
        navs.append(nav)
        sections.append(section)

    # Couleurs des tokens Pygments mappées sur les mêmes variables CSS que
    # l'éditeur Prism, pour une coloration unifiée et adaptée au thème clair/sombre.
    pygments_css = (
        ".codehilite .c,.codehilite .ch,.codehilite .cm,.codehilite .c1,.codehilite .cs,.codehilite .cp{color:var(--tok-comment);font-style:italic}\n"
        ".codehilite .k,.codehilite .kd,.codehilite .kn,.codehilite .kr,.codehilite .kc,.codehilite .kt,.codehilite .kp{color:var(--tok-keyword)}\n"
        ".codehilite .s,.codehilite .s1,.codehilite .s2,.codehilite .sb,.codehilite .sc,.codehilite .sd,.codehilite .se,.codehilite .sh,.codehilite .si,.codehilite .sx,.codehilite .sr,.codehilite .ss,.codehilite .dl{color:var(--tok-string)}\n"
        ".codehilite .m,.codehilite .mi,.codehilite .mf,.codehilite .mh,.codehilite .mo,.codehilite .il{color:var(--tok-number)}\n"
        ".codehilite .nf,.codehilite .fm,.codehilite .na{color:var(--tok-function)}\n"
        ".codehilite .o,.codehilite .ow,.codehilite .p{color:var(--tok-operator)}\n"
        ".codehilite .nb,.codehilite .bp,.codehilite .nc,.codehilite .nn,.codehilite .no,.codehilite .ne{color:var(--tok-builtin)}\n"
        ".codehilite .nt{color:var(--tok-keyword)}"
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        TEMPLATE.replace("/*__PYGMENTS__*/", pygments_css)
        .replace("<!--__NAV__-->", "\n      ".join(navs))
        .replace("<!--__SECTIONS__-->", "\n".join(sections)),
        encoding="utf-8",
    )
    print(f"Écrit : {OUT.relative_to(ROOT)}  ({OUT.stat().st_size // 1024} Ko)")


TEMPLATE = r"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Intro web : les briefs</title>
  <meta name="description" content="Briefs du module d'introduction au web : HTML, CSS, JS, GitHub Pages, Supabase.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@400;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1/components/prism-core.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1/components/prism-clike.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1/components/prism-javascript.min.js" defer></script>
  <style>
    :root {
      --bg: #fbfaf7;
      --panel: #ffffff;
      --ink: #1f2430;
      --muted: #6b7280;
      --line: #e7e3da;
      --accent: #3b82f6;
      --accent-soft: #eaf1ff;
      --principal: #10b981;
      --bonus: #d97706;
      --sidebar-w: 270px;
      --code-bg: #f6f8fa;
      --code-fg: #24292e;
      --tok-comment: #6a737d;
      --tok-keyword: #cf222e;
      --tok-string: #0a7d33;
      --tok-number: #0550ae;
      --tok-function: #6639ba;
      --tok-operator: #57606a;
      --tok-builtin: #953800;
    }
    html[data-theme="dark"] {
      --bg: #14161b;
      --panel: #1b1e25;
      --ink: #e8e6e1;
      --muted: #9aa1ad;
      --line: #2c313b;
      --accent: #6ea8fe;
      --accent-soft: #232a38;
      --principal: #34d399;
      --bonus: #f59e0b;
      --code-bg: #0f1117;
      --code-fg: #e6e6e6;
      --tok-comment: #6b7a8f;
      --tok-keyword: #c792ea;
      --tok-string: #c3e88d;
      --tok-number: #f78c6c;
      --tok-function: #82aaff;
      --tok-operator: #89ddff;
      --tok-builtin: #ffcb6b;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: "Inter", system-ui, sans-serif;
      background: var(--bg);
      color: var(--ink);
      display: flex;
      min-height: 100vh;
    }
    a { color: var(--accent); }

    /* Sidebar */
    .sidebar {
      width: var(--sidebar-w);
      flex: 0 0 var(--sidebar-w);
      border-right: 1px solid var(--line);
      background: var(--panel);
      padding: 24px 18px;
      display: flex;
      flex-direction: column;
      gap: 18px;
      position: sticky;
      top: 0;
      height: 100vh;
      overflow-y: auto;
    }
    .brand { font-family: "Crimson Pro", serif; font-size: 1.45rem; font-weight: 700; line-height: 1.1; }
    .brand small { display: block; font-family: "Inter"; font-size: .72rem; font-weight: 500; color: var(--muted); text-transform: uppercase; letter-spacing: .08em; margin-top: 6px; }
    nav { display: flex; flex-direction: column; gap: 4px; }
    .nav-item {
      text-align: left;
      border: none;
      background: transparent;
      color: var(--ink);
      font: inherit;
      font-weight: 500;
      padding: 9px 12px;
      border-radius: 8px;
      cursor: pointer;
      transition: background .12s;
    }
    .nav-item:hover { background: var(--accent-soft); }
    .nav-item.active { background: var(--accent-soft); color: var(--accent); font-weight: 600; }
    .legend { font-size: .78rem; color: var(--muted); display: flex; flex-direction: column; gap: 6px; }
    .dot { display: inline-block; width: 9px; height: 9px; border-radius: 50%; margin-right: 7px; vertical-align: middle; }
    .dot.p { background: var(--principal); }
    .dot.b { background: var(--bonus); }
    .sidebar-footer { margin-top: auto; font-size: .76rem; color: var(--muted); line-height: 1.5; }
    .theme-btn { border: 1px solid var(--line); background: transparent; color: var(--muted); font: inherit; font-size: .8rem; padding: 6px 10px; border-radius: 8px; cursor: pointer; }

    /* Main */
    main { flex: 1; padding: 48px 7vw; max-width: 960px; }
    .page-toolbar { display: flex; justify-content: flex-end; margin-bottom: 8px; }
    .src-toggle { border: 1px solid var(--line); background: var(--panel); color: var(--muted); font: inherit; font-size: .8rem; padding: 6px 12px; border-radius: 8px; cursor: pointer; }
    .src-toggle:hover { color: var(--accent); border-color: var(--accent); }
    .md-source { background: var(--code-bg); color: var(--code-fg); border: 1px solid var(--line); border-radius: 10px; padding: 18px; overflow-x: auto; font-size: .82rem; line-height: 1.5; }

    /* Prose */
    .prose { font-size: 1.02rem; line-height: 1.68; }
    .prose h1 { font-family: "Crimson Pro", serif; font-size: 2.3rem; line-height: 1.12; margin: 0 0 .3em; }
    .prose h2 { font-family: "Crimson Pro", serif; font-size: 1.55rem; margin: 1.8em 0 .5em; padding-bottom: .25em; border-bottom: 1px solid var(--line); }
    .prose h3 { font-size: 1.18rem; margin: 1.5em 0 .4em; }
    .prose h3.is-principal { color: var(--principal); }
    .prose h3.is-principal::before { content: "● "; }
    .prose h3.is-bonus { color: var(--bonus); }
    .prose h3.is-bonus::before { content: "○ "; }
    .prose h4 { font-size: 1.02rem; margin: 1.3em 0 .3em; }
    .prose blockquote { border-left: 3px solid var(--accent); margin: 1.2em 0; padding: .4em 1.1em; background: var(--accent-soft); border-radius: 0 8px 8px 0; color: var(--muted); }
    .prose code { background: var(--accent-soft); padding: .12em .4em; border-radius: 5px; font-size: .88em; }
    .prose pre { background: var(--code-bg); border-radius: 10px; padding: 16px 18px; overflow-x: auto; border: 1px solid var(--line); }
    .prose pre code { background: none; padding: 0; color: var(--code-fg); }
    .prose table { border-collapse: collapse; width: 100%; margin: 1.2em 0; font-size: .94rem; }
    .prose th, .prose td { border: 1px solid var(--line); padding: 8px 12px; text-align: left; }
    .prose th { background: var(--accent-soft); }
    .prose ul, .prose ol { padding-left: 1.4em; }
    .prose li { margin: .25em 0; }
    .prose img { max-width: 100%; border-radius: 8px; }
    .codehilite { background: var(--code-bg); color: var(--code-fg); border-radius: 10px; padding: 16px 18px; overflow-x: auto; margin: 1.2em 0; border: 1px solid var(--line); }
    .codehilite pre { background: none; padding: 0; margin: 0; color: var(--code-fg); }
    /*__PYGMENTS__*/

    /* Diagrammes mermaid */
    .mermaid { background: #fff; text-align: center; margin: 1.4em 0; border: 1px solid var(--line); border-radius: 12px; padding: 18px; overflow-x: auto; }
    .mermaid:not([data-processed]) { min-height: 40px; color: transparent; }
    .mermaid svg { max-width: 100%; height: auto; }

    /* Playgrounds interactifs */
    .pg { border: 1px solid var(--line); border-radius: 12px; overflow: hidden; margin: 1.5em 0; background: var(--panel); }
    .pg-htmllabel { font-size: .72rem; text-transform: uppercase; letter-spacing: .07em; color: var(--muted); padding: 10px 14px 0; font-weight: 600; }
    .pg .codehilite { margin: 6px 14px 10px; }
    .pg-bar { display: flex; align-items: center; justify-content: space-between; gap: 8px; padding: 8px 14px; background: var(--accent-soft); border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); }
    .pg-lang { font-size: .76rem; color: var(--muted); font-weight: 600; }
    .pg-actions { display: flex; gap: 6px; }
    .pg-run, .pg-reset { font: inherit; font-size: .82rem; font-weight: 600; border: none; border-radius: 7px; cursor: pointer; }
    .pg-run { background: var(--accent); color: #fff; padding: 6px 13px; }
    .pg-run:hover { filter: brightness(1.06); }
    .pg-reset { background: transparent; color: var(--muted); border: 1px solid var(--line); padding: 6px 10px; }
    .pg-reset:hover { color: var(--ink); }
    .pg-editor { position: relative; background: var(--code-bg); }
    .pg-editor .pg-hl, .pg-editor .pg-code { margin: 0; border: 0; padding: 14px; font-family: "SF Mono", ui-monospace, Menlo, Consolas, monospace; font-size: .9rem; line-height: 1.55; tab-size: 2; white-space: pre-wrap; word-break: break-word; overflow-wrap: break-word; }
    .pg-hl { position: absolute; inset: 0; z-index: 0; background: var(--code-bg); color: var(--code-fg); overflow: hidden; pointer-events: none; }
    .pg-hl code { font: inherit; white-space: inherit; word-break: inherit; display: block; background: none; }
    .pg-code { position: relative; z-index: 1; display: block; width: 100%; resize: none; background: transparent; color: transparent; caret-color: var(--code-fg); outline: none; }
    .pg-code::selection { background: rgba(110,168,254,.35); color: transparent; }
    .pg-code::-moz-selection { background: rgba(110,168,254,.35); color: transparent; }
    .pg-hl .token.comment, .pg-hl .token.prolog, .pg-hl .token.doctype, .pg-hl .token.cdata { color: var(--tok-comment); font-style: italic; }
    .pg-hl .token.keyword { color: var(--tok-keyword); }
    .pg-hl .token.string, .pg-hl .token.template-string, .pg-hl .token.char, .pg-hl .token.attr-value, .pg-hl .token.regex { color: var(--tok-string); }
    .pg-hl .token.number, .pg-hl .token.boolean { color: var(--tok-number); }
    .pg-hl .token.function, .pg-hl .token.attr-name { color: var(--tok-function); }
    .pg-hl .token.operator, .pg-hl .token.punctuation { color: var(--tok-operator); }
    .pg-hl .token.property-access, .pg-hl .token.constant, .pg-hl .token.class-name, .pg-hl .token.builtin, .pg-hl .token.tag { color: var(--tok-builtin); }
    .pg-stage { width: 100%; min-height: 80px; border: none; border-top: 1px solid var(--line); background: #fff; display: block; }
    .pg-stage.pg-hidden { display: none; }
    .pg-console { font-family: "SF Mono", ui-monospace, Menlo, monospace; font-size: .84rem; line-height: 1.5; background: #14161b; color: #cfe3ff; }
    .pg-console:empty { display: none; }
    .pg-console .pg-line { padding: 5px 14px; border-top: 1px solid rgba(255,255,255,.06); white-space: pre-wrap; word-break: break-word; }
    .pg-console .pg-error { color: #ff9b9b; }
    .pg-console .pg-warn { color: #ffd479; }
    .pg-console .pg-info, .pg-console .pg-debug { color: #9aa1ad; }

    /* Mobile */
    .mobile-bar { display: none; }
    @media (max-width: 820px) {
      body { flex-direction: column; }
      .mobile-bar { display: flex; align-items: center; gap: 12px; padding: 12px 16px; border-bottom: 1px solid var(--line); background: var(--panel); position: sticky; top: 0; z-index: 20; }
      .mobile-bar button { border: 1px solid var(--line); background: transparent; color: var(--ink); font: inherit; padding: 6px 10px; border-radius: 8px; }
      .sidebar { position: fixed; inset: 0 auto 0 0; z-index: 30; transform: translateX(-100%); transition: transform .2s; width: 84vw; }
      .sidebar.open { transform: translateX(0); }
      main { padding: 28px 6vw; }
    }
  </style>
</head>
<body>
  <div class="mobile-bar">
    <button id="menu-btn">☰ Briefs</button>
    <strong>Intro web</strong>
  </div>

  <aside class="sidebar" id="sidebar">
    <div class="brand">Intro web<small>HTML · CSS · JS · GitHub · Supabase</small></div>
    <nav id="nav">
      <!--__NAV__-->
    </nav>
    <div class="legend">
      <span><span class="dot p"></span>principal, à finir</span>
      <span><span class="dot b"></span>bonus, si le temps</span>
    </div>
    <div class="sidebar-footer">
      <button class="theme-btn" id="theme-btn">Thème clair / sombre</button>
      <p style="margin:.8em 0 0">Promo Level-Up · briefs en Markdown, compilés en HTML par <code>tools/build_site.py</code>.</p>
    </div>
  </aside>

  <main id="main">
    <!--__SECTIONS__-->
  </main>

  <script>
    const pages = [...document.querySelectorAll('.page')];
    const navItems = [...document.querySelectorAll('.nav-item')];
    const sidebar = document.getElementById('sidebar');

    function show(slug) {
      const target = pages.find(p => p.id === slug) ? slug : pages[0].id;
      pages.forEach(p => p.hidden = p.id !== target);
      navItems.forEach(n => n.classList.toggle('active', n.dataset.target === target));
      if (location.hash !== '#' + target) history.replaceState(null, '', '#' + target);
      sidebar.classList.remove('open');
      window.scrollTo(0, 0);
      const vis = pages.find(p => !p.hidden);
      if (vis) vis.querySelectorAll('.pg-code').forEach(pgAutosize);
      if (vis && window.__renderMermaid) window.__renderMermaid(vis);
    }

    navItems.forEach(n => n.addEventListener('click', () => show(n.dataset.target)));
    window.addEventListener('hashchange', () => show(location.hash.slice(1)));

    document.querySelectorAll('.src-toggle').forEach(btn => {
      const el = document.getElementById(btn.dataset.src);
      btn.addEventListener('click', () => {
        el.hidden = !el.hidden;
        btn.textContent = el.hidden ? 'Voir la source Markdown' : 'Masquer la source';
      });
    });

    document.getElementById('menu-btn')?.addEventListener('click', () => sidebar.classList.toggle('open'));

    const themeBtn = document.getElementById('theme-btn');
    const saved = localStorage.getItem('theme');
    if (saved) document.documentElement.dataset.theme = saved;
    themeBtn.addEventListener('click', () => {
      const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
      document.documentElement.dataset.theme = next;
      localStorage.setItem('theme', next);
    });

    // --- Playgrounds : exécution de JS dans un iframe sandboxé ---
    function pgAutosize(t) { t.style.height = 'auto'; t.style.height = (t.scrollHeight + 2) + 'px'; }

    function pgHighlight(ta) {
      var holder = ta.parentNode.querySelector('.pg-hl code');
      if (!holder) return;
      if (window.Prism && Prism.languages && Prism.languages.javascript) {
        holder.innerHTML = Prism.highlight(ta.value, Prism.languages.javascript, 'javascript');
      } else {
        holder.textContent = ta.value;
      }
    }

    function pgSrcdoc(code, stage, token) {
      var safe = JSON.stringify(code).replace(/</g, '\\u003c');
      return ['<!doctype html><html><head><meta charset="utf-8"><style>',
        'body{font:14px/1.6 system-ui,-apple-system,sans-serif;color:#1f2430;margin:12px}',
        'button{font:inherit;padding:5px 11px;border:1px solid #cfd4dd;border-radius:7px;background:#f3f4f6;cursor:pointer}',
        'h1,h2,h3{margin:.2em 0 .4em}*{box-sizing:border-box}',
        '</style></head><body>', stage,
        '<scr' + 'ipt>(function(){var T=' + token + ';',
        'function fmt(v){if(typeof v==="string")return v;if(v===undefined)return "undefined";if(v===null)return "null";try{return JSON.stringify(v)}catch(e){return String(v)}}',
        'function send(l,a){parent.postMessage({__pg:true,token:T,level:l,text:[].map.call(a,fmt).join(" ")},"*")}',
        '["log","info","warn","error","debug"].forEach(function(m){var o=console[m]?console[m].bind(console):function(){};console[m]=function(){send(m,arguments);o.apply(null,arguments)}});',
        'window.addEventListener("error",function(e){send("error",[e.message])});',
        'window.addEventListener("unhandledrejection",function(e){send("error",["Promesse rejetee : "+((e.reason&&e.reason.message)||e.reason)])});',
        'function sendSize(){var h=Math.max(document.body?document.body.scrollHeight:0,document.documentElement.scrollHeight);parent.postMessage({__pgsize:true,token:T,height:h},"*")}',
        'if(window.ResizeObserver){new ResizeObserver(sendSize).observe(document.documentElement)}',
        'window.addEventListener("load",sendSize);setTimeout(sendSize,60);setTimeout(sendSize,500);',
        'var CODE=' + safe + ';try{(0,eval)(CODE)}catch(e){send("error",[e.message])}sendSize();',
        '})();<\/scr' + 'ipt></body></html>'].join('');
    }

    var pgToken = 0;
    function pgRun(w) {
      var code = w.querySelector('.pg-code').value;
      var tpl = w.querySelector('template.pg-html');
      var iframe = w.querySelector('.pg-stage');
      var cons = w.querySelector('.pg-console');
      cons.innerHTML = '';
      iframe.style.height = '';
      iframe.srcdoc = pgSrcdoc(code, tpl ? tpl.innerHTML : '', ++pgToken);
    }

    window.addEventListener('message', function (e) {
      var d = e.data;
      if (!d || (d.__pg !== true && d.__pgsize !== true)) return;
      var frames = document.querySelectorAll('.pg-stage'), iframe = null;
      for (var i = 0; i < frames.length; i++) { if (frames[i].contentWindow === e.source) { iframe = frames[i]; break; } }
      if (!iframe) return;
      if (d.__pgsize === true) {
        if (!iframe.classList.contains('pg-hidden')) {
          iframe.style.height = Math.min(Math.max(d.height + 6, 40), 1400) + 'px';
        }
        return;
      }
      var cons = iframe.closest('.pg').querySelector('.pg-console');
      var line = document.createElement('div');
      line.className = 'pg-line pg-' + d.level;
      line.textContent = d.text;
      cons.appendChild(line);
      cons.scrollTop = cons.scrollHeight;
    });

    document.querySelectorAll('.pg').forEach(function (w) {
      var code = w.querySelector('.pg-code');
      var hl = w.querySelector('.pg-hl');
      w.querySelector('.pg-run').addEventListener('click', function () { pgRun(w); });
      var reset = w.querySelector('.pg-reset');
      if (reset) reset.addEventListener('click', function () {
        code.value = w.querySelector('.pg-initial').value;
        w.querySelector('.pg-console').innerHTML = '';
        var st = w.querySelector('.pg-stage');
        st.removeAttribute('srcdoc');
        st.style.height = '';
        pgHighlight(code);
        pgAutosize(code);
      });
      code.addEventListener('keydown', function (ev) {
        if (ev.key === 'Tab') {
          ev.preventDefault();
          var s = this.selectionStart, en = this.selectionEnd;
          this.value = this.value.slice(0, s) + '  ' + this.value.slice(en);
          this.selectionStart = this.selectionEnd = s + 2;
          pgHighlight(this);
        }
      });
      code.addEventListener('input', function () { pgHighlight(code); pgAutosize(code); });
      code.addEventListener('scroll', function () { hl.scrollTop = code.scrollTop; hl.scrollLeft = code.scrollLeft; });
      pgHighlight(code);
    });

    // Prism est chargé en defer : recolorer une fois prêt.
    window.addEventListener('load', function () {
      document.querySelectorAll('.pg-code').forEach(function (t) { pgHighlight(t); });
    });

    show(location.hash.slice(1) || pages[0].id);
  </script>
  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
    mermaid.initialize({ startOnLoad: false, theme: 'neutral', securityLevel: 'loose' });
    window.__renderMermaid = function (root) {
      var nodes = (root || document).querySelectorAll('.mermaid:not([data-processed])');
      if (nodes.length) mermaid.run({ nodes: nodes });
    };
    var vis = document.querySelector('.page:not([hidden])');
    window.__renderMermaid(vis || document);
  </script>
</body>
</html>
"""


if __name__ == "__main__":
    main()
