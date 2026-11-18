🚦 THREE SECURITY CHECKS ON ONE APP

🟢 Supabase security advisor: no serious problems
🟢 Free external scanner: no serious problems
🔴 Testing with real roles: any contractor could read every maintenance request in the system

Bas Kramer runs Meldpunt Vastgoed from Amersfoort, a facility management SaaS built with Lovable and Supabase: property managers log maintenance requests, and contractors update their status. Before a contract with a housing association, he ran the first two checks. Both green. The housing association still wanted proof of an independent review, and pentest prices made Bas hesitate.

Why the lights disagreed: every table had Row Level Security, which kept the advisor happy. But the policies themselves were the problem. LaunchStudio's test, with accounts for two property managers and two contractors, found:
🔴 Several policies let any authenticated user read all maintenance requests, across all properties
🔴 Contractors could change the status of other contractors' jobs by calling the API directly
🔴 Photo uploads in a public bucket
🔴 A service key used in an Edge Function that could be called without authentication

Turning red to green (LaunchStudio, 6 business days, €2,200):
✓ Policies rewritten for each role, with automated tests for every table
✓ Contractor updates restricted to their assigned jobs
✓ Photos in private storage, with signed links
✓ The Edge Function secured, and the key rotated
✓ Rate limits and security headers
✓ A tested backup restore, and a report

The housing association accepted the report for the first contract year, and asked for a formal pentest before renewal. When that pentest happened a year later, it found just two low-severity issues.

"Every automated check was green. One afternoon of testing with real roles showed that any contractor could read every request in the system." - Bas Kramer

https://launchstudio.eu/en/blog/cost-of-a-security-review-for-an-ai-built-app

#Security #Pentest #Supabase #Lovable #AIFounder #LaunchStudio #Manifera
