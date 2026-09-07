---
Title: "'I Don't Even Know What to Ask For' — Scoping Without the Vocabulary"
Keywords: how to scope a development project, dont know technical terms, describing your app to a developer, non-technical founder scoping, discovery call preparation, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# 'I Don't Even Know What to Ask For' — Scoping Without the Vocabulary

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "'I Don't Even Know What to Ask For' — Scoping Without the Vocabulary",
  "description": "A practical guide for non-technical founders who feel unable to write a scope or ask the right questions because they lack the vocabulary, walking through how to translate what you actually know about your product into something an engineer can quote against.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-02-18",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/i-dont-even-know-what-to-ask-for" }
}
</script>

"So, what do you need?"

"I don't know. Just... make it work?"

That exchange, or a slightly more polite version of it, is where a lot of founder-developer conversations actually start, and it's the moment a lot of founders quietly panic — not because the question is unfair, but because they genuinely don't have the words for the answer. You know your product. You built it, or prompted an AI tool to build it, screen by screen, over months. What you don't have is the vocabulary to translate "make it work" into the specific, checkable list an engineer needs to quote you a fixed price. That gap is not a knowledge deficit about your own product. It's a translation problem, and translation problems have a specific, learnable fix.

## Why "I Don't Know What to Ask For" Is the Wrong Frame

The frame itself is doing damage before the conversation even starts, because it implies the burden is on you to arrive with technical fluency you don't have and shouldn't need. Nobody expects a patient describing chest pain to arrive with a cardiology vocabulary — they're expected to describe symptoms, in their own words, and the diagnosis is the doctor's job to construct from that description. The equivalent expectation applies here: you're not supposed to arrive already knowing that you need "server-side row-level security" or "idempotent webhook handling." You're supposed to arrive able to describe what your product does, who uses it, and what's gone wrong or feels uncertain — and a good engineer's actual job, the first job, before any code gets touched, is translating that description into the technical list themselves.

If a prospective partner responds to "I don't know what to ask for" with anything other than a structured set of questions designed to draw that description out of you, that's a signal about them, not about you — a mature intake process exists precisely because most founders arrive exactly where you are.

## What You Actually Already Know (Even If It Doesn't Feel Technical)

Before worrying about vocabulary, take stock of what you can describe without any technical language at all, because it turns out to be almost everything an engineer needs as a starting point.

You know who uses your product and what they can do — a customer signs up, browses something, buys something, messages someone, uploads a file. You know what kind of information the product collects — names, emails, payment details, health information, messages, photos, addresses. You know what happens when something goes wrong that you've personally witnessed — a page that doesn't load, a payment that seemed to go through but didn't show up anywhere, an error message you didn't understand. You know what you're afraid of, even vaguely — "what if someone sees another customer's information," "what if the payment thing breaks," "what if it just goes down and I don't know how to fix it."

None of that requires a single technical term, and all of it is exactly the raw material a scope document gets built from. The translation from "customers upload photos and I'm worried about who can see them" to "we need to verify file storage access controls are scoped per user" is the engineer's job, not yours — your job is only the first half of that sentence.

It helps to notice, too, that you already perform a version of this translation constantly without thinking of it as technical work. Every time you prompted Lovable or Bolt to "add a way for customers to leave a review" or "make sure people can't edit someone else's booking," you were describing a requirement in plain language and letting the tool figure out the implementation. A discovery call with an engineer works the same way, just with a person doing the translating instead of a model, and with the added benefit that a person can ask you a clarifying question back — something the AI tool, prompted once and left to guess, generally couldn't.

## A Walkthrough: Turning a Vague Worry Into a Checkable Requirement

Here's how that translation actually happens, worked through concretely, because seeing it done once makes the process far less mysterious the next time.

Vague worry: "I'm scared someone could see another user's stuff." Translated question from the engineer: "when a user is logged in, can you show me — right now, in the actual product — where they'd see a list of their own items, bookings, or messages?" Your answer, in plain language, describing what you see on screen. Follow-up: "does that list ever include an ID, either visible or in the page's address bar, that looks like it could be changed to see someone else's version?" You might not know the answer, and that's fine — the engineer checks it directly against the code, using your description of the screen as the starting point for where to look.

Vague worry: "I don't know if payments actually work properly." Translated question: "walk me through exactly what happens, step by step, when a customer's card is declined — what do they see, what do you see, does anything change in your dashboard?" Again, your description in plain language is the input; the technical diagnosis of whether webhook handling is idempotent or whether failed payments are logged correctly is built from that description, not expected from you upfront.

This is the actual shape of a competent discovery call: specific, scenario-based questions from the engineer, plain-language answers from you, with the technical translation happening entirely on their side of the table.

## Preparing Without Learning to Code

There's a middle ground between "learn enough technical vocabulary to scope this myself" and "show up with nothing" that takes an evening, not a course. Walk through your own product as if you were a new user, and separately as if you were a second user who shouldn't see the first user's information, writing down anything that surprises you either way. Make a list of every third-party service your product connects to — payment processor, email sender, map or file storage, anything with a login you set up during the build — because this list alone answers several technical questions before they're even asked. Write down, in a sentence each, the worst thing you can imagine going wrong for a customer, a payment, and your own access to the system. And gather your logins: which email owns your hosting account, your database, your domain — this is unglamorous but saves real time in the first call.

None of this requires understanding what any of these services technically do. It requires knowing that they exist and that you have access to them, which is an inventory task, not a technical one.

## The Questions Worth Asking Back, Even Without the Vocabulary

Not knowing what to ask for doesn't mean staying silent during the call — it means asking different questions than a technical founder would, and they're just as valuable. Ask "can you explain what you just found in a way I'd understand if I had to repeat it to my co-founder?" Ask "if I only fix one thing on this list, which one, and why that one specifically?" Ask "how will I know, myself, without asking you, whether this is actually fixed?" These questions don't require any technical fluency, and they do something important: they force a translation back into plain language, which tells you whether the person you're talking to can actually explain their own findings clearly, or only in jargon that keeps you dependent on them to interpret it.

That last point matters more than it might seem. A partner who can't or won't explain a finding in plain language is either not confident enough in their own diagnosis to simplify it, or is using complexity as a way to seem more necessary than they are. Either read is worth taking seriously.

It's also fine, and often useful, to say the vocabulary gap out loud rather than trying to disguise it. "I don't know if that's the right word for it, but here's what I mean" is a more efficient sentence than reaching for a half-remembered technical term you picked up from a blog post and hoping it lands correctly. Engineers who work with non-technical founders regularly are used to parsing approximate descriptions and asking a clarifying question rather than taking an imprecise term at face value — the imprecision costs you nothing as long as you're specific about the underlying scenario, even if you're vague about its name.

## What a Good Discovery Call Actually Produces

The output of a well-run intake conversation, starting from "I don't know what to ask for," should be a written document you can read and understand without a glossary — not because it's been dumbed down, but because a good translation renders technical necessity in terms of what it accomplishes for you and your customers, not in the vocabulary of how it's implemented. "Customer data stays private between accounts" is a complete, checkable requirement in plain English; the row-level security policy that accomplishes it is an implementation detail you don't need to track, only to know exists.

LaunchStudio's own discovery process is built around exactly this principle, because the overwhelming majority of the founders coming through it arrive in precisely your position — a working prototype, no technical vocabulary, and a real product they understand better than anyone despite not being able to name what's underneath it. Backed by Manifera's engineers translating founder descriptions into fixed-scope technical plans for over a decade, the process exists specifically so "I don't know what to ask for" is the correct, expected starting sentence, not a disadvantage to overcome before the conversation can begin.

If the vocabulary gap has been keeping you from starting the conversation at all, that's solvable in one call, not one course. [Describe your product exactly as you'd describe it to a friend](https://launchstudio.eu/en/#contact), worries and all, and let the technical translation happen on the other side of the table, where it belongs.

## Real example

### A Founder Who Brought a List of Worries Instead of a Spec

Anneke Voss ran a small booking platform for freelance makeup artists, built in Lovable, and had put off reaching out for months specifically because, in her words, "I wouldn't even know how to describe what I need." When a mutual contact finally pushed her to have a call anyway, she came prepared not with technical requirements but with a plain list: three things she was scared of, one thing that had happened once that she didn't understand, and a list of every login she could find associated with the product.

Her three fears were: another artist seeing a client's booking details, a payment "disappearing" the way one had during testing, and not knowing who to call if the site went down. The one thing she didn't understand was a message she'd once seen in her Supabase dashboard that she'd screenshotted but never investigated. That screenshot, translated by the engineer on the call, turned out to describe a failed database migration that had left one table without the ownership field the rest of the schema used — precisely the mechanism behind her first fear.

**Result:** the scoping call produced a written plan addressing all three fears specifically, the missing migration was completed as the first item, and the platform launched two weeks later with Anneke able to explain, in her own words, exactly what had been fixed and why it mattered.

> *"I thought I needed to learn to talk like a developer before I could even start the conversation. It turned out I just needed to talk like myself, and let him do the translating."*
> — **Anneke Voss, Founder, a booking platform for makeup artists (The Hague)**

**Cost & Timeline:** Launch Ready package, database migration completion and access control — live in 10 business days.

## Frequently Asked Questions

### Do I need to learn any technical terms before my first call with a developer?
No. A competent intake process is designed to work entirely from your plain-language description of the product, its users, and your concerns — technical vocabulary is the engineer's job to supply, not yours to arrive with.

### What if I describe something wrong or use the wrong word for a feature?
That's expected and not a problem — a good engineer asks follow-up questions specifically to resolve exactly this kind of ambiguity, often by asking you to show the actual screen rather than describe it, which sidesteps vocabulary entirely.

### How do I know if the scope document I get back is actually correct?
Read it and ask yourself whether you understand every line without needing it explained further. If a line only makes sense with jargon you don't follow, ask for it to be rewritten in plain language — a good scope document should be fully readable by you, not just accurate to a technical reviewer.

### Is it a bad sign if I have almost nothing written down about my own product?
Not by itself — plenty of founders arrive with only what's in their head, built iteratively through prompting an AI tool rather than through upfront planning. The inventory suggested in this article takes one evening and closes most of that gap before the first call.

### Should I be worried that not knowing the vocabulary makes me an easier target to overcharge?
It's a fair concern, which is exactly why a fixed, written scope document matters — it converts the engagement from "trust their expertise on the price" to "check this specific checkable list against what's delivered," regardless of who understands the underlying vocabulary better.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Do I need to learn any technical terms before my first call with a developer?", "acceptedAnswer": { "@type": "Answer", "text": "No. A competent intake process is designed to work entirely from your plain-language description of the product, its users, and your concerns — technical vocabulary is the engineer's job to supply, not yours to arrive with." } },
    { "@type": "Question", "name": "What if I describe something wrong or use the wrong word for a feature?", "acceptedAnswer": { "@type": "Answer", "text": "That's expected and not a problem. A good engineer asks follow-up questions to resolve exactly this kind of ambiguity, often by asking you to show the actual screen rather than describe it, which sidesteps vocabulary entirely." } },
    { "@type": "Question", "name": "How do I know if the scope document I get back is actually correct?", "acceptedAnswer": { "@type": "Answer", "text": "Read it and ask whether you understand every line without needing it explained further. If a line only makes sense with jargon you don't follow, ask for it to be rewritten in plain language." } },
    { "@type": "Question", "name": "Is it a bad sign if I have almost nothing written down about my own product?", "acceptedAnswer": { "@type": "Answer", "text": "Not by itself. Plenty of founders arrive with only what's in their head, built iteratively through prompting an AI tool rather than upfront planning. A short inventory exercise closes most of that gap before the first call." } },
    { "@type": "Question", "name": "Should I be worried that not knowing the vocabulary makes me an easier target to overcharge?", "acceptedAnswer": { "@type": "Answer", "text": "It's a fair concern, which is exactly why a fixed, written scope document matters — it converts the engagement into a checkable list against what's delivered, regardless of who understands the underlying vocabulary better." } }
  ]
}
</script>
