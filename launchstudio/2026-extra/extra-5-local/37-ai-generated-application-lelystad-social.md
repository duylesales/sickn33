✈️ PRE-FLIGHT CHECK: Vluchtplan, Lelystad

Ilse Mulder is a logistics coordinator working near Lelystad Airport. Over several weeks she built Vluchtplan in Cursor, writing the whole matching algorithm and interface herself. It matches cargo capacity on regional charter flights with shippers who need the space. Two logistics companies were ready to pilot it.

Before take-off, LaunchStudio ran its six-point pre-launch checklist.

Result: 3 of 6 items FAILED.

❌ Data isolation: no RLS policies. Any shipper account could see every other shipper's pricing and cargo details.
❌ Payments: booking deposits still ran in Stripe test mode, with the live keys hardcoded incorrectly.
❌ Concurrency: no handling for two shippers booking the same cargo slot at the same time.

Status: GROUNDED.

Repairs (7 business days, €1,400):
🔧 Proper per-company data isolation
🔧 A correctly configured live payment flow with webhook verification
🔧 Optimistic locking on bookings to prevent double bookings

Status: CLEARED FOR TAKE-OFF. In week one, both logistics companies processed real cargo bookings, with zero data exposure and zero double bookings.

"I thought I was almost done. LaunchStudio's checklist showed me I was maybe sixty percent done, and the missing forty percent was exactly the part that would have caused real damage with real logistics companies." - Ilse Mulder

Run a pre-flight check on your AI-generated application: https://launchstudio.eu/en/blog/ai-generated-application-lelystad

#AINativeFounder #LaunchStudio #Manifera #Lelystad #LaunchReady
