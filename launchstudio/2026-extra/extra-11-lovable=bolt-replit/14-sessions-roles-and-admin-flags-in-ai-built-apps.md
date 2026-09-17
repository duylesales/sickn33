---
Title: "Supabase Security: Sessions, Roles and the Admin Flag Problem"
Keywords: supabase security, authentication roles admin flag, session management AI app, privilege escalation prototype, ai app security, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Supabase Security: Sessions, Roles and the Admin Flag Problem

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Supabase Security: Sessions, Roles and the Admin Flag Problem",
  "description": "How AI-generated apps typically model identity and permission, why an admin field in a user record is a vulnerability rather than a feature, and how to build a role system that holds up.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-16",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/sessions-roles-and-admin-flags-in-ai-built-apps" }
}
</script>

Somewhere in most AI-built applications there is a column called `is_admin`, or a field called `role` holding the word "admin", sitting in the same table as the user's display name and profile picture. It works. The admin dashboard appears for the right people and stays hidden for everyone else.

The question that decides whether it is a feature or a vulnerability is: who can write to that column? In a surprising number of prototypes, the answer is the user.

## Three Questions Every App Has to Answer

Authentication in a real product is not one problem but three, and generated apps usually solve the first well and the other two by accident.

**Who are you?** Login, sessions, tokens. Supabase Auth, Auth0, Firebase and their equivalents handle this competently, which is why AI-built apps get a working login screen so quickly.

**What are you allowed to do?** Roles, permissions, ownership. This is where prototypes are weakest, because it requires knowledge of your business that no prompt supplied.

**Is that still true right now?** Sessions expire, roles change, accounts get suspended, subscriptions lapse. A permission decided at login and never revisited is a permission that outlives its justification.

## Why an Admin Field in the User Table Is Dangerous

The pattern is ubiquitous because it is the obvious thing to generate: users have properties, admin-ness is a property, so it goes in the users table.

The danger arrives when that table is exposed through an automatically generated API, as it is in a typical Supabase setup, and the access policy allows people to update their own row. That policy is reasonable on its face — users should be able to change their own display name. It also means a user can send an update setting their own role to admin, unless the policy explicitly prevents writing to that specific column.

The attack requires no tooling and no skill: open the network tab, observe the shape of a profile update request, send the same request with an extra field. If your app then reads the role from that table to decide what the user may see, you have handed out administrative access through a settings page.

There is a second, quieter version. Some generated apps read the role in the browser and use it to decide which interface to render. Hiding a button is not a permission check — anyone can call the underlying endpoint directly. If the server does not independently verify the role, the admin panel is protected by politeness.

## What a Sound Model Looks Like

**Roles live somewhere users cannot write.** A separate table with policies that permit reading your own role and prohibit writing any role, or role claims managed server-side. The column your users can edit and the column that grants power must not be the same column.

**Permissions are enforced at the data layer.** Not in the interface, and not only in an API route. In a Supabase-backed app that means row level security policies that check the requester's role for the operations that matter, so an endpoint cannot be bypassed by calling the database API directly.

**The server decides, the interface follows.** Render an admin menu based on a role if you like — but every privileged operation must re-check the role server-side, as if the interface did not exist.

**Roles are few and named after the business.** Owner, staff, member, viewer. Five well-understood roles beat twenty granular permissions that nobody can reason about and that drift out of alignment with reality.

**Changes take effect immediately.** When someone is removed from a team or demoted, the next request should reflect it. If your app caches permissions in a long-lived token, a removed user stays powerful until that token expires — which is exactly the window you were trying to close.

## The Multi-Tenant Trap

The most common serious version of this problem appears in products selling to organisations: a clinic, a school, a hospitality group. Users belong to an organisation, and data belongs to an organisation.

Generated apps typically enforce "you can see your own records" and stop there, because that is the rule a single-user prototype needs. What they miss is the second condition — you can see records belonging to your organisation, and only your organisation.

The failure looks like this: an employee of Clinic A can read records from Clinic B by changing an identifier, because every check is about the individual rather than about the tenancy. For a business-to-business product, this is not merely a bug. It is the specific thing every procurement questionnaire asks about, and the reason a deal stalls after a security review.

Getting this right means every query and every policy carries the organisation condition, and that the organisation identifier comes from the server's view of the session rather than from something the browser sent.

## Sessions: The Part Everyone Configures Once and Forgets

**Token lifetime.** Long sessions are convenient and mean a stolen token is useful for longer. Short sessions with refresh are the standard compromise; the default your tool chose was optimised for building, not for your risk.

**Invalidation on password change.** If changing a password does not end other sessions, a user who suspects compromise cannot actually remove the intruder.

**Logout that reaches the server.** Clearing the interface is not ending a session.

**Suspended accounts.** Blocking a login does nothing about a session already in progress unless something checks account status on each request.

## Test Your Own Permission Model in Twenty Minutes

- Create two normal accounts and one admin. Log in as a normal user.
- Open the network tab, find a profile update request, and resend it with a role or admin field added. Then check whether your role changed.
- Call an admin endpoint directly while logged in as a normal user, bypassing the interface.
- If your product has organisations, create two and try to read the other one's records by changing an identifier.
- Change a password in one browser and see whether the second browser is still authenticated.
- Remove a user from a team and see how long they retain access.

Every one of these is a five-line test in a browser console and each corresponds to a real incident pattern. Anything that succeeds is a finding.

## Building the Layer That Was Never Prompted

Permission modelling is the clearest example of work that cannot be generated, because the rules come from your business rather than from your code. LaunchStudio's engineers build it as part of the last-mile: roles moved out of user-writable tables, policies enforced at the database layer, tenancy conditions applied consistently, session behaviour tightened, privileged operations verified server-side, and the whole model tested by trying to break it as a normal user.

The interface you built in Lovable, Bolt or Cursor stays untouched, the code stays yours, and the result is left documented and AI-readable so you can keep building. That is the [Launch Ready package](https://launchstudio.eu/en/#packages), delivered by Manifera's team from Amsterdam and Ho Chi Minh City, with eleven years of production work behind it for clients including Vodafone, TNO and CFLW.

If you have an `is_admin` column and you are not certain who can write to it, [talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact).

## Invitations: The Flow That Quietly Leaks Access

If your product has teams or organisations, the invitation flow deserves its own scrutiny, because it is where permission decisions are made by people who are not thinking about permissions.

**Invitation links are credentials.** A link that grants membership on click is a key sent by email. It should be single-use, tied to a specific address, and expire — a week is generous. Generated invite flows routinely produce links that work forever, for anyone, and those links end up forwarded, pasted into group chats and left in inboxes indefinitely.

**The inviter's rights bound the invitation.** A member should not be able to invite someone as an administrator. If the role is chosen in the browser and sent with the request, it can be altered, so the server must check that the inviter is permitted to grant that role.

**Email change is an access change.** If a user can change their account email without confirming the new address, an invitation tied to an address becomes transferable. Confirm new addresses before they take effect, and notify the old one.

**Removal must be immediate and complete.** When someone leaves an organisation, their sessions should stop working for that organisation's data on the next request — not when a token expires. Test this specifically: remove a user in one browser and try to load an organisation record in theirs.

**Pending invitations are state.** An invitation sent to someone who has not yet accepted, for an organisation that has since changed hands or deleted a project, should not grant access to whatever now occupies that place.

Each of these is a small piece of logic, and together they decide whether your team feature is a convenience or the widest door in your product.

## Real example

### A Veterinary Platform Where Any Clinic Could Read Any Other

Marijn Kuipers built DierZorg in Lovable: a shared platform where independent veterinary practices around Apeldoorn manage appointments and patient records. Eleven clinics had signed up before the first security review.

Two findings mattered. The user profile table contained a `role` field with a policy allowing users to update their own row, so any registered user could make themselves an administrator by adding one field to a settings request. And every data policy checked only that the requester was authenticated and owned the record — nothing checked which clinic the record belonged to, so a vet at one practice could open another practice's patient records by changing a number in the address.

The second finding was the commercial one: DierZorg was in the middle of a procurement conversation with a nine-practice group whose questionnaire asked precisely this.

Nine business days of work: roles moved into a server-managed table with read-only access for users, all privileged operations verified server-side, an organisation condition added to every policy and every query with the clinic identifier derived from the session rather than the request, sessions invalidated on password change and on removal from a practice, and a test suite that logs in as two users from different clinics and asserts neither can read the other's data.

**Result:** the nine-practice group signed six weeks later after a clean security review, and DierZorg now runs the permission test suite on every deploy.

> *"Any of my users could have promoted themselves to admin from the settings page. It had been live for four months and the only reason nothing happened is that nobody tried."*
> — **Marijn Kuipers, Founder, DierZorg (Apeldoorn)**

**Cost & Timeline:** €3,700 (Launch Ready Package: role model, tenancy isolation, session hardening, permission tests) — completed in 9 business days.

## Frequently Asked Questions

### What is wrong with storing a role in the user table?

Nothing, provided users cannot write to that column. The problem arises when a policy lets people update their own profile row and the role sits in the same row, which allows a user to grant themselves administrative access with one extra field in a normal request.

### Is hiding the admin menu enough to protect it?

No. Hiding an interface element removes the invitation, not the capability. Anyone can call the underlying endpoint directly, so every privileged operation must verify the role on the server independently of what the interface shows.

### How do I stop one customer organisation seeing another's data?

Every policy and query needs an organisation condition, and the organisation identifier must come from the server's view of the session rather than from a value the browser supplied. This is the single most common finding in business-to-business prototypes.

### Should sessions expire quickly?

Shorter sessions with refresh are the usual compromise. More important than duration is invalidation: sessions should end when a password changes, when an account is suspended and when a user is removed from an organisation.

### Can I test this without technical help?

Largely yes. Create two accounts, try to read each other's data by changing identifiers, attempt to add a role field to a profile update, and check whether a password change logs out a second browser. Anything that succeeds is a finding worth acting on.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is wrong with storing a role in the user table?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nothing, provided users cannot write to that column. The problem is a policy allowing profile updates on a row that also holds the role, letting a user grant themselves admin access with one extra field."
      }
    },
    {
      "@type": "Question",
      "name": "Is hiding the admin menu enough to protect it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Hiding an interface element removes the invitation, not the capability. Privileged operations must verify the role server-side independently of the interface."
      }
    },
    {
      "@type": "Question",
      "name": "How do I stop one customer organisation seeing another's data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Every policy and query needs an organisation condition, with the identifier taken from the server's view of the session rather than from the browser. This is the most common finding in B2B prototypes."
      }
    },
    {
      "@type": "Question",
      "name": "Should sessions expire quickly?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Shorter sessions with refresh are the usual compromise, but invalidation matters more: sessions should end on password change, suspension and removal from an organisation."
      }
    },
    {
      "@type": "Question",
      "name": "Can I test this without technical help?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Largely yes — create two accounts, try to read each other's data by changing identifiers, attempt to add a role field to a profile update, and check whether a password change ends a second session."
      }
    }
  ]
}
</script>
