---
Title: "Who Owns What: Client Relationships, Code, and Credit in White-Label Work"
Keywords: IP ownership white-label contract, agency subcontractor agreement, client relationship ownership clause, work for hire agency, non-solicitation subcontractor, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Agency / Freelancer (White-Label Partner)
---

# Who Owns What: Client Relationships, Code, and Credit in White-Label Work

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Who Owns What: Client Relationships, Code, and Credit in White-Label Work",
  "description": "Ownership disputes in white-label engineering work rarely start with malice; they start with a contract that never named who owns the code, the client relationship, or the right to reference the work. A clause-by-clause guide to settling it upfront.",
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
  "datePublished": "2027-01-17",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/who-owns-what-client-relationships-code-and-credit"
  }
}
</script>

Nobody reads the ownership clause until there's a dispute. That's not a flaw in how agencies operate — it's just how contracts work in practice, sitting unread in a folder while everyone's busy actually delivering the project, right up until the moment something goes sideways and three different parties suddenly have three different assumptions about who owns what. By then, the clause you didn't write carefully six months ago is the only thing standing between a clean resolution and an expensive one.

White-label engineering work has three separate ownership questions bundled into it, and most standard agency contracts only clearly address one of them, if that. This is a clause-by-clause walkthrough of all three, written for the moment before the dispute, when it's still cheap to get right.

## Question One: Who Owns the Code?

This is the question most agencies get right by default, mostly because it's the one client-facing brand promises already cover clearly — LaunchStudio's own standard, for instance, is that the founder always owns the code, full stop, in their own repository and accounts. The clause that needs to exist in your subcontractor agreement is one that flows this ownership through correctly: your agreement with your technical partner should explicitly state that all work product, code, and deliverables transfer to the end client (or to you, for immediate transfer to the client) upon delivery and payment, with no retained rights, licensing fees, or usage restrictions on the subcontractor's side.

The specific trap here is a subcontractor agreement that's silent on this point, defaulting to whatever jurisdiction's general work-for-hire rules happen to apply — which vary enough between contexts that "silent" is functionally the same as "unclear," and unclear ownership on the actual product being delivered is the single worst thing to discover mid-dispute. Get this in writing explicitly, even with a subcontractor you trust completely, because the clause exists for the scenario where trust isn't the operative factor — a falling-out, a subcontractor's own business dissolving, an estate dispute if something happens to a sole proprietor you've been working with. None of these are pleasant to think about in advance, which is exactly why they need to be handled in a document rather than left to good faith in the moment.

## Question Two: Who Owns the Client Relationship?

This is the question that actually causes most white-label disputes, and it's rarely about code at all — it's about who the client considers "theirs" once the engagement is underway, and what happens if either party in the agency-subcontractor relationship wants to work with that client again independently later. The clause that matters here is a mutual non-solicitation agreement, specific and time-bound: your subcontractor agrees not to solicit or directly contract with your client for a defined period (commonly twelve to twenty-four months) after the engagement ends, without your involvement or a referral fee arrangement, and you agree to a reciprocal standard regarding any of the subcontractor's other clients you might be introduced to.

This clause matters more, not less, in an "introduced specialist" disclosure posture — covered in more depth in a companion piece on [presenting a technical partner to your client](https://launchstudio.eu/en/#contact) — where the client has direct contact with your subcontractor during the engagement. Without a non-solicitation clause in place, a client who had a great experience working directly with your technical partner has every reasonable incentive to just contact that partner directly for the next project, cutting you out entirely — not necessarily out of bad faith, simply because there's nothing preventing it and the client has no obligation to route future work through you if you never established that expectation contractually.

## Question Three: Who Gets Credit, and Where

This is the question agencies most often skip entirely, and it becomes a live issue specifically around portfolio use, case studies, and testimonials — situations where both you and your technical partner might reasonably want to reference the same delivered project as proof of capability. The clause worth having: explicit, mutual agreement on what each party can reference publicly, and how. A reasonable standard is that you, as the client-facing agency, retain primary case-study rights (with client permission, separately) as the delivery partner of record, while your technical subcontractor retains the right to reference the engineering work in generalized terms — "helped launch a booking platform for an EU-based client" — without naming the client, the agency, or specific proprietary details, unless you've explicitly agreed otherwise for a specific project.

This matters more than it might seem, because credit disputes are disproportionately damaging to a subcontractor relationship relative to how small they often are in dollar terms — a technical partner publicly referencing "delivered production security for [Client Name]" without your knowledge, in a context where the client believed the work was entirely yours under an invisible white-label posture, is exactly the kind of disclosure mismatch that can cost you a client relationship over something that was never actually about the work quality at all.

## A Fourth Question Hiding Inside the First Three: Data Processing Chains

Once your subcontractor handles any of the client's user data — which, on a launch engagement touching authentication, payments, or hosting, is nearly always — a fourth ownership-adjacent question arrives that many agencies miss entirely: who is the data processor, and does the chain of agreements actually reflect reality under GDPR. If you've signed a Data Processing Agreement with your client as the data processor, but your subcontractor is the party actually touching production data on your behalf, your subcontractor is legally a sub-processor, and GDPR requires that relationship to be documented too, with your client's awareness that a sub-processor is involved. Skipping this isn't just a paperwork gap; it's the kind of thing that surfaces badly during an enterprise client's security questionnaire, or worse, during an actual data incident, when "who exactly had access to this data, under what agreement" turns out to have no clean answer. Building a standard sub-processor clause into your subcontractor agreement — one that flows the same data-handling obligations you've committed to your client down to your subcontractor — closes this gap before it becomes a live problem rather than a theoretical one.

## Drafting This Without a Full Legal Team

None of this requires an expensive, bespoke legal engagement to get right — a template subcontractor agreement covering these three areas, reviewed once by a lawyer for your specific jurisdiction and then reused across engagements, is the practical standard most agencies running white-label work at any real volume land on. The one-time cost of getting a lawyer to review a template non-solicitation and IP-assignment clause, typically a few hundred euros, is small relative to the cost of even one dispute resolved without clear contractual language to point to. Ask any technical partner you're considering working with regularly whether they have a standard agreement they use for exactly this kind of relationship — a partner who's done this before, at volume, usually already has language ready, which is itself a useful signal about how seriously they take the commercial side of the relationship rather than just the delivery side.

## What Happens Without These Clauses

Worth being concrete about the actual failure mode, because "get this in writing" can sound like generic caution until you picture the specific scenario it prevents. A subcontractor agreement silent on code ownership means a dispute over final delivery — a payment disagreement, a scope disagreement — can leave a client's product in genuine limbo, with no clear contractual party obligated to hand over clean, complete code and access. A relationship silent on non-solicitation means your best subcontractor becomes, over enough engagements, a direct competitor for your own client base, armed with the exact relationships and reputation you paid to build. A relationship silent on credit means a public case study, posted with good intentions, becomes a client-trust crisis over a disclosure posture nobody actually agreed to in the first place. None of these outcomes require anyone to act in bad faith — they happen because the document that should have named the boundary never did, and reasonable people on both sides interpreted the gap differently once it mattered.

## Handling Access and Handover If the Relationship Ends

One more scenario worth naming explicitly in the agreement, because it's easy to overlook while a relationship is going well: what happens to code, credentials, and account access if you and your subcontractor stop working together. A clause requiring a clean, documented handover — all access credentials returned or rotated, all code delivered in its final state to the client's own repository, no residual access left dangling on either side — protects everyone, including the client, from the messiest version of a subcontractor relationship ending badly. Without this, a dissolved partnership can leave a client's production systems with orphaned access nobody remembers to revoke, which is a security liability that has nothing to do with the quality of engineering that was originally delivered and everything to do with a process nobody thought to formalize while the relationship was still working.

## Reviewing an Existing Relationship for Gaps

If you're already running white-label engagements without having addressed these three questions explicitly, the fix isn't necessarily re-papering everything at once — start with whichever gap carries the most active risk given your current relationships. An agency working with a subcontractor who has direct client contact under an introduced-specialist posture should prioritize the non-solicitation clause first, since that's the highest-probability dispute given the current setup. An agency planning to use delivered projects in marketing materials soon should settle the credit question before the first case study goes live, not after a subcontractor objects to how they were represented, or weren't.

[LaunchStudio](https://launchstudio.eu/en/) operates from standard agreements that address all three of these questions clearly with every agency partner, reflecting [Manifera's 11+ years of running exactly this kind of commercial relationship at scale](https://www.manifera.com/about-us/) — which means the clauses this article describes aren't theoretical, they're the actual terms a Manifera partnership starts from.

Get our standard subcontractor terms as a starting point for your own agreement — [book a 15-minute call](https://launchstudio.eu/en/#contact) and we'll walk through what's in them and why.

## Real example

### An Agency Partner in Action: The Case Study That Caused a Falling-Out

Joris Bakker ran a small product studio in Delft that had worked with the same freelance backend developer on white-label launch projects for over a year, on nothing more formal than an informal day-rate agreement with no written IP or non-solicitation terms. When the developer published a portfolio case study naming Joris's biggest client directly, describing the security work in specific technical detail the client had never agreed to have made public, the client — who believed the entire engagement had been handled invisibly by Joris's studio alone — called Joris directly, upset and confused about who else had access to their systems.

Joris had no contractual basis to have prevented the disclosure, since nothing in his informal arrangement with the developer had addressed credit or public reference rights at all, and the relationship with both the developer and, more damagingly, the client became strained over something that had nothing to do with the quality of the actual delivered work.

**Result:** Joris moved to a written subcontractor agreement for every future technical partner, explicitly covering code ownership, a two-year non-solicitation term, and a defined credit policy requiring his sign-off before any project reference goes public — and has had zero recurrence of the issue across the eleven engagements since.

> *"The work was excellent. The falling-out had nothing to do with skill and everything to do with something we'd simply never written down. That's a cheap lesson compared to what it could have cost."*
> — **Joris Bakker, Founder, Bakker Studio (Delft)**

## Frequently Asked Questions

### Do I need a lawyer to draft a subcontractor agreement, or can I use a template?

A template covering code ownership, non-solicitation, and credit rights, reviewed once by a lawyer familiar with your jurisdiction, is the practical standard for most agencies — a full bespoke legal drafting exercise for every subcontractor relationship is rarely necessary once you have a solid reusable template in place.

### How long should a non-solicitation clause typically last?

Twelve to twenty-four months after an engagement ends is common in white-label engineering relationships, balancing reasonable protection for the agency against the recognition that a client relationship can't be permanently locked away from a subcontractor forever.

### What if my technical partner already has their own standard agreement?

Review it carefully against the three questions in this article — code ownership, client relationship protection, and credit rights — rather than assuming a partner's own template automatically covers your interests as the agency in the relationship.

### Can I still let my technical partner reference our work together in their portfolio?

Yes, and it's often reasonable to allow generalized references, like project type and outcome without naming your specific client, while reserving named, detailed case studies for your own sign-off, particularly if your disclosure posture with the client was invisible or named-partner rather than fully introduced.

### What's the biggest mistake agencies make with these agreements?

Treating an informal, trust-based arrangement as sufficient because the relationship has gone well so far — the clauses exist specifically for the scenario where trust stops being the operative factor, whether through a falling-out, a business change, or simple miscommunication about what was always assumed rather than agreed.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need a lawyer to draft a subcontractor agreement, or can I use a template?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A template covering code ownership, non-solicitation, and credit rights, reviewed once by a lawyer familiar with your jurisdiction, is the practical standard for most agencies rather than a full bespoke drafting exercise each time."
      }
    },
    {
      "@type": "Question",
      "name": "How long should a non-solicitation clause typically last?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Twelve to twenty-four months after an engagement ends is common, balancing reasonable protection for the agency against the recognition that a client relationship can't be permanently locked away from a subcontractor forever."
      }
    },
    {
      "@type": "Question",
      "name": "What if my technical partner already has their own standard agreement?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Review it carefully against code ownership, client relationship protection, and credit rights, rather than assuming a partner's own template automatically covers your interests as the agency in the relationship."
      }
    },
    {
      "@type": "Question",
      "name": "Can I still let my technical partner reference our work together in their portfolio?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, generalized references without naming the specific client are often reasonable, while named, detailed case studies should typically require your sign-off, particularly under an invisible or named-partner disclosure posture."
      }
    },
    {
      "@type": "Question",
      "name": "What's the biggest mistake agencies make with these agreements?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Treating an informal, trust-based arrangement as sufficient because the relationship has gone well so far, when the clauses exist specifically for the scenario where trust stops being the operative factor."
      }
    }
  ]
}
</script>
