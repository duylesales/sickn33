---
Title: "Lovable Security Review: What It Actually Involves"
Keywords: ai app security, lovable security, security review process, penetration test versus code review, remediation report, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable Security Review: What It Actually Involves

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Security Review: What It Actually Involves",
  "description": "What happens during a review of an AI-generated application: the five areas examined, the difference between a review and a penetration test, what the report contains, and how to read findings without panicking.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-11",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/what-a-security-review-actually-looks-like" }
}
</script>

Founders imagine a security review as something between an exam and an audit: an expert disappears with the code and returns with a verdict. The reality is more useful and considerably less dramatic. It is a structured attempt to behave badly in your product, followed by a list of what worked, ordered by how much it would cost you.

Knowing the shape in advance makes the exercise far less intimidating, and it helps you tell a serious review from a scan report with a logo on it.

## What It Is and What It Is Not

**A security review** examines how your application is built and configured: who can reach what data, where credentials live, how access rules are expressed, what happens with uploads and payments, and whether the infrastructure around it is sound. It is done with access to the code and the accounts, which is what makes it efficient.

**A penetration test** attacks the running system from outside, usually without that access, simulating what an external attacker could achieve. It answers a different question and is normally what an enterprise customer means when they ask for one.

**An automated scan** runs tooling against your dependencies and endpoints. It is cheap, useful for known vulnerable libraries, and incapable of finding the flaw that matters most in AI-built products — that one customer can read another's records — because no scanner knows what your data means.

For a small product, the review is the right first step, because the findings in AI-generated applications are overwhelmingly design and configuration rather than exotic vulnerabilities.

## The Five Areas Examined

**Access control.** Can an authenticated user reach data that is not theirs, by changing an identifier, calling an endpoint directly, or exploiting a missing rule on a table nobody thought about? In multi-tenant products, can one organisation reach another's records? This is where most serious findings live.

**Credentials and configuration.** What is published in the frontend bundle, what is in the repository and its history, where secrets are stored, whether keys are scoped and rotatable, and whether anything metered is uncapped.

**Data handling.** Where data is stored geographically, what is retained and for how long, whether deletion works, what third parties receive, and whether uploads are validated, private and stripped of metadata.

**The money and identity paths.** Whether payments complete reliably including the abandoned cases, whether entitlement follows payment state, whether sessions expire and invalidate correctly, and whether roles can be self-granted.

**Operational readiness.** Backups that restore, monitoring that alerts, logging that would let you answer "who accessed this and when", and a deployment process with a rollback.

A review that covers only the first two is a partial review. The last one is skipped most often and is what determines whether you could answer a customer after an incident.

## How It Is Actually Done

Mostly by using your product adversarially, with the code open alongside.

Two accounts are created and used properly, then each tries to reach the other's data through every path the product offers. Requests are observed in a browser's developer tools and replayed with values changed. The published bundle is searched for credentials. The repository history is examined. Database access rules are read table by table and tested by attempting to bypass them. A live payment is made and deliberately abandoned. A file is uploaded that is not what it claims to be. A backup is restored into a scratch environment and verified.

None of it requires exotic tooling. It requires someone who has seen where these products break and who is systematic about trying.

## What the Report Should Contain

A useful report has five properties, and a report missing them is a document rather than a deliverable.

**Findings ordered by business impact,** not by technical severity in the abstract. "Any customer can read every other customer's records" outranks an outdated library with no known exploit path in your usage.

**Evidence for each.** The exact request, the exact response, reproducible by you. A finding you cannot reproduce is an opinion.

**A concrete remediation** per finding, specific to your stack rather than a link to a general article.

**An honest severity assessment,** including findings that are theoretically true and practically irrelevant. Reports that grade everything as critical are selling urgency.

**What was checked and found sound.** This half matters: it is what you show a customer, and it tells you where you do not need to spend money.

## Reading Findings Without Panicking

Nearly every AI-built product produces findings. The number is not the signal; the categories are.

**Findings you must fix before customers arrive:** anything in access control, exposed credentials, unvalidated payment paths.

**Findings to fix soon:** missing rate limits, weak session handling, uploads without restrictions, absent monitoring.

**Findings to note and schedule:** dependency versions, hardening measures, defence in depth on paths already protected.

**Findings that do not apply:** every report contains some. A good reviewer says so rather than padding the list.

A first review typically produces between eight and twenty items across those categories. That is normal, and it is a sign that the review was thorough rather than that your product is unusually bad.

## What Happens After

The review is half the engagement. Remediation is the other half, and the useful pattern is to fix in the order above, verify each fix by reproducing the original finding and confirming it now fails, and then record what was fixed and what was deliberately accepted.

That record is worth as much as the fixes. It is what you hand to the next customer's privacy officer, what you give to the next engineer, and what prevents the same finding being rediscovered at your expense in a year.

## When to Have One Done

**Before your first business customer,** because their procurement will ask questions you need answers to.

**Before handling sensitive data** — health, financial, children's, employment.

**After a significant change,** particularly one involving authentication, payments or a new integration.

**When you inherit a product** you did not build.

**Annually thereafter,** which is a lighter exercise once the foundations are sound.

Not, ideally, after an incident — though that is when many founders first ask.

## What a Review Costs and What It Saves

For a small AI-built product, a focused review and remediation together generally sits inside LaunchStudio's fixed range of €800 to €7,500, depending on how many of the five areas need work. That is deliberately set against the alternative: a customer discovering the finding during their own assessment, or an incident requiring a notification you cannot substantiate.

The review is done by Manifera's engineers — eleven years of production and security work for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City — and the frontend you built in Lovable, Bolt or Cursor is never rebuilt. You receive the findings, the fixes, the verification, and the documentation. See what the [Launch Ready package](https://launchstudio.eu/en/#packages) covers, or [send us your prototype link](https://launchstudio.eu/en/#contact) and you will get an initial read within one business day.

## How to Prepare for One

A review costs less and finds more when the reviewer does not spend the first day orienting themselves. Four things prepared in advance make the difference.

**Access, arranged before the start.** Repository, hosting, database, storage and the relevant third-party accounts, with their own credentials rather than shared ones. Time spent waiting for access is time you are paying for.

**Two working test accounts,** in different organisations if your product has them, populated with realistic data. Reviewers need to behave like two different customers, and creating that state themselves takes an hour of your budget.

**A sentence about what matters most.** What data would hurt you most if exposed, which flows involve money, who your customers are. This lets a reviewer weight findings by your business rather than in the abstract.

**An honest list of what you already know is wrong.** Every founder has a mental list. Sharing it does not lose you credibility; it saves the reviewer from rediscovering it and lets them spend the time on what you cannot see.

Do not tidy the code first. A review of a cleaned-up version tells you about the cleaned-up version, and the point is to examine what your customers are actually using.

## What to Do With the Report Afterwards

The report has a second life beyond the fixes, and founders routinely file it and forget it.

**Keep the remediation record, not just the findings.** What was fixed, when, and what was accepted with a reason. That document answers a customer's question about your security posture far better than a clean report would, because it shows a process rather than a snapshot.

**Do not send the raw findings to customers.** A list of vulnerabilities, including ones you fixed, is not a reassuring document and in some cases is genuinely sensitive. Send a summary: a review was conducted, these areas were covered, findings were remediated, here is the date.

**Re-test after remediation.** A fix that was not verified by reproducing the original finding is a belief. The verification step is what turns the report into evidence.

**Put the next one in the calendar.** Annually, or after any significant change to authentication, payments or data handling. The second review is always cheaper than the first, because the foundations are already in place.

## Real example

### Fourteen Findings, Three That Mattered

Anne-Fleur Sluiter had Bewaarplan live for five months: a document-retention tool used by eleven small accountancy practices around Apeldoorn, holding client financial documents. A practice's own IT adviser asked for evidence of a security review before renewing.

The review took three days and produced fourteen findings. Three were serious: the storage bucket holding client documents was public with predictable file names, meaning any document was retrievable by anyone who guessed an address; a staff role field was writable by the account holder, so any user could grant themselves administrative access; and there was no logging of document access, so the question "who opened this client file" had no answer.

Six were moderate — no rate limiting, long-lived sessions surviving password changes, uploads unvalidated, no monitoring, backups never restored, dependency versions. Five were minor or did not apply, and the report said so.

Remediation took eight business days, in order of impact, with each fix verified by reproducing the original finding and confirming it failed. The report and the remediation record were handed over together.

**Result:** the practice renewed, and Anne-Fleur has since sent the same document to two prospective customers before being asked — which she says has shortened both conversations considerably.

> *"Fourteen findings sounds like a disaster. Three of them mattered, and the report told me which three, which is the entire reason it was worth paying for."*
> — **Anne-Fleur Sluiter, Founder, Bewaarplan (Apeldoorn)**

**Cost & Timeline:** €4,100 (review plus remediation of eleven findings, with verification and documentation) — completed in 11 business days.

## Frequently Asked Questions

### What is the difference between a security review and a penetration test?

A review examines the code and configuration with access to both, which finds design and access-control problems efficiently. A penetration test attacks the running system from outside without that access. For AI-built products the review usually finds more, sooner.

### Will an automated scanner find these problems?

Rarely the important ones. Scanners find known vulnerable dependencies and common misconfigurations. They cannot determine that one customer can read another's records, because that requires understanding what your data means.

### How many findings should I expect?

Typically eight to twenty for a first review of an AI-built product, across severities. The number matters less than the categories: access control and credential findings are the ones that block a launch.

### What should the report give me?

Findings ordered by business impact, reproducible evidence for each, concrete remediation specific to your stack, an honest severity assessment including what does not apply, and a statement of what was checked and found sound.

### When is the right time to have one?

Before your first business customer, before handling sensitive data, after significant changes to authentication or payments, and when you inherit a product you did not build — rather than after an incident, which is when most founders first ask.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the difference between a security review and a penetration test?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A review examines code and configuration with access to both, finding design and access-control problems efficiently; a penetration test attacks the running system from outside."
      }
    },
    {
      "@type": "Question",
      "name": "Will an automated scanner find these problems?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Rarely the important ones. Scanners find known vulnerable dependencies, not that one customer can read another's records, which requires understanding your data."
      }
    },
    {
      "@type": "Question",
      "name": "How many findings should I expect?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Typically eight to twenty for a first review, across severities. The categories matter more than the count."
      }
    },
    {
      "@type": "Question",
      "name": "What should the report give me?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Findings ordered by business impact, reproducible evidence, concrete stack-specific remediation, honest severity, and what was checked and found sound."
      }
    },
    {
      "@type": "Question",
      "name": "When is the right time to have one?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Before your first business customer, before handling sensitive data, after major changes, and when inheriting a product you did not build."
      }
    }
  ]
}
</script>
