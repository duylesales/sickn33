🚨 Thomas van Leeuwen's Zorgrooster handles rostering for 23 home care organisations — about 1,400 carers. Then he signed a regional care group with 2,600 carers, nearly doubling his user base, going live on a Monday. Their shifts start at 7:00, and most carers open the app between 6:45 and 7:15. 😳

A load test at three times the care group's size failed badly: the roster took 9.8 seconds at p95, connections started failing at ~400 users, and the nightly hours calculation took six hours — finishing after the morning peak had begun. Here's how to load test before a large customer onboards: 🧠

❌ A roster query fetching far more than one carer's week, with missing indexes
❌ A row level security helper running a subquery for every row
❌ Edge functions opening direct database connections instead of using the pooler
❌ Push notifications sent inside the request, and a nightly job that didn't scale

✅ Customer peak modelled from their real shift start, with generated data at 3x their scale
✅ Realistic k6 load and spike tests with 900 arriving carers, think time and pass/fail thresholds
✅ One RPC per carer-week with composite indexes, a stable security definer RLS helper, and the transaction pooler
✅ Notifications queued, the nightly job batched and parallelised, then a compute upgrade — only after the code fixes

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we run this rehearsal before the onboarding that matters most. ⚙️

His result: €5,400, five business days. Final test: roster p95 of 420 ms at 3x peak, zero errors, nightly job in 35 minutes. 2,600 carers started on a Monday without a single speed complaint — for about €110 a month more. 🚀

👉 Lovable hosting: load testing before a large customer onboards: https://launchstudio.eu/en/blog/lovable-hosting-load-testing-before-a-large-customer-onboards

#LoadTesting #Performance #Supabase #SaaS #LaunchStudio #Manifera
