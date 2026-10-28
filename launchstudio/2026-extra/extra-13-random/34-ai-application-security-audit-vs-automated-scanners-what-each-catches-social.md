🚨 Niels Brandsma, a backend developer in Hoofddorp, built SlotPark with Cursor: companies near Schiphol share unused parking spaces with each other's employees. Security-conscious, he ran Dependabot, Semgrep, gitleaks and a weekly OWASP ZAP scan. All green. Twelve companies, 400 employees. Then a prospective airline-services customer required an independent review before signing. 😳

The review found nothing the scanners had missed in their own categories - and four things they couldn't see. Any employee could view and cancel other companies' bookings by changing an ID. The company-admin API checked that you were an admin, but not of which company. RLS was on with a policy allowing reads by any authenticated user. And invoice amounts came from prices the client sent. Here's what scanners catch - and what only a security audit finds: 🧠

❌ Broken access control by changing an ID
❌ Admin checks without a tenant check
❌ RLS that exists but allows everything
❌ Prices trusted from the client

✅ Ownership and tenant checks fixed on the server
✅ RLS policies rewritten to scope by company and user
✅ Price calculation moved to the server
✅ 27 automated authorisation tests for every role and tenant boundary, in the same CI pipeline as the scanners

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we use tools as instruments - and human judgement for what they can't know: who should own which data. ⚙️

His result: €1,250, five business days. The airline-services company signed after the review and re-test report, and over the next year the authorisation tests caught two regressions the still-green scanners missed. 🚀

👉 AI application security audit vs automated scanners: what each catches: https://launchstudio.eu/en/blog/ai-application-security-audit-vs-automated-scanners-what-each-catches

#AppSecurity #SAST #DevSecOps #Cursor #LaunchStudio #Manifera
