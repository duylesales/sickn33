🚨 Maartje Klaassen's Verbruik monitors energy consumption for six housing associations and two property managers around Almelo and Hengelo — about 11,000 homes. For eighteen months it was fine. Then, on the first working day of every month, it became unusable for about forty minutes. 😳

She assumed it was a hosting problem. It was nine numbers on a dashboard, each reading 7.4 million rows. Here's how reporting quietly takes down a product: 🧠

❌ Nine dashboard figures computed live, each scanning the full readings table
❌ No index on date or association — including the columns the access policies filter on
❌ One query per building: 340 round trips for the largest association
❌ An annual export that loaded everything into memory and failed silently for the two largest customers

✅ Query plans captured for every dashboard element, to locate the scans precisely
✅ Indexes on association, date and meter — policy columns included — taking the dashboard from 47 seconds to 4
✅ A daily summary table bringing it under a second, with per-building queries collapsed into one
✅ Exports as background jobs delivered by signed link, a separate connection pool for reporting, and slow-query alerts

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make reporting fast without slowing down the rest of your product. 📊

Her result: nine business days and €4,600 later — no month-end incident in eleven months, the two associations compiling reports by hand stopped, and one mentioned the export in a contract extension. 🚀

👉 Lovable + Supabase reporting queries that don't slow you down: https://launchstudio.eu/en/blog/lovable-supabase-reporting-queries-that-do-not-slow-you

#Supabase #Lovable #Performance #PostgreSQL #LaunchStudio #Manifera
