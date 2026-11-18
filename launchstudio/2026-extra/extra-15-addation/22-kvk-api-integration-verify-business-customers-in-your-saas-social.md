🔍 CASE FILE: The 400 Bakeries That Weren't

THE CLIENT
Yusuf Demir, Tilburg. Built Bakkersgroothandel Online with Bolt and Supabase: a B2B platform where bakeries and cafés order flour, yeast, packaging and equipment from a regional wholesaler, with 30-day invoice payment for verified business customers.

THE WEAK POINT
The sign-up form asked for company name, address and KVK number as free-text fields. Nobody checked any of them.

THE EVIDENCE, six months later
• Around 400 accounts created by people who weren't businesses, drawn by trade prices
• Several of them ordered on invoice terms and never paid
• Real customers with misspelled names and wrong addresses, so invoices bounced
• About a fifth of the "KVK numbers" were actually VAT numbers or typos
• A Belgian café chain invoiced with Dutch VAT, because nobody validated its VAT number

THE SOLUTION (LaunchStudio, 8 business days, €2,700)
• Company search in sign-up, via a Supabase edge function calling the KVK Search and Basic Profile APIs, key in secret storage, debounced queries, per-user rate limits
• New accounts verified against active registrations and food and hospitality SBI codes
• A manual review queue for foreign businesses and edge cases
• VAT numbers checked through VIES, with result and date stored
• Invoice payment only for verified accounts, and existing customers asked to confirm their company on next login

CASE CLOSED
Fake trade accounts dropped to almost zero within a month, and unpaid invoices from unverified accounts stopped. Addresses now come from the register, so bounced invoices fell sharply. Belgian customers get correct reverse-charge invoices. KVK costs: under €30 a month.

"We were trusting whatever people typed in a form. Now the register does the first check, and our team only reviews the cases that actually need a human." - Yusuf Demir

https://launchstudio.eu/en/blog/kvk-api-integration-verify-business-customers-in-your-saas

#KVK #B2B #Wholesale #FraudPrevention #AIFounder #LaunchStudio #Manifera
