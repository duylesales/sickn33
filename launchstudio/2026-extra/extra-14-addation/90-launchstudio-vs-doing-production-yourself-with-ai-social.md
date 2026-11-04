🚨 Daan Wolthuis, a backend developer in Utrecht, built Sportschoolrooster with Bolt: class scheduling and memberships for small gyms. He chose to do production work himself with Cursor, and spent five weekends on RLS, Stripe subscriptions, EU hosting and a CI pipeline. Before onboarding his first three gyms, he booked a review anyway. 😳

Doing it himself taught him his own stack. The review caught the two things he didn't know he didn't know: 🧠

❌ An insert policy without "with check" - members could create bookings for other gyms
❌ A Stripe webhook handler that wasn't idempotent - a retried event could double-credit class packs
❌ Both invisible in normal testing, because everything appeared to work
❌ Exactly the kind of gap AI tools write confidently without flagging

✅ The rest of his RLS, Stripe, EU hosting and CI work confirmed as solid
✅ Clear guidance on both findings
✅ Daan fixed both issues himself, using the review
✅ LaunchStudio verified the fixes before launch

At **LaunchStudio**, backed by Manifera's 160+ projects and 120+ engineers, we don't only take apps to production - we also review the work of founders who did it themselves. 🛠️

💡 His result: €900, four business days. Sportschoolrooster launched with three gyms, and Daan kept full ownership of the work and the knowledge, at a fraction of the cost of outsourcing everything. 🚀

👉 Should you do production yourself with AI, or bring in a partner? Here's the honest comparison: https://launchstudio.eu/en/blog/launchstudio-vs-doing-production-yourself-with-ai

#IndieHacker #Supabase #Cursor #AppSecurity #LaunchStudio #Manifera
