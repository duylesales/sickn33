---
Title: "Invite and Team Accounts: What Breaks When a Second Person Logs In"
Keywords: multi user SaaS accounts, team invite flow implementation, roles and permissions prototype, seat based billing, shared account data isolation, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Invite and Team Accounts: What Breaks When a Second Person Logs In

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Invite and Team Accounts: What Breaks When a Second Person Logs In",
  "description": "Almost every AI-built product assumes one person per account, and the assumption is invisible until a customer invites a colleague. A guide to the decisions behind team accounts: invitations, roles, seat billing, and what happens when someone leaves the company.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-03-10",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/invite-and-team-accounts-what-breaks-when-a-second-person-logs-in" }
}
</script>

The first customer who asks whether their colleague can have a login is good news, and it is also the moment a specific architectural assumption in your product becomes expensive. Nearly every prototype is built on the idea that a user and an account are the same thing: data belongs to a person, permissions mean "is this your record," and billing attaches to a login. That model works perfectly until two people need to see the same information, at which point it does not bend — it has to be replaced.

Retrofitting is genuinely more involved than building it in, which puts founders in an awkward position before launch: build for teams you do not have yet, or ship for individuals and pay later. The answer is not automatic, but the decision should be deliberate, and there is a cheap middle path most founders never hear about.

## The Assumption Hiding in Every Prototype

Ask an AI tool to build "a project management app where users can create projects" and you will get a database where each project row records which user created it, and access rules that grant access when the requesting user matches. Clean, simple, and structurally single-tenant per person.

Now the customer invites a colleague. Every question suddenly has no answer. Can the colleague see the projects? The rule says no — they did not create them. Who is billed? The subscription is attached to the first person's login. If the first person leaves the company, what happens to the projects? They belong to a login that no longer works, at a business that still pays you.

The fix is not a feature but a change of shape: data belongs to an *organisation*, people belong to that organisation with a role, and permission is evaluated as "is this person a member of the organisation that owns this record, with sufficient rights." That is a different structure for essentially every table and every access rule in the product — which is why the cost of retrofitting is measured in weeks rather than days, and why it touches the parts most likely to break in subtle ways.

## The Cheap Middle Path Before Launch

Here is the thing that saves the most money and is almost never mentioned: you do not have to build team features before launch. You have to build the *structure* that makes them possible, and that is a fraction of the work.

Concretely: create an organisation record for every customer at signup, even when it contains exactly one person. Attach data ownership to the organisation rather than the person. Give every membership a role, even if there is only ever "owner" at first. Attach the subscription to the organisation, not the login.

There is no interface for any of this. No invitation flow, no member management, no role switching, no seat billing. From the customer's perspective, nothing exists. But when the first customer asks for a colleague, adding invitations is a few days of interface work rather than a rewrite of every access rule in the product — and, critically, none of your existing customer data has to be migrated, which is the part that carries real risk of getting someone's records wrong.

This is a small architectural decision with a large option value, and it is the single most useful thing to insist on before launch if there is any chance your customers work in teams.

## Roles: Start With Two, Not Six

When you do build team access, resist the elaborate permission matrix. Almost every early product needs exactly two roles.

**Owner** can manage billing, invite and remove people, and delete the account. **Member** can use the product. That is enough for the overwhelming majority of small-team customers, and it is honest about how much granularity you can actually enforce correctly.

The temptation is to add viewer, editor, admin, and per-resource permissions because a prospect asked. Each additional role multiplies the number of access combinations that must be enforced *on the server* and tested. A permission model that exists in the interface but not in the database is worse than none, because it makes a promise about who can see what that the product does not keep — and that promise is the sort of thing that ends up in a customer's security questionnaire.

Two roles that are genuinely enforced beat five that are enforced in the interface only. Add the third when a paying customer's requirement is specific enough to test.

## The Invitation Flow and Its Awkward Cases

Invitations look trivial and contain a surprising number of states that prototypes handle badly.

**The invited person already has an account.** They should join the organisation, not be blocked by "email already registered." This is the single most common invitation bug and it produces a confusing dead end for a new user you are trying to acquire.

**The invitation expires.** Tokens should have a lifetime — seven days is reasonable — and an expired link needs a clear message and a way to request a new one, not an error page.

**The invitation is forwarded.** An invite link that anyone can use grants access to your customer's data to whoever receives the forward. Tie the token to the invited address, or require sign-in with that address to accept.

**The same person is invited twice.** Re-inviting should update the existing invitation rather than create a second one, or you get two links in different states and unpredictable behaviour depending on which is clicked.

**The invitation is declined or the person never accepts.** Pending invitations need to be visible and cancellable by the owner. Otherwise a mistyped address sits as an open invitation to an unknown inbox indefinitely.

Each of these is a small piece of work. Together they are the difference between an invitation flow that quietly works and one that generates support conversations from customers who are actively trying to expand their usage.

## Seat Billing and the Departure Problem

If you charge per seat, several decisions must be made before the first invitation is sent.

**When does adding a user cost money?** At invitation, or at acceptance? Charging on invitation is simpler and feels wrong to customers when the person never accepts. Charging on acceptance is fairer and requires your billing to react to an event that may happen days later.

**Is the change prorated?** Adding a fifth user mid-month should usually charge a partial amount rather than nothing until renewal. Payment providers support this, but it has to be implemented rather than assumed.

**What happens when someone is removed?** Do you refund, credit, or simply reduce the next invoice? Reducing the next invoice is the simplest defensible answer, provided it is stated.

Then there is the departure problem, which every business customer eventually has. An employee leaves. Their access must be revocable immediately — including any active sessions, not merely their ability to log in again — and everything they created must remain with the organisation rather than vanishing. Prototypes that attach data to individual users produce the worst possible version of this: removing the departed employee's account deletes or orphans their work, sometimes silently, and the customer discovers it later.

Getting organisation-level ownership, enforced roles, and clean revocation right is core production work, and it is the area where AI-generated products most often carry an assumption that cannot be patched superficially. LaunchStudio, backed by Manifera's 11+ years of engineering experience, restructures single-user prototypes into multi-tenant products with access rules enforced at the database level. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Real example

### The Colleague Who Could See Everyone's Clients

Ravi Kumar had built Cliëntlijn, a small-practice CRM for independent accountants, in Lovable, and launched it to individual users. Six weeks in, three customers asked to add colleagues, so he added an invitation flow himself over a weekend.

The invitation worked. The access rules did not. The generated database policy granting access to client records had been written as "allow if the requesting user is authenticated" — a placeholder from an early prompt that had never been tightened, and which had been invisible while every account had exactly one user who only ever saw their own data through interface filtering.

The moment a second person logged in, they could reach any client record in the system through direct requests, including those belonging to other accounting practices. No customer discovered it. A pre-expansion review did, four days after the invitation feature went live.

**Result:** organisation-scoped ownership introduced across every table, database-level policies rewritten and tested with multiple accounts, invitation tokens bound to the invited address, and immediate session revocation on removal. The existing accounts were migrated without data loss.

> "The permission bug had been sitting there since the first week. It could not do any harm while everyone was alone in their own account, and it became a data breach the day I added the feature customers were asking for."
> — **Ravi Kumar, Founder, Cliëntlijn**

**Cost & Timeline:** multi-tenant restructure and access-rule rebuild delivered in 5 business days, fixed price.

## Frequently Asked Questions

### Should I build team accounts before launch if all my customers are individuals?

Build the structure, not the features. Creating an organisation record per customer and attaching data and billing to it costs little at the start and turns a later rewrite into a few days of interface work.

### How many roles does an early-stage product need?

Two: owner, who manages billing and membership, and member, who uses the product. Additional roles multiply the access combinations you must enforce and test on the server, and are best added when a paying customer's requirement is specific.

### What is the most common invitation bug?

Blocking someone who already has an account with an "email already registered" error instead of adding them to the organisation. Close behind are invite links that work for anyone they are forwarded to.

### Should I charge for a seat at invitation or at acceptance?

Acceptance is fairer and is what customers expect, but it requires billing to react to an event that may occur days later. Whichever you choose, state it clearly and prorate mid-period changes.

### What happens to a departing employee's work?

It must remain with the organisation. Products that attach data ownership to individual logins risk deleting or orphaning that work when the account is removed, which is one of the strongest reasons to establish organisation-level ownership early.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Should I build team accounts before launch if all my customers are individuals?", "acceptedAnswer": { "@type": "Answer", "text": "Build the structure, not the features. An organisation record per customer, with data and billing attached to it, costs little initially and turns a later rewrite into a few days of interface work." } },
    { "@type": "Question", "name": "How many roles does an early-stage product need?", "acceptedAnswer": { "@type": "Answer", "text": "Two: owner, managing billing and membership, and member, using the product. More roles multiply the combinations that must be enforced and tested on the server." } },
    { "@type": "Question", "name": "What is the most common invitation bug?", "acceptedAnswer": { "@type": "Answer", "text": "Blocking someone who already has an account with an email-already-registered error instead of adding them to the organisation, followed by invite links that work for anyone they are forwarded to." } },
    { "@type": "Question", "name": "Should I charge for a seat at invitation or at acceptance?", "acceptedAnswer": { "@type": "Answer", "text": "Acceptance is fairer and is what customers expect, though it requires billing to react to a later event. Either way, state the rule and prorate mid-period changes." } },
    { "@type": "Question", "name": "What happens to a departing employee's work?", "acceptedAnswer": { "@type": "Answer", "text": "It must remain with the organisation. Products attaching ownership to individual logins risk deleting or orphaning that work when the account is removed." } }
  ]
}
</script>
