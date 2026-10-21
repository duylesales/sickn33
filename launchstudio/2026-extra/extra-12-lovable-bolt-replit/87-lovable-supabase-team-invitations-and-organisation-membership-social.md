🚨 Joost Verhagen's Werkbonapp runs digital work orders for 48 installation companies — around 600 technicians. Team support had been added in Lovable with an invite button and one organisation_id column per profile. Then an installer noticed work orders being viewed by a technician they'd removed four months earlier. 😳

"Removing" someone only hid them from the team list. Their access through the API was untouched — and the invite links never expired. Here's how to build team invitations and memberships that actually hold: 🧠

❌ One organisation_id per profile, so a subcontractor couldn't belong to two installers
❌ Invite links containing the organisation ID, never expiring, usable by anyone
❌ Removal that set a flag instead of revoking access or ending sessions
❌ No audit of who invited, changed or removed whom

✅ Separate memberships and invitations tables; all 600 profiles backfilled
✅ Row level security rewritten across 17 tables around one membership helper, verified with cross-organisation tests
✅ Random, hashed invite tokens: 7-day expiry, single use, bound to the invited email
✅ Removal that deletes the membership, signs out sessions and revokes tokens — plus a last-owner guard and an audit log

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build this when a single-user product gets its first team customer. ⚙️

His result: €3,400, three business days. The backfill found 37 departed technicians across 11 companies who still had access — four had used it. All revoked on day one, and two installers upgraded because adding subcontractors finally worked. 🚀

👉 Lovable Supabase: team invitations and organisation membership: https://launchstudio.eu/en/blog/lovable-supabase-team-invitations-and-organisation-membership

#Supabase #Lovable #SaaS #AppSecurity #LaunchStudio #Manifera
