---
Title: "Comparing Two Quotes Properly When You Can't Judge the Technical Detail"
Keywords: comparing development quotes, normalise software quotes, evaluating dev proposals, fixed price vs hourly, choosing a development partner, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Comparing Two Quotes Properly When You Can't Judge the Technical Detail

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Comparing Two Quotes Properly When You Can't Judge the Technical Detail",
  "description": "Two quotes for the same prototype rarely describe the same work, which makes the cheaper number meaningless on its own. This is a step-by-step method for rewriting both quotes into one comparable sheet, pricing the gaps, and deciding without being able to read a line of code.",
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
  "datePublished": "2027-01-06",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/comparing-two-quotes-when-you-cant-judge-the-detail"
  }
}
</script>

Eleven line items in one quote. Two paragraphs in the other. Same prototype, same brief, same week — and a €7,000 gap between them.

Most founders in this position do the only thing available to them: they read both documents several times, feel vaguely uneasy, and then pick based on which person they liked more on the call. That's not an unreasonable tiebreaker, but it's a terrible primary criterion, because the two documents almost certainly aren't describing the same work. Before you can compare prices you have to make the two quotes comparable, and that is a task you can do entirely without technical knowledge. It takes about ninety minutes and a spreadsheet.

## First, Accept That You're Not Comparing Prices Yet

A software quote is two things fused into one number: a scope (what will exist when they're done) and a risk position (who pays if it takes longer than expected). Two quotes can differ by 4× while both being honest, because one includes hosting setup, payment integration, a migration of your test data, and thirty days of bug fixes, and the other includes "backend work."

So the first move is to stop treating the totals as data. Write both numbers on a sticky note, put it face down, and don't look at it again until the end of this process. Everything that follows is about reconstructing what each quote actually contains.

## Build One Sheet With Twelve Rows

Open a spreadsheet. One column for each vendor, plus a first column with these rows. This list isn't arbitrary — every row on it is something founders routinely discover was nobody's job after the invoice was paid.

1. **Authentication** — signup, login, password reset, email verification
2. **Permissions** — who can see and change whose data, enforced on the server
3. **Payments** — provider, subscription vs one-off, failed-payment handling, refunds
4. **Database** — schema changes, indexes, backups, and who owns the account
5. **Hosting and deployment** — which platform, whose account, who pays the monthly bill
6. **Domain, SSL, email sending** — including deliverability setup for transactional email
7. **Data migration** — moving your existing test or real users to the new setup
8. **Environments** — is there a staging copy, or does everything change on the live site?
9. **Testing** — what gets tested, by whom, and what "done" means
10. **Documentation and handover** — can another developer pick this up in six months?
11. **Post-launch support** — how long, what's covered, response times
12. **Ownership and access** — code repository, cloud accounts, third-party keys, in whose name

Now go through each quote line by line and put its own words into the matching row. Where a quote says nothing about a row, write **"not mentioned"** in red. Do not write "probably included." The whole value of this exercise lives in the red cells.

## A Worked Example

Here's a real-shaped comparison for a Lovable-built booking app, after normalisation:

| Row | Vendor A — €2,900 fixed | Vendor B — €11,400 (est., hourly) |
|---|---|---|
| Authentication | "Harden existing Supabase auth, add password reset" | "Rebuild auth with NextAuth" |
| Permissions | "Server-side access rules per organisation" | Not mentioned |
| Payments | "Stripe subscriptions + failed payment retry" | "Stripe integration" |
| Database | "Keep existing schema, add indexes, enable backups" | "New schema, migrate data" |
| Hosting | "Deploy to your Vercel account, you own the billing" | "Deployed to our managed platform" |
| Domain/SSL/email | "Included; Resend for transactional email + SPF/DKIM" | Not mentioned |
| Migration | "Existing 40 test users migrated" | "Migrate data" (unquantified) |
| Environments | "Staging + production" | Not mentioned |
| Testing | "Manual test pass on 14 listed flows before go-live" | "QA as needed" |
| Handover | "README + architecture note + 1h walkthrough call" | Not mentioned |
| Support | "30 days bug fixes included" | "Support at €95/hour" |
| Ownership | "All code and accounts in your name" | "Repo in our org, transferred on final payment" |

Notice what just happened. The expensive quote has *more* red cells, not fewer. It's also the one that rebuilds a working frontend and holds your code in its own organisation until final payment. That is not automatically disqualifying — some excellent teams work that way — but it is now a visible, discussable fact rather than an invisible one.

## Send Both Vendors the Same Three Questions

Red cells aren't accusations; they're usually just omissions. Fill them in with one email, identical to both, which also tells you something about responsiveness:

> Hi — I'm comparing two proposals and I want to make sure I'm reading yours fairly. Three questions:
>
> 1. Of these twelve items, which are included in your price, which are explicitly excluded, and which would be extra? [paste the list]
> 2. If the work takes 50% longer than you expect, what happens to the price and to my timeline?
> 3. At the end, whose accounts hold the code, the database, and the hosting — and what would it take to move to another developer six months later?

Question 2 is the one that separates a fixed price from a fixed-price-shaped estimate. Question 3 is the one that separates a partner from a landlord.

Answers should arrive within a business day or two. A vendor who takes eight days to answer three yes/no questions while trying to win your business will not be faster once they have your money.

## Price the Red Cells Yourself

Once the blanks are filled in, put a euro figure next to every excluded item so that both totals mean the same thing. You can use rough public numbers — you're not producing an audit, you're producing comparability:

- **Payment integration** done properly (webhooks verified, retries, refunds): roughly €400–€1,200 of work
- **Server-side permissions** on a multi-user app: €500–€1,500 depending on how many roles you have
- **Hosting and deployment setup**, done once and documented: €200–€600
- **Transactional email with deliverability** (SPF, DKIM, a real sending domain): €150–€400
- **A staging environment**: usually €200–€500 to set up, and the thing that prevents you breaking your live site at 11pm
- **Thirty days of post-launch bug fixing**: at €95/hour, budget 6–10 hours, so €570–€950

Add the relevant figures to whichever quote excluded them. In the example table above, Vendor B's €11,400 becomes something closer to €13,500–€15,000 once permissions, email, staging and support are priced in — and the ownership question stays unresolved.

Sometimes the exercise runs the other way and the cheap quote turns out to be cheap because it's leaving out the two things that matter most. That result is just as useful and considerably more common than founders expect.

## Compare Who Absorbs the Surprise

Every prototype hides something. The relevant question isn't whether surprises appear, it's who pays for them.

A **fixed price** transfers that risk to the vendor. They looked at your code, they made a judgement, and if it takes 40% longer than they thought, that's their problem. The trade is that you're paying a premium for that certainty, and the vendor will be strict about scope changes — which is reasonable, since scope discipline is what makes the fixed price possible.

An **hourly estimate** transfers the risk to you. It's often cheaper if everything goes well, and everything rarely goes well in a codebase generated by prompting. When you see "estimate: 90–120 hours," treat 120 as the number and ask what happens at 150.

Neither model is superior. But you should know which one you bought, and a founder who can't afford a 60% overrun should not be buying the second one no matter how attractive the headline number looks.

The payment schedule tells you the same story from a different angle, so add it as a thirteenth row. A quote asking for 100% up front is asking you to carry all of the risk in exchange for none of the certainty. A quote asking for nothing until the end is unusual and often means the vendor is under-resourced and hoping. The healthy shapes for small engagements are roughly 50/50 split across a start and a verified finish, or three payments tied to named milestones — and crucially, the last payment should be released against something you can check yourself, not against "completion" as declared by the person invoicing you. If a vendor resists tying the final tranche to the acceptance criteria in their own scope, ask why; the answer is usually that the criteria aren't specific enough to be checkable, which is a scope problem you'd rather surface now.

## When They're Still Not Comparable, Make Them Quote Each Other

If after all this the two proposals still describe genuinely different projects — one hardening your existing app, one rebuilding it — you have one clean move left. Send each vendor the *other's* scope, anonymised, and ask: **"Can you price this specific scope, and if you think it's the wrong scope, tell me why in three sentences."**

This is the most informative €0 you'll ever spend. You'll learn whether the expensive vendor can articulate a real reason for the rebuild beyond preference, and whether the cheap vendor is cheap because they're efficient or because they're skipping the part that keeps your users' data separate. You'll also see how each one behaves when challenged, which is the behaviour you'll be living with for the next three months.

## The Tiebreak That Isn't Price

If two normalised quotes land within about 15% of each other, price has stopped being a useful signal — the difference is inside the noise of estimation. Break the tie on things that compound:

- **Who owns the accounts on day one.** Code and cloud accounts in your name from the start removes an entire category of future hostage situation.
- **How specific they were about your code.** A vendor who named files and found a real flaw during scoping has already demonstrated the skill you're buying.
- **What their handover contains.** If the answer is "we'll document it," ask to see a documentation example from a past project with the client details removed.
- **Whether they said no to anything.** A vendor who agreed to everything either misunderstood the brief or intends to renegotiate later.

For calibration on the market: traditional agencies quote €20,000–€500,000 and typically want to rebuild; freelancers land between €5,000 and €20,000 with wide quality variance. [LaunchStudio](https://launchstudio.eu/en/) sits deliberately at the other end — €800–€3,500 for last-mile hardening, one to three weeks, frontend untouched, everything in your accounts — because the engineering comes from a team that has already shipped 160+ production projects at [Manifera](https://www.manifera.com/portfolio/) and is doing a narrow job rather than an open-ended one. Put us in column three of your sheet and apply the same red cells. If another quote survives the normalisation better, that's the right answer.

**Want a sanity-check number before you start? The [LaunchStudio price calculator](https://launchstudio.eu/#calculator) gives you a realistic range in about a minute — useful as a third data point when two quotes disagree by an order of magnitude.**

## Real example

### A Founder in Action: The Quote That Got Cheaper by Getting Bigger

Thijs van Ommeren, a former events producer in Eindhoven, built StageCrew — a Lovable app for booking freelance technical crew for venues — and received quotes of €3,400 and €12,800. He assumed the second was thorough and the first was naive, and had nearly signed the expensive one.

Normalising both onto a twelve-row sheet reversed his reading. The expensive proposal excluded permissions between venues (crucial, since venues must never see each other's booking rates), said nothing about transactional email, and held the repository in the vendor's own GitHub organisation until final payment. The cheaper one covered all three explicitly. When Thijs sent both vendors the same three questions, the expensive vendor's answer to the overrun question was "we'd discuss it," and the cheaper vendor's was a named cap.

**Result:** Thijs hired the cheaper vendor for €3,400 fixed, added venue-level data separation and Mollie subscription billing for a further €900 agreed up front, and went live in eleven working days with every account in his own name.

> *"I nearly paid four times more for a proposal that was missing the two things I actually lay awake about. The spreadsheet took me an evening and it was the highest-paid evening of my year."*
> — **Thijs van Ommeren, Founder, StageCrew (Eindhoven)**

---

## Frequently Asked Questions

### Is it rude to send both vendors the same list of questions?

No — it's normal procurement, and good vendors expect it. If anything, a partner who takes structured comparison as an insult is telling you how they'll react the first time you question an invoice.

### What if one vendor refuses to break their price into line items?

Ask once, framed around your own need rather than distrust: "I need to compare like for like — can you split this into scope areas?" A refusal to itemise usually means either the price is a round-number guess or the scope hasn't been thought through, and both are things you want to find out before signing rather than after.

### Should I always add the excluded items to the cheaper quote and then re-rank?

Yes, but note whether an exclusion is deliberate or accidental. A vendor who says "hosting is excluded because you should own that account and it costs you €20 a month" is making a defensible choice; a vendor who simply never mentioned hosting hasn't thought about it.

### How much price difference is meaningful once both quotes are normalised?

Below roughly 15% the gap is inside normal estimation error and you should decide on ownership, specificity and handover instead. Above 2×, one of the two proposals is solving a different problem and you need to find out which one matches the problem you actually have.

### Can I show one vendor's price to the other to negotiate?

You can, but it tends to produce a discounted version of the same scope rather than a better proposal. Asking a vendor to price the competing *scope* gets you far more useful information than asking them to beat a competing *number*.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is it rude to send both vendors the same list of questions?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, it is normal procurement and good vendors expect it. A partner who treats structured comparison as an insult is showing you how they will react the first time you question an invoice."
      }
    },
    {
      "@type": "Question",
      "name": "What if one vendor refuses to break their price into line items?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ask once, framed around your need to compare like for like. A refusal to itemise usually means the price is a round-number guess or the scope has not been thought through, and both are better discovered before signing."
      }
    },
    {
      "@type": "Question",
      "name": "Should I always add the excluded items to the cheaper quote and then re-rank?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, but note whether each exclusion is deliberate or accidental. Excluding hosting so you own the account is a defensible choice; never mentioning hosting means it was not considered."
      }
    },
    {
      "@type": "Question",
      "name": "How much price difference is meaningful once both quotes are normalised?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Below roughly 15% the gap sits inside normal estimation error, so decide on ownership, specificity and handover instead. Above 2x, one proposal is solving a different problem and you need to identify which matches your actual problem."
      }
    },
    {
      "@type": "Question",
      "name": "Can I show one vendor's price to the other to negotiate?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You can, but it usually produces a discounted version of the same scope rather than a better proposal. Asking a vendor to price the competing scope yields far more information than asking them to beat a competing number."
      }
    }
  ]
}
</script>
