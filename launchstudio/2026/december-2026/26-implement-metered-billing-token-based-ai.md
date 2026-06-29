---
Title: How to Implement Metered Billing for Token-Based AI Products
Keywords: Metered, Billing, Token-Based, AI, Products, Stripe
Buyer Stage: Consideration
---

# How to Implement Metered Billing for Token-Based AI Products

Pricing an AI SaaS is notoriously difficult. If you charge a flat $20/month, 90% of your users will be profitable, but 10% will be "power users" who burn through $150 of OpenAI API credits every month, destroying your margins. The only mathematically sound way to price a high-volume AI product—where inference costs scale linearly with usage—is **Metered Billing** (also known as usage-based billing). You charge the customer based on exactly how many tokens they consume. While this protects your margins perfectly, implementing metered billing requires a robust architectural bridge between your Next.js backend, your database, and Stripe.

## The Flawed Approach: Direct Stripe Webhooks

The instinct for many developers is to report usage directly to Stripe every time the user makes an AI query:

1. User clicks "Generate."
2. Node.js backend calls OpenAI.
3. Node.js backend immediately calls the Stripe API: `stripe.subscriptionItems.createUsageRecord({ quantity: 1500_tokens })`.

**This approach will crash your application.**
- Stripe's API is not designed to handle high-frequency, real-time usage reporting. If your app processes 50 requests per second, you will hit Stripe rate limits instantly.
- If the Stripe API call fails (network timeout), you lose that revenue forever.
- It adds 300ms of latency to every single user action.

## The Robust Architecture: Aggregation and Reporting

A production-grade metered billing system decouples the *consumption* of tokens from the *reporting* of tokens. 

### Step 1: The Local Ledger (Supabase)

When a user executes an AI query, your backend must record the token usage in your own database (Supabase) in real-time. This is your internal ledger.

```sql
CREATE TABLE ai_usage_ledger (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  organization_id UUID NOT NULL REFERENCES organizations(id),
  timestamp TIMESTAMPTZ DEFAULT NOW(),
  model VARCHAR NOT NULL,
  prompt_tokens INT NOT NULL,
  completion_tokens INT NOT NULL,
  billed_to_stripe BOOLEAN DEFAULT FALSE
);
```

When your Next.js backend receives the API response from OpenAI, it extracts the token counts (included in the `usage` object of the OpenAI response) and `INSERT`s a row into this table. This database write is extremely fast and entirely under your control.

### Step 2: The Aggregation Cron Job

Instead of reporting to Stripe on every query, you aggregate the usage and report it to Stripe in bulk on a schedule (e.g., once an hour, or once a day).

You can use a scheduled Supabase Edge Function or an external cron service (like Inngest or a standard Vercel Cron Job). 

The cron job executes the following logic:
1. Query the `ai_usage_ledger` for all rows where `billed_to_stripe = FALSE`.
2. Group the rows by `organization_id` and sum the total tokens.
3. For each organization, make a single API call to Stripe:
   ```typescript
   await stripe.subscriptionItems.createUsageRecord(
     subscriptionItemId, 
     { quantity: totalTokens, timestamp: Math.floor(Date.now() / 1000), action: 'increment' }
   );
   ```
4. Update the rows in `ai_usage_ledger`, setting `billed_to_stripe = TRUE`.

This architecture is infinitely scalable. Whether an organization makes 1 query or 10,000 queries in an hour, you only make one API call to Stripe.

## The Hybrid Model: Credits + Metered

Pure metered billing has a UX problem: users hate unpredictability. They fear "leaving the lights on" and getting a $5,000 bill at the end of the month.

The standard industry compromise is the **Hybrid Model**:
- The user pays a flat $50/month base subscription.
- This subscription includes 1,000,000 tokens (or "credits").
- If they exceed 1,000,000 tokens, they are billed on a metered basis (e.g., $10 per 100,000 additional tokens).

Stripe handles this beautifully using "Tiers" in their billing portal. Your application logic remains exactly the same—you still report all usage via the cron job. Stripe's billing engine automatically handles the math, applying the usage against their free allowance and only charging the credit card for the overage.

## Handling Pre-paid Credits

Some AI startups prefer a "Top-up" model. The user buys $20 worth of credits, and the app deducts from that balance in real-time. 

In this scenario, you must enforce the check synchronously. Before making the OpenAI call, you query Supabase: `SELECT balance FROM wallets WHERE user_id = X`. If the balance is less than the estimated cost of the prompt, you return a `402 Payment Required` error. After the OpenAI call succeeds, you decrement the balance using a secure Postgres RPC function to avoid race conditions.

## The LaunchStudio Approach

At LaunchStudio, we build AI SaaS products that are structurally profitable from day one. We implement enterprise-grade metered billing architectures that decouple real-time token tracking in Supabase from batched reporting to Stripe. We ensure your revenue logic is flawless, your API limits are enforced, and your profit margins are protected against power users.

---

*Struggling to figure out how to charge for your AI product without losing money on API costs? LaunchStudio implements robust metered billing and hybrid pricing models for AI startups. [Let's talk pricing architecture](https://launchstudio.eu/en/).*
