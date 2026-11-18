🌦️ MONDAY MORNING FORECAST for Zorgrooster, issued by a load test before go-live

06:45-07:15: a front of 900 carers arriving over thirty minutes, opening the app to see the day's clients.

Expected conditions:
☁️ Roster screen: heavy, p95 of 9.8 seconds
⛈️ Around 400 concurrent users: connection errors, requests failing
🌫️ Starting a visit: delays of several seconds, as a push notification to the coordinator ran inside the request and hit the provider's rate limit
🌙 Overnight: the worked-hours calculation, twenty minutes today, running six hours at the new scale and still going when the morning peak begins

Thomas van Leeuwen built Zorgrooster in Lovable: rostering and visit registration for 23 small home care organisations, about 1,400 carers in total. Then he signed a regional care group with 2,600 carers, almost double his whole user base, going live on a Monday. Its shifts start at 7:00. The forecast came from a production-like environment with generated data at three times the group's size. 🏠

Changing the weather (LaunchStudio, 5 business days, €5,400):
✓ The roster query rewritten to fetch one week for one carer through a single RPC, with two composite indexes
✓ The row level security helper rewritten as a stable security definer function with an indexed membership lookup, removing a per-row subquery
✓ Edge functions moved to the transaction pooler
✓ Push notifications moved to a queue with a worker
✓ The hours calculation batched by organisation and week, running in parallel with a concurrency limit
✓ Database compute raised one size, after the code fixes
✓ Load and spike tests rerun after every change

REVISED FORECAST, at three times the expected peak
☀️ Roster p95: 420 milliseconds
☀️ Errors: none
☀️ Nightly calculation: 35 minutes

The group was onboarded in two stages. On the second Monday, 2,600 carers started their shifts without a single support call about speed. Infrastructure costs rose by about €110 a month.

"The first test told me that on our biggest customer's first morning, the roster would take ten seconds to load and then stop loading at all. I would much rather have heard it from k6 than from nine hundred carers." - Thomas van Leeuwen

https://launchstudio.eu/en/blog/lovable-hosting-load-testing-before-a-large-customer-onboards

#LoadTesting #Performance #Supabase #SaaS #LaunchStudio #Manifera
