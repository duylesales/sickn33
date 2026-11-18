📊 AUDIT SCORECARD: Startdag

Total findings: 11
🔴 Critical: 3
🟠 High and medium: the rest, including missing retention rules for personal data and a non-EU email provider without a documented transfer basis

Pieter-Jan Claes, an HR consultant in Ghent, built Startdag with Lovable and refined it in Cursor: small companies send new hires contracts, policies and first-week schedules, and track what each person has signed. Two Flemish companies used it. Then a Dutch staffing agency with 300 placements a year wanted to roll it out, if an independent security review came first.

The demo had looked perfect. The three critical findings:
🔴 #1 Signed contracts in a public storage bucket, with predictable file names
🔴 #2 A Row Level Security policy on documents that let any logged-in user list every company's documents
🔴 #3 An admin endpoint that trusted an is_admin value sent from the browser

Pieter-Jan chose audit plus fixes (14 business days, €5,400):
✓ Documents moved to a private bucket with signed, expiring URLs
✓ RLS policies rewritten around company membership
✓ Admin checks moved to the server
✓ Retention rules that delete candidate documents after a configurable period
✓ Processors and data locations documented for the agency's privacy officer

RE-TEST SCORECARD
🔴 Critical: 0 open
🟠 High: 0 open

The staffing agency signed a two-year contract. And the audit summary is now a standard attachment in Pieter-Jan's sales conversations.

"Without the audit I would have sold contracts with a public link to every signed document. The scary part is that nothing looked wrong." - Pieter-Jan Claes

https://launchstudio.eu/en/blog/ai-generated-code-audit-what-a-vibe-code-audit-covers

#VibeCoding #AISecurity #CodeAudit #GDPR #LaunchStudio #Manifera
