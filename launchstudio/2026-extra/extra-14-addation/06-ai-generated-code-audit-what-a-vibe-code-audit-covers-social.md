🚨 Pieter-Jan Claes, an HR consultant in Ghent, built Startdag with Lovable and Cursor: onboarding software where companies send new hires contracts and policies to sign. A Dutch staffing agency with 300 placements a year wanted to roll it out - after an independent security review. 😳

The app passed every demo. The audit found eleven issues, three of them critical. Here's what "nothing looked wrong" was hiding: 🧠

❌ Signed contracts in a public storage bucket with predictable file names
❌ An RLS policy that let any logged-in user list every company's documents
❌ An admin endpoint that trusted an is_admin value sent from the browser
❌ No retention rules, and an email provider outside the EU without a documented transfer basis

✅ Private bucket with signed, expiring URLs
✅ RLS policies rewritten around company membership
✅ Admin checks moved to the server
✅ Retention rules plus documented processors and data locations for the agency's privacy officer

At **LaunchStudio**, backed by Manifera's security-first engineering and 11+ years of delivery, a vibe code audit gives you prioritised findings, fixes and a summary you can share with customers. 🛠️

💡 His result: €5,400, fourteen business days. The re-test confirmed every critical and high finding fixed, the agency signed a two-year contract, and the audit summary is now a standard attachment in his sales calls. 🚀

👉 Built with Lovable, Bolt, Cursor, v0 or Replit? See what a vibe code audit covers: https://launchstudio.eu/en/blog/ai-generated-code-audit-what-a-vibe-code-audit-covers

#VibeCoding #AISecurity #CodeAudit #GDPR #LaunchStudio #Manifera
