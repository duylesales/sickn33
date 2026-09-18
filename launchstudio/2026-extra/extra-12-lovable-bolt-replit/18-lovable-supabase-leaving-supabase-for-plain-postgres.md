---
Title: "Lovable Supabase: Leaving Supabase for Plain Postgres"
Keywords: lovable supabase, migrating off Supabase, managed Postgres, auth migration, vendor lock-in, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Scale-Up
---

# Lovable Supabase: Leaving Supabase for Plain Postgres

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Leaving Supabase for Plain Postgres",
  "description": "When a product outgrows Supabase, what actually has to move: the database is easy, auth and storage are not. The honest reasons to leave, the reasons that are not reasons, and the order that works.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-19",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-supabase-leaving-supabase-for-plain-postgres" }
}
</script>

Let us begin with the recommendation, because most articles on this subject bury it: for the overwhelming majority of products built with Lovable, staying on Supabase is the right decision, and the migration being contemplated is a solution to a problem that has a cheaper fix.

That said, some products do outgrow it, and the ones that do are better served by understanding what the move actually involves than by discovering it half-way through. The database is the easy part. Everything built around the database is the work.

## The Reasons That Are Not Reasons

Four motivations come up repeatedly and none of them survives examination.

**"It is getting expensive."** Compare honestly. Supabase's bill covers a managed database, authentication, storage, an API layer and backups. Replacing it with a managed Postgres instance plus an auth service plus object storage plus the engineering time to wire them together is frequently more expensive, and always more expensive when you count the maintenance.

**"Performance is bad."** Almost always missing indexes, N+1 queries or connection mismanagement. Those problems move with you. A product that is slow on Supabase will be slow on anything else, at greater cost.

**"We might get locked in."** Supabase is Postgres. Your data, schema, functions and triggers are standard and portable. The lock-in is real only in auth, storage and realtime — and it is modest even there.

**"Investors asked about scale."** Supabase runs products considerably larger than yours. If the question needs an answer, the answer is a capacity plan, not a migration.

## The Reasons That Are Real

Three, and they are all structural rather than technical annoyances.

**A regulatory or contractual requirement about where data lives or who operates it.** A public-sector customer, a healthcare contract, or an enterprise procurement demanding a specific region, provider or certification that you cannot satisfy on your current plan. This is the most common genuine reason and it usually arrives attached to a large contract.

**A scale or workload the platform is not shaped for.** Very heavy write volume, large analytical workloads alongside transactional ones, or a need for Postgres extensions and configuration the managed environment does not offer.

**A deliberate architectural consolidation.** You already run substantial infrastructure elsewhere, and having the database next to it — same network, same monitoring, same team — is simpler overall. This is a real reason and it applies to fewer small products than believe it does.

## What Moves Easily

The database itself is genuinely straightforward. It is Postgres: dump it, restore it, verify the row counts. Your schema, indexes, constraints, functions and triggers all come across.

Two caveats. Supabase installs a handful of extensions, some of which you may be using without knowing — check before assuming the target supports them. And row-level security policies come across, but they reference the identity of the calling user, which after the move is no longer supplied by Supabase's auth. Those policies need rewriting against whatever mechanism replaces it.

Budget a day for this part, most of which is verification rather than transfer.

## What Does Not Move Easily

**Authentication is the hard part.** Password hashes can usually be exported and imported, so users need not reset passwords — but the tokens your application issues change format, every session is invalidated at cutover, and anything depending on the identity claim inside those tokens must be rewritten. That includes every row-level security policy, which is why the two pieces of work are really one.

Social logins have to be re-established with each provider, and the redirect URLs updated. Users who signed up with Google keep their account only if you match them on email, which needs care to avoid merging two people who share one.

**Storage is a copy plus a rewrite.** Moving the objects is a script. The work is in every place your application generated a Supabase URL, every signed URL mechanism, every upload path, and every permanent link already sent to a customer.

**Realtime has no drop-in equivalent.** If your product depends on live updates, that is a component you are now building or buying.

**Edge functions are ordinary code** and port easily, but their deployment, secrets and invocation all change.

## The Order That Works

Do it in stages with the product running throughout. Everything at once is how a weekend becomes a week.

First, move the database and point the application at the new one during a short maintenance window. Keep auth and storage where they are — Supabase auth can continue to work against a database you no longer host, which is the property that makes a staged migration possible at all.

Second, migrate authentication. This is the cutover with user-visible effect: sessions end, everyone signs in again. Do it at a low-traffic hour, communicate beforehand, and have a tested route back.

Third, migrate storage, with a period where your application reads from both locations so nothing breaks while objects are copied.

Finally, remove the remaining dependencies and close the account — after a decent interval, with a verified backup taken first.

## Before You Commit

Two pieces of work are worth doing before deciding, and both have value even if you stay.

Run a full restore test on your current setup. A product whose team has never restored a backup is not ready to migrate anything, and the exercise frequently reveals that recovery does not work as assumed.

And rehearse the migration on a copy. Restore the database somewhere else, point a staging application at it, migrate a subset of users and objects, and time every step. The rehearsal tells you the real duration, finds the extension you did not know you used, and converts the cutover from an event into a repeat performance.

## The Middle Option Founders Miss

Between staying and leaving there is a third arrangement that resolves most of the genuine reasons: keep Supabase and change its shape.

Data residency requirements are frequently satisfied by a region change or a plan with different terms. Enterprise procurement questions are often about certifications and contractual commitments that exist on higher tiers. Extension and configuration needs sometimes resolve with a dedicated instance.

Ask before you migrate. A conversation with a vendor is cheaper than an engineering project, and the answer is surprisingly often that the thing you are about to spend three weeks building already exists as a setting.

## Reduce the Lock-In Without Moving

There is a set of changes that makes a future migration cheap, costs little, and improves your product whether or not you ever leave. If the question is on your mind, this is the work to do instead.

**Put the platform behind your own boundary.** Application code that calls the Supabase client everywhere is code where every file knows which vendor you use. The same code calling your own data functions — which happen to use Supabase inside — changes in one place if that ever changes. This is ordinary good structure, and it is the single largest determinant of migration cost.

**Own your identity model.** Keep your own users table with your own identifiers, linked to the auth provider's identity rather than keyed by it. Then swapping the provider changes one column, not every foreign key in the schema.

**Store file references, not URLs.** A database column holding a full Supabase URL is a column that must be rewritten at migration and that breaks in every email already sent. A column holding a path, with URLs generated at read time, is portable by construction.

**Keep migrations in your repository.** A schema that exists only in a dashboard cannot be recreated anywhere, which makes even a rehearsal impossible.

Do these four and the migration you are worrying about becomes a fortnight instead of a quarter — and in the far more likely event that you never migrate, you have a cleaner codebase and an easier product to hand to somebody else.

## Setting This Up

A staged migration for a small product is typically two to three weeks: a rehearsal on a copy with every step timed, database migration with extension and policy verification, an authentication cutover including password hash import, social login re-establishment and policy rewriting against the new identity source, storage copied with a dual-read period and existing links handled, realtime replaced if used, edge functions redeployed with their secrets, monitoring and backups established on the new platform with a restore actually tested, and the old environment retired after a verified interval.

LaunchStudio does both halves of this conversation — including telling founders not to migrate, which is the more common outcome. The engineers are Manifera's: eleven years, 160+ projects, infrastructure work for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City.

[Tell us why you are thinking about moving](https://launchstudio.eu/en/#contact). Half the time the answer is an index.

## Real example

### A Contract That Required a Different Answer

Gerlof Tichelaar built Zorgdossier in Lovable: care plan administration for small-scale residential care providers, 26 organisations, around 1,400 residents.

The migration was not his idea. A regional healthcare group offered a contract covering nine locations, and their procurement required that personal data be processed on infrastructure under a specific agreement with a named certification, in a specific region, with contractual terms his plan did not provide. The contract was worth more than his existing revenue.

He first asked Supabase, which is the step most founders skip, and part of the requirement was satisfiable on different terms. The region and certification were not, given his timeline.

Sixteen business days across three weeks: a full rehearsal on a copy, which found two extensions in use that the target did not enable by default and measured the real cutover at 40 minutes rather than the two hours assumed; the database migrated to managed Postgres in the required region, with row counts and constraint checks verified against the source; authentication moved with password hashes imported so no resident's carer had to reset anything, 31 row-level security policies rewritten against the new identity claim, and social login re-established for the two organisations using it; a two-week dual-read period for storage while 94,000 documents were copied, with previously issued links redirected rather than broken; realtime replaced with polling on the two screens that used it, after establishing that live updates were not clinically necessary; backups configured with a restore performed and timed; and the old project retired after a month with a verified archive.

**Result:** the contract was signed. Gerlof's monthly infrastructure cost rose from €85 to €310, which he describes as the least interesting number in the project. The rehearsal is the part he recommends to other founders: the 40-minute cutover happened at six on a Sunday morning and nobody noticed.

> *"I did not migrate because Supabase was not good enough. I migrated because a procurement department needed a specific answer, and that is the only reason I would do it again."*
> — **Gerlof Tichelaar, Founder, Zorgdossier (Leeuwarden)**

**Cost & Timeline:** €11,800 (rehearsal, database migration with extension and constraint verification, auth cutover with hash import and 31 policy rewrites, storage copy with dual-read and link redirection, realtime replacement, backup and restore verification, decommissioning) — completed in 16 business days.

## Frequently Asked Questions

### Is Supabase hard to leave?

The database is not — it is standard Postgres. Authentication, storage and realtime are the work, and authentication is the one with user-visible effect because every session ends at cutover.

### Will my users have to reset their passwords?

Not if password hashes are exported and imported, which is normally possible. They will be signed out at cutover and will need to sign in again.

### Is migrating cheaper than staying?

Usually not. Supabase's price covers a database, auth, storage, an API and backups; replacing those separately plus the engineering time is frequently more expensive to run and always more to maintain.

### My app is slow — will moving fix it?

Almost never. Slowness is usually missing indexes, N+1 queries or connection mismanagement, and those travel with you at higher cost.

### What should I do before deciding?

Ask the vendor whether your requirement is satisfiable on different terms, run a restore test on what you have, and rehearse the migration on a copy. All three are useful even if you stay.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is Supabase hard to migrate away from?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The database is standard Postgres and moves easily. Authentication, storage and realtime are the real work, with auth causing the only user-visible cutover."
      }
    },
    {
      "@type": "Question",
      "name": "Will users have to reset passwords after migrating?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Normally no — password hashes can be exported and imported. Everyone is signed out at cutover and must sign in again."
      }
    },
    {
      "@type": "Question",
      "name": "Is leaving Supabase cheaper?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually not. The bill covers database, auth, storage, API and backups; assembling equivalents separately costs more to run and to maintain."
      }
    },
    {
      "@type": "Question",
      "name": "Will migrating off Supabase fix performance?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Almost never. Missing indexes, N+1 queries and connection mismanagement travel with you and cost more to run elsewhere."
      }
    },
    {
      "@type": "Question",
      "name": "What should I do before deciding to migrate?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ask the vendor whether the requirement is satisfiable on other terms, test a restore of your current backups, and rehearse the migration on a copy."
      }
    }
  ]
}
</script>
