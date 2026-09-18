---
Title: "AI App Security: Preparing for a Penetration Test"
Keywords: ai app security, penetration test, pentest preparation, scope, remediation, security report, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Scale-Up
---

# AI App Security: Preparing for a Penetration Test

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI App Security: Preparing for a Penetration Test",
  "description": "A customer's procurement asked for a pentest report. What a test actually covers, what to fix before paying for one, how to scope it, and what to do with the findings when they arrive.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-22",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-app-security-preparing-for-a-penetration-test" }
}
</script>

The request usually arrives in the same email as the data processing agreement: do you have a recent penetration test report?

For a founder whose product was built with AI tools over a few months, this is an uncomfortable question. It is also a solvable one, and the sequence matters — commissioning a test before doing the obvious work is an expensive way to be told what you already suspected.

A test costs between four and fifteen thousand euros for a small product. Paying that to discover exposed keys and missing authorisation checks is a poor use of the money.

## What a Test Is and Is Not

A penetration test is a time-boxed attempt by a professional to break your application, followed by a report describing what they found, how serious it is, and how to fix it.

It is not a certification. It is not a guarantee. It is a snapshot of a specific scope on a specific date, and a product that changes weekly is a product whose report ages quickly.

That matters for how you present it. "We had a test in March and remediated all findings" is a true and useful statement. "We are secure because we had a pentest" is neither, and experienced procurement people can tell the difference.

## Fix the Obvious Things First

Before commissioning anything, spend a week on what a competent tester will certainly find in an AI-built product. Each of these has been covered in this series and each is cheap compared to a report line describing it.

Secrets in the frontend bundle or in the repository. Storage buckets that are public. Missing authorisation checks on endpoints — the cross-account test, run systematically. Row-level security disabled or incomplete on any table. Webhook endpoints without signature verification. Session tokens in local storage. Unvalidated uploads. Enumeration in login and reset flows. Dependencies with known vulnerabilities in request-handling paths. Missing rate limits on authentication and expensive operations.

A day and a half of this typically removes most of what would otherwise fill the report's high-severity section, and it changes the economics of the test entirely: you are paying to find what you could not find yourself, rather than to be told what a checklist would have caught.

## Scoping Without Wasting Money

The scope decides both the price and the usefulness. Four decisions.

**What is included.** The web application, its API, the authentication flows, the database exposure. Usually not your marketing site. Be explicit about third-party services, which are generally out of scope and should not be tested without their permission.

**How much the tester knows.** Give them documentation, accounts at each permission level, and an architecture description. A tester who spends two days discovering your structure is a tester not spending two days attacking it. Black-box testing is appropriate for some purposes and is a poor use of a small budget.

**Which environment.** A staging environment identical to production, with realistic anonymised data, is the right answer. Testing against production risks real damage and real customer impact.

**Whether retesting is included.** It should be. Findings are fixed and then verified, and a report that states the fixes were confirmed is worth considerably more to a customer than one listing unresolved issues.

## Choosing Who Does It

Ask for a redacted example report. The difference between a good and a poor test is visible immediately: good reports explain the impact in business terms, give reproduction steps, and recommend specific fixes. Poor reports are a scanner's output with a cover page.

Ask what proportion is manual. Automated scanning finds a fraction of what matters; authorisation flaws — the most common serious issue in AI-built products — are found by a person reasoning about your application.

Ask who will do the work and what their experience is with your stack. And check whether they are used to working with small products: a firm whose engagements are usually banks may quote a process you neither need nor can absorb.

## During the Test

Give them working accounts before the start date, not on the morning. Tell them about known issues rather than letting them spend time rediscovering what you already plan to fix.

Warn whoever monitors your systems, so a testing burst is not treated as an incident. Agree a contact route for anything critical found mid-test — a serious flaw should reach you immediately, not in a report three weeks later.

And keep a normal deployment freeze during the window, or the report will describe code that no longer exists.

## The Report Is a Work Plan

A report will contain more findings than you expected and most will be low severity. Do not treat all of them equally.

Fix critical and high findings immediately, before the report is shared with anyone. Fix medium findings on a stated timeline. For low and informational findings, decide deliberately — some are worth fixing, some are acceptable risks, and a documented decision to accept a risk is a legitimate and professional answer.

Then produce the artefact your customers actually want: a summary stating when the test was done, by whom, what the scope was, how many findings there were by severity, that the critical and high findings were remediated and retested, and the date of the retest. One page. That is what goes to procurement, not the full report, which contains a map of your application and should be shared under an agreement if at all.

## What a Test Will Not Tell You

Three categories fall outside almost every engagement, and knowing that keeps you from mistaking a clean report for a complete picture.

**Your own operations.** Who has access to production, whether a departing contractor's credentials were removed, whether backups are tested, whether anyone would notice an incident at three in the morning. These are where a substantial share of real breaches begin and no external test touches them.

**Your suppliers.** The test covers your application, not your hosting platform, your database provider or the model API your AI feature calls. Their security is addressed through their own certifications and your contracts, not through your report.

**The code written after the test.** This is the awkward one for products built at speed. A test in March says nothing about an agent session in June, and in a product where features are added weekly the report describes something increasingly historical.

That last point argues for a specific habit rather than more testing. The self-review checklist you built while preparing — the cross-account test, the bundle scan, the bucket audit — should be run as a routine, ideally automated, rather than once. A test is a periodic external opinion; the routine is what keeps the answer true in between.

For most small products the sensible cadence is an annual test, quarterly self-review, and automated checks on every deployment.

## The Cheaper Alternatives, and When They Are Enough

A full engagement is not the only option, and for a product whose customers have not yet demanded one, three lighter approaches deliver a meaningful share of the value.

**A security code review.** An experienced engineer reads your application with access to the source, looking for the categories that matter. It is faster than a test, usually cheaper, and for AI-built products it frequently finds more — because the flaws are structural and visible in the code rather than subtle and behavioural.

**A scoped assessment.** Rather than the whole product, test the parts that matter most: authentication, authorisation, payments, file handling. Two or three days of specialist attention on the areas where a failure would be serious, at a fraction of the cost.

**A vulnerability disclosure policy.** A page stating that you welcome security reports, how to reach you, and that you will not pursue anyone acting in good faith. It costs nothing and it converts the person who finds a flaw in your product from someone who might publish it into someone who emails you. Several of the incidents described throughout this series reached the founder this way.

The order that suits most products: a disclosure policy immediately, a code review once you have paying customers, a scoped assessment when you handle anything sensitive, and a full test when a customer's procurement requires the report or when the product is large enough that its own behaviour has become hard to reason about.

## Setting This Up

Preparing properly is typically one to two weeks: the obvious findings remediated first through a systematic self-review, a staging environment with realistic anonymised data, documentation and accounts prepared at each permission level, scope defined with retesting included, a tester chosen on the basis of a sample report and manual proportion, a deployment freeze during the window, immediate triage of anything critical, remediation of high findings before sharing, a documented decision for each accepted low-severity risk, and a one-page summary for customers.

LaunchStudio does the preparation and the remediation, and works alongside the testing firm during the engagement. The engineers are Manifera's — eleven years, 120+ engineers, and a long history of being tested on behalf of clients including Vodafone, TNO and CFLW.

[Ask us to run the self-review first](https://launchstudio.eu/en/#contact). It is a fraction of the cost of finding the same things in a report.

## Real example

### Two Reports, Six Months Apart

Arnoud Steenbergen built Contractbeheer in Lovable: contract lifecycle management for facility management companies, 22 customers including three regional hospital groups.

A hospital procurement process required a penetration test report. He commissioned one immediately, for €7,500, from the first firm that answered.

The report contained 31 findings: 4 critical, 9 high. The critical ones were a service role key in the frontend bundle, a public storage bucket containing signed contracts, missing authorisation on 17 endpoints, and row-level security disabled on six tables. He had paid a specialist firm to tell him things a systematic self-review would have surfaced in a day, and he could not share the report with the hospital.

Then the preparation, and a second test: three business days of self-review and remediation covering keys, buckets, cross-account authorisation testing, row-level security, webhook verification, session storage, upload validation, enumeration, dependencies and rate limits; a staging environment built with anonymised production data; documentation and four accounts at different permission levels prepared; a second test scoped with retesting included, for €6,200, from a firm chosen after reading a redacted sample report and confirming that two thirds of the work was manual.

The second report contained 11 findings: 0 critical, 2 high — a business logic flaw allowing a contract approval step to be skipped through a direct API call, and a rate limiting gap on document generation. Neither would have been found by any checklist. Both were fixed in four days and retested.

**Result:** the one-page summary went to the hospital's procurement team and the contract was signed. Arnoud has since run a test annually, and reports that the second engagement was more valuable at lower cost because the testers spent their time on his application's actual logic rather than on a list of defaults.

> *"The first report told me my front door was open. I paid seven and a half thousand euros for that. The second one found something that genuinely needed a person to think about my product for a week."*
> — **Arnoud Steenbergen, Founder, Contractbeheer (Ede)**

**Cost & Timeline:** €4,900 for preparation and remediation (self-review across ten categories, staging environment with anonymised data, documentation and test accounts, post-report fixes) — completed in 7 business days, alongside a €6,200 external test.

## Frequently Asked Questions

### Should I get a pentest before or after fixing obvious issues?

After. A week of systematic self-review removes most of what a tester would otherwise report, so your budget buys findings you could not have discovered yourself.

### What should a test cost for a small product?

Typically four to fifteen thousand euros depending on scope, with retesting included. Be wary of quotes far below that, which usually indicate automated scanning with a cover page.

### Should testers be given documentation and accounts?

Yes. A tester spending two days mapping your application is two days not spent attacking it. Black-box testing is a poor use of a limited budget.

### Do I have to fix every finding?

No. Fix critical and high immediately, medium on a timeline, and decide deliberately on low and informational — a documented accepted risk is a legitimate answer.

### What do I actually send to customers?

A one-page summary: date, tester, scope, findings by severity, confirmation that high findings were remediated and retested. The full report maps your application and should not be circulated freely.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should I fix known issues before commissioning a pentest?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. A week of systematic self-review removes most predictable findings so the test buys insight you could not produce yourself."
      }
    },
    {
      "@type": "Question",
      "name": "What does a penetration test cost for a small product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually four to fifteen thousand euros with retesting included. Much cheaper quotes generally mean automated scanning with a cover page."
      }
    },
    {
      "@type": "Question",
      "name": "Should testers get documentation and accounts?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — time spent mapping your application is time not spent attacking it, and black-box testing wastes a small budget."
      }
    },
    {
      "@type": "Question",
      "name": "Must every finding be fixed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Critical and high immediately, medium on a timeline, and low findings decided deliberately with accepted risks documented."
      }
    },
    {
      "@type": "Question",
      "name": "What should be shared with customers after a test?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A one-page summary of date, tester, scope, severity counts and confirmed remediation. The full report maps your application."
      }
    }
  ]
}
</script>
