import json
from pathlib import Path
from html import escape

ROOT = Path(__file__).parent
SITE = "https://foridahmed3834-byte.github.io/My-website"
posts = json.loads((ROOT/"posts.json").read_text(encoding="utf-8"))

def make_page(p):
    title = escape(p["title"], quote=True)
    desc = escape(p["description"], quote=True)
    url = f"{SITE}/blog-post-{p['id']}.html"
    image = f"{SITE}/{p['image']}"
    return f"""<!doctype html>
<html lang="bn"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{image}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Forid Ahmed">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{image}">
<link rel="stylesheet" href="style.css"></head>
<body>
<header><div class="container"><nav><a class="brand" href="index.html">Forid Ahmed</a>
<a href="index.html">সব Blog</a></nav></div></header>
<main class="container"><article>
<img class="cover" src="{p["image"]}" alt="{title}" onerror="this.style.display='none'">
<h1>{title}</h1><div class="date">Published: {p["date"]}</div>
<div class="content">{p["content"]}</div>
<div class="actions"><a class="btn" href="index.html">← সব Blog</a>
<a class="btn" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u={url}">Facebook Share</a></div>
</article></main><footer>© Forid Ahmed</footer></body></html>"""

for p in posts:
    (ROOT/f"blog-post-{p['id']}.html").write_text(make_page(p), encoding="utf-8")

print(f"Done: {len(posts)} blog pages generated.")
