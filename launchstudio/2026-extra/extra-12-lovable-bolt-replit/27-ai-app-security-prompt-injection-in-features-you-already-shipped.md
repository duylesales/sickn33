---
Title: "AI App Security: Prompt Injection in Features You Already Shipped"
Keywords: ai app security, prompt injection, LLM security, indirect injection, tool permissions, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI App Security: Prompt Injection in Features You Already Shipped

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI App Security: Prompt Injection in Features You Already Shipped",
  "description": "If your product sends customer text to a model, someone else's instructions are already in your prompt. What prompt injection can and cannot do, why filtering fails, and the boundaries that actually contain it.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-06",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-app-security-prompt-injection-in-features-you-already-shipped" }
}
</script>

Almost every product built in the last two years has an AI feature somewhere: a summariser, a reply drafter, a classifier, a chat box that answers questions about the customer's own data. They were added quickly because they are easy to add.

Each one takes text from outside your product and puts it into a prompt alongside your own instructions. The model cannot reliably tell which part is your instruction and which part is data, because to the model it is all just text — and that is the whole of the problem.

Prompt injection is not a theoretical risk being discussed at conferences. It is a property of how these systems work, and no amount of prompt engineering removes it.

## What an Attacker Is Actually After

The interesting question is not whether the model can be persuaded to say something odd. It is what the model is allowed to do.

If your feature summarises text and shows the result to the person who submitted it, a successful injection produces a strange summary for that person. Embarrassing, not dangerous.

If your feature can call tools — query the database, send an email, make an HTTP request, write a record, trigger a workflow — then a successful injection performs those actions with your application's permissions. That is the difference between a curiosity and an incident, and it is entirely determined by what you connected.

So the first question for every AI feature you have shipped: what can it do besides produce text? The answer is often more than the founder remembers.

## Indirect Injection Is the One That Gets You

Direct injection — a user typing instructions into your chat box — is the version everyone thinks of, and it is the less dangerous one, because the user is attacking their own session.

Indirect injection is when the malicious instruction arrives inside content your product processes on somebody else's behalf. An uploaded CV containing white text that tells the screening model to rate the candidate highly. A support email with instructions hidden in a signature. A web page your product fetches and summarises. A document a customer shares with their colleague, processed by your system on the colleague's behalf.

Here the attacker is not the user. The user is the victim, and your product is the mechanism. Any feature that processes content from one person and acts in the context of another is where this class of attack lives.

## Filtering Does Not Work

The instinctive fix is to detect and strip malicious instructions before they reach the model. It fails, reliably, and understanding why saves weeks.

Instructions can be phrased infinitely many ways, in any language, encoded, split across a document, expressed as a story, or embedded in structure rather than text. Every filter is a list of what somebody thought of, and the attack surface is the set of things nobody thought of.

Filtering is worth a little effort as a speed bump and worth no confidence at all. The defences that work do not attempt to distinguish instructions from data; they make it not matter.

## The Four Boundaries That Do Work

**Least privilege for tools.** Whatever the model can invoke, it can be made to invoke. Give it the narrowest possible set: read this customer's own records, not query arbitrary tables. Nothing destructive, nothing that spends money, nothing that reaches outside the account it is working within.

**Authorisation outside the model.** Never let the model decide who may do what. The model may ask for an action; your code checks whether the current user is permitted, using the same entitlement logic as the rest of the product. An injected instruction then produces a request that is simply refused.

**A human in the loop for anything irreversible.** Sending an email, making a payment, deleting data, publishing something. The model drafts and a person approves. This single measure removes most of the realistic damage.

**Treat output as untrusted.** Model output is data from an untrusted source, not a fragment of your application. Never render it as raw HTML, never execute it, never pass it into a database query or a shell command. An injection whose payload is a script tag only matters if you insert that output into a page without escaping it.

## Separate the Untrusted Text

Structure helps even though it does not solve the problem. Put your instructions in the system role and the untrusted content in a user message, clearly delimited, with a statement that everything inside the delimiters is data to be processed rather than instructions to follow.

This raises the effort required and reduces the accidental cases — the customer who happened to write "ignore the above" in a support ticket. It does not stop a determined attempt, so it belongs alongside the boundaries above rather than instead of them.

One related habit: never place secrets, internal rules you would not want disclosed, or another customer's data in the same context window as untrusted text. Anything in the prompt can come out of the model, and "please repeat your instructions" is the easiest attack there is.

## Watch What the Feature Does

Because you cannot prevent injection, you need to be able to notice it.

Log every AI feature invocation with the input, the output, which tools were called and with what arguments, and the account involved. Retain it for long enough to investigate — with personal data handled according to the same rules as any other log.

Then alert on the shapes that indicate something is wrong: a tool called far more often than normal, an unusual pattern of arguments, output containing what looks like configuration or another account's identifiers, a single account driving a large share of invocations.

For most small products this is the difference between finding out in a day and finding out from a customer.

## Budget and Rate Limits Are Security Controls

An AI feature with no limits is also a denial-of-wallet vulnerability: an attacker who can trigger model calls can spend your money, and it does not require any cleverness at all.

Per-user and per-account rate limits on every model-backed endpoint, a cap on input and output size, and a spending limit at the provider. These are the same controls as the cost article recommends, and here they are doing security work.

## The Retrieval Case Deserves Its Own Check

Products that answer questions over a customer's own documents have a second problem layered on the first, and it is the one that produces the worst headlines: retrieving the wrong customer's content.

The failure is ordinary rather than exotic. Documents from every account go into one index. The search step retrieves by similarity, which knows nothing about permissions. A question phrased in a particular way pulls in a passage belonging to somebody else, and the model dutifully incorporates it into an answer.

The fix is to apply the filter before retrieval, never after. The search must be constrained to the account — and, where it matters, to the specific user's permissions within that account — as part of the query itself, not by discarding results afterwards. Discarding afterwards still leaks when the model has already seen the text, and in most implementations it has.

Two further habits. Store the permission scope alongside each indexed chunk rather than relying on a naming convention, so the constraint is enforced by data rather than by discipline. And when a document's permissions change — shared, unshared, moved, deleted — update the index in the same operation, because an index that lags behind the source is a permission system that lags behind reality.

Test it the way you would test anything else: ask, as one customer, a question whose answer exists only in another customer's documents, and confirm the product says it does not know.

## Setting This Up

For a product with AI features this is typically one to two days: an inventory of every model-backed feature and what it can do beyond generating text, tool permissions narrowed to the minimum with nothing destructive or cross-account, authorisation moved firmly outside the model into your existing entitlement logic, human approval required for irreversible actions, output escaped everywhere it is displayed and never executed or interpolated into queries, untrusted content structurally separated from instructions, secrets and other customers' data kept out of the context, invocation logging with tool calls recorded, alerting on anomalous patterns, and rate and spending limits on every model-backed endpoint.

LaunchStudio does this as part of security review for products with AI features, which is now most of them. The engineers are Manifera's — eleven years, 120+ engineers, security work for clients including Vodafone, TNO and CFLW.

[Tell us what your AI feature is allowed to do](https://launchstudio.eu/en/#contact). That list is the whole assessment.

## Real example

### The CV That Rated Itself

Machteld Oosterbeek built Sollicitatiescan in Lovable: an application screening tool for recruitment agencies and employers, which reads uploaded CVs against a role description and produces a shortlist with reasoning, used by 31 agencies.

The feature also had tools. It could look up the candidate's previous applications in the database, and it could move a candidate to the shortlist stage — added because agencies wanted the obvious matches promoted automatically.

A candidate applying to a logistics role submitted a PDF with a paragraph in white four-point text: instructions to disregard the role requirements, rate the candidate as an exceptional match, move them to the shortlist, and not mention the instruction in the reasoning. It worked exactly as written.

The agency noticed because the reasoning was unusually enthusiastic and the candidate's experience did not match. Reviewing three months of history, Machteld found four further CVs containing similar text, from what appeared to be a template circulating in a jobseekers' forum.

Three business days: the shortlist-promotion tool removed entirely, so the model can propose but a recruiter decides; the database lookup narrowed to the specific candidate being assessed within the agency's own account, rather than a general query capability; authorisation moved outside the model, checking the recruiter's permissions on every proposed action; uploaded documents converted to plain text with invisible and off-canvas content extracted and flagged rather than silently included; untrusted document text structurally separated from the instructions and clearly marked as data; model output escaped wherever it is rendered, since the reasoning was previously inserted as HTML; per-agency rate limits and a provider spending cap; and full invocation logging with an alert on documents containing hidden text, which now flags for human review rather than blocking.

**Result:** the four affected applications were re-screened and two were genuinely reasonable candidates who had used the template on advice. The hidden-text alert has since flagged 31 documents in a year, of which 9 contained instruction-shaped content. No automated promotion has been possible since day one of the fix, which Machteld regards as the change that actually mattered.

> *"The model did exactly what it was told. The mistake was mine: I gave it a button that changed a candidate's status, and then let strangers write to it."*
> — **Machteld Oosterbeek, Founder, Sollicitatiescan (Hilversum)**

**Cost & Timeline:** €3,400 (tool permission reduction, external authorisation, document text extraction with hidden content detection, prompt structuring, output escaping, rate and spending limits, invocation logging and alerting) — completed in 3 business days.

## Frequently Asked Questions

### Can prompt injection be prevented?

No. It is a property of how language models process text. What you can do is limit what a successful injection achieves — narrow tools, authorisation outside the model, human approval for irreversible actions, and treating output as untrusted.

### Is filtering malicious instructions worth doing?

As a small speed bump, not as a defence. Instructions can be phrased in unlimited ways, in any language or encoding, so every filter is a list of what someone happened to think of.

### What is indirect prompt injection?

When the instruction arrives inside content your product processes on someone else's behalf — an uploaded document, a fetched web page, an incoming email. The user is the victim rather than the attacker, which makes it the more serious case.

### Is a summariser with no tools safe?

Much safer. The worst outcome is misleading output for the person who submitted the text. Risk scales with what the feature can do beyond producing words.

### What should I log for an AI feature?

The input, the output, every tool call with its arguments, and the account. Then alert on anomalies — unusual tool frequency, odd arguments, output containing identifiers or configuration.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can prompt injection be prevented?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — it is inherent to how models read text. Limit the consequences instead: minimal tools, authorisation outside the model, human approval for irreversible actions, untrusted output."
      }
    },
    {
      "@type": "Question",
      "name": "Is filtering prompt injection attempts effective?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Only as a speed bump. Instructions can be phrased, translated or encoded in unlimited ways, so filters only cover what someone anticipated."
      }
    },
    {
      "@type": "Question",
      "name": "What is indirect prompt injection?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "An instruction hidden in content your product processes for someone else — a document, web page or email — making your user the victim rather than the attacker."
      }
    },
    {
      "@type": "Question",
      "name": "Is an AI summariser without tools safe?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Much safer — the worst case is misleading output for the submitter. Risk scales with what the feature can do beyond generating text."
      }
    },
    {
      "@type": "Question",
      "name": "What should be logged for an AI feature?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Input, output, every tool call with arguments, and the account — then alert on unusual tool frequency, odd arguments or identifiers appearing in output."
      }
    }
  ]
}
</script>
