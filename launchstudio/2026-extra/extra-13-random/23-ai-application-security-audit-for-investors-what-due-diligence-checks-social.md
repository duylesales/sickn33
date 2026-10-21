🚨 Julian Maas, a former construction project manager in Amsterdam, built Prijsbouwer with Bolt and later Cursor: SaaS that lets renovation contractors turn room measurements into detailed quotes, with client approval and deposits. Ninety contractors paid monthly. An Amsterdam seed fund issued a term sheet — subject to technical due diligence in six weeks. 😳

Julian had a pre-diligence review done first. Contractors could read each other's material price libraries through an unprotected API route. The GitHub repo was still owned by a freelancer, with a Stripe secret key in its history. Backups covered seven days and had never been restored. There was no IP assignment, and the only documentation was a Cursor rules file. Here's what investor due diligence checks in an AI-built app: 🧠

❌ Cross-tenant access to commercially sensitive data
❌ Code and secrets owned by a former freelancer
❌ Untested, short backups
❌ No documentation an outside reviewer can follow

✅ Row level security closing the cross-tenant exposure
✅ All secrets rotated, the repository moved to company ownership, IP assignment signed
✅ Backups extended to 30 days with a documented restore
✅ Vulnerable dependencies updated and a four-page technical overview — with every finding marked resolved in the data room

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we look before the investors do — so their reviewer finds a clean system and a clear story. ⚙️

His result: €4,600, fourteen business days. The fund's reviewer raised no blocking issues, the round closed on the original terms, and the overview was called "unusually clear for a company at this stage." 🚀

👉 AI application security audit for investors: what due diligence checks: https://launchstudio.eu/en/blog/ai-application-security-audit-for-investors-what-due-diligence-checks

#DueDiligence #SeedFunding #Startups #AppSecurity #LaunchStudio #Manifera
