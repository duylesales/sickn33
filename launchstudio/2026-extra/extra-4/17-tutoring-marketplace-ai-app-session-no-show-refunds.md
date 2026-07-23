---
Title: "AI Tutoring Marketplaces: Session No-Shows Break the Refund Logic Nobody Tested"
Keywords: ai saas, two-sided marketplace, tutoring marketplace app, no-show refund logic, ai-generated code
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# AI Tutoring Marketplaces: Session No-Shows Break the Refund Logic Nobody Tested

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Tutoring Marketplaces: Session No-Shows Break the Refund Logic Nobody Tested",
  "description": "AI-built tutoring marketplaces usually handle the student no-show case and quietly forget the tutor no-show case, leaving paying students charged in full with no refund path when the tutor is the one who doesn't show.",
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
  "datePublished": "2026-07-23",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/tutoring-marketplace-ai-app-session-no-show-refunds"
  }
}
</script>

Everyone tests the happy path. Everyone also remembers to test what happens when the customer doesn't show up — that's the obvious edge case, the one every marketplace founder thinks to ask their AI builder for. Almost nobody tests the opposite scenario: what happens when the person getting paid is the one who doesn't show. That asymmetry is exactly where a lot of AI-generated tutoring marketplaces quietly fall apart.

## The Refund Logic Every Marketplace Founder Forgets to Test

When you prompt an AI builder to "handle no-shows" for a two-sided booking marketplace, it tends to build the version that protects the person paying — a student misses a session, gets flagged, maybe loses eligibility for a refund depending on the cancellation window. That's a reasonable default, and it's the scenario most founders describe when they're specifying the feature, because it's the one that protects the business model: don't refund people who wasted a tutor's time. What that default quietly assumes is that the *tutor* is always the reliable party. Nothing in most prompts specifies what happens when that assumption breaks.

## Four No-Show Scenarios, and the One Everyone Skips

A complete no-show policy for a two-sided marketplace actually needs to handle four distinct cases: the student doesn't show and the tutor is paid regardless (or not, per your policy), the tutor doesn't show and the student needs a full refund, both parties show but the session is cut short, and neither party shows and the booking simply lapses. Most AI-generated implementations we've reviewed handle exactly one of these cleanly — student no-show — because it's the version the founder described in detail. The tutor no-show path is either entirely missing or routes through the same logic as a normal completed session, meaning the student's payment is captured and released to the tutor as if the session happened, with no refund mechanism at all.

## Why This Is a Trust-and-Retention Problem, Not Just a Refund Bug

A missing refund path doesn't just cost you one angry support ticket. In a tutoring marketplace, trust between student and platform is the entire product — parents booking sessions for their kids, students prepping for exams on a deadline, adults fitting lessons around a work schedule. A tutor no-show that results in a full charge with no recourse is the fastest way to turn a paying customer into a public complaint, and in a marketplace still building its reputation, a handful of stories like that can outweigh months of good word-of-mouth. Our engineers have shipped 160+ projects for enterprise clients, and the lesson that carries over directly to marketplace founders is the same one every payments-heavy product eventually learns: the exception paths are the product, because that's what people remember.

## Building Refund Logic That Actually Covers Both Sides

Fixing this means treating no-show handling as a state machine with a defined outcome for each of the four scenarios above, not a single "no-show" flag applied uniformly regardless of which party missed the session. It also means the tutor no-show path needs its own trigger — ideally something the student or an admin can confirm — that routes to an automatic or fast-tracked refund rather than silently completing the transaction. Our team, working out of LaunchStudio's Singapore hub, builds this as an explicit rules layer sitting on top of your existing Stripe integration, so the payment logic reflects what actually happened in the session rather than defaulting to "assume it went fine."

You can [describe your project here](https://launchstudio.eu/en/#contact) and we'll respond within one business day with a read on what your current no-show logic actually covers. For a sense of how Manifera approaches marketplace payment architecture more broadly, see our [offshore software development](https://www.manifera.com/services/offshore-software-development/) practice, which supports exactly this kind of scoped engineering work.

## Real example

### An AI-Native Founder in Action: The No-Show Nobody Planned For

Sanne Kok, a founder in Delft, built BijlesMatch — an online tutoring marketplace connecting students with tutors for subject-specific lessons — using Lovable. The booking and payment flow worked well, and the student no-show policy — charge the student, no refund, if they cancel too close to the session — was implemented exactly as specified.

The gap surfaced when a tutor simply didn't join a scheduled video session. The student had already been charged at booking, as designed. But because the app's no-show logic only had a defined path for student no-shows, the session was marked "completed" by default once the scheduled time passed, and the payment was released to the tutor as normal. The student messaged Sanne directly asking why they'd been charged in full for a lesson that never happened, and Sanne discovered there was no refund mechanism for this scenario at all — not a missing button, but a missing code path.

LaunchStudio's engineers rebuilt the no-show logic into four explicit outcomes covering both student and tutor no-shows, added a student-side "tutor didn't show" report that triggers an automatic refund hold pending confirmation, and adjusted the payment-release timing so funds aren't released to the tutor until session completion is actually confirmed by both sides or a defined timeout passes.

**Result:** tutor no-shows now trigger an automatic refund path instead of silently completing as a paid session, closing the exact gap that had gone untested.

> *"I built the no-show policy from the student's side because that's the risk I was worried about protecting the business from. I never once thought to ask: what if it's the tutor who flakes?"*
> — **Sanne Kok, Founder, BijlesMatch (Delft)**

**Cost & Timeline:** €700 (four-state no-show logic rebuild, tutor no-show refund path, payment-release timing fix) — completed in 3 business days.

---

## Frequently Asked Questions

### Why do AI builders default to only handling student no-shows?

Because founders typically describe the no-show feature from the perspective of protecting revenue against the paying customer, and the AI implements exactly that scenario rather than inferring the symmetric case on the other side of the marketplace.

### How common is this gap in two-sided marketplace apps?

Very common — any marketplace where one side pays and the other side delivers a scheduled service tends to have this same asymmetry, whether it's tutoring, coaching, fitness classes, or consulting sessions.

### What does a properly built no-show policy actually require?

It needs explicit, separate outcomes for each combination of who did and didn't show, tied to distinct triggers — cancellation windows, no-show reports, and timeout-based confirmations — rather than a single flag applied to every case.

### Does LaunchStudio only work with founders who already have paying customers?

No — we work with founders at consideration stage too, reviewing a prototype before real transaction volume exposes a gap like this one, which is often cheaper and faster than fixing it after a support backlog builds up.

### Is LaunchStudio's Singapore team experienced with marketplace-specific payment logic?

Yes — Singapore is LaunchStudio's Southeast Asia hub, and two-sided marketplace payment and refund architecture is one of the most frequent project types the team there handles.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why do AI builders default to only handling student no-shows?",
      "acceptedAnswer": { "@type": "Answer", "text": "Founders typically describe the no-show feature from the perspective of protecting revenue against the paying customer, and the AI implements exactly that scenario rather than inferring the symmetric case." }
    },
    {
      "@type": "Question",
      "name": "How common is this gap in two-sided marketplace apps?",
      "acceptedAnswer": { "@type": "Answer", "text": "Very common — any marketplace where one side pays and the other side delivers a scheduled service tends to have this same asymmetry, whether it's tutoring, coaching, fitness classes, or consulting." }
    },
    {
      "@type": "Question",
      "name": "What does a properly built no-show policy actually require?",
      "acceptedAnswer": { "@type": "Answer", "text": "Explicit, separate outcomes for each combination of who did and didn't show, tied to distinct triggers — cancellation windows, no-show reports, and timeout-based confirmations." }
    },
    {
      "@type": "Question",
      "name": "Does LaunchStudio only work with founders who already have paying customers?",
      "acceptedAnswer": { "@type": "Answer", "text": "No — LaunchStudio also reviews prototypes at consideration stage before real transaction volume exposes gaps like this one, often cheaper than fixing it after a support backlog builds up." }
    },
    {
      "@type": "Question",
      "name": "Is LaunchStudio's Singapore team experienced with marketplace-specific payment logic?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes — Singapore is LaunchStudio's Southeast Asia hub, and two-sided marketplace payment and refund architecture is one of the most frequent project types the team there handles." }
    }
  ]
}
</script>
