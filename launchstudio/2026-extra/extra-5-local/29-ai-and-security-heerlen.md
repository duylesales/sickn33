---
Title: "AI and Security in Heerlen: The Conversation Founders Have Too Late"
Keywords: ai and security, ai app security risks, ai generated code security, Heerlen
Buyer Stage: Awareness
Target Persona: Non-Technical Founder
---

# AI and Security in Heerlen: The Conversation Founders Have Too Late

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI and Security in Heerlen: The Conversation Founders Have Too Late",
  "description": "Founders in Heerlen tend to raise AI and security questions after launch, not before. Here's why that timing costs more than it needs to.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-23",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/29-ai-and-security-heerlen" }
}
</script>

When does a founder actually start thinking about AI and security? Almost never before launch, and almost always right after something goes wrong. That's not a criticism — it's a pattern nearly universal among first-time founders using AI tools, and it's worth naming directly because Heerlen, a city that has spent three decades reinventing itself from a mining economy into a service and administrative hub, understands better than most what it costs to fix a foundation after the fact rather than before. The old Oranje-Nassau mine sites that once anchored the local economy didn't collapse because nobody knew mining was risky — they closed because the industry the region had built everything around changed faster than the underlying structure could adapt. Software security has a smaller-scale version of the same lesson: the risk was always there, it just wasn't the thing anyone was actively managing until it forced the issue.

## Why the AI and Security Conversation Gets Delayed

The delay isn't laziness. It's that AI and security don't feel connected while you're building. Lovable, Bolt, Cursor, and v0 all produce apps that look and behave securely — login screens that work, forms that validate, data that saves and loads correctly. Security failures are, almost by definition, invisible in normal operation. A missing rate limit doesn't show up until someone hammers your login endpoint. An exposed API key doesn't show up until someone opens dev tools and looks. The absence of a problem feels identical to the absence of a vulnerability, right up until it doesn't — and a founder testing their own app, using their own account, in the way they always use it, will simply never trigger the condition that exposes the gap.

Heerlen's economy today leans heavily on administrative and financial services — APG, one of the Netherlands' largest pension administrators, is headquartered here in the city center, and the broader Limburg region's service sector has grown up around exactly this kind of white-collar, data-handling work. Founders building tools in or adjacent to this ecosystem are often building something that touches financial or personal data from day one, which raises the cost of a delayed security conversation considerably compared to, say, a purely internal scheduling tool.

## What "Too Late" Actually Looks Like

In practice, "too late" isn't usually a headline-grabbing breach. It's smaller and more common than that: a prospective enterprise customer's security questionnaire that your AI-built app can't pass, an investor's technical due diligence that flags basic gaps, or — most often — a curious user who stumbles onto data they shouldn't see and reports it, as happened to more than one founder in our own case files. It rarely announces itself as a crisis. It shows up as an awkward pause in an otherwise good sales call, or a one-line Slack message from a beta user that starts with "hey, weird question, but..." Each of these is recoverable, but each is more expensive to fix reactively, under time pressure and reputational risk, than it would have been to address as a planned step before launch.

LaunchStudio was built around this exact timing problem. Backed by Manifera — trusted by Vodafone, TNO, and CFLW Cyber Strategies for security-focused engineering work, with a development hub in Ho Chi Minh City handling much of this review capacity — the company treats security as a scheduled step in getting an AI prototype to production, not an emergency response after the fact. That's a deliberate design choice: security review priced and timed like any other predictable part of shipping, rather than an unplanned cost that only appears after something breaks.

## Starting the Conversation Earlier Than You Think You Need To

The founders who come out ahead aren't the ones who avoid AI tools out of security caution — they're the ones who schedule a security pass as a normal step, the same way you'd schedule a design review, rather than waiting for a reason to need one. If you're building something in Heerlen or anywhere in Limburg that will eventually touch real user data or payments, [talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#process) before your launch date, not after your first incident. Manifera's broader security-adjacent engineering work is visible in its [custom software development services](https://www.manifera.com/services/custom-software-development/).

## The Questions to Ask, Even If You Can't Read the Answer Yourself

You don't need to be able to read code to have a productive security conversation about your own product — you just need to ask questions specific enough that a vague answer becomes obvious. A non-technical founder who asks "is it secure?" will usually get reassured. A founder who asks one of the questions below will get either a confident, specific answer or a hesitation worth paying attention to.

**Five questions that work regardless of your technical background**

- **"If I log in as myself and change the ID in the URL to a number that isn't mine, what happens?"** This is the exact question that exposed the gap in PensioPortal below. A confident answer explains the specific check that prevents it. A vague answer, or "it shouldn't happen," is worth pushing on further.
- **"Where do failed login attempts get slowed down or blocked?"** If nobody can point to a specific mechanism, your login page likely has no protection against someone automatically guessing thousands of passwords.
- **"If something goes wrong at 2am, how do we find out — from a monitoring tool, or from a customer email?"** This tells you whether anyone would actually notice a problem before it reaches a user.
- **"Who besides me can see the raw database, and would I know if they looked at something they shouldn't?"** This surfaces whether any audit logging exists at all.
- **"What's the plan if a customer reports a security problem tomorrow?"** A team with no answer to this has not yet thought about security as an ongoing responsibility, only as a one-time checkbox.

None of these questions require you to evaluate the technical answer yourself — they require you to notice whether the answer is specific or evasive, and to treat evasiveness as useful information rather than something to politely let slide. A confident, specific answer to all five is a genuinely good sign. A pattern of "we haven't gotten to that yet" across two or more of them is the moment to schedule the review, not the moment to assume it'll probably be fine, since that assumption is exactly what let Mark Souren's authorization gap sit unnoticed for as long as it did.

## Real example

### An AI-Native Founder in Action: Mark Souren's PensioPortal

Mark Souren, based in Heerlen and with a background adjacent to the region's pension administration sector, built PensioPortal — a tool helping small employers consolidate and explain employee pension contribution statements — using Lovable over about two and a half weeks. The product's entire value proposition depended on handling sensitive financial data accurately and safely, which made it exactly the kind of project where the AI-and-security conversation should have happened before day one.

It didn't, and it surfaced during a pilot with a mid-sized Limburg employer: an HR staff member testing the tool discovered that changing a numeric ID in the browser address bar pulled up a different employee's full pension contribution history, name, and salary band. Lovable had built functional, good-looking pages for viewing individual pension records, but no server-side check confirmed the logged-in user actually had permission to view the record being requested.

LaunchStudio's engineers implemented proper server-side authorization checks on every record-level endpoint, added structured audit logging so any future access attempt would be traceable, and ran a broader review confirming no other endpoints shared the same flaw.

**Result:** PensioPortal relaunched with verified access controls and has since passed two employer security reviews without a follow-up question.

> *"I genuinely didn't know 'security' was a separate task from 'building the app.' I thought Lovable handled that. Now I know exactly what it doesn't."*
> — **Mark Souren, Founder, PensioPortal (Heerlen)**

**Cost & Timeline:** €1,250 (authorization fix, audit logging, endpoint review) — completed in 5 business days.

---

## Frequently Asked Questions

### Why do founders usually only think about AI and security after something goes wrong?
Security failures are invisible during normal use — an AI-built app can look and function correctly while still having gaps like missing authorization checks, which only surface when someone specifically looks for them or stumbles onto them.

### Is Heerlen's data-handling sector unusually exposed to this risk?
Heerlen's concentration of pension and financial administration services, including APG's headquarters, means many local founders build products touching sensitive financial data early, raising the stakes of a delayed security review.

### What does a proactive security review with LaunchStudio actually involve?
It typically means auditing authentication, authorization, data access rules, and secrets handling against your specific AI-built stack before launch, rather than after an incident.

### Who is behind LaunchStudio's security-focused engineering approach?
LaunchStudio is led by Herre Roelevink, CEO of LaunchStudio and Managing Director of Manifera, whose background includes cybersecurity work and a collaboration with TNO on Dark Web Monitor.

### Does LaunchStudio only work with financial or pension-related products?
No, this article uses Heerlen's pension-administration sector as a relevant local example, but LaunchStudio reviews AI-built apps handling any kind of sensitive user data.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Why do founders usually only think about AI and security after something goes wrong?", "acceptedAnswer": { "@type": "Answer", "text": "Security failures are invisible during normal use, so an AI-built app can look and function correctly while still having gaps like missing authorization checks." } },
    { "@type": "Question", "name": "Is Heerlen's data-handling sector unusually exposed to this risk?", "acceptedAnswer": { "@type": "Answer", "text": "Heerlen's concentration of pension and financial administration services, including APG's headquarters, means many local founders build products touching sensitive financial data early." } },
    { "@type": "Question", "name": "What does a proactive security review with LaunchStudio actually involve?", "acceptedAnswer": { "@type": "Answer", "text": "It typically means auditing authentication, authorization, data access rules, and secrets handling against your specific AI-built stack before launch." } },
    { "@type": "Question", "name": "Who is behind LaunchStudio's security-focused engineering approach?", "acceptedAnswer": { "@type": "Answer", "text": "LaunchStudio is led by Herre Roelevink, CEO of LaunchStudio and Managing Director of Manifera, with a background in cybersecurity and a collaboration with TNO." } },
    { "@type": "Question", "name": "Does LaunchStudio only work with financial or pension-related products?", "acceptedAnswer": { "@type": "Answer", "text": "No, LaunchStudio reviews AI-built apps handling any kind of sensitive user data, not only financial or pension-related products." } }
  ]
}
</script>
