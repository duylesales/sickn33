🚨 Gerlof Tichelaar's Zorgdossier manages care plans for 26 small-scale residential care providers — about 1,400 residents. Then a regional healthcare group offered a contract for nine locations, worth more than his existing revenue. Their procurement required a specific region, certification and contract terms his Supabase plan didn't offer. 😳

He asked Supabase first — the step most founders skip. Part of it was solvable; the region and certification weren't, in time. Here's what leaving Supabase actually involves: 🧠

❌ "It's expensive", "it's slow", "lock-in" — usually not real reasons to leave
❌ Assuming the database is the hard part (it isn't — it's standard Postgres)
❌ Underestimating auth: every session ends and every RLS policy needs rewriting
❌ Skipping the rehearsal and guessing how long the cutover will take

✅ A full rehearsal on a copy — which found two missing extensions and timed the cutover at 40 minutes, not two hours
✅ Password hashes imported so no carer had to reset anything, and 31 RLS policies rewritten
✅ 94,000 documents copied during a two-week dual-read period, with old links redirected
✅ Realtime replaced with polling where it wasn't clinically needed, and a restore tested before retiring the old project

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we'll also tell you not to migrate — which is the more common answer. 🧭

His result: sixteen business days and €11,800 later, the contract was signed. The 40-minute cutover happened at six on a Sunday morning, and nobody noticed. Infrastructure went from €85 to €310 a month — the least interesting number in the project. 🚀

👉 Leaving Supabase for plain Postgres: https://launchstudio.eu/en/blog/lovable-supabase-leaving-supabase-for-plain-postgres

#Supabase #PostgreSQL #Migration #HealthTech #LaunchStudio #Manifera
