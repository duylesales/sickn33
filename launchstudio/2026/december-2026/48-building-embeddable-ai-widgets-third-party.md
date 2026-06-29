---
Title: Building Embeddable AI Widgets for Third-Party Websites
Keywords: Embeddable, AI, Widgets, Third-Party, Websites, Next.js, iframe
Buyer Stage: Consideration
---

# Building Embeddable AI Widgets for Third-Party Websites

You have built a phenomenal AI-powered customer support agent. It knows everything about a company's product line thanks to a massive RAG pipeline, and it can chat fluently with customers. There is just one problem: it lives on your domain (`app.yoursaas.com`). If a company wants to use your AI agent to support their customers, they have to link their customers away from their own website and over to yours. That is a terrible user experience. To unlock massive B2B growth, your AI SaaS cannot just be a destination; it must be **embeddable**. You must allow your customers to take your AI agent and inject it directly into their own websites using a simple `<script>` tag or `<iframe>`.

## The Two Architectures of Embeddable AI

There are two primary ways to distribute an embeddable AI widget. Both require careful handling of Cross-Origin Resource Sharing (CORS) and security, but they offer different levels of control.

### 1. The Iframe Approach (The Fastest)

An `<iframe>` is essentially a window into your application embedded on another site.

**How it works:**
You build a specific route in your Next.js application, for example, `/widget/[org_id]`. This page strips away all your standard SaaS navigation and only renders the AI chat interface. The customer embeds it on their site like this:

```html
<iframe src="https://app.yoursaas.com/widget/org_abc123" width="400" height="600" frameborder="0"></iframe>
```

**The Pros:**
- Extreme isolation. The host website's CSS and JavaScript cannot interfere with your AI chat interface.
- Fastest time to market.

**The Cons:**
- Visually rigid. If the customer wants the widget to "pop open" when a user clicks a button on their site, it is very difficult to coordinate that animation across the iframe boundary.

### 2. The Injected JavaScript Approach (The Premium Way)

This is the gold standard used by Intercom and Stripe. You provide the customer with a `<script>` tag that they place in their HTML `<head>`.

**How it works:**
The script downloads a bundled JavaScript file from your CDN. This script uses React (or vanilla JS) to dynamically create DOM elements on the host website, rendering a floating chat bubble in the bottom right corner. When clicked, it renders the full AI chat interface.

```html
<script src="https://cdn.yoursaas.com/widget.js" data-org-id="org_abc123"></script>
```

**The Pros:**
- Flawless integration. The widget feels like a native part of the host website.
- You can track events on the host website (e.g., "User clicked the checkout button, let's have the AI offer a discount").

**The Cons:**
- CSS conflicts. The host website's aggressive global CSS might accidentally style your AI chat buttons, breaking your layout. You must aggressively scope your CSS (using Shadow DOM or strict BEM naming conventions).

## Securing Embeddable AI Endpoints

When your AI widget lives on `customer-site.com`, it must make API calls back to your backend at `api.yoursaas.com` to stream the LLM responses. This exposes a massive security vulnerability.

If your widget only relies on the `data-org-id="org_abc123"` attribute to know which RAG database to query, a malicious hacker can simply copy that ID, put the widget on their own spam site, and drain your customer's API credits.

**The Defense Architecture:**

1. **Domain Whitelisting:** In your SaaS dashboard, force the customer to explicitly define which domains are allowed to host their widget (e.g., `www.megacorp.com`).
2. **Strict CORS Policies:** Your Next.js API routes must enforce strict CORS. If an API request comes from an `Origin` that is not in the organization's whitelist, reject it immediately with a `403 Forbidden`.
3. **Rate Limiting by IP:** Since widget users are anonymous, you cannot rate-limit them by a user ID. You must use Upstash Redis at the Vercel Edge to rate-limit AI queries by the end-user's IP address, preventing a single visitor from exhausting the organization's quota.

## Handling Authentication in Widgets

Usually, embeddable AI agents talk to anonymous website visitors. But what if the widget needs to know who the user is? (e.g., An internal IT helpdesk AI embedded in a corporate intranet).

Do not try to pass JWTs through url parameters or complex iframe messaging. Use standard OAuth flows or a secure signed-token exchange where the host server securely signs a payload identifying the user, passes it to the widget, and the widget verifies the signature with your backend before starting the AI session.

## The LaunchStudio Approach

At LaunchStudio, we know that embeddable widgets are the ultimate growth hack for B2B AI products. We architect secure, highly performant embeddable widget systems using Next.js. We build the Shadow DOM JavaScript bundles to prevent CSS conflicts, configure strict CORS policies tied to Supabase whitelists, and implement Edge rate-limiting to protect your LLM budget.

---

*Want to let your customers embed your AI product directly on their websites? LaunchStudio builds secure, embeddable widget architectures for AI SaaS platforms. [Get in touch](https://launchstudio.eu/en/).*
