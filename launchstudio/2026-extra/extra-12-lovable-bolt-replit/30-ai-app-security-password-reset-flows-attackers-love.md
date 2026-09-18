---
Title: "AI App Security: Password Reset Flows Attackers Love"
Keywords: ai app security, password reset, account recovery, token expiry, user enumeration, email change, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI App Security: Password Reset Flows Attackers Love

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI App Security: Password Reset Flows Attackers Love",
  "description": "Password reset is the back door to every account, and AI-generated implementations get it wrong in consistent ways. Token design, enumeration, the email change nobody protects, and what to do after a reset.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-12",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-app-security-password-reset-flows-attackers-love" }
}
</script>

Every account in your product has two doors. The front one is the login form, which founders think about, test and occasionally add a second factor to. The back one is password reset, which exists to let someone in without knowing the password — and is built in ten minutes, once, and never looked at again.

An attacker choosing between them will not choose the front door.

This is worth an afternoon precisely because it is unglamorous. Nobody demos a reset flow. Nobody notices it working. And it is the mechanism by which accounts are taken over in products that are otherwise carefully built.

## What a Reset Token Must Be

Six properties, and generated implementations typically miss two or three.

**Unpredictable.** Generated from a cryptographically secure source, long enough that guessing is hopeless. A token derived from a timestamp, an email address or a sequential value can be produced by anyone who thinks about it.

**Short-lived.** Fifteen to sixty minutes. A reset link valid for a week is a key sitting in an inbox — and inboxes are forwarded, synced to devices, and occasionally read by other people.

**Single use.** Invalidated the moment it is used. A link that still works after the password has been changed is a link an attacker can use later, having intercepted the email once.

**Bound to one account**, and invalidating any previous outstanding token for that account, so requesting a new reset cancels the old.

**Stored hashed**, not in plain text. Your database is the one place the token should not be readable, for the same reason you do not store passwords.

**Invalidated on use of any other recovery path**, so a reset and an email change cannot be in flight simultaneously.

## Say the Same Thing Whether the Account Exists or Not

If your reset form says "no account with that email" for unknown addresses and "check your inbox" for known ones, you have built a tool for confirming who uses your product.

That matters more than it sounds. For a product serving a sensitive category — debt counselling, legal advice, healthcare, a dating service — membership is itself confidential. And for any product, a confirmed list of real customer addresses is what makes a phishing campaign effective.

The correct response is identical in both cases: *if an account exists for that address, we have sent a link*. Same text, same status, and roughly the same timing — a response that returns instantly for unknown addresses and takes 400 milliseconds for real ones leaks the same information through the clock.

The same discipline applies to registration and to login, where "this email is already registered" is the most common enumeration leak in AI-built products.

## Rate Limit the Request, Not Just the Attempt

Two limits, and the second is usually missing.

Limit reset requests per account and per address, so an attacker cannot generate hundreds of tokens for one victim — which both raises the chance of interception and floods the person with mail.

Limit reset requests per IP address and per time window, because the same endpoint sends email on demand to arbitrary addresses. Without a limit, your product is a free mailing tool with your domain's reputation attached, and the first consequence is that your legitimate mail starts going to spam folders.

## After a Reset, End Everything Else

A password reset frequently means "I think someone else has access". The flow should behave as though that is true.

Invalidate every other session for the account, so an attacker who is signed in is signed out. Notify the account's email address that the password was changed, with a time and a way to respond if it was not them — sent to the address on file at the time of the change, which is the notification that catches an account takeover in progress.

And do not sign the user in automatically from the reset link itself. The link proves access to an inbox; asking them to log in with the new password proves they chose it.

## The Email Change Is the Real Vulnerability

Password reset gets attention. Changing the email address on an account gets almost none, and it is the more powerful action — whoever controls the address controls every future reset.

Three protections, and AI-generated implementations rarely have any.

Require the current password, or a second factor, before the change is accepted. Verify the new address by sending a confirmation link to it, and do not apply the change until it is clicked. And notify the old address, with a window in which the change can be reversed from that message.

That last one is what saves an account when a session has already been compromised: the attacker changes the email, the real owner receives a message at the old address, and clicking a link undoes it.

## Support Recovery Is the Human Version

Eventually someone loses access to their email and writes to you. Whatever you do next is your account recovery process, whether or not you have designed one.

Decide in advance what evidence you require — something only the account holder would know, confirmation from another user in the same organisation, a verified payment detail — and write it down. Then follow it, including when the person is frustrated and senior and in a hurry, because that is precisely the pressure a social engineering attempt applies.

Record every manual recovery: who asked, what was verified, who approved it. For a business product this is also what a customer's security questionnaire asks about.

## Password Rules That Help Rather Than Annoy

While you are in this part of the product, the rules around the password itself are worth revisiting, because the conventional advice most generated code implements is now considered actively unhelpful.

Composition requirements — one uppercase, one number, one symbol — push people toward predictable substitutions and a note in a drawer. Forced rotation every 90 days produces the same password with an incrementing digit. Both were dropped from serious guidance years ago and both still appear in new applications because they are what the training data contains.

What current guidance supports: a minimum length of at least twelve characters with no composition rules and no arbitrary maximum below 64; checking the chosen password against a list of known breached passwords, which is a free API call and catches the genuinely dangerous choices; allowing spaces and the full character set so passphrases work; and never expiring passwords on a schedule, only on evidence of compromise.

Store them with a modern password hashing algorithm designed for the purpose. If you use an authentication provider this is handled; if any part of your application hashes passwords itself — which happens in AI-built products that added a second login path for administrators — check what it uses, because a fast general-purpose hash is the wrong tool and appears with some regularity.

One more small thing that measurably reduces support volume: let people see what they typed. A visibility toggle on the password field is not a security weakness, and it prevents a great many failed logins.

And treat the login form's own rate limiting as part of this work: a small number of attempts per account and per address, with a delay rather than a permanent lock, so a determined guesser is stopped without giving anyone a way to lock your customers out of their own accounts on purpose.

## Setting This Up

For an existing product this is typically half a day: reset tokens generated securely, expiring within an hour, single use, hashed at rest, and invalidating prior tokens; identical responses and timing regardless of whether an account exists, applied to registration and login too; rate limits per account and per IP; all other sessions invalidated on reset with a notification to the address on file; no automatic sign-in from the link; email changes requiring the current password, confirmation at the new address and a reversible notification to the old one; and a written support recovery procedure with a record of each use.

LaunchStudio covers recovery flows in security review, where they are consistently weaker than the login they protect. The engineers are Manifera's — eleven years, 120+ engineers, clients including Vodafone, TNO and CFLW.

[Ask us to attempt a reset against your own account](https://launchstudio.eu/en/#contact). It is the fastest security test we run.

## Real example

### An Account Taken Over Through the Email Change

Gerben Stuiver built Klantportaal in Lovable: a customer portal for accountancy and administration offices, where 62 offices share documents and messages with around 4,000 business clients.

The password reset was reasonable: a random token, expiring in 24 hours. The email change was not protected at all. A signed-in user could change the address on the account with no password confirmation, no verification of the new address, and no notification to the old one.

A client's laptop was compromised through unrelated malware and the session cookie was stolen. The attacker used the session to change the email address on the account to one they controlled, waited for the session to expire, and then used the ordinary password reset flow — which now sent to their address — to set a password. They had the account permanently, and the real owner was locked out with no notification of anything.

The business discovered it when their accountant mentioned a document request they had not made.

Two business days: email changes now require the current password, send a confirmation link to the proposed new address, apply only when confirmed, and notify the old address with a 48-hour reversal link; reset token lifetime cut from 24 hours to 30 minutes, made single use, hashed at rest, and invalidating any previous outstanding token; identical responses and timing for known and unknown addresses across reset, registration and login, which had previously stated plainly whether an email was registered; rate limits per account and per IP on the reset endpoint, which had none and had been used to send 900 reset emails in one afternoon the previous month; all sessions invalidated on password change with a notification to the address on file; automatic sign-in from the reset link removed; and a written support recovery procedure requiring confirmation from a second contact at the same office, with every use recorded.

**Result:** the account was recovered manually and the incident reported to the affected business and their accountant. In the following year the old-address notification has been triggered by four email changes, one of which was reversed by a client who had not made it — an attempted takeover caught in eleven minutes by a message that cost nothing to send.

> *"Everyone protects the password. Nobody protects the address the password reset goes to, and that is the one that actually owns the account."*
> — **Gerben Stuiver, Founder, Klantportaal (Zwolle)**

**Cost & Timeline:** €2,300 (email change protection with confirmation and reversal, reset token hardening, enumeration removal across three flows, rate limiting, session invalidation and notification, support recovery procedure) — completed in 2 business days.

## Frequently Asked Questions

### How long should a password reset link be valid?

Fifteen to sixty minutes, single use, and invalidated when a newer one is requested. A link valid for a day or a week is a key sitting in an inbox.

### Why should the reset form not say whether an account exists?

Because it confirms who uses your product — which is confidential for sensitive categories and, for any product, gives a phishing campaign a verified address list. Keep the response and its timing identical.

### Should a reset link sign the user in automatically?

No. The link proves access to an inbox. Ask them to sign in with the new password so the account is entered by someone who knows the credential.

### What protects the email change on an account?

The current password or a second factor, confirmation at the new address before the change applies, and a notification to the old address with a reversal link. Most AI-built products have none of these.

### What should happen to other sessions after a password reset?

All of them should end. A reset often means the user suspects someone else has access, and the flow should behave as though that is true.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long should a password reset link last?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Fifteen to sixty minutes, single use, hashed at rest, and invalidated when a newer request is made."
      }
    },
    {
      "@type": "Question",
      "name": "Why must a reset form not reveal whether an account exists?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It confirms who your customers are — sensitive in itself and the basis of an effective phishing list. Keep response text and timing identical."
      }
    },
    {
      "@type": "Question",
      "name": "Should a reset link log the user in automatically?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. The link only proves inbox access; require a sign-in with the newly chosen password."
      }
    },
    {
      "@type": "Question",
      "name": "How should an email address change be protected?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Require the current password or a second factor, confirm at the new address before applying, and notify the old address with a reversal link."
      }
    },
    {
      "@type": "Question",
      "name": "What happens to sessions after a password reset?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They should all be invalidated, since a reset usually means the user suspects someone else has access."
      }
    }
  ]
}
</script>
