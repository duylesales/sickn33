🖱️ What happened when an installer clicked "Remove" on a technician

✓ Hidden from the team list
✓ A flag set
✗ The organisation column on their profile: untouched
✗ Their access through the API: untouched
✗ Their sessions: still signed in

And the invite link that brought them in? It held the company's ID, never expired, and let anyone who opened it sign up into that company.

Joost Verhagen built Werkbonapp in Lovable: digital work orders for 48 installation companies, around 600 technicians. Teams had been added with an invite button and an organisation_id column on each profile. 🔧

Two things surfaced in one month:
• A subcontractor working for two installers couldn't be added to the second, because a profile could only hold one organisation. The workaround was a second email address.
• An installer saw work orders being viewed by an account they'd removed four months earlier.

What "Remove" does now (LaunchStudio, 3 business days, €3,400):
✓ Deletes the membership
✓ Signs out every session
✓ Revokes calendar feed tokens
✓ Keeps their work orders, attributed to "former member"
✓ Writes the event to an audit log each company's admins can see

And around it:
✓ Separate memberships and invitations tables, with all 600 profiles backfilled
✓ Row level security on 17 tables rewritten around a membership helper, checked with a cross-organisation test suite
✓ Invite tokens that are random, hashed, single-use, bound to the invited email, and expire after seven days, with every old-style link invalidated
✓ A last-owner guard in the database, and seat counts checked at invite and acceptance

The backfill found 37 removed technicians across 11 companies who still had working access. All were revoked on day one. Logs showed four had used it after removal. Subcontractors now belong to several installers with one login, and two installers moved to bigger plans within the month because adding subcontractors finally worked.

"Removing someone took them off the screen and nothing else. Thirty-seven people who had left still had access, and four of them had used it." - Joost Verhagen

https://launchstudio.eu/en/blog/lovable-supabase-team-invitations-and-organisation-membership

#Supabase #Lovable #SaaS #AppSecurity #LaunchStudio #Manifera
