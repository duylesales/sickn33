---
Title: "AI-Generated Code Audit: What a Vibe Code Audit Covers"
Keywords: ai-generated code audit, vibe code audit, ai code security audit, audit lovable app, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# AI-Generated Code Audit: What a Vibe Code Audit Covers

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-Generated Code Audit: What a Vibe Code Audit Covers",
  "description": "An AI-generated code audit examines apps built with Lovable, Bolt, Cursor, v0 or Replit for security, data protection and operational risks. This page explains the audit scope, deliverables, pricing and when an audit is worth commissioning.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-14",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-generated-code-audit-what-a-vibe-code-audit-covers" }
}
</script>

Forty-five percent. That is the share of AI-generated code containing security vulnerabilities, according to the research LaunchStudio cites on its homepage. If your product was built with Lovable, Bolt, Cursor, v0 or Replit, the odds are that something in it needs attention. An AI-generated code audit tells you what, how serious it is and what to do first, before a customer, an investor or an attacker finds it for you.

This page describes what a vibe code audit from LaunchStudio covers and what you receive at the end.

## Myth: "My App Works, So It Is Probably Fine"

Working and safe are different properties. AI tools optimise for the first: they generate code that does what you asked. They are much weaker at the second, which is about what the app does when someone asks for something you did not intend. A logged-in user changing an ID in a request. A webhook sent twice. A form field containing a script. None of these show up when you click through your own app.

## Myth: "An Automated Scanner Is the Same as an Audit"

Scanners are useful and we use them. They catch outdated dependencies, some injection patterns and secrets committed to git. They cannot tell you that your invoices table is readable by every logged-in user because a Row Level Security policy says `true`, or that your admin route checks a flag the user can set themselves. Those are logic problems, and they are the most common serious findings in AI-built apps.

## Myth: "An Audit Means a Rewrite"

Almost never. Most findings are fixed with targeted changes: a policy rewritten, a key moved, a check added on the server. The audit's purpose is to make the remaining work small and specific.

## What the Vibe Code Audit Covers

| Domain | Questions we answer |
| --- | --- |
| Access control | Can any user read or change data that belongs to someone else? Are admin functions protected on the server? |
| Authentication | Are sessions, tokens, password resets and email confirmation handled safely? |
| Secrets | Are any keys exposed in the browser, the repository history or logs? |
| Database | Are Row Level Security policies complete and correct? Are constraints and indexes in place? |
| Input and output | Is user input validated server-side? Can it reach queries, HTML or file paths unsafely? |
| Payments | Are webhooks verified and idempotent? Can a client manipulate prices or plan levels? |
| Third parties | Which services receive personal data, and where are they located? |
| Data protection | Is personal data minimised, retained deliberately and deletable on request? |
| Operations | Are there backups with tested restores, monitoring, alerting and a safe deploy path? |

For apps serving EU customers, the data protection part maps findings to practical GDPR obligations such as processor agreements and data location.

## What You Receive

1. **Executive summary.** One page, in plain language, suitable for a co-founder, investor or customer.
2. **Findings register.** Every issue with severity, location, a reproduction description and recommended fix.
3. **Fix plan.** Findings grouped into "before launch", "within 30 days" and "when convenient", with effort estimates.
4. **Walkthrough call.** 45 minutes to go through the critical and high findings.
5. **Optional re-test.** After fixes, we verify each critical and high item and issue an updated summary.

## Pricing and Timeline

| Scope | Price | Timeline |
| --- | --- | --- |
| Single app, standard Supabase or Firebase backend | €1,200-€2,500 | 5-7 business days |
| SaaS with payments, roles and integrations | €2,500-€4,500 | 7-10 business days |
| Audit plus fixes of critical and high findings | €3,500-€7,500 | 2-3 weeks |

Prices are fixed after a 15-minute call. An NDA is available before we read any code.

## Who Performs the Audit

LaunchStudio is backed by Manifera, trusted by Vodafone, TNO and CFLW. Manifera's founder Herre Roelevink co-founded CyberDevOps, now CFLW Cyber Strategies, which developed a Dark Web Monitor together with TNO, and that security lineage shapes how audits are run. Engineers work from Manifera's development centre in Ho Chi Minh City, coordinated with the Amsterdam office at Herengracht 420 for Dutch and European clients. More on the team is available on [Manifera's about page](https://www.manifera.com/about-us/).

Our checks draw on established references such as the [OWASP Top 10](https://owasp.org/www-project-top-ten/), adapted to the patterns AI tools actually produce.

## When to Commission an Audit

- Before your first paying customers
- Before an investor's technical due diligence
- When an enterprise customer sends a security questionnaire
- After a freelancer or AI tool made large changes you did not review
- After any incident, however small

If you want to do a first pass yourself, our companion article with a [25-point vibe code audit checklist](https://launchstudio.eu/en/blog/vibe-code-audit-checklist-25-checks-before-launch) covers what a founder can check without reading code.

## Real example

### An AI-Native Founder in Action: The HR Onboarding Tool That Passed a Demo and Failed an Audit

Pieter-Jan Claes, an HR consultant in Ghent, built Startdag with Lovable and later refined it in Cursor: an onboarding platform where small companies send new hires contracts, policies and first-week schedules, and track what each person has signed. Two Flemish companies used it, and a Dutch staffing agency with 300 placements a year wanted to roll it out.

The agency required an independent security review. LaunchStudio's audit found eleven issues. Three were critical: signed contracts were stored in a public storage bucket with predictable file names, the Row Level Security policy on the documents table allowed any authenticated user to list all companies' documents, and an admin endpoint trusted an `is_admin` value sent from the browser. Several medium findings concerned missing retention rules for personal data and an email provider located outside the EU without a documented transfer basis.

Pieter-Jan chose the audit-plus-fixes option. Engineers moved documents to a private bucket with signed, expiring URLs, rewrote the RLS policies around company membership, moved admin checks to the server, added retention rules that delete candidate documents after a configurable period, and documented processors and data locations for the agency's privacy officer.

**Result:** The re-test showed all critical and high findings resolved. The staffing agency signed a two-year contract, and Startdag's audit summary became a standard attachment in Pieter-Jan's sales conversations.

> *"Without the audit I would have sold contracts with a public link to every signed document. The scary part is that nothing looked wrong."*
> - **Pieter-Jan Claes, Founder, Startdag (Ghent)**

**Cost & Timeline:** €5,400 (audit, fixes of critical and high findings, re-test and summary) - completed in 14 business days.

## Frequently Asked Questions

### What is a vibe code audit?

A vibe code audit is a security and quality review of an app built mostly through AI tools and prompts. It focuses on the risks those tools typically introduce: incomplete access control, exposed keys, unverified webhooks and missing data protection measures, rather than code style.

### How is an AI-generated code audit different from a penetration test?

A penetration test attacks a running system from the outside. An audit reads the code and configuration from the inside. For AI-built apps, an audit usually finds more for less money, because most serious issues are visible in policies and server logic. Larger companies sometimes require both.

### Can I show the audit report to customers or investors?

Yes. The executive summary is written to be shared. Many founders attach it to security questionnaires or due diligence data rooms. The full findings register is usually kept internal until fixes are complete.

### Why does a cybersecurity heritage matter for auditing AI code?

AI tools make the same categories of mistakes repeatedly, and those categories match how attackers work: guessing IDs, replaying requests, reading public storage. A team shaped by cybersecurity work, as Manifera is through Herre Roelevink's CFLW background, looks there first.

### Does a code audit help with GDPR compliance in the Netherlands?

It helps with the technical side. The audit identifies where personal data is stored, who can access it, which processors receive it and whether it can be deleted. That is the input your privacy statement, processing register and processor agreements need, and it is what the Autoriteit Persoonsgegevens would expect you to know.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is a vibe code audit?",
      "acceptedAnswer": { "@type": "Answer", "text": "A security and quality review of an app built mostly with AI tools and prompts, focused on typical risks such as incomplete access control, exposed keys, unverified webhooks and missing data protection." }
    },
    {
      "@type": "Question",
      "name": "How is an AI-generated code audit different from a penetration test?",
      "acceptedAnswer": { "@type": "Answer", "text": "A penetration test attacks a running system from outside; an audit reads code and configuration from inside. For AI-built apps an audit usually finds more for less, since most issues sit in policies and server logic." }
    },
    {
      "@type": "Question",
      "name": "Can I show the audit report to customers or investors?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. The executive summary is written to be shared with customers and investors. The full findings register usually stays internal until fixes are complete." }
    },
    {
      "@type": "Question",
      "name": "Why does a cybersecurity heritage matter for auditing AI code?",
      "acceptedAnswer": { "@type": "Answer", "text": "AI tools repeat mistakes that match attacker behaviour, such as guessable IDs and public storage. A team shaped by cybersecurity work, like Manifera through Herre Roelevink's CFLW background, checks those first." }
    },
    {
      "@type": "Question",
      "name": "Does a code audit help with GDPR compliance in the Netherlands?",
      "acceptedAnswer": { "@type": "Answer", "text": "It covers the technical side: where personal data lives, who can access it, which processors receive it and whether it can be deleted, which is what privacy documents and the Autoriteit Persoonsgegevens expect." }
    }
  ]
}
</script>
