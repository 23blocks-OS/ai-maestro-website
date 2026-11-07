# AI Maestro website

The marketing site of [AI Maestro](https://github.com/23blocks-OS/ai-maestro), served at **https://getaimaestro.com**: the home page, the iPhone app, vision, ecosystem, experiments and the blog.

The product site is separate. Install and documentation live at **https://aimaestro.sh**, served from `docs/` of the product repo (`curl -fsSL aimaestro.sh/install | bash` installs AI Maestro). Links from here to a docs page are absolute `https://aimaestro.sh/<page>.html` URLs, and "Get started" points there.

Static HTML (no build step): each page is a file at the root, with `blog/`, `images/` and `videos/` beside them. GitHub Pages serves `main` at `/`, and `CNAME` holds the domain. `.nojekyll` keeps Pages from running Jekyll.

## Editing

Edit the HTML, preview with any static server (`python3 -m http.server`), and open a pull request. A merge to `main` goes live in a minute or two. Add new pages to `sitemap.xml`, and new blog posts to `blog/index.html` and `blog/feed.xml`.

The header is the same on every page. Change it in `partials/nav.html`, then run `python3 scripts/sync-nav.py` to write it into every page (`--check` only reports pages that differ). A new page gets it on the next run, as long as it has a `<nav>` element.

Website changes do not need an AI Maestro release. A new docs page goes in the product repo, not here.

## History

Until November 2026 the whole site, marketing and docs, lived in `docs/` of the product repo at ai-maestro.23blocks.com. That domain now serves a small redirect site that sends each old page to its new home on getaimaestro.com or aimaestro.sh.
