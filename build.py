#!/usr/bin/env python3
"""Baut die Web-App (index.html) aus app.html.

app.html ist die gemeinsame Quelle: Sie wird so wie sie ist als Claude-Artifact
veröffentlicht. index.html bekommt zusätzlich einen vollständigen <head> mit
Manifest, Icons und Service Worker, damit die App installierbar und offline nutzbar ist.
Aufruf: python3 build.py
"""
import hashlib
import pathlib
import re

root = pathlib.Path(__file__).parent
body = (root / "app.html").read_text(encoding="utf-8")

title = re.search(r"<title>(.*?)</title>", body).group(1)
body = re.sub(r"<title>.*?</title>\n?", "", body, count=1)
body = re.sub(r'<meta name="claude:viewport-fit-sides"[^>]*>\n?', "", body, count=1)

head = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="Gehalt, Ausgaben und ETF-Sparplan in Vier-Monats-Fenstern planen.">
<meta name="theme-color" content="#000000">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Finanzplan">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/icon-192.png" type="image/png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<style>
:root {{ padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); }}
html, body {{ margin: 0; }}
img {{ max-width: 100%; }}
[hidden] {{ display: none !important; }}
</style>
</head>
<body>
"""

tail = """
<script>
if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(() => {}));
}
</script>
</body>
</html>
"""

html = head + body + tail
(root / "index.html").write_text(html, encoding="utf-8")

# Cache-Version an den Inhalt koppeln, damit Updates sicher ankommen
version = hashlib.sha1(html.encode()).hexdigest()[:10]
sw = (root / "sw.template.js").read_text(encoding="utf-8").replace("__VERSION__", version)
(root / "sw.js").write_text(sw, encoding="utf-8")
print(f"index.html und sw.js gebaut (Version {version})")
