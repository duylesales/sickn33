🗓️ Fridays at Klimslot

FRIDAY 1: Update published. The booking calendar shows no slots.
FRIDAY 2: Update published. New members can't sign up.
FRIDAY 3: Update published. A database change wipes course capacity for existing courses.
Every weekend after: Lars fixes it while members email the front desk.

Lars Mulder runs a network of climbing gyms in Utrecht and built Klimslot with Lovable and Supabase for booking time slots and courses. He improved it every week, usually on quiet Friday afternoons. Three Fridays in a row, something broke in production.

Because production was the only environment there was. And the inventory showed more:
• The Supabase project sat in the account of a freelancer who'd helped at the start
• The domain was registered privately by a former partner
• The live Stripe key was used for testing
• Database changes left no record

What LaunchStudio set up (5 business days, €1,950):
✓ The Supabase project and domain moved into Lars's business accounts
✓ Separate staging and production projects, each with its own keys and data
✓ Lovable connected to GitHub, with a pipeline: staging automatically, production on approval
✓ Database changes captured as migrations and applied through the pipeline
✓ Email authentication records, so booking confirmations stop landing in spam
✓ A tested restore to staging, uptime monitoring and error tracking
✓ A rollback, practised by Lars during handover

FRIDAYS NOW
Changes almost every week for three months, and no production incidents. Twice, a change that would have broken bookings was caught on staging. Confirmations reach inboxes again, and front desk complaints dropped noticeably.

"I still build on Friday afternoons. The difference is that now Friday's mistakes stay on staging." - Lars Mulder

https://launchstudio.eu/en/blog/production-deployment-service-for-ai-built-apps

#Deployment #Lovable #Supabase #DevOps #AIFounder #LaunchStudio #Manifera
