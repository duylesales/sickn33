🪙 Congratulations. You've launched a currency.

That's what happens when 34 shops let customers earn points in one place and spend them in another. You're not running a stamp card anymore. You're running a small monetary system, and it needs what every currency needs: protection against counterfeiting, controlled issuance, and bookkeeping.

Spaarpas had none of the three.

Daan Koopman manages a shopping street association in Bergen op Zoom and built Spaarpas in Bolt: a digital stamp card shared by 34 local shops. Customers collect points at any shop and redeem them for vouchers at others. Shops pay a monthly fee and settle redeemed vouchers at month end. About 5,200 residents signed up in three months. Then came the first promotion: double points on a Saturday.

COUNTERFEITING
• Each customer had a static QR code, and staff scanned it and typed an amount
• Screenshots of vouchers were redeemed at several shops

ISSUANCE
• A group of accounts collected the sign-up bonus dozens of times, with disposable email addresses
• Two shops' tablets issued points twice when the connection dropped and staff retried

BOOKKEEPING
• At month end, the settlement report didn't match what shops remembered, and there was no history to check

The central bank, rebuilt (LaunchStudio, 9 business days, €2,600):
✓ The balance column replaced by a ledger, with opening balances reconstructed from available logs and uncertain accounts flagged
✓ Earning and redemption made transactional, with idempotency keys
✓ Static codes replaced by rotating, single-use codes validated on the server
✓ Sign-up bonuses tied to verified phone numbers
✓ Every staff action logged per employee
✓ Expiry and refund reversals
✓ A monthly settlement report per shop

The next promotion ran with no duplicate redemptions, and the month-end settlement matched to the voucher. Spaarpas grew to 51 shops, and the association's treasurer now uses the ledger report instead of a spreadsheet.

"We thought we'd built a stamp card. We'd actually built a small currency with no bookkeeping." - Daan Koopman

https://launchstudio.eu/en/blog/building-an-ai-loyalty-app-ai-app-production-problems-with-points-and-fraud

#Loyalty #FraudPrevention #Ledger #Bolt #LaunchStudio #Manifera
