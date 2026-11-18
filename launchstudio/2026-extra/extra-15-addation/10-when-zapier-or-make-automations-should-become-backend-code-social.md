🁢 The domino chain behind one course enrolment

Domino 1: A student pays through Mollie. A webhook fires.
Domino 2: Make creates the student in a CRM.
Domino 3: Another scenario grants course access in Supabase.
Domino 4: A third generates and emails an invoice through the accounting tool.
Domino 5: A fourth adds the student to the group call calendar.

When every domino falls in order, it's magic. Noor El Amrani, a financial coach in Almere, built Geldcoach Academie this way in Lovable: video lessons, worksheets and monthly group calls.

At around 300 enrolments a month, dominoes started falling the wrong way:
💥 A retried Mollie webhook sometimes sent two invoices
💥 Twice, the access scenario broke after an API change, and students who had paid couldn't log in for two days
💥 Refunds meant manual work in four tools
💥 Make became one of the biggest monthly costs
💥 Student names, emails and payment amounts passed through three platforms missing from the privacy policy

What LaunchStudio did (10 business days, €3,300):
• Documented all eleven scenarios and moved the four critical ones into Supabase edge functions
• Verified Mollie webhooks, recorded by payment ID and processed once
• Access, invoicing and calendar invites handled in one function, with retries and clear failure handling
• Invoices created with idempotency keys, and a refund flow that removes access and creates credit notes
• Alerts to Noor by email and SMS, convenience scenarios left in Make, and the privacy policy updated

Since then: no student double-invoiced or locked out after paying. Make costs down about 70%. Refunds are one button.

"Make let me start without a developer. It was never meant to be the place where my students' access depended on everything going right." - Noor El Amrani

When should automations become backend code? https://launchstudio.eu/en/blog/when-zapier-or-make-automations-should-become-backend-code

#Make #Zapier #Mollie #EdTech #AIFounder #LaunchStudio #Manifera
