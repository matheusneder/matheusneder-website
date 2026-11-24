#!/usr/bin/env python3
"""Sanity checks for the static site (no dependencies).

- every local href/src/srcset reference in the HTML files resolves to a file
- sitemap.xml is well-formed XML
- CNAME contains exactly the expected custom domain
"""
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "matheusneder.com"
errors = []


class Refs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []

    def handle_starttag(self, tag, attrs):
        for k, v in attrs:
            if not v:
                continue
            if k in ("href", "src"):
                self.refs.append(v)
            elif k == "srcset":
                self.refs += [p.split()[0] for p in v.split(",") if p.strip()]


def is_local(ref):
    u = urlparse(ref)
    return not u.scheme and not u.netloc and not ref.startswith(("#", "//", "mailto:", "tel:", "data:"))


for page in sorted(ROOT.glob("**/*.html")):
    if any(p in page.relative_to(ROOT).parts for p in (".git", ".claude", "_site")):
        continue
    parser = Refs()
    parser.feed(page.read_text(encoding="utf-8"))
    for ref in parser.refs:
        if not is_local(ref):
            continue
        path = unquote(urlparse(ref).path)
        base = ROOT if path.startswith("/") else page.parent
        target = (base / path.lstrip("/")).resolve()
        if target.is_dir():
            target = target / "index.html"
        if not target.exists():
            errors.append(f"{page.relative_to(ROOT)}: broken reference '{ref}'")

try:
    ET.parse(ROOT / "sitemap.xml")
except Exception as e:  # noqa: BLE001
    errors.append(f"sitemap.xml: {e}")

cname = (ROOT / "CNAME").read_text(encoding="utf-8").strip() if (ROOT / "CNAME").exists() else None
if cname != DOMAIN:
    errors.append(f"CNAME must contain '{DOMAIN}', found {cname!r}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("Site checks passed.")
