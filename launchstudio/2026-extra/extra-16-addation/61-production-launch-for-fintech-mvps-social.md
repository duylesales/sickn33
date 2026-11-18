📒 RECONCILIATION (illustrative figures, real problem)

Group balance in the app: €1,284.57
Partner's statement: €1,284.56
Difference: €0.01

A cent doesn't sound like much. Until you have to explain it to a family saving for a holiday. 💶

Mehmet Yildiz runs a Rotterdam start-up that built Spaarpot with Cursor and Supabase: families and friend groups save together for trips and events. Money is collected and paid out through a licensed payment institution partner, so Spaarpot never holds funds itself. Before granting live access, the partner sent a technical questionnaire. And a pilot with 40 groups showed small differences between app balances and the partner's statements.

Where the cents went:
• Balances stored as decimal numbers, updated directly on each contribution, with rounding in the browser
• Retried webhooks occasionally crediting a contribution twice
• A failed request sometimes updating a balance without a matching transaction
• The partner's API key in a client-side function
• A broad policy letting group members see other groups' contributions
• No audit log

The new books (LaunchStudio, Launch & Grow, 15 business days, €5,800, plus €49/month):
✓ Amounts in integer cents, with an explicit currency
✓ Contributions and payouts as append-only transactions, with balances derived from them
✓ Verified, idempotent webhooks, keyed by the partner's event IDs
✓ A daily reconciliation of every transaction against the partner's records, with alerts on differences
✓ The API key moved server-side and rotated
✓ Group separation enforced with Row Level Security and tests
✓ MFA and step-up confirmation for payouts
✓ An audit log of every financial change
✓ A security overview and architecture summary for the partner's questionnaire

The partner granted live access three weeks after receiving the documentation. In four months of live operation, reconciliation found two differences, both caused by delays at the partner and resolved automatically the next day.

📒 RECONCILIATION, since launch
Difference: €0.00

"A cent a day does not sound like much, until you have to explain it to a family saving for a holiday. Now every euro in the app matches a euro at our partner." - Mehmet Yildiz

https://launchstudio.eu/en/blog/production-launch-for-fintech-mvps

#Fintech #PSD2 #DORA #Supabase #AIFounder #LaunchStudio #Manifera
