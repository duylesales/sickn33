🎫 Five support tickets about one bug

TICKET → Stripe: "Payments and webhook deliveries confirmed." ✅
TICKET → Supabase: "Your database is healthy." ✅
TICKET → Email provider: "No messages were requested for those students." ✅
TICKET → Lovable: "Try checking the webhook function." ✅
FORUM → Vercel community: helpful replies. ✅

Every answer was correct. The bug was still there. 🧘

Linda Smeets runs Yogaleerlijn from Nijmegen, an online course platform for yoga teachers built with Lovable, Supabase, Vercel, Stripe and an email provider. After a price change, some students paid for a course but never got access, or the welcome email. Linda asked everyone. Each platform checked its own part, and each part was fine.

The bug lived in the space between them.

Linda moved to Launch & Grow. LaunchStudio traced it in an hour: after the price change, the webhook handler looked up courses by an old price ID, failed silently, and still told Stripe "success." So Stripe never retried. And because access was never granted, no welcome email was ever requested.

The fix (6 business days, €2,600, plus €49/month):
✓ The handler now uses product metadata instead of price IDs
✓ Failures return errors, so Stripe retries
✓ Alerts on failed processing
✓ Staging and monitoring
✓ Affected students reconciled, granted access, and sent an apology email Linda approved

All 23 affected students had access the same day. Under the ongoing service, a later Stripe API version change was handled two months before its deadline. And Linda now opens platform tickets only for platform problems.

"Every platform told me their part was fine, and they were right. The bug lived in the space between them, where nobody was looking." - Linda Smeets

https://launchstudio.eu/en/blog/launchstudio-vs-platform-support-plans

#Support #Stripe #Supabase #Lovable #AIFounder #LaunchStudio #Manifera
