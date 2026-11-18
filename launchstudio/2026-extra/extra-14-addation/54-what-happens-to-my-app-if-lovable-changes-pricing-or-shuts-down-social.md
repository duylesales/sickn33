Q&A: the question every acquirer of a Lovable app will ask 🤝

Q: What does the app do?
A: Huurcheck, built by Thomas Veldkamp in Lovable, helps Dutch tenants check whether their rent is reasonable under rental rules and generates a letter to their landlord. Several thousand users. A legal services company wanted to buy it.

Q: "What happens if Lovable changes or disappears?"
A, before: Uncomfortable. The app was published on a Lovable domain with a custom domain pointed at it. The backend ran on Lovable Cloud. The GitHub repository sat on Thomas's personal account, months out of date, because sync had been disconnected.

Q: What changed?
A: In 12 business days, for €4,400, LaunchStudio:
• Reconnected GitHub, under a company organisation
• Migrated the backend to a company-owned Supabase project in Frankfurt
• Deployed the app from GitHub to Vercel, on Thomas's domain
• Moved the rent calculation rules into database functions, with tests
• Wrote an operating document for the acquirer

Q: "What happens if Lovable changes or disappears?"
A, after: The app keeps running. Code, backend and deployment are all owned by the company, and documented.

Q: And the deal?
A: The acquirer's follow-up review found no platform dependency issues, and the deal closed on the original terms. During the transition, Thomas even kept editing the interface in Lovable.

"I had built a business on a tool. The buyer wanted to know I had built it on something I owned." - Thomas Veldkamp

https://launchstudio.eu/en/blog/what-happens-to-my-app-if-lovable-changes-pricing-or-shuts-down

#Lovable #VendorLockIn #Supabase #DueDiligence #LaunchStudio #Manifera
