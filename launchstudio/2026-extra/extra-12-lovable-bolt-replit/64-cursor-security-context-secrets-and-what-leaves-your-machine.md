---
Title: "Cursor Security: Context, Secrets and What Leaves Your Machine"
Keywords: cursor security, AI editor privacy, code privacy, .cursorignore, customer data, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Cursor Security: Context, Secrets and What Leaves Your Machine

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cursor Security: Context, Secrets and What Leaves Your Machine",
  "description": "An AI editor sends parts of your project to a model to answer. What that includes, what your customers' processing agreements say about it, and the settings and habits that keep it defensible.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-19",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/cursor-security-context-secrets-and-what-leaves-your-machine" }
}
</script>

An AI editor works by sending context to a model. Your open file, related files, sometimes an index of the whole project, plus whatever you paste into a conversation.

That is the product working as designed, and it is also a data flow out of your development environment that most founders have never characterised. For a solo developer with no customer data on the machine, the risk is modest. For someone with a production database export in a folder, or a customer's processing agreement in a drawer, it deserves ten minutes of thought.

## What Actually Leaves

Three categories, in increasing order of what people expect.

**Code you are working on.** The current file and files the editor judges relevant. This is the core of the product and the reason it is useful.

**Project-wide context.** Many editors index the repository so the assistant can answer questions about code you are not looking at. That index is derived from your whole project, including files you never open.

**Whatever you paste.** An error message with a stack trace and request data. A row from the database to explain a bug. A configuration file. This is the category with the highest risk, because it is the one where customer data most often appears, and it is entirely under your control.

## Settings Worth Checking Once

Editors differ and change, so verify rather than assume — the point is to know, not to trust a recollection.

**Whether your code is retained or used for training.** There is usually a privacy mode that guarantees it is not. Turn it on, and confirm what the setting actually promises rather than what its name suggests.

**What is excluded from indexing.** Most editors support an ignore file. Use it for anything holding secrets or data: environment files, key material, database dumps, exports, anything under a directory of customer samples.

**Where processing happens.** Which provider, which region. This is the answer you will need when a customer asks, and it belongs on the subprocessor list discussed elsewhere in this series if it touches anything of theirs.

**Whether a business tier gives better terms.** For a company with customer obligations, it frequently does, and the difference is contractual rather than technical.

## Do Not Keep Customer Data on Your Machine

This is the recommendation that removes most of the problem, and it is not really about AI editors at all.

A production export on a laptop is a risk regardless of what else is installed: the laptop is lost, the folder is synced to a cloud account, a backup includes it, an ignore rule is missed. The editor is one more path, not the cause.

Work against seeded data as described earlier in this series. Where you genuinely need a customer's data to reproduce a problem, extract the minimum, anonymise it, keep it for the investigation and delete it afterwards.

If you do hold a real export temporarily, keep it outside the project directory entirely — not merely ignored — so that no indexing decision can reach it.

## The Paste Habit Is the Real Risk

Most exposure through these tools is not the index. It is a person pasting something to get help.

A stack trace containing a request body with a customer's name and address. A database row to explain why a calculation is wrong. A configuration file with a live key to ask why a connection fails. Each is a reasonable thing to want help with and each sends real data to a third party.

Two habits cover it. Redact before pasting — replace names, addresses, identifiers and keys with placeholders, which takes fifteen seconds and almost never changes the answer. And ask about the shape rather than the content: "why would this query return nothing when the row exists" is answerable without the row.

For keys specifically: never paste one, ever, for any reason. If a key has been pasted, rotate it, as described in the secret rotation article in this series.

## What Your Customers' Agreements Say

If you process personal data for business customers, your processing agreement almost certainly requires you to list your subprocessors and to notify before adding one.

The question this raises is narrow and worth answering honestly: does your development tooling process your customers' personal data? If you work only against seeded data, the answer is no and the tool is not a subprocessor — it processes your code, which is yours.

If you routinely paste production data into an assistant, the answer is yes, and that is a subprocessor you have not declared. The correct response is not usually to declare it; it is to stop doing that, which is both easier and better.

Write down which of the two describes you. It is the question a thorough customer will eventually ask, and having considered it before being asked is the whole of a good answer.

## When the Assistant Can Run Commands

The newer capability worth a separate thought: editors and agents that execute commands, edit files across the project, install packages and call services on your behalf.

This is genuinely useful and it changes the risk from disclosure to action. A model that can run a command can run the wrong one, and the failure modes are familiar to anyone who has worked with a capable but unsupervised helper: a destructive command run against the wrong environment, a migration applied to production because the credentials in the environment pointed there, a package installed without anyone reading its name.

Four measures keep it comfortable.

**Approve commands rather than allowing them wholesale**, at least until you know how a particular agent behaves. The confirmation step is where you notice that the database URL in that terminal is the live one.

**Never give the development environment production credentials.** This is the measure that matters most, because it converts a whole class of catastrophe into an error message.

**Work in a branch**, so file changes across the project can be discarded in one action.

**Keep destructive operations out of reach.** A database account for development that cannot drop tables is one that cannot be persuaded to.

None of this is an argument against the capability, which saves real time. It is the same argument the AI security article in this series makes about tools and models generally: the question is never whether the thing can be tricked, but what it is able to do when it is.

## The Machine Itself

One step back from the editor, the development machine is the weakest link in most small software companies, and it holds more than any single tool does: repository access, deployment credentials, provider dashboards, password manager, email.

Five measures, none of which takes long, and all of which a customer's security questionnaire eventually asks about.

**Full disk encryption**, which is a setting on every current operating system and turns a stolen laptop from an incident into an inconvenience.

**A password manager** with unique credentials per service, and multi-factor authentication on everything that offers it — starting with your repository host, your hosting platform, your database provider and your domain registrar, because those four are the keys to the product.

**Automatic operating system and browser updates**, since the realistic threat to a founder's laptop is ordinary malware rather than anything targeted.

**Separate accounts or profiles** for work and everything else, which limits what a compromised browser session reaches.

**A backup of the machine itself**, so the laptop failing on a Tuesday is not also a data loss event.

This is unglamorous and it is the honest answer to a question that sits underneath everything in this article: the most likely way your customers' data is exposed is not a subtle flaw in your application, and not a model provider's retention policy. It is the device where all of your access lives.

## Setting This Up

For a founder using an AI editor this is typically half a day: privacy and retention settings confirmed rather than assumed, an ignore file covering environment files, keys, dumps and exports, production data kept outside the project directory and preferably off the machine entirely, seeded data used for development, a redaction habit before pasting with an absolute rule against pasting keys, the processing location recorded, business tier terms evaluated if you have customer obligations, and a written position on whether your tooling touches customer data.

LaunchStudio covers development environment practices as part of preparing a product for business customers, where the question arrives in procurement. Behind it is Manifera — eleven years, 120+ engineers, clients including Vodafone, TNO and CFLW.

[Ask us what your development setup would look like to a customer's auditor](https://launchstudio.eu/en/#contact).

## Real example

### A Database Export in the Project Folder

Marnix Bouwhuis built Debiteurenbeheer in Cursor: receivables and payment reminder administration for accountancy offices, 29 offices managing around 18,000 debtors on behalf of their clients.

Debugging a reconciliation problem, he had exported a production table to a CSV file and left it in the project directory, where it stayed for four months. The editor's project index included it, and he had twice pasted rows from it into a conversation to ask why amounts were not matching.

The data was names, addresses, outstanding amounts and payment histories of businesses that were his customers' customers — data he processed as a processor, under agreements that named his subprocessors and did not include any AI tooling.

He found it while preparing answers for an accountancy group's audit.

Two business days: the export deleted and a rule adopted that production data never enters the project directory; an ignore file covering environment files, key material, exports and dumps; editor privacy settings confirmed with retention disabled, and a business tier taken for the contractual terms it provides; a seeded development dataset built with realistic shape so production data is not needed for ordinary work; a documented procedure for the cases where a customer's data genuinely must be reproduced — minimum extract, anonymised, deleted afterwards, recorded; a redaction habit adopted with an absolute rule against pasting credentials; a written assessment concluding that the four-month period constituted processing by an undeclared subprocessor, which was disclosed to the affected offices with a description of the remediation; and the provider's data handling terms filed with the subprocessor documentation.

**Result:** the accountancy group accepted the disclosure and proceeded, which Marnix attributes to having found it himself and explained it fully rather than being asked. He notes that the seeded dataset removed the reason he had been exporting production data in the first place.

> *"The file sat in my project for four months and I pasted rows from it twice. Nothing was hacked. I had simply sent my customers' customers' data to a company nobody had agreed to."*
> — **Marnix Bouwhuis, Founder, Debiteurenbeheer (Amersfoort)**

**Cost & Timeline:** €2,400 (data removal and project hygiene rules, ignore file, editor privacy configuration and business tier, seeded development dataset, reproduction procedure, redaction practices, disclosure assessment and documentation) — completed in 2 business days.

## Frequently Asked Questions

### What does an AI editor send to the model?

The file you are working on, files it judges relevant, often an index of the whole project, and anything you paste into a conversation. The last is where customer data usually appears.

### Is my code used for training?

Most editors have a privacy mode that prevents retention and training. Turn it on and confirm what the setting actually promises rather than relying on its name.

### Should I add an ignore file?

Yes — covering environment files, key material, database dumps and exports. Better still, keep production data outside the project directory entirely so no indexing decision can reach it.

### Is my AI editor a subprocessor?

Only if it processes your customers' personal data. Working against seeded data, it processes your code, which is yours. Routinely pasting production rows makes it one, and the fix is to stop rather than to declare it.

### What if I have pasted a key?

Rotate it. Generate a replacement, deploy it, revoke the old one, and then review whether it was used. Removing it from the conversation changes nothing.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What does an AI editor send to the model?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The open file, related files, often a project-wide index, and anything you paste — the last being where customer data usually appears."
      }
    },
    {
      "@type": "Question",
      "name": "Is my code used to train models?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most editors offer a privacy mode preventing retention and training. Enable it and verify what the setting actually commits to."
      }
    },
    {
      "@type": "Question",
      "name": "Should I use an ignore file with an AI editor?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, for environment files, keys, dumps and exports — and keep production data outside the project directory entirely."
      }
    },
    {
      "@type": "Question",
      "name": "Is an AI editor a subprocessor under my customer agreements?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Only if it processes customers' personal data. Against seeded data it processes your own code; pasting production rows makes it one."
      }
    },
    {
      "@type": "Question",
      "name": "What should I do if I pasted an API key?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Rotate it — generate a replacement, deploy, revoke the old one, then check provider logs. Deleting the conversation changes nothing."
      }
    }
  ]
}
</script>
