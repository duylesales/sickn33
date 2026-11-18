🧾 MONDAY MORNING BILLING EMAIL

Model provider charges, Saturday and Sunday: €3,100
Monthly revenue, for comparison: €3,800
Documents that caused it: 11
Model calls those 11 documents generated: 41,000

Daniël Wubbels built Bestekcheck with Lovable: it reads construction specifications and flags inconsistencies for small contractors and architects. 40 subscribers, €95 a month. On a Friday evening, he deployed a change to how documents were split before going to the model. On documents above a certain length, it produced overlapping segments, and each segment triggered a further split. 🏗️

Nothing errored. The feature appeared to work. The output was correct. There was nothing to notice, except a number on a dashboard he had no reason to open on a Saturday.

What LaunchStudio added (2 business days, €2,400):
✓ A hard cap on segments per document, failing loudly instead of carrying on
✓ Recursion depth limited, so a split can't trigger a split
✓ Per-account rate limiting on document processing, set well above normal use
✓ Bounded retries with backoff, replacing unlimited retries on model timeouts
✓ A spending cap at the model provider that suspends instead of billing beyond it
✓ An hourly alert if model call volume reaches ten times normal
✓ Cost attribution per document and per account, so Daniël can see what each customer costs
✓ Response length limits and context trimming, cutting ordinary per-document cost by 40%
✓ Results cached by document hash, which covers 18% of uploads, since contractors re-upload revised specs that are mostly unchanged

🧾 AFTERWARDS
The provider credited part of the weekend after Daniël explained the loop. The remaining €1,900 was a month of profit.
In two years since, the volume alert has fired twice: once for a real bug caught in eleven minutes, once for a legitimately large customer.
And per-document cost is 40% lower than before the incident.

"The feature worked. The output was correct. There was nothing to notice except a number on a dashboard I had no reason to open on a Saturday." - Daniël Wubbels

https://launchstudio.eu/en/blog/lovable-hosting-cost-control-when-traffic-is-unpredictable

#CloudCosts #AI #FinOps #Lovable #LaunchStudio #Manifera
