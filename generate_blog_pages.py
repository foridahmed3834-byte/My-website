import json, html
from pathlib import Path

ROOT=Path(__file__).parent
SITE="https://foridahmed3834-byte.github.io/My-website"
posts=json.loads((ROOT/"posts.json").read_text(encoding="utf-8"))

CSS='body{margin:0;background:#f3f6f2;color:#16241d;font-family:Arial,"Noto Sans Bengali",sans-serif;line-height:1.8}\n.top{background:#0b3d2e;color:#fff;padding:18px}.nav{max-width:920px;margin:auto;display:flex;justify-content:space-between}.nav a{color:#fff;text-decoration:none;font-weight:700}\n.wrap{max-width:920px;margin:auto;padding:25px 16px 60px}.post{background:#fff;border-radius:16px;padding:28px;box-shadow:0 8px 24px #0002}.cover{width:100%;max-height:480px;object-fit:cover;border-radius:12px}\n.date{color:#a67c2f;font-size:13px}.post h1{font-size:clamp(28px,5vw,44px);line-height:1.25;color:#0b3d2e}.body{font-size:18px;color:#51625a}\n.actions{display:flex;flex-wrap:wrap;gap:10px;border-top:1px solid #e1e8e2;margin-top:28px;padding-top:18px}.btn{display:inline-block;text-decoration:none;border:0;border-radius:999px;padding:9px 16px;background:#0b3d2e;color:#fff;cursor:pointer}.fb{background:#1877f2}\nfooter{text-align:center;background:#0b3d2e;color:#fff;padding:22px}'

for p in posts:
    title=html.escape(p["title"],quote=True)
    desc=html.escape(p["description"],quote=True)
    url=f"{SITE}/blog-post-{p['id']}.html"
    image=f"{SITE}/{p['image']}"
    local=html.escape(p["image"],quote=True)
    fb=html.escape("https://www.facebook.com/sharer/sharer.php?u="+url,quote=True)
    content=p.get("content","")
    page=f'''<!doctype html><html lang="bn"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:image" content="{image}"><meta property="og:url" content="{url}">
<meta property="og:type" content="article"><meta property="og:site_name" content="Forid Ahmed">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{image}">
<style>{{CSS}}</style></head><body>
<header class="top"><div class="nav"><a href="index.html">Forid Ahmed</a><a href="blog.html">সব Blog</a></div></header>
<main class="wrap"><article class="post"><img class="cover" src="{local}" alt="{title}">
<div class="date">Published on {html.escape(p["date"])}</div><h1>{title}</h1><div class="body">{content}</div>
<div class="actions"><a class="btn" href="blog.html">← সব Blog</a><a class="btn fb" target="_blank" href="{fb}">Facebook Share</a>
<button class="btn" onclick="navigator.clipboard.writeText(location.href)">Copy Link</button></div></article></main>
<footer>© Forid Ahmed</footer></body></html>'''
    (ROOT/f"blog-post-{p['id']}.html").write_text(page,encoding="utf-8")

print(f"Generated {len(posts)} blog pages.")
