🚨 Sven Mulder, treasurer of a hockey club in Deventer, built Teamkas in Lovable to collect membership dues. It worked so well he turned it into a SaaS: within six months, 23 clubs, about 110 administrators and a few thousand paying members. Then the new season hit all of them at once. 😳

The payments overview took over ten seconds for larger clubs. Reminder emails hit Supabase's built-in limits and hundreds never went out. Two treasurers editing the same fee overwrote each other - and when a member was charged twice, Sven couldn't see why. Here are the AI app problems that only appear at around 100 users: 🧠

❌ Every transaction fetched and filtered in the browser
❌ Transactional email sent through a development-grade sender
❌ Last save wins - conflicting edits silently lost
❌ No admin view, no audit trail for support questions

✅ Heavy queries rewritten with pagination, server-side filters and indexes
✅ All email moved to a transactional provider with an authenticated sending domain
✅ Optimistic locking, so conflicting edits trigger a warning instead of an overwrite
✅ A simple admin view with a per-member audit log, plus monitoring on load times and email delivery

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we harden SaaS products at the point where the first hundred users expose them - and keep your interface intact. ⚙️

His result: €3,800, thirteen business days. The overview dropped from 10+ seconds to under one, reminder delivery rose from ~60% to 99%+, outstanding dues fell by about a third - and Teamkas grew to 41 clubs by season's end. 🚀

👉 AI app production problems that only appear at 100 users: https://launchstudio.eu/en/blog/ai-app-production-problems-that-only-appear-at-100-users

#SaaS #Lovable #Scalability #Startups #LaunchStudio #Manifera
