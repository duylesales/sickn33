🧪 Try this on your own app. It takes thirty seconds.

1. Log in and open one of your own records, say an invoice.
2. Look at the end of the URL. Is it a number?
3. Change it by one.

If someone else's record opens, you have the bug AI code writes most often.

One freelancer found it in Factuurstroom by accident: he mistyped his own invoice number and landed on somebody else's. He tried three more, then wrote to the founder. By then, he'd seen four invoices from three different businesses: client names and addresses, line items, amounts, and the freelancers' own bank details. 🧾

Coen Bleeker built Factuurstroom in Lovable: invoicing and payment follow-up for freelancers and small agencies, 380 users across the Netherlands. Invoices sat at URLs ending in a sequential number. Every endpoint checked for a valid session. None checked ownership. He'd spent a week on two-factor authentication, and left the front door of every record open.

What LaunchStudio changed (2 business days, €3,800):
✓ An inventory of 47 endpoints taking IDs: 31 had no ownership check
✓ All 31 fixed by scoping queries to the session's account, with a shared data-access helper so the scoped fetch is the default
✓ Nested records fixed too, like invoice lines and payments fetched by ID without validating the parent invoice
✓ Row Level Security on all 14 tables (it had been on 4)
✓ Random IDs in URLs, with the readable invoice number kept as a separate display field
✓ An automated test that logs in as a second organisation, requests every known ID, and fails the build if any data comes back
✓ Access logs reviewed to measure the exposure

The logs showed 61 cross-account requests over fourteen months: 54 from the four users who'd stumbled on it and stopped, and 7 from one account over one evening. Coen notified the affected businesses and the Autoriteit Persoonsgegevens. The automated test has since failed twice on new endpoints, both before deployment.

"Anyone who could log in could read every invoice in the system by typing a different number. I had spent a week on two-factor authentication and left the front door of every record open." - Coen Bleeker

https://launchstudio.eu/en/blog/ai-app-security-idor-the-bug-ai-code-writes-most-often

#AppSecurity #IDOR #AccessControl #Lovable #LaunchStudio #Manifera
