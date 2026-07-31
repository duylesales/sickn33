# SEO/GEO Audit: onlyaijobs.eu

**Date:** July 31, 2026
**Auditor:** Automated SEO/GEO analysis (external, black-box)
**Target:** https://onlyaijobs.eu/

---

## Executive Summary

onlyaijobs.eu is currently **invisible to search engines, AI answer engines, and this audit's own tooling**. Every single URL tested on the domain — the homepage, `/robots.txt`, `/sitemap.xml`, `/llms.txt`, and `/favicon.ico` — is intercepted by a **BunkerWeb JavaScript proof-of-work bot challenge** before any real content is served. Search verification (`site:onlyaijobs.eu`) returns zero indexed pages, and brand-name searches across the open web return zero mentions of the site anywhere (LinkedIn, Product Hunt, press, forums). This is not a ranking or content-quality problem; it is a **crawlability blackout** that sits upstream of every other SEO/GEO factor. No amount of on-page optimization will matter until this is fixed, because Google, Bing, and LLM crawlers (GPTBot, ClaudeBot, PerplexityBot, etc.) cannot get past the challenge page to read a single sentence of real content.

Because of this, this report cannot evaluate on-page SEO (titles, headings, content depth, schema markup) or true GEO readiness (structured data, E-E-A-T signals) from direct observation — that entire layer of the site is currently unreachable by automated agents, which is itself the headline finding. Everything below is evidence-based, drawn from raw HTTP responses, DNS/TLS records, and external search verification.

**Overall verdict: 🔴 Critical — the site is functionally unindexable in its current configuration.**

---

## Methodology & Limitations

This audit relied entirely on external, unauthenticated tooling — no access to Google Search Console, analytics, or the site's own admin panel was available. Methods used:

1. Direct HTTP requests (`curl`) to the homepage and key crawler-facing files, inspecting status codes, headers, and body content.
2. An automated markdown-rendering fetch tool (equivalent to how many LLM-based browsing tools operate).
3. DNS resolution (`dig`) and TLS certificate inspection (`openssl s_client`) for infrastructure context.
4. `whois` lookup for domain registration context (limited by `.eu` TLD privacy — EURid does not expose registrant details publicly).
5. Web search verification (`site:` operator and brand-name queries) to check indexation and off-page mentions.
6. Wayback Machine / archive.org lookups, to check for any historically archived version of the site.

**Important limitation:** because the site blocks automated access uniformly, this report cannot describe what a human visitor sees in a real browser (where the JS challenge resolves after a few seconds and the real page loads). The findings below describe what **every non-browser crawler and bot** — including the search and AI crawlers this audit is meant to optimize for — actually experiences.

---

## Critical Finding #1: Total Crawler Lockout via BunkerWeb Challenge

Every URL tested returns either a redirect into, or the body of, a bot-detection interstitial:

| URL | Result |
|---|---|
| `https://onlyaijobs.eu/` | `302` → `/challenge`, then `200` serving a JS proof-of-work "Bot Detection" page (not site content) |
| `https://onlyaijobs.eu/robots.txt` | `302 Found` (redirected into the challenge flow instead of serving the file) |
| `https://onlyaijobs.eu/sitemap.xml` | `302 Found` (same) |
| `https://onlyaijobs.eu/llms.txt` | `302 Found` (same) |
| `https://onlyaijobs.eu/favicon.ico` | `302 Found` (same) |

The challenge page itself is served by **BunkerWeb** (an open-source WAF/reverse-proxy), and its HTML is explicit about intent:

- `<title>Bot Detection</title>`
- `<meta name="description" content="Please wait while we check if you are a Human">`
- `<meta name="robots" content="nofollow,noarchive,noindex">`
- A hidden form that computes a SHA-256 proof-of-work nonce client-side via JavaScript and POSTs it to `/challenge` before the real page is released
- Footer: "Protected by BunkerWeb"

**Why this is critical, not cosmetic:**

- **Googlebot, Bingbot, GPTBot, ClaudeBot, PerplexityBot, and virtually every other crawler do not execute this kind of client-side proof-of-work JavaScript the way a real browser does**, and even when a crawler *can* run JS (Googlebot can, in a delayed second wave), proof-of-work / CAPTCHA-style challenges are specifically designed to filter out non-human, non-interactive clients — which is exactly what every search and AI crawler is.
- `robots.txt` and `sitemap.xml` are supposed to be served **unconditionally, with no redirects or challenges**, per the robots exclusion protocol. Search engines that can't fetch `robots.txt` cleanly will either assume the most conservative (block-everything) interpretation or simply deprioritize/distrust the domain's crawl budget.
- The challenge page's own `<meta name="robots" content="nofollow,noarchive,noindex">` tag means that even in the rare case a crawler's request is treated as "successful," what gets indexed is a `noindex` interstitial — i.e., **explicitly telling search engines not to index the only page they can actually see.**
- `llms.txt` — the emerging convention for signaling AI/LLM crawlers what content to ingest — is also gated behind the same wall, so even a well-behaved AI crawler respecting that convention cannot read it.

This single misconfiguration (the WAF's crawler/bot rule set is not allow-listing known good search and AI bots, and is not exempting `robots.txt`/`sitemap.xml`/`llms.txt` from the challenge) is sufficient on its own to explain every downstream symptom found in this audit.

---

## Critical Finding #2: Zero Search Index Presence

A `site:onlyaijobs.eu` query and multiple brand-name searches (`"OnlyAIJobs" AI jobs board`, `onlyaijobs.eu LinkedIn`, `onlyaijobs.eu Product Hunt`) returned **zero results from the domain itself** across all queries. All returned results were unrelated third-party job boards (aijobs.ai, aijobs.com, theaijobboard.com, jobforagent.com, EU-run job portals like EURES) — competitors and adjacent sites, never onlyaijobs.eu.

This is consistent with, and directly explained by, Finding #1: if crawlers cannot get past the bot challenge, there is nothing for them to index. It is not (based on available evidence) a penalty, manual action, or content-quality issue — it looks like a site that has never been successfully crawled.

**Wayback Machine check:** Attempts to check archive.org for historical snapshots were inconclusive (repeated timeouts/connection errors from this environment). This is not strong evidence either way, but combined with the zero-index finding, there is no confirmed evidence the site has ever been crawled and archived by any third party.

---

## Infrastructure & Technical Context

Findings unrelated to the bot wall, gathered via DNS/TLS inspection:

| Item | Value |
|---|---|
| A record | `136.243.57.57` (Hetzner-range IP) |
| `www` subdomain | CNAMEs to apex, resolves to the same IP |
| Nameservers | `ns1/ns2/ns3.digitalocean.com` |
| TLS certificate | Let's Encrypt, issued **June 10, 2026**, expires **September 8, 2026** (standard 90-day cert) |
| TLD registry | `.eu`, registered via EURid (registrant details are privacy-protected by default under EURid policy — not retrievable via public WHOIS) |
| HTTP/3 | Advertised via `alt-svc: h3` header |
| Security headers observed on the challenge response | HSTS, `x-frame-options: SAMEORIGIN`, `x-content-type-options: nosniff`, `referrer-policy: no-referrer-when-downgrade`, nonce-based CSP |

The June 2026 certificate issuance date suggests the current deployment is fairly recent (a re-issued 90-day Let's Encrypt cert doesn't prove the site's true launch date, but it's consistent with the "never indexed" finding — this may simply be a new or recently-relaunched project that hasn't had crawlers reach it yet). Security header hygiene (HSTS, CSP, nosniff, frame-options) is otherwise solid, which suggests a reasonably competent infrastructure setup — the crawler-blocking issue looks like an overly aggressive default WAF bot-fight-mode setting, not general neglect.

---

## On-Page SEO — Unable to Assess

Because every automated fetch (including this audit's own tooling) is served the challenge page instead of real content, none of the following could be evaluated directly and should be checked manually via a real browser or Google Search Console:

- Title tags / meta descriptions on real pages
- Heading structure (H1/H2 hierarchy)
- Content depth and quality on job listings, about/contact pages
- Internal linking structure
- Structured data (`JobPosting` schema.org markup is the single highest-leverage schema type for a jobs site, and critical for Google Jobs rich results — cannot confirm presence or absence)
- Image alt text, Core Web Vitals, mobile rendering

**This absence of data is itself the finding**: an SEO/GEO audit — whether run by a human consultant, an automated tool, Google's own systems, or an AI assistant a job-seeker asks "find me AI jobs in Europe" — hits the identical wall. If this report's tooling can't see the content, neither can the systems that are supposed to surface it to users.

---

## GEO (AI/LLM Discoverability) Assessment

GEO readiness depends on content being both crawlable and structured for extraction by LLM-based answer engines (ChatGPT browsing, Perplexity, Claude, Google AI Overviews). Findings:

- **`llms.txt` is present as a route but unreachable** — it 302-redirects into the same challenge, so even AI crawlers specifically looking for this convention are blocked.
- **No known AI crawler allow-listing detected.** BunkerWeb (and WAFs generally) typically require an explicit bot allow-list (by user-agent and/or verified reverse-DNS/IP ranges) for Googlebot, Bingbot, GPTBot, ClaudeBot, PerplexityBot, and CCBot. Nothing in the observed behavior suggests this has been configured — all requests, including plain `curl`, hit the same wall a malicious scraper would.
- **Zero brand presence to anchor GEO answers.** GEO also benefits heavily from off-site brand signals (being cited, linked, or discussed elsewhere) so that LLMs encounter the brand even without crawling the site directly. No such mentions were found anywhere in this audit.

---

## Prioritized Recommendations

**P0 — Fix immediately (blocks everything else):**
1. In the BunkerWeb configuration, add an allow-list exemption for verified search/AI crawler user-agents and IP ranges (Googlebot, Bingbot, GPTBot, ClaudeBot, PerplexityBot, CCBot, at minimum) so they bypass the JS/proof-of-work challenge entirely.
2. Explicitly exclude `/robots.txt`, `/sitemap.xml`, `/llms.txt`, and `/favicon.ico` from the bot-challenge rule set — these must always return `200` with real content, unconditionally, regardless of client.
3. Remove or scope the `noindex,nofollow,noarchive` robots meta tag so it only applies to the challenge/interstitial route itself, never leaks onto real content pages.

**P1 — Once crawlable, verify:**
4. Confirm `robots.txt` doesn't itself disallow crawling once it's actually reachable.
5. Submit `sitemap.xml` via Google Search Console and Bing Webmaster Tools once confirmed reachable, and request indexing.
6. Add `JobPosting` structured data (schema.org) to every job listing page — this is the single highest-impact SEO action for a jobs site, enabling Google for Jobs rich results.
7. Verify `llms.txt` content is actually useful once reachable (should point AI crawlers to key pages/content, not just exist as a stub).

**P2 — Build discoverability once the wall is down:**
8. Establish basic off-site presence (LinkedIn company page, a Product Hunt or directory listing, a few backlinks) — currently there is zero external footprint to anchor either traditional search or AI-answer-engine citations.
9. Re-run a full on-page audit (titles, headings, content depth, internal linking, Core Web Vitals) once real content is reachable by automated tools — this report could not evaluate any of that layer.

---

## Appendix: Raw Evidence Summary

- `curl -D - https://onlyaijobs.eu/ -L` → `302` to `/challenge`, then `200` serving BunkerWeb "Bot Detection" interstitial (saved locally during this audit for reference).
- `curl -o /dev/null -w "%{http_code}" https://onlyaijobs.eu/robots.txt` → `302`
- `curl -o /dev/null -w "%{http_code}" https://onlyaijobs.eu/sitemap.xml` → `302`
- `curl -o /dev/null -w "%{http_code}" https://onlyaijobs.eu/llms.txt` → `302`
- `curl -o /dev/null -w "%{http_code}" https://onlyaijobs.eu/favicon.ico` → `302`
- WebFetch (markdown-rendering fetch tool) on homepage → `HTTP 429 Too Many Requests` (consistent with active bot-mitigation/rate-limiting, not a one-off fluke)
- `site:onlyaijobs.eu` search → 0 results from the domain
- `"OnlyAIJobs" AI jobs board` search → 0 results from the domain; only competitor job boards
- `onlyaijobs.eu LinkedIn` search → 0 results
- `onlyaijobs.eu Product Hunt` search → 0 results
- `dig onlyaijobs.eu A` → `136.243.57.57`; NS on `digitalocean.com`
- TLS cert → Let's Encrypt, issued 2026-06-10, expires 2026-09-08
- `whois onlyaijobs.eu` → registrant details privacy-protected by EURid (standard for `.eu` domains)
- archive.org / Wayback Machine lookups → inconclusive (timeouts/connection errors from this audit environment; no confirmed historical snapshot found)

---

*This audit was conducted externally and automatically, without access to the site owner's analytics, Search Console, or CMS. All findings reflect what public, unauthenticated crawlers and tools experience when reaching onlyaijobs.eu — which is the same experience Google, Bing, and AI crawlers currently have.*
