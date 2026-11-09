---
Title: "Red Flags When Hiring Someone to Fix Your AI App"
Keywords: red flags hiring developer, warning signs software agency, hiring someone to fix ai app, bad developer signs startup, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Red Flags When Hiring Someone to Fix Your AI App

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Red Flags When Hiring Someone to Fix Your AI App",
  "description": "A list of warning signs for non-technical founders hiring a freelancer, agency or service to fix or launch an app built with Lovable, Bolt, v0, Cursor or Claude Code, grouped by the sales conversation, the quote, ownership and access, the work itself and after delivery, with what each red flag means, what to ask instead and the green flags that indicate a trustworthy partner.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-09-20",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/red-flags-when-hiring-someone-to-fix-your-ai-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "OWASP Top 10", "url": "https://owasp.org/www-project-top-ten/" },
    { "@type": "CreativeWork", "name": "Supabase: Shared responsibility model", "url": "https://supabase.com/docs/guides/deployment/shared-responsibility-model" },
    { "@type": "CreativeWork", "name": "GitHub: Managing access to your repository", "url": "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens: Verwerkersovereenkomst", "url": "https://www.autoriteitpersoonsgegevens.nl/themas/basis-avg/avg-algemeen/verwerkersovereenkomst" }
  ]
}
</script>

**Short answer:** The biggest red flags when hiring someone to fix an AI-built app are: quoting without looking at the app, recommending a rebuild without explaining why, vague scope with no exclusions, creating accounts in their own name, asking for your passwords instead of their own access, no written deliverables, no testing with several user roles and no plan for after launch. Each of these makes problems more likely and harder to recover from. Good partners do the opposite: they look first, write things down, work in your accounts and explain trade-offs plainly.

Founders without technical background are at a disadvantage when hiring technical help. They cannot judge code quality from a conversation, and most suppliers sound confident. Red flags are a practical substitute: patterns of behaviour that predict trouble regardless of how good someone sounds. This page lists the most important ones, grouped by the stage at which they appear, with what to ask instead.

## Key Takeaways

- **Watch behaviour, not claims:** what a supplier does before signing predicts how they work.
- **Ownership red flags** are the most costly to fix later.
- **Vague scope** almost always becomes a dispute or an incomplete result.
- **A rebuild recommendation** should come with clear reasons and alternatives.
- **Green flags** are easy to spot once you know what to look for.

## Red Flags in the Sales Conversation

| Red flag | What it may mean | Ask instead |
| --- | --- | --- |
| They quote without looking at your app | The price is a guess; scope will change later | "Can you look at the project before quoting?" |
| They ask no questions about users or data | They do not know what matters for your app | "What would you need to know about our users?" |
| Everything is "easy" or "a quick fix" | Inexperience or a sales tactic | "What could make this harder than expected?" |
| They criticise your choice of tool strongly | They may push their own stack | "What would you keep, and why?" |
| They promise "100% secure" or "bank-grade" | Marketing language, not engineering | "How will you test access between users?" |
| Pressure to sign quickly | Discount tactics or capacity filling | "Can I have a few days to compare?" |
| No references or examples | Limited relevant experience | "Can I speak to two founders you helped?" |

## Red Flags in the Quote

| Red flag | What it may mean | Ask instead |
| --- | --- | --- |
| A single sentence of scope | Unclear deliverables; disputes later | "Can you list the work items?" |
| No exclusions | Everything will be "extra" later | "What is not included?" |
| No assumptions | Price can change for any reason | "What is the price based on?" |
| No timeline | No accountability | "When will each part be done?" |
| "Unlimited revisions" | Scope is not understood | "How are changes handled?" |
| Hosting bundled with an unexplained markup | Lock-in and hidden margins | "Can hosting be billed directly to us?" |
| Large upfront payment for a long project | Risk if the relationship fails | "Can we pay per milestone?" |

## Red Flags About Ownership and Access

These are the most important, because they are the hardest to undo.

| Red flag | What it may mean | Ask instead |
| --- | --- | --- |
| They create the database or hosting in their own account | You do not own your product | "Can you work in accounts in our company name?" |
| They want your personal passwords | Shared logins, no audit trail | "Can I invite you with your own access?" |
| They move code to their own repository | Your code becomes harder to retrieve | "Will the code stay in our repository?" |
| Domain registered by them | Your address belongs to someone else | "Will the domain be in our name?" |
| No processing agreement offered when handling personal data | Data protection obligations ignored | "Can we sign a processing agreement?" |
| Reluctance to document access | Hard to remove access later | "Can you list every access you will have?" |

In the Netherlands and the EU, if a supplier processes personal data on your behalf, a processing agreement is generally required; the Dutch Data Protection Authority explains the basics. A supplier who has never heard of one is a concern.

## Red Flags in How the Work Is Done

| Red flag | What it may mean | Ask instead |
| --- | --- | --- |
| Testing only with one account | Cross-user data leaks will be missed | "How do you test with different roles?" |
| Fixes made directly in production | Risk of breaking the live app | "Will changes go through staging first?" |
| Disabling database policies to fix errors | Security made worse to make things work | "How do you handle permission errors?" |
| No written updates | You cannot see progress or decisions | "How often will I get updates?" |
| No tests added | Problems will return | "Which tests will you add?" |
| Changing the interface without asking | Scope creep, surprise for users | "Will the app look the same?" |
| Ignoring your AI tool workflow | You cannot continue building | "Can I keep using my AI tool afterwards?" |

## Red Flags After Delivery

| Red flag | What it may mean | Ask instead |
| --- | --- | --- |
| No handover document | Knowledge stays with the supplier | "What will I receive in writing?" |
| Access not removed when you ask | Lingering security risk | "Please confirm access is removed." |
| No support after launch | You are alone when problems appear | "What happens in the first days after launch?" |
| Bugs from their work treated as new paid work | No accountability | "Are issues from your work fixed for free?" |
| Monitoring alerts go only to them | You cannot see your own app's health | "Can alerts also go to me?" |

## The Rebuild Recommendation

A rebuild recommendation deserves special attention. Sometimes a rebuild is the right answer: the app is fundamentally unsuitable, the data model cannot support the business or the code is beyond repair. More often, AI-built apps that already work can be made production ready with targeted fixes. A good supplier explains why a rebuild is needed, what alternatives they considered, what it will cost compared with fixing and how long your product will be frozen. A supplier who recommends a rebuild without these explanations, especially in their own preferred stack, may be optimising for their workflow rather than your business.

## Why These Red Flags Matter More for AI-Built Apps

AI-built apps often have specific weak spots: loose database policies, keys in the frontend, payments granted on a success page, public storage and accounts spread across personal logins. A supplier who does not know these patterns will miss them. A supplier who works carelessly, for example by disabling a policy to fix a permission error, can make them worse. And because founders often keep building with AI tools afterwards, a supplier who ignores that workflow leaves a codebase the founder cannot safely change.

## Green Flags

- They look at your app before quoting
- They ask about your users, roles, data and deadlines
- They explain risks and trade-offs in plain language
- They tell you what they will not do
- They work in your accounts with their own access
- They list scope, assumptions and exclusions
- They test with several user roles
- They use staging and add tests
- They write things down: updates, decisions, handover
- They respect your AI tool workflow
- They have references you can contact
- They are comfortable recommending someone else when it fits better

## What to Do When You Spot a Red Flag

A single red flag is not always disqualifying. Inexperienced but honest freelancers may simply not know to list exclusions, and will happily do so when asked. Raise it directly and watch the response. A good supplier adjusts: they add exclusions, move accounts into your name, agree to staging. A supplier who becomes defensive, dismissive or vague is telling you how the project will go.

## Protecting Yourself Contractually

Simple contractual points prevent many problems: written scope with exclusions, ownership of code and intellectual property assigned to you, accounts in your company's name, a processing agreement for personal data, payment by milestones, an agreed change process and a clause about handover and access removal at the end. Templates from the KVK or a lawyer can help. None of this needs to be adversarial; good suppliers expect it.

## If You Already Hired Someone and See Red Flags

Sometimes founders realise mid-project that something is wrong. A calm, practical approach works best. First, secure ownership: ask for accounts, repositories and domains to be moved into your name or confirm they already are, and create your own admin access to every service. Second, ask for a written status: what has been done, what remains and what has changed. Third, if trust is low, ask an independent party to review the work so far before paying further invoices. Most problems can be resolved through a direct conversation once the facts are clear. If not, having ownership and documentation in hand makes it far easier to switch to another supplier without starting over.

## A Short Checklist for Your First Call

Before the first conversation with any supplier, prepare five questions and listen carefully to the answers:

1. "Can you look at the app before giving me a price?"
2. "How do you check that one user cannot see another user's data?"
3. "Will everything stay in accounts in my company's name?"
4. "What will I receive in writing at the end?"
5. "What happens if something breaks a week after launch?"

Experienced suppliers answer these easily and concretely. If the answers are vague, defensive or full of jargon you cannot follow, you have learned something important before spending any money.

## Trust Your Instinct, Then Verify

Many founders tell us afterwards that something felt off early on: a supplier who never wrote anything down, or who brushed off a question about ownership. Instinct is a useful signal, but verification is better. Ask for the specific thing that worried you, in writing, and see what comes back.

## What We Need From You

- A 15-minute intro call
- Read access to your code and configuration
- Any quotes or proposals you want a second opinion on

Use the [price calculator](https://launchstudio.eu/en/#calculator) for an indication.

## Price Overview

| Package | Price |
| --- | --- |
| Launch Ready | €800-€3,500 fixed, including 48 hours of post-launch support |
| Launch & Grow | €2,500-€7,500 fixed, plus €49 per month for ongoing care |

## Why Founders Choose LaunchStudio

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, working for clients such as Vodafone and TNO. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at Manifera's development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore. We look before we quote, work in your accounts, write scope and exclusions down and leave a handover you can use without us.

## Real example

### An AI-Native Founder in Action: The Supplier Who Owned Everything

Wessel de Bruijn runs a booking platform for boat rentals in Giethoorn, built with Lovable and Supabase. A year earlier, a small agency had "made it production ready". When Wessel wanted to add a second location and change the pricing, he discovered that the Supabase project, the Netlify site and the domain were all in the agency's accounts, the agency had moved the code to its own repository and the monthly hosting invoice included an unexplained margin. The agency was slow to respond and quoted a high price for the changes.

Wessel contacted LaunchStudio. The first step was not technical: with Wessel, LaunchStudio drafted a polite request to the agency to transfer the accounts, repository and domain, referring to the ownership clause in their original agreement. The agency complied within two weeks. LaunchStudio then reviewed the app and found that several database policies had been disabled to "fix errors", payments relied on the success page and there were no backups beyond the default.

The fixed quote of €2,300 covered restoring and testing the policies, verified Mollie webhooks, backups with a restore test, staging, monitoring and documentation, with everything in Wessel's accounts.

**Result:** Wessel's hosting costs fell because he now paid providers directly. The second location launched for the new season, and he made the pricing change himself in Lovable with the tests confirming nothing broke.

> *"I thought I had a partner. I actually had a landlord. Now the house is mine."*
> - **Wessel de Bruijn, Founder, Vaarplek (Giethoorn)**

**Cost & Timeline:** €2,300 (Launch Ready package: ownership recovery support, policy restoration with tests, webhooks, backups, staging, monitoring and documentation) - completed in 6 business days after the transfer.

## Frequently Asked Questions

### What is the biggest red flag when hiring a developer for an AI-built app?

Creating accounts, code repositories or domains in their own name instead of yours. It is the hardest problem to undo and gives the supplier control over your product. Insist on working in accounts your company owns.

### Is a rebuild recommendation always a red flag?

No. Sometimes a rebuild is right. It becomes a red flag when it comes without clear reasons, alternatives and a cost comparison with fixing the existing app, especially when the supplier proposes their own preferred stack.

### How can I check a supplier without technical knowledge?

Watch behaviour: do they look at your app before quoting, ask about users and data, write scope and exclusions, work in your accounts and offer references? Ask how they test access between users and listen for specific answers.

### How does Manifera's experience help avoid these problems?

Manifera has 11+ years of experience, 160+ delivered projects and 120+ engineers, working for clients such as Vodafone and TNO under clear contracts. LaunchStudio follows the same practices: written scope, client-owned accounts, documentation and accountability after delivery.

### Can a bad supplier hurt my SEO and AI visibility?

Yes. Losing control of your domain, changing URLs without redirects, downtime during disputes or slow, poorly configured hosting can all hurt search rankings and how AI answer engines see your site. Owning your domain and hosting protects your visibility.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the biggest red flag when hiring a developer for an AI-built app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Creating accounts, repositories or domains in their own name instead of yours." }
    },
    {
      "@type": "Question",
      "name": "Is a rebuild recommendation always a red flag?",
      "acceptedAnswer": { "@type": "Answer", "text": "No, but it should come with reasons, alternatives and a cost comparison." }
    },
    {
      "@type": "Question",
      "name": "How can I check a supplier without technical knowledge?",
      "acceptedAnswer": { "@type": "Answer", "text": "Watch behaviour and ask how they test access between users." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help avoid these problems?",
      "acceptedAnswer": { "@type": "Answer", "text": "LaunchStudio follows Manifera's practices of written scope, client-owned accounts and documentation." }
    },
    {
      "@type": "Question",
      "name": "Can a bad supplier hurt my SEO and AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, through lost domains, broken URLs, downtime or poor hosting." }
    }
  ]
}
</script>
