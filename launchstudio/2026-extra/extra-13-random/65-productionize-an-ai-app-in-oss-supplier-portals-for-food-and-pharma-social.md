📋 AUDIT REPORT (pre-audit): Recepturo specification portal

REQUEST FROM THE RETAILER'S AUDITOR
Show the specification history for one product line.

FINDINGS
❌ Document history: not available. New uploads overwrote old ones, so only current files existed.
❌ Approval records: none showed who had approved what.
❌ Approval integrity: approvals could be edited afterwards.
❌ Supplier separation: suppliers could open other suppliers' documents through the API by changing an ID.
❌ Certificate expiry reminders: stopped three months earlier when a scheduled function failed. Nobody noticed.

Ruud van Kessel spent fifteen years as a quality manager at a food producer near Oss before founding Recepturo, built in Lovable: food producers request and manage specifications, allergen declarations and certificates from their ingredient suppliers. Seven producers and about 230 suppliers used it. Then one producer's largest retail customer scheduled a supplier audit.

In quality management, a document without its history isn't evidence. The portal had kept the documents, and thrown the evidence away.

CORRECTIVE ACTIONS (LaunchStudio, Launch & Grow, 15 business days, €4,600, plus €49/month)
✓ Document versions, with statuses and validity periods
✓ Existing files migrated as version one, with their upload dates
✓ An append-only audit trail, stored separately and readable by quality managers
✓ Supplier and producer separation, enforced with Row Level Security
✓ Expiry reminders rebuilt as monitored scheduled jobs, with escalation
✓ An audit export: a time-stamped package per product
✓ Hosting in an EU region, with backups and a tested restore

AUDIT OUTCOME
The producer passed the retail audit using Recepturo's export, and the auditor's report noted the document control positively. Recepturo grew to 16 producers the following year, two of them in pharmaceutical excipients.

"In quality management, a document without its history isn't evidence. My portal had the documents and had thrown the evidence away." - Ruud van Kessel

https://launchstudio.eu/en/blog/productionize-an-ai-app-in-oss-supplier-portals-for-food-and-pharma

#FoodSafety #Pharma #AuditTrail #Lovable #LaunchStudio #Manifera
