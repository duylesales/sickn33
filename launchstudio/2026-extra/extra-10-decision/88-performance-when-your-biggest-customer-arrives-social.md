🚨 Elif's biggest customer — 1,400 employees, six years of history — got a 38-second load time and frequent timeouts, on the account paying her the most. 😳

Building and testing only against small accounts feels efficient. Here's the bill that comes due: 🧠

❌ The overview page fetched all employees, then queried each one's absence records individually — 1,401 queries where two would do
❌ There was no pagination, so every one of 1,400 employees loaded regardless of what was actually needed
❌ The absence table had no index on the employee reference, so each of those 1,401 queries scanned the whole table
❌ The slow page was consuming most of the database's capacity for the better part of a minute, degrading things for smaller customers too

✅ Test with an account holding far more data than your largest real one — 100,000 records if your biggest is 5,000
✅ Fetch related data in one query instead of in a loop; it's a habit, not an architecture change
✅ Paginate every list from the start — retrofitting it later means changing the interface, the API, and everything downstream
✅ Read your database's slow query log — a handful of queries usually account for nearly all the load

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we test AI-built products against the volume your next big customer will actually bring. ⚡

Her result: the N+1 pattern replaced with two queries, pagination added at 50 per page, indexes added, and dashboard totals precomputed nightly — load time dropped from 38 seconds to 400 milliseconds. 🚀

👉 Find out what your product does at 50x your current data: https://launchstudio.eu/en/blog/performance-when-your-biggest-customer-arrives

#SaaS #DevOps #Performance #ScaleUp #LaunchStudio #Manifera
