# ChatGPT Ads Plan: LaunchStudio (detailed)

> **Prepared:** 18 Nov 2026 · **Market:** NL first, then EU · **Language:** English
> **Internal inputs:** `google_ads_kpi_forecast_18eur_nov2026.md` (CPL, CAC, LP conversion, deal value), `google_ads_keywords_launchstudio.md`, `google_ads_conversion_fix.md`, the `landing_*_brief.md` files.
> **External inputs:** third-party guides on ChatGPT Ads (sources in §14). OpenAI publishes few official numbers. Anything marked ⚠️ must be checked inside Ads Manager before launch.

---

## 0. Summary

| Item | Decision |
|---|---|
| Channel | ChatGPT Ads, self-serve via **ads.openai.com** (open in the EU since late Aug 2026) |
| Structure | **1 campaign, 6 ad groups.** The minimum budget applies per campaign (≈ €15/day on EUR billing ⚠️), so 6 separate campaigns would need ≥ €90/day |
| Budget | **€20/day ≈ €600/month** for the test. Drop to €15/day over the holidays |
| Objective | Clicks, with CPC bidding. Start bid **€4**. Switch to conversion-optimised bidding only once there are ≥ 30 tracked leads |
| Primary KPI | **Cost per qualified lead (CPL) ≤ €200** |
| North-star KPI | **CAC ≤ €800**, the break-even point (€2,000 average deal × ~40% margin) |
| Test length | 10 weeks: 24 Nov 2026 → 1 Feb 2027 |
| Total test spend | ≈ €1,350 |
| Kill rule | €1,200 spent with 0 qualified leads → pause the channel |

---

## 1. Platform facts (Nov 2026)

| Topic | What is known | Impact on this plan |
|---|---|---|
| Availability | Self-serve ads open in 31 European markets (EU-27 + IS, LI, NO, CH), including NL | We can launch now |
| Who sees ads | Only users on the **Free and Go** plans. Plus/Pro/Team/Enterprise users see no ads | Many builders pay for ChatGPT, so our reach is smaller than it looks. This is the biggest risk |
| Targeting | **No keywords, no match types.** Placement uses conversation context, landing page, ad text, and the **context hints** we supply at ad group level | Google keywords become context hints (§5) |
| Personalisation in the EEA | Personalised ads and custom audiences are limited or not available yet ⚠️ | Contextual targeting only |
| Hierarchy | Campaign (objective, location, budget) → Ad group (bid, destination, context hints) → Ad (creative) | Same logic as Google/Meta |
| Minimum budget | ≈ **€15/day per campaign** on EUR billing (≈ $25/day in USD) ⚠️ | Use one campaign |
| Budget behaviour | A daily budget is an average. One day can reach 2× the budget; a week caps at 7× | Expect uneven daily spend |
| Bidding | CPC, CPM, and conversion-optimised CPC (oCPC, still billed per click). Reports say Target CPC/CPA replace Max CPC for new campaigns from 9 Nov 2026 ⚠️ | Start with CPC or Target CPC |
| Recommended CPC | $3-5 is OpenAI's suggested starting bid. Reported range: $3-22 | Start at €4 |
| CPM | Reported $25-45 (it was $60 at launch) | Reference only |
| Conversion tracking | OpenAI pixel and/or Conversions API. The click ID `oppref` is appended to the landing URL. Default window: 30 days | Set up before launch (§4) |
| Creative limits | Title max 50 characters (shows best under ~30), body max 100 (best 32-48), square image ≥ 640×640 up to 1200×1200, plus a logo ⚠️ | Copy in §6 is written to ≤ 30 / ≤ 100 |
| Restricted categories (EU) | Banks, insurers, clinics and law firms are closed for now | Not us. Software services are allowed |

---

## 2. Objective and audience

**Business goal:** add a second lead source next to Google Search, at a CPL equal to or below Google's (base case €200).

**ICP (who we pay to reach):**
- Founder or solo builder, NL/EU
- Has an app already **built** in Lovable, Bolt, Replit or Cursor, often with Supabase
- Has real users or a launch within 3 months
- Faces one of these triggers: customer security/privacy questionnaire, enterprise deal, adding payments, a bug the AI tool can't fix, slow app, GDPR/AVG question

**Not our audience:** students, people who want to learn to code, job seekers, "build me an app from scratch for free" requests.

**What counts as a qualified lead (all 4 must be true):**
1. Has an existing app (or a working prototype)
2. Based in the EU
3. Accepts the price range (€800-7,500 fixed)
4. Wants to start within 3 months

---

## 3. Offer and message

| Element | Content |
|---|---|
| Core promise | "Your AI-built app works. We make it safe to sell." |
| Proof (from the website) | 11+ years, 160+ projects, fixed price €800-7,500, 1-3 weeks, EU team (Manifera) |
| Proof (from case studies) | Real examples: exposed keys found, RLS fixed, payments added, enterprise questionnaires answered |
| CTA | "Book a review" (main) · "Get a fixed quote" (secondary) |
| Lead magnet (fallback) | The 20-item "Launch readiness" checklist already on the site |

---

## 4. Setup checklist (week 0: 18-23 Nov)

**Account**
- [ ] Create an account at ads.openai.com under the company (not a personal login). Billing in **EUR**
- [ ] Add 2 admins (owner + marketer)
- [ ] Confirm the minimum daily budget shown in the account ⚠️

**Tracking**
- [ ] Ads Manager → Tools → Conversions → create a data source
- [ ] Install the OpenAI pixel on every landing page (through GTM if a template exists, otherwise directly in `<head>`)
- [ ] Optionally, also send events through the Conversions API, using the **same event ID** as the pixel to avoid double counting
- [ ] Confirm the `oppref` parameter survives redirects and is stored in a first-party cookie
- [ ] Set up these events:

| Event | Fires when | Type |
|---|---|---|
| `book_review` | Review/booking form submitted successfully | **Primary** |
| `quote_request` | Quote form submitted successfully | Primary |
| `mailto_click` | Email link clicked | Secondary |
| `checklist_download` | Checklist lead magnet submitted | Secondary |
| `pricing_calc_use` | Price calculator used | Micro |

- [ ] Re-check every form listed in `google_ads_conversion_fix.md` (`qqContactForm`, `cContactForm`, `quote-form`, `lsContactForm`, `security-quote`, `launchInquiry`). Each must fire on **successful** submit, not on button click
- [ ] Add UTMs to every ad: `utm_source=chatgpt&utm_medium=cpc&utm_campaign=ls_chatgpt_test&utm_content=<adgroup>_<ad>`
- [ ] Set up GA4 / CRM: store `utm_source`, `utm_content` and the `oppref` click ID in the lead record
- [ ] CRM fields for qualification: has_app (Y/N), tool (Lovable/Bolt/Replit/Cursor), EU (Y/N), budget OK (Y/N), start < 3 months (Y/N)
- [ ] Submit one test lead per form and confirm it shows in Ads Manager within 24 h

**Landing pages**
- [ ] One landing page per ad group (§5). Use the existing `landing_*_brief.md` pages where they exist
- [ ] English version, mobile first. The form must be above the fold on mobile
- [ ] State "fixed price €800-7,500" and "1-3 weeks" in the first screen
- [ ] Page load time < 2.5 s on mobile (LCP)

---

## 5. Campaign structure

**Campaign:** `LS | ChatGPT | EU-NL | Test` · Objective: Clicks · Location: Netherlands (add BE + DE in phase 3) · Budget: €20/day

| Ad group | Context hints (from Google keywords + typical prompts) | Landing page | Start bid |
|---|---|---|---|
| **AG1 Lovable** | lovable developer, lovable expert, lovable app production, lovable supabase, hire lovable developer, "my lovable app is ready to launch", "lovable app security" | Lovable / AI app into production page (`landing_ai_app_into_production_brief.md`) | €4 |
| **AG2 Bolt / Replit / Cursor** | bolt.new developer, replit deployment, replit to production, cursor developer, "deploy my bolt app", "move replit app to own hosting" | Prototype to production page (`landing_prototype_to_production_brief.md`) | €3.50 |
| **AG3 Security** | supabase rls, supabase security audit, ai app security audit, "is my supabase key safe", "row level security not working", pentest preparation | Security review page (`landing_ai_app_security_brief.md`) | €4.50 |
| **AG4 Payments** | stripe integration developer, mollie integration, saas subscription billing, "add payments to lovable app", failed payments, VAT invoices | Integrations page (`landing_ai_app_integrations_brief.md`) | €3.50 |
| **AG5 Compliance** | gdpr compliance saas, security questionnaire, data processing agreement, AVG, "enterprise customer asks for security documents" | Security review page (compliance section) | €3.50 |
| **AG6 Stuck bug** | fix ai generated code, vibe coding developer, ai app code review, "lovable keeps breaking", "cursor can't fix this bug" | Vibe coding / rescue page (`landing_ai_app_vibe_coding_brief.md`) | €4 |

**Exclusions** (wherever Ads Manager allows; otherwise filter through copy): free, tutorial, course, learn, jobs, salary, template, download, "how to build an app".
**Copy qualifier:** every ad says "already built" or "your app", so beginners self-filter and clicks stay cheaper.

**Budget control:** the budget sits at campaign level and is shared by all 6 ad groups. Steer spend with bids and by pausing ad groups. Target split in phase 1:

| AG1 | AG2 | AG3 | AG4 | AG5 | AG6 |
|---:|---:|---:|---:|---:|---:|
| 25% | 10% | 25% | 10% | 10% | 20% |

If one ad group takes more than 40% of spend for 3 days in a row, lower its bid by €0.50.

---

## 6. Ads (2-3 per ad group)

Titles ≤ 30 characters, bodies ≤ 100 characters. Image: square 1200×1200 with a clean product/UI visual and the logo. No text-heavy images.

| AG | Title | Body |
|---|---|---|
| AG1-A | Built in Lovable? Go live. | Security, payments and GDPR fixed by an EU team. Fixed price €800-7,500. |
| AG1-B | Lovable app, production-ready | We review and fix your Lovable + Supabase app before real users arrive. |
| AG2-A | Bolt or Replit app? Go live. | Own hosting, real domain, safe deploys. Fixed price, done in 1-3 weeks. |
| AG2-B | From prototype to real users | Your app works in preview. We make it work in production. EU engineers. |
| AG3-A | Is your Supabase key public? | We check RLS, keys and auth at code level. Fixed-price security review. |
| AG3-B | AI app security review | Find what AI-generated code misses before a customer or attacker does. |
| AG3-C | Fix RLS before you launch | Row level security, storage and endpoints checked by experienced engineers. |
| AG4-A | Stripe or Mollie, done right | Subscriptions, failed cards, VAT invoices and refunds that hold up in production. |
| AG4-B | Add payments to your app | Payments built properly for your Lovable or Bolt app. Fixed price, EU team. |
| AG5-A | Enterprise questionnaire help | Answer security and GDPR questions with evidence, not guesses. |
| AG5-B | GDPR for your AI-built app | DPA, subprocessors, retention and deletion: built in, not just written down. |
| AG6-A | Bug your AI can't fix? | Experienced engineers fix what prompting can't. Fixed price, 1-3 weeks. |
| AG6-B | Lovable keeps breaking? | Stop the prompt loop. We find the cause in the code and fix it for good. |

**Creative rules**
- Name the problem in the title. ChatGPT users are mid-question, so match the question
- One claim per ad. No unsourced statistics
- No em dash
- Keep the wording in sync with the landing page headline

---

## 7. Bidding and budget

| Phase | Dates | Daily budget | Bidding | Goal |
|---|---|---:|---|---|
| 0 Setup | 18-23 Nov | €0 | - | Tracking verified, ads approved |
| 1 Test | 24 Nov - 14 Dec (3 wks) | €20 | CPC / Target CPC, start bids per §5 | ≥ 300 clicks, first CPL per ad group |
| 2 Holiday | 15 Dec - 4 Jan (3 wks) | €15 (minimum) | Same | Keep learning; expect ~-30% leads (NL B2B holiday dip) |
| 3 Optimise | 5 Jan - 1 Feb (4 wks) | €20 | Same. Budget only to the best 2-3 ad groups | CPL ≤ €200 |
| 4 Decide | 2 Feb | - | - | Scale, hold, or stop (§10) |

**Spend estimate:** phase 1 ≈ €420 + phase 2 ≈ €315 + phase 3 ≈ €560 = **≈ €1,300-1,350**.

**Bid rules**
- Don't change bids in the first 7 days unless spend is 0 (then +€0.50)
- CTR > 1% but CPL > €400 → the problem is the landing page or qualification, not the bid. Don't raise bids
- Consider oCPC / Target CPA only with ≥ 30 `book_review` + `quote_request` conversions in 30 days. That is unlikely at this budget, so plan for CPC throughout the test

---

## 8. KPIs

### 8.1 Funnel targets

| Stage | KPI | Target | Alarm | Action at alarm |
|---|---|---|---|---|
| Delivery | Impressions/day | ≥ 300 | < 100 for 5 days | Broaden context hints, +€0.50 bid |
| Attention | CTR | ≥ 0.8% | < 0.4% after 2,000 impr. | Rewrite the title to match the prompt more closely |
| Cost | Avg. CPC | ≤ €5 | > €8 for 2 weeks | Lower bids, pause the most expensive ad group |
| Landing | LP conversion (leads ÷ clicks) | ≥ 3% | < 1.5% after 100 clicks | Fix the LP before spending more |
| Lead | **CPL (all leads)** | **≤ €200** | > €400 after 30 days | Pause that ad group |
| Quality | Qualified lead rate | ≥ 50% | < 30% | Tighten copy ("already built"), adjust hints |
| Quality | Cost per qualified lead | ≤ €400 | > €800 | Stop the ad group |
| Sales | Lead → call booked | ≥ 50% | < 30% | Reply within 1 h; check lead routing |
| Sales | Call → deal | ≥ 15% | < 10% | Sales script, quote within 24 h |
| Business | **CAC** | **≤ €800** | > €1,600 after 60 days | Stop scaling |
| Business | ROAS (deal value ÷ spend) | ≥ 2.5× | < 1× after 90 days | Re-evaluate the channel |

### 8.2 Benchmarks (for context only)

| Metric | ChatGPT Ads, B2B (reported) | Google Search NL (our own forecast) |
|---|---|---|
| CTR | 0.5-1.2% | 4-6% |
| CPC | $3-8 | €6.50-10 |
| CPM | $25-45 | - |
| LP conversion | ~1.8% (B2B SaaS projection) | 2.5-6% |
| Cost per MQL | $120-250 (one agency) | CPL €108-400 |

⚠️ One public B2B test spent ~$2,300 for 739 clicks and **zero qualified leads**. Clicks are not leads, so judge only on qualified leads.

---

## 9. Forecast (per month at €600)

| | Conservative | Base | Optimistic |
|---|---:|---:|---:|
| CPC | €7 | €5 | €3 |
| Clicks | 86 | 120 | 200 |
| CTR (impressions needed) | 0.5% (~17,000) | 0.8% (~15,000) | 1.2% (~16,700) |
| LP conversion | 1.5% | 3% | 5% |
| **Leads** | **1.3** | **3.6** | **10** |
| **CPL** | **€460** | **€167** | **€60** |
| Qualified (50%) | 0.6 | 1.8 | 5 |
| Close rate (of all leads) | 10% | 15% | 25% |
| New customers | 0.13 | 0.54 | 2.5 |
| **CAC** | **€4,600** | **€1,110** | **€240** |
| Revenue at €2,000/deal | €260 | €1,080 | €5,000 |

**Over the 10-week test (base case):** ≈ €1,350 spend · ≈ 270 clicks · ≈ 8 leads · ≈ 1 customer.
**Break-even:** at CPL €167 we need a **≥ 21% close rate** to reach CAC ≤ €800. Closing more deals moves CAC more than bidding does.

---

## 10. Decision rules (2 Feb 2027)

| Result after 10 weeks | Decision |
|---|---|
| CPL ≤ €200 **and** ≥ 1 deal | **Scale:** €30/day, add BE + DE, test new ad groups |
| CPL €200-400, ≥ 50% qualified | **Hold:** keep €15-20/day on the best 2 ad groups, run 4 more weeks |
| CPL > €400 or < 30% qualified | **Stop:** move the budget back to Google Search or SEO/GEO content |
| €1,200 spent, 0 qualified leads (at any time) | **Stop immediately** |

---

## 11. Weekly routine (every Monday, ~30 min)

1. Export last 7 days per ad group: impressions, clicks, CTR, CPC, spend, conversions
2. Match the conversions to CRM leads and mark each one qualified or not
3. Update the KPI table (§8.1) and flag any alarm
4. Apply at most **2 changes** per week (bids, pausing, a new ad). Log them in the change log
5. Read 5 recent lead messages: do they mention the problem the ad promised?
6. Every 2 weeks: replace the worst-performing ad in each ad group with a new variant

**Change log template**

| Date | Ad group | Change | Reason | Result after 7 days |
|---|---|---|---|---|

---

## 12. Reporting template (weekly)

| Week | Spend | Impr. | Clicks | CTR | CPC | Leads | Qualified | CPL | Cost/qualified | Calls | Deals | Revenue | Notes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| W1 | | | | | | | | | | | | | |

---

## 13. Risks and mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Our ICP uses paid ChatGPT plans and never sees ads | High | Measure impressions in week 1; if < 100/day, broaden hints or stop early |
| Clicks from curious beginners, not buyers | High | "Already built" in every ad; qualification fields in the CRM; judge on qualified CPL |
| Broken tracking (as happened on Google) | Medium | §4 checklist; test leads before launch; count leads by hand as backup |
| Platform rules change (bidding, minimums) | Medium | Check Ads Manager settings weekly; this plan uses only basic CPC |
| No personalised targeting in the EEA | Certain | Contextual hints only; landing pages matched to topic |
| Holiday dip in late December | Certain | Minimum budget 15 Dec - 4 Jan; don't judge results in that window |
| Low volume, so results aren't statistically meaningful | High | Decide on the 10-week total, not on single weeks |

---

## 14. Sources (external, check before relying on them)

- Europe availability: [move.marketing](https://move.marketing/en/blog/chatgpt-ads-in-europe), [indexlab.ai](https://www.indexlab.ai/blog/chatgpt-ads-europe-self-serve-live), [li.solutions](https://li.solutions/blog/chatgpt-ads-europe/)
- Minimum budget (EUR): [indexlab.ai](https://www.indexlab.ai/blog/chatgpt-ads-plugin-custom-audiences-euro-minimum), [soku.ai](https://soku.ai/blog/chatgpt-ads-minimum-budgets-by-country), [metaturbine.com](https://metaturbine.com/blog/chatgpt-ads-launched-in-europe-here-is-what-actually-shipped)
- Pricing (CPC/CPM): [webfx.com](https://www.webfx.com/blog/ai/chatgpt-ads-cost/), [sprites.ai](https://www.sprites.ai/blog/chatgpt-ads-cost), [digitalapplied.com](https://www.digitalapplied.com/blog/chatgpt-ads-marketers-pricing-targeting-guide)
- Creative specs and targeting: [indexlab.ai](https://www.indexlab.ai/guides/chatgpt-ads/creative-specs), [spaceads.agency](https://www.spaceads.agency/blog/chatgpt-ad-formats-character-limits-creative-specs), [contexthints.com](https://www.contexthints.com/guide/how-chatgpt-ads-work.html)
- Conversion tracking: [OpenAI Help: Conversion Measurement](https://help.openai.com/en/articles/20001409-conversion-measurement), [OpenAI Developers: Conversion-Optimized Campaigns](https://developers.openai.com/ads/conversion-optimized-campaigns), [synlig.ai](https://synlig.ai/en/guides/openai-pixel/)
- Campaign structure: [trucommerce.ai](https://trucommerce.ai/insights/openai-ads-manager-complete-guide), [receptivemedia.co.uk](https://www.receptivemedia.co.uk/openai-ads-manager-first-look/)
- B2B benchmarks: [obilityb2b.com](https://www.obilityb2b.com/blog/chatgpt-ads-best-practices-for-b2b-marketers/), [nakora.ai](https://nakora.ai/chatgpt-ads/conversion-rate-benchmarks), [firstpagesage.com](https://firstpagesage.com/seo-blog/chatgpt-ads-conversion-rate/), [stratezik.com](https://www.stratezik.com/blog/chatgpt-ads-benchmarks), [airops.com](https://www.airops.com/blog/chatgpt-ads-performance)
