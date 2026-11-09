🏢 Bas Kramer runs a facility management SaaS from Amersfoort, built with Lovable and Supabase: property managers log maintenance requests, contractors update their status. Before a contract with a housing association, he ran the Supabase security advisor and a free external scanner. Both said green. ✅

One afternoon of testing with real roles said something else: 🧠

❌ Every table had Row Level Security, but several policies let any logged-in user read every request
❌ Contractors could change the status of other contractors' jobs through the API
❌ Photo uploads in a public bucket
❌ A service key inside an Edge Function callable without authentication

✅ Policies rewritten per role, with automated tests for every table
✅ Contractor updates restricted to assigned jobs
✅ Photos in private storage with signed links, the function secured and the key rotated
✅ Rate limits, security headers and a tested backup restore, plus a shareable report

At **LaunchStudio**, backed by Manifera's 11+ years of delivering software for security-conscious clients such as Vodafone and TNO, our reviews find and fix the issues scanners can't see. 🛠️

His result: €2,200, six business days. The housing association accepted the report, and a formal pentest a year later found only two low-severity issues. 🚀

👉 The cost of a security review for an AI-built app: https://launchstudio.eu/en/blog/cost-of-a-security-review-for-an-ai-built-app

#Security #Pentest #Supabase #Lovable #AIFounder #LaunchStudio #Manifera
