# Tejas — Portfolio

Single-file site: `index.html` (v9.3 — liquid type hero, factory canvas, repos glass ring, light/dark themes).

**Live:** https://tejs2005.github.io/portfolio/

## Rules

- `git commit` + a `snapshots/vN-*.html` copy **before** every major change.
- Deploy is GitHub Pages on `Tejs2005/portfolio`, branch `master`, no build step.
  Push and it rebuilds in ~45 s.

## Custom domain — read this before touching `CNAME`

The site was unreachable for a while because `CNAME` was committed **before** the
domain existed. GitHub Pages treats a committed `CNAME` as authoritative immediately:
it starts redirecting the repo's own Pages URL to that domain, with no verification
and no warning. The domain did not resolve, so every URL 301'd to a
domain-for-sale page.

So the order is fixed:

1. Registration PR is merged on [`is-a-dev/register`](https://github.com/is-a-dev/register)
   (tracking PR: #60962, `domains/tejasz.json`).
2. Confirm it actually resolves:
   ```bash
   dig +short tejasz.is-a.dev                                          # want Tejs2005.github.io.
   curl -sS -o /dev/null -w '%{http_code}\n' https://tejasz.is-a.dev/  # want 200
   ```
3. **Only then** add `CNAME` containing `tejasz.is-a.dev`, commit, push, and tick
   *Enforce HTTPS* in Settings → Pages.
4. Then flip `canonical` / `og:url` / `og:image` / `twitter:image` in `index.html`
   from `tejs2005.github.io/portfolio/` to `https://tejasz.is-a.dev/`.

Until step 2 passes, `CNAME` must **not** exist in this repo. A 302 on
`tejasz.is-a.dev` is the expected answer before merge, not a failure.

Diagnosis shortcut if the site ever goes down while Pages reports `built`:
`git log -- CNAME` first, not the build log.

## Social card

`og-image.png` (1200×630) is generated, not designed by hand — it is composed in the
site's own light palette (`#f7f3ea` ground, `#171b1f` ink, `#b8360a` accent,
`#0e9d6e` live dot). The render script is deliberately **not** in this repo
(see commit `dc904f1`, path hygiene); only the PNG is tracked. Regenerate it if the
hero copy changes.
