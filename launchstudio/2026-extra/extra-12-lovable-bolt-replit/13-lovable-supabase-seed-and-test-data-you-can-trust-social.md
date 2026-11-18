🎭 THE CAST OF THE TEST DATABASE
Test User
Jan Jansen
...and names like them: 30 people in total, all invented by the founder

🎭 THE CAST OF ONE REAL COURSE IN LIMBURG
Müller
Peña
Van 't Hoff

Sanne Verkerk built Deelnemerslijst in Lovable: registration and attendance for training providers, 73 providers, around 11,000 participants a year. Every feature worked perfectly before release, then produced a support ticket within a fortnight.

The one that forced the issue: the certificate export. For that Limburg course, the CSV came out with three malformed rows: Müller, Peña and Van 't Hoff. The provider only found out after sending 84 certificates to a corporate client, three of them blank. From the client's side, it was the provider's mistake.

Sanne had tested everything, against thirty people called Jan.

A cast that looks like real life (LaunchStudio, 2 business days, €2,300):
✓ A seed script generating 4,000 participants across twelve providers, deliberately uneven: one provider holding 2,600 of them
✓ Names with apostrophes and diacritics, plus a 180-character company name
✓ Records spread over two years, some older than two schema changes
✓ 15% with empty optional fields, and a few dangling references
✓ Four named test accounts, including a second provider for isolation checks and one deactivated user
✓ A staging refresh that copies production and anonymises during the copy: participants, free-text notes, uploaded certificates, audit logs and payment identifiers
✓ Email credentials removed from staging, with every address rewritten to a capture domain
✓ A local snapshot and restore, in four seconds

On its first run, the new seed reproduced the export bug, plus two nobody had reported: a list page that timed out for the largest provider, and a search that ignored diacritics completely. Support tickets caused by data shape fell from about three a week to two in the whole next quarter.

"I had tested everything. I had just tested it all against thirty people I invented, who were all called Jan and had all signed up last Tuesday." - Sanne Verkerk

https://launchstudio.eu/en/blog/lovable-supabase-seed-and-test-data-you-can-trust

#Supabase #Testing #DataQuality #Lovable #LaunchStudio #Manifera
