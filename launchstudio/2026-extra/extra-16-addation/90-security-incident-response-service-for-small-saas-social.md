🚨 THE ORDER THAT MATTERS: stop it, keep the evidence, find out exactly what happened, then decide

THE TRIGGER
A Tuesday afternoon. A customer of Factuurvrij, a bookkeeping SaaS for freelancers that Sarah Kuipers built in Haarlem with Bolt and Supabase, emailed: by changing a number in the address bar, she could open other customers' invoices, with names, addresses and amounts. Sarah contacted LaunchStudio within the hour.

STEP 1: STOP IT (within ninety minutes)
✓ The invoices table policy restored, so customers see only their own records
✓ Invoice PDFs moved from a public bucket to private storage with signed links
✓ A service key found in a client-side function, rotated

STEP 2: KEEP THE EVIDENCE
✓ Logs and storage access records exported before anything else was changed

STEP 3: FIND OUT EXACTLY WHAT HAPPENED (within 36 hours)
• The vulnerable policy came from an AI-generated change, eleven days earlier
• Around 1,300 invoices had been reachable in that period
• Besides the reporting customer and Sarah's own test account, logs showed two more accounts accessing other customers' invoices: 14 invoices in total

STEP 4: DECIDE
✓ Sarah's privacy adviser assessed the facts
✓ Sarah reported the breach to the Autoriteit Persoonsgegevens within the 72-hour window
✓ Affected customers were informed, with a message drafted together
✓ Root causes fixed: access tests in the pipeline, project instructions for Bolt, and logging of invoice access
✓ An incident report documenting everything

The incident response cost €2,400.

Customers appreciated the quick, honest notification, and churn afterwards was minimal. Three months later, the access tests blocked a similar AI-generated change before it reached production.

"The worst hour of my business became manageable because someone knew the order: stop it, keep the evidence, find out exactly what happened, then decide." - Sarah Kuipers

https://launchstudio.eu/en/blog/security-incident-response-service-for-small-saas

#DataBreach #GDPR #IncidentResponse #Bolt #AIFounder #LaunchStudio #Manifera
