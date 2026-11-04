🚨 Ruud Koopman built Klantbezoek in Lovable: a CRM-lite for the field sales reps of a building supplies wholesaler, used on phones between customer visits. Reps complained they were logged out constantly - often while typing visit notes, which were then lost. Some were logged out twenty times a day. 😳

Every logout cost a rep their notes and their patience. The cause turned out to be four copies of the same login code arguing with each other. Here's what was going on: 🧠

❌ A Supabase client created in four different components, each refreshing tokens on its own schedule
❌ The app reachable on both klantbezoek.nl and www.klantbezoek.nl
❌ Notification emails linking to the www version, a different session
❌ Token refresh failing on weak mobile connections after phones locked, signing users out instead of retrying

✅ One shared Supabase client module, imported everywhere
✅ www redirected to the canonical domain, with redirect settings updated
✅ Refresh handling that retries when the connection returns instead of signing out
✅ Draft visit notes saved locally, so nothing is lost if a session does expire

At **LaunchStudio**, backed by Manifera's 11+ years of authentication work, we trace the full session lifecycle - because most "random" logouts have one or two fixable causes. 🛠️

💡 His result: €1,200, four business days. Unexpected logouts dropped from a daily complaint to essentially none, and visit notes logged per rep rose noticeably once reps trusted the app. 🚀

👉 Is your Lovable app logging users out at random? Here are the six usual causes and how to fix them: https://launchstudio.eu/en/blog/why-does-my-lovable-app-log-users-out

#Lovable #Supabase #Authentication #UX #LaunchStudio #Manifera
