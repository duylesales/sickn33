---
Title: Building an AI Admin Dashboard with Next.js and Tremor
Keywords: Admin, Dashboard, AI, SaaS, Next.js, Tremor, React
Buyer Stage: Awareness
---

# Building an AI Admin Dashboard with Next.js and Tremor

When you launch an AI SaaS product, all your engineering effort goes into the customer-facing application. The LLM integration, the chat interface, the document parsing—that is what sells the product. But within weeks of going live, you will realize a painful truth: **you are flying blind**. You do not know which users are burning through API credits, which prompts are generating errors, or which models are driving up your OpenAI bill. You need an internal admin dashboard. For AI startups building on Next.js, the fastest and most elegant way to build this is with **Tremor**.

## Why AI SaaS Needs Specialized Analytics

A standard SaaS dashboard tracks MRR, active users, and churn. An AI SaaS dashboard needs to track entirely different metrics:

1. **Token Consumption per User:** In a traditional SaaS, a power user costs you slightly more server compute. In an AI SaaS, a power user can cost you $50/day in API fees. You need a leaderboard of top token consumers instantly available.
2. **Model Latency and Errors:** If OpenAI's `gpt-4o` API degrades, your app degrades. You need real-time charts tracking inference latency and 5xx error rates across different models.
3. **Prompt Auditing:** When a user reports a "hallucination," your support team needs to immediately pull up the exact system prompt, user prompt, and model temperature that generated that response.
4. **Feature Usage (RAG vs Chat):** Which features are driving API costs? You need to split costs between vector embedding generation (cheap) and long-context inference (expensive).

## Enter Tremor: The React Library for Dashboards

[Tremor](https://tremor.so/) is an open-source React component library built on top of Tailwind CSS, designed specifically for building dashboards. Instead of wrestling with raw Chart.js or D3, Tremor provides pre-styled, responsive charts, scorecards, and data tables that look like they belong in a million-dollar enterprise product.

### The Stack

- **Framework:** Next.js (App Router)
- **Styling:** Tailwind CSS + Tremor
- **Data Fetching:** Server Components connecting directly to Supabase/Postgres
- **Authentication:** Supabase Auth with Role-Based Access Control (RBAC)

## Building the Core Views

Here is how you structure the admin dashboard using Tremor components:

### 1. The Executive Overview (Scorecards)

The top of your dashboard should feature a grid of Tremor `Card` components containing key metrics:
- Total Tokens Consumed (Today)
- Estimated OpenAI/Anthropic Bill (MTD)
- Total Inference Errors (24h)
- Active Users vs Idle Users

```tsx
<Grid numItemsSm={2} numItemsLg={4} className="gap-6">
  <Card>
    <Text>API Spend (MTD)</Text>
    <Metric>$4,231.00</Metric>
    <Flex className="mt-4">
      <Text>+12.5% from last month</Text>
    </Flex>
  </Card>
  {/* Add more cards for Tokens, Errors, Users */}
</Grid>
```

### 2. Token Consumption Trends (Area Charts)

Use Tremor's `AreaChart` to visualize token usage over time. This is critical for identifying sudden spikes (e.g., a user attempting to scrape your AI endpoint).

```tsx
<Card className="mt-6">
  <Title>Token Consumption Over Time</Title>
  <AreaChart
    className="h-72 mt-4"
    data={tokenData}
    index="date"
    categories={["GPT-4o", "Claude-3.5-Sonnet", "Embeddings"]}
    colors={["blue", "emerald", "amber"]}
  />
</Card>
```

### 3. The Power User Leaderboard (Data Tables)

Use Tremor's `Table` component to rank users by API cost. If you offer a $20/month flat-rate plan, and a user is costing you $40 in API fees, your admin team needs to see this immediately to enforce fair use limits.

### 4. The Inference Log (Searchable Grid)

Build a detailed view where admins can search through the raw `ai_logs` table. When a user reports a bug, admins can search by `user_id` and view the exact JSON payload sent to the LLM.

## Securing the Admin Dashboard

An admin dashboard is a massive security liability. It provides full access to user data, API logs, and billing information. You must secure it ruthlessly:

1. **Strict RBAC:** Use Postgres Row-Level Security (RLS). Create a custom `role` column on your `users` table. The admin dashboard should only query data if `auth.jwt() ->> 'role' = 'admin'`.
2. **Separate Next.js Layout:** Put the admin dashboard under a `/app/(admin)/admin/` route group with a dedicated `layout.tsx`. Add a middleware that redirects non-admins immediately.
3. **Audit Logging:** Every action taken in the admin dashboard (e.g., manually granting a user extra credits, viewing a conversation log) must be logged in an `admin_audit_log` table.

## The LaunchStudio Approach

At LaunchStudio, we know that an AI startup without an admin dashboard is a startup that will eventually be bankrupted by unmonitored API costs or blind-sided by support tickets. For every AI SaaS we deploy, we build a comprehensive Next.js + Tremor admin portal. We connect it directly to the Supabase backend, visualizing token usage, RAG pipeline metrics, and system errors out of the box.

---

*Need visibility into your AI product's usage and costs? LaunchStudio builds production-ready AI SaaS platforms complete with enterprise-grade admin dashboards. [Talk to us](https://launchstudio.eu/en/).*
