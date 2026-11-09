☕ Vera Hofman runs a small coffee roastery in Deventer and built Bonenpost with Bolt and Supabase: about 900 subscribers get freshly roasted beans every two or four weeks, paid through Mollie. Then the complaints formed a pattern. Some customers charged twice in one week, skipped deliveries arriving anyway, and failed debits silently stopping deliveries. Cancelling? Only by email. 📬

The assessment explained it all: 🧠

❌ One scheduled function creating charge and order, rerunning from the start after timeouts
❌ The spring clock change shifting the schedule and running one cycle twice
❌ Skips after the fulfilment export ignored, and failed SEPA debits and later reversals never handled
❌ Orders exported as a spreadsheet and uploaded by hand each cycle

✅ Idempotency keys per subscription and cycle, with orders created only from verified webhooks
✅ Cycle dates stored with time zone information and tested across clock changes
✅ A clear cut-off two days before roasting, a dunning flow with retries and payment update links, and reversals updating status
✅ Orders sent to the fulfilment partner's API after the cut-off, plus online cancellation with confirmation

At **LaunchStudio**, backed by Manifera's 11+ years of building payment, scheduling and integration systems for clients such as Vodafone and TNO, we make every cycle produce one payment and one order. 🛠️

Her result: €3,200, eight business days. Double charges stopped, and the dunning flow recovered a large share of failed payments within two months. 🚀

👉 Production launch for subscription e-commerce: https://launchstudio.eu/en/blog/production-launch-for-subscription-ecommerce

#Subscriptions #Ecommerce #Mollie #Bolt #AIFounder #LaunchStudio #Manifera
