---
Title: "Data Breach Notification: 72 Hours and What You Need Ready"
Keywords: data breach notification, 72 hours, Autoriteit Persoonsgegevens, incident response, breach register, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Scale-Up
---

# Data Breach Notification: 72 Hours and What You Need Ready

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Data Breach Notification: 72 Hours and What You Need Ready",
  "description": "The clock starts when you become aware, not when you understand. What counts as a breach, who notifies whom, what to prepare before it happens, and how to make the assessment defensible.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-12",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/data-breach-notification-72-hours-and-what-you-need-ready" }
}
</script>

Seventy-two hours sounds generous until you are inside it. The clock starts when you become aware that a breach has occurred — not when you understand what happened, not when you have finished fixing it, and not on Monday if it was Saturday.

Within that window you must decide whether to notify the Autoriteit Persoonsgegevens, prepare the notification if so, and separately assess whether to tell the affected individuals. All while the technical problem is still in front of you.

Almost everything that makes this survivable is prepared beforehand. This article is the preparation.

## More Than a Hack

A personal data breach is any security incident leading to accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data.

That covers considerably more than an attacker.

A misconfigured storage bucket exposing documents. An email with customer data sent to the wrong recipient. A bulk email revealing every address in the To field. A laptop lost with a database export on it. A deletion that destroyed records with no backup. A bug showing one customer another customer's data. A contractor retaining access after leaving.

Several of these look like mistakes rather than incidents, and founders talk themselves out of recognising them. The definition does not require malice or sophistication.

## Who Notifies Whom

If you are a processor — which you are for data your customers put into your product — you do not notify the regulator. You notify your customer, the controller, without undue delay, and they decide about the regulator and the individuals.

Your processing agreements will specify a window for that notification, often 24 or 48 hours. Check what you signed, because it is probably tighter than the regulator's 72.

For your own data — your users' accounts, your billing records — you are the controller and the obligation to notify is yours.

A single incident is frequently both, which is why the contact list needs to exist in advance rather than being assembled while you are trying to think.

## The Assessment That Decides

Notification to the regulator is required unless the breach is unlikely to result in a risk to the rights and freedoms of the people concerned. That is a judgement, and it must be made deliberately and recorded.

The factors that matter: what data was involved and how sensitive it is; how many people; whether they can be identified; whether the data was encrypted or otherwise unintelligible to whoever obtained it; whether there is evidence of actual access as opposed to theoretical exposure; and what realistic harm could follow.

Notifying the individuals is a separate and higher threshold — required when the risk to them is high. The practical difference: an exposure of email addresses may warrant a regulator notification and not an individual one, while an exposure of health information or credentials almost certainly warrants both.

When it is close, notify. A precautionary report is a considerably better position than a decision not to report that is later examined.

## What to Prepare Now

Six things, none of which takes long, and all of which are impossible to assemble under pressure.

**A contact list.** Who at each customer receives a breach notification, the regulator's reporting route, your lawyer, your insurer, and any provider you would need to reach urgently.

**A notification template** for customers, with the fields the regulator's form requires: what happened, when, what data, how many people, what you have done, what you are doing, and who to contact.

**Your data inventory.** The register described elsewhere in this series is what lets you answer "what data was involved" in minutes rather than days.

**Logging that can answer what was accessed.** Without it, every assessment defaults to assuming the worst, because you cannot demonstrate otherwise.

**A breach register.** You must record every breach including those you decide not to report, with the reasoning. This is checked.

**A decision about who decides.** For a solo founder that is you; for a team, name the person, because the worst version of this is three people waiting for each other.

## During the Window

An order of operations that works.

Contain first — stop the exposure, revoke the credential, take the feature offline. Then preserve evidence, particularly logs, before anything rotates them away.

Establish the facts you can: what, when, how many, whether there is evidence of access. Write them down as you go with timestamps, because the notification requires a chronology and reconstructing one afterwards is unreliable.

Notify your affected customers within your contractual window, even if your understanding is incomplete. A notification saying what you know and what you are still establishing is expected; silence is not.

Then make the regulatory assessment, notify if required — and an incomplete notification within 72 hours followed by an update is acceptable, whereas a late complete one is not.

Afterwards, write the review: what happened, why, what changed as a result. That document is what a customer's follow-up questions are answered from.

## Encryption Changes the Assessment

One technical measure has a direct effect on whether notification is required, and it is worth understanding precisely because founders overstate it.

If the data was rendered unintelligible to whoever obtained it — properly encrypted, with the key not also compromised — the risk to individuals may be low enough that notifying them is not required. The regulator notification threshold is separate and lower.

The qualification matters. A stolen laptop with an encrypted disk and a strong passphrase is a different situation from a database export sitting in an encrypted bucket that the compromised credential could also decrypt. Encryption at rest protects against physical theft of storage; it protects against nothing when the attacker is using your application's own access.

So the honest question is not "was it encrypted" but "could the person who obtained it read it". For most application-level breaches — a leaked key, an authorisation bug, an email to the wrong person — the answer is yes, and encryption is irrelevant to the assessment.

Where it genuinely helps is the category of incident involving lost devices and lost media, and in reducing what a partial compromise yields. Both are worth having. Neither is a reason to skip an assessment, and describing an incident as low risk on the basis of encryption that did not apply to it is the sort of reasoning that does not survive examination.

## Telling People Well

If individuals must be informed, how you do it affects the outcome more than the fact of doing it.

The regulation asks for the nature of the breach, a contact point, the likely consequences, and the measures taken or proposed. In plain language, not legal phrasing.

What works in practice: say what happened in the first sentence, without preamble. Say specifically what data about them was involved — people's first question is always what did they get about me, and a generic description leaves them assuming the worst. Say what you have done and by when. Say what they should do, if anything, and be concrete: change a password, watch for a particular kind of message, contact you with a reference. Give a real contact route that a person answers.

What fails: an apology that occupies three paragraphs before the facts, passive constructions that avoid naming who was responsible, minimising language that invites the reader to disagree, and a no-reply address.

For a business product the message usually goes from your customer to their people rather than from you, which means your job is to give them a draft they can adapt along with the facts to fill it. Doing that unprompted, within hours, is what turns an incident into a demonstration of competence — which is a strange thing to say about a breach, and is repeatedly what the founders who handled one well report afterwards.

## Setting This Up

For an existing product this is typically one day: a contact list covering customers, the regulator, legal and insurance; notification templates matching the required fields; a data inventory sufficient to answer what was involved; logging and retention adequate to establish what was accessed; a breach register including unreported incidents with reasoning; a documented decision process naming who decides; the contractual notification windows from every signed agreement tabulated; and a short written procedure covering contain, preserve, establish, notify, assess, review.

LaunchStudio prepares this as part of production readiness and is on the contact list for customers under the managed arrangement at €49 per month. The engineers are Manifera's — eleven years, clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City.

[Ask us what your first hour would look like](https://launchstudio.eu/en/#contact). Most founders have never thought it through.

## Real example

### A Saturday Morning Email

Bart-Jan Roozen built Hulpvraag in Lovable: intake and referral administration for municipal social support teams, used by 11 municipalities handling around 9,000 cases a year.

On a Saturday morning a case worker emailed to say she had received a weekly summary containing another municipality's cases. A change deployed on Friday had introduced a fault in the recipient filtering of a scheduled job, and the summary had gone to all 140 users across all 11 municipalities. It contained names, addresses and brief descriptions of social support needs — sensitive information about identifiable people in vulnerable circumstances.

He became aware at 09:40 on Saturday. His 72 hours ended on Tuesday morning, and his processing agreements required customer notification within 24 hours.

What followed, in order: the scheduled job disabled by 09:55 and logs preserved before rotation; by 11:30, the facts established from send logs — 140 recipients, 11 municipalities, 612 cases described, all recipients being authorised professionals under professional confidentiality obligations, with no evidence of onward distribution; all 11 municipal contacts notified by 13:00 with what was known and what was still being established, within the contractual window; a recall request and an instruction to delete sent to all 140 recipients with confirmation requested, of which 128 confirmed by Monday; legal advice taken Saturday afternoon; the assessment concluding that although recipients were professionals bound by confidentiality, the data was special category and identifiable, so the risk was not unlikely; the regulator notified on Sunday afternoon, well inside the window, with an update submitted on Wednesday; each municipality supported in their own assessment of whether to inform affected residents, which three did; the bug fixed and a test added covering per-recipient filtering; and a review document produced on Tuesday.

**Result:** the regulator accepted the notification and the remediation without further action. All 11 municipalities remained customers, and two said afterwards that the speed and completeness of the Saturday notification was why. Bart-Jan's view is that the preparation done four months earlier — contact list, templates, logging — is the only reason the first four hours were productive.

> *"I found out at twenty to ten on a Saturday. Without the contact list and the template I would have spent the first three hours working out who to tell and what to say, and those were the three hours that mattered."*
> — **Bart-Jan Roozen, Founder, Hulpvraag (Zwolle)**

**Cost & Timeline:** €3,400 (incident response including containment, evidence preservation, fact establishment, customer and regulator notification, recall coordination, legal input, bug fix with regression test, review documentation) — completed in 4 business days following same-day response.

## Frequently Asked Questions

### When does the 72 hours start?

When you become aware that a breach has occurred — not when you understand it or have fixed it. Weekends included.

### Is an email sent to the wrong person a breach?

Yes, if it contained personal data. So is a misconfigured bucket, a lost laptop with an export, a bug showing one customer another's data, and a deletion with no backup.

### Do I notify the regulator or my customer?

As a processor, your customer, within the window your processing agreement specifies — frequently 24 or 48 hours. They decide about the regulator. For your own users' data you are the controller and notify directly.

### What if I do not have all the facts within 72 hours?

Submit an incomplete notification within the window and update it. A partial timely report is acceptable; a complete late one is not.

### Do I have to record breaches I decide not to report?

Yes. Every breach goes in a register with the reasoning for not reporting. That register is checked, and an absent one is itself a finding.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "When does the 72-hour breach clock start?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "When you become aware a breach occurred — not when you understand or fix it, and weekends count."
      }
    },
    {
      "@type": "Question",
      "name": "Is an email to the wrong recipient a data breach?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes if it contained personal data, as are misconfigured buckets, lost devices with exports, and bugs exposing one customer's data to another."
      }
    },
    {
      "@type": "Question",
      "name": "As a processor, who do I notify?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Your customer, within the window your processing agreement sets — often 24 or 48 hours. They decide about the regulator and individuals."
      }
    },
    {
      "@type": "Question",
      "name": "What if the facts are incomplete within 72 hours?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Notify within the window with what you know and update afterwards. A partial timely report is acceptable; a late complete one is not."
      }
    },
    {
      "@type": "Question",
      "name": "Must unreported breaches be recorded?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — every breach goes in a register with the reasoning for not reporting, and the register itself is checked."
      }
    }
  ]
}
</script>
