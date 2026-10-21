---
Title: "Lovable Hosting: Feature Flags and Releasing to Some Customers First"
Keywords: lovable feature flags, staged rollout, kill switch, beta programme, release management, Supabase, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Hosting: Feature Flags and Releasing to Some Customers First

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Hosting: Feature Flags and Releasing to Some Customers First",
  "description": "Deploying code and releasing a feature do not have to be the same moment. How feature flags let you ship to a few customers first, switch off a broken or expensive feature in seconds, and run a beta programme — and how to keep flags from becoming a mess.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-21",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-hosting-feature-flags-and-releasing-to-some-customers-first" }
}
</script>

In most AI-built products, deploying and releasing are the same event. The code goes live, and every customer sees the new feature at the same moment. If it works, nobody notices the risk that was taken. If it does not — a calculation that is wrong for one kind of customer, a screen that fails on the data of the largest account, an integration that overwhelms a supplier — every customer meets the problem at once, and the only remedy is a rollback that takes everything else in the release with it.

Feature flags separate the two. Code is deployed whenever it is ready, switched off. The feature is then released deliberately: first to you, then to a few friendly customers, then to a percentage, then to everyone — with the ability to switch it off again in seconds, without a deployment, if something goes wrong.

For a small product this sounds like enterprise machinery. It is not. A table, a function and a few habits give most of the benefit, and they change how comfortable releasing feels more than almost any other practice. This article covers the kinds of flags, a simple implementation on Supabase, staged rollouts, kill switches, the difference between flags and plans, and the discipline that keeps flags from becoming permanent clutter.

## Four Kinds of Flag

The word covers several different tools, and treating them as one is how flag systems become confusing.

**Release flags** hide a feature until it is ready and control its rollout. They are temporary: once the feature is released to everyone, the flag and the old code path are removed. Most flags should be this kind.

**Kill switches** turn off something that already works — an AI feature, an outbound integration, an expensive report, SMS reminders — when it misbehaves, costs too much, or depends on a supplier that is having an outage. They are permanent and should be tested regularly, like a fire alarm.

**Customer flags** enable something for specific organisations: a feature built for one large customer, an early-access programme, a configuration only some customers need. They can be long-lived, and they shade into the next category.

**Entitlements** decide what a customer has paid for — plan limits, premium modules. They look like flags but are not; they belong to billing, as discussed below.

Name each flag with its kind — `release.online_booking`, `kill.ai_recall_suggestions`, `customer.bulk_import_v2` — so anyone reading the code knows how long it is meant to live.

## A Minimal Implementation

For a Supabase product, two tables and one function cover most needs.

```sql
create table feature_flags (
  key text primary key,
  description text not null,
  kind text not null check (kind in ('release', 'kill', 'customer')),
  enabled boolean not null default false,       -- global default
  rollout_percent int not null default 0 check (rollout_percent between 0 and 100),
  owner text not null,
  expires_on date,                              -- required for release flags
  updated_at timestamptz not null default now()
);

create table feature_flag_overrides (
  flag_key text references feature_flags(key) on delete cascade,
  organisation_id uuid references organisations(id) on delete cascade,
  enabled boolean not null,
  primary key (flag_key, organisation_id)
);
```

Evaluation follows a fixed order: an explicit override for the organisation wins; otherwise the organisation is included if it falls within the rollout percentage; otherwise the global default applies.

```ts
function isEnabled(flag: Flag, orgId: string, overrides: Map<string, boolean>): boolean {
  const override = overrides.get(orgId);
  if (override !== undefined) return override;
  if (flag.rollout_percent > 0 && bucket(flag.key, orgId) < flag.rollout_percent) return true;
  return flag.enabled;
}

// Stable bucket 0–99: the same organisation always lands in the same bucket for a flag.
function bucket(flagKey: string, orgId: string): number {
  return parseInt(sha256(flagKey + ':' + orgId).slice(0, 8), 16) % 100;
}
```

Two details matter. Roll out by organisation rather than by user, so colleagues in the same company see the same product — nothing generates confused support tickets faster than two people at one customer seeing different screens. And use a stable hash, so increasing the percentage from 10 to 25 adds organisations without removing any that already had the feature.

Load the flags once per request or cache them for a short period — thirty to sixty seconds — rather than querying for every check. A kill switch that takes a minute to take effect is fine; one that requires a deployment is not.

## Evaluate on the Server

Flags can be evaluated in the browser or on the server, and the difference matters.

A flag evaluated only in the frontend hides a button. It does not prevent the endpoint behind the button from working, and anyone can call that endpoint directly, as the admin panel and IDOR articles in this series describe. Every flag that guards behaviour — not only appearance — must be checked on the server as well: in the edge function, in the RPC, or in a row level security policy if it controls access to data.

Evaluated in the browser, flags also reveal what is coming. A list of every flag and its state, sent to every client, tells competitors and curious customers about unreleased features. Send the client only the evaluated results it needs for the current organisation, not the full configuration.

The rule: a flag is never a security boundary. It controls when something is released, not who is allowed to do it. Who is allowed is the job of permissions.

## Staged Rollouts in Practice

A release with flags typically follows the same sequence.

1. **Deploy dark.** The code is in production, the flag is off for everyone. Nothing changes for customers.
2. **Internal.** Enable it for your own organisation and use it on real infrastructure.
3. **Beta customers.** Enable it for a handful of organisations who have agreed to see new features early and tell you what breaks — ideally including one of your largest accounts, because large accounts find the problems small ones never trigger.
4. **Percentage.** 10%, then 25%, then 50%, over days rather than minutes, watching error rates, performance and support messages at each step.
5. **Everyone.** The flag is on globally.
6. **Clean up.** Within a few weeks, remove the flag and the old code path.

The monitoring at step four is what makes the percentages meaningful. Tag errors and slow requests with the flags that were active, so that "errors increased after the rollout went to 25%" is visible in the logs article's tooling rather than inferred from a feeling.

Not every change needs every step. A copy change needs none. A new calculation, a new integration, a redesigned workflow or anything touching money deserves the full sequence.

## Kill Switches for the Things That Can Hurt You

Some features are valuable and risky: they cost money per use, depend on an external supplier, or affect people outside your product. Each of these should have a kill switch from the day it is built.

**AI features** — when the model provider has an outage, when costs spike because of a loop or abuse, or when output quality drops. The AI cost and evaluation articles in this series describe the failure modes.

**Outbound messages** — SMS, email campaigns, WhatsApp notifications — when a bug sends too many or to the wrong people.

**Integrations** — accounting sync, payment provider calls, a customer's webhook — when the other side is failing and your retries are making it worse.

**Expensive background work** — large reports, bulk recalculations — when they threaten the database at a busy moment.

A kill switch should switch the feature off cleanly: the interface explains that the feature is temporarily unavailable, queued work waits rather than failing, and nothing is half-done. Test each kill switch periodically — switch it off and on in a quiet hour — because a switch nobody has used is a switch nobody knows works.

## Flags Are Not Plans

The most common design mistake is to implement pricing with feature flags: a flag per premium feature, switched on for paying customers by hand.

It works for three customers and fails at thirty. Nobody can see which customer has paid for what, upgrades and downgrades require manual flag changes that are forgotten, and the flag table becomes a second, unreliable billing system.

Keep them separate. Entitlements are derived from the customer's subscription — plan, add-ons, limits — as the subscription and trial articles in this series describe, and checked by an entitlement function. Feature flags control the release of features, independent of what anyone has paid. A new premium feature typically needs both: the flag decides whether the feature is released yet, the entitlement decides whether this customer has bought it.

## Flags and Database Changes

Flags make the application switchable; they do not make the database switchable. A feature that requires a new column or table needs that change in place before the flag is turned on for anyone, and it must keep working whether the flag is on or off.

This is the expand-and-contract pattern from the zero-downtime deploy article in this series: add the new structure alongside the old, have the code write to both while the flag is in rollout, switch reads behind the flag, and remove the old structure only after the flag has been retired. Turning a flag off must never leave data the old code cannot read.

## Keep Flags From Becoming Debt

Every flag doubles the number of paths through a piece of code. Ten flags in one area means that area can behave in more ways than anyone has tested. Flag systems fail not because of the mechanism but because flags are never removed.

Four habits prevent it.

**Every release flag has an owner and an expiry date**, enforced by the table. A check in CI or a weekly report lists flags past their expiry.

**Removing the flag is part of the feature.** The task is not finished until the flag and the old path are deleted. Put it on the list when the flag is created.

**Limit the number of active release flags.** If there are more than a handful, the team is starting more than it finishes.

**Record every change** — who switched which flag for whom, and when — in the audit log, and show recent changes next to error graphs. "The errors started when someone turned this on for 50%" should take seconds to see.

## Testing Both Paths

While a flag exists, both paths are production code and both need tests. Run the relevant tests with the flag on and off, at least for release flags that touch money, permissions or data.

For kill switches, test the off state specifically: the feature is unavailable, the interface says so, queued work is preserved, and nothing errors.

And remove the tests for the old path along with the flag, so the suite does not keep testing behaviour that no longer exists.

## Telling Customers What Changed

A staged rollout creates a communication question that an all-at-once release does not: at any moment, some customers have a feature and others do not.

Three practices keep that from becoming confusing.

**Announce at the moment a customer receives the feature, not when it is deployed.** An in-product notice driven by the same flag — "New: book online from your website" — appears only for organisations where the flag is on. Release notes on your site describe features that are available to everyone, with beta features labelled as such.

**Prepare support before the first percentage.** The people answering customer questions — often the founder — need to know which organisations have which features. A small panel in your admin view showing the active flags for an organisation answers "why does my colleague at the other branch see something I do not?" in seconds.

**Give administrators a choice for disruptive changes.** A redesigned workflow that changes how staff work every day is easier to accept if the customer's administrator can switch to it at a moment that suits them — within a window, after which it becomes the default. Implemented as a customer-controlled override on the release flag, it costs little and converts resistance into planning.

Done this way, a staged rollout is not only safer; it is noticeably better received, because customers experience new features as something arriving deliberately rather than something that happened to them overnight.

## Build or Buy

The minimal implementation above is enough for most small products, and it has the advantage of living in your own database, close to your organisations and permissions.

Dedicated tools — Unleash and Flagsmith, both available self-hosted or in EU regions, PostHog's feature flags if you already use it for analytics, LaunchDarkly at the enterprise end — add an interface for non-developers, richer targeting, experiment analysis and SDKs. They become worth it when several people manage releases, when you run experiments that need statistics, or when the number of flags grows beyond what a table and a short admin page handle comfortably. If you use one, it receives organisation identifiers and possibly user attributes, which makes it a subprocessor to list, as the subprocessors article in this series describes.

## A Beta Programme Customers Value

Flags make a beta programme easy to run, and a beta programme is worth more than the risk reduction alone.

Invite customers who like being early — usually a mix of enthusiastic small accounts and one or two larger ones — and give them an explicit agreement: they see features before others, they tell you what is wrong, and they accept that things may change. Mark beta features visibly in the interface. Ask for feedback at a specific moment rather than in general.

Customers in a beta programme tend to become the product's strongest references, because they helped shape it. And features released to them first arrive at everyone else with the rough edges already found.

## Setting This Up

For a Lovable or Supabase product, this is typically two to three days: a flag table with kinds, owners and expiry dates, per-organisation overrides, server-side evaluation with stable percentage bucketing and short caching, only evaluated results sent to the client, flags never used as security boundaries, a release sequence from dark deploy through internal, beta and percentages to everyone, errors and performance tagged with active flags, kill switches for AI features, outbound messages, integrations and heavy jobs with clean off states tested periodically, entitlements kept separate from flags, expand-and-contract for database changes behind flags, an audit log of flag changes, a report of expired flags, tests for both paths, and a small beta programme with visible beta labels.

LaunchStudio sets this up as part of making releases routine for products whose customers rely on them every day. The engineers are Manifera's — eleven years, 120+ engineers, 160+ projects, from Amsterdam and Ho Chi Minh City.

[Ask us how to release your next feature to three customers first](https://launchstudio.eu/en/#contact).

## Real example

### Double-Booked Dental Chairs on a Monday Morning

Evelien Hartman built Tandartsplanner in Lovable: appointment scheduling, recall reminders and online booking for dental practices, used by 58 practices.

A new online booking widget — patients booking directly from a practice's website — was released on a Monday morning to every practice at once. For practices that used split chairs, where one dental chair is shared between a dentist and a hygienist in the same hour, the widget's availability calculation was wrong. Within three hours, eleven practices had double-booked chairs, and receptionists were phoning patients to move appointments.

Switching the widget off meant a rollback. The release also contained a migration and two unrelated fixes, so the rollback took the morning, during which online booking was unavailable everywhere. The same month, an AI feature that suggested which patients to recall had a cost spike when a loop called the model repeatedly, and there was no way to stop it without deploying.

Three business days: a feature flag table with kinds, owners and expiry dates, with per-practice overrides and stable percentage rollout; flags evaluated on the server in the booking and recall functions, with only evaluated results sent to the browser; kill switches for the AI recall suggestions, SMS reminders and the online booking widget, each with a clean unavailable state; a beta group of six practices — including the two largest and two that used split chairs — that agreed to receive features first; errors and slow requests tagged with active flags in the logs; an audit of flag changes visible in the admin page; a weekly report of release flags past their expiry date; and tests for the booking calculation with the new widget's flag on and off.

**Result:** the corrected widget was released through the beta group, then 25%, then everyone, over two weeks without a double booking. In the following six months nine features went out the same way; one problem in a new invoicing screen was caught at three practices and switched off in under a minute. When the model provider had a two-hour outage, the AI kill switch was turned on and practices saw a clear message instead of errors.

> *"Releasing to all fifty-eight practices at once meant eleven of them found the bug for us before ten o'clock. Now six practices find it, and I switch it off before the others even see it."*
> — **Evelien Hartman, Founder, Tandartsplanner (Leiden)**

**Cost & Timeline:** €2,800 (flag table with overrides and percentage rollout, server-side evaluation, kill switches for AI, SMS and booking with clean off states, beta programme setup, flag-tagged error logging, flag change audit, expiry reporting, dual-path tests) — completed in 3 business days.

## Frequently Asked Questions

### What is a feature flag?

A switch that controls whether a feature is active, for everyone or for specific customers, without deploying new code. It separates deploying code from releasing a feature.

### Do small products need feature flags?

Most benefit from a minimal version: a table, per-organisation overrides, server-side checks and kill switches for risky features. It takes a few days and makes releases far less risky.

### Can a feature flag protect a feature from unauthorised use?

No. Flags control release, not authorisation. Anything a flag hides in the interface must also be checked on the server, and who may use it is decided by permissions.

### Should I use flags for paid features?

Not as the billing mechanism. Entitlements come from the subscription; flags control whether a feature is released yet. A premium feature typically checks both.

### How do I stop flags piling up?

Give every release flag an owner and an expiry date, make removing the flag part of finishing the feature, limit active release flags and report expired ones automatically.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is a feature flag?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A switch that turns a feature on or off for everyone or specific customers without a deployment, separating deploy from release."
      }
    },
    {
      "@type": "Question",
      "name": "Do small SaaS products need feature flags?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A minimal version — a table, per-organisation overrides, server checks and kill switches — makes releases much safer for a few days of work."
      }
    },
    {
      "@type": "Question",
      "name": "Is a feature flag a security control?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — flags control release, not authorisation. Check flagged behaviour on the server and use permissions for access."
      }
    },
    {
      "@type": "Question",
      "name": "Should feature flags implement pricing plans?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — entitlements come from the subscription; flags only decide whether a feature is released. Premium features check both."
      }
    },
    {
      "@type": "Question",
      "name": "How do I prevent feature flag debt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Give release flags owners and expiry dates, remove them as part of the feature, limit how many are active, and report expired ones."
      }
    }
  ]
}
</script>
