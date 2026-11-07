#!/usr/bin/env python3
"""Checks for the /business/ preview. Run from the repository root:

    python3 business/check.py

Exits 1 on a structural or link failure. Network checks can be skipped with
--local.
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE = ROOT / "business" / "index.html"
HTML = PAGE.read_text(encoding="utf-8")
LOCAL = "--local" in sys.argv
errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


require("noindex, nofollow" in HTML, "missing noindex, nofollow")
require(
    'rel="canonical" href="https://getaimaestro.com/business/"' in HTML,
    "canonical must be the business path, not the homepage",
)
require(HTML.count("<h1") == 1, "expected exactly one h1")
require("<main" in HTML and "<header" in HTML and "<footer" in HTML and "<nav" in HTML, "missing a landmark")
require('href="#content"' in HTML, "missing skip target")

forbidden = [
    "googletagmanager",
    "google-analytics",
    "gtag(",
    "GTM-",
    "plausible",
    "posthog",
    "segment.com",
    "hotjar",
    "facebook.net",
    "fonts.googleapis.com",
    "cdn.tailwindcss.com",
    "gsap",
    "syne",
    "DM Sans",
    "JetBrains Mono",
]
lower = HTML.lower()
for token in forbidden:
    if token.lower() in lower:
        fail(f"page contains forbidden token: {token}")

require('data-ab-hook="business-handoff"' in HTML, "missing primary handoff hook")
require('data-ab-hook="technical-evaluation"' in HTML, "missing technical evaluation hook")
require("fetch(" not in HTML and "XMLHttpRequest" not in HTML, "page should not start a request")
require("navigator.sendBeacon" not in HTML, "page should not beacon")

js = (ROOT / "business" / "company.js").read_text(encoding="utf-8")
require("fetch(" not in js and "sendBeacon" not in js, "script should stay local")
require("clipboard" in js, "copy control should use the clipboard")

for tag in re.findall(r"<img\b[^>]*>", HTML):
    if "alt=" not in tag:
        fail(f"image missing alt: {tag[:80]}")
for tag in re.findall(r"<button\b[^>]*>", HTML):
    if 'type="button"' not in tag:
        fail(f"button missing type: {tag[:80]}")

hrefs = re.findall(r'(?:href|src)="([^"]+)"', HTML)
for ref in hrefs:
    if ref.startswith(("mailto:", "javascript:", "#")):
        if ref.startswith("javascript:"):
            fail(f"script URL: {ref}")
        continue
    if ref.startswith(("http://", "https://")):
        continue
    if ref.startswith("/"):
        relative = ref.lstrip("/")
        path = (ROOT / relative).resolve() if relative else ROOT / "index.html"
    else:
        path = (PAGE.parent / ref).resolve()
    if not path.exists():
        fail(f"missing local file: {ref}")

shared = [
    "index.html",
    "robots.txt",
    "sitemap.xml",
    "partials/nav.html",
    "scripts/sync-nav.py",
    "CNAME",
]
diff = subprocess.run(
    ["git", "diff", "--exit-code", "origin/main", "--", *shared],
    cwd=ROOT,
    capture_output=True,
    text=True,
)
if diff.returncode != 0:
    fail("shared files differ from origin/main:\n" + (diff.stdout or diff.stderr))

if not LOCAL:
    external = sorted(set(re.findall(r'href="(https?://[^"]+)"', HTML)))
    agent = "AIMaestroPreviewCheck/1.0"
    for url in external:
        request = urllib.request.Request(url, method="GET", headers={"User-Agent": agent})
        try:
            with urllib.request.urlopen(request, timeout=25) as response:
                status = response.status
                response.read(256)
        except urllib.error.HTTPError as exc:
            status = exc.code
        except Exception as exc:  # noqa: BLE001 - report and continue
            fail(f"link failed {url}: {exc}")
            continue
        if status >= 400:
            # The canonical preview URL is the path this change adds. It 404s
            # until a merge to main. Every other link must already resolve.
            if status == 404 and url.rstrip("/") == "https://getaimaestro.com/business":
                print("note: preview URL is not live yet (expected before merge)")
                continue
            fail(f"link {status} {url}")

if errors:
    print(f"{len(errors)} problem(s):")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)

print("business preview checks passed")
