🚨 Merel Kok runs a small architecture studio in Schiedam and wanted Ontwerpkluis: a public portfolio that ranks for "renovation architect" around Rotterdam, plus a private portal where clients review drawings and approve design phases. She built it all in Lovable first. 😳

The portal worked. The portfolio barely got indexed in two months. She rebuilt the portfolio in v0 - it indexed quickly - then started rebuilding the portal there too, and stalled. Here's what was going on: 🧠

❌ Lovable's client-rendered portfolio pages hardly visible to search engines
❌ The v0 rebuild stuck on authentication and file permissions for the portal
❌ Two half-finished versions and no shared backend
❌ Client drawings with no proper access control

✅ Both kept: the v0 Next.js site for public pages on the main domain, the Lovable portal on a subdomain
✅ One shared Supabase project in Frankfurt, with Row Level Security so clients see only their own projects
✅ Drawings in private storage with signed URLs, plus comment and approval flows with email notifications
✅ Vercel environment variables per environment and structured data on project pages

At **LaunchStudio**, backed by Manifera's 11+ years of React and Next.js work, we let each tool do what it's good at - and connect them properly. 🛠️

💡 Her result: €4,600, thirteen business days. The portfolio was indexed within weeks and started bringing in renovation enquiries from Rotterdam and Delft, and fourteen clients used the portal in its first quarter. 🚀

👉 v0 or Lovable - UI generator or app builder? Here's how to choose, or use both: https://launchstudio.eu/en/blog/v0-vs-lovable-ui-generator-or-app-builder

#v0 #Lovable #NextJS #SEO #LaunchStudio #Manifera
