🪣 The €0 checkout and its leaks

Gijs Hermans runs Lichtlessen, an online course platform for hobby photographers in Roermond, built with Lovable and Supabase, with monthly and yearly memberships through Stripe. His AI tool built the checkout in one evening. Cost: €0.

Six months later, Gijs estimated it was leaking several hundred euros a month.

LEAK 1: Members whose cards failed kept their access
LEAK 2: A few members paid, and never got access
LEAK 3: No proper handling for upgrades, refunds or cancellations
LEAK 4: Hours every quarter for his accountant, matching payouts to invoices without correct VAT

Patching the bucket (LaunchStudio, 6 business days, €2,300):
🔧 Access granted by verified, idempotent webhooks, not by the success page
🔧 Failed renewals handled by Stripe's retry and email flows, with access ending after the final attempt
🔧 Proration for upgrades from monthly to yearly
🔧 Refunds that remove access
🔧 A customer portal, so members manage their own billing
🔧 Stripe Tax, enabled after Gijs checked the approach with his accountant
🔧 A reconciliation of the past six months: 23 members with access but no active payment, and 4 who had paid without access, all resolved with Gijs's approval

THE BUCKET NOW
Recovered revenue from members without valid payments covered the project within about four months. The accountant's quarterly reconciliation went from hours to a quick look at an export. And support emails about access almost stopped.

"The checkout was free to build. Not fixing it was costing me every month." - Gijs Hermans

https://launchstudio.eu/en/blog/cost-to-add-payments-to-an-ai-built-app

#Payments #Stripe #Mollie #SaaS #AIFounder #LaunchStudio #Manifera
