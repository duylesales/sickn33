🔒 Dorian built Ledgerly, a multi-tenant AI bookkeeping platform, using **Bolt** — but a €140,000 enterprise contract was contingent on passing a SOC 2 Type I audit in just 30 days. 🧠

If your multi-tenant AI platform has Row Level Security defined but not consistently enforced, no change management process, and no incident response plan, a SOC 2 audit will find every single gap.

❌ RLS present in the schema but relying on application code, not the database, to isolate tenant data
❌ A single shared admin credential with unrestricted, unlogged database access
❌ No documented incident response plan, sub-processor inventory, or deployment review process

✅ RLS rewritten and enforced on every tenant table, scoped to a `firm_id` claim, tested against adversarial queries
✅ Role-based access control, MFA, and a GitHub-based change management workflow with pull request review
✅ A documented incident response plan and encrypted backups, built alongside the founder

At **LaunchStudio**, we've been fixing exactly this class of production engineering problem since 2014 through Manifera, across 160+ delivered projects. 🛡️

Ledgerly passed its SOC 2 Type I audit with no exceptions, five days ahead of deadline, and Dorian signed the €140,000 annual contract. (€6,400 (Enterprise Hardening Package) — audit-ready in 19 business days.) 🚀

👉 See how we fixed it: [Link to article]

#LaunchStudio #Manifera #AISaaS #SOC2 #MultiTenantSecurity
