# OnlyAIJobs — Paid Advertising Plan (Multi-Channel, Execution-Ready)

**Property:** onlyaijobs.eu (English + Dutch)
**Prepared:** 8 September 2026
**Companion documents:** [`google_ads_keywords_onlyaijobs.md`](./google_ads_keywords_onlyaijobs.md) · [`google_ads_rsa_copy_onlyaijobs.md`](./google_ads_rsa_copy_onlyaijobs.md) · [`seo_geo_plan_onlyaijobs.md`](./seo_geo_plan_onlyaijobs.md) · [`implementation_plan.md`](./implementation_plan.md) · [`onlyaijobs_info.md`](./onlyaijobs_info.md)
**Source data:** direct crawl of onlyaijobs.eu on 8 September 2026 (via GPTBot user-agent) · [`seo-geo-audit-onlyaijobs-eu-2026-09-08.md`](./seo-geo-audit-onlyaijobs-eu-2026-09-08.md)

---

## 1. Executive Summary

OnlyAIJobs is a two-sided marketplace with **52 vacancies, all of them roughly a month old, 40 employers, an empty blog, no analytics, and two of its most commercially important pages serving a blank admin shell**. The site has been invisible to Google for 39 consecutive days.

A conventional paid plan would open by allocating budget across Google, LinkedIn and Meta. That would be the wrong advice here, and this document does not give it.

**The single sentence that governs this plan: buy supply, not demand.**

Paying to send job seekers to a board with 52 stale listings does not build a marketplace — it burns the first impression of every person it reaches, and they do not come back. Every euro in the first phase goes to acquiring employers and vacancies. Job-seeker advertising is gated behind a supply threshold of 120 live listings, and the gate is not negotiable.

Three consequences:

1. **Phase 1 paid spend is small and entirely employer-facing** (€440–€800/month). The measurable outcome is not clicks or leads — it is *new vacancies published*.
2. **The cheapest supply channel is not advertising at all.** Direct outreach to the ~40 employers already listing, plus regional partners (Brainport Eindhoven, Midpoint Brabant, universities, gemeenten), will outperform paid acquisition per euro for at least the first six months.
3. **Nothing runs before measurement exists.** No GA4 or GTM was detected on the site. Spending without conversion tracking is not marketing, it is donation.

---

## 2. The Marketplace Sequencing Problem

| Stage | Supply | What paid spend should do | What it must not do |
|---|---|---|---|
| **Now (52 listings, stale)** | Critical | Acquire employers; make listing effortless | Advertise to job seekers |
| **120 live listings** | Thin but viable | Begin job-seeker acquisition in the strongest 3–5 cities | Go national |
| **300 live listings** | Workable | Scale job seekers; introduce retargeting | Chase EU-wide keywords |
| **1,000+ listings** | Real marketplace | Brand campaigns, aggregator partnerships | — |

**🇻🇳 Vì sao thứ tự này quan trọng**: người tìm việc quay lại một job board vì có tin mới; nhà tuyển dụng đăng tin vì có người tìm việc. Cả hai đều đúng, nhưng chỉ một phía có thể được mua bằng tiền một cách hiệu quả ở giai đoạn đầu — và đó là phía nhà tuyển dụng, vì họ chỉ cần một lý do (miễn phí, đúng đối tượng), trong khi người tìm việc cần một kho tin đủ lớn mới quay lại.

---

## 3. Prerequisites — None of This Runs Without Them

| # | Prerequisite | Status today | Blocks |
|---|---|---|---|
| 1 | GA4 + conversion tracking installed | ❌ Not detected | Everything |
| 2 | `/pages/info-for-employers` has real content | ❌ Serves blank admin shell | All employer campaigns |
| 3 | A vacancy submission flow (form, not just an email address) | ❌ Email only | Conversion measurement |
| 4 | Pricing decision beyond the free first listing | ❌ Undefined | Any ROI calculation |
| 5 | 120+ live vacancies | ❌ 52, all ~1 month old | All job-seeker campaigns |
| 6 | Per-job URLs + `JobPosting` schema | ❌ Neither exists | Retargeting, PMax, Google Jobs |

> **Item 3 deserves emphasis.** The current instruction is *"send an email with a link to the job listing to info@onlyaijobs.eu"*. Asking a recruiter to compose an email is a far higher-friction conversion than a form, and it produces no trackable conversion event. Replacing it with a two-field form (company URL + vacancy URL) is likely the highest-ROI change in this entire document, and it costs a day of development.

---

## 4. Channel Plan

### 4.1 Google Ads — Employer Side (Phase 1) 🥇

The full campaign and keyword build is in [`google_ads_keywords_onlyaijobs.md`](./google_ads_keywords_onlyaijobs.md). Summary:

| Campaign | Language | Budget | Target |
|---|---|---|---|
| `OAJ-Employers-NL` | 🇳🇱 | €400/month | `vacature plaatsen`, `gratis vacature plaatsen`, `ai specialist werven` |
| `OAJ-Employers-EN` | 🇬🇧 | €200/month | `post ai job`, `where to post ai vacancy`, `hire ai engineer netherlands` |
| `OAJ-Brand` | both | €40/month | Brand defence |

**Primary KPI: cost per new vacancy published.** Target under €80. If it exceeds €150, the problem is the landing page or the submission friction, not the bid — fix those before adding budget.

### 4.2 LinkedIn — Employer Side (Phase 1–2) 🥈

LinkedIn is the only channel where hiring managers at AI-employing companies can be targeted by title and company directly. For a supply-constrained marketplace this is more valuable than search, because it reaches employers who were not searching for a job board today.

| Campaign | Audience | Budget | Format |
|---|---|---|---|
| `LI-Employers-ABM` | Named account list: the ~40 companies already listing + 200 Dutch companies with AI roles on other boards. Titles: HR Manager, Recruiter, Talent Acquisition, CTO, Engineering Manager | €400/month | Single image + text ads |
| `LI-Employers-Broad` | NL + BE, company size 50–5,000, industries: Software, IT Services, Manufacturing, Logistics, Financial Services. Titles: Recruiter, Talent Acquisition, HR Manager | €300/month | Sponsored content |

**Message:** "You are paying Indeed per click for CVs that aren't AI people. Your first listing here is free."

> **Cách xây danh sách ABM rẻ nhất**: lấy đúng ~40 công ty đã đăng tin trên site (Accenture, Cegeka, Sendcloud, Mollie, Heijmans, Rexel, VINCI Energies, AMCS, Boltrics, Winparts, Hoppinger, WebNL, 4Dotnet…) làm hạt giống, rồi mở rộng bằng công ty tương tự. Họ đã đăng một tin — thuyết phục họ đăng tin thứ hai rẻ hơn nhiều so với tìm nhà tuyển dụng hoàn toàn mới.

### 4.3 Direct Outreach — Not Advertising, But the Best Supply Channel 🥇

Cheaper and higher-converting than any paid channel at this stage. Budget: staff time, not media spend.

| Target | Approach | Expected yield |
|---|---|---|
| The ~40 employers already listing | Email: "Your vacancy has been live for a month. Want to refresh it or add the other roles you're hiring for? Still free." | High — they have already said yes once |
| Dutch companies with AI roles posted elsewhere | Manual prospecting on Indeed/LinkedIn, then a one-line offer | Medium |
| Recruitment agencies specialising in data/AI | Bulk listing arrangement | High volume per contact |
| Regional bodies: Brainport Eindhoven, Midpoint Brabant, gemeenten, JADS, TU/e, Fontys, Tilburg University | Partnership framed around regional talent retention — **the founding story is literally their policy objective** | Very high strategic value; often free |

**🇻🇳 Đây là kênh bị đánh giá thấp nhất nhưng phù hợp nhất.** Câu chuyện "giữ nhân tài ở lại vùng thay vì chảy về Randstad" chính là mục tiêu chính sách của Brainport, Midpoint Brabant và các gemeente. Họ có ngân sách, có kênh truyền thông, và không cạnh tranh với OnlyAIJobs. Một quan hệ đối tác vùng có thể mang lại nhiều tin tuyển dụng hơn cả năm chạy Google Ads.

### 4.4 Meta & TikTok — Job Seeker Side (Phase 2, gated) 🥉

Only after 120 live listings.

| Campaign | Audience | Budget | Note |
|---|---|---|---|
| `META-Seekers-Regional` | NL, 22–35, interests: machine learning, data science, Python, AI; radius targeting around cities with ≥3 listings | €300/month | Radius targeting mirrors the product's own USP |
| `TIKTOK-Graduates` | NL, 20–27, education/tech interests | €200/month | Only if the graduate persona (A) is prioritised; creative must be native, not banner-style |

Creative angle for both: *"Je hoeft niet naar de Randstad te verhuizen"* — the founding story, which is emotionally specific in a way generic job-board ads are not.

### 4.5 Reddit & Communities — test only

r/Netherlands, r/cscareerquestionsEU, r/MachineLearning (no self-promotion allowed — participate, don't advertise), Dutch Slack/Discord data communities. €100/month test, kill within 60 days if cost per landing-page visit exceeds €3.

### 4.6 Channels explicitly NOT recommended now

| Channel | Why not |
|---|---|
| **Google Display / PMax** | No conversion history to optimise against; PMax needs conversion volume to function at all |
| **Job aggregator paid feeds** (Jooble, Talent.com) | Paying to send traffic to 52 stale listings |
| **X / Twitter** | Dutch job seekers and Dutch recruiters are not there |
| **Broad EU-wide campaigns** | 49/52 listings are in the Netherlands. Advertising EU-wide sells something the site does not have. |

---

## 5. Budget Tiers

### Tier 0 — Foundation (€0 media, 2–4 weeks)
Install GA4. Write the employer and job-seeker pages. Build the submission form. Start direct outreach. **No media spend.**

### Tier 1 — Supply Acquisition (€1,140/month)
| Line | Budget |
|---|---|
| Google Ads — `OAJ-Employers-NL` | €400 |
| Google Ads — `OAJ-Employers-EN` | €200 |
| Google Ads — Brand | €40 |
| LinkedIn — `LI-Employers-ABM` | €400 |
| Reddit/community test | €100 |
| **Total** | **€1,140** |

**Exit criterion:** 120 live vacancies and cost per new vacancy under €80.

### Tier 2 — Two-Sided (€2,600/month)
Adds: `LI-Employers-Broad` (€300), `OAJ-Seekers-NL-Role` (€500), `OAJ-Seekers-NL-City` (€300), `META-Seekers-Regional` (€300), plus a €60 increase in brand defence.

**Exit criterion:** 300 live vacancies, organic job-seeker sessions growing month over month.

### Tier 3 — Scale (€5,000/month)
Adds: English job-seeker campaigns, retargeting (requires per-job URLs), TikTok graduate campaign, and a 40% uplift on Tier 2 lines that are converting.

> **Spending discipline:** do not advance a tier until the current tier's exit criterion is met. A marketplace that scales advertising ahead of supply spends more to disappoint more people.

---

## 6. UTM Convention

```
utm_source   = google | linkedin | meta | tiktok | reddit | partner
utm_medium   = cpc | paid-social | referral | outreach
utm_campaign = oaj-<side>-<channel>-<lang>     e.g. oaj-employer-google-nl
utm_content  = <adgroup>-<asset>               e.g. age1-rsa1-h1a
utm_term     = {keyword}
```

`<side>` is either `employer` or `seeker` — **every URL must declare which side of the marketplace it is acquiring**, because the two have completely different conversion definitions and must never be blended into a single "conversions" number.

### Conversion events to define in GA4

| Event | Side | Definition |
|---|---|---|
| `vacancy_submitted` | Employer | Submission form completed (**the primary KPI**) |
| `employer_email_click` | Employer | Click on `info@onlyaijobs.eu` — the current fallback |
| `job_outbound_click` | Seeker | Click through to an employer's own vacancy page |
| `job_saved` | Seeker | "Saved jobs" interaction |
| `filter_used` | Seeker | Engagement signal, not a conversion |

---

## 7. KPIs

| Metric | Now | Tier 1 exit | Tier 2 exit | Month 12 |
|---|---|---|---|---|
| Live vacancies | 52 (all stale) | 120 | 300 | 800 |
| New vacancies/month | ~0 | 40 | 90 | 200 |
| Cost per new vacancy | n/a | < €80 | < €60 | < €40 |
| Active employers | ~40 | 70 | 150 | 350 |
| Job seeker sessions/month | unknown (no analytics) | 500 | 3,000 | 15,000 |
| Outbound clicks to employers | unknown | 150 | 1,200 | 6,000 |
| Repeat employers (posted ≥2 roles) | unknown | 15% | 30% | 45% |

**Repeat-employer rate is the health metric that matters most.** An employer who posts a second vacancy is telling you the first one worked. No amount of traffic growth compensates for that number staying at zero.

---

## 8. 90-Day Execution Checklist

### Weeks 1–3 — Foundation (no media spend)
- [ ] Install GA4 + define the five conversion events in §6
- [ ] Fix the WAF so Googlebot can reach the site (see the audit — outstanding for 39 days)
- [ ] Write real content for `/pages/info-for-employers` and `/pages/info-for-job-seekers`, in EN and NL
- [ ] Build a two-field vacancy submission form to replace the email instruction
- [ ] Decide pricing beyond the free first listing
- [ ] Email all ~40 current employers asking for a refresh or additional roles
- [ ] Open conversations with 3 regional partners (Brainport, Midpoint Brabant, one university)

### Weeks 4–7 — Employer acquisition
- [ ] Launch `OAJ-Employers-NL`, `OAJ-Employers-EN`, `OAJ-Brand`
- [ ] Launch `LI-Employers-ABM` against the seed list of 40 + 200 prospects
- [ ] Daily search-term review for the first 14 days
- [ ] Weekly measurement of the only number that matters: new vacancies published

### Weeks 8–12 — Evaluate and gate
- [ ] Assess cost per new vacancy; if above €150, pause media and fix conversion friction
- [ ] If live listings reach 120: open Tier 2 job-seeker campaigns in the 3–5 strongest cities only
- [ ] If listings stay below 120: keep all budget on supply, do not open job-seeker campaigns
- [ ] Reddit/community test verdict — continue or kill
- [ ] First partnership agreement signed

---

## 9. Risks

| Risk | Severity | Mitigation |
|---|---|---|
| **Job-seeker campaigns launched before supply exists** | 🔴 High | The 120-listing gate. This is the most likely way to waste the entire budget. |
| **WAF still blocking Google** | 🔴 High | Paid traffic works regardless of the WAF, but every euro of paid spend on a site invisible to organic search has no compounding effect. Fix first. |
| **No analytics** | 🔴 High | Nothing can be optimised. Install before spending. |
| **Email-only submission** | 🟡 Medium | High friction, untrackable. Replace with a form. |
| **Stale listings** | 🟡 Medium | Ads bring people to month-old jobs. Refresh before advertising. |
| **Unclear pricing** | 🟡 Medium | Cannot compute ROI on employer acquisition without knowing listing value |
| **Positioning conflict (EU vs regional NL)** | 🟡 Medium | Decide before Tier 2 — it determines geo targeting and language split |
| **Competing head-on with Indeed** | 🟡 Medium | Never bid on generic `vacatures`. Only niche AI terms and long-tail role+city. |

---

*OnlyAIJobs.eu · Plan based on a direct crawl performed 8 September 2026*
