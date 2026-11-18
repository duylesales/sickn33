🧊 A painting company's planner: the iceberg

ABOVE THE WATERLINE (what everyone saw)
Schildersplanner, built in Lovable by Sabine Kroes, co-owner of a painting company in Heerhugowaard with fourteen painters. Customers request quotes, the office plans jobs, painters log hours from their phones. It never broke. Three other painting companies were licensing it.

〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️

BELOW THE WATERLINE (what nobody saw)
Eleven n8n workflows doing the real work: confirmations, invoices in the accounting software, a Google Sheet the office depended on, and payment reminders. And underneath them:
• An invoice workflow that retried on timeouts without checking whether the invoice already existed
• A payment reminder workflow triggered from the browser, through a public webhook URL with no authentication
• Over 200 failed executions in two months, and nobody notified
• Every workflow running on Sabine's personal Google and accounting credentials, with full access
• Execution logs keeping customer addresses and job notes forever, on a US-hosted cloud plan
• Two licensees' data flowing through the same workflows, without separation

It surfaced when one customer asked why she'd received three identical invoices, and another hadn't received one at all for a job finished six weeks earlier.

WHAT LAUNCHSTUDIO BUILT UNDER WATER (7 business days, €1,900)
⚓ Invoice creation moved into the app backend, with idempotency keys and a record of issued invoices
⚓ Every webhook trigger authenticated, and called from the server
⚓ An error workflow notifying the office by email and Slack
⚓ Company service accounts per licensee, instead of personal credentials
⚓ n8n on an EU-hosted instance, with 14-day log retention
⚓ Workflows exported to Git, with separate test copies
⚓ The missing and duplicate invoices reconciled

Duplicate and missing invoices stopped. Failed executions now reach the office within minutes. The four painting companies run on separated workflows, and Sabine has added two more licensees.

"The app never broke. The invisible part behind it broke quietly, and our customers were the ones who noticed." - Sabine Kroes

https://launchstudio.eu/en/blog/ai-app-production-problems-in-n8n-and-make-automations-the-workflow-glue-that-breaks

#n8n #Make #Automation #Lovable #LaunchStudio #Manifera
