🎮 CHARACTER SHEET: Support Agent (before the fix)

Class: support team member (one of five)
Powered by: the Supabase service role key
Can view: every subscriber's details and payment status
Can edit: all of it
Special ability: export all data
Special ability: issue refunds
Leaves a trace: never

Ivo Ramaker runs Fietsabonnement, a bike subscription service in Amsterdam with about 2,000 subscribers. His customer app was built in Lovable. For his support team, he quickly built an internal panel in Lovable too, using the service role key so the panel could "see everything."

He considered moving the panel to Retool. LaunchStudio compared the options with him: his data was already in Supabase, the panel needed a custom bike swap workflow, and he didn't want per-user fees as the team grew. They kept Lovable, and fixed the character sheet (7 business days, €2,600):
✓ The service role key removed from the panel
✓ Staff roles in a roles table: agent, senior agent, admin
✓ RLS policies for staff access
✓ Refunds and exports moved into edge functions, limited to senior roles
✓ An audit log of sensitive actions, with a review screen for Ivo
✓ MFA for all staff

🎮 CHARACTER SHEET: Support Agent (after)
Can view: what the role allows
Refunds and exports: senior roles only
Leaves a trace: always

The team kept a fast, custom panel. Ivo can see who issued every refund and export. And two months later, the audit log resolved a customer dispute in minutes.

"I built the support panel for speed. I hadn't noticed I'd also built the most dangerous screen in my company." - Ivo Ramaker

https://launchstudio.eu/en/blog/lovable-vs-retool-for-internal-tools

#Lovable #Retool #InternalTools #Supabase #LaunchStudio #Manifera
