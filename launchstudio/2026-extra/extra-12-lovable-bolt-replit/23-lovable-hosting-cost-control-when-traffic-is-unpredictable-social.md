🚨 Daniël Wubbels's Bestekcheck reads construction specifications for 40 contractors and architects at €95/month. One Friday evening he deployed a change to how documents were split before going to the model. Nothing errored. The feature worked. 😳

Over the weekend, eleven documents generated 41,000 model calls. The bill: €3,100 — against monthly revenue of €3,800. He found out from a billing email on Monday. Here's how usage-priced hosting bills explode: 🧠

❌ A split that triggered further splits — recursion with no limit
❌ Unlimited retries on model timeouts
❌ No spending cap at the provider and no alert on call volume
❌ No idea what each customer or document actually cost

✅ A hard cap on segments per document and limited recursion depth — failing loudly instead of continuing
✅ Per-account rate limits and bounded retries with backoff
✅ A provider spending cap that suspends rather than bills, plus an hourly alert at 10× normal volume
✅ Cost attribution per document and account, trimmed context, response limits and cached results for identical documents

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we set the caps before you need them — and find the line on your bill that's actually a bug. 💸

His result: two business days and €2,400 later, the volume alert has fired twice in two years — once catching a real bug within eleven minutes. Per-document cost is now 40% lower than before the incident. 🚀

👉 Cost control when traffic is unpredictable: https://launchstudio.eu/en/blog/lovable-hosting-cost-control-when-traffic-is-unpredictable

#CloudCosts #AI #FinOps #Lovable #LaunchStudio #Manifera
