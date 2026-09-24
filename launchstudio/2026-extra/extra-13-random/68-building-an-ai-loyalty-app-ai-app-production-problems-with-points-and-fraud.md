---
Title: "Building an AI Loyalty App? AI App Production Problems With Points and Fraud"
Keywords: ai app production problems, loyalty app, points ledger, loyalty fraud, bolt loyalty app, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Building an AI Loyalty App? AI App Production Problems With Points and Fraud

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Building an AI Loyalty App? AI App Production Problems With Points and Fraud",
  "description": "Loyalty points are a currency, and AI-built loyalty apps rarely treat them like one. This article covers the AI app production problems in loyalty systems — balance fields, replayable QR codes, race conditions, expiry, refunds and liabilities — and how a ledger fixes them.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-07",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/building-an-ai-loyalty-app-ai-app-production-problems-with-points-and-fraud" }
}
</script>

A loyalty app looks like the friendliest possible product: collect stamps, earn points, get a free coffee. Under the surface it is a small bank. Points are a currency that customers value, shops pay for and fraudsters love. AI coding tools build loyalty apps as if points were a number on a profile, and that is where the AI app production problems start — duplicated rewards, balances that drift, and a single screenshot of a QR code redeemed a hundred times.

## Points Are Money, So Treat Them Like Money

The typical AI-generated design has a `points` column on the user table. Earning adds to it; redeeming subtracts. It works in a demo. In production it causes:

- **Lost updates** when two transactions change the balance at the same time.
- **No history,** so nobody can explain why a customer has 340 points.
- **No reversals,** so refunded purchases keep their points.
- **No reconciliation** between what shops paid for and what customers received.

The production approach is a **ledger**: every earn, redeem, expiry, reversal and manual adjustment is an immutable entry with an amount, a reason, a reference and a timestamp. The balance is the sum of entries (or a cached value derived from them). Mistakes are corrected with new entries, never by editing old ones.

## Race Conditions at the Counter

A customer taps "redeem" twice on a slow connection, or two staff members scan the same card simultaneously. If the app checks the balance and then subtracts in separate steps, both redemptions succeed and the balance goes negative. Redemptions must happen in a single database transaction with a check that the balance is sufficient, plus an idempotency key per request so retries do not double-spend.

## QR Codes That Can Be Replayed

Many AI-built loyalty apps generate a static QR code per customer or per reward. Anyone can screenshot it, share it in a group chat and redeem it repeatedly. Safer patterns include:

- **Short-lived codes** that rotate every minute or so, generated for a specific redemption.
- **Single-use tokens** marked as used in the database the moment they are scanned.
- **Staff-side scanning** that validates on the server, not in the customer's app.

The same applies to earning: a static "scan to get a stamp" poster at the counter will be photographed and scanned from home.

## Fraud and Other AI App Production Problems You Should Expect

- Fake accounts to collect sign-up bonuses repeatedly
- Referral loops between accounts controlled by one person
- Staff issuing points to themselves or friends
- Scripts calling the earn endpoint directly
- Points transferred to accounts that resell rewards

Defences are mostly simple: rate limits, one sign-up bonus per verified phone number or payment method, staff actions logged per employee, earning only via server-validated transactions, and anomaly alerts for unusual patterns.

## Expiry, Refunds and Terms

Points need clear rules: when they expire, whether refunds reverse them, what happens to points when a shop leaves the programme. Each rule becomes a ledger entry type and a scheduled job. Your terms should say the same thing the code does.

## Multi-Shop Programmes and Liability

When several shops share a programme, each point issued is a promise someone must honour. The ledger must record which shop issued and which shop redeemed, so settlements between shops are correct. Outstanding points are effectively a liability; your accountant may want to know how many exist.

## A Ledger Schema You Can Start With

Solving AI app production problems in loyalty apps starts with replacing a balance column by a ledger:

```sql
CREATE TABLE points_ledger (
  id              bigserial PRIMARY KEY,
  member_id       uuid NOT NULL,
  program_id      uuid NOT NULL,
  shop_id         uuid,
  entry_type      text NOT NULL,   -- earn, redeem, expire, reverse, adjust
  points          int  NOT NULL,   -- positive for earn, negative for redeem/expire
  reference       text,            -- receipt number, voucher id, reason
  idempotency_key text UNIQUE,
  created_by      uuid,            -- staff member or system
  created_at      timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX points_ledger_member ON points_ledger (member_id, created_at);
```

The balance is `SUM(points)` for a member, optionally cached in a table updated in the same transaction. Entries are never updated or deleted; corrections are new entries with type `adjust` or `reverse` and a reference to the original. This makes every balance explainable and every mistake reversible.

## Redemption as a Single Transaction

A redemption must check and deduct in one step:

```sql
BEGIN;
SELECT balance FROM member_balances WHERE member_id = $1 FOR UPDATE;
-- application checks balance >= cost
INSERT INTO points_ledger (member_id, program_id, shop_id, entry_type, points, reference, idempotency_key, created_by)
VALUES ($1, $2, $3, 'redeem', -$4, $5, $6, $7);
UPDATE member_balances SET balance = balance - $4 WHERE member_id = $1;
COMMIT;
```

The row lock prevents two redemptions from spending the same points, and the idempotency key ensures that a retried request after a dropped connection does not deduct twice.

## Secure Codes for Earning and Redeeming

Replace static QR codes with codes that carry little value if copied:

- **Redemption codes** generated on demand, valid for a minute or two, for a specific reward and member, marked used on scan.
- **Earning** via staff scanning the member's rotating code and entering the purchase amount, or via integration with the till system, rather than members scanning a static poster.
- **Signed codes** (for example containing a server-generated signature) so fabricated codes are rejected without a database lookup.

Log every scan with shop, device and staff member for auditing.

## Fraud Signals Worth Monitoring

| Signal | Possible abuse | Response |
| --- | --- | --- |
| Many accounts from one device or IP | Bonus farming | Limit bonuses, require verification |
| Points issued far above typical purchase size | Staff misuse | Alert shop owner, require approval above threshold |
| Redemptions at many shops in minutes | Shared screenshots or credential sharing | Short-lived codes, rate limits |
| Referral chains between new accounts | Referral fraud | Reward only after qualifying purchases |
| Frequent adjustments by one staff member | Manipulation | Review audit log |

Simple dashboards and weekly reviews catch most patterns before they become costly.

## Settlement Between Participating Shops

In multi-shop programmes, settlement is the financial heart. Record for each entry which shop issued points and which shop redeemed them; value points at an agreed rate; produce a monthly statement per shop showing points issued, points redeemed and the resulting balance to pay or receive. Reconcile statements against the ledger and keep them immutable once issued. Clear settlement rules — agreed in writing by participating shops — prevent disputes that can break up a local programme.

## Expiry and Accounting

Expiry rules — for example points valid for 12 months after earning — are implemented as scheduled jobs that add expiry entries per member, oldest points first. Notify members before points expire, which also encourages visits. For accounting, outstanding points represent an obligation; your accountant may want regular reports of issued, redeemed, expired and outstanding points to reflect this properly in the books.

## Privacy in Loyalty Programmes

Loyalty data reveals shopping habits. Collect only what the programme needs, explain clearly how data is used, obtain consent for marketing and personalised offers separately, and let members see their history and delete their account. Participating shops should see only their own customers' interactions unless members agree to broader sharing.

## Integrating With Till Systems

The most reliable way to issue points is from the till: the purchase amount comes from the point-of-sale system, not from manual entry. Many POS systems offer APIs or integrations; where they do not, a simple flow where staff scan the member code and the POS sends the amount works well. Integration reduces staff errors and staff fraud, and gives both shops and the programme accurate data. Use per-shop API credentials, idempotent processing of each transaction and reconciliation reports that compare POS totals with points issued.

## Designing Rewards That Resist Gaming

Reward design influences fraud. Rewards that can be redeemed for cash-like value (vouchers usable anywhere) attract more abuse than rewards tied to experiences or specific products. Thresholds, caps per period and minimum purchase amounts for earning reduce gaming. Referral bonuses paid only after the referred member's first qualifying purchase remove most referral fraud. Before launching a promotion, ask "how would someone exploit this?" and set limits accordingly.

## Promotions Without Chaos

Double-points days and bonus campaigns cause spikes and edge cases. Configure promotions as data — start and end time in local time, eligible shops and products, multiplier or bonus, caps per member — rather than code changes. Test them on staging with realistic transactions, monitor issuance during the promotion and have a way to end a campaign early if something goes wrong.

## Member Experience

Members judge a loyalty app by simplicity: fast access to their code (even offline), a clear balance with history, understandable rewards and reminders before points expire. Showing the history — "earned 12 points at the bakery on Tuesday" — builds trust and reduces support questions. It is only possible with a ledger, which is one more reason the ledger is worth building from the start.

## Support Tools for Shops and Administrators

Shops need to correct mistakes — a wrong amount entered, a refund — without contacting the programme administrator for every case. Give shop managers a limited adjustment tool with reasons required and thresholds above which approval is needed; give administrators a view of each member's ledger and all adjustments. Every correction becomes a new ledger entry, preserving the complete history.

## Reporting to Participating Shops

Shops stay in a programme when they see its value: customers who visit more often, cross-visits from other shops, redemption patterns and the net settlement position. Monthly reports built from the ledger — not from estimates — make the programme's value visible and keep participation high.

## When the Programme Grows

As a local programme grows to more shops or towns, expect new requirements: regional rules, different point values, separate settlement groups and possibly regulatory questions if points begin to function like a payment instrument across many unrelated merchants. Keep an eye on this boundary and take advice as the programme expands, so growth does not unexpectedly change the rules that apply to you.

## The Loyalty Principle

Treat points as money from day one: every movement recorded, every redemption atomic, every code short-lived and every correction a new entry. A programme built this way can grow from one street to a whole town without the bookkeeping ever falling apart.

## A Quick Test

Try redeeming the same reward twice from two phones at the same moment. If both succeed, start with the ledger and transactions described above.

## Where LaunchStudio Fits

LaunchStudio turns AI-built loyalty apps into systems that hold up: a points ledger with migration from existing balances, transactional redemptions with idempotency, rotating single-use codes, staff audit trails, fraud controls, expiry jobs and settlement reports — with the customer-facing app unchanged. LaunchStudio is powered by Manifera, a software development company with 11+ years of experience building transactional systems for clients such as Vodafone, with engineers in Ho Chi Minh City and offices in Amsterdam and Singapore. See [Manifera's technologies](https://www.manifera.com/about-us/manifera-technologies/). Martin Fowler's writing on [accounting patterns](https://martinfowler.com/eaaDev/AccountingNarrative.html) explains why ledgers beat balance fields.

[Get a fixed-price quote](https://launchstudio.eu/en/#contact) before your next promotion goes live.

## Real example

### An AI-Native Founder in Action: A Town-Wide Stamp Card and a Shared Screenshot

Daan Koopman, who manages a shopping street association in Bergen op Zoom, built Spaarpas in Bolt: a digital stamp card shared by 34 local shops. Customers collect points at any participating shop and redeem them for vouchers at others; shops pay a monthly fee and settle redeemed vouchers at month end. About 5,200 residents signed up in the first three months.

The first promotion — double points on a Saturday — exposed everything. Each customer had a static QR code, and points were added by staff scanning it and typing an amount. Screenshots of vouchers were redeemed at several shops. A group of accounts collected the sign-up bonus dozens of times with disposable email addresses. Two shops found that their tablets had issued points twice when the connection dropped and staff retried. At month end, the settlement report did not match what shops remembered, and there was no history to check.

Over nine business days, LaunchStudio's engineers replaced the balance column with a ledger, reconstructing opening balances from available logs and flagging uncertain accounts, made earning and redemption transactional with idempotency keys, replaced static codes with rotating single-use codes validated on the server, tied sign-up bonuses to verified phone numbers, logged every staff action per employee, added expiry and refund reversals, and built a monthly settlement report per shop.

**Result:** The next promotion ran without duplicate redemptions, and the month-end settlement matched to the voucher. Spaarpas expanded to 51 shops, and the association's treasurer now uses the ledger report instead of a spreadsheet.

> *"We thought we'd built a stamp card. We'd actually built a small currency with no bookkeeping."*
> — **Daan Koopman, Founder, Spaarpas (Bergen op Zoom)**

**Cost & Timeline:** €2,600 (Launch Ready package: ledger, transactional redemptions, secure codes, fraud controls and settlement) — completed in 9 business days.

## Frequently Asked Questions

### Why is a points balance column a problem in a loyalty app?

Concurrent updates can overwrite each other, and there is no history to explain, audit or reverse changes. A ledger of immutable entries solves both.

### How do I stop customers from reusing a screenshot of a QR code?

Use short-lived, single-use codes validated and marked as used on the server at the moment of scanning.

### What loyalty fraud should I expect at launch?

Repeated sign-up bonuses, referral loops, staff issuing points to themselves and scripted calls to earning endpoints. Rate limits, verification and staff audit logs cover most of it.

### How does Manifera's transactional experience apply to loyalty systems?

Manifera builds systems where every unit of value must be traceable. The same ledger, idempotency and reconciliation patterns apply to loyalty points.

### Can a local loyalty programme gain visibility through search and AI assistants?

Yes. A clear public page listing participating shops, rewards and rules, with local business structured data, helps residents and AI assistants find the programme.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Why is a points balance column a problem in a loyalty app?", "acceptedAnswer": { "@type": "Answer", "text": "Concurrent updates overwrite each other and there is no history; a ledger fixes both." } },
    { "@type": "Question", "name": "How do I stop customers from reusing a screenshot of a QR code?", "acceptedAnswer": { "@type": "Answer", "text": "Use short-lived single-use codes validated on the server." } },
    { "@type": "Question", "name": "What loyalty fraud should I expect at launch?", "acceptedAnswer": { "@type": "Answer", "text": "Repeated sign-up bonuses, referral loops, staff abuse and scripted earning, mostly stopped by limits, verification and logs." } },
    { "@type": "Question", "name": "How does Manifera's transactional experience apply to loyalty systems?", "acceptedAnswer": { "@type": "Answer", "text": "The same ledger, idempotency and reconciliation patterns used for traceable value apply." } },
    { "@type": "Question", "name": "Can a local loyalty programme gain visibility through search and AI assistants?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, with a public page of shops, rewards and rules using local structured data." } }
  ]
}
</script>
