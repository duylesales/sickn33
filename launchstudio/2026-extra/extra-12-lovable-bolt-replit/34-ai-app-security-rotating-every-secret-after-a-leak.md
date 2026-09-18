---
Title: "AI App Security: Rotating Every Secret After a Leak"
Keywords: ai app security, secret rotation, credential leak, key compromise, incident response, git history, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI App Security: Rotating Every Secret After a Leak

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI App Security: Rotating Every Secret After a Leak",
  "description": "A key has been exposed. What to rotate, in what order, why deleting the commit does nothing, and how to work out whether it was used — written for the founder discovering this on a Tuesday evening.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-20",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-app-security-rotating-every-secret-after-a-leak" }
}
</script>

You have found a key somewhere it should not be. In a public repository. In the JavaScript bundle your site serves. In a screenshot in a support thread. Pasted into a chat with a contractor who left in March.

The next hour matters, and the instinct — delete it, quickly, before anyone notices — is the wrong move. Removing a secret from where you found it does not make it stop working, and while you are tidying, the credential is still valid.

This article is the order of operations, written to be followed rather than admired.

## Rotate First, Tidy Afterwards

The only action that reduces risk is making the old value useless. Everything else is housekeeping.

So: go to the provider, generate a new credential, deploy it, and revoke the old one. In that order — generate and deploy before revoking, so your product does not go down while you work, unless the exposure is severe enough that downtime is preferable to continued access.

For most providers this takes minutes. Do it before investigating how it happened, before deciding whether anyone found it, and before removing the file.

## Deleting the Commit Does Nothing

If the secret was committed to a repository, removing it in a new commit removes it from the current state and from nothing else. The old commit still contains it, anyone who cloned the repository has it, and if the repository is public it may already be in automated scanning archives.

Rewriting history is possible and, for a repository with collaborators, disruptive — and it still does not help with copies that already exist. Treat the credential as compromised, permanently, and rotate. Cleaning history afterwards is reasonable hygiene, not remediation.

The same applies to a key that was in a JavaScript bundle: every visitor who loaded that page has a copy, and caches persist. Rotation is the only thing that helps.

## Rotate What Was Near It, Too

A leaked credential rarely travels alone. If a `.env` file reached a repository, everything in it is exposed, not only the value you noticed. If a contractor's machine or account is the concern, every credential they had access to is in scope.

Work from the container rather than from the single value. What file, what machine, what account, what channel — and then everything that was in it.

Order by consequence. Database credentials and anything granting administrative access first. Payment provider keys next. Email and messaging credentials after that, since a compromised sending identity damages your domain's reputation as well. Analytics and low-privilege service keys last.

## Then Find Out Whether It Was Used

Once the credential is dead, establish what happened. Most providers can tell you more than founders expect.

Look for: requests from addresses or regions you do not recognise, activity at times nobody was working, volumes that do not match your product's normal pattern, and administrative actions — created keys, changed settings, new users, exports.

For a database credential, look at what was read as well as changed. Bulk reads are the signature of data being taken, and they are easy to miss because nothing is different afterwards.

Write down what you find and when you looked, including a clear statement if you found nothing. That record is what you will need if you have to tell anyone, and reconstructing it later from memory is much weaker.

## Decide Whether You Must Notify

If personal data may have been accessed, you have obligations under the GDPR, and the clock is short: 72 hours from becoming aware, to the Autoriteit Persoonsgegevens, unless the breach is unlikely to result in a risk to the people concerned.

Two points founders get wrong. "Unlikely to result in a risk" is an assessment you must be able to justify, not a default. And notifying the affected individuals is a separate question, required when the risk to them is high.

Make the assessment deliberately and record the reasoning: what data was reachable, whether there is evidence of access, what the realistic consequence would be. Take advice if it is close. Under-reporting a genuine breach is a considerably worse position than a report that turns out to be precautionary.

## Close the Route

A credential leaks through a route, and if the route stays open the next one follows.

The routes, roughly by frequency in AI-built products: a secret given a public prefix so it was compiled into the browser bundle; an environment file committed because ignore rules did not cover it; a key pasted into a chat, a ticket or a screenshot; a shared account with a password several people know; and a contractor's access never removed.

Each has a specific fix, and now — while the incident is fresh and the motivation exists — is the only time it will actually get done. Build-time scanning that fails the build on a detected secret, ignore rules verified, a password manager with per-person access rather than shared logins, and an offboarding checklist.

## Reduce What a Single Leak Costs

Two structural changes make the next incident smaller.

Use narrow credentials. One key per integration, scoped to what that integration needs, so a leak affects one thing. A single administrative key used everywhere means every leak is total.

And know where each credential is used. A simple list — this key, this provider, used by these parts of the product, last rotated on this date — turns rotation from an investigation into a task. Most founders discover during an incident that they do not know which key is used where, and that discovery is what makes a Tuesday evening long.

## Rotating Without an Outage

The reason secrets go years without being rotated is that rotation feels dangerous: change the value and something stops working, usually the thing you were not thinking about.

Three patterns remove the fear, and adopting them in calm conditions is what makes an emergency rotation a twenty-minute job.

**Two valid values during a transition.** Where the provider allows multiple active keys — most do — create the new one, deploy it, confirm traffic is using it, then delete the old. Nothing is ever without a working credential.

**Verification that accepts either.** For things you verify rather than send, such as webhook signatures, accept both the current and previous secret for a few days. The switch at the provider then becomes a non-event.

**Configuration, not code.** A credential referenced from environment configuration is rotated by changing a value and restarting. One hard-coded in source requires a commit, a review and a deployment, which is why nobody does it at nine on a Sunday evening.

Then rotate on a schedule rather than only on incidents — annually is reasonable for most products, and more often for anything with broad access. The value of the schedule is not that it prevents a leak; it is that the procedure is familiar, tested and undramatic on the day you need it in a hurry.

One caution worth stating: rotate one credential at a time, and confirm the product still works before moving to the next. A rotation of nine secrets in a single change produces an outage whose cause could be any of them, which is a worse evening than the one you were already having.

## Setting This Up

For a product that has just had an exposure, or that wants to be ready: the affected credential rotated and revoked with the replacement deployed first, everything in the same container rotated in order of consequence, provider logs reviewed for use with findings written down, a documented breach assessment against the 72-hour obligation, the route closed with build-time secret scanning and verified ignore rules, shared accounts replaced with per-person access, an offboarding checklist, credentials narrowed to one per integration with minimum scope, and an inventory recording where each is used and when it was last rotated.

LaunchStudio does this both as an incident response and as preparation, and under the managed arrangement at €49 per month the scanning and the inventory are maintained rather than remembered. The engineers are Manifera's — eleven years, 120+ engineers, clients including Vodafone, TNO and CFLW.

[Tell us what you found and where](https://launchstudio.eu/en/#contact). The first hour is the one that matters.

## Real example

### A Repository Made Public by Accident

Suzanne Grotenhuis built Inspectierapport in Lovable: inspection reporting for building surveyors and installation inspectors, 39 firms producing around 2,000 reports a month.

She made her repository public to share a code sample with a prospective contractor, intending to revert it. She did, four days later. An environment file had been committed eleven months earlier, before ignore rules were in place, and it contained the Supabase service role key, the email provider credentials, an API key for a mapping service billed by usage, and the signing secret for her payment webhooks.

Within a day of the repository going public, automated scanners had found it. She learned this from the mapping provider, who suspended her account for anomalous usage — 140,000 requests in eleven hours from addresses she did not recognise.

Same evening, then two business days: the mapping key rotated first since abuse was in progress; the Supabase service role key rotated and deployed next, as the credential with unrestricted database access; email credentials and the webhook signing secret rotated after that, with the webhook handler temporarily accepting both old and new to avoid dropping deliveries; every credential in the file treated as compromised regardless of whether it appeared used; database access logs reviewed with Supabase support, showing no queries from unrecognised sources in the exposure window; email provider logs reviewed, showing no sends; a breach assessment documented concluding that personal data in the database had been reachable but showed no evidence of access, with the reasoning recorded and legal advice taken, resulting in a precautionary report to the Autoriteit Persoonsgegevens; build-time secret scanning added; ignore rules corrected and history rewritten as hygiene; shared logins replaced with per-person access in a password manager; and a credential inventory created listing nine secrets, their scope, where each is used and when it was last rotated.

**Result:** the mapping provider waived €2,840 of usage after reviewing the timeline. No evidence of database or email access was found. Suzanne's assessment was that the service role key being in that file for eleven months was the real incident, and that the four public days were simply when it was noticed.

> *"I rotated the mapping key first because that was the one costing me money. It took me an hour to realise the file also had the key that can read every inspection report in the product."*
> — **Suzanne Grotenhuis, Founder, Inspectierapport (Amersfoort)**

**Cost & Timeline:** €3,100 (emergency rotation of nine credentials in order of consequence, dual-secret webhook transition, provider log review, breach assessment and regulatory report, secret scanning, history and ignore remediation, access management, credential inventory) — completed in 2 business days after same-evening triage.

## Frequently Asked Questions

### What is the first thing to do when a key leaks?

Rotate it. Generate the replacement, deploy it, revoke the old value. Investigation and cleanup come afterwards; while you tidy, the old credential still works.

### Does deleting the commit fix a leaked secret?

No. The old commit retains it, clones already exist, and public repositories are scanned automatically within minutes. Rotation is the only remediation; cleaning history is hygiene.

### What else should I rotate besides the key I found?

Everything in the same container — the whole environment file, every credential the compromised account or machine could reach — ordered by consequence, starting with database and administrative access.

### Do I have to report it?

If personal data may have been accessed, you have 72 hours to notify the Autoriteit Persoonsgegevens unless you can justify that a risk is unlikely. Document the assessment either way and take advice when it is close.

### How do I make the next leak cheaper?

Narrow credentials — one per integration with minimum scope — and an inventory recording where each is used and when it was rotated, so rotation is a task rather than an investigation.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the first step when a credential leaks?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Rotate it — generate the replacement, deploy it, revoke the old one. Investigation and cleanup come after, since the old value works until revoked."
      }
    },
    {
      "@type": "Question",
      "name": "Does removing the commit fix a leaked secret?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Old commits retain it, clones exist, and public repositories are scanned within minutes. Only rotation remediates."
      }
    },
    {
      "@type": "Question",
      "name": "What else should be rotated besides the exposed key?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Everything in the same file, machine or account, ordered by consequence — database and administrative credentials first."
      }
    },
    {
      "@type": "Question",
      "name": "Must a credential leak be reported to the regulator?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "If personal data may have been accessed, within 72 hours unless you can justify that risk is unlikely. Document the assessment either way."
      }
    },
    {
      "@type": "Question",
      "name": "How do I limit the damage of a future leak?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "One narrowly scoped credential per integration, plus an inventory of where each is used and when it was last rotated."
      }
    }
  ]
}
</script>
