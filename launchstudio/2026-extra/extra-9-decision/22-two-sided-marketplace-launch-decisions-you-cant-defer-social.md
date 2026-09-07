🚨 140 tradespeople, 60 jobs a week, and a founder running every payout by hand from a Friday spreadsheet. Week nine: two disputes after sellers were already paid, one transfer to a mistyped IBAN. 😳

Liquidity gets all the attention. The money architecture underneath it is what actually breaks: 🧠

❌ Buyer funds land in your company account, mixed with your own runway
❌ "Paid" is a boolean instead of a transaction state machine with a release date
❌ Sellers get verified with a Google Form instead of real KYC
❌ No clawback mechanism exists for a chargeback that lands after payout

✅ Split payments at authorisation with a connected-accounts provider like Mollie or Stripe Connect
✅ Build an explicit state machine: pending, authorised, disputed, released
✅ Verify sellers through the payment provider, not passport scans you now have to store
✅ Freeze the payout clock the moment a dispute opens

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build the payment splitting, state machine and payout logic that a marketplace prototype never had. 💳

His result: Friday payout runs disappeared, both disputes resolved from held funds, and onboarding went from a three-day back-and-forth to a fifteen-minute flow that added 90 suppliers the next month. 🚀

👉 Send your prototype link for free feedback: [Link to article]

#Marketplace #SaaS #LaunchStudio #Manifera #ProductionReady #Fintech
