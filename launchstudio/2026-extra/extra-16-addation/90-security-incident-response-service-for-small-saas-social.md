🔓 Sarah Kuipers runs a bookkeeping SaaS for freelancers from Haarlem, built with Bolt and Supabase. On a Tuesday afternoon a customer emailed: by changing a number in the address bar, she could open other customers' invoices, with names, addresses and amounts. Sarah contacted LaunchStudio within the hour. The GDPR's 72-hour clock had started. ⏳

What had gone wrong: 🧠

❌ An AI-generated change eleven days earlier had loosened the invoices policy
❌ Invoice PDFs sat in a public bucket
❌ A service key was used in a client-side function
❌ No tests or access logging to catch it

How the incident was handled: ✅

✅ Contained within ninety minutes: policy restored, PDFs moved to private storage with signed links, key rotated
✅ Logs and storage access records exported before anything else changed
✅ Impact assessed with facts: around 1,300 invoices reachable, with actual access by two other accounts to 14 invoices
✅ Her privacy adviser assessed the facts, the breach was reported to the Autoriteit Persoonsgegevens within 72 hours and affected customers informed, followed by access tests, Bolt instructions and invoice access logging

At **LaunchStudio**, backed by Manifera's 11+ years of operating systems for security-conscious clients and a CEO who co-founded a cybersecurity company, we bring calm, facts and a clear sequence of steps. 🛠️

Her result: €2,400, assessment done within 36 hours. Churn was minimal, and three months later the tests blocked a similar AI change before production. 🚀

👉 Security incident response service for small SaaS: https://launchstudio.eu/en/blog/security-incident-response-service-for-small-saas

#DataBreach #GDPR #IncidentResponse #Bolt #AIFounder #LaunchStudio #Manifera
