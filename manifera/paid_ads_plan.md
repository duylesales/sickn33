# Manifera — Paid Advertising Plan (Multi-Channel, Execution-Ready)

**Property:** manifera.com (English-only)
**Prepared:** 8 September 2026
**Companion documents:** [`google_ads_keywords_manifera.md`](./google_ads_keywords_manifera.md) · [`google_ads_rsa_copy_manifera.md`](./google_ads_rsa_copy_manifera.md) · [`seo_geo_plan_vendor_keywords.md`](./seo_geo_plan_vendor_keywords.md) · [`implementation_plan.md`](./implementation_plan.md)
**Source data:** `keyword-planner-manifera.com-2026-06-12 (1).csv` (1,595 keywords) · [`manifera_info.md`](./manifera_info.md) · [`seo-geo-audit-manifera-com.md`](./seo-geo-audit-manifera-com.md) · content library of 1,460 English articles

---

## 1. Executive Summary

Manifera sells a high-consideration, high-value service: dedicated offshore engineering teams governed from Amsterdam. A single closed deal is worth €60,000+ over its first year. That economics permits expensive clicks — but the search market is small, so **paid search alone cannot fill the pipeline**.

The three findings that shape this entire plan:

1. **Search demand is thin and heavily polluted.** The keyword export shows 137,460 monthly searches, but `software in software` (49,500) and `dev ops` (5,400) alone account for 40% of that, and neither has commercial intent. Genuine vendor-selection demand is roughly **900–1,200 searches per month globally**, and the Netherlands slice of that is under 150.
2. **The money is in low-volume, high-bid terms.** `custom software development companies` has 70 monthly searches and a top-of-page bid of **$14.33–$34.36**. That bid is the market telling us where buyers with budgets are searching. Volume is the wrong metric here; bid is the signal.
3. **Manifera has two paid assets most competitors don't**: a real Amsterdam address for local targeting, and 1,460 written English articles — 513 of them decision-stage — that can be used as retargeting fuel, LinkedIn document ads, and lead-magnet material without writing anything new.

**Therefore the channel mix is deliberately inverted from a typical agency plan:** Google Search takes the smallest workable budget to capture existing intent, LinkedIn carries demand *creation* against a named account list, and agency directories (Clutch, Sortlist) get real budget because they intercept buyers already in a shortlist mindset.

---

## 2. Funnel Mapping (Buyer Stage → Channel Role)

| Stage | Buyer state | Channel | Asset | Success metric |
|---|---|---|---|---|
| **Problem-aware** | "We can't hire fast enough in the EU" | LinkedIn Sponsored Content, Meta prospecting | Awareness articles (292 in library), `dutchvsvietnam` cluster | Cost per qualified engaged view |
| **Solution-aware** | "Should we outsource, and to where?" | LinkedIn Document Ads, Google Search AG2/AG7, Reddit | `extra-6-dutchvsvietnam` (100 articles), consideration library (638) | Landing page visit rate, lead magnet downloads |
| **Vendor-aware** | "Which company do we shortlist?" | Google Search AG1/AG3/AG6, Clutch/Sortlist sponsorship, Bing | Decision library (513 articles), portfolio, case studies | Cost per proposal request |
| **Decision** | "Is Manifera legitimate?" | Brand campaign, retargeting, review platforms | Clutch reviews, FeaturedCustomers (29 reviews/19 case studies), testimonials | Proposal → meeting conversion |
| **Post-meeting** | "Justifying the choice internally" | Retargeting (Meta/LinkedIn), email | Case studies, ROI comparison, contract-model articles | Meeting → contract rate |

> Note that stages 3–5 are where Manifera's existing content library is strongest (513 decision-stage articles). The gap is stage 1–2 demand creation, which is why LinkedIn takes the largest single budget line in §9.

---

## 3. Keyword Strategy — What Not to Bid On

### 3.1. Cleaning the CSV before it touches an account

| Do not bid | Why | Action |
|---|---|---|
| `software in software` (49,500) | Syntactic noise, no intent | Account-level negative |
| `dev ops` (5,400), `developer s` (2,900) | Career/definition intent | Account-level negative |
| `application development` (1,300), `app development` (1,300) | Global head terms, mixed intent, mostly US | Exact match only, NL/BE/DE geo only, hard daily cap |
| `mobile app development` + ~20 duplicate variants (880 each) | Planner duplicates one search set across many rows; treating them as additive volume overstates the market by an order of magnitude | Pick two variants, exact match |
| `ai developers` (320), `app developers` (320) | Heavy job-seeker contamination | Exact match + job-seeker negative list |

### 3.2. What to bid on, ranked by commercial value

| Priority | Cluster | Representative terms | Combined vol | Why |
|---|---|---|---|---|
| 1 | Vendor selection | `custom software development companies/firms`, `software development company/firm` | ~580 | Highest bids in the entire dataset ($14–$34) |
| 2 | Offshore & dedicated teams | `offshore app development`, `dedicated software development team`, `offshore development team` | ~250 | Near-zero competition, exact match for Manifera's core product |
| 3 | Netherlands local | `software companies amsterdam`, `software companies in netherlands`, `software development companies in netherlands` | ~100 | Only cluster where the Amsterdam office is an unassailable advantage; one term has Competition Index **100** |
| 4 | Custom software & web app | `custom software development services`, `bespoke software development services`, `web application development` | ~230 | Mid-funnel, cheap, maps to existing service pages |
| 5 | Vietnam/Singapore sourcing | `it outsourcing company in vietnam`, `software development company vietnam` | ~80 | Buyers already sold on offshore, choosing a country |
| 6 | Mobile app (company-qualified only) | `mobile app development company`, `app development firm` | ~200 | Only variants containing company/firm/companies |
| 7 | Cost/BOFU | `custom software development cost`, `custom software development pricing` | ~150 | Only after a real pricing page exists |
| 8 | AI emerging | `ai software development companies`, `offshore ai developers` | ~90 | Audience-building for retargeting, not direct lead gen |

Full keyword tables with match types, bids and priorities: [`google_ads_keywords_manifera.md`](./google_ads_keywords_manifera.md) §3.

### 3.3. Gaps requiring separate research before spend

The June 2026 export contains **almost no eCommerce/Magento keywords** (two terms, 10 volume each) despite webshop development being one of Manifera's six services, and **zero** results for `staff augmentation` or `legacy modernization` — both of which are standard procurement vocabulary for the MNC persona. Run a dedicated Keyword Planner export for these three areas plus a Netherlands-only location filter before committing budget to §9 Tier 2.

---

## 4. Google Ads — Search Campaign Build

Nine campaigns, eight ad groups, detailed in [`google_ads_keywords_manifera.md`](./google_ads_keywords_manifera.md) §2–§4. Summary of the build rules:

| Rule | Detail |
|---|---|
| **Geo** | NL, BE, DE, SE, DK, NO, FI, IE, CH, AT for core campaigns. Never US/IN/BD — those auctions are set by low-cost agencies Manifera does not compete with. |
| **Language** | English only. Manifera.com has no Dutch pages (the legacy `/nl/` section is retired — see audit Finding #6). Bidding on Dutch keywords without Dutch landing pages destroys Quality Score. |
| **Match types** | Phrase and Exact only for the first 90 days. No Broad Match until at least 50 conversions exist to train the algorithm. |
| **Bidding** | Manual CPC or Maximize Clicks with a CPC cap for the first 30 days, to learn actual CPCs. Switch to Maximize Conversions only after 30 conversions in 30 days per campaign. |
| **Rollout** | Weeks 3–4: AG1, AG2, Brand only. Week 5+: AG3, AG6. Later, conditionally: AG4, AG5, AG7, AG8. |
| **Negatives** | Six shared lists applied account-wide from day one (job seekers, education/DIY, free/download, CSV junk heads, wrong-segment/no-code, packaged-software). |

**Ad copy:** 105 headlines and 28 descriptions, all length-verified, in [`google_ads_rsa_copy_manifera.md`](./google_ads_rsa_copy_manifera.md).

---

## 5. LinkedIn Ads — The Primary Demand-Creation Channel

LinkedIn is where Manifera's buyers are identifiable by job title and company size in a way Google search intent can never be. With search volume this thin, LinkedIn is not a supplementary channel — it is the growth engine.

### 5.1. Audience definitions (build these three in Campaign Manager first)

| Audience | Definition | Est. size (NL+BE) |
|---|---|---|
| **A1 — Core ICP** | Job titles: CTO, VP Engineering, Head of Engineering, IT Director, Engineering Manager · Company size 50–1,000 · Industries: Software, IT Services, Financial Services, Logistics, Healthcare · Geo: Netherlands, Belgium | 15,000–25,000 |
| **A2 — Founder/Exec** | Job titles: CEO, COO, Founder, Managing Director · Company size 11–200 · Same industries · Geo: NL, BE, DE | 30,000–50,000 |
| **A3 — Named accounts (ABM)** | Uploaded company list: 200–400 NL/BE/DE companies matching the profile of Manifera's best existing clients (look at the 19 published case studies to derive the pattern) | 200–400 companies |

### 5.2. Campaign 1 — `LI-Awareness-SponsoredContent`

- **Objective:** Engagement (not conversions — do not optimise for clicks on cold traffic)
- **Audience:** A1 + A2, exclude existing customers and employees
- **Budget:** €1,200/month (Tier 2)
- **Format:** Single image + document ads
- **Creative source:** The existing library. Turn these into carousel/document ads verbatim — no new writing required:
  - `extra-6-dutchvsvietnam/04-offshore-app-development-netherlands-vs-vietnam.md` → "Netherlands vs Vietnam: the real cost and governance comparison"
  - `extra-9-decision/03-final-vendor-checklist-before-you-sign-a-software-outsourcing-contract.md` → "The 12-point checklist before you sign an outsourcing contract"
  - `extra-9-decision/04-5-red-flags-walk-away-offshore-app-development-company.md` → "5 red flags that should end a vendor conversation"
  - `extra-3-longtail/03-fixed-price-vs-hourly-software-development.md` → "Fixed price vs time and materials: which one protects you"
- **Success metric:** Cost per document-ad open under €12; engagement rate above 1.2%

### 5.3. Campaign 2 — `LI-ABM-NamedAccounts`

- **Objective:** Website visits, then conversions
- **Audience:** A3 only
- **Budget:** €800/month
- **Format:** Single image + text ads, high frequency (this is a small audience — repetition is the point)
- **Message:** Amsterdam office, Dutch contracts, Vietnamese engineering. Directly addresses the "who governs the team" objection that kills most offshore deals.
- **Success metric:** Percentage of target accounts reached (aim 60%+), then meetings booked

### 5.4. Campaign 3 — `LI-Retargeting-Consideration`

- **Activate once the LinkedIn Insight Tag has tagged 500+ visitors.**
- **Audience:** Website visitors (90-day window), video viewers 50%+, document ad openers
- **Budget:** €500/month
- **Offer:** "Get a costed team proposal in 48 hours" — the highest-converting offer Manifera can make, because it is concrete, time-bound and free.
- **Success metric:** Cost per proposal request under €400

### 5.5. Campaign 4 — `LI-MessageAds` (Phase 2, week 9+)

Do not launch before a warm audience exists. Send only to A3 members who have already engaged. Message from Herre Roelevink personally (founder-to-founder messages outperform company messages by a wide margin in B2B services). Budget €300/month.

---

## 6. Agency Directories — A Channel Google Doesn't Cover

This is the highest-intent paid inventory available to a development agency, and Manifera already has organic profiles on all of them.

| Platform | Current state | Paid action | Budget/month | Why |
|---|---|---|---|---|
| **Clutch** | Organic profile with client reviews | Sponsored listing in "Software Developers Netherlands" / "Offshore Development" categories | €600–1,000 | Buyers on Clutch are building shortlists, not browsing. Highest intent of any paid inventory in this plan. |
| **Sortlist** | Directory listing | Paid lead package (NL market) | €300–500 | Strong in Benelux specifically |
| **FeaturedCustomers** | 29 reviews, 19 case studies | Upgrade to a paid vendor profile | €200 | Already the strongest social-proof asset; make it visible |
| **The Manifest / GoodFirms** | Unverified | Claim profiles first (free), evaluate paid later | €0 initially | Do not pay until organic profile is complete |

**Prerequisite:** before any directory spend, collect 5+ new Clutch reviews from recent clients. A sponsored listing pointing at a thin review profile converts poorly and wastes the entire spend.

---

## 7. Meta, Bing, Reddit and X

### 7.1. Microsoft (Bing) Ads — cheap duplicate of Google

Import the entire Google Search account into Microsoft Advertising. Bing skews older and more corporate/enterprise IT — exactly Manifera's persona C. CPCs typically run 30–50% below Google.
**Budget:** €400/month (Tier 2). **Effort:** one afternoon (direct import). **This is the best value line item in the plan.**

### 7.2. Meta (Facebook + Instagram) — retargeting only

Cold B2B prospecting on Meta for a €60k service does not work. Use Meta exclusively for:
- **Retargeting** website visitors (180-day window) with case studies and testimonials — €300/month
- **Reach** for the Dutch SME founder audience via interest + employer targeting — €200/month, only at Tier 3

### 7.3. Reddit — evaluate, do not commit

Relevant subreddits (r/ExperiencedDevs, r/cto, r/Netherlands business threads) are hostile to vendor advertising. Test €150/month with genuinely useful content (the cost-breakdown articles), measure, and kill it within 60 days if cost per landing-page visit exceeds €8.

### 7.4. X (Twitter) — not recommended

Manifera's audience (Dutch enterprise IT decision-makers) has low active presence on X. Skip entirely and reallocate to LinkedIn.

---

## 8. Landing Pages — Build These Before Spending

Three pages gate portions of this plan. **Do not activate the dependent campaigns until the corresponding page is live.**

### 8.1. `/amsterdam-software-development/` — gates AG6 (NL Local)

- H1: "Software Development Company in Amsterdam"
- Above the fold: the Herengracht 420 address, a photo of the office, and "Dutch contracts, euro invoicing, EU data hosting"
- Section: how a Dutch-managed, Vietnam-built team actually works day to day (this is the objection that decides the deal)
- Section: 3 case studies from Dutch clients
- Section: map + "book a meeting at our office" calendar embed
- Internal links: 8–12 of the 200 existing local articles (Amsterdam, Amstelveen, Haarlem, Zaanstad, Hilversum…)

### 8.2. `/software-development-cost/` — gates AG5 (BOFU Cost)

- Must contain **real numbers**. A cost page without prices converts worse than no page at all.
- Publish indicative monthly team rates by seniority mix and engagement model, with the caveat that final pricing depends on scope.
- Source material already written: `extra-3-longtail/02-custom-software-development-cost-breakdown.md`, `01-mobile-app-development-cost-2026.md`, `03-fixed-price-vs-hourly-software-development.md`
- Include the ROI comparison against hiring in-house in the Netherlands — that is the actual decision being made.

### 8.3. `/get-a-team-proposal/` — the shared conversion page for every channel

- One offer, repeated across Google, LinkedIn, Bing and directories: a costed team proposal within 48 hours.
- Form fields: company, role, roles needed, team size, timeline, work email. **No phone number** — it depresses B2B form completion by 30–40%.
- Trust strip: Clutch rating, 160+ projects, 120+ clients, founded 2014, three office locations.

---

## 9. Budget Tiers

### Tier 1 — Lean (€3,000/month) — first 60 days

| Line | Budget | Note |
|---|---|---|
| Google Search — AG1 Vendor Selection | €900 | |
| Google Search — AG2 Offshore Teams | €600 | |
| Google Search — Brand | €80 | Non-negotiable |
| LinkedIn — Awareness (A1+A2) | €700 | |
| Clutch sponsored listing | €600 | Only after 5+ fresh reviews |
| Bing (imported) | €120 | |
| **Total** | **€3,000** | |

### Tier 2 — Standard (€6,000/month) — this document's default

| Line | Budget | Note |
|---|---|---|
| Google Search — AG1 | €1,200 | |
| Google Search — AG2 | €800 | |
| Google Search — AG3 Custom/Web | €500 | |
| Google Search — AG6 NL Local | €600 | Requires §8.1 page live |
| Google Search — AG4 Mobile | €300 | Exact match only |
| Google Search — Brand | €150 | |
| LinkedIn — Awareness | €1,200 | |
| LinkedIn — ABM named accounts | €500 | |
| Clutch + Sortlist | €900 | |
| Bing | €400 | |
| Meta retargeting | €250 | Requires 1,000+ monthly visitors |
| **Total** | **€6,800** → trim AG4 and Meta to hit €6,000 exactly if needed | |

### Tier 3 — Aggressive (€12,000/month) — only after 20+ closed-won attributions

Add: LinkedIn retargeting (€800), LinkedIn Message Ads (€400), AG5 cost campaign (€500, requires §8.2), AG7 sourcing (€400), AG8 AI (€300), PMax retargeting (€500), Meta reach (€200), Reddit test (€150), plus roughly 40% uplift across the Tier 2 Google and LinkedIn lines.

> **Spending discipline:** do not move to the next tier until the current one produces a cost per proposal request under €400 for two consecutive months. Scaling a channel that isn't converting simply loses money faster.

---

## 10. UTM Convention (enforce from day one)

```
utm_source   = google | linkedin | bing | clutch | sortlist | meta | reddit
utm_medium   = cpc | paid-social | directory | retargeting
utm_campaign = mf-<channel>-<cluster>-<geo>     e.g. mf-google-vendorselection-nl
utm_content  = <adgroup>-<asset-id>             e.g. ag1-rsa1-h1a
utm_term     = {keyword}                        (Google/Bing auto-insert)
```

Rules: lowercase only, hyphens never underscores, campaign names identical between the ad platform and the UTM so GA4 (property `G-ZGH74C8BL4`) and the ad platforms reconcile without manual mapping. Register the three conversion events — `form_submit_contact`, `proposal_request`, `phone_call_60s` — as GA4 key events and import them into Google Ads with Enhanced Conversions enabled.

---

## 11. KPIs and Targets

| Metric | Month 1 | Month 3 | Month 6 | How measured |
|---|---|---|---|---|
| Paid sessions/month | 400 | 1,200 | 2,500 | GA4 |
| Cost per click (Google core) | €8–15 | €7–13 | €6–12 | Google Ads |
| Landing page → lead rate | 2% | 4% | 6% | GA4 conversion |
| Leads/month (all paid) | 8 | 25 | 45 | CRM |
| Cost per lead | < €375 | < €240 | < €150 | Blended |
| Proposal requests/month | 3 | 10 | 18 | CRM |
| Cost per proposal request | < €1,000 | < €600 | < €400 | Blended |
| SQLs/month | 2 | 6 | 12 | Sales qualification |
| Closed deals/quarter | — | 1–2 | 3–5 | CRM |
| Blended CAC | — | < €5,000 | < €3,500 | Total spend ÷ closed |

**Reality check on timing:** the sales cycle for a dedicated-team contract runs 60–120 days. Month 1 and 2 will show cost and no revenue. That is expected, not failure. Judge Google Search on cost per proposal request from month 2, and LinkedIn on pipeline influence from month 4 — never earlier.

---

## 12. 90-Day Execution Checklist

### Weeks 1–2 — Measurement and prerequisites
- [ ] GA4 key events defined and verified (`form_submit_contact`, `proposal_request`, `phone_call_60s`)
- [ ] Google Ads conversion import + Enhanced Conversions live
- [ ] LinkedIn Insight Tag installed site-wide
- [ ] Meta Pixel installed (for later retargeting; do not run ads yet)
- [ ] Six shared negative keyword lists created in Google Ads
- [ ] Build `/get-a-team-proposal/` (§8.3)
- [ ] Request 5+ new Clutch reviews from recent clients
- [ ] Fix the homepage H1 and add Organization schema (audit findings #1, #2) — this affects every paid landing session too

### Weeks 3–4 — First euro spent
- [ ] Launch AG1, AG2 and Brand only, Tier 1 budget, manual CPC
- [ ] Daily search-term review for the first 14 days; expand negatives every day
- [ ] Launch LinkedIn `LI-Awareness-SponsoredContent` with 4 document ads sourced from the article library
- [ ] Import the Google account into Bing

### Weeks 5–8 — Expand what works
- [ ] Publish `/amsterdam-software-development/` (§8.1), then launch AG6
- [ ] Launch AG3
- [ ] Activate Clutch sponsored listing (only if reviews landed)
- [ ] Build A3 named-account list and launch `LI-ABM-NamedAccounts`
- [ ] First copy rotation: replace all assets rated "Low" in Google Ads Asset Performance

### Weeks 9–12 — Optimise and decide
- [ ] Activate LinkedIn retargeting (Insight Tag should now have 500+ visitors)
- [ ] Publish `/software-development-cost/` (§8.2); launch AG5 only if the page has real numbers
- [ ] Meta retargeting on if monthly traffic exceeds 1,000 sessions
- [ ] Full 90-day review: cost per proposal request by channel, then decide Tier 2 or hold
- [ ] Feed the winning ad messaging back into the homepage and service pages

---

## 13. Risks and Notes

| Risk | Likelihood | Mitigation |
|---|---|---|
| **Search volume too small to spend the budget** | High | Expected. Google Search will likely underspend its allocation. Roll the surplus into LinkedIn and Clutch rather than loosening match types — loosening is how accounts start paying for `software in software`. |
| **Attribution invisible on a 60–120 day cycle** | High | Track proposal requests as the primary paid KPI, not closed revenue. Ask "how did you hear about us" on the form and reconcile against UTM quarterly. |
| **Homepage converts poorly** | Medium | The audit found the H1 is a testimonials heading and there is no Organization schema. Both affect paid landing quality. Fix before scaling spend. |
| **Clutch spend wasted on a thin profile** | Medium | Gate directory spend behind 5+ fresh reviews. |
| **Competing on price against low-cost agencies** | Medium | Never mention "cheap" or "low cost" in any ad. Manifera's position is governance and reliability, not the lowest rate. All 105 approved headlines follow this rule. |
| **No Dutch-language landing pages** | Low | Deliberate. The site is English-only and the legacy `/nl/` section is retired. Revisit only if a Dutch site section is ever rebuilt. |
| **eCommerce/Magento demand invisible in the data** | Medium | Run the supplementary keyword research in §3.3 before committing Tier 2 budget. |

---

*Prepared for Manifera Software Development Pte Ltd · Amsterdam · Singapore · Ho Chi Minh City*
