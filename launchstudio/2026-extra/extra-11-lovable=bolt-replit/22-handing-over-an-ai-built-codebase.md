---
Title: "Lovable Developer Handover: What a Proper One Contains"
Keywords: lovable developer, handover documentation, code ownership founder, agency white label delivery, runbook known issues, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Agency / Freelancer (White-Label Partner)
---

# Lovable Developer Handover: What a Proper One Contains

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Developer Handover: What a Proper One Contains",
  "description": "The nine things that should change hands when an engagement ends: repository, accounts, secrets, runbook, known issues and the decisions nobody wrote down — with a checklist for founders and agencies on both sides of the delivery.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-24",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/handing-over-an-ai-built-codebase" }
}
</script>

A handover is not a moment. It is a set of objects, and the reason so many engagements end badly is that everyone treats it as an event — a final call, a "you're all set", an invoice — rather than a delivery with a contents list.

The test is simple and unforgiving: three months after the engagement ends, with the original engineer unreachable, can a competent stranger pick this up and make a change safely? For most AI-built products that have passed through a freelancer or an agency, the answer is no, and the reason is rarely bad faith. It is that nobody agreed what handover meant.

## Nine Things That Should Change Hands

**One: the repository, in your account.** Not shared with you, not exported as a zip — owned by you, with the full commit history. History matters: it is how the next person understands why something is the way it is, and it is where you check whether credentials were ever committed.

**Two: every account, in your name.** Hosting, database, domain registrar, payment provider, email service, error tracking, any AI or third-party API. Your email, your billing details, contractors granted access you can revoke. This is the item most often skipped and the most expensive to fix later.

**Three: a secrets inventory.** A list of every credential the application uses, where each one lives, what it unlocks and how to rotate it. Not the values in a document — the map. Anyone who has held the values should be assumed to still have them, so this list is also your rotation plan.

**Four: a runbook.** One page: how to run the app locally, how to deploy, how to roll back, how to restore a backup, and what to do when the site is down. Written for someone who was not there.

**Five: the architecture in plain language.** Two paragraphs and, ideally, a rough diagram: what talks to what, where data lives, which parts are third-party. The next engineer will reconstruct this in a day if it does not exist, and charge you for the day.

**Six: the decisions and their reasons.** Why this region, why this payment provider, why the access model works the way it does, which approaches were tried and rejected. This is the knowledge that evaporates completely when someone leaves, and it is cheap to record while it is fresh.

**Seven: an honest known-issues list.** Everything found and not fixed, everything deferred, everything the engineer would do differently with more budget. A handover with no known issues is not a clean codebase; it is an incomplete document.

**Eight: the tests and how to run them,** along with what they cover and, more usefully, what they do not.

**Nine: a support window.** Two weeks of availability for questions, agreed in advance and priced in. Not open-ended maintenance — a defined period during which "how does this bit work" gets an answer.

## The AI-Specific Additions

An AI-built codebase has three items that a traditional handover does not need, and they are the ones that determine whether you can keep working the way you were.

**Can it still be edited in the original tool?** If work was done in Lovable, Bolt or Cursor, the handover should state explicitly whether the project remains editable there, and if the structure changed, what that means for future prompting. A founder who loses this has quietly lost the cheap iteration loop they built the product to have.

**Which parts were generated and which were written deliberately.** The next person treats these differently: generated code needs verification, hand-written code carries intent. A note in the README saves a great deal of guessing.

**Where generated patterns were deliberately left alone.** Sometimes the right call is not to refactor something that works. Saying so prevents the next engineer from "fixing" a deliberate decision.

## For Agencies: Handover Is Part of the Product

If you deliver AI-built products for clients, the handover is where your reputation is made or quietly damaged, because it is the part the client experiences after the excitement has faded.

Two practices separate agencies that get repeat work from those that do not. First, handover artefacts are produced during the engagement, not assembled at the end — the runbook is written when the deploy pipeline is built, the decisions are recorded when they are made. Assembling it afterwards takes three times as long and produces something thinner.

Second, the handover is demonstrated rather than sent. A forty-minute call in which the client deploys a trivial change themselves, follows the runbook to restore a backup into a scratch environment, and opens the error tracker, is worth more than a twenty-page document. It also surfaces the gaps while you are still engaged rather than three months later.

For white-label work the same applies, one step removed: your production partner hands you a pack you can pass on under your own brand, which is only possible if it was written to be read by someone who was not in the room.

## What Founders Should Ask For Before Signing

Put the handover in the brief, not in the final week. Five lines is enough: the repository and all accounts in my name from day one, a runbook covering deploy, rollback and restore, a secrets inventory, a known-issues list, and confirmation that I can still edit the project in the tool I started with.

Then verify it before the final payment. Make a small change yourself and deploy it. Follow the runbook to restore a backup. Rotate one credential using the inventory. If all three work, the handover is real. If any of them stalls, you have found the gap while you still have leverage.

## The Cost of Getting This Wrong

The visible cost is the next engineer's ramp-up, typically a week of paid archaeology to reconstruct what a two-page document would have said.

The invisible costs are worse. Accounts in someone else's name become a negotiation, occasionally an unpleasant one. Credentials held by former contractors remain valid indefinitely because nobody knows where they all are. A product that can no longer be edited in its original tool loses the iteration speed that justified building it that way. And a known-issues list that was never written means the same problem is discovered three times by three different people, each of whom charges you to find it.

None of that is dramatic. It is simply a tax on everything you do afterwards.

## How We Hand Things Over

LaunchStudio treats the handover as a deliverable with a contents list rather than a courtesy: repository and accounts in your name from the start, documented changes with reasons, a runbook covering deploy, rollback and restore, a secrets inventory with rotation instructions, the tests and their limits, an honest list of what we found and did not fix, and an explicit statement that the codebase remains conventional and AI-readable so you can keep working in Lovable, Bolt or Cursor. Two weeks of support afterwards is included rather than sold.

That discipline comes from Manifera, where eleven years of enterprise delivery for clients including Vodafone, TNO and CFLW means handovers are audited rather than assumed. Agencies use the same pack under their own branding when we work as a silent production partner.

If you are commissioning work on an AI-built product, or delivering it for a client, [describe your project](https://launchstudio.eu/en/#contact) and we will send you the handover contents list we work to — whether or not you engage us.

## If You Never Received a Handover

Most founders reading this are not commissioning work — they are holding a product that was handed over badly, or not at all. Reconstructing the pack yourself is possible and worth an afternoon.

**Start with an inventory of accounts.** Go through your card statements and your email for every service the product might use. Founders routinely find subscriptions they had forgotten and, more usefully, services registered in someone else's name.

**Establish what you can actually do alone.** Can you deploy a change? Restore a backup? Rotate a key? Whatever stalls is your highest-priority gap, and the answer tells you what to ask a new engineer for first.

**Write the architecture paragraph yourself,** badly. Two sentences describing what talks to what, even if imprecise, is better than nothing and gives the next engineer something to correct rather than to invent.

**Ask the previous developer three specific questions,** not an open request for documentation. "Where are the environment variables stored", "how do I deploy", and "what would you fix first" get answered; "can you send me the docs" does not.

**Then rotate everything** you cannot account for. It is the cheapest way to close a handover you never received.

## The Handover Conversation Itself

The documents matter less than the forty minutes in which they are demonstrated, and that session has a shape worth following.

**Start with the map, not the details.** Two minutes on what talks to what. Everything afterwards lands better once the listener has a frame.

**Then do, rather than describe.** The person receiving the handover deploys a trivial change themselves, with the outgoing engineer watching and saying nothing unless asked. Anything that stalls is a gap in the runbook, discovered at the only moment it is cheap to fix.

**Walk the failure paths.** Where the error tracker lives, what the last three incidents looked like, what to do when the site does not respond. Recovery is what people need to have seen once.

**Read the known-issues list aloud.** Written lists get skimmed; spoken ones get questioned, and the questions surface context that never made it into the document.

**Record it.** A forty-minute recording is the cheapest documentation ever produced, and it is what the next engineer watches in month four when nobody involved is reachable.

## Real example

### An Agency That Lost a Client to a Missing Runbook

Bureau Nordkaap, a six-person digital studio in Leeuwarden, delivered a membership platform for a regional cycling association. The build went well: a Bolt prototype taken to production, payments integrated, launched on time, client delighted.

Eleven weeks later the association's treasurer emailed at 21:40 on a Sunday: the site was down and nobody at the bureau was reachable. The developer who had built it was on holiday. Nobody else knew how to deploy, the hosting account was in that developer's personal name, the database credentials existed only in his password manager, and there was no runbook.

The site came back on Monday afternoon. The association moved its maintenance contract to another supplier the following month, and the reason they gave was not the outage — it was that a five-hour problem had become a seventeen-hour one for reasons that had nothing to do with the software.

Bureau Nordkaap now produces handover artefacts during every engagement and runs a demonstration call at the end. Their production partner delivers the same pack on white-label work, which the bureau passes on under its own branding.

**Result:** across eleven subsequent projects, three have had incidents outside working hours. All three were resolved by someone other than the original developer, twice by the client themselves following the runbook.

> *"We hadn't done anything wrong technically. We'd just made ourselves the only route to a working website, and the client noticed before we did."*
> — **Joke Hoekstra, Director, Bureau Nordkaap (Leeuwarden)**

**Cost & Timeline:** €1,400 (handover pack, accounts migration, runbook and demonstration call, retrofitted for two existing clients) — completed in 3 business days.

## Frequently Asked Questions

### What is the single most important handover item?

Accounts in your own name, from the beginning. Everything else can be reconstructed with effort; an account held by someone who has stopped replying is a negotiation with no technical solution.

### How do I verify a handover is real?

Test it yourself before final payment: deploy a trivial change, follow the runbook to restore a backup into a scratch environment, and rotate one credential using the inventory. Three exercises, an hour, and any gap appears while you still have leverage.

### Should a handover include a list of things that are wrong?

Yes. A known-issues list is a sign of a thorough engagement, not a failed one. Its absence usually means the same problems will be rediscovered later by someone billing you to find them.

### Will production work stop me editing my app in Lovable or Cursor?

It should not, and the handover should say so explicitly. Ask for confirmation that the codebase remains conventional and AI-readable, and verify it by making one small change yourself in your original tool.

### As an agency, when should handover artefacts be written?

During the engagement, at the moment each decision is made or each pipeline is built. Assembling them at the end takes three times longer and produces a thinner document, usually under deadline pressure.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the single most important handover item?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Accounts in your own name from the beginning. Everything else can be reconstructed with effort, but an account held by someone unreachable is a negotiation rather than a technical problem."
      }
    },
    {
      "@type": "Question",
      "name": "How do I verify a handover is real?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Before final payment, deploy a trivial change yourself, follow the runbook to restore a backup into a scratch environment and rotate one credential using the inventory."
      }
    },
    {
      "@type": "Question",
      "name": "Should a handover include a list of things that are wrong?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. A known-issues list signals a thorough engagement; its absence usually means the same problems will be rediscovered later at your expense."
      }
    },
    {
      "@type": "Question",
      "name": "Will production work stop me editing my app in Lovable or Cursor?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It should not, and the handover should state so. Ask for confirmation that the codebase stays conventional and AI-readable, then verify with one small change yourself."
      }
    },
    {
      "@type": "Question",
      "name": "As an agency, when should handover artefacts be written?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "During the engagement, as decisions are made and pipelines built. Assembling them at the end takes longer and produces a thinner result."
      }
    }
  ]
}
</script>
