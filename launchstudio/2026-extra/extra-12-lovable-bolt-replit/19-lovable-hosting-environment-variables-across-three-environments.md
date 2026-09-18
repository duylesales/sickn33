---
Title: "Lovable Hosting: Environment Variables Across Three Environments"
Keywords: lovable hosting, environment variables, secrets management, staging configuration, build-time variables, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Hosting: Environment Variables Across Three Environments

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Hosting: Environment Variables Across Three Environments",
  "description": "Configuration is where AI-built apps leak keys and break deploys. Which variables are public by design, how to keep development, staging and production apart, and what to do when a secret gets into the bundle.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-21",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-hosting-environment-variables-across-three-environments" }
}
</script>

Two failures account for most configuration incidents in AI-built products, and they are opposites.

The first: a secret that was supposed to stay on the server ends up in the JavaScript sent to browsers, where anyone can read it. The second: a variable that should have been set in production was not, so the deploy succeeded and the feature silently did nothing — emails not sent, payments not captured, errors not reported.

Both come from the same root. Configuration was set up once, in a hurry, by pasting values wherever the tool asked for them, and nobody has looked at it since.

## Public and Secret Are Not the Same Word

Modern frontend frameworks distinguish variables that get compiled into the browser bundle from those that stay on the server, and they do it with a naming prefix. In Vite-based projects — which is what Lovable produces — anything beginning `VITE_` is public. In Next.js it is `NEXT_PUBLIC_`.

Public does not mean "visible to logged-in users". It means compiled into a file anybody can download and read, forever, in every copy of that build.

The rule that follows is absolute: if a value must not be known by your users, it must not have a public prefix, and it must not be referenced in code that runs in the browser. No exceptions, no "it is only a test key", no "nobody would look".

Some values are public by design and that is fine. A Supabase anonymous key is meant to be in the browser — its safety comes from row-level security, not from secrecy. A Stripe publishable key is public by definition. Analytics identifiers, the application's own URL, feature flags: all public, all harmless.

What must never be public: the Supabase service role key, any payment provider secret key, database connection strings, email provider credentials, webhook signing secrets, and any API key for a service that charges by usage.

## The Service Role Key Deserves Its Own Paragraph

Among all the secrets an AI-built Supabase application handles, one is categorically worse to leak.

The service role key bypasses row-level security entirely. Whoever holds it can read, modify and delete every row in your database, regardless of any policy you have written. It is not a key with elevated permissions; it is a key with all permissions.

It appears in frontend code with some regularity, because an AI session hit a permissions error, and using that key made the error go away. The result works perfectly and is catastrophic.

Check for it specifically: search your repository for the variable name, search your built output, and open your deployed site's JavaScript and search there too. Finding it means rotating the key and assuming the old one is compromised.

## Three Environments, Three Sets of Values

Every environment needs its own complete set: development on your machine, staging, production.

Development values come from a local file that is never committed. Staging and production values live in your hosting platform's configuration, entered once, and ideally visible to as few people as possible.

What matters is that they are genuinely separate. A staging environment using production's database is not a staging environment. A staging environment using production's email credentials will eventually email your customers. A staging environment using production's payment keys will eventually charge someone.

Where a service has no test mode, staging gets no credentials at all and the code handles their absence gracefully. Absent credentials fail loudly and harmlessly; borrowed production credentials fail quietly and expensively.

## Commit an Example, Never a Value

The file listing which variables exist belongs in your repository. The values do not.

An `.env.example` with every variable name, a comment explaining what each is for, and either a placeholder or an obviously fake value is one of the highest-value files a project can have. It tells a new developer — or you in eight months — exactly what must be set, which is the information that is otherwise locked in one person's memory.

Alongside it, a check at startup that every required variable is present and fails immediately if not. The alternative is a deploy that succeeds and a feature that does not work, discovered by a customer a fortnight later.

And confirm your ignore rules actually cover the local file. Secrets committed to a repository stay in its history after deletion, which is why the correct response to finding one is to rotate the credential rather than to remove the file.

## Build Time Versus Run Time

A subtlety that produces baffling behaviour: public variables are baked in when the application is built, not read when it runs.

Change one in your hosting dashboard and nothing happens until you rebuild. Founders change a value, reload, see the old behaviour, and conclude that the platform is broken or the cache is stale.

Server-side variables are read at run time and take effect on the next invocation. So the same dashboard contains two kinds of setting that behave differently, and knowing which is which saves an afternoon roughly once a quarter.

The practical habit: after changing any public variable, trigger a rebuild and verify in the deployed output rather than assuming.

## Preview Deployments Need Thought

Platforms that build a preview for every branch are a genuine productivity gain and a quiet exposure.

Those previews inherit environment variables, which can mean a branch built from an outside contribution runs with credentials you would not hand out. And previews are frequently public URLs, indexed by search engines, containing whatever data their environment points at.

Two settings fix it: previews get their own non-production values, and they are protected from public access and from indexing. Both take minutes and neither is on by default in most setups.

## When a Key Has Leaked

Assume any secret that has been in a public bundle, a repository, a screenshot or a support ticket is compromised, regardless of how briefly.

The sequence is: rotate the credential at the provider first, so the old one stops working; deploy the new value; then look at what the old one could have reached and whether it was used, which most providers can tell you from their logs. Removing the key from your code is part of the fix, not the fix itself — copies of your build and your repository history persist.

Then close the route that put it there, because a key leaked once through frontend code will be leaked again by the next session that hits the same permissions error.

## Who Can Change Production, and How You Would Know

Configuration is a category of change that bypasses every safeguard you have built around code. There is no review, no test run, no deployment record — someone edits a field in a dashboard and the behaviour of your product changes, immediately, everywhere.

For a solo founder that is acceptable, provided the risk is understood. As soon as a second person has access, it deserves two small controls.

The first is a record. Most platforms log configuration changes; find that log once, know where it is, and check it when something inexplicable starts happening. A large share of "nothing changed and it broke" incidents are a variable that somebody changed with good intentions.

The second is a list of who holds access, reviewed when people join or leave. A contractor given dashboard access for a week in spring generally still has it in autumn, and dashboard access is usually access to every secret the product holds. Removing it is a two-minute task that nobody ever schedules.

One more habit worth the effort: when you change a production value, write down what and why, in the same place you note deploys. Configuration drift — the gradual divergence between environments as values are changed in one and not another — is invisible until it causes a bug that reproduces nowhere, and a dated list of changes is the fastest route back.

## Setting This Up

For an existing product this is typically half a day: every variable classified as public or secret with the naming enforced, the built output and deployed JavaScript searched for anything that should not be there, leaked credentials rotated, three complete environment sets established with no shared credentials between them, an example file committed with a startup check for required variables, ignore rules verified, preview deployments given their own values and protected from public access, and a short note recording where each value comes from and who can change it.

LaunchStudio does this as part of production readiness, and the bundle search in particular finds something more often than not. The engineers are Manifera's — eleven years, 120+ engineers, clients including Vodafone, TNO and CFLW.

[Ask us to search your deployed bundle](https://launchstudio.eu/en/#contact). It takes five minutes.

## Real example

### A Key in the Bundle Since March

Jelmer Ottevanger built Inkoopportaal with Lovable: a purchasing portal where 19 wholesalers publish price lists and around 300 retailers place orders.

Early in the build an AI session had hit a row-level security error while writing an admin report. The fix it produced used the Supabase service role key, and because the report ran in the browser, the key was given a public prefix. The report worked. The key had been in every JavaScript bundle served from the site since March.

Jelmer found it in September, while reading an article much like this one, by opening his own site's source and searching for the variable name.

One business day, starting the same evening: the service role key rotated immediately at Supabase, before anything else; the admin report rewritten as a server-side function with proper authorisation, using the anonymous key and policies like the rest of the application; the entire deployed bundle searched for the other secrets, which found an email provider key that had arrived the same way; both credentials rotated and access logs reviewed with Supabase support, showing no unexpected usage patterns in the period; three complete environment sets separated, since staging had been sharing production's database and email credentials; an example file committed with a startup check for eleven required variables; preview deployments given their own values and put behind access protection; and a pre-deploy check added that scans the built output for known secret patterns and fails the build.

**Result:** no evidence the key had been used, which Jelmer describes as luck rather than a result. The build-time scan has since blocked one further attempt to reference a server-side key from browser code, in a session six weeks later that had made exactly the same mistake for exactly the same reason.

> *"It worked, so I never looked at it again. The key that can read every wholesaler's pricing had been sitting in a file anyone could download for six months."*
> — **Jelmer Ottevanger, Founder, Inkoopportaal (Zwijndrecht)**

**Cost & Timeline:** €1,700 (credential rotation, admin report rewrite, bundle audit, environment separation, example file and startup validation, preview protection, automated secret scanning in the build) — completed in 1 business day.

## Frequently Asked Questions

### Which variables are safe to expose to the browser?

Supabase anonymous keys, payment publishable keys, analytics identifiers, your own URLs and feature flags. Never service role keys, payment secret keys, database URLs, email credentials or webhook signing secrets.

### How do I check whether a secret is in my bundle?

Open your deployed site's JavaScript and search for the variable name or the value. Also search your repository and your built output locally. It takes minutes.

### Why did changing a variable not take effect?

Public variables are compiled in at build time, so they need a rebuild. Server-side variables are read at run time and apply on the next invocation.

### What do I do if a key has leaked?

Rotate it at the provider first, then deploy the new value, then review the provider's logs for use of the old one. Removing it from your code is not sufficient — copies persist in history and in old builds.

### Do preview deployments need separate configuration?

Yes. They inherit variables by default, and preview URLs are often public and indexable. Give them non-production values and put them behind access protection.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Which environment variables are safe to expose to the browser?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Supabase anonymous keys, publishable payment keys, analytics ids, your own URLs and feature flags — never service role keys, secret keys, database URLs or webhook secrets."
      }
    },
    {
      "@type": "Question",
      "name": "How do I check whether a secret is in my JavaScript bundle?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Open the deployed site's JavaScript and search for the variable name or value, and search your repository and local build output too."
      }
    },
    {
      "@type": "Question",
      "name": "Why did changing an environment variable have no effect?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Public variables are baked in at build time and need a rebuild; server-side variables are read at run time."
      }
    },
    {
      "@type": "Question",
      "name": "What should I do if an API key has leaked?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Rotate it at the provider first, deploy the new value, then review provider logs for use of the old key. Deleting it from code is not enough."
      }
    },
    {
      "@type": "Question",
      "name": "Do preview deployments need their own configuration?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — they inherit production variables by default and their URLs are often public and indexable. Give them separate values and access protection."
      }
    }
  ]
}
</script>
