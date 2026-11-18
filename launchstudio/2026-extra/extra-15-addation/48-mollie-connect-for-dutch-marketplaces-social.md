⚽ AGENDA: Clubkas general meeting

1. Opening
Kees Verbruggen built Clubkas with Bolt and Supabase: amateur sports clubs in Noord-Brabant use it to manage memberships, collect contributions and sell event tickets. 34 clubs and growing.

2. Treasurer's report
All club payments ran through Kees's own Mollie account. Each month he transferred every club's money, keeping a small fee.

3. Points raised by members
• Club treasurers want payments in their own accounts
• Kees's accountant has concerns about holding funds for others
• Monthly transfers take a full day, and occasionally go to the wrong club
• Refunds for cancelled events are calculated by hand

4. Technical points
• The redirect after iDEAL was treated as proof of payment, so some failed payments were recorded as paid
• The Mollie API key sat in a frontend environment file

5. Proposal (LaunchStudio, 15 business days, €6,200)
• Mollie Connect: each club connects its own Mollie account through OAuth, tokens encrypted and stored server-side, onboarding status visible to club admins
• Payments created on each club's account, with an application fee for Clubkas
• Membership contributions via SEPA direct debit, with mandates from a first iDEAL payment
• A webhook handler that fetches payment status with the right club's credentials, idempotently
• Event cancellations refunded through the platform, with clear fee rules
• The exposed key rotated, and daily reconciliation between Mollie and Clubkas

6. Vote
Carried.

7. Any other business
First season on the new setup: around 4,200 membership contributions collected via SEPA, failed collections handled automatically, payment status errors gone, and no more transfer day for Kees.

8. Closing words
"My clubs trusted me with their money, which was exactly the problem. Now Mollie holds it and I just make the platform work." - Kees Verbruggen

https://launchstudio.eu/en/blog/mollie-connect-for-dutch-marketplaces

#Mollie #MollieConnect #SEPA #SportsTech #AIFounder #LaunchStudio #Manifera
