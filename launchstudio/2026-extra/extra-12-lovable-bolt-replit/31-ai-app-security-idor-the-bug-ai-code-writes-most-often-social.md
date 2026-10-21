🚨 Coen Bleeker's Factuurstroom handles invoicing for 380 freelancers and small agencies. Invoices lived at a URL ending in a sequential number. A user mistyped his own invoice number — and landed on somebody else's: client name and address, amounts, and the freelancer's bank details. 😳

He tried three more before writing to Coen. Every endpoint required a login. None checked ownership. Here's the bug AI-generated code writes most often: 🧠

❌ 31 of 47 endpoints with an identifier and no ownership check
❌ Nested records fetched by ID without validating the parent invoice
❌ Row-level security enabled on only four of fourteen tables
❌ Sequential invoice IDs in URLs, inviting enumeration

✅ Every query scoped to the session's account, via a shared data-access helper that makes the safe way the default
✅ Nested identifiers validated against their parent record
✅ RLS policies on all 14 tables, and random IDs in URLs — with the readable invoice number kept for display
✅ An automated test that signs in as a second organisation, requests every ID, and fails the build on any data

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we open your records from another account — ten minutes, and the test that matters most. 🔍

His result: two business days and €3,800 later, log review found 61 cross-account requests in fourteen months; the affected businesses and the Dutch Data Protection Authority were notified. The automated test has since caught two new faulty endpoints before deployment. 🚀

👉 IDOR, the bug AI code writes most often: https://launchstudio.eu/en/blog/ai-app-security-idor-the-bug-ai-code-writes-most-often

#AppSecurity #IDOR #AccessControl #Lovable #LaunchStudio #Manifera
