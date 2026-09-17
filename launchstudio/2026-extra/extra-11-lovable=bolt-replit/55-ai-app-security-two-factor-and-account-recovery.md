---
Title: "AI App Security: Two-Factor Authentication and Account Recovery"
Keywords: ai app security, supabase security, two factor authentication saas, account recovery codes, support driven account takeover, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI App Security: Two-Factor Authentication and Account Recovery

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI App Security: Two-Factor Authentication and Account Recovery",
  "description": "Adding a second factor is the easy half. Recovery is where account takeovers actually happen, and where founders answering support emails become the weakest link. What to build, in what order, and how to test it.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-27",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-app-security-two-factor-and-account-recovery" }
}
</script>

There is a version of account takeover that requires no technical skill at all. Someone emails a founder, says they have lost access to their account and changed phone, sounds reasonable, provides a piece of information that is public or guessable, and asks for help getting back in. The founder — helpful, busy, running a small product where every customer matters — helps.

That is the most likely way an account in your product will be taken over, and it is entirely unaffected by whatever authentication you built. Which is the point of this article: a second factor without a considered recovery path does not add security, it adds a support queue with a door in it.

## When a Second Factor Becomes Necessary

Not on day one for most consumer products, and sooner than founders expect for others.

**Your product holds business-critical data.** Finance, client records, health, anything that would be damaging in a competitor's or a stranger's hands.

**Accounts control money.** Payouts, invoices, refunds, anything where a takeover converts directly into loss.

**Your customers are businesses.** Enterprise and public-sector buyers increasingly expect it, and it appears in procurement questionnaires as a yes-or-no question.

**Users have elevated roles.** Even where ordinary accounts do not need it, administrators should — the accounts that can act on everyone else's data are the ones worth protecting first.

A sensible sequence for a small product: build it optional for everyone, require it for administrative roles, and enable enforcement per organisation when a business customer asks.

## The Options, and What They Cost Your Users

**Authenticator apps** generating time-based codes. The reasonable default: free, offline, no dependency on a phone network, and supported by every password manager your users already have.

**Passkeys**, which use the device's own biometrics or PIN. The best user experience available and increasingly well supported, with the caveat that recovery and multi-device behaviour need thought.

**Email codes.** Weak as a second factor when email is also your password-reset channel, because compromising one compromises both. Better than nothing, and not what you should tell a business customer you have.

**SMS codes.** Widely understood and the least robust of the options, because numbers can be ported and messages intercepted. Acceptable as an option users choose, not as your only mechanism.

**Hardware keys.** Excellent, and unnecessary for most products at this stage.

For a small Dutch product, authenticator apps with passkeys as an upgrade path covers almost every realistic requirement.

## Recovery Is the Hard Part, and the Whole Point

Every second factor creates a new way for legitimate users to lock themselves out. Phones are lost, replaced, reset and stolen — routinely, by people who have done nothing wrong.

Your recovery design determines your actual security level, because an attacker will always attempt the weakest path. If your recovery is "email us and we will disable it", then your second factor is decorative and your real authentication mechanism is the judgement of whoever reads support email at nine in the morning.

**Recovery codes** are the standard answer: a set of single-use codes shown once at enrolment, which the user stores. They work, provided you insist the user acknowledges saving them and provided you check them properly when used.

**A second registered device** or a second passkey. The best option for users who have one, and worth prompting for at enrolment.

**A verified fallback**, such as a confirmed secondary email or an administrator within the same organisation who can reset a colleague. This is particularly useful for business products, where the customer's own administrator becomes the recovery path rather than you.

What should not be a recovery path: personal questions with guessable answers, and an unstructured conversation with you.

## The Support-Driven Takeover

This deserves its own procedure, because it is the realistic threat and because good intentions are what make it work.

Write down, before you need it, what evidence you require to restore access. Something only the account holder would have: a recent invoice number, a payment reference, access to a confirmed alternative address, confirmation from an administrator at the same organisation. Then apply it every time, including when the person is frustrated, sounds senior, or is in a hurry — those are precisely the pressure tactics that social engineering relies on.

Two further rules. Never confirm what you already know about an account to someone whose identity is unproven, including whether the account exists. And when access is restored, notify the original address on record, so that a genuine takeover produces an alarm somewhere.

For a product with business customers, the cleanest arrangement is to move recovery to their side: their administrator resets their colleague, and you are not in the loop at all.

## What to Build, in Order

**Enrolment that works on one device,** with codes shown once and an explicit confirmation that they have been saved.

**Recovery codes,** single-use, invalidated when regenerated, and checked with the same care as a password.

**Device management,** so a user can see and remove registered factors — which is also how someone who suspects compromise removes an attacker's device.

**Re-authentication for sensitive actions.** Changing the email address, disabling the second factor, changing payout details, deleting the account. A valid session is not sufficient for these, because sessions get borrowed.

**Notifications on security events.** Second factor enabled, disabled, device added, recovery code used, password changed. Sent to the address on record, always, even when the user performed the action themselves.

That last item is cheap and disproportionately valuable: it is how a legitimate user finds out that something happened without them.

## Business Customers and Enforcement

Once you sell to organisations, the requirement shifts from offering a second factor to being able to require one.

Practically that means enforcement at the organisation level — an administrator can mandate it for everyone in their account — plus visibility of who has enrolled, plus a grace period so enforcement does not lock out an entire customer on the day it is switched on.

This is a small feature that appears in procurement questionnaires disproportionately often, and having it is frequently the difference between a long conversation and a short one.

## What Not to Do

**Do not make it mandatory for everyone on day one** without a recovery path you have tested, unless you enjoy support volume.

**Do not rely on email as the second factor** when email also resets the password.

**Do not disable someone's second factor on request** without applying your evidence rule.

**Do not skip re-authentication** for the actions that change how an account is secured.

**Do not implement the codes yourself** if a well-tested library exists for your stack — this is exactly the category where generated code produces something that works and is subtly wrong.

## Testing Your Own Implementation

Half an hour, and it finds most of what is broken.

Enrol a second factor and confirm you are prompted on the next login. Use a recovery code, then try the same code again — it must fail. Regenerate the codes and confirm the old ones no longer work. Attempt to disable the second factor and check whether you are asked to re-authenticate. Change the email address and see whether the old address is notified. Log in on a second browser, remove that device from the first, and see whether the second session is actually ended. Then check your own inbox: did any of these produce a notification?

Anything that behaves unexpectedly is a finding, and most are configuration or a missing call rather than a rebuild.

## Building It Properly

This is one of the areas where generated implementations look complete and leave the important half missing — enrolment tends to work, recovery tends not to exist, and re-authentication is almost never there.

LaunchStudio builds the whole path as part of taking an AI-built product live: a second factor using a well-tested implementation for your stack, recovery codes that behave correctly, device management, re-authentication on sensitive actions, security notifications, organisation-level enforcement for business customers, and a written support procedure for the case where someone genuinely loses everything — with the interface you built in Lovable left as it is.

The engineers are Manifera's, with eleven years of production authentication work behind them for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City. [Talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact), or see what the [Launch Ready package](https://launchstudio.eu/en/#packages) includes.

## Rolling It Out Without Locking People Out

Introducing a second factor to an existing user base is where well-intentioned security creates support volume, and a staged rollout avoids nearly all of it.

**Start optional, with a prompt.** Offer it, explain briefly what it protects, and let people opt in. Early adopters find the problems in your enrolment flow before everyone meets them.

**Require it for administrative roles next.** The accounts that can act on other people's data are worth protecting first, and the affected group is small enough to support individually.

**Then offer enforcement to business customers,** with a grace period so their staff enrol over a fortnight rather than being locked out on a Monday morning.

**Communicate before, not during.** An email a week ahead explaining what will change, why, and what to do if they lose their device removes most of the confused replies.

**Watch the enrolment funnel.** People who start and abandon are telling you the flow is unclear, and that is a fixable product problem rather than user reluctance.

Rolled out this way, a second factor arrives without a support spike. Rolled out as a mandatory switch flipped on a Tuesday, it produces a week you will remember.

## Real example

### A Takeover That Arrived Through the Contact Form

Erik Vlietstra ran Salarisplan in Lovable: a payroll-preparation tool used by eleven small accountancy practices around Zwolle, holding employee data and payment instructions for their clients.

Two-factor authentication had been added six months earlier and was working. Recovery had not been designed: the enrolment screen showed codes, nothing insisted they be saved, and when a user lost a phone Erik disabled the second factor manually after an email exchange.

In March someone emailed claiming to be a bookkeeper at one of the practices, saying she had a new phone and needed access before a deadline. The message used the practice's real name, referenced a genuine payroll date that was publicly inferable, and applied pressure. Erik disabled the second factor and sent a reset link.

It was not her. The account was accessed, payment details on two employee records were altered, and the change was caught by the practice's own review the following day before any payment ran.

Six business days of work: recovery codes implemented properly with mandatory acknowledgement and single use; device management added; re-authentication required for disabling a factor, changing an email address and altering payment details; security notifications sent to the address on record for every such event; organisation-level enforcement so practice owners could mandate the second factor; recovery moved to the practice's own administrator rather than to Erik; and a written evidence rule for the cases that still reach support.

**Result:** no financial loss occurred, the practice stayed after being told plainly what had happened, and two recovery requests since have been handled by practice administrators without Erik being involved.

> *"My authentication was fine. The way in was me, being helpful, on a Tuesday morning, to someone who sounded like they were having a bad day."*
> — **Erik Vlietstra, Founder, Salarisplan (Zwolle)**

**Cost & Timeline:** €2,700 (recovery codes, device management, re-authentication, security notifications, organisation enforcement, support procedure) — completed in 6 business days.

## Frequently Asked Questions

### When does a small product need two-factor authentication?

When it holds business-critical or sensitive data, when accounts control money, when you sell to organisations that ask, or for administrative roles specifically. Offering it optionally and requiring it for administrators is a sensible first step.

### Which second factor should I use?

Authenticator apps are the reasonable default — free, offline and widely supported — with passkeys as an upgrade. Email codes are weak when email also resets the password, and SMS is acceptable as an option rather than as the only mechanism.

### What is the most common way accounts are actually taken over?

Through support. Someone contacts the founder claiming to have lost their device, applies mild pressure, and is helped. A written evidence rule applied every time is the defence, and it matters more than the factor itself.

### What should recovery look like?

Single-use recovery codes acknowledged at enrolment, a second registered device where possible, and for business products an administrator at the customer who can reset colleagues — which removes you from the loop entirely.

### Which actions should require re-authentication?

Disabling the second factor, changing the email address, changing payout or payment details, and deleting the account. A valid session is not sufficient for these, because sessions are borrowed more often than passwords are stolen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "When does a small product need two-factor authentication?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "When it holds sensitive or business-critical data, when accounts control money, when business customers ask, or for administrative roles — offering it optionally and requiring it for admins is a sensible start."
      }
    },
    {
      "@type": "Question",
      "name": "Which second factor should I use?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Authenticator apps as the default, with passkeys as an upgrade. Email codes are weak when email also resets passwords, and SMS should be an option rather than the only mechanism."
      }
    },
    {
      "@type": "Question",
      "name": "What is the most common way accounts are actually taken over?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Through support — someone claims to have lost their device and is helped. A written evidence rule applied every time is the real defence."
      }
    },
    {
      "@type": "Question",
      "name": "What should recovery look like?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Single-use recovery codes acknowledged at enrolment, a second registered device, and for business products an administrator who can reset colleagues."
      }
    },
    {
      "@type": "Question",
      "name": "Which actions should require re-authentication?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Disabling the second factor, changing email address, changing payment details and deleting the account."
      }
    }
  ]
}
</script>
