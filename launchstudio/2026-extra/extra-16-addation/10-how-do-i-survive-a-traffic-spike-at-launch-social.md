📋 LAUNCH RUNBOOK: Budgetbuddy, Sunday morning

THE MOMENT
Femke Jansen built Budgetbuddy with Lovable and Supabase: a personal finance app for young adults that categorises spending and sets savings goals. A popular Dutch personal finance newsletter, with tens of thousands of subscribers, agreed to feature it on a Sunday morning. Femke had tested it with friends.

PRE-LAUNCH REVIEW: the bottlenecks
⚠️ The landing page was an app route, loading the full JavaScript bundle and querying the database for testimonials before rendering
⚠️ Confirmation emails went through the default development email service, with low limits. Most new users would never have received theirs.
⚠️ Onboarding generated an AI savings plan during sign-up: up to fifteen seconds per user, with no rate limit
⚠️ Load test, 2,000 simulated sign-ups in fifteen minutes: failed after a few hundred

PREPARATION (LaunchStudio, 8 business days, €3,200)
☑ A static, server-rendered landing page on a CDN, with optimised images and testimonials embedded at build time
☑ Auth emails through a transactional provider via custom SMTP, authenticated domain, adequate quotas
☑ The AI plan moved to a background job: a simple default plan shown immediately, the personalised one shortly after, rate-limited per account with a spending cap
☑ Turnstile on sign-up, and indexed onboarding queries
☑ Compute upgraded for launch week
☑ A waitlist switch and a monitoring dashboard on standby
☑ Load test, 5,000 sign-ups in fifteen minutes: no errors

LAUNCH DAY
Around 6,400 visitors and about 2,300 sign-ups in the first three hours. No errors. Confirmation emails within seconds. Waitlist switch: never used. Compute scaled back down the following week.

"Without the review, my big moment would have been thousands of people waiting for an email that never came." - Femke Jansen

https://launchstudio.eu/en/blog/how-do-i-survive-a-traffic-spike-at-launch

#Launch #Lovable #Supabase #ProductHunt #AIFounder #LaunchStudio #Manifera
