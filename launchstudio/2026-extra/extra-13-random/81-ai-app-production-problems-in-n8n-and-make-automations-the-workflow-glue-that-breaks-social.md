🚨 Sabine Kroes, co-owner of a painting company in Heerhugowaard with fourteen painters, built Schildersplanner in Lovable: customers request quotes, the office plans jobs and painters log hours from their phones. Behind it ran eleven n8n workflows — confirmations, invoices, a Google Sheet, payment reminders. Three other painting companies licensed it. Then one customer received three identical invoices, and another received none for a job finished six weeks earlier. 😳

The invoice workflow retried on timeouts without checking whether the invoice already existed. The reminder workflow was triggered from the browser through a public, unauthenticated webhook. Over 200 failed executions in two months notified nobody. Every workflow used Sabine's personal credentials, logs kept customer addresses forever on a US-hosted plan, and two licensees' data shared the same workflows. Here's where AI apps break in the n8n and Make glue: 🧠

❌ Retries that create duplicate invoices
❌ Public webhook triggers called from the browser
❌ Failed runs that alert nobody
❌ Personal credentials and no separation between customers

✅ Invoice creation moved into the backend with idempotency keys and a record of issued invoices
✅ All webhook triggers authenticated and called from the server, plus an error workflow alerting the office by email and Slack
✅ Company service accounts per licensee, n8n on an EU-hosted instance with 14-day log retention
✅ Workflows exported to Git with separate test copies — and missing and duplicate invoices reconciled

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we review the invisible part behind your app before your customers notice it. ⚙️

Her result: €1,900, seven business days. Duplicate and missing invoices stopped, failures now reach the office within minutes, and Sabine has added two more licensees. 🚀

👉 AI app production problems in n8n and Make automations: the workflow glue that breaks: https://launchstudio.eu/en/blog/ai-app-production-problems-in-n8n-and-make-automations-the-workflow-glue-that-breaks

#n8n #Make #Automation #Lovable #LaunchStudio #Manifera
