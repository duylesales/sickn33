---
Title: "Lovable Custom Domain: Migrating a Live Domain Safely"
Keywords: lovable custom domain, dns migration, ttl, registrar transfer, downtime, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Scale-Up
---

# Lovable Custom Domain: Migrating a Live Domain Safely

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Custom Domain: Migrating a Live Domain Safely",
  "description": "Moving a domain that customers already use is a different exercise from setting one up. TTL, the order of operations, keeping email working, and the callback URLs that lock people out.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-08",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-custom-domain-migrating-a-live-domain-safely" }
}
</script>

Pointing a fresh domain at a new product is a ten-minute job with no consequences. Moving a domain that hundreds of people already use is a different exercise entirely, because every mistake is visible to customers in real time and some of them are not reversible within the hour.

The situations are ordinary. You are changing hosting. You are consolidating a domain registered by a former freelancer. You are moving from one registrar to another after a bad support experience. Or you are switching a live product from a platform's address to your own for the first time.

None of it is difficult. All of it is unforgiving about order.

## What Can Actually Go Wrong

Worth being concrete, because it determines how carefully you sequence things.

**Your site becomes unreachable** for some visitors and not others, for a period you did not choose, because DNS answers are cached at every layer between your customer and you.

**Your email stops,** which is worse than the site being down and takes longer to notice. Moving a domain's DNS without carrying the mail records across is the single most damaging mistake in this process.

**Nobody can log in,** because your authentication provider's callback URLs still name the old address.

**Payments stop being recorded,** because your payment provider's webhook points at an address that no longer answers.

**Your rankings dip,** because search engines see one address replaced by another without the redirects that explain the relationship.

Five separate systems, each configured somewhere else, each perfectly happy to keep pointing at the old address indefinitely.

## Lower the TTL First

The single most useful preparation, and the one most often skipped.

Every DNS record carries a time-to-live: how long resolvers may cache the answer. If yours is set to a day and you change a record, some visitors will keep reaching the old address for a day, and you cannot make them stop.

So, several days before the move, lower the TTL on the records you will change to something short — a few minutes. Wait for the old, longer TTL to expire everywhere. Then, when you make the actual change, propagation is measured in minutes rather than a day, and if something is wrong you can revert equally fast.

Raise it again a week after the move. A short TTL means more lookups and slightly slower first responses; you want it short only for the window in which you might change your mind.

## The Order That Avoids Downtime

**One: inventory everything using this domain.** The site, the mail, the subdomains, the authentication callbacks, the webhooks, anything with the domain in a configuration file, and any third party you gave the address to. This list is the migration; missing entries are the incidents.

**Two: export the complete current DNS zone.** Every record, exactly as it is. This is your reference and your undo.

**Three: build the new environment and confirm it works** at a temporary address, before touching anything live. It should be serving your real application with real data before DNS changes at all.

**Four: recreate every record at the new provider before switching,** including mail records — SPF, DKIM, DMARC, and the mail exchange records themselves — so the new configuration is complete and waiting rather than being assembled under pressure.

**Five: update the callbacks and webhooks that accept multiple values.** Authentication providers and payment providers generally allow both old and new addresses to be registered simultaneously. Add the new one before the switch; remove the old one after. This alone converts two of the five failures above into non-events.

**Six: switch, at a quiet hour,** and watch. Not Friday evening. Early on a weekday morning, when you can respond.

**Seven: verify immediately** — the site on both www and bare versions, the certificate, a login, a test payment, and an email sent and received.

**Eight: clean up after a week,** removing the old callbacks and raising the TTL, but keeping the old address redirecting for as long as it costs nothing.

## Email Deserves Its Own Paragraph

Because it is where the serious damage happens.

Mail records are entirely separate from the records pointing at your site, and moving DNS to a new provider without carrying them across means mail silently stops being delivered. Senders receive rejections you never see; your customers assume you are ignoring them.

Carry the mail exchange records, SPF, DKIM and DMARC across exactly. Then, after the switch, send a test message from your product and from your own mailbox, to several different providers, and confirm both arrive and are authenticated. Check your provider's dashboard for authentication failures over the following days, because a partially correct configuration delivers most mail and quietly fails some.

## Transferring the Registrar Is a Separate Operation

Two things get conflated: changing where DNS is answered, and changing who the domain is registered with.

Changing DNS is fast and reversible. Changing registrar is a formal process involving an authorisation code, a confirmation, and typically several days — and many registrars lock a domain for a period after a transfer or a recent registration, which can prevent a second move.

Do not do both at once. Move DNS, confirm everything works, then transfer the registrar separately when nothing else is in flight. And check before you start whether the domain is locked or recently transferred, since discovering that mid-migration is how a planned morning becomes a planned fortnight.

For a `.nl` domain, the process has its own specifics; confirm current requirements with your registrar rather than assuming it matches a `.com`.

## Keeping Search Intact

If the address itself is changing — not just where it points — redirect every old address to its exact counterpart on the new domain, permanently, one hop, and keep those redirects live for years rather than months. Tell your search console about the move using its change-of-address facility. Update your sitemap and canonical tags. And expect a modest dip for a few weeks even when everything is right.

If only the hosting is changing and the addresses stay identical, none of this applies — which is a good reason to avoid changing both at once.

## The Verification List

After the switch: both www and bare versions resolve and one redirects to the other; the certificate is valid on every variant including subdomains; a real user can log in; a test payment completes and the webhook is recorded; email sends and arrives authenticated at several providers; scheduled jobs still run; no configuration file anywhere still names the old address; and your error tracker is quiet.

Run it deliberately rather than assuming. Most post-migration incidents are items from this list that nobody checked because the site loaded.

## Telling People, and the Addresses You Do Not Control

If the address itself is changing rather than only where it points, there is a second migration happening in places you cannot edit.

**Your customers' bookmarks and saved logins.** These follow redirects, so they keep working — provided the redirects stay live. Which is the argument for keeping the old domain registered and redirecting for years rather than months. Letting it lapse means somebody else can register it, and a domain your customers still type is not one to hand to a stranger.

**Links inside documents you already sent.** Invoices, reports, contracts, confirmation emails. Every one of those contains an address, and you cannot reissue them. Redirects are the only thing standing between those documents and a dead link.

**Integrations built by your customers.** A customer whose system calls your API at the old address will break unless you keep it answering. Tell them individually, with a date, and use your per-key usage data to see who has actually moved rather than trusting that they read the email.

**Things printed on physical objects.** Signage, vehicle livery, stickers on equipment, business cards. These are not updatable at all, which occasionally makes keeping the old domain a permanent commitment rather than a transitional one.

**Your own material.** Email signatures, social profiles, listings in directories, the address on your invoices. These are easy to update and the easiest to forget, and the ones you forget will quietly send people to a redirect for years.

**Announce it once, plainly, before the change** — what is changing, when, and that nothing they do will break. Then say it again in the product afterwards, briefly. Customers interpret an unannounced address change as instability, and a two-line notice converts it into competence.

## Doing It Without a Bad Morning

For a live product this is a planned, bounded exercise: everything using the domain inventoried, the zone exported, TTLs lowered in advance, the new environment stood up and verified before anything switches, every record including mail recreated ahead of time, callbacks and webhooks registered for both addresses across the change, the switch executed at a quiet hour with verification immediately afterwards, redirects and search console handled where addresses change, and the registrar transfer done separately once everything is stable.

LaunchStudio runs this for products with live customers, and the whole configuration is documented afterwards so the next change is yours to make. The engineers are Manifera's: eleven years of production migrations for clients including Vodafone, TNO and CFLW, from Amsterdam Herengracht 420 and Ho Chi Minh City.

[Tell us what your domain currently serves](https://launchstudio.eu/en/#contact) for a specific plan, usually within one business day, or see the [packages](https://launchstudio.eu/en/#packages).

## Real example

### The Site Moved and the Email Did Not

Vincent Bogaers built Taxatierapport with Lovable: property valuation reporting used by nineteen estate agents and four valuation firms around Bergen op Zoom and Roosendaal. Reports are produced in the product and emailed to clients and lenders.

He moved hosting and decided to consolidate the DNS at the same provider while he was at it. He recreated the records pointing at the site, switched the name servers on a Thursday afternoon, and the site came up on the new host within twenty minutes. He considered it done.

The mail exchange records had not been recreated. For three days, every message sent to any address at the domain was rejected — including the address printed on every valuation report as the contact for questions, and the address lenders replied to.

Two further problems surfaced on Monday. Nobody could log in, because the authentication provider's callback URLs still named the old hosting address; the agents had spent Friday assuming the system was "having a moment". And the payment webhook for the firms' monthly subscriptions pointed at the old address, so eleven days of subscription events went unrecorded, including two cancellations that continued to have access.

Five business days of work: mail exchange records restored along with SPF, DKIM and DMARC, with delivery tested against four major providers and the authentication results checked over the following week; the rejected mail could not be recovered, so Vincent contacted every agent and the four lenders he could identify directly; authentication callbacks corrected with both addresses registered during the transition; the payment webhook repointed with signature verification and event deduplication added, and the eleven days reconciled against the provider's records; TTLs lowered and a documented zone export produced; a full inventory written of everything using the domain; and the registrar transfer he had also been planning was deliberately postponed and done separately three weeks later, uneventfully.

**Result:** no incidents during the registrar transfer, and the inventory document is now what Vincent works from for any DNS change. He estimates the three days of lost email cost him one valuation firm's trust for the better part of a year.

> *"The site was up in twenty minutes and I thought I had done it. For three days every email to my company was rejected, including the address printed on every report I had ever sent."*
> — **Vincent Bogaers, Founder, Taxatierapport (Bergen op Zoom)**

**Cost & Timeline:** €2,800 (mail record restoration and delivery verification, authentication callback correction, webhook repointing and reconciliation, zone documentation and inventory) — completed in 5 business days.

## Frequently Asked Questions

### How do I avoid downtime when moving a domain?

Lower the TTL several days in advance so cached answers expire quickly, build and verify the new environment at a temporary address first, recreate every record before switching, and switch at a quiet weekday hour when you can watch and revert.

### Why did my email stop when I moved DNS?

Because mail records are separate from the records pointing at your site. Moving DNS without carrying across the mail exchange records plus SPF, DKIM and DMARC means messages are rejected silently, and senders see it before you do.

### Why can nobody log in after the move?

Because your authentication provider's callback URLs still name the old address. Most providers accept several, so register the new address before the switch and remove the old one a week later.

### Should I change registrar at the same time?

No. Changing where DNS is answered is fast and reversible; transferring a registrar is a formal multi-day process with locking periods. Do the DNS move, confirm everything works, then transfer separately.

### What must I check immediately after switching?

Both www and bare versions, the certificate on every variant, a real login, a test payment with its webhook recorded, email sent and received authenticated, scheduled jobs still running, and no configuration still naming the old address.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do I avoid downtime when moving a domain?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Lower TTLs days in advance, verify the new environment at a temporary address, recreate every record before switching, and switch at a quiet weekday hour."
      }
    },
    {
      "@type": "Question",
      "name": "Why did my email stop when I moved DNS?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Mail records are separate from site records. Without carrying across the mail exchange records plus SPF, DKIM and DMARC, messages are rejected silently."
      }
    },
    {
      "@type": "Question",
      "name": "Why can nobody log in after the move?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Authentication callback URLs still name the old address. Register the new one before the switch and remove the old one afterwards."
      }
    },
    {
      "@type": "Question",
      "name": "Should I change registrar at the same time?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — DNS changes are fast and reversible, registrar transfers are multi-day with locking periods. Do them separately."
      }
    },
    {
      "@type": "Question",
      "name": "What must I check immediately after switching?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Both domain versions, certificates, a real login, a test payment with webhook recorded, authenticated email delivery, scheduled jobs, and stale configuration."
      }
    }
  ]
}
</script>
