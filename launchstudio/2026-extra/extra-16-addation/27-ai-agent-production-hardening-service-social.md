🕵️ How one email could have paid a fake invoice

From an attacker's point of view, the target was simple: Factuurmaat's inbox agent. It read incoming supplier emails, extracted invoices, matched them to purchase orders and could schedule payments through a banking integration.

So the attacker's plan would need only one thing: an email with hidden text.

Maarten Bos, who runs Factuurmaat from Breda and built it with Claude Code and Supabase, found this out the safe way. A security engineer friend ran the test. The hidden text made the agent schedule a payment to a new bank account, with no check at all.

The risk review found why it was so easy:
• The agent used a database key with access to every customer
• It processed external emails with every tool available, payments and outgoing email included
• No limits on steps or spend
• Retries could create duplicate scheduled payments
• The only record was a chat transcript that disappeared after a week

How LaunchStudio closed it (18 business days, €6,900, plus €49/month):
✓ Two stages: a reading stage with read-only tools producing structured invoice data, and an action stage that runs only after a user reviews a clear preview
✓ Tools scoped to the customer's organisation, acting with the user's own permissions
✓ Payments to new or changed bank accounts blocked until the customer confirms outside the agent flow
✓ Idempotency keys on scheduled payments
✓ Step, token and spend limits
✓ An audit trail of every run, and a kill switch per customer
✓ An evaluation set of 80 scenarios, including 20 manipulated emails

In testing, all 20 manipulated emails were blocked or flagged. In the first three months of production, the agent flagged 11 real suspicious invoices for review. Maarten published a page explaining the controls, and two accountancy firms that had hesitated signed up after reading it.

"The agent was my best feature and my biggest risk. Now it still does the boring work, but it cannot move money without a human saying yes." - Maarten Bos

https://launchstudio.eu/en/blog/ai-agent-production-hardening-service

#AIAgents #PromptInjection #Security #ClaudeCode #AIFounder #LaunchStudio #Manifera
