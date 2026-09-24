---
Title: "AI Development Red Flags: Eight Things in Your Codebase That Mean 'Get a Review'"
Keywords: ai development, ai code red flags, when to get a code review, ai generated code warning signs, bolt app review, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# AI Development Red Flags: Eight Things in Your Codebase That Mean "Get a Review"

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Development Red Flags: Eight Things in Your Codebase That Mean 'Get a Review'",
  "description": "Eight warning signs a non-technical founder can spot in an AI development project — without reading code — that indicate the app needs a professional review before real users or payments arrive.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-05",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-development-red-flags-eight-things-in-your-codebase-that-mean-get-a-review" }
}
</script>

Non-technical founders often ask: "How would I even know if my app has a problem?" You cannot read the code, and the app works when you click through it. But AI development leaves visible traces — in how the app behaves, how it was built and what your tools and accounts show. None of these red flags prove there is a vulnerability. Each one means the chance is high enough that a professional review is worth it before real users or payments arrive.

## Red Flag 1: You Can See Other People's Data by Changing a Number

Open something that belongs to you — an order, a booking, a profile — and look at the web address. If it contains a number, change it slightly while logged in. If you see someone else's data, you have found the most common serious problem in AI-built apps. This one is not a maybe; it is a stop sign.

## Red Flag 2: The Page Source Contains Words Like "secret" or "sk_"

Right-click, choose "View page source," and search for `secret`, `sk_`, `service_role` or `api_key`. Some keys are designed to be public, but secret keys for payments, AI services or database administration must never appear there.

## Red Flag 3: "Admin" Is Only Hidden, Not Protected

If your admin area is protected only because normal users don't see the link, try opening its address in a private browser window or while logged in as a normal user. If it loads, anyone who guesses the address can use it.

## Red Flag 4: The App Says "Paid" Before the Payment Provider Does

Start a test payment, then close the payment page before returning. If your app shows the order as paid — or never records a payment that actually went through — payments are confirmed the wrong way.

## Red Flag 5: Everything Lives on One Account You Don't Fully Control

If the database, hosting or domain is on a freelancer's account, a former co-founder's email, or a personal account without two-factor authentication, you do not fully control your product. This is an ownership red flag with direct security consequences.

## Red Flag 6: You Have Never Restored a Backup

If you do not know whether backups exist, or have never restored one, assume you cannot recover from a mistake. Many AI-built apps run for months without working backups.

## Red Flag 7: Changes Go Straight to Live

If every edit in your AI tool is immediately visible to customers, with no test environment, one prompt can break the app for everyone — and you have no easy way back.

## Red Flag 8: You Find Out About Problems From Customers

If nobody is alerted when the app goes down or errors occur, your customers are your monitoring system. That usually means many problems happen without anyone noticing.

## How Many Flags Is Too Many?

- **Red flag 1, 2, 3 or 4:** get a review before inviting more users or taking payments. These can harm customers directly.
- **Red flags 5–8 only:** less urgent, but plan a review before growth or a big launch.
- **Three or more flags of any kind:** a structured review will almost certainly find more.

## Why These AI Development Flags Appear

They are not signs of a bad founder or a bad tool. AI development tools build what you describe, and they are excellent at screens and flows. They do not decide who may see what, where secrets belong, or how your business should recover from a mistake — unless someone tells them. The flags are simply the places where nobody did.

## How to Check Each Red Flag, Step by Step

AI development red flags are only useful if you can check them reliably. A step-by-step guide for non-technical founders:

**Red flag 1 — changing a number.** Create two accounts (use a second email address). With account A, create an item and note its address. Log out, log in as B, paste A's address. Also try changing the last digit of your own item's address while logged in as A. If anything that is not yours appears, stop and note it.

**Red flag 2 — secrets in page source.** On any page of your app, right-click → View page source, then search for `sk_`, `secret`, `service_role`, `api_key`, `password`. Repeat on the JavaScript files listed in the browser's network tab. Write down every match with the surrounding text.

**Red flag 3 — hidden admin.** Log in as a normal user, then type your admin page's address directly. Try also in a private window without logging in.

**Red flag 4 — payment confirmed early.** In test mode, start a payment, close the payment tab before returning and check the order. Then complete a payment normally and check again.

**Red flag 5 — ownership.** List every service your app uses and check which email owns it and whether two-factor authentication is on.

**Red flag 6 — backups.** Log into your database provider, find backups, check they are enabled and ask your engineer to restore one into a test project.

**Red flag 7 — changes go live directly.** Ask: when I change something in my AI tool, where does it appear first? If the answer is "live," this flag is raised.

**Red flag 8 — customers as monitoring.** Ask: if the app went down now, who would get a message, and how?

## Interpreting What You Find

| Finding | Severity | What to do |
| --- | --- | --- |
| Another user's data visible | Critical | Pause new signups; fix access control before anything else |
| Secret key in page source | Critical | Rotate the key immediately; move calls server-side |
| Admin page reachable by normal users | Critical | Protect with server-side role checks |
| Payment marked paid without payment | High | Switch to webhook confirmation before taking more payments |
| Accounts not owned by you | High | Transfer ownership and enable 2FA |
| No tested backup | High | Enable backups and restore once |
| Changes go straight to live | Medium | Set up staging before the next major change |
| No alerts | Medium | Add uptime and error alerts this week |

Critical findings deserve action the same day; high findings within days; medium within weeks.

## Additional Warning Signs Worth Noticing

Beyond the eight red flags, several other signs suggest a review is due: error messages that show technical details such as database table names; files uploaded by users accessible through public links; login forms that say "no account with this email"; no limit on repeated login attempts; test data or test users visible in production; and code changes you cannot trace because the project is not connected to a repository. Each is a smaller signal, but together they indicate that production basics were not yet addressed.

## Why Checking Yourself Is Valuable Even Before Hiring Help

Running the checks yourself has three benefits. It gives you a concrete picture of risk instead of a vague worry. It makes conversations with engineers faster and more precise, because you can say exactly what you observed. And it gives you a way to verify the work afterwards: once fixes are made, rerun the checks and see the flags disappear. Founders who do this remain in control of their product even when they cannot read its code.

## When to Stop Testing and Call Someone

If red flag 1, 2 or 3 is raised, stop exploring further on your live app and get help. These findings mean real users' data or real money may be exposed, and further poking around can create confusion about what happened. Note what you found, change nothing else, and ask an engineer to confirm the issue, check logs for misuse and fix it. If personal data may have been accessed by someone who should not have seen it, the incident may need to be assessed for notification to the data protection authority.

## Red Flags in the Development Process, Not Just the App

Some warning signs are about how the app is built rather than what it does: no one can explain where the latest version of the code is; changes are made directly in the AI builder without any history; a freelancer holds the only copy of the database password; there is no list of external services; and nobody knows which version is running in production. These process flags predict future incidents as reliably as technical ones, because they mean problems cannot be traced or reversed.

## Red Flags in Supplier Answers

When you ask a developer or agency about the flags, their answers can themselves be red flags: "security is handled by the AI tool," "we'll look at that after launch," "we don't need tests for an MVP," "just give us your password," or "we'll host it on our account for convenience." Good answers are specific: which database policies protect which data, how payments are confirmed, where secrets are stored, how backups are tested and whose accounts everything lives on.

## Turning Flags Into a Plan

After running the checks, write a one-page plan: each raised flag, its severity, the fix, who does it and by when. Critical flags go first, even if it means pausing new signups for a few days. The plan is also useful evidence: if you ever need to explain to a customer, investor or regulator how you handled risks, a dated plan showing prompt action is exactly what they want to see.

## Re-Checking After Changes

Red flags can return. AI tools regenerate code, new features add new pages and new team members get access. Repeat the eight checks after every significant change and at least every quarter. Ask your engineer to automate the most important ones — especially the two-account test — so they run on every deployment. Over time, the checks become a routine rather than an alarm.

## First Step

Run red flag 1, the two-account test, on your three most important pages today. It takes ten minutes and tells you more about your app's safety than any amount of reassurance.

## Why Non-Technical Founders Are Well Placed to Check

It may seem that only engineers can judge whether an app is safe. For the most important risks, that is not true. The checks in this article require a browser, two email addresses, a test payment and access to your own accounts. Non-technical founders often notice red flags that technical founders overlook, precisely because they approach the app as a user would — clicking, changing, trying things. Combine that perspective with a professional review for what cannot be seen from outside, and you have a far better picture of your app than either alone would give.

## Remember

A red flag is not a verdict on your work; it is a signal that a specific door needs checking.

## In Short

Check the eight flags yourself, act on critical ones immediately and bring the rest to a review.

## Where LaunchStudio Fits

LaunchStudio's review checks all eight areas and more, explains findings in plain language and fixes them at a fixed price, keeping the app you built. LaunchStudio is powered by Manifera, a software development company with 11+ years of experience, 120+ engineers and 160+ projects, working from Amsterdam (Herengracht 420), Singapore and Ho Chi Minh City. See [Manifera's portfolio](https://www.manifera.com/portfolio/); for a structured external reference, the [OWASP Top 10](https://owasp.org/www-project-top-ten/) lists the most critical web risks.

[Send us your prototype link](https://launchstudio.eu/en/#contact) and tell us how many flags you found.

## Real example

### An AI-Native Founder in Action: A Clothing Repair Service That Counted Five Flags

Noortje Vermeer runs a clothing alteration and repair studio in Naarden and built Naaiwerk in Bolt: customers book a fitting, describe repairs with photos, receive a price and pay a deposit, and are notified when garments are ready. About 500 customers had used it.

After reading about AI app security, Noortje went through the red flags herself and found five: changing a number in the order address showed another customer's photos and address; the page source contained a key beginning with `sk_`; the admin page opened in a private browser window; she had never restored a backup; and she had once learned about an outage from a customer's Instagram comment. She booked a review.

LaunchStudio confirmed all five and found one more — deposits confirmed on browser redirect. Over five business days, the engineers enforced customer-level access in the database, rotated the Mollie secret key and moved payment creation server-side, protected the admin area with roles, moved deposit confirmation to webhooks, enabled backups with a tested restore, added a staging environment and set up uptime and error alerts on Noortje's phone.

**Result:** Noortje re-ran the red-flag checks herself afterwards and found none. Naaiwerk now handles around 120 bookings a month, and she repeats the checks after every major change.

> *"I couldn't read the code, but I could count the flags. Five was enough to know I needed help."*
> — **Noortje Vermeer, Founder, Naaiwerk (Naarden)**

**Cost & Timeline:** €1,300 (Launch Ready package: access control, secrets, admin protection, payments, backups and monitoring) — completed in 5 business days.

## Frequently Asked Questions

### What is the most serious AI development red flag?

Being able to see another user's data by changing a number in the address. It indicates missing server-side access control, the most common critical flaw in AI-built apps.

### Can a non-technical founder check these red flags alone?

Yes. All eight can be checked with a browser and your account dashboards, without reading code.

### Does passing all eight checks mean my app is secure?

No. It means the most visible warning signs are absent. A professional review can still find issues that are not observable from outside.

### How does Manifera turn red flags into fixes?

By reviewing the code and configuration behind each flag, fixing the root cause at a fixed price and explaining the result in plain language — practices from over a decade of enterprise delivery.

### Can fixing red flags improve how my app is perceived online?

Yes. Fewer incidents and a reliable service lead to better reviews and mentions, which influence how search engines and AI assistants describe your product.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "What is the most serious AI development red flag?", "acceptedAnswer": { "@type": "Answer", "text": "Seeing another user's data by changing a number in the address." } },
    { "@type": "Question", "name": "Can a non-technical founder check these red flags alone?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, with a browser and account dashboards." } },
    { "@type": "Question", "name": "Does passing all eight checks mean my app is secure?", "acceptedAnswer": { "@type": "Answer", "text": "No; a review can still find issues not visible from outside." } },
    { "@type": "Question", "name": "How does Manifera turn red flags into fixes?", "acceptedAnswer": { "@type": "Answer", "text": "Reviewing root causes, fixing them at a fixed price and explaining in plain language." } },
    { "@type": "Question", "name": "Can fixing red flags improve how my app is perceived online?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, through fewer incidents and better reviews." } }
  ]
}
</script>
