---
Title: "What Your Engineering Partner Needs From You on Day One"
Keywords: engineering partner onboarding, day one checklist founder, giving developer access, prototype handover, launch preparation, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# What Your Engineering Partner Needs From You on Day One

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What Your Engineering Partner Needs From You on Day One",
  "description": "A non-technical founder who has just signed an engineering engagement has one job in the first 48 hours: unblock the team. This article lists exactly which accounts, credentials, and decisions to prepare, in what order, and what happens to your timeline when any of them are missing.",
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
  "datePublished": "2027-01-04",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/what-your-engineering-partner-needs-from-you-day-one"
  }
}
</script>

**Engineer, Monday 09:14:** "Morning! Ready to start. Can you invite me to the repo and the Supabase project?"
**Founder, Monday 09:20:** "Sure — what's a repo?"
**Engineer, Monday 09:22:** "The GitHub project your Lovable app exports to. Do you know if it was ever connected?"
**Founder, Wednesday 16:41:** "OK, found it. It was under my old email. Also I think I need to reset the password on the Supabase one, hold on."

That exchange is completely normal, nobody in it did anything wrong, and it still cost two and a half days of a two-week engagement. The work you paid for did not start on Monday morning; it started Wednesday evening. Nothing about the quote changed, nothing about the scope changed, and yet roughly 12% of the calendar time you bought evaporated into password resets. This article is the list that prevents that — the specific accounts, credentials, and decisions to have ready before the first working day, written for a founder who built their product with Lovable or Bolt and has never once thought about DNS.

## Why Day One Is the Cheapest Day to Be Organised

A short, fixed-price hardening engagement has a shape that most founders don't see: the first two days are almost entirely about understanding what exists. An engineer opens your codebase, reads how your data is structured, checks what your AI tool wired up automatically, and builds a mental map. Every hour they cannot see something, they are guessing — and guessing on a two-week engagement is how a "small change" turns into a discovery on day nine.

The asymmetry is what matters here. Gathering your accounts takes you maybe ninety minutes of unglamorous clicking. Not gathering them costs the engagement two to four days, and those days come out of the delivery end, not the start. A three-week project that begins on Wednesday of week one does not become a four-week project — it becomes a three-week project with one less week of real engineering in it. Nobody sends you an invoice for that. You just get a slightly thinner launch.

There is also a quieter cost. When an engineer is blocked, they context-switch to something else, and coming back to your codebase means re-reading the parts they had already mapped. In practice a two-day access delay in week one costs closer to two and a half days of output. So: ninety minutes of your time, or two and a half days of theirs. That is the trade you are making, and it is the easiest one you will make all month.

## Asset One: The Repository, and Whether You Actually Own It

Your code lives somewhere. If you built in Lovable or Bolt, there is usually a GitHub connection — either one you set up during a "connect to GitHub" step you half-remember, or one that was never created, meaning your code exists only inside the AI tool's own workspace. Both are fine. What is not fine is finding out which on Monday morning.

Log into GitHub before day one and check three things. First, does a repository for this product exist, and does it contain recent code — click into it and confirm the last commit date roughly matches the last time you changed anything. Second, is it under your personal account or an organisation? If it is under a personal account tied to an email you no longer use, fix that now, because transferring a repo mid-engagement is the kind of two-hour errand that becomes a two-day errand. Third, is it private? If your repository is public and contains anything resembling a key, treat that as a live issue and mention it on day one rather than discovering it in the audit.

If no GitHub connection exists at all, say so plainly. In Lovable you can connect one from the project settings, and the export usually takes a few minutes. Doing it yourself before the engagement starts means the engineer's first commit lands in a repo you own, on an account you control — which is the whole point of owning your code rather than renting it from a tool.

## Asset Two: The Database and Backend Accounts

Most AI-built products have a Supabase or Firebase project sitting behind them, created either by you during setup or automatically by the tool. Find it. In Supabase, log in and confirm you can see the project dashboard and the organisation it belongs to. In Firebase, confirm you are listed as Owner on the project inside the Google Cloud console, not just as a collaborator on someone else's.

The specific trap here is shared or borrowed accounts. A surprising number of prototypes are running on a Supabase project created under a technical friend's login "just to get it working," or on a free-tier account attached to a co-founder who has since left. If that describes you, resolve it before day one — either by transferring the project or by accepting you may need a fresh project and a data migration, which is a real scope item and should be priced, not discovered.

While you are in there, note two facts your engineer will ask for within the first hour: roughly how many rows are in your main tables, and whether there is any real customer data in the database. The answer to the second question changes everything about how the work is done. Real personal data means staging environments need scrubbed copies, GDPR obligations are live, and nobody is running experiments against production. Made-up test data means the team can move considerably faster. Be honest here even if the honest answer is "there are eleven real signups from friends and one of them is my sister."

## Asset Three: Payments — the Account You Should Not Hand Over

Stripe and Mollie are different from everything else on this list, because they touch money that is legally and practically yours. The correct posture is: you own the account, you never share the login, and you invite your engineering partner as a team member with a restricted role.

Create the account yourself, in your company's name, with your own email and your own two-factor authentication. In Stripe, that means going to Settings → Team and inviting the engineer with the Developer role, which allows API keys, webhooks, and test-mode work but not payouts, bank detail changes, or the ability to remove you. In Mollie — which is often the better fit if most of your customers are Dutch and expect iDEAL — the equivalent is adding a user to your organisation rather than sharing credentials, and keeping the bank account and payout settings under your own login only.

Do the boring registration work in advance, because payment onboarding is the single most common cause of a launch date slipping by a week and it is entirely outside your engineer's control. Stripe and Mollie both run identity and business verification: Chamber of Commerce (KvK) number, VAT number, a bank account in the business's name, sometimes a copy of your ID, sometimes a request for extra documentation about what you sell. That review can take anywhere from a few hours to several business days, and no amount of engineering skill makes it go faster. Start it the day you sign the contract, not the week you plan to launch.

## Asset Four: Domain, DNS, and the Email Sending Domain

This is the section founders skip, and it is the one that most often ruins launch week. Three separate things live here, and they are commonly confused with each other.

Your **domain registrar** is where you bought the domain — TransIP, Namecheap, GoDaddy, Cloudflare, Google Domains. You need to be able to log in. If your domain was bought by a designer, a former co-founder, or an agency that built your landing page in 2024, find out now, because recovering a domain from someone who has stopped answering email is a multi-week problem with no engineering solution.

Your **DNS** is the settings panel inside that registrar (or inside Cloudflare, if you moved DNS there) where records are added. Your engineer will need to add or change records to point the domain at your hosting and to authorise email sending. Rather than handing over your registrar password, check whether your provider supports delegated access — Cloudflare has member roles including a DNS-only role, and Cloudflare in particular is worth moving DNS to for exactly this reason. If your registrar has no such feature, the workable alternative is that you keep the login and add the records yourself while the engineer reads them out on a call. It takes twenty minutes and it is far safer than sharing a password that also controls your domain ownership.

Your **email sending domain** is the third thing, and it is not the same as your inbox. If your product sends password resets, receipts, or notifications, those emails go out through a service like Resend, Postmark, SendGrid, or Mailgun, and they will land in spam unless SPF, DKIM, and DMARC records are added to your DNS and verified. Domain verification and reputation warm-up take time; DMARC in particular is something you want in place days before launch, not on launch morning. Create the sending account in advance and tell your engineer which one you chose.

## Asset Five: A Written Note Explaining What the Product Actually Does

Your engineer can read your code. They cannot read your intentions, and the gap between those two things is where most misunderstandings live. Write one page — genuinely one page, in plain language, no technical vocabulary required — covering four things.

Who uses this, and are there different kinds of user? "Freelance bookkeepers sign up and add clients; clients get a read-only login" is one sentence that determines an entire permissions model. What does someone pay for, and how — one-off, monthly subscription, per-use? That determines the payment architecture. What must absolutely never happen — "one bookkeeper must never see another bookkeeper's clients" — becomes a testable security requirement rather than an unspoken assumption. And what is fake right now? Almost every AI-generated prototype contains screens that look functional but are wired to placeholder data. You know which ones. Your engineer will otherwise spend half a day discovering it.

That last point deserves emphasis, because it is where non-technical founders lose the most time to embarrassment. There is nothing shameful about a prototype with a beautiful dashboard powered by hard-coded numbers — that is what these tools produce, and roughly 80% of AI-built projects never reach production precisely because that gap goes unaddressed. Naming it on day one is not a confession, it is scoping.

## Asset Six: One Decision-Maker, One Channel, One Response Window

The final thing your engineering partner needs from you is not a credential. It is a commitment about how decisions get made.

Name one person — almost certainly you — who can answer product questions without a committee. Pick one channel and use it for everything: a shared Slack channel, a WhatsApp group, or email, but one of them, not all three. Questions scattered across three tools get answered twice or not at all, and no one can reconstruct what was decided.

Then agree a response window, out loud. Something like: "I will answer any question within one business day, and I'm reachable same-day on Tuesday and Thursday afternoons." That single sentence is worth more than daily check-ins, because it tells the team when to batch questions and when to expect an answer, instead of making them guess whether you have vanished. On a two-week engagement, a founder who reliably answers within a day is a better partner than one who is constantly available but unpredictable.

## What You Should Not Prepare, and What to Say Instead of "I Don't Know"

You do not need to write technical requirements, propose an architecture, or research whether you should be on AWS. If you find yourself reading about Postgres row-level security at midnight before day one, stop — you are doing the job you hired out, and doing it worse. You also do not need to tidy your code, delete unused screens, or "clean things up before they see it." Engineers who work with AI-generated code every day expect what they are going to find; tidying it usually removes context they wanted.

And when you genuinely do not know something — which login the Supabase project is under, whether emails are being sent, what happens if two people sign up with the same address — say exactly that. "I don't know, and here is where I'd look" is a useful answer. A confident guess is not. LaunchStudio is powered by Manifera, a software development company with 11+ years of experience, and the single most useful thing in a kickoff conversation has never been a founder's technical fluency; it is their accuracy about what they do and don't know.

Ninety minutes of preparation, six items, one page of plain English. Get those in place and your engagement starts on Monday morning rather than Wednesday evening — which, on a fixed-price two- or three-week build, is most of the difference between a comfortable launch and a rushed one. If you want to see how the first days are structured before you commit to anything, the [LaunchStudio process page](https://launchstudio.eu/en/#process) walks through it, and the engineering standards behind it come from [Manifera's custom software practice](https://www.manifera.com/services/custom-software-development/).

Not sure what you're even looking at in your own accounts? Send us your prototype link and we'll tell you what's connected, what isn't, and what you'd need to gather — no charge, no commitment.

## Real example

### A Founder in Action: The Ninety Minutes That Saved a Week

Sanne Vermeulen, a former horticulture consultant in Utrecht, built Kweekplan — a planting and crop-rotation planner for small market gardeners — in Lovable over six weekends. She signed a fixed-price hardening engagement and, the day before kickoff, worked through a preparation list rather than waiting to be asked.

She found three things. Her GitHub repo existed but was under a Gmail address she had stopped using in 2025, so she transferred it. Her Supabase project had been created by a friend during a debugging session at a meetup, so she moved it to her own organisation. And she had no Mollie account at all, despite planning to charge €9/month with iDEAL — so she started the KvK verification on the Friday. Mollie's review took four business days, and it ran entirely in parallel with the engineering work instead of blocking it.

**Result:** Kweekplan's engagement started with full access at 09:00 on day one, the payment integration was tested in live mode on day eight instead of day twelve, and the product went live on the originally quoted date with two spare days used for a proper end-to-end test of the subscription flow.

> *"I almost didn't bother with the checklist because it looked like admin. It was the highest-leverage ninety minutes of the whole project — I basically bought back a week of engineering time by clicking around in accounts on a Sunday."*
> — **Sanne Vermeulen, Founder, Kweekplan (Utrecht)**

**Cost & Timeline:** €2,400 (Launch Ready package, auth hardening, data isolation, and Mollie subscriptions) — live in 11 business days.

---

## Frequently Asked Questions

### What if my code only exists inside Lovable and was never connected to GitHub?

That is common and completely fine. Connect GitHub from your Lovable project settings before day one — the export usually takes a few minutes — so the first commit of the engagement lands in a repository you own on an account you control. If you cannot get it working, say so early; it is a ten-minute fix for an engineer but only if they know about it before Monday.

### Should I give my engineering partner my Stripe login so they can set everything up?

No. Create the Stripe account yourself in your company's name with your own two-factor authentication, then invite the engineer under Settings → Team with the Developer role. That gives them API keys, webhooks, and test mode while keeping payouts, bank details, and account ownership exclusively yours.

### How far in advance should I start payment provider verification?

Start it the day you sign the contract. Stripe and Mollie both run business identity checks requiring your KvK number, VAT number, and a business bank account, and that review takes anywhere from a few hours to several business days for reasons no engineer can accelerate. Started early, it runs invisibly in the background; started late, it is the reason your launch slips.

### I don't control my domain — a designer bought it years ago. Is that a real problem?

Yes, and it is worth solving immediately rather than at launch. Domain recovery from an unresponsive third party can take weeks and has no technical workaround, so contact them the week you sign. If they are genuinely unreachable, buying a new domain early is far better than discovering the problem the day before you go live.

### Do I need to understand what SPF, DKIM, and DMARC are?

No — you need to know that they exist, that they are DNS records controlling whether your product's emails reach inboxes, and that they need setting up before launch rather than after. Your job is making sure someone can add records to your DNS; your engineer's job is knowing which records.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What if my code only exists inside Lovable and was never connected to GitHub?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "That is common and fine. Connect GitHub from your Lovable project settings before day one so the first commit lands in a repository you own, and tell your engineer early if you cannot get the export working."
      }
    },
    {
      "@type": "Question",
      "name": "Should I give my engineering partner my Stripe login so they can set everything up?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Create the Stripe account yourself in your company's name with your own two-factor authentication, then invite the engineer under Settings and Team with the Developer role so payouts, bank details, and ownership stay yours."
      }
    },
    {
      "@type": "Question",
      "name": "How far in advance should I start payment provider verification?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Start it the day you sign the contract. Stripe and Mollie both run business identity checks needing your KvK number, VAT number, and a business bank account, and that review can take several business days no engineer can speed up."
      }
    },
    {
      "@type": "Question",
      "name": "I don't control my domain — a designer bought it years ago. Is that a real problem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, and it should be solved immediately. Domain recovery from an unresponsive third party can take weeks with no technical workaround, so contact them the week you sign or buy a new domain early."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need to understand what SPF, DKIM, and DMARC are?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. You need to know they are DNS records that control whether your product's emails reach inboxes and that they must be set up before launch. Your job is ensuring someone can add DNS records; your engineer knows which ones."
      }
    }
  ]
}
</script>
