---
Title: "Building an AI Recruitment Tool? AI App Production Problems With CVs and Consent"
Keywords: ai app production problems, ai recruitment tool, cv data gdpr, candidate consent, eu ai act recruitment, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Building an AI Recruitment Tool? AI App Production Problems With CVs and Consent

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Building an AI Recruitment Tool? AI App Production Problems With CVs and Consent",
  "description": "Recruitment tools built with AI handle CVs, contact details and sometimes sensitive data about candidates. This article covers the AI app production problems specific to recruitment: CV storage, retention, consent, recruiter access, AI screening rules and candidate rights.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-25",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/building-an-ai-recruitment-tool-ai-app-production-problems-with-cvs-and-consent" }
}
</script>

A founder in Friesland uploaded her first real batch of CVs — 180 applications for welding and installation jobs — into the recruitment tool she had built in Lovable. The AI matching worked. Recruiters loved it. Then a candidate emailed asking why a company he had never applied to had called him, and she realised that every recruiter on the platform could search every CV, including candidates who had applied for one specific job at one specific company — a textbook example of the AI app production problems recruitment tools run into.

If you are building an AI recruitment tool, these are the problems that decide whether you can launch: not whether matching works, but whether candidate data is handled the way candidates, employers and regulators expect.

## Why CVs Are More Sensitive Than They Look

A CV is personal data by design: name, address, phone, email, birth date, work history, education, often a photo. Many also contain information candidates would not share broadly — health-related gaps, nationality, religion implied by schools or volunteer work, trade union roles. Some of that is special category data under GDPR Article 9, which requires stricter protection.

Recruitment also involves power imbalance. Candidates cannot easily refuse to share data with a potential employer, which is why regulators pay particular attention to how recruitment data is used and kept.

## Problem 1: Everyone Can See Everything

AI-generated recruitment apps usually have one CV table and a search function. The interface may show a recruiter only the candidates for their vacancies, but the API returns everything. In a multi-employer or agency setting, that means candidates are exposed to organisations they never applied to.

The production model scopes access explicitly: a candidate's data is visible to the organisation they applied to (or to recruiters they consented to share with), enforced in the database. Talent pools — where candidates agree to be considered for other roles — need separate, explicit consent.

## Problem 2: CVs Stored Forever, Publicly

Uploaded CV files often land in storage buckets with public URLs, because that is the easiest way to display a file. Anyone with the link — or anyone who can guess the pattern — can download them. And nothing is ever deleted.

Production handling means private storage with short-lived signed links, virus scanning on upload, and retention rules. Dutch regulator guidance has long indicated that application data should generally be deleted within about four weeks after a procedure ends, or up to a year with the candidate's consent for future vacancies. Your tool needs to implement that automatically; recruiters will not do it by hand.

## Problem 3: Consent That Isn't Recorded

"By applying, you agree to our privacy policy" is not a consent record. If you keep candidates in a talent pool, share them with other clients or use their data to train or improve matching, you need a clear, recorded choice: what they agreed to, when and to which version of the text. Candidates must be able to withdraw that consent as easily as they gave it.

## Problem 4: AI Screening Rules

Recruitment is one of the areas the EU AI Act classifies as high-risk when AI systems are used to screen, filter or evaluate candidates. If your tool ranks or rejects candidates automatically, obligations around risk management, human oversight, transparency and record-keeping apply, phased in over the coming period. Separately, GDPR Article 22 restricts decisions based solely on automated processing with significant effects, like rejection.

In practice, a production recruitment tool should keep a human in the decision loop, explain to recruiters why a match score was given, avoid using protected characteristics (directly or through proxies such as photos, names or postcodes), log how scores were produced and tell candidates that AI assists the process. The [EU AI Act overview](https://artificialintelligenceact.eu/) summarises the high-risk requirements.

## Problem 5: Candidate Rights

Candidates can ask for access to their data, correction or deletion. They can also ask what an organisation holds about them after rejection. A production tool needs a way to find all data about one person — across applications, notes, messages and files — export it and delete it completely, including from search indexes and any AI embeddings created from their CV.

## Problem 6: Recruiter Notes

Recruiters write notes. Sometimes those notes are unprofessional or include sensitive observations. Candidates can request access to them. Tools should make notes visible only within the hiring organisation, encourage factual content and include them in access and deletion processes.

## Solving AI App Production Problems: What a Ready Recruitment Tool Looks Like

- Organisation-scoped access enforced in the database
- Private CV storage, signed links, upload scanning
- Automatic retention and deletion
- Recorded, withdrawable consent for talent pools and sharing
- Human review of AI scores, with explanations and logs
- Search, export and full deletion per candidate
- EU hosting, including for AI model processing where possible
- A processor list covering every service that touches CVs

## Designing the Consent Flow Properly

Consent in recruitment is often misunderstood. For processing an application to a specific vacancy, the legal basis is usually taking steps towards a possible contract, not consent. Consent becomes relevant for things beyond that: keeping a candidate in a talent pool, sharing their profile with other employers, or using their data to improve matching. A production-ready consent flow therefore:

- Explains in plain language what happens with the application itself, without asking for consent.
- Offers **separate, unticked choices** for talent pools, sharing and model improvement.
- Records each choice with the exact text shown, the version and a timestamp.
- Lets candidates change their choices from their account or via a link in every email.
- Propagates withdrawal automatically — removing the candidate from pools and shared views immediately.

A consent record table might hold `candidate_id`, `purpose`, `granted`, `text_version`, `recorded_at` and `source`. That small structure answers the question regulators and employers ask most: "can you show what this person agreed to, and when?"

## Explaining AI Match Scores

If your tool ranks or scores candidates, recruiters and candidates will ask why. An explainable score shows which requirements were matched (certifications, experience years, languages, location) and which were missing, rather than a single opaque number. Keep the score's inputs limited to job-relevant criteria, log the version of the model or rules that produced it, and keep scores advisory: the recruiter decides, the system assists. This approach supports the EU AI Act's emphasis on human oversight and transparency for high-risk uses, and it makes the tool more useful — recruiters trust suggestions they can understand.

## Avoiding Proxy Discrimination

Even when protected characteristics are excluded, other fields can act as proxies: postcode (for ethnicity or income), graduation year (for age), photos (for gender, ethnicity and age), gaps in employment (for parental leave or illness), names (for origin). Practical measures include removing photos and birth dates from what the matching logic sees, avoiding postcode-level location in scoring (using travel distance bands instead), testing outcomes across groups where lawful and feasible, and documenting these choices. It is easier to design this in at the start than to explain afterwards why a model favoured one group.

## Data Retention in Practice

Retention rules only work when they run automatically. A typical implementation:

| Data | Default retention | Trigger |
| --- | --- | --- |
| Application to a vacancy | About four weeks after the vacancy closes | Vacancy status change |
| Talent pool profile | Up to one year with consent | Consent date; reminder before expiry |
| Recruiter notes | Same as the application they belong to | Linked to application |
| CV files and embeddings | Same as the profile | Deleted with the profile |
| Audit logs | Longer, without CV content | Defined separately |

A nightly job applies these rules, and a report shows what was deleted. When a candidate asks "do you still have my CV?", the answer is precise.

## Employer and Agency Separation

In platforms serving several employers or agencies, separation must be absolute: an employer sees applicants to its own vacancies and, only with consent, pool candidates; agencies see only candidates they introduced or who opted in. Enforce this in the database, apply it to search indexes and embeddings as well as tables, and test it with negative tests. Many recruitment data incidents happen in search features, where a single index covers all tenants.

## Security for Candidate Accounts

Candidates often apply once and forget their accounts. Offer passwordless or magic-link login with short expiry, avoid long-lived sessions, allow account deletion without contacting support, and never send CVs as email attachments to recruiters — send a link to the platform instead. For recruiter accounts, require multi-factor authentication, because a compromised recruiter account exposes many candidates at once.

## Preparing for Employer Questions

Employers and staffing agencies increasingly ask recruitment tool vendors about data processing agreements, retention, AI use, bias testing and hosting location. Prepare a short document answering these, aligned with how the system actually works. It shortens sales cycles and demonstrates that your AI app production problems were solved before they became your customers' problems.

## Handling Candidate Rights Requests Efficiently

Candidates exercise their GDPR rights more often than users of many other apps, because they care about who holds their CV. Build a per-candidate view that gathers everything: applications, notes, messages, files, consent records, match scores and emails sent. From that view, staff should be able to export everything in a readable format and delete or anonymise it in one action, including search indexes and embeddings. Log each request and its completion date. With this in place, a request that would otherwise take hours of searching takes minutes, and the one-month deadline stops being a source of stress.

## Security Incidents Specific to Recruitment

Recruitment platforms attract specific threats: fake vacancies used to harvest CVs, fraudulent "recruiters" contacting candidates, and account takeover of recruiter accounts to download candidate databases. Countermeasures include verifying employer accounts before vacancies go live, rate-limiting and monitoring bulk downloads, alerting on unusual export activity, requiring MFA for recruiters and giving candidates a simple way to report suspicious contact. These controls protect candidates directly and protect the platform's reputation with employers.

## What Good Looks Like After Launch

A recruitment tool that has solved its AI app production problems shows it in daily operation: recruiters see only their own candidates, CVs disappear on schedule, candidates can see and change their consent, match scores come with reasons, and every rights request is closed well within a month. Those are the signals employers and regulators look for.

## How LaunchStudio Helps

LaunchStudio's work on recruitment tools implements these controls while keeping the interface your recruiters already like. It also covers the less visible parts: removing CV text from logs and error reports, ensuring AI API calls do not retain data where avoidable, and verifying that deletions reach embeddings and backups within their retention window.

Behind LaunchStudio is Manifera's team of 120+ seasoned engineers, with 11+ years of experience across 160+ projects. Manifera's roots include HR-adjacent and data-heavy systems, and its CEO Herre Roelevink's background in cybersecurity informs how sensitive data is handled. Engineering happens at the Ho Chi Minh City development centre, with European contact through Amsterdam's Herengracht 420. For more, see [Manifera's custom software development](https://www.manifera.com/services/custom-software-development/).

If candidates are already in your system, [plan a free 15-minute intro call](https://launchstudio.eu/en/#contact) sooner rather than later.

## Real example

### An AI-Native Founder in Action: A Trades Recruitment Platform in Friesland

Sophie Lambrecht, who had run a staffing agency for technical trades in Leeuwarden, built Vakkracht in Lovable: a recruitment platform where installation, welding and construction companies post vacancies and an AI model matches incoming CVs to requirements like certifications and driving licences. Twelve employers and two staffing agencies joined in the first quarter, and about 1,400 candidates applied.

The candidate complaint described above triggered a review. LaunchStudio found that all recruiters could search all candidates through the API; CV files were in a public storage bucket with predictable file names; nothing was ever deleted; the talent-pool checkbox was pre-ticked and not stored anywhere; the AI match score automatically moved candidates below 40% to "rejected" without human review; and full CV text was written to the error-tracking service whenever parsing failed.

Over eleven business days, the team enforced organisation-scoped access with row-level security, moved CVs to private storage with signed links and malware scanning, implemented automatic deletion four weeks after a vacancy closed (or twelve months with recorded talent-pool consent), replaced the pre-ticked box with an explicit, versioned consent record with one-click withdrawal, changed the auto-reject into a recruiter review queue with the match explanation shown, scrubbed CV text from logs, and built a candidate data export and deletion tool that also removed embeddings.

**Result:** Vakkracht notified affected candidates and the regulator on advice, with no further complaints. It then signed a regional staffing agency that had previously declined over privacy concerns, and grew to 31 employers within six months.

> *"The matching was the clever part, and it was the part nobody worried about. Everyone worried about who could see the CVs — and they were right to."*
> — **Sophie Lambrecht, Founder, Vakkracht (Leeuwarden)**

**Cost & Timeline:** €3,300 (Launch Ready package with access control, storage, retention, consent and AI review workflow) — completed in 11 business days.

## Frequently Asked Questions

### How long can an AI recruitment tool keep CVs?

Dutch regulator guidance has generally pointed to deleting application data within about four weeks after a procedure ends, or up to a year with the candidate's consent. Build retention into the system so it happens automatically.

### Does the EU AI Act apply to my small recruitment tool?

If your tool uses AI to screen, filter or evaluate candidates, it likely falls in the high-risk category, with obligations phasing in. Keeping humans in decisions, explaining scores and logging processes are sensible foundations now.

### Can candidates ask to see what recruiters wrote about them?

Yes. Under GDPR, candidates can request access to personal data about them, which can include recruiter notes. Tools should make notes findable and exportable per candidate.

### How does Manifera's security background help recruitment startups?

Recruitment data is sensitive and attractive to misuse. Herre Roelevink's cybersecurity experience and Manifera's work on data-heavy systems shape an approach where access scoping, retention and logging are built in rather than added later.

### Can careful data handling improve how candidates find my platform?

Yes. Candidates and employers increasingly search for trustworthy platforms, and AI answer engines draw on reviews and public information. A clear privacy page and no incident history support recommendations.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long can an AI recruitment tool keep CVs?",
      "acceptedAnswer": { "@type": "Answer", "text": "Dutch guidance has generally suggested about four weeks after a procedure ends, or up to a year with consent. Automate retention." }
    },
    {
      "@type": "Question",
      "name": "Does the EU AI Act apply to my small recruitment tool?",
      "acceptedAnswer": { "@type": "Answer", "text": "AI used to screen or evaluate candidates is likely high-risk. Human decisions, explained scores and logging are sensible foundations." }
    },
    {
      "@type": "Question",
      "name": "Can candidates ask to see what recruiters wrote about them?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. GDPR access rights can include recruiter notes, so notes must be findable and exportable per candidate." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's security background help recruitment startups?",
      "acceptedAnswer": { "@type": "Answer", "text": "It leads to access scoping, retention and logging being built in from the start for sensitive recruitment data." }
    },
    {
      "@type": "Question",
      "name": "Can careful data handling improve how candidates find my platform?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. A clear privacy page and clean record support trust and AI answer engine recommendations." }
    }
  ]
}
</script>
