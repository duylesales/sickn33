⏳ Countdown to 1 January: the Belgian Peppol mandate

AUTUMN 2025
Kevin Peeters, a Flemish-Dutch founder living in Breda, runs Praktijkfactuur, built with Lovable and Supabase. Independent physiotherapists and small group practices in Flanders and the southern Netherlands use it to plan sessions and invoice clients, including companies that pay for employee treatments. About 140 practices, two thirds of them in Belgium.

Practices start asking: can we send Peppol invoices to the companies we bill?

The honest answer: not yet.
• Invoices were PDFs generated in the browser
• Business recipients' VAT numbers were optional free-text fields
• Credit notes weren't supported
• Totals sometimes differed by one cent from the sum of the lines, because amounts were stored as decimals

THE WORK (LaunchStudio, 15 business days, €5,800)
→ An access point provider integrated through its API
→ The invoice model mapped to Peppol BIS Billing 3.0, with validation and Dutch-language errors before sending
→ Required VAT and company number fields, plus a Peppol directory lookup that shows whether a company can receive e-invoices
→ Money migrated to integer cents, with consistent VAT rounding
→ Structured credit notes
→ Delivery and rejection statuses returned through verified, idempotent webhooks into a visible status column
→ Sent UBL files stored for the retention period

MID-DECEMBER
Peppol sending goes live, two weeks before the mandate applies.

Q1 2026
Around 3,900 Peppol invoices sent, with a rejection rate below 1%, almost all caused by recipients' incomplete registrations. Several Dutch practices began using it for corporate clients as well.

"My users were physiotherapists, not accountants. They needed the invoices to just work on 1 January, and they did." - Kevin Peeters

https://launchstudio.eu/en/blog/peppol-e-invoicing-for-saas-in-belgium-and-the-netherlands

#Peppol #EInvoicing #Belgium #SaaS #AIFounder #LaunchStudio #Manifera
