# Company page preview

Alternate marketing page for companies. It is a static preview on its own path. It is not the public homepage, and it is not a running experiment.

## Where it lives

- Path: `/business/` (`business/index.html`)
- Public URL after a merge to `main`: `https://getaimaestro.com/business/`
- This branch does not publish that URL. GitHub Pages for this repo serves `main` only. There is no preview workflow.

`/business/` does not collide with an existing page. GitHub Pages serves `business/index.html` at `/business/` because the site is already a static tree (`.nojekyll`, no build). `/next/` was not used. It reads like a product version.

The root homepage, `robots.txt`, `sitemap.xml`, and `partials/nav.html` are unchanged. This page is not in the sitemap and not in the site header. `scripts/sync-nav.py` only rewrites `*.html` at the repo root and `blog/*.html`, so it will not replace this header.

## How to read it locally

From the repository root:

```bash
python3 -m http.server
```

Open `http://127.0.0.1:8000/business/`.

Check links, the noindex policy, and that shared files are untouched:

```bash
python3 business/check.py
```

## Indexing

The page sets `noindex, nofollow` and a canonical URL of `https://getaimaestro.com/business/`. `robots.txt` is intentionally unchanged. A disallow there would stop crawlers from seeing the noindex tag. The page is omitted from `sitemap.xml` for the same reason: it should not be offered as a public URL yet.

## What the page is allowed to say

Companies are the customer. IT staff, advisers, and consultants are how a company evaluates and installs it. The page describes the current self-hosted MIT core and the paid remote companion, and it labels the managed company platform and customer-cloud implementation help as planned. It does not offer signup, provisioning, a partner directory, certification, SSO, RBAC, a compliance claim, or an SLA.

Facts are drawn from the product repository and from `https://aimaestro.sh/`. Agent programs do not have equal chat, status, or approval support. Provider processing, including memory consolidation, is stated separately from self-hosting. The page does not claim that all data stays on the machine. The MIT license, model and provider charges, machines, and the companion purchase are separate costs.

## Analytics already on the site

Existing pages load Google Tag Manager, container `GTM-W72WHGDW`, in the document head. The repository has no consent banner and no other analytics vendor. This preview does not load that container and does not send events. The `data-ab-*` attributes are inert hooks. `company.js` only writes the brief to the clipboard.

## If this later becomes a test

Do not randomize traffic onto this URL until the page is an approved candidate. A preview path is not an assignment.

Proposed events, not implemented:

- Primary, business intent: `business_handoff`. The visitor copies the evaluation brief, the action that prepares a forward to IT or an adviser. The hook is `data-ab-hook="business-handoff"` on the copy control.
- Secondary, technical evaluation: `technical_evaluation`. A click from this page to `aimaestro.sh` or to a linked product document. The hook is `data-ab-hook="technical-evaluation"`.
- Not a conversion: `see-workflow` and `open-brief`. Those only move the reader down this page.

Exposure, if a test is approved later:

- Assign a browser to control (today’s homepage) or this variant before render.
- Persist the assignment in a first-party cookie. Do not re-roll it on every visit.
- Keep a control. Do not send every visitor to `/business/`.
- Record only an event name, the variant id, and the timestamp the analytics tool already stores. Do not send the brief text, form fields, or a new identifier. This page has no form.
- The live site’s tag manager loads without a consent banner in this repo. Reusing it, or adding any vendor, needs an explicit decision. This page should stay free of tags until that decision.
- No sample size is proposed here. There is no baseline and no traffic measurement in this change.

## Type

Source Serif 4, Source Sans 3, and IBM Plex Mono are self-hosted from `business/fonts/` under the SIL Open Font License. License texts are in `business/fonts/licenses/`. Mono is used only for the install command and technical identifiers. The current site’s display face is not used. The constellation mark is the existing logo.
