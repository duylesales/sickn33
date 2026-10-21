🚨 Marnix Oosterveld's Offerteroute manages quotations for 61 kitchen and bathroom installers — about 900 a month. Customers started receiving two copies of every quotation, some at three in the morning. Two replied to both, and one argued about a price that had changed between versions. 😳

Nothing in his code sent a second email. A database trigger did — written by an AI session eight months earlier, in a chat he didn't remember. Here's what hides in an AI-built Supabase schema: 🧠

❌ Eleven triggers nobody could explain — two duplicating application logic
❌ A trigger calling an external webhook inside a transaction, causing timeouts
❌ Three triggers firing into tables that had been replaced
❌ A security definer function returning any company's quotations to any logged-in user

✅ Every function and trigger inventoried and described in one sentence
✅ Email and webhook work moved into application code, where it can be retried and logged
✅ The security definer function rewritten with an explicit membership check and fixed search path
✅ Timestamp and counter triggers kept and covered by SQL tests — and the whole schema committed as a baseline migration

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we find what your database does that your code never mentions. 🗄️

His result: three business days and €2,700 later, the duplicate emails and intermittent timeouts stopped, and the exposed function was closed before anyone used it. Marnix now has a two-page document explaining what his database does on its own. 🚀

👉 Database functions and triggers worth keeping: https://launchstudio.eu/en/blog/lovable-supabase-database-functions-and-triggers-worth-keeping

#Supabase #PostgreSQL #DatabaseDesign #Lovable #LaunchStudio #Manifera
