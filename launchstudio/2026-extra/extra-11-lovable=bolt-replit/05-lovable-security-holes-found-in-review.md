---
Title: "Lovable Security: Five Holes We Find in AI-Built Apps"
Keywords: lovable security, ai app security, IDOR vulnerability prototype, file upload security, rate limiting AI app, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable Security: Five Holes We Find in AI-Built Apps

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Security: Five Holes We Find in AI-Built Apps",
  "description": "The recurring weaknesses in AI-built applications, explained without jargon: object reference flaws, missing server-side checks, unprotected uploads, absent rate limiting and leaky error messages — plus how to test each one yourself.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-07",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-security-holes-found-in-review" }
}
</script>

There is a particular moment in a security review that founders find hard to watch. An engineer logs into the app as a normal user, changes a single number in the address bar, and the screen fills with somebody else's data. It takes four seconds, requires no tools, and it is the most common finding in AI-built applications by a wide margin.

What follows is the five weaknesses that come up most often, in the order they tend to be found. None of them are exotic. All of them are invisible while you are building, because an app with these holes behaves perfectly for a user who is not looking for them.

## One: You Can Read Other People's Records by Changing a Number

Your app has addresses like `/invoice/1043` or `/booking/22`. The page loads the record matching that number. The question nobody asked during the build is: does anything check that this record belongs to the person asking?

In AI-generated applications, frequently not. The frontend only ever shows you links to your own records, so during testing you never try anything else. But the address bar is editable, and `/invoice/1042` is a perfectly valid request.

**Test it yourself in two minutes.** Log in as one user, note a record's address, then log in as a different user in a private window and open that same address. If you see the first user's data, you have found it. Do this for every kind of record your app stores — bookings, messages, documents, profiles. The fix belongs in the database access rules and the server-side checks, not in hiding the links.

## Two: The Checks Live in the Browser, Where Anyone Can Remove Them

A form validates that a discount code is real, that a quantity is positive, that a user is an administrator before showing the admin button. If all of that logic runs in the visitor's browser, it is advice rather than enforcement.

Anyone can open developer tools, alter the page, and submit whatever they want directly to your API. The browser is not a trusted environment — it is a program running on someone else's computer, under their control.

The practical consequence is not usually dramatic hacking. It is a user setting a quantity to `-1` and receiving a refund, or a curious customer discovering that the "admin" flag is a field they can send. Every rule that matters commercially or legally has to be enforced on the server, with the browser version kept only as a convenience for honest users.

## Three: Anyone Can Upload Anything, Anywhere

If your app accepts files — profile photos, CVs, invoices, damage photos — three questions decide whether that feature is a convenience or a liability: what types are accepted, how large can they be, and who can read them afterwards.

AI-built upload features typically answer "anything", "any size", and "anyone with the link". That combination means your storage bill is controlled by your least considerate visitor, that executable content can be hosted on your domain, and that a file uploaded by one customer can often be retrieved by another simply by guessing or sharing the address.

The fix is unglamorous: restrict file types on the server rather than in the browser, cap sizes, generate unpredictable file names rather than using the uploaded one, and put access rules on the storage bucket so that a file belongs to the account that uploaded it.

## Four: There Is Nothing Stopping Repetition

Nothing in a default AI-built app stops someone calling your login endpoint ten thousand times, submitting your contact form continuously, or requesting password resets for every email address they can think of.

The results range from irritating to expensive. Automated signups fill your database with fake accounts. Repeated password reset requests turn your transactional email provider into a spam source and get your sending domain reputation damaged. And if any endpoint calls a paid service — a mapping API, an AI model, an SMS provider — a loop running overnight becomes a bill.

Rate limiting is the answer, and it needs to sit at the server or the edge rather than in the interface. For most small products this is a modest amount of configuration, not a project.

## Five: Your Error Messages Are Telling Strangers Too Much

When something fails in a prototype, the app often shows exactly what went wrong: the database query, the table name, the internal path, sometimes a fragment of configuration. This is enormously helpful while building and it is a map for anyone probing your app.

There is a subtler version that catches out even careful builders. A login form that says "no account with that email" for one case and "incorrect password" for another has just confirmed which email addresses are registered — useful information for anyone with a list of addresses and bad intentions.

Production behaviour should be: a generic message for the user, a detailed record in your logs, and identical responses for cases that should not be distinguishable from outside.

## Why These Five, Specifically

They share a cause. Each of these holes is invisible unless someone deliberately behaves like an adversary, and AI coding tools have no model of an adversary at all. Lovable, Bolt, Cursor and Replit are built to make the thing you described work. They do that extremely well, which is why roughly 80% of the product arrives in days.

What they cannot do is ask the hostile questions: what if this person is not who they claim, what if they change this value, what if they run this a million times. That reasoning is the remaining 20% — and it is the part that decides whether your launch is a milestone or an incident.

## A Self-Review You Can Run This Week

- Open a record belonging to another account by editing the address. Repeat for each record type.
- Submit a form with values the interface would not allow — a negative number, an enormous quantity, a role field you invented.
- Upload a file that is not what your app expects, and check whether size and type are enforced.
- Click a password reset link twice, and check whether it still works after being used.
- Read the exact wording of your login failure messages.
- Log out, then try to open an address that requires being logged in.

Anything that succeeds where it should not is a finding. Write it down rather than fixing it immediately — the list as a whole usually reveals a pattern about where enforcement is missing, and fixing the pattern is faster than fixing six symptoms.

## Closing the Gaps Without Rebuilding the App

Every issue above is fixable without touching the interface you built. That is the entire premise of LaunchStudio: the frontend stays, and the enforcement layer goes underneath it — access rules per record, validation moved server-side, upload restrictions, rate limiting, and error handling that says nothing useful to a stranger. It is the work in the [Launch Ready package](https://launchstudio.eu/en/#packages), typically measured in days rather than months, and delivered by Manifera engineers who have spent eleven years securing production systems for clients including Vodafone, TNO and CFLW from Amsterdam and Ho Chi Minh City.

If any of the six self-review steps above produced an uncomfortable result, [send us your prototype link](https://launchstudio.eu/en/#contact) and you will get a specific assessment of what is exposed within one business day.

## The Sixth One: Sessions That Never Really End

This did not make the list of five because it is slightly less universal, and it belongs here because when it goes wrong the consequences are unusually hard to explain to a customer.

**Password reset links that work more than once.** A reset link is a temporary key to an account. If it does not expire after use, or does not expire at all, then an old email sitting in a forwarded thread or a shared inbox remains a working way into that account months later.

**Logging out that only logs out the screen.** In many generated apps, signing out clears the interface while the underlying session token remains valid. On a shared or public computer, that is the difference between a session ending and a session appearing to end.

**Sessions that survive a password change.** The main reason people change a password is that they believe someone else has it. If existing sessions are not invalidated at that moment, the person you were trying to remove stays logged in — which makes the security action the user took functionally decorative.

**Tokens with very long lifetimes.** Convenient during development, because nobody gets logged out while testing. In production, a long-lived token copied from a device is a long-lived problem.

The test takes ten minutes. Request a password reset and use the link twice. Log in on a second browser, change your password in the first, and see whether the second is still authenticated. Log out and try to reopen a page that requires being signed in using the browser's back button. Anything that still works is a finding, and all four are configuration rather than code in most stacks.

## Why These Appear Together

It is rare to find one of these in isolation, and the reason is instructive. Each hole comes from the same missing step: nobody ever asked what an unfriendly user would try.

A prototype is built by describing desired behaviour. Every instruction is about what should happen — a user books a slot, an assessor uploads a photo, an admin sees a dashboard. Nothing in that process generates the opposite question, which is what happens when someone does the thing you did not describe.

So the holes arrive as a set, and they close as a set too. Once someone works through an app asking the hostile questions systematically, the fixes tend to land in the same few places: the database access layer, the server-side validation layer, and the storage rules. That is why a review usually costs less than founders expect — the findings are numerous and the remediation is concentrated.

## Real example

### A Damage Reporting App Where Every Photo Was Public

Ilse Kramer built ScheldeScan in Lovable for a network of independent car-damage assessors around Dordrecht. Assessors photograph vehicle damage, the app stores the images with a claim reference, and insurers receive a report link.

The review found four of the five patterns above. Claim pages loaded by reference number with no ownership check, so any assessor could open any other assessor's claims. Photo uploads accepted any file type up to any size and stored them under predictable names in a publicly readable bucket, meaning the images — including vehicle registration plates and, in several cases, visible house numbers — were retrievable by anyone who guessed an address. The report link contained no expiry. And the login form distinguished between unknown email and wrong password.

Seven business days of work: ownership checks enforced at the database level for every claim record, uploads restricted by type and size with randomised names and per-account bucket policies, report links reissued as signed URLs with an expiry, rate limiting added on login and report generation, and login responses made uniform.

**Result:** ScheldeScan passed its first insurer's supplier security questionnaire five weeks later, which it had previously postponed twice because nobody could answer the question about access controls.

> *"We had been sending insurers links to photos of their customers' cars that anyone with a browser could have found. Nothing had gone wrong yet. That was luck, not design."*
> — **Ilse Kramer, Founder, ScheldeScan (Dordrecht)**

**Cost & Timeline:** €3,200 (Launch Ready Package: access control, upload hardening, rate limiting) — completed in 7 business days.

## Frequently Asked Questions

### If nothing has gone wrong yet, is my app actually at risk?

Absence of incident is not evidence of protection — most small apps are simply not interesting enough to attract attention yet. The risk changes the moment you have customers worth targeting, a competitor who is curious, or a user who edits a URL out of boredom.

### Can I fix these myself if I built the app with AI?

Some of them, yes — upload limits and error messages are approachable. The access control layer is harder, because the correct fix lives in database policies and server-side checks rather than in the interface, and a partial fix tends to feel finished while leaving the hole open.

### Will fixing security break my app's design?

No. Every issue described here is enforced behind the interface. Users notice nothing except that certain abuses stop working, which is the intended outcome.

### How is this different from adding a login screen?

A login screen establishes who someone is. These issues are about what an authenticated person is allowed to do. Most of the findings in AI-built apps are not about strangers getting in; they are about legitimate users reaching data that is not theirs.

### Does a security review slow down my launch?

It usually shortens the path, because the alternative is discovering these problems during a customer's supplier assessment or after an incident. A focused review and remediation typically takes days, which is faster than rebuilding trust with a customer who found the hole first.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "If nothing has gone wrong yet, is my app actually at risk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Absence of incident is not evidence of protection — most small apps are simply not yet interesting enough to attract attention. The risk changes once you have customers worth targeting, a curious competitor or a user who edits a URL."
      }
    },
    {
      "@type": "Question",
      "name": "Can I fix these myself if I built the app with AI?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Some, such as upload limits and error messages. The access control layer is harder because the correct fix lives in database policies and server-side checks, and a partial fix tends to feel finished while leaving the hole open."
      }
    },
    {
      "@type": "Question",
      "name": "Will fixing security break my app's design?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. These issues are enforced behind the interface. Users notice nothing except that certain abuses stop working, which is the intended outcome."
      }
    },
    {
      "@type": "Question",
      "name": "How is this different from adding a login screen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A login screen establishes identity. These issues concern what an authenticated person may do. Most findings in AI-built apps involve legitimate users reaching data that is not theirs."
      }
    },
    {
      "@type": "Question",
      "name": "Does a security review slow down my launch?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It usually shortens the path, because the alternative is discovering these problems during a customer's supplier assessment or after an incident. Review and remediation typically take days."
      }
    }
  ]
}
</script>
