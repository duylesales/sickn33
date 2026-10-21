🚨 Daan Koopman, who manages a shopping street association in Bergen op Zoom, built Spaarpas in Bolt: a digital stamp card shared by 34 local shops. Collect points anywhere, redeem vouchers at other shops, settle at month end. 5,200 residents signed up in three months. Then the first double-points Saturday exposed everything. 😳

Every customer had a static QR code. Voucher screenshots were redeemed at several shops. A group of accounts claimed the sign-up bonus dozens of times with throwaway emails. Two shops' tablets issued points twice when staff retried after a dropped connection. And at month end, the settlement report didn't match what shops remembered — with no history to check. Here's what loyalty apps face in production: 🧠

❌ Points stored as a single balance column
❌ Static QR codes that can be screenshotted and replayed
❌ Retries that double-issue points
❌ Settlement with no ledger behind it

✅ A points ledger, with opening balances reconstructed from logs and uncertain accounts flagged
✅ Transactional earning and redemption with idempotency keys
✅ Rotating single-use codes validated on the server, and sign-up bonuses tied to verified phone numbers
✅ Every staff action logged per employee, expiry and refund reversals, and a monthly settlement report per shop

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we treat points like money — because your customers, shops and fraudsters already do. ⚙️

His result: €2,600, nine business days. The next promotion ran with zero duplicate redemptions, month-end settlement matched to the voucher, and Spaarpas grew to 51 shops — the treasurer now uses the ledger report instead of a spreadsheet. 🚀

👉 Building an AI loyalty app? AI app production problems with points and fraud: https://launchstudio.eu/en/blog/building-an-ai-loyalty-app-ai-app-production-problems-with-points-and-fraud

#Loyalty #FraudPrevention #Ledger #Bolt #LaunchStudio #Manifera
