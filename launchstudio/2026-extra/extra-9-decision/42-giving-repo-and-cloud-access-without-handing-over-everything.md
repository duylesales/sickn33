---
Title: "Giving Repo and Cloud Access Without Handing Over the Keys to Everything"
Keywords: scoped developer access, least privilege contractor, GitHub collaborator permissions, Supabase service role key, secret rotation, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Giving Repo and Cloud Access Without Handing Over the Keys to Everything

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Giving Repo and Cloud Access Without Handing Over the Keys to Everything",
  "description": "A technical solo founder bringing in an outside engineering team has to grant real access without granting ownership of their business. This is a service-by-service breakdown of the exact roles, scoped keys, and rotation steps that make that possible on GitHub, Supabase, Firebase, Stripe, Mollie, DNS, and email.",
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
  "datePublished": "2027-01-06",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/giving-repo-and-cloud-access-without-handing-over-everything"
  }
}
</script>

Every guide about working with outside developers tells you to trust the people you hire. Almost none of them mention that trust is not an access model. You can completely trust a team and still have no business making them Project Owner on your Google Cloud project, because the risk you are managing is not "will they steal my Stripe balance" — it is device compromise, a leaked token in a CI log, a subcontractor you never met, and the fact that in nine weeks you will need to cleanly revoke everything and will not remember where you granted it.

The reflex — click Invite, pick the highest role so nothing gets blocked, move on — is understandable when you are one person trying not to be the bottleneck. It is also how founders end up with three ex-collaborators still holding Admin on the repo and a `service_role` key that has been pasted into two Slack workspaces. What follows is the version that takes about forty minutes to set up correctly, service by service, with the actual role names.

## The Principle: Grant Capability, Not Ownership

There is one distinction that makes every decision below obvious. Ownership is the ability to change who has access, to delete the resource, or to move money. Capability is the ability to do the work. Outside engineers need capability in abundance and ownership never.

The practical test: for every permission you are about to grant, ask whether it lets the grantee remove *you*, delete the resource entirely, or redirect funds or traffic. If yes, that is ownership and it stays with you. If no, be generous — under-granting is its own failure mode, and an engineer who has to ask you to run every migration is one you are paying to wait.

The second principle is that everything you grant must be revocable in a single, findable place. Individual user invitations are revocable. A password shared over WhatsApp is not, because you cannot know where it went. This is why "invite them as a user" is almost always better than "here's the login," even when the login feels faster on a Monday morning.

## GitHub: Write Access, Protected Main, No Admin

If your code sits in a personal repo, move it into a GitHub organisation first. It is free, it takes five minutes, and it gives you an audit log, a members list, and the ability to remove someone in one click without touching your personal account. Personal repos give you outside collaborators with no org-level visibility and no central offboarding.

Grant the **Write** role, not Admin and not Maintain. Write covers everything an engineer actually does: push branches, open pull requests, review, comment, run and read Actions. Admin adds the ability to change branch protection, manage webhooks, transfer the repo, and delete it — none of which is engineering work. Maintain sits in between and is fine if you want them managing issues and releases, but Write is the correct default for a fixed-scope engagement.

Then make Write safe by protecting the branch that matters. On `main`: require a pull request before merging, require at least one approving review, block force pushes, and block deletions. Enable "Require status checks to pass" if you have CI. This is the trade that makes generous access comfortable — the engineer can do anything they need on a branch, and nothing lands on your production branch without a reviewable diff you can read at your own pace.

Two more repo-level details worth doing while you are in there. Check **Settings → Deploy keys** and **Settings → Secrets and variables → Actions** before the engagement, because AI-scaffolded projects often carry deploy keys with write access and secrets nobody remembers adding. And if you need to give a machine or script access rather than a person, use a fine-grained personal access token or a GitHub App installation scoped to the single repository, never a classic token with full `repo` scope — a classic PAT grants access to every repository the issuing account can see, including your unrelated side projects.

## Supabase: Roles at the Organisation Level, and the Key That Ruins Your Week

Supabase permissions live on the organisation, not the project, which is the first thing to internalise: adding someone to your org gives them access to every project inside it. If you have three side projects in one org, split the one you are contracting out into its own organisation before inviting anyone.

Within the org, invite as **Developer** rather than Owner or Administrator. Developer covers the database, edge functions, storage, auth configuration, and logs. Owner adds billing, org deletion, and member management. Administrator sits between. For a hardening engagement, Developer is almost always sufficient, and if something genuinely requires elevation you can grant it for the afternoon and drop it back.

The key that deserves paranoia is `service_role`. It bypasses row-level security entirely — that is its whole purpose — so it is not a credential with elevated permissions, it is a credential with *no* permissions checks at all. Never paste it into a chat message, never commit it, and never expose it to any client-side code. If your AI tool ever wrote it into a frontend file or a `.env` that ended up committed, treat it as burned and rotate it in Settings → API before the engagement starts, not after.

Also: give the team a **separate staging project**, not a shared production one. It costs little at small scale, and it means the honest answer to "can I test this migration?" is yes rather than a negotiation. If your production database contains real user data, populate staging with a scrubbed dump — anonymised emails, no real payment references — rather than a straight copy, both for GDPR reasons and because a mistake in staging should never be able to email your actual customers.

## Firebase: Predefined IAM Roles Instead of Project Owner

Firebase access is Google Cloud IAM access, which people forget, and Project Owner on a GCP project is an enormous grant — billing, IAM, every enabled API, and the ability to remove you.

Use predefined roles instead. `roles/firebase.developAdmin` gives full read/write to Firebase products (Firestore, Realtime Database, Auth configuration, Storage rules) without IAM or billing control. Add `roles/firebasehosting.admin` if they are handling deploys and `roles/cloudfunctions.developer` if there are functions. Keep `roles/owner` and `roles/resourcemanager.projectIamAdmin` on your account only.

The Firebase-specific hazard in AI-generated code is a service account JSON key committed to the repo. Check `git log --all --full-history -- '*serviceAccount*.json'` before you start. If one exists anywhere in history, disable that key in the IAM console — deleting the file from the working tree does nothing, because the key remains valid until it is revoked at the source. Then create a fresh key and put it in a secret manager rather than a file.

## Stripe and Mollie: Restricted Roles Plus Restricted Keys

Stripe's role model is genuinely good and almost nobody uses it. Under **Settings → Team and security**, invite with the **Developer** role: API keys, webhooks, logs, test mode, and Stripe CLI access, but no ability to initiate payouts, change bank details, or remove team members. Reserve Administrator for yourself. If the work is purely integration-side, the **Analyst** role plus a restricted key is even tighter.

Then use **restricted API keys** rather than the secret key. In the API keys dashboard you can create a key with per-resource permissions — write access to Checkout Sessions and Customers, read on Charges, nothing on Payouts or Balance — and you can create a separate one per environment. Rotating a restricted key when the engagement ends is a thirty-second job with no blast radius on anything else.

Mollie, which is the sensible default if your buyers are Dutch and expect iDEAL, has a coarser model: add the engineer as a user on the organisation and keep the bank account and payout settings under a login only you hold. Mollie also separates test and live API keys clearly, so give live keys only when you are actually ready to test live flows, and generate a fresh one at that point rather than reusing whatever has been in circulation since your prototype.

For both, enable webhook signature verification from day one and hand over the signing secret through your password manager, not through the chat channel where you coordinate work.

## DNS: The One Grant That Should Almost Never Be Wholesale

Registrar access is the most dangerous credential you own, more than Stripe, because control of the domain means control of email, password resets, and every OAuth callback. Someone with registrar access can take over your identity across every service you use.

Do not share the registrar login. If your DNS is on Cloudflare, add the engineer as a **member scoped to the single zone** with a DNS-editing role, which lets them add and verify records without touching your account, other domains, or the registrar itself. Cloudflare's audit log then shows exactly which record changed and when. If your DNS sits at TransIP, Namecheap, or another registrar without granular delegation, do not go looking for a workaround — the correct answer is that they send you the records and you paste them in during a fifteen-minute call. It is genuinely faster than the alternatives and it keeps the highest-value credential in exactly one place.

Whichever route you take, keep registrar-level transfer lock enabled throughout and make sure the registrar's own account uses hardware or app-based two-factor, not SMS.

## Email Sending: Use a Subdomain So a Bad Week Stays Contained

Send transactional email from a subdomain — `mail.yourdomain.eu` or `send.yourdomain.eu` — rather than the root domain. This costs nothing and it means the sending reputation of your product's password resets and receipts is separated from the domain you use for your own business correspondence. If something goes wrong during setup and a batch of test emails gets flagged, the damage is contained to a subdomain you can rebuild.

Set SPF, DKIM, and DMARC on that subdomain, start DMARC at `p=none` with a reporting address so you can see what is actually sending as you, and tighten to `p=quarantine` once the flow is clean. In Resend, Postmark, or SendGrid, create a dedicated API key with send-only permissions for the engineering work rather than sharing the full-access key that can also read your suppression lists and message contents.

## Secrets: What to Rotate Before, During, and After

Assume that anything ever typed into an AI coding tool's chat window, committed to a repo, or pasted into Slack is compromised. That is not a slight on the tools; it is a reasonable posture given that roughly 45% of AI-generated code ships with security vulnerabilities and credential handling is one of the most common categories.

Before the engagement: rotate anything with a plausible exposure history, and search git history properly with `git log -p -S'sk_live'` or a scanner like `gitleaks detect --no-git=false`. Removing a `.env` in a later commit does not remove it from history — it needs `git filter-repo` or BFG, followed by a force-push and a rotation of everything it contained, because any clone or fork still holds the old objects.

During: keep secrets in one shared vault — a 1Password or Bitwarden collection created for this engagement — with per-credential items rather than a single note. That way revocation later is a list you can read rather than an archaeology exercise across chat logs.

After: rotate everything the engagement touched, on a schedule you set in advance. Not because you suspect anyone, but because a credential's exposure grows with the number of machines it has lived on, and rotation is cheap while an unknown is not.

## The Offboarding List You Write on Day One, Not Day Sixty

Write the revocation checklist at the same time you grant access, while you still remember every place you clicked. It takes four minutes and it is the difference between a clean close-out and a lingering, unverifiable one. A workable version: GitHub org members and outside collaborators; deploy keys and Actions secrets; Supabase org members and rotated `service_role` and `anon` keys; Firebase IAM bindings and any service account keys; Stripe team members and restricted keys; Mollie users and API keys; Cloudflare zone members; email provider API keys; the shared vault itself; and any OAuth apps or CI integrations authorised during the work.

Then actually run it on the last day, and confirm rather than assume — GitHub, Cloudflare, and Stripe all expose audit logs showing whether a removal actually landed. Behind LaunchStudio is Manifera's team of 120+ seasoned engineers, and the engagements that end cleanest are invariably the ones where the founder handed over a revocation list on the final call instead of promising to get around to it.

Scoped access is not a trust exercise; it is a design exercise you do once, in about forty minutes, and it makes an outside engagement both safer and faster because nobody is waiting on a permission they should already have had. Do it before kickoff rather than during. If you want a second opinion on what your current setup exposes, [LaunchStudio](https://launchstudio.eu/en/) works this way by default, and the underlying engineering practice comes out of [Manifera's offshore delivery teams](https://www.manifera.com/services/offshore-software-development/) working under enterprise access controls.

Want to sanity-check your permissions model against someone who reads AI-generated code every day? [Talk to an engineer](https://launchstudio.eu/en/#contact) — bring your repo and your list of connected services and you will get a straight answer about what is over-granted.

## Real example

### An Indie Hacker in Action: The Key That Was Still Live Eight Months Later

Thijs Bakker, a solo founder in Eindhoven, built Routewise — a route-planning and proof-of-delivery tool for independent couriers — in Cursor, with a Supabase backend and Stripe subscriptions. Before bringing in outside help for security and payment hardening, he ran a credential audit as part of setting up scoped access.

The audit surfaced three problems, none of which he had suspected. A Firebase service account JSON from an abandoned early version was still in git history and its key was still enabled in IAM, eight months after the code path had been deleted. His Supabase `service_role` key had been pasted into a Cursor chat and into a Discord thread while debugging. And a former freelance designer still held Write access to the repo, plus a deploy key created in 2025 that nobody could account for.

**Result:** All three were resolved before the engagement began — the Firebase key disabled at source, the Supabase keys rotated, the stale collaborator and deploy key removed — and the engagement ran on scoped roles throughout: Write on a protected `main`, Developer on a dedicated Supabase org, and a restricted Stripe key limited to Checkout and Customers. Offboarding on the final day took eleven minutes against a written list.

> *"None of what I found was malicious. It was just eight months of moving fast, and every one of those credentials was a real exposure I'd have carried into launch without noticing."*
> — **Thijs Bakker, Founder, Routewise (Eindhoven)**

**Cost & Timeline:** €2,900 (Launch Ready package, RLS hardening, webhook verification, and credential rotation) — live in 9 business days.

---

## Frequently Asked Questions

### Is Write access on GitHub really enough for an engineering team to do their job?

Yes, for essentially any fixed-scope engagement. Write covers pushing branches, opening and reviewing pull requests, and running Actions — the entire engineering workflow. Admin only adds repository administration: branch protection rules, webhooks, transfers, and deletion, which are your decisions rather than theirs.

### Why does Supabase access need a separate organisation rather than just inviting someone to the project?

Because Supabase grants membership at the organisation level, so an invitation to one project effectively grants access to every project in that org. If you have unrelated side projects sharing an organisation, move the contracted project into its own org before inviting anyone.

### What is the actual difference between the Supabase anon key and the service_role key?

The `anon` key is designed to be public and is constrained by your row-level security policies. The `service_role` key bypasses row-level security completely by design, so it must never reach client-side code or a chat window, and it should be rotated immediately if it ever has.

### Deleting a committed secret from the repo isn't enough — why not?

Because git keeps the full history, so the old commit containing the secret is still retrievable by anyone with a clone or a fork. Rewriting history with `git filter-repo` or BFG removes the object, but the credential itself must still be rotated at the provider, since copies may already exist elsewhere.

### Should I really refuse to share my domain registrar login, even with a team I trust?

Yes, and it is the one place worth being inflexible. Registrar access allows domain transfer, email redirection, and control of password-reset flows across every service you use — a broader grant than any payment or database credential. Delegate a Cloudflare zone role if you can, or paste records yourself during a short call if you cannot.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is Write access on GitHub really enough for an engineering team to do their job?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Write covers pushing branches, opening and reviewing pull requests, and running Actions, which is the entire engineering workflow. Admin only adds repository administration such as branch protection, webhooks, transfers, and deletion, which are the owner's decisions."
      }
    },
    {
      "@type": "Question",
      "name": "Why does Supabase access need a separate organisation rather than just inviting someone to the project?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Supabase grants membership at the organisation level, so inviting someone to one project effectively grants access to every project in that organisation. Move the contracted project into its own org before inviting anyone."
      }
    },
    {
      "@type": "Question",
      "name": "What is the actual difference between the Supabase anon key and the service_role key?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The anon key is meant to be public and is constrained by row-level security policies. The service_role key bypasses row-level security entirely by design, so it must never reach client-side code or chat, and should be rotated immediately if it has."
      }
    },
    {
      "@type": "Question",
      "name": "Deleting a committed secret from the repo isn't enough — why not?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Git retains full history, so the commit containing the secret remains retrievable from any clone or fork. History rewriting with git filter-repo or BFG removes the object, but the credential still has to be rotated at the provider."
      }
    },
    {
      "@type": "Question",
      "name": "Should I really refuse to share my domain registrar login, even with a team I trust?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Registrar access permits domain transfer, email redirection, and control of password-reset flows across every service you use, making it a broader grant than any payment or database credential. Delegate a scoped Cloudflare zone role, or add records yourself during a short call."
      }
    }
  ]
}
</script>
