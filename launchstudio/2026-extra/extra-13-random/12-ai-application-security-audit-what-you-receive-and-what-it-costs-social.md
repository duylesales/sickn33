🚨 Eline Rademaker, a veterinary nurse in Apeldoorn, built Huisdierpas in Lovable: a marketplace connecting pet owners with vetted sitters - including pet medical notes on allergies and medication. Before launching beyond 40 pilot owners she collected quotes: a €450 automated scan, or a €14,000 penetration test. 😳

She chose neither. A €950 focused review found 13 issues - three critical: sitters could read every pet's medical notes, message threads opened by changing an ID, and a Supabase service key sat in the frontend. The automated scan she ran for comparison caught the key… and none of the access-control issues. Here's what a security audit should deliver - and cost: 🧠

❌ A cheap scan that misses logic flaws like broken access control
❌ A penetration test priced for an enterprise, not an early-stage app
❌ Medical notes readable across the whole platform
❌ A full-access service key in the browser bundle

✅ A written report: scope, ranked findings, evidence, fixes - and what was found sound
✅ Row level security tying medical notes to active bookings; participant checks on messages
✅ The service key rotated and removed from the frontend; rate limiting and upload limits
✅ A documented re-test showing every critical finding fixed

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering and a founder rooted in cybersecurity, we review the logic scanners can't see - at a fixed price. ⚙️

Her result: €2,750 total (€950 review + €1,800 fixes and re-test). Huisdierpas reached 520 owners and 85 sitters in four months, and the re-test report helped land a partnership with a regional pet insurer. 🚀

👉 AI application security audit: what you receive and what it costs: https://launchstudio.eu/en/blog/ai-application-security-audit-what-you-receive-and-what-it-costs

#AppSecurity #Lovable #SecurityAudit #Startups #LaunchStudio #Manifera
