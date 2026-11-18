🔑 THE ROTATION ORDER, the night a repository went public

1. The mapping API key
Why first: abuse was already happening, and costing money. 140,000 requests in eleven hours, from addresses she didn't recognise.

2. The Supabase service role key
Why second: it has unrestricted access to the whole database, every inspection report included.

3. The email provider credentials
Why: assume every credential in the file is compromised, used or not.

4. The payment webhook signing secret
How: with the handler accepting both old and new secrets for a while, so no deliveries were dropped.

Suzanne Grotenhuis built Inspectierapport in Lovable: inspection reporting for building surveyors and installation inspectors, 39 firms, around 2,000 reports a month. She made her repository public to share a code sample with a prospective contractor, and made it private again four days later. But an environment file committed eleven months earlier, before ignore rules existed, held all four secrets. Scanners found it within a day. She found out when the mapping provider suspended her account. 🏗️

It took her an hour to realise the file also held the key that can read every report in the product.

The rest of the response (LaunchStudio, same-evening triage, then 2 business days, €3,100):
✓ Database access logs reviewed with Supabase support: no queries from unknown sources in the window
✓ Email provider logs reviewed: no sends
✓ A breach assessment documented, with legal advice, ending in a precautionary report to the Autoriteit Persoonsgegevens
✓ Secret scanning in the build
✓ Ignore rules corrected, and history rewritten as hygiene
✓ Shared logins replaced by per-person access in a password manager
✓ A credential inventory: nine secrets, their scope, where each is used, and when each was last rotated

The mapping provider waived €2,840 of usage after reviewing the timeline. No evidence of database or email access was found. Suzanne's own conclusion: the real incident was the service role key sitting in that file for eleven months. The four public days were just when it got noticed.

"I rotated the mapping key first because that was the one costing me money. It took me an hour to realise the file also had the key that can read every inspection report in the product." - Suzanne Grotenhuis

https://launchstudio.eu/en/blog/ai-app-security-rotating-every-secret-after-a-leak

#IncidentResponse #Secrets #AppSecurity #Lovable #LaunchStudio #Manifera
