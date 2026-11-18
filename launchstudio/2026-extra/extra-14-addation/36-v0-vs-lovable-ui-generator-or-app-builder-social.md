📐 FLOOR PLAN: an architecture studio's website and client portal

Merel Kok runs a small architecture studio in Schiedam. She wanted Ontwerpkluis: a public portfolio that ranks for "renovation architect" in the Rotterdam region, plus a private client portal where clients review drawings, comment and approve design phases.

ATTEMPT 1: Everything in Lovable
The portal worked well. The portfolio pages were client-rendered and barely indexed after two months.

ATTEMPT 2: Everything in v0 with Next.js
The portfolio indexed quickly. The portal stalled on authentication and file permissions.

THE FINAL PLAN, drawn by LaunchStudio:

🏛️ GROUND FLOOR: open to the public
The v0 Next.js site on the main domain, with structured data on project pages and environment variables configured per Vercel environment.

🔐 FIRST FLOOR: clients only
The Lovable portal on a subdomain.
• Row Level Security, so clients see only their own projects
• Drawings in private storage with signed URLs
• Comment and approval flows with email notifications

🧱 FOUNDATION: shared by both
One Supabase project in Frankfurt.

Built in 13 business days, for €4,600.

COMPLETION REPORT
The portfolio pages were indexed within weeks and started bringing in renovation enquiries from Rotterdam and Delft. Fourteen active clients used the portal in its first quarter. Merel keeps editing each floor in the tool that suits it.

"I kept trying to pick one tool. The answer was to let each do what it's good at and connect them properly." - Merel Kok

https://launchstudio.eu/en/blog/v0-vs-lovable-ui-generator-or-app-builder

#v0 #Lovable #NextJS #SEO #LaunchStudio #Manifera
