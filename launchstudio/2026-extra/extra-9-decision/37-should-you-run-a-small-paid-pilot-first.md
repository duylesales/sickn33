---
Title: "Should You Run a Small Paid Pilot Before the Full Engagement?"
Keywords: paid pilot project, trial project with a dev partner, white-label development partner, vetting a subcontractor, agency production partner, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Agency / Freelancer (White-Label Partner)
---

# Should You Run a Small Paid Pilot Before the Full Engagement?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Should You Run a Small Paid Pilot Before the Full Engagement?",
  "description": "A paid pilot is the most reliable way for an agency to test a white-label engineering partner, but only if it is designed to reveal behaviour rather than skill. How to size one, what to measure, what it costs, and when to skip it entirely.",
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
  "datePublished": "2027-01-20",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/should-you-run-a-small-paid-pilot-first"
  }
}
</script>

Your client has a Lovable app, a launch date, and no idea that the interface they love is sitting on a backend with no server-side permissions. You've found a production partner who says they do exactly this. Their references check out. Do you hand them the whole €9,000 build, or do you buy €700 of work first and watch what happens?

Most agencies default to the full engagement, because pilots feel like an admission of doubt and because splitting a project adds coordination overhead you're not being paid for. That default is wrong more often than it's right — but only if you understand what a pilot is actually for. It is not a skills test. Skill is what references and code reviews establish. A pilot tests something references cannot: how a partner behaves inside *your* process, under *your* deadline, with *your* client's name on the invoice.

## What You're Actually Buying With a Pilot

Three things, none of which appear in a proposal:

**Response behaviour.** How long between you sending the repository and the first substantive question? How long between a Slack message and an answer during your working hours? The pattern established in the first week is the pattern for the whole engagement, and it's very cheap to observe.

**Question quality.** A partner who reads a codebase properly comes back with awkward questions — *"your client's `bookings` table has no venue column, so how are two venues meant to stay separate?"* A partner who doesn't comes back with "looks good, when do we start?" That difference will cost you €4,000 and a client relationship if you find it out in week six instead of week one.

**White-label discipline.** Do they stay behind your brand without being reminded? Do their commit emails leak their own domain into a repository your client can read? Does their handover document have their logo on it? These are small things individually and they are exactly the small things that end white-label relationships.

## Design the Pilot to Be Diagnostic, Not Decorative

A badly designed pilot tells you nothing and costs a week. Five constraints make one useful.

**It has to be real.** Throwaway test tasks get throwaway effort and, worse, get staffed with whoever's free. Pick something that will actually ship in the final product, so both sides treat it as real work.

**It has to be small enough to fail safely** — three to five working days, one deliverable, one deadline. If the pilot goes badly, you've lost a week and a few hundred euros, not a client.

**It has to sit on the client's actual codebase**, not a sanitised sample. The whole point is watching someone work inside AI-generated code with inconsistent conventions, which is a different experience from working in a clean repo.

**It has to include one deliberate ambiguity.** Leave one requirement slightly underspecified — not a trap, just a normal gap of the sort every brief contains. Then watch: do they ask, assume and tell you, or assume and stay quiet? The third behaviour is the one that produces surprises in month two.

**It has to end in an artifact.** A short written handover — what changed, why, what to watch. This is the single best predictor of what the final handover will look like.

## Five Pilot Units That Work for AI-Prototype Projects

Pick one. Each is genuinely useful work, self-contained, and touches a different competence:

1. **Auth hardening** — password reset, email verification, session expiry on an existing Supabase or Firebase setup. Tests whether they can work *with* existing infrastructure rather than replacing it.
2. **One payment path end to end** — a single Stripe or Mollie flow with verified webhooks and a failed-payment case. Tests whether they know that a payment isn't confirmed until the server says so.
3. **Deployment and environments** — staging plus production, CI on push, environment variables handled properly, deployed into *your client's* accounts. Tests operational discipline, and delivers the thing agencies most often lack.
4. **One access-control fix with policies written at the database** — take a known broken route and make it right, including row-level security. Tests whether their idea of a fix is a patch or a rule.
5. **A written repository audit** — findings with file references, severity, and a remediation estimate for each. Tests exactly the artifact you'll be reselling to clients, and costs the least.

Number five is the best first pilot for most agencies, because the deliverable is portable: even if you don't proceed, you own a findings document you can use to scope the project with anyone.

## Price It Properly, and Don't Ask for It Free

Free trial work attracts the wrong partners. A team with a full pipeline declines; a team without one accepts and staffs it with someone learning on your client's code. Pay standard rates.

Realistic pilot sizing for last-mile work on an AI-built app is roughly €400–€900 — a repository audit at the low end, a payment flow or deployment setup at the top. Against a €5,000–€9,000 full engagement, that's 8–12% spent on de-risking the other 90%, which is a rate any agency principal would accept on a client project.

Bill it through to your client as a discovery or technical audit phase. Clients accept this readily — it maps onto how they already think about design discovery — and it means the pilot costs your agency nothing but attention. It also protects you commercially: if the audit reveals the project is twice the size everyone assumed, you renegotiate scope with evidence in hand instead of absorbing the difference.

Two contract points, both short. The pilot carries no obligation on either side to proceed. And IP assigns to you (or your client) on payment for the pilot, independent of what happens next — otherwise a failed pilot leaves you unable to use work you paid for.

## The Scorecard

Score out of two on each, before you get sentimental about the people:

| What you're watching | 0 | 1 | 2 |
|---|---|---|---|
| Time to first substantive question | Never asked | Day 3+ | Within 24h |
| Found something you hadn't briefed | No | Mentioned in passing | Documented with a fix |
| Handled the deliberate ambiguity | Assumed silently | Assumed and mentioned later | Asked before building |
| Hit the date | Late, no warning | Late, flagged early | On time |
| Handover artifact | None | A few bullet points | Something you'd forward to a client |
| White-label discipline | Branding leaked | Reminded once | Invisible throughout |
| Behaviour when corrected | Defensive | Compliant | Explained the trade-off, then adapted |

Twelve or better and you have a partner. Below eight, you have a supplier who'll need managing, and you should price that management into the next quote or walk. The middle is where judgement lives — and where the "behaviour when corrected" row usually decides it, because that's the row that predicts month four.

## When Not to Run a Pilot

Pilots have real costs: two contracting cycles, two onboarding conversations, a week of calendar time, and a client wondering why nothing visible has happened.

Skip it when **the deadline genuinely can't absorb a week** — but be honest that you're accepting risk rather than eliminating it, and shrink the first engagement instead.

Skip it when **the whole engagement is under about €2,500**, because the overhead of splitting it exceeds what you'd learn.

Skip it when **the work isn't decomposable** — some migrations and re-architectures can't be sliced without doing the analysis anyway, in which case make the analysis the pilot.

Skip it when **you have a strong reference from someone whose judgement you trust and who used the same partner for the same kind of work recently**. That's better evidence than a pilot, and it's free.

And watch for **pilot theatre**: some firms staff pilots with their strongest engineer and then rotate. Neutralise it in one sentence — *"who's doing the pilot, and will the same people be on the main engagement?"* — and put the answer in the follow-on agreement.

## The Second Thing a Pilot Reveals: Whether You Want to Resell This

There's a strategic question hiding underneath the tactical one. Agencies rarely bring in a production partner once. If this works, you'll do it four more times this year, and what you're really evaluating is whether "our clients' AI prototypes get taken to production" can become a repeatable line on your own rate card rather than a one-off favour.

That changes what you watch for. Can they quote quickly enough for you to answer a client in two days? Is their pricing predictable enough that you can build a margin on top without guessing? Will they let you own the client relationship entirely? Do they document well enough that your own developers can maintain the result, or does every future change route back through them?

A pilot answers all four, which is why it's worth running even when you're fairly confident. You're not testing whether they can do the job; you're testing whether they can be a component of your business.

For reference on what to expect commercially: [LaunchStudio](https://launchstudio.eu/en/) works as a silent production partner behind agencies and freelancers — fixed quotes in the €800–€3,500 range for Launch Ready scopes, one to three weeks, your branding throughout, and the client's accounts holding everything from day one. The engineers come from [Manifera's offshore delivery teams](https://www.manifera.com/services/offshore-software-development/), where working invisibly inside someone else's process has been the normal operating model for over eleven years. Start with an audit pilot rather than a full build; if the scorecard doesn't clear twelve, don't send the next one.

**Bring us one real client project as a paid pilot — an audit or a single payment flow — and see how the scorecard comes out before you commit anything larger.**

## Real example

### An Agency Partner in Action: The €650 Audit That Resized a €9,000 Project

Studio Meridiaan, a six-person brand and product studio in Nijmegen, had a client with a Bolt-built marketplace for equipment rental and a launch date eleven weeks out. The studio's own team could handle design and content but had no backend capability, and founder Lieke Vermeulen was choosing between two production partners with similar quotes.

Rather than picking, she bought a €650 repository audit from each, on the same codebase, with the same three-day deadline and one deliberately vague line in the brief about how deposits should be held. One partner delivered a competent list of dependency issues on day four without asking anything. The other asked about the deposit handling within six hours, then delivered eleven findings with file references — including that the rental price was being sent from the browser to the payment call, meaning a renter could set their own price.

**Result:** Studio Meridiaan billed both audits through to the client as a discovery phase, used the stronger findings document to rescope the build from €9,000 to €11,200 with the client's agreement, and ran the full engagement with the second partner under their own branding across seven weeks.

> *"The audits cost my client €1,300 and saved them from a marketplace where the buyer picks the price. I've run every partner through the same three-day test since."*
> — **Lieke Vermeulen, Founder, Studio Meridiaan (Nijmegen)**

---

## Frequently Asked Questions

### Should I tell the partner it's a pilot, or just call it a small project?

Tell them. A partner who knows they're being evaluated puts their best foot forward, which is precisely what you want to see — you're measuring their ceiling and their process, not catching them out. It also makes the no-obligation ending straightforward rather than awkward.

### Can I run two partners on the same pilot at once?

Yes, and comparing identical briefs is far more informative than assessing one in isolation. Be transparent that it's a comparison and pay both properly; running a covert bake-off tends to get discovered and ends relationships you may want later.

### What if my client won't pay for a discovery phase?

Reframe it as risk reduction with a number attached: an audit that resizes the project before contracts are signed is cheaper than discovering the gap in week six. If they still refuse, fund it yourself for the first partner you're evaluating and treat it as business development.

### How do I stop a pilot turning into an expectation of discounted rates later?

Price the pilot at standard rates from the start and say in writing that it carries no commercial precedent. Discounted pilots create exactly the anchoring problem you're worried about, and they also signal that you'll negotiate on price rather than scope.

### Does a pilot replace the need for references and a technical review?

No — it's the third leg. References tell you about reliability over months, a technical review tells you whether the code is any good, and a pilot tells you how they behave inside your process. Each catches something the other two miss.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should I tell the partner it's a pilot, or just call it a small project?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Tell them. You are measuring their ceiling and their process rather than catching them out, and being open makes a no-obligation ending straightforward instead of awkward."
      }
    },
    {
      "@type": "Question",
      "name": "Can I run two partners on the same pilot at once?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, and identical briefs compared side by side are far more informative than one assessed alone. Be transparent that it is a comparison and pay both properly, since covert bake-offs tend to be discovered."
      }
    },
    {
      "@type": "Question",
      "name": "What if my client won't pay for a discovery phase?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Reframe it as risk reduction with a number attached, since an audit that resizes the project before contracts are signed is cheaper than discovering the gap in week six. If they still refuse, fund the first one yourself as business development."
      }
    },
    {
      "@type": "Question",
      "name": "How do I stop a pilot turning into an expectation of discounted rates later?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Price the pilot at standard rates and state in writing that it sets no commercial precedent. Discounted pilots create the anchoring problem and signal that you negotiate on price rather than scope."
      }
    },
    {
      "@type": "Question",
      "name": "Does a pilot replace the need for references and a technical review?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, it is the third leg. References cover reliability over months, a technical review covers code quality, and a pilot covers behaviour inside your process."
      }
    }
  ]
}
</script>
