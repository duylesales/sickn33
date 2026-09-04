---
Title: "What a Real Security Audit Report Looks Like — and What a Fake One Looks Like"
Keywords: security audit report, penetration test report, AI code security review, vulnerability findings, scanner output vs audit, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# What a Real Security Audit Report Looks Like — and What a Fake One Looks Like

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What a Real Security Audit Report Looks Like — and What a Fake One Looks Like",
  "description": "A genuine security audit report contains findings with file or route references, reproduction steps, evidence and specific remediation, while a fake one is a scanner dump in a PDF wrapper. This is how to tell them apart before you pay for one or hand one to a customer.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2027-01-12",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/what-a-real-security-audit-report-looks-like"
  }
}
</script>

The PDF arrives on a Thursday. Thirty-one pages, your logo on the cover, a green banner reading **SECURITY ASSESSMENT — PASSED**, and inside, page after page of a table you half-recognise: package name, installed version, fixed version, CVE identifier, severity. Fourteen Highs, most of them in transitive dependencies of a build tool that never runs in production. Then two pages of general recommendations about enabling HTTPS and using strong passwords, and a signature block.

That document cost €1,900 and it is worth approximately nothing, because it is `npm audit` and a dependency scanner in a Word template. It contains no evidence that anyone opened your code. And here's the uncomfortable part: it will still be enough to satisfy some enterprise procurement checklists, which is exactly why this market exists.

If you're going to buy an audit — or accept one from a partner as proof they know what they're doing — you need to be able to grade the artifact itself.

## Automated Tooling Is an Input, Not a Deliverable

Nobody serious avoids scanners. `npm audit`, Dependabot, Snyk, Trivy, Semgrep, `gitleaks`, OWASP ZAP's baseline scan and `nuclei` all belong in the workflow, and a report that ignored dependency CVEs entirely would also be incomplete. The distinction isn't tools versus no tools. It's whether a human took the tool output and did something with it.

The thing a human does is **triage for reachability**. A critical CVE in `lodash` matters if the vulnerable function is called with user input on a live route; it doesn't matter if the package is only pulled in by a dev-time bundler that never ships. A report listing fourteen Highs without saying which ones are reachable from your application's actual entry points has skipped the entire job and handed you the raw material as though it were the finished work.

The second thing a human does is find the class of bug no scanner finds. For AI-generated applications this is decisive, because the characteristic vulnerabilities of Lovable, Bolt, v0 and Cursor output are almost all **business-logic authorisation failures**, and automated tools cannot detect them. A scanner has no idea that `/api/invoices/:id` should only return invoices belonging to the requesting organisation. It sees a 200 response and moves on. Roughly 45% of AI-generated code ships with security vulnerabilities, and the ones that end up in incident reports are overwhelmingly of this kind: object-level authorisation, tenant isolation, mass assignment, price tampering, unverified webhooks — not an outdated `axios`.

## The Anatomy of a Real Finding

A genuine report is a collection of findings, and every finding has the same eight parts. This is the shape you're checking for:

1. **Identifier and title** — stable reference (`FIND-004`), one specific sentence
2. **Severity, with the reasoning** — a CVSS v3.1 vector string, or a stated rubric with impact and likelihood assessed separately for *your* deployment, not a generic score copied from a database
3. **Affected asset** — the file and line, the route and method, the table, the bucket. Named.
4. **Preconditions** — who can exploit this: anonymous, any authenticated user, a user of a different tenant, an admin
5. **Reproduction** — the exact request. Copy-pasteable.
6. **Evidence** — the redacted response proving it worked
7. **Impact** — what an attacker gets, stated in terms of your business
8. **Remediation** — the specific change, not a link to an OWASP cheat sheet

Here's what one looks like written out properly:

```
FIND-004 — Broken object-level authorisation on invoice retrieval
Severity: High (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N — 7.7)
Affected: app/api/invoices/[id]/route.ts:14–29 (GET)
Preconditions: any authenticated user with any active account

The handler loads the invoice by primary key and returns it without
checking that invoice.organisation_id matches the caller's organisation.
The organisation filter exists in the frontend query hook only
(lib/hooks/useInvoices.ts:22), which the client controls.

Reproduction:
  1. Authenticate as user@tenant-b.example (org_id 88)
  2. GET /api/invoices/4193
     Authorization: Bearer <tenant-b token>
  3. Response 200 with invoice belonging to org_id 41

Evidence: 200 OK, body contains {"id":4193,"organisation_id":41,
"customer_name":"[REDACTED]","total_cents":184500,...}

Impact: any registered user can enumerate sequential IDs and read every
invoice in the system, including customer names, amounts, and billing
addresses across all 60 tenant organisations. Sequential integer IDs make
full extraction trivial (~4,200 requests).

Remediation: add the organisation filter to the server-side query
(.eq('organisation_id', session.org_id)) and enable row-level security on
public.invoices so the constraint is enforced at the database rather than
in a single handler. Re-verify with the tenant-b token expecting 404.

Retest 2027-01-22: PASSED — returns 404.
```

You could hand that to any competent developer and they'd fix it in twenty minutes. That's the test. **A finding is real if it's actionable without asking the auditor a question.**

## Side by Side

| | Real audit | Scanner dump in a PDF |
|---|---|---|
| Findings reference | File paths, line numbers, routes, tables | Package names only |
| Reproduction | Exact requests, roles used, expected vs actual | Absent, or "see tool output" |
| Evidence | Redacted responses, screenshots of the actual app | Screenshot of the tool's dashboard |
| Severity | Rated for your deployment, reasoning shown | Copied from the CVE database |
| Business logic | Access control, tenancy, payment flows tested by hand | Not covered at all |
| Scope statement | What was and wasn't tested, credentials, dates | "Full application security scan" |
| False positives | Explicitly dismissed with reasons | Everything included to inflate the count |
| Remediation | Specific code or config change | Generic advice, often copy-pasted |
| Retest | Section with dates and pass/fail per finding | None |

## The Scope Statement Is Where Honest Reports Are Honest

Flip to the methodology section. A real one tells you what *wasn't* done, which is the part that establishes credibility:

> Tested: the web application at staging.example.com between 6 and 9 January 2027, authenticated as three roles (anonymous, member, org-admin) using accounts provided by the client; the Supabase project's RLS policies and storage bucket ACLs; the Stripe webhook handler; and the repository at commit `a3f19c2`.
>
> Not tested: denial-of-service and load behaviour; the marketing site; third-party SaaS integrations beyond the boundary of our request; physical and social engineering; mobile clients. No source code was available for the `pdf-render` microservice, which was tested black-box only.

Any report that claims full coverage without naming a time box, a commit hash, an environment and a set of roles is claiming something no assessment can deliver. Time-boxed work is the norm; pretending otherwise is the tell.

Similarly, a legitimate "no significant findings" result is possible — but it reads like *"within the scope and eight hours described above, we found three Low and no High or Critical issues; note that tenant isolation could only be partially assessed because we were given accounts in a single organisation."* It never reads like a green PASSED banner.

## Five Tells You Can Check in Ninety Seconds

Before reading a single finding in detail:

**Search the PDF for a `/` character in a code font.** If there are no file paths or route paths anywhere in the document, nobody read your code.

**Search for "curl" or "POST" or "Authorization".** No requests means no reproduction means no verification.

**Check whether any finding is marked as a false positive or informational-only.** Real triage always dismisses something. A report where every scanner hit survived to the final document didn't triage.

**Look for the retest section.** Its absence isn't fatal — retests are often a separate engagement — but its presence is a strong positive signal, because it means they intend to be measured on whether the fixes worked.

**Read the executive summary and ask whether it names your top three risks in plain sentences.** "The most serious issue is that any logged-in user can read every other customer's invoices" is an executive summary. "The application demonstrates a moderate security posture with opportunities for improvement" is filler.

## Reproduce One Finding Yourself

This is the strongest verification available to you, and it costs an evening. Pick one finding — ideally a Medium, since Criticals may have been fixed already — and follow its reproduction steps against your own staging environment. Either you see what the report says you'll see, or you don't.

If the steps don't work, that's not automatically fraud; environments drift and a finding from three weeks ago may have been incidentally fixed. But ask, and grade the answer. An auditor who says *"that route was changed in commit 9d2 — here's the same class of issue still present at `/api/exports`"* is real. An auditor who becomes vague is not.

The same technique works on a *partner's* audit report from a previous project, offered to you as proof of competence during vetting. Ask them to walk you through one finding from it — redacted, obviously — and explain why they rated it the severity they did. Someone who wrote it will happily argue about the CVSS vector. Someone who bought a template won't know what a CVSS vector is.

## Audit, Pen Test, Code Review, Attestation — Four Different Things

Be precise about what you're buying, because the words get used interchangeably by sellers and not by buyers:

- **Secure code review** — a human reads the source, usually with Semgrep or CodeQL assistance. Best value for AI-generated codebases, because most of the real bugs are visible in the source and cheap to find there.
- **Penetration test** — black or grey box testing of the running application. Finds what's actually exploitable, including configuration issues invisible in source. Typically €4,000–€15,000 from a specialist firm for a small app.
- **Vulnerability scan** — automated, continuous, cheap, and appropriate as a baseline. Should cost tens of euros a month, not thousands per report.
- **Attestation / letter of assurance** — a one-page summary an enterprise customer's procurement team can file. It's a *summary of* an assessment, and worthless without the assessment behind it.

An enterprise prospect asking for "your latest security report" usually wants the attestation letter plus a redacted findings summary. Have both; don't buy the letter alone.

## Where a Practical Middle Sits

For a solo founder with an AI-built product and a first enterprise prospect, a full pen test is often premature and a scanner subscription alone is insufficient. The productive middle is a human code review focused on the failure classes AI tools actually produce — object-level authorisation, RLS policies, tenant scoping, webhook verification, secrets in the client bundle, mass assignment — delivered as findings you can act on, followed by fixes.

That's the shape of the security work inside [LaunchStudio's](https://launchstudio.eu/en/) hardening engagements, which sit in the €800–€3,500 range and run one to three weeks; the reviewers are the same engineers who handle security work at [Manifera](https://www.manifera.com/about-us/manifera-technologies/), whose eleven years of enterprise delivery is the reason the reports come with reproduction steps rather than a badge. If you'd rather use an independent specialist firm for the assessment and someone else for the fixes, that's a perfectly good structure too — arguably a cleaner one, since the auditor has no incentive to find work for themselves.

**Send us a real report you've been handed and we'll tell you, free, whether it's an assessment or a scanner dump — or bring us a repo and talk to an engineer who reads AI-generated code for a living.**

## Real example

### An Indie Hacker in Action: The Report That Failed Its Own Reproduction Steps

Ruben Hoekstra, a solo developer in Groningen, built ShiftLedger — a Cursor-assisted shift-scheduling tool for hospitality groups — and bought a €1,600 "security assessment" to satisfy a hotel chain's vendor questionnaire. The report listed nineteen findings, seventeen of them npm dependency CVEs, and gave the application an overall rating of "Low Risk."

Ruben tried to reproduce two findings and couldn't, because neither had reproduction steps. What made him uneasy was different: the report said nothing about authorisation at all, and he knew his own `/api/shifts` route filtered by venue in the React Query hook rather than on the server. He tested it himself with a second account. It returned every venue's shifts, including hourly rates.

A second reviewer, given the repository, produced eleven findings with file references — the shifts route, a storage bucket set to public, an unverified Mollie webhook that accepted a forged paid status, and RLS disabled on four tables.

**Result:** ShiftLedger's authorisation moved server-side with RLS enforced at the database, the webhook was signature-verified, and Ruben passed the hotel chain's review with a real findings summary plus a retest page — for €2,700, delivered in eight working days.

> *"The first report gave me a Low Risk rating for an app where anyone with an account could read every hotel's wage data. The second one gave me eleven problems and a bad afternoon, which is what I'd actually paid for."*
> — **Ruben Hoekstra, Founder, ShiftLedger (Groningen)**

---

## Frequently Asked Questions

### Is a CVSS score required for a report to be legitimate?

Not required, but a stated severity *rubric* is. Some firms use a simple impact-times-likelihood matrix and explain it clearly, which is fine — what's not fine is a severity number with no method behind it, or a CVSS score with no vector string, since the vector is where the reasoning lives.

### How much should a genuine security review of a small AI-built app cost?

A focused human code review of a single-product codebase typically lands in the low four figures; a full black-box penetration test from a specialist firm generally starts around €4,000 and rises with scope. Anything offering a "full audit" for a few hundred euros is selling you scanner output.

### Should the same company fix the issues it found?

It's efficient and common, and it's also a mild conflict of interest. The mitigation is a report specific enough that any developer could act on it — which is another reason to insist on file references and reproduction steps, since they make the findings portable to a second opinion.

### What do I actually send an enterprise customer who asks for security documentation?

Usually a one-page attestation naming the scope, dates and headline result, plus a redacted findings summary showing counts by severity and remediation status. Sending the full report with file paths and reproduction steps to a prospect is oversharing and occasionally dangerous.

### My app is on Supabase and the dashboard says everything is green. Isn't that enough?

The dashboard tells you the platform is healthy, not that your policies are correct. The most common serious finding in Supabase-backed prototypes is RLS disabled or written permissively on tables the client queries directly — a green dashboard is entirely compatible with every row being readable by any authenticated user.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is a CVSS score required for a report to be legitimate?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not required, but a stated severity rubric is. A simple impact-times-likelihood matrix explained clearly is fine; a severity number with no method, or a CVSS score with no vector string, is not."
      }
    },
    {
      "@type": "Question",
      "name": "How much should a genuine security review of a small AI-built app cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A focused human code review of a single-product codebase typically lands in the low four figures, while a full black-box penetration test from a specialist firm generally starts around 4,000 euros. A few hundred euros buys scanner output."
      }
    },
    {
      "@type": "Question",
      "name": "Should the same company fix the issues it found?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It is efficient and common, and also a mild conflict of interest. The mitigation is a report specific enough that any developer could act on it, which makes the findings portable to a second opinion."
      }
    },
    {
      "@type": "Question",
      "name": "What do I actually send an enterprise customer who asks for security documentation?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually a one-page attestation naming scope, dates and headline result, plus a redacted findings summary with counts by severity and remediation status. Sending the full report with file paths and reproduction steps to a prospect is oversharing."
      }
    },
    {
      "@type": "Question",
      "name": "My app is on Supabase and the dashboard says everything is green. Isn't that enough?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The dashboard shows the platform is healthy, not that your policies are correct. The most common serious finding in Supabase-backed prototypes is row-level security disabled or written permissively on tables the client queries directly."
      }
    }
  ]
}
</script>
