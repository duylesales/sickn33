💬 REVIEW COMMENTS on one developer's DIY production setup

✅ RLS: solid
✅ Stripe subscriptions: solid
✅ EU hosting: solid
✅ CI pipeline: solid
⚠️ bookings insert policy: no "with check". Members can create bookings for other gyms.
⚠️ Stripe webhook handler: not idempotent. A retried event can double-credit class packs.

Two comments. Everything else: approved. 🏋️

Daan Wolthuis, a backend developer in Utrecht, built Sportschoolrooster with Bolt as a side project: class scheduling and memberships for small gyms. He decided to do the production work himself, with Cursor, and spent five weekends on RLS, Stripe subscriptions, EU hosting and a CI pipeline.

Before onboarding his first three gyms, he booked a review with LaunchStudio (4 business days, €900). The review found the two issues above, the kind you don't know you don't know.

Daan fixed both himself, using the review's guidance. LaunchStudio verified the fixes.

✅ Insert policy: fixed
✅ Webhook handler: fixed

Sportschoolrooster launched with three gyms. Daan kept full ownership of the work and the knowledge, at a fraction of the cost of outsourcing everything.

Doing production yourself with AI? Then a second pair of eyes is the cheapest part of it.

"Doing it myself taught me my own stack. The review caught the two things I didn't know I didn't know." - Daan Wolthuis

https://launchstudio.eu/en/blog/launchstudio-vs-doing-production-yourself-with-ai

#IndieHacker #Supabase #Cursor #AppSecurity #LaunchStudio #Manifera
