📝 THE SCORING SHEET: twelve questions, four suppliers

Hidde Sterk runs Bijlesplanner from Groningen, built with v0, Cursor and Supabase: tutoring agencies match students with tutors, schedule lessons and invoice parents through Stripe. Before a growth push, he wanted the app production ready, and spoke to four suppliers.

He couldn't judge code. But he could judge answers. So he asked every supplier the same twelve questions, and noted the answers in a spreadsheet.

SUPPLIERS A AND B
How will you test access between agencies? ✗ Couldn't explain
Bonus red flag: one suggested "turning off the strict security" to fix a permission error Hidde mentioned

SUPPLIER C
Most questions: ✓ answered well
Where will everything be hosted? ✗ In its own account

SUPPLIER D (LaunchStudio)
All twelve: ✓ answered specifically
Testing: with agency, tutor and parent accounts
Payments: webhook verification and reconciliation, explained
Ownership: everything stays in Hidde's accounts, confirmed in the quote

The project that followed (8 business days, €3,100) found three things:
• Parents could see other families' lesson notes through a shared view
• Stripe invoices were marked paid on the redirect
• The Supabase project was on a co-founder's personal account
All fixed, with role-based policies and tests, a secured view, Stripe webhooks, an ownership transfer, staging and monitoring.

The next quarter, Hidde onboarded twelve new tutoring agencies. And he shared his question spreadsheet with two founder friends, who used it for their own hiring decisions.

"I could not judge code, but I could judge answers. The same twelve questions made the differences between suppliers obvious within a week." - Hidde Sterk

https://launchstudio.eu/en/blog/questions-to-ask-before-hiring-help-for-production

#Hiring #Founders #v0 #Supabase #AIFounder #LaunchStudio #Manifera
