---
Title: "It Works in the Demo: Why 'AI Works' Isn't the Same as Ready to Ship"
Keywords: ai works, ai coding, ai secure, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# It Works in the Demo: Why 'AI Works' Isn't the Same as Ready to Ship

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "It Works in the Demo: Why 'AI Works' Isn't the Same as Ready to Ship",
  "description": "A direct look at the gap between 'AI works' as a demo claim and 'ready to ship' as a production claim, with a specific breakdown of how unsanitized input becomes a real vulnerability.",
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
  "datePublished": "2026-07-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/it-works-in-the-demo-ai-works-isnt-ready-to-ship"
  }
}
</script>

You've finished your prototype. It works. Every button does what it's supposed to do, every screen loads, every workflow completes exactly as you designed it. So why does almost every experienced engineer respond to "it works" with a follow-up question rather than a congratulations? Because "works" is doing a lot of quiet, unexamined lifting in that sentence, and the specific thing it usually means — works for me, the way I use it — is a much narrower claim than founders tend to assume.

## Two Very Different Meanings of "Works"

"Works" can mean: this specific sequence of actions, performed by the person who built it, produces the expected result. Or it can mean: this application behaves safely and correctly under a very wide range of inputs, including ones nobody anticipated, from users who don't behave the way the founder imagined they would. AI coding tools are optimized almost entirely toward proving the first meaning, because that's the meaning a demo naturally tests — and the second meaning is the one that actually determines whether a product survives contact with real, unpredictable users.

## Where the Gap Between the Two Meanings Actually Lives

The gap tends to concentrate in exactly the places a founder's own testing never goes: free-text input fields, search boxes, file uploads, and anywhere a user supplies a value the application then uses to construct a database query or file path. A founder searching their own test data types reasonable search terms and gets reasonable results — because that's what "testing search" means to someone who isn't specifically trying to break it.

## Why Unsanitized Input Is the Textbook Version of This Problem

A search field that passes user input directly into a database query without properly sanitizing it can, in the worst case, allow a specifically crafted input to manipulate the query itself — extracting data it was never meant to return, or in more severe cases modifying or deleting records outright. This isn't a hypothetical: it's one of the oldest, most well-documented classes of vulnerability in web development, and AI-generated code that hasn't been specifically reviewed for it is exactly as exposed as hand-written code with the same oversight would be.

## Why "I Tested Search and It Worked Fine" Doesn't Rule This Out

Testing search with normal search terms — a product name, a customer's name, a reasonable keyword — never triggers this failure mode, because normal search terms are, by definition, not the specifically malformed input that exposes the underlying gap. The two tests look identical from the outside (you type something, you get results) but only one of them is actually probing whether the query construction underneath is safe.

## What a Real Fix Looks Like, Concretely

Closing this gap means replacing direct string-concatenation into queries with properly parameterized queries or an ORM layer that handles escaping automatically, and applying that pattern consistently across every input field that reaches the database, not just the ones a founder happens to remember. [LaunchStudio](https://launchstudio.eu/en/) audits exactly this pattern across an entire codebase as part of its standard review, backed by Manifera's 11+ years of production engineering experience across Node.js, Laravel, and .NET backends.

Manifera's engineers, working primarily out of the Ho Chi Minh City development center on Pho Quang Street with client coordination through the Amsterdam office at Herengracht 420, apply this same review pattern regardless of which specific backend framework a founder's AI tool happened to generate.

[Send us your prototype link — we'll give you free advice](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: The Search Box That Could See Everything

Tim, a former warehouse operations manager turned founder in The Hague, built RouteWise, an AI-assisted logistics tracking app built with Lovable, letting dispatch teams search shipment records by customer name or tracking number.

A partner's IT contractor, poking at the search field out of professional habit, entered a deliberately malformed search string and got back a list of shipment records belonging to a completely different, unrelated customer account. LaunchStudio's review confirmed the search feature passed raw user input directly into the database query without sanitization.

**Result:** LaunchStudio replaced the vulnerable query construction with properly parameterized queries across every search and filter feature in the app, closing the exposure without changing the search experience Tim's dispatch teams were already used to.

> *"I tested that search box constantly while building it. I searched real customer names and real tracking numbers a hundred times. It never once occurred to me to type something deliberately weird into it."*
> — **Tim Oosterhuis, Founder, RouteWise (The Hague)**

**Cost & Timeline:** €2,100 (input sanitization and query hardening audit) — completed in 6 business days.

---

## Frequently Asked Questions

### A backend-focused engineer might call this "SQL injection" specifically — is that too technical a term for a founder to need to know?

The term itself doesn't matter much for a founder to memorize, but recognizing the pattern is useful: any field where a user types something that later gets used to look something up in a database is worth asking about specifically, even without knowing the formal vulnerability name.

### Does using an ORM or a managed database platform like Supabase automatically prevent this, or can it still happen there?

It reduces the risk substantially when used as intended, since most ORMs parameterize queries by default, but it's still possible to bypass that protection with raw query calls, which AI coding assistants sometimes generate when a standard ORM method doesn't easily express what was asked for.

### Manifera has decades of combined engineering experience across very different tech stacks — does that breadth actually help with a Lovable-generated Node.js app specifically?

Yes, precisely because this class of vulnerability isn't stack-specific — the same underlying pattern (unsanitized input reaching a query) shows up across PHP, Node.js, Python, and .NET alike, so broad backend experience translates directly rather than requiring stack-specific specialization.

### Herre Roelevink's own background includes cybersecurity work with TNO — does that experience shape how LaunchStudio treats a finding like Tim's?

It's a direct throughline — TNO-affiliated security research treats exactly this category of input-handling flaw as foundational rather than exotic, and that same foundational treatment is what LaunchStudio applies when this pattern turns up in an AI-native founder's codebase.

### Is this the kind of issue a founder should expect a freelancer to catch, or does it require something more specialized?

It depends heavily on the individual freelancer's specific security background rather than freelancing as a category — this is part of why LaunchStudio positions itself against generalist freelancers specifically for founders who want assurance the review was done by someone with dedicated security experience, not just general coding ability.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does a founder need to know the term 'SQL injection' specifically?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, recognizing the pattern of user input reaching a database lookup matters more than knowing the formal term."
      }
    },
    {
      "@type": "Question",
      "name": "Does using an ORM or Supabase automatically prevent this issue?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It reduces risk substantially by default, but raw query calls can still bypass that protection."
      }
    },
    {
      "@type": "Question",
      "name": "Does broad backend experience across stacks actually help with this specific issue?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, because the underlying pattern isn't stack-specific and shows up across PHP, Node.js, Python, and .NET alike."
      }
    },
    {
      "@type": "Question",
      "name": "Does a cybersecurity background shape how this kind of finding gets treated?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, this category of input-handling flaw is treated as foundational rather than exotic, consistent with that background."
      }
    },
    {
      "@type": "Question",
      "name": "Should a general freelancer be expected to catch this kind of issue?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It depends heavily on that individual's security background, not on freelancing as a category."
      }
    }
  ]
}
</script>
