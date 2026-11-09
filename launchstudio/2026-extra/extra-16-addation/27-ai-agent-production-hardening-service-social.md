📬 Maarten Bos runs a bookkeeping SaaS for small contractors from Breda and built Factuurmaat with Claude Code and Supabase. Its agent read supplier emails, extracted invoices, matched them to purchase orders and could schedule payments through a banking integration. Customers loved it. Then a security engineer friend sent one email with hidden text, and the agent scheduled a payment to a new bank account without any check. 😨

The risk review found more: 🧠

❌ A database key with access to all customers
❌ External emails processed with every tool available, including payments
❌ No limits on steps or spend, and retries that could duplicate payments
❌ The only record a chat transcript that disappeared after a week

✅ A two-stage design: read-only tools for emails, actions only after a clear user preview
✅ Tools scoped to the customer's organisation and the user's permissions
✅ Payments to new or changed accounts blocked until confirmed outside the agent, with idempotency keys
✅ Limits, an audit trail, a kill switch per customer and 80 evaluation scenarios, 20 of them manipulated

At **LaunchStudio**, backed by Manifera's 11+ years of software and security engineering, we make AI agents controllable without making them less useful. 🛠️

His result: €6,900, eighteen business days. All 20 manipulated emails were blocked, and 11 real suspicious invoices were flagged in three months. 🚀

👉 AI agent production hardening service: https://launchstudio.eu/en/blog/ai-agent-production-hardening-service

#AIAgents #PromptInjection #Security #ClaudeCode #AIFounder #LaunchStudio #Manifera
