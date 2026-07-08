💸 A fintech startup built a beautiful P2P payment app. Launched in NL.

3 months later: Cease-and-desist from the Dutch Central Bank (DNB).

They thought using Stripe meant they didn't need a PSD2 license.
They were wrong.

Fintech is software where getting the tech right is only 50% of the job.

**The regulatory trifecta in Europe:**
⚖️ **PSD2** — payment licensing + Strong Customer Authentication (SCA)
🛡️ **DORA** — operational resilience & incident reporting (mandatory 2025)
🕵️ **KYC/AML** — identity verification & sanctions screening

**Fintech architecture vs Standard SaaS:**

❌ Standard: Floating-point math (`10.00`)
✅ Fintech: Integer math (`1000` cents) or `BigDecimal`. Floats leak pennies over millions of transactions.

❌ Standard: "Oops, network error, retry request"
✅ Fintech: Idempotency keys. Never charge the user twice.

❌ Standard: Update row in DB.
✅ Fintech: Double-entry bookkeeping. Credits must equal debits. Atomicity is non-negotiable.

**The startup shortcut:** Don't get your own banking license (€500K+ and 18 months). Use a Banking-as-a-Service (BaaS) provider like Solarisbank or Swan (€10K-€50K/year).

Build the UX. Rent the license.

#Fintech #PSD2 #KYC #SoftwareDevelopment #BankingAsAService #CTO #Manifera
