---
Title: "Testing Your Own Product Before Launch: A Non-Technical Founder's Script"
Keywords: how to test your app before launch, founder testing checklist, Stripe test cards, password reset testing, user data isolation check, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Testing Your Own Product Before Launch: A Non-Technical Founder's Script

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Testing Your Own Product Before Launch: A Non-Technical Founder's Script",
  "description": "A non-technical founder can run a genuinely useful pre-launch test pass in about ninety minutes without writing a line of code. This is the exact script: signup, payment, decline, refund, password reset, and the wrong-user data check that matters most.",
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
  "datePublished": "2027-01-16",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/testing-your-own-product-before-launch-a-founders-script"
  }
}
</script>

There is a comfortable belief among non-technical founders that testing is the developer's job, and that a founder poking at their own product is at best redundant and at worst annoying. It sounds like respect for expertise. It is actually a misunderstanding of what testing is for.

Your engineer tests whether the code does what they built it to do. You test whether the product does what a real person needs it to do — and those diverge constantly, because the engineer has never been your customer and never will be. The founder pass finds a different class of bug: the confirmation email that arrives in Dutch when the interface is in English, the cancellation flow that works but leaves the user staring at a blank screen, the second account that can see the first account's data through a page nobody thought to check. None of that shows up in an engineer's tests, and all of it shows up in yours.

What follows takes about ninety minutes, requires no technical knowledge, and should be run on staging before launch and again on production immediately after. Do it once and you will never again feel like a passenger on your own launch.

## Before You Start: The Ten-Minute Setup

Get five things in place first, because improvising them mid-test is how a pass gets abandoned halfway.

**Two separate email addresses you actually control.** If you use Gmail, plus-addressing gives you infinite ones: `you+testA@gmail.com` and `you+testB@gmail.com` both land in your inbox but count as distinct addresses to your product. You need two because half of what you are testing is whether users are properly separated from each other.

**Two browser windows that don't know each other.** One normal window for Account A, one private/incognito window for Account B. Sessions do not leak between them, so you can be two different people simultaneously. This one detail is what makes the wrong-user test possible without a second laptop.

**Your phone, on mobile data rather than home Wi-Fi.** More than half of your first visitors will arrive on a phone, and mobile data catches a category of problem — assets that only load on your network, slow connections, autofill behaving differently — that a desktop pass never sees.

**Test card numbers.** In Stripe test mode, `4242 4242 4242 4242` with any future expiry and any CVC succeeds; `4000 0000 0000 0002` is always declined; `4000 0025 0000 3155` forces a 3D Secure authentication step, which European cards will regularly trigger under SCA rules. Mollie has an equivalent test mode where you select the outcome directly. Ask your engineer to confirm you are pointed at test mode before you start, so nothing you do here touches real money.

**A single note document with a timestamp column.** Every finding gets a time. When your engineer goes looking in the logs, "16:42, clicked Pay, spinner never stopped" is ten times more useful than "payment was broken yesterday."

## Test One: Signup, Including the Three Ways It Should Fail

Sign up as Account A, exactly as a stranger would — do not use a saved password, do not skip the empty fields, do not take the path you know works.

Then deliberately break it, because the happy path is the one thing everyone has already tested. Sign up with the *same* email address twice: you should get a clear message, not a crash and not a silent second account. Sign up with a nonsense email like `test@test` and confirm it is refused before submission rather than after. Sign up with a two-character password and check whether anything stops you — plenty of AI-generated prototypes enforce password rules in the interface and nowhere else, which means they are not enforced at all.

Then check the confirmation email. Did it arrive, and how quickly? Anything over two minutes on a quiet system is worth flagging. Is it in the inbox or in spam — check spam specifically, because a launch where every confirmation lands in spam is a launch where nobody activates. Does the sender address look like your product rather than `noreply@sendgrid.net`? Does the link in it actually work, and does it still work if you open it on your phone rather than the machine that requested it? And what happens if you click it twice, or click it a week from now — an expired-link message is fine, a stack trace is not.

## Test Two: Payment, and the Card That Should Be Declined

Pay as Account A with the success card. Watch what happens on screen, and watch what happens after: does the page confirm clearly, does the account visibly become a paying account, does the receipt email arrive, and does the payment appear in your Stripe or Mollie dashboard with the right amount and currency?

Then the declined card, which is the test almost nobody runs and which will affect real customers within your first week — decline rates on legitimate European card payments are meaningfully non-zero. Use `4000 0000 0000 0002` and observe: does the user see a human-readable message explaining the card was declined and inviting them to try another, or a blank screen, an infinite spinner, or a raw error string? Critically, is the account left in a sensible state — not half-upgraded, not charged, not locked out of retrying?

Then the 3D Secure card, which forces the extra verification step European customers see constantly. Complete it once, then run it again and *abandon* it — close the verification window. Your product should treat that as no payment rather than as a completed one.

Finally, the double-click test. On the payment button, click twice quickly. You should end up with one charge. If you end up with two, you have found something that will generate refund requests and support email from day one.

## Test Three: Refund, Cancellation, and the Path Back Out

Founders rehearse the path into paying and almost never rehearse the path out, which is backwards — the way out is where your reputation lives and where the compliance obligations sit.

Cancel Account A's subscription from inside the product. Three questions: does the interface confirm it clearly, does the user keep access until the end of the period they paid for, and does the cancellation actually register in Stripe or Mollie rather than only in your own database? A cancellation that updates your app but not the payment provider means you will keep charging someone who believes they cancelled — the single fastest way to earn a chargeback.

Then issue a refund from the payment dashboard and watch what your product does. Does the account lose paid access? Is there a notification? Does anything break? Refunds are usually handled by a webhook, and webhooks are exactly where AI-generated code is thinnest, so this test finds real problems disproportionately often.

Then delete the account, if your product offers it. Under GDPR you need a genuine path to erasure, and this test tells you whether "delete" removes the data or just hides the login. Ask your engineer directly what happens to the underlying records and what the retention position is — you need to be able to answer that question when a customer asks it, and eventually one will.

## Test Four: Password Reset, on a Device You Are Not Logged Into

Password reset is the most-used support path in any product and the one most likely to be half-built, because it works fine in the demo where you are already logged in.

Log out completely. Request a reset for Account A. Time how long the email takes. Open the link on your phone — a different device, not logged in — and set a new password. Then confirm three things: the new password works, the old password no longer works, and any existing sessions elsewhere behave as you would expect.

Then test the misuse cases. Request a reset for an address that does not exist in your system: the response should be identical to the real one ("if that address exists, we've sent a link"), because a different message tells an attacker which of your customers' email addresses are registered. Click the same reset link twice — the second attempt should be refused. And leave a reset link for an hour before using it, then check whether expiry is enforced at all; a link that works indefinitely is a permanent key to that account sitting in an inbox.

## Test Five: The Wrong-User Check, Which Is the Whole Ballgame

This is four minutes of work and it is the most important thing on this list. It is also the check most likely to fail on an AI-generated product, because these tools produce interfaces that hide the wrong data rather than backends that refuse to serve it.

In your normal window, be Account A and create something real — an order, a client, a booking, a project, whatever your product's core object is. Look at the address bar while you are on that item's page. There is almost always an identifier in it: a number, or a long string like `/orders/3f8a...`. Copy the whole URL.

Now go to your incognito window, log in as Account B, and paste Account A's URL. You should see a "not found" or "not authorised" message. If you see Account A's data, stop testing and send that URL to your engineer immediately, because that is a live data breach in waiting and it is not a small fix.

Then repeat it in the two places people forget: any print, export, or PDF view (these frequently use a separate code path with none of the same checks), and any shared or public link feature. And try one more variation — while logged in as B, edit the number in the address bar to a nearby value, `/orders/104` instead of `/orders/105`. Walking the numbers like this is precisely what a curious person does, and it takes no skill whatsoever.

## Test Six: The Ugly-Reality Pass

Ten minutes on the things real users do that demos never show. Create an account and immediately look at a screen with nothing in it — the empty dashboard, the empty list. Does it explain what to do next, or is it a blank rectangle? First impressions are made here.

Type a genuinely long name, a name with an apostrophe or an umlaut, and an emoji into your main text fields. Dutch and Belgian customers will bring `Van der Meer-Ó Súilleabháin` sooner than you think, and text handling bugs are cheap to fix before launch and embarrassing after.

Use the browser back button after every important action — after paying, after submitting a form, after logging out. Back-button behaviour after a payment is a classic source of duplicate submissions. Then hit refresh in the middle of a multi-step flow and see whether it survives. Finally, log out and try to reach a logged-in page directly by URL; you should land on the login screen, and after logging in you should ideally arrive where you were trying to go.

## Writing It Up So It Gets Fixed

How you report determines how fast things get fixed. For each finding, four lines: what you did, what you expected, what happened, and the timestamp. Add a screenshot or a short screen recording. Do not diagnose the cause — "the button is broken because the database isn't connected" sends your engineer down your guess instead of their own investigation, and founders' guesses about causes are wrong more often than not.

Then sort your list into three buckets and send it as three lists, not one: **must fix before launch** (anything from Test Five, anything involving money, anything that loses data), **fix in the support window** (annoying but survivable), and **after launch** (polish, wording, preferences). Sorting it yourself is the single most valuable thing you can do with the list, because it tells your engineer what you consider a launch blocker rather than making them guess — and it is a judgement only you can make. Manifera, the software company LaunchStudio grew out of, has spent 11+ years shipping software for clients who test exactly this way, and a well-triaged founder bug list is consistently the most useful document produced in the final week of any engagement.

Ninety minutes, six tests, no technical knowledge required — and a materially better launch, because you will have exercised the paths your customers use rather than the path the demo takes. Run it on staging this week, and run it again on production within an hour of going live. If you want a second pair of eyes on what you find, [LaunchStudio](https://launchstudio.eu/en/) reads AI-generated code all day, backed by [Manifera's engineering team](https://www.manifera.com/about-us/) in Amsterdam and Ho Chi Minh City.

Run the script, then send us your list of what broke — we'll tell you which items are genuinely launch-blocking and which can wait, at no cost.

## Real example

### A Founder in Action: The PDF That Leaked

Nadia el Amrani, a former lettings agent in Rotterdam, built Huurhelder — a rent tracking and maintenance-request tool for small private landlords — in Lovable. Before launch she ran a founder test pass on staging with two accounts, expecting it to be a formality since the security work had already been signed off.

Tests one through four passed. Test five passed too, on every normal screen: logging in as landlord B and pasting landlord A's tenant URL returned a clean "not authorised" page. Then she tried it on the monthly statement PDF — a feature she used constantly and which generated a downloadable file at its own address. Landlord B downloaded landlord A's statement, with tenant names, addresses, and payment histories intact.

**Result:** The PDF generator ran server-side through an endpoint that had never been covered by the new access rules, because it predated them and lived in a different part of the codebase. It was fixed in half a day, and the same review found two export endpoints with the same weakness. Huurhelder launched four days later with all three closed.

> *"I nearly skipped the test because a professional had already signed the work off. He'd checked the app. Nobody had checked the PDF, because nobody except me actually downloads those every month."*
> — **Nadia el Amrani, Founder, Huurhelder (Rotterdam)**

**Cost & Timeline:** €2,650 (Launch Ready package, access control, Mollie payments, and export endpoint hardening) — live in 11 business days.

---

## Frequently Asked Questions

### Won't my engineering team be offended if I test their work myself?

A good team actively wants it, because you find a different class of problem than they do — you know what your product is supposed to feel like to a real customer, and they know what the code does. Offer your findings as observations with timestamps rather than as verdicts and it reads as collaboration, which is what it is.

### How do I make sure my testing doesn't charge real money or email real customers?

Ask your engineer to confirm you are on staging pointed at the payment provider's test mode, and that staging uses invented or anonymised data rather than a copy of your real customer list. Both should already be true; asking takes thirty seconds and removes the anxiety that stops most founders from testing properly.

### What if I find something and I'm not sure whether it's actually a bug?

Report it anyway, described factually. Ambiguous findings are cheap for an engineer to evaluate and expensive for a customer to encounter, and "this felt confusing but might be intended" is a perfectly professional thing to write. Over-reporting is a much smaller problem than under-reporting.

### Do I need to run the whole script again after launch?

Run the money and access parts again on production within an hour of going live — signup, one real payment with a real card, and the wrong-user check — because configuration differs between staging and production and that is exactly where launch-day surprises come from. The full pass can wait until your next significant change.

### My product doesn't take payments yet. Which tests still apply?

Everything except tests two and three. Signup, password reset, the wrong-user check, and the ugly-reality pass are the ones that matter most regardless of whether money is involved, and the wrong-user check in particular is where free products get into just as much trouble as paid ones.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Won't my engineering team be offended if I test their work myself?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A good team wants it, because you find a different class of problem: you know how the product should feel to a real customer, they know what the code does. Report observations with timestamps rather than verdicts and it reads as collaboration."
      }
    },
    {
      "@type": "Question",
      "name": "How do I make sure my testing doesn't charge real money or email real customers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ask your engineer to confirm you are on staging, pointed at the payment provider's test mode, with invented or anonymised data rather than a copy of your real customer list. Both should already be true, and asking takes thirty seconds."
      }
    },
    {
      "@type": "Question",
      "name": "What if I find something and I'm not sure whether it's actually a bug?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Report it factually anyway. Ambiguous findings are cheap for an engineer to evaluate and expensive for a customer to hit, and over-reporting is a far smaller problem than under-reporting."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need to run the whole script again after launch?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Run the money and access tests again on production within an hour of going live: signup, one real payment, and the wrong-user check. Configuration differs between staging and production, which is where launch-day surprises originate."
      }
    },
    {
      "@type": "Question",
      "name": "My product doesn't take payments yet. Which tests still apply?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "All of them except the payment and refund tests. Signup, password reset, the wrong-user data check, and the ugly-reality pass matter regardless of whether money is involved, and free products get into just as much trouble on data access as paid ones."
      }
    }
  ]
}
</script>
