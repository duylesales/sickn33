---
Title: "AI and Security: The Gap Every Founder Discovers Too Late"
Keywords: ai and security, security ai, ai secure, ai security vulnerabilities, ai data security
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# AI and Security: The Gap Every Founder Discovers Too Late

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI and Security: The Gap Every Founder Discovers Too Late",
  "description": "Everyone talks about AI and security like the tools handle it automatically. A technical look at exactly what AI coding tools leave unvalidated, and why input validation is the gap founders find last.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-08-13",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-and-security-the-gap-every-founder-discovers-too-late" }
}
</script>

Everyone says AI can build your entire app for you, security included, because it "follows best practices" out of the box. Nobody mentions that "best practices" in this context usually means things like password hashing and HTTPS — the visible, well-documented half of security — while leaving the invisible half almost entirely untouched. That invisible half is input validation, and it's where AI and security part ways most often, quietly, in a way that doesn't show up until someone deliberately goes looking for it or, worse, exploits it.

This isn't a criticism of the tools. Lovable, Bolt, Cursor, and v0 are trained to produce code that satisfies a functional description, and "validate every field on the server before trusting it" is rarely part of that description unless you explicitly ask for it. The result is a category of vulnerability that's boring to explain, easy to miss, and genuinely dangerous: forms and APIs that trust the data arriving instead of checking it. It's also, frustratingly, one of the least visually dramatic categories of security gap — there's no scary error message, no obvious crash, nothing that would prompt a founder to go looking for a problem in the first place.

## What Input Validation Actually Means, Technically

When a user submits a form — a booking date, a quantity, a price, a discount code — that data travels from their browser to your server as a plain request your server has to decide whether to trust. Client-side validation, the kind built into most AI-generated frontends, checks that data before it leaves the browser: is this field empty, is this a valid date format, does this number look reasonable. That's useful for user experience. It is not security, because anyone can bypass client-side validation entirely by sending a request directly to your API, skipping the browser interface altogether. Server-side validation — checking the same rules again, on the server, on every request, regardless of where it came from — is the part that actually protects you, and it's the part AI tools most often skip unless explicitly instructed.

## Where This Specifically Breaks: A Technical Walkthrough

Take a booking or e-commerce style app, the kind AI tools generate constantly. A typical unvalidated flow looks like this: the frontend shows available dates and calculates a price based on selections. The request sent to the server includes the date, the service selected, and — because it was simpler to build this way — the price itself, calculated client-side and just passed along. The server, trusting the frontend did its job, saves that price directly.

The technical problem: nothing stops a request from being sent with a different price than what the frontend displayed. Opening browser developer tools, intercepting the request, and changing a price field from €80 to €8 before it reaches the server takes under a minute for anyone who knows to try it, and the server has no way of knowing the number didn't come from its own price calculation, because it never recalculated it. The same pattern applies to dates (booking outside allowed hours), quantities (ordering negative or absurdly large amounts), and discount codes (applying an expired or nonexistent one that a client-side check never actually confirmed against the database).

The fix, technically, is straightforward but has to be deliberate: never trust a value that originated in the browser for anything that affects money, access, or data integrity. Recalculate the price server-side from the selected service and its known rate. Re-validate the date against actual availability, server-side, at the moment of booking. Re-check the discount code against the database, not against a value the frontend already claims is valid. None of this is exotic engineering — it's a specific, checkable discipline that a prompt has to explicitly request, because a functional description of "let users book a service and pay" doesn't imply it on its own.

## A Second Technical Example: The Quantity Field Nobody Bounds

Price manipulation is the clearest example because it involves money directly, but the same unvalidated pattern shows up in less obvious places too. Take a quantity field on an order form — how many units of something a customer wants. A typical AI-generated flow checks, client-side, that the field isn't empty and is a positive number, which covers the normal case of someone ordering a reasonable amount. What it usually doesn't check, server-side, is whether the quantity is bounded at all. Submit a request directly with a quantity of negative one, and depending on how the total is calculated, the app might compute a negative charge — effectively crediting the account instead of charging it. Submit a quantity of ten million, and depending on how inventory is decremented, the same request might drive a stock count deeply negative, corrupting every subsequent calculation that depends on it.

Neither of these requires any special tooling to attempt — both are a matter of sending a slightly different number in a request that would otherwise look completely ordinary. And neither gets caught by client-side validation, because client-side validation, by definition, only runs when someone is going through the actual interface rather than sending a request directly. This is exactly why "input validation" as a category is worth treating as its own checklist item, distinct from authorization and distinct from payment integration — it's the discipline of never trusting a number, string, or date just because it arrived in the expected shape.

Importantly, this isn't a payments-only concern, even though the price example is the easiest to picture. Any app with forms or APIs accepting values that influence an outcome carries the same exposure — a scheduling tool with no payment feature at all can still have unbounded date fields, unchecked quantity limits on a waitlist, or an access-level parameter nobody thought to re-verify server-side. The specific values differ by product; the underlying discipline of re-checking everything server-side doesn't.

## AI and Security in Practice: Where to Look in Your Own App

If you want a concrete way to spot this in your own AI-built product without reading code, look at any form involving money, dates, or quantities, and ask: does the value that determines the outcome (the price charged, the slot reserved, the discount applied) get recalculated on the server, or is it simply accepted from what the browser sent? If you genuinely don't know the answer, that's the honest state most AI-built prototypes are in before a dedicated review — not because the founder did anything wrong, but because this specific question was never part of the original prompt.

Manifera's engineers — the same team that has delivered production-grade software for eleven-plus years, out of a development center on Pho Quang Street in Ho Chi Minh City among other locations — treat this exact validation gap as a standard item on every AI-generated codebase review, precisely because it shows up so consistently across different tools and different products. If you want your specific booking, checkout, or form-heavy flow checked for this, [talk to an engineer who reviews AI-generated code regularly](https://launchstudio.eu/en/#contact) rather than guessing whether your app has the gap.

## Real example

### An AI-Native Founder in Action: The Price That Wasn't Really the Price

Esmée Kuiper, a founder based in Haarlem, built "Boekingsbuddy" — a booking tool for small hair salons — using Lovable. Clients could pick a stylist, a service, and a time slot, and the app calculated the price based on the service selected before sending them to payment. It worked exactly as demoed, every time Esmée tried it herself.

What Esmée hadn't checked, because there was no obvious reason to, was what the actual request sent to the server contained. The price shown to the customer was calculated in the browser and passed along as a plain field in the booking request — the server accepted whatever number arrived rather than recalculating it from the selected service. The booking date had a similar gap: the server accepted any date sent, including dates outside the salon's actual operating hours, because availability was only checked visually on the frontend calendar, not re-verified server-side.

Esmée found LaunchStudio through a comparison thread about launching Lovable apps safely. Engineers rebuilt the booking endpoint to recalculate price server-side from the salon's actual rate table, added server-side availability checks against real operating hours and existing bookings, and added logging so any mismatch between a submitted price and the recalculated one would be flagged automatically going forward. The same review also found that the number of add-on services a customer could select per booking had no upper bound enforced server-side — cosmetically limited to five on the frontend, but unlimited if the request was sent directly, which could have let someone book an absurd number of add-ons at the base calculated rate before the fix went in.

Esmée's reaction, once it was explained plainly, was less about the specific bug and more about how invisible it had been. Nothing about Boekingsbuddy looked unfinished. The calendar was polished, the confirmation emails were on brand, the whole thing photographed well for a launch announcement. The gap lived entirely underneath that surface, in a place a founder testing her own product from the front end would never naturally look.

> *"I had no idea the price customers saw was basically just a suggestion the server was trusting blindly. Once it was explained to me, it seemed obvious. Before that, I would never have known to ask."*
> — **Esmée Kuiper, Founder, Boekingsbuddy (Haarlem)**

**Cost & Timeline:** €1,250 (server-side price recalculation, availability validation, add-on quantity bounding, mismatch logging) — completed in 5 business days.

## Frequently Asked Questions

### What's the difference between client-side and server-side validation?

Client-side validation checks data in the browser before it's sent, mainly for user experience. Server-side validation checks the same data again on the server, on every request, and is the part that actually prevents manipulation since browser checks can be bypassed entirely.

### Why don't AI coding tools add server-side validation automatically?

Because a typical prompt describes the desired outcome, like "let users book a service," without specifying that every value affecting price or access must be re-verified server-side. That requirement has to be stated explicitly to be built.

### How can I check if my app has this specific gap without reading code?

Look at any form involving money, dates, or quantities and ask whether the value that determines the outcome would be recalculated on the server if you sent a manipulated request directly, bypassing the frontend entirely.

### Is this the same issue as the authorization gap other AI security articles mention?

It's related but distinct. Authorization is about who can access which data. Input validation is about whether the values submitted, regardless of who submits them, are actually verified before being trusted.

### Can this kind of fix be applied without changing my app's design?

Yes. Server-side validation and recalculation happen behind the scenes and don't require any visible change to the interface a founder already built and likes.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "What's the difference between client-side and server-side validation?", "acceptedAnswer": { "@type": "Answer", "text": "Client-side validation checks data in the browser for user experience. Server-side validation checks the same data again on the server and is what actually prevents manipulation." } },
    { "@type": "Question", "name": "Why don't AI coding tools add server-side validation automatically?", "acceptedAnswer": { "@type": "Answer", "text": "A typical prompt describes the desired outcome without specifying that values affecting price or access must be re-verified server-side, so it has to be explicitly requested." } },
    { "@type": "Question", "name": "How can I check if my app has this specific gap without reading code?", "acceptedAnswer": { "@type": "Answer", "text": "Look at any form involving money, dates, or quantities and ask whether the outcome would be recalculated server-side if the request were sent directly, bypassing the frontend." } },
    { "@type": "Question", "name": "Is this the same issue as the authorization gap other AI security articles mention?", "acceptedAnswer": { "@type": "Answer", "text": "It's related but distinct. Authorization is about who can access which data. Input validation is about whether submitted values are verified before being trusted." } },
    { "@type": "Question", "name": "Can this kind of fix be applied without changing my app's design?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. Server-side validation happens behind the scenes and doesn't require any visible change to the existing interface." } }
  ]
}
</script>
