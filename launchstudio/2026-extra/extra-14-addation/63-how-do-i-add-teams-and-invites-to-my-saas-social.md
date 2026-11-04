🚨 Rianne Mulders built Uurwerk in Lovable: time tracking and invoicing for freelance designers. It grew to 600 users - then small design agencies started asking for team accounts with shared clients, shared projects and one invoice. She prompted "add teams". It created a teams table, team members still couldn't see shared projects, and one attempt made every project visible to everyone. 😳

Teams sounded like one feature. It turned out to be a new foundation under every feature she already had. Here's why prompting didn't work: 🧠

❌ A teams table added, but every policy still based on user_id
❌ No memberships or roles, so no way to say who could see what
❌ No secure invitation flow
❌ Stripe billing still attached to individual users

✅ Organisations, memberships and invitations designed as one change
✅ organisation_id added to clients, projects, time entries and invoices, with every policy rewritten around membership
✅ An invitation flow with expiring tokens and seat limits, and Stripe customers moved to organisations with per-seat pricing
✅ All 600 existing users migrated into personal organisations over a weekend

At **LaunchStudio**, backed by Manifera's 120+ engineers and 11+ years of multi-tenant B2B systems, we build teams as the foundation they are - not a patchwork of prompts. 🛠️

💡 Her result: €4,700, thirteen business days. Existing freelancers noticed only a new "Invite team" button, 34 agencies joined team plans within three months, and average revenue per account roughly doubled. 🚀

👉 Turning your AI-built tool into a B2B SaaS? Here's how to add teams and invitations properly: https://launchstudio.eu/en/blog/how-do-i-add-teams-and-invites-to-my-saas

#SaaS #B2B #Supabase #Lovable #LaunchStudio #Manifera
