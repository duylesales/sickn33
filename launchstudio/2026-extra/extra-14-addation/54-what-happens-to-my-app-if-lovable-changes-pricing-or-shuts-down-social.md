🚨 Thomas Veldkamp built Huurcheck in Lovable: a tool for Dutch tenants to check whether their rent is reasonable and generate a letter to their landlord. It grew to several thousand users, and a legal services company wanted to buy it. Then the acquirer's technical review asked one question: "What happens if Lovable changes or disappears?" 😳

His honest answer was uncomfortable. He had built a business on a tool - the buyer wanted to know he'd built it on something he owned. Here's what the review found: 🧠

❌ The app published on a Lovable domain, with his custom domain pointed at it
❌ The backend running on Lovable Cloud
❌ The GitHub repository on his personal account, months out of date because sync had been disconnected
❌ Rent calculation rules living only inside generated components

✅ GitHub reconnected under a company organisation
✅ The backend migrated to a company-owned Supabase project in Frankfurt
✅ The app deployed from GitHub to Vercel on Thomas's own domain
✅ Rent rules moved into tested database functions, plus an operating document for the acquirer

At **LaunchStudio**, backed by Manifera's 11+ years of vendor transitions and platform migrations, we let you keep building fast in Lovable while you own the code, data, hosting and domain. 🛠️

💡 His result: €4,400, twelve business days. The acquirer's follow-up review found no platform dependency issues, and the deal closed on the original terms. 🚀

👉 What actually depends on Lovable in your app? Here are the five steps to independence: https://launchstudio.eu/en/blog/what-happens-to-my-app-if-lovable-changes-pricing-or-shuts-down

#Lovable #VendorLockIn #Supabase #DueDiligence #LaunchStudio #Manifera
