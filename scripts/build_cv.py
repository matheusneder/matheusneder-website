#!/usr/bin/env python3
"""Build the published /cv/ folder from the Markdown CVs in cv/.

For every cv/*.md, writes into the output folder (default: _site/cv):

- a copy of the Markdown file;
- a PDF of it (A4, site fonts embedded), printed by headless Chrome,
  Chromium or Edge;

and then an index.html that lists every file in the folder, because
GitHub Pages has no directory listing of its own.

Requires the packages in scripts/requirements-cv.txt and a Chromium-based
browser. Set CHROME to the browser executable to choose one.

Usage: python scripts/build_cv.py [OUTPUT_DIR]
"""
import argparse
import base64
import html
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import quote

import markdown
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "cv"
FONTS = ROOT / "assets" / "fonts"
DEFAULT_OUT = ROOT / "_site" / "cv"

# File name suffix -> (html lang, document title suffix).
LANGS = {
    "pt": ("pt-BR", "Currículo"),
    "en": ("en", "Curriculum Vitae"),
}

# Static weights cut from the site's variable fonts: Chrome embeds variable
# fonts in PDFs as Type3 outlines, which text extraction (ATS) handles poorly.
FONT_WEIGHTS = (
    ("Inter", "inter-latin-wght.woff2", (400, 600)),
    ("Manrope", "manrope-latin-wght.woff2", (700, 800)),
)
WEIGHT_NAMES = {400: "Regular", 600: "SemiBold", 700: "Bold", 800: "ExtraBold"}

BROWSERS = (
    "google-chrome", "google-chrome-stable", "chromium", "chromium-browser",
    "chrome", "msedge", "microsoft-edge",
)
BROWSER_PATHS = (
    r"%ProgramFiles%\Google\Chrome\Application\chrome.exe",
    r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe",
    r"%LocalAppData%\Google\Chrome\Application\chrome.exe",
    r"%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe",
    r"%ProgramFiles%\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
)

# Print style: same fonts and accent colour as the site (assets/css/main.css).
CSS = """
@page { size: A4; margin: 15mm 17mm; }
:root { --text: #1c1e21; --muted: #565b62; --accent: #1f5f5b; }
html { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
body { margin: 0; color: var(--text); font: 9.5pt/1.45 "Inter", system-ui, sans-serif; }
h1, h2, h3 { font-family: "Manrope", "Inter", sans-serif; line-height: 1.2; break-after: avoid; }
h1 { margin: 0 0 3pt; font-size: 22pt; font-weight: 800; color: var(--accent); letter-spacing: -0.01em; }
h1 + p { margin: 0 0 5pt; color: var(--muted); }
h1 + ul, h1 + p + ul { display: flex; flex-wrap: wrap; gap: 1pt 14pt; margin: 0; padding: 0; list-style: none; }
h1 + ul li, h1 + p + ul li { margin: 0; }
h2 { margin: 14pt 0 6pt; padding-bottom: 3pt; border-bottom: 1.2pt solid var(--accent);
     font-size: 11pt; font-weight: 700; color: var(--accent); text-transform: uppercase; letter-spacing: 0.06em; }
h3 { margin: 10pt 0 1pt; font-size: 10.5pt; font-weight: 700; }
h2 + h3 { margin-top: 0; }
h3 + p { margin-top: 0; color: var(--muted); break-after: avoid; }
p { margin: 0 0 5pt; orphans: 2; widows: 2; }
ul { margin: 0 0 6pt; padding-left: 13pt; }
li { margin: 0 0 2pt; break-inside: avoid; }
li::marker { color: var(--accent); }
strong { font-weight: 600; }
a { color: var(--accent); text-decoration: none; }
"""

CV_PAGE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>{fonts}{css}</style>
</head>
<body>
{body}
</body>
</html>
"""

INDEX_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light dark">
  <title>Index of /cv/</title>
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <style>
    :root {{
      color-scheme: light dark;
      --bg: light-dark(#f7f6f2, #121416);
      --text: light-dark(#1c1e21, #e9e7e2);
      --muted: light-dark(#565b62, #a4a9af);
      --line: light-dark(#e1ded6, #2b2f34);
      --accent: light-dark(#1f5f5b, #7fc4ba);
    }}
    body {{ margin: 0; padding: 2rem 1.25rem; background: var(--bg); color: var(--text);
           font: 1rem/1.5 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; }}
    main {{ max-width: 44rem; margin: 0 auto; }}
    h1 {{ margin: 0 0 1rem; font-size: 1.25rem; font-weight: 600; }}
    table {{ width: 100%; border-collapse: collapse; font-variant-numeric: tabular-nums; }}
    th, td {{ padding: 0.5rem 0.75rem; border-bottom: 1px solid var(--line); text-align: left; }}
    th {{ color: var(--muted); font-size: 0.875rem; font-weight: 600; }}
    .size {{ text-align: right; white-space: nowrap; color: var(--muted); }}
    a {{ color: var(--accent); }}
  </style>
</head>
<body>
  <main>
    <h1>Index of /cv/</h1>
    <table>
      <thead><tr><th>Name</th><th class="size">Size</th></tr></thead>
      <tbody>
        <tr><td><a href="../">../</a></td><td class="size">-</td></tr>
{rows}
      </tbody>
    </table>
  </main>
</body>
</html>
"""


def font_faces():
    css = []
    for family, file, weights in FONT_WEIGHTS:
        for weight in weights:
            font = instantiateVariableFont(TTFont(FONTS / file), {"wght": weight})
            font.flavor = None
            # PostScript name: what PDF viewers show in the font list.
            font["name"].removeNames(nameID=6)
            font["name"].setName(f"{family}-{WEIGHT_NAMES[weight]}", 6, 3, 1, 0x409)
            buf = io.BytesIO()
            font.save(buf)
            # Inlined: a file:// page cannot load file:// fonts (CORS).
            data = base64.b64encode(buf.getvalue()).decode("ascii")
            css.append(f'@font-face {{ font-family: "{family}"; font-weight: {weight}; '
                       f'src: url(data:font/ttf;base64,{data}) format("truetype"); }}')
    return "\n".join(css)


def find_browser():
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    for name in BROWSERS:
        if path := shutil.which(name):
            return path
    for candidate in BROWSER_PATHS:
        path = Path(os.path.expandvars(candidate))
        if "%" not in str(path) and path.is_file():
            return str(path)
    sys.exit("No Chrome, Chromium or Edge found; set CHROME to the browser executable.")


def render_html(md_file, fonts):
    text = md_file.read_text(encoding="utf-8")
    suffix = md_file.stem.rsplit("-", 1)[-1]
    lang, label = LANGS.get(suffix, LANGS["pt"])
    heading = re.search(r"^#\s+(.+?)\s*$", text, re.M)
    title = f"{heading.group(1)} - {label}" if heading else md_file.stem
    body = markdown.markdown(text, extensions=["extra", "sane_lists"])
    return CV_PAGE.format(lang=lang, title=html.escape(title), fonts=fonts, css=CSS, body=body)


def print_pdf(browser, page, pdf, profile):
    pdf.unlink(missing_ok=True)
    cmd = [
        browser, "--headless", "--disable-gpu", "--no-first-run", "--no-default-browser-check",
        "--disable-extensions", f"--user-data-dir={profile}",
        "--no-pdf-header-footer", f"--print-to-pdf={pdf}", page.as_uri(),
    ]
    if os.environ.get("CI"):
        # CI runners may block Chrome's sandbox; the page is our own local file.
        cmd.insert(1, "--no-sandbox")
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if not pdf.is_file() or pdf.read_bytes()[:5] != b"%PDF-":
        sys.exit(f"Failed to print {pdf.name} (exit {result.returncode}):\n{result.stderr}")


def human_size(n):
    for unit in ("B", "KB", "MB"):
        if n < 1024 or unit == "MB":
            return f"{n} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024


def write_index(out):
    rows = []
    for f in sorted(out.iterdir()):
        if f.is_file() and f.name != "index.html":
            name = html.escape(f.name)
            rows.append(f'        <tr><td><a href="{quote(f.name)}">{name}</a></td>'
                        f'<td class="size">{human_size(f.stat().st_size)}</td></tr>')
    (out / "index.html").write_text(INDEX_PAGE.format(rows="\n".join(rows)), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("out", nargs="?", type=Path, default=DEFAULT_OUT,
                        help="output folder (default: _site/cv)")
    out = parser.parse_args().out.resolve()
    if out == SRC.resolve():
        sys.exit("The output folder must not be the source folder cv/.")

    sources = sorted(SRC.glob("*.md"))
    if not sources:
        sys.exit(f"No Markdown files in {SRC}.")
    out.mkdir(parents=True, exist_ok=True)
    browser, fonts = find_browser(), font_faces()

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for md_file in sources:
            shutil.copyfile(md_file, out / md_file.name)
            page = tmp / f"{md_file.stem}.html"
            page.write_text(render_html(md_file, fonts), encoding="utf-8")
            pdf = out / f"{md_file.stem}.pdf"
            print_pdf(browser, page, pdf, tmp / "profile")
            print(f"{md_file.relative_to(ROOT)} -> {pdf}")
    write_index(out)
    print(f"Listing -> {out / 'index.html'}")


if __name__ == "__main__":
    main()
