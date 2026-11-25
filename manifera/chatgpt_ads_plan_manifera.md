# ChatGPT Ads Plan: Manifera (€400 test)

> **Prepared:** 25 Nov 2026 · **Revised:** 25 Nov 2026 (total budget set to €400) · **Market:** Netherlands, Belgium, Germany · **Language:** English (manifera.com is English-only)
> **Internal inputs:** [`paid_ads_plan.md`](./paid_ads_plan.md) (deal value, KPI targets, UTM convention, GA4 events), [`google_ads_keywords_manifera.md`](./google_ads_keywords_manifera.md), [`google_ads_rsa_copy_manifera.md`](./google_ads_rsa_copy_manifera.md), [`manifera_info.md`](./manifera_info.md), [`seo-geo-audit-manifera-com-2026-11-19.md`](./seo-geo-audit-manifera-com-2026-11-19.md), and the LaunchStudio test plan [`../launchstudio/chatgpt_ads_plan_launchstudio.md`](../launchstudio/chatgpt_ads_plan_launchstudio.md).
> **External inputs:** third-party reports on ChatGPT Ads (sources in §15). OpenAI publishes few official numbers. Anything marked ⚠️ must be checked inside Ads Manager before launch.

---

## 0. Summary

| Item | Decision |
|---|---|
| Why test it | Manifera's Google Search market is thin (genuine vendor-selection demand ≈ 900-1,200 searches/month globally, < 150 in NL). ChatGPT is where buyers now ask "which company should build this?" A small, tracked test shows whether that conversation can be bought |
| What €400 can prove | Not a full channel verdict. It answers three questions: (1) do our ads get delivered to this audience at all, (2) at what CPC and CTR, (3) do the clicks behave like buyers (engaged sessions, at least one real lead)? |
| Channel | ChatGPT Ads, self-serve via **ads.openai.com** (open in Europe since 31 Aug 2026) |
| Structure | **1 campaign, 2 ad groups** (vendor selection, dedicated team). More ad groups would split ≈ 75 clicks too thin to learn anything |
| Budget | **€400 total.** €15/day, the platform minimum per campaign on EUR billing ⚠️, for **26 days** = €390 + €10 buffer |
| Test window | **7 Jan → 1 Feb 2027.** January avoids the Dutch holiday dip and lands when companies open new-year budgets. Setup and tracking tests run before Christmas |
| Where the money comes from | Google Search is expected to underspend its Tier 1 allocation (`paid_ads_plan.md` §13). Take the €400 from that surplus |
| Objective | Clicks, manual max CPC. Start bid **€4.50**, cap **€6** |
| Primary KPI | **≥ 1 qualified lead** from the €400 (cost per qualified lead ≤ €400) |
| Leading KPIs | ≥ 500 impressions/day (needed to spend €15/day at a 0.6% CTR), CTR ≥ 0.6%, CPC ≤ €6, engaged sessions ≥ 50% |
| Kill rule | After €200 spent: CTR < 0.3% **or** fewer than 100 impressions/day → stop and keep the rest of the €400 |
| Next step if it works | Scale to the larger 12-week plan (≈ €25/day, 5 ad groups) described in §11 |

---

## 1. Platform facts (Nov 2026)

| Topic | What is known | Impact on Manifera |
|---|---|---|
| Availability | Self-serve ads in 31 European markets (EU-27 + IS, LI, NO, CH), including NL, BE, DE | We can launch in January |
| Who sees ads | Only users on **Free and Go** plans. Plus, Pro, Team, Business and Enterprise users see no ads | **The biggest risk.** Many CTOs and engineering leads use a paid or company ChatGPT plan. Founders and SME owners are more likely to be reachable |
| Targeting | **No keywords, no match types.** Placement uses the conversation context, the landing page, the ad text and the **context hints** set per ad group | Google keywords become context hints (§5) |
| Personalisation in the EEA | Personalised ads and custom audiences are limited or not available ⚠️ (sources conflict) | Contextual targeting only |
| Hierarchy | Campaign (objective, location, budget) → Ad group (bid, destination, context hints) → Ad | Same logic as Google/Meta |
| Minimum budget | ≈ **€15/day per campaign** on EUR billing; the minimum follows the account's billing currency, not the target country ⚠️ | €15/day is both our floor and our ceiling. This is why the test lasts 26 days |
| Budget behaviour | A daily budget is a 7-day average. One day can spend up to 2× | Check total spend daily; pause the campaign at €390-400 |
| New accounts | Reports say new self-serve accounts can be limited to home-country targeting until identity verification and a spend threshold clear ⚠️ | Open the account under the entity whose country matches the target market (§4) |
| Bidding | Objectives: Reach (CPM), Clicks (CPC), Conversions (oCPC, billed per click). Bid strategies: "Maximize results" (default) or manual max CPC | Manual max CPC, so a few expensive clicks cannot eat the budget |
| Observed CPC | Mostly reported at **$3-5**, higher in competitive B2B categories | Start at €4.50, cap at €6 |
| Conversion tracking | OpenAI pixel and/or Conversions API. Click ID `oppref` is appended to the landing URL. Default window 30 days | Set up and test before Christmas (§4) |
| Creative limits | Title max 50 characters (shows best under ~30), body max 100 characters, square image 640×640 to 1200×1200, plus logo ⚠️ | Copy in §6 fits these limits |
| Restricted categories (EU) | Financial, legal and health services are restricted outside the US | Software development services are allowed |

---

## 2. Objective and audience

**Business goal:** find out, for €400, whether ChatGPT can put Manifera in front of companies choosing a software partner, and whether those clicks behave like buyers.

**Who we pay to reach (ICP):**

| Persona | Profile | Typical ChatGPT question | Reachable via ads? |
|---|---|---|---|
| **A. Founder / CEO of an SME or scale-up** (main target in this test) | 10-200 employees, NL/BE/DE, has a product to build or extend, no large in-house team | "Which software development company in the Netherlands can build our platform?" | Good: often on Free or Go |
| **B. CTO / Head of Engineering** | 50-1,000 employees, hiring is too slow, needs extra capacity | "Offshore vs nearshore dedicated team: which is safer for a Dutch company?" | Limited: many use paid plans |

Persona C (IT Director, legacy and cloud migration) is left out of this test because the budget cannot cover a third ad group. It returns in the scaled plan (§11).

**Not our audience:** freelancers looking for work, students, job seekers, people wanting a free app or a template, one-off micro jobs.

**Qualified lead = all 4 true:**
1. A company, not an individual (work email or company named in the form)
2. Based in the EU/EEA, the UK or Switzerland
3. Needs a team (≥ 2 engineers) or a project of meaningful size; not a one-off micro job
4. Wants to start within 6 months

---

## 3. Offer and message

| Element | Content |
|---|---|
| Positioning | European governance, Vietnamese engineering capacity. Never "cheap" or "low cost" (same rule as all Google copy) |
| Core promise | "A dedicated engineering team, managed from Amsterdam." |
| Verified proof (homepage, checked 25 Nov 2026) | 160 applications · 120 global clients · 30 experts and growing · since 2014 · offices in Amsterdam, Singapore and Ho Chi Minh City |
| Response promise (contact page) | "We will contact you within one working day" |
| CTA | "Talk to our team" |
| Do **not** use | "Proposal in 48 hours", "team in 2-4 weeks", "Dutch contracts", "GDPR-ready", "NDA on request", "interview every engineer". None of these appear on manifera.com; confirm with management before using any of them |

---

## 4. Setup checklist (26 Nov - 19 Dec 2026)

Everything here costs €0 and should be finished before Christmas, so the €400 is spent only on a working setup.

**Account**
- [ ] Create the account at ads.openai.com under a company login, with **EUR billing**
- [ ] Choose the legal entity on purpose: if the account is registered to the Singapore entity, check that NL/BE/DE targeting is available ⚠️ (new accounts may be locked to home-country targeting). If not, use the Dutch office details
- [ ] Add 2 admins (marketing + one manager)
- [ ] Confirm the minimum daily budget shown in the account ⚠️. If it is above €15, the test shortens to €400 ÷ minimum days

**Tracking**
- [ ] Ads Manager → Conversions → create a data source
- [ ] Install the OpenAI pixel site-wide through the theme header, a header-scripts plugin or GTM. **Never paste scripts into post content**: the WAF blocks it and posts must stay script-free
- [ ] Make sure the `oppref` parameter survives redirects (http → https, trailing slash) and is stored in a first-party cookie
- [ ] Events (aligned with the GA4 key events in `paid_ads_plan.md` §10):

| Event | Fires when | Type |
|---|---|---|
| `form_submit_contact` | Contact form sent successfully (Contact Form 7 `wpcf7mailsent`, not the button click) | **Primary** |
| `phone_call_click` | Click on a `tel:` link (NL +31 619 70 10 01, SG +65 9853 2842, VN +84 28 66522286) | Secondary |
| `email_click` | Click on a `mailto:` link | Secondary |
| `portfolio_view` | Portfolio page viewed for ≥ 30 s | Micro |

- [ ] UTMs on every ad, following the Manifera convention: `utm_source=chatgpt&utm_medium=cpc&utm_campaign=mf-chatgpt-<cluster>-eu&utm_content=<adgroup>-<ad>` (lowercase, hyphens)
- [ ] GA4 (`G-ZGH74C8BL4`): confirm `chatgpt / cpc` appears as its own source/medium
- [ ] CRM fields per lead: source, utm_content, oppref, company, country, team size needed, start date, qualified (Y/N), proposal requested (Y/N), deal value
- [ ] Add "How did you hear about us?" to the contact form, with "ChatGPT" as an option
- [ ] Send one test lead and confirm it appears in Ads Manager within 24 h

**Landing pages**

| Page | Status | Use |
|---|---|---|
| `/services/custom-software-development/` | Live | AG1 |
| `/services/offshore-software-development/` | Live | AG2 |
| `/contact-us/` | Live | Where the form is; linked from both pages |

- [ ] Both landing pages show the contact CTA in the first mobile screen
- [ ] Fix the homepage H1 and empty H1s (audit F1, F2) before launch: ChatGPT also reads the landing page to decide placement

---

## 5. Campaign structure

**Campaign:** `mf-chatgpt-eu-test400` · Objective: Clicks · Locations: Netherlands, Belgium, Germany · Budget: €15/day · Dates: 7 Jan - 1 Feb 2027

| Ad group | Context hints (from Google keywords + typical prompts) | Landing page | Start bid | Target share |
|---|---|---|---|---:|
| **AG1 Vendor selection** | custom software development company, software development company netherlands, software development partner europe, bespoke software development services, "which company can build our platform", "how to choose a software development company", "build vs outsource software" | `/services/custom-software-development/` | €4.50 | 60% |
| **AG2 Dedicated / offshore team** | dedicated software development team, offshore development team, hire offshore developers, staff augmentation, software development vietnam, "offshore vs nearshore for a Dutch company", "how much does a development team cost" | `/services/offshore-software-development/` | €4.50 | 40% |

**Exclusions** (where Ads Manager allows; otherwise filter through copy): jobs, salary, vacancy, freelance, internship, course, tutorial, free, template, "learn to code".

**Copy qualifier:** every ad mentions "team", "company" or "your platform", so job seekers and hobbyists filter themselves out.

If one ad group takes more than 75% of spend for 3 days in a row, lower its bid by €0.50.

---

## 6. Ads (3 per ad group)

Titles ≤ 30 characters, bodies ≤ 100 characters (checked). Image: square 1200×1200, a real team or office photo with the logo. No stock photos, no text-heavy images.

| AG | Title | Body |
|---|---|---|
| AG1-A | Software partner in Amsterdam | Custom software built by our own engineers, managed from Amsterdam. 160 apps since 2014. |
| AG1-B | Need a team to build it? | Web, mobile and business software for SMEs and enterprises. Talk to our team. |
| AG1-C | Shortlisting dev companies? | 120 global clients since 2014. Ask us how we would build your platform. |
| AG2-A | A dedicated dev team for you | Your own engineers, managed from Amsterdam. Scale up without hiring delays. |
| AG2-B | Offshore team, EU management | Engineering capacity in Vietnam, governance in Amsterdam. Talk to our team. |
| AG2-C | Can't hire developers fast? | Add a dedicated team to your roadmap. We reply within one working day. |

**Creative rules**
- Match the question the user is asking; name the problem in the title
- One claim per ad, and only claims that are on manifera.com (§3)
- Never "cheap", "low cost" or "best"
- No em dash
- Do not rotate in new ads during the 26 days: with this little traffic, changes make the results unreadable. Pause only an ad with CTR below half of its ad group's average after 1,000 impressions

---

## 7. Timeline, bidding and budget

| Phase | Dates | Daily budget | Spend | Goal |
|---|---|---:|---:|---|
| 0 Setup | 26 Nov - 19 Dec 2026 | €0 | €0 | Account, pixel and test lead working; ads approved |
| 1 Run, first half | 7 - 19 Jan 2027 (13 days) | €15 | ≈ €195 | Delivery and CTR per ad group |
| Checkpoint | 20 Jan | - | - | Apply the kill rule (§0); adjust bids once |
| 2 Run, second half | 20 Jan - 1 Feb (13 days) | €15 | ≈ €195 | Leads and lead quality |
| Stop | 1 Feb, or earlier when spend reaches €400 | €0 | **≈ €390-400** | - |
| Decide | 3 Feb 2027 | - | - | Scale, extend or stop (§11) |
| Pipeline check | 31 May 2027 | - | - | Count proposals and deals from test leads (60-120 day sales cycle) |

**Bid rules**
- No bid changes before the 20 Jan checkpoint, unless spend is €0 for 2 days (then +€0.50)
- Never above €6 max CPC: at €400, every €1 of CPC removes about 10 clicks from the test
- At the checkpoint: CPC ≤ €4 with low impressions → +€0.50; CPC > €6 → -€0.50
- Conversion-optimised bidding is not an option at this budget (it needs ≥ 30 conversions in 30 days)

---

## 8. KPIs

### 8.1 Targets for the €400 test

With ≈ 60-110 clicks, lead numbers will be small. The test is judged first on delivery and click quality, then on whether at least one real lead arrives.

| Stage | KPI | Target | Alarm | Action at alarm |
|---|---|---|---|---|
| Delivery | Impressions/day | ≥ 500 | < 200 for 5 days (the budget will underspend) | Broaden context hints; +€0.50 bid at the checkpoint. Below 100/day: kill rule |
| Attention | CTR | ≥ 0.6% | < 0.3% after 2,000 impressions | Stop at the checkpoint (kill rule) |
| Cost | Average CPC | ≤ €6 | > €6 for 5 days | Lower the max CPC by €0.50 |
| Click quality | Engaged sessions (GA4) | ≥ 50% | < 30% | The audience or landing page is wrong; note it for the decision |
| Click quality | Avg. engagement time | ≥ 45 s | < 20 s | Same as above |
| Lead | Leads (all) | ≥ 2 | 0 after €300 | Prepare to stop |
| Quality | **Qualified leads** | **≥ 1** | 0 at €400 | Stop or extend only on strong click quality (§11) |
| Sales | Lead → first call | 100% within one working day | Any lead not called back | Fix the lead routing immediately |

### 8.2 Benchmarks (context only)

| Metric | ChatGPT Ads, B2B (reported) | Manifera Google Search (plan targets) |
|---|---|---|
| CPC | $3-5, higher in competitive B2B | €8-15 (month 1) |
| CTR | ~0.5-1.2% | 3-6% |
| Lead rate | ~1.5-2% (B2B projections) | 2% → 6% (months 1-6) |
| Cost per lead | Ranges from about 40-60% below Google to zero leads at all | < €375 → < €150 (months 1-6) |

⚠️ Public B2B tests are mixed. One compliance-services advertiser reported a cost per lead of $92 on ChatGPT vs $158 on Google, but its ChatGPT leads converted to customers at a lower rate. An industrial agency spent $1,470 for 259 clicks and zero conversions. **Judge this test on lead quality, never on clicks alone.**

---

## 9. Forecast for €400

| | Conservative | Base | Optimistic |
|---|---:|---:|---:|
| CPC | €6 | €4.50 | €3.50 |
| Clicks | 67 | 89 | 114 |
| CTR | 0.4% | 0.6% | 1.0% |
| Impressions needed | ~16,700 | ~14,800 | ~11,400 |
| Impressions/day (26 days) | ~640 | ~570 | ~440 |
| Lead rate | 1% | 2% | 3.5% |
| **Leads** | **0.7** | **1.8** | **4.0** |
| **Cost per lead** | **€600** | **€225** | **€100** |
| Qualified (40%) | 0.3 | 0.7 | 1.6 |
| **Cost per qualified lead** | **€1,500** | **€570** | **€250** |

**Reading the forecast honestly:**
- The base case gives **about 2 leads and an expected 0.7 qualified leads, roughly a 50% chance of at least one**. A result of zero leads is possible even if the channel works, simply because ~90 clicks is a small sample
- That is why the decision in §11 also uses delivery, CTR and engaged sessions, not leads alone
- One deal (≈ €60,000 first-year value) returns about 150× the €400, so a single qualified lead that converts would justify the scaled plan

---

## 10. Link to SEO/GEO (organic ChatGPT visibility)

- manifera.com is **not** blocked for GPTBot, ChatGPT-User or ClaudeBot (audit 19 Nov 2026), so AI assistants can read and cite the site
- Before the test (December) and after it (February), run the 10-prompt GEO test from the audit in a **logged-out/Free** ChatGPT session. Note which prompts show a Manifera ad, a Manifera citation, or a competitor. This gives a free before/after comparison next to the paid numbers
- Fix audit items F1 (homepage H1), F2 (empty H1s), F5 (BlogPosting schema, `sameAs`) and F9 (`llms.txt` header) in parallel. They help both organic citation and ad placement quality

---

## 11. Decision rules (3 Feb 2027)

| Result after €400 | Decision |
|---|---|
| ≥ 1 qualified lead **and** CTR ≥ 0.6% | **Scale:** move to the 12-week plan at ≈ €25/day (≈ €750/month), add AG3 cost/models, AG4 cloud migration and AG5 AI to production, build `/get-a-team-proposal/` |
| 0 qualified leads, but CTR ≥ 0.6% **and** engaged sessions ≥ 50% | **Extend once:** another €400 (26 days at €15/day) on the better ad group only. The clicks look like buyers; the sample was too small |
| CTR < 0.3% **or** < 100 impressions/day | **Stop:** the audience is not reachable through ChatGPT ads yet. Put the next €400 into Clutch or LinkedIn ABM (`paid_ads_plan.md` §5-6) and re-test in 6 months |
| Engaged sessions < 30% | **Stop:** clicks are curiosity, not buying intent |
| 31 May 2027: a test lead becomes a proposal or a deal | Keep ChatGPT Ads in the mix regardless of the February decision |

---

## 12. Routine during the test (twice a week, ~15 min)

**Every Monday and Thursday, 7 Jan - 1 Feb:**
1. Check total spend against the €400 cap; pause when it reaches €390-400
2. Note impressions, clicks, CTR, CPC and spend per ad group
3. Match any conversions to CRM leads; mark each lead qualified or not
4. Call back every new lead within one working day
5. No changes outside the 20 Jan checkpoint, except pausing an ad (§6) or the campaign (kill rule)

**Change log**

| Date | Ad group | Change | Reason | Result after 7 days |
|---|---|---|---|---|

---

## 13. Reporting template

| Period | Spend | Impr. | Impr./day | Clicks | CTR | CPC | Engaged % | Leads | Qualified | Cost/lead | Cost/qualified | Notes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 7-12 Jan | | | | | | | | | | | | |
| 13-19 Jan | | | | | | | | | | | | |
| 20-26 Jan | | | | | | | | | | | | |
| 27 Jan - 1 Feb | | | | | | | | | | | | |
| **Total** | | | | | | | | | | | | |

---

## 14. Risks and mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Sample too small for a clear answer | Certain | Judge on delivery, CTR and engaged sessions as well as leads; the "extend once" rule in §11 |
| CTOs and IT directors use paid ChatGPT plans and never see ads | High | Founder/SME questions in AG1; the kill rule stops the test at €200 if delivery is too low |
| Clicks from job seekers and freelancers | High | "Team"/"company" in every ad; exclusions; qualification in the CRM |
| Spend runs over €400 (daily budget can spend 2× on single days) | Medium | Check spend twice a week; pause at €390-400 |
| Minimum budget higher than €15/day in the account | Medium | Confirm during setup; shorten the test to fit €400 instead of raising spend |
| Long sales cycle hides results | Certain | Decide on leads in February; count deals at the 31 May pipeline check |
| Broken tracking on Contact Form 7 | Medium | Fire on `wpcf7mailsent`; send a test lead before Christmas; count leads by hand as backup |
| Account limited to home-country targeting | Medium | Decide the legal entity before signup (§4) |
| Unverified claims slipping into ads | Medium | Only the claims listed in §3; management sign-off for anything else |

---

## 15. Sources (external, check before relying on them)

- Europe availability, EEA rules and the €15/day floor: [trucommerce.ai](https://trucommerce.ai/chatgpt-ads/europe), [mairateam.com](https://mairateam.com/en/chatgpt-ads-europe-guide/), [indexlab.ai](https://www.indexlab.ai/blog/chatgpt-ads-plugin-custom-audiences-euro-minimum), [soku.ai](https://soku.ai/blog/chatgpt-ads-minimum-budgets-by-country)
- Costs, billing and bidding: [flyweel.co](https://www.flyweel.co/blog/openai-launches-chatgpt-ads), [hellogrowth.ai](https://hellogrowth.ai/en/blog/advertising-in-chatgpt), [botrank.ai](https://www.botrank.ai/post/chatgpt-ads-best-practices-guide)
- B2B fit and results: [in-sync.io](https://www.in-sync.io/en/knowledge/chatgpt-ads), [factors.ai](https://www.factors.ai/blog/chatgpt-ads-b2b), [workshopdigital.com](https://www.workshopdigital.com/blog/chatgpt-ads-for-b2b/), [windmillstrategy.com](https://www.windmillstrategy.com/chatgpt-ads-b2b-industrial-manufacturing-pilot/), [stubgroup.com](https://stubgroup.com/case-study/chatgpt-ads-case-study/), [mediapost.com](https://www.mediapost.com/publications/article/417528/data-reveals-chatgpt-ads-not-performing.html?edition=143701), [adventureppc.com](https://www.adventureppc.com/blog/chatgpt-ads-vs-linkedin-ads-for-b2b-lead-generation-in-2026)
- Conversion tracking: [OpenAI Help: Conversion Measurement](https://help.openai.com/en/articles/20001409-conversion-measurement), [OpenAI Developers: Conversion-Optimized Campaigns](https://developers.openai.com/ads/conversion-optimized-campaigns)
- Earlier research for the LaunchStudio test (creative specs, structure, benchmarks): see §14 of [`../launchstudio/chatgpt_ads_plan_launchstudio.md`](../launchstudio/chatgpt_ads_plan_launchstudio.md)
