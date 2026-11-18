MYTH: "Forty prompts in, a Bolt app needs a rebuild."
FACT: Tim's app stayed the same. Only the parts he couldn't see were fixed. ⚽

Tim Groen runs a sports club management start-up in Apeldoorn and built Clubkas with Bolt and Supabase: amateur football clubs manage members, collect contributions through Mollie and plan volunteer shifts. After about forty iterations, it worked well for his own club. Five other clubs wanted to join.

MYTH: "If it works for my club, it's safe for six."
FACT: Three tables had Row Level Security switched off after an error during development. Any logged-in member could read every member's address and phone number.

MYTH: "The payment page knows who paid."
FACT: Members were marked as paid on the redirect page, not by Mollie.

MYTH: "My project is mine."
FACT: The Supabase project was linked to a personal account belonging to Tim's brother.

Also found: three versions of the member list component, two unused, and default Supabase emails that often failed.

What LaunchStudio did (5 business days, €1,950):
✓ Policies rewritten for members, board members and administrators, with tests
✓ Payments moved to verified Mollie webhooks, with existing payment records reconciled
✓ Unused components removed
✓ The Supabase project transferred to Tim's company
✓ A custom email provider configured
✓ Netlify with a custom domain, plus backups and monitoring
✓ Project instructions, so Bolt keeps the policies in place

Within a month, all five new clubs onboarded, around 1,200 members in total. Tim kept building in Bolt, and the tests caught one policy change from a later prompt before it reached production.

"I expected to hear that I needed to rebuild everything. Instead the app stayed the same, and the parts I could not see were fixed." - Tim Groen

https://launchstudio.eu/en/blog/cost-to-make-a-bolt-app-production-ready

#Bolt #Supabase #Mollie #ProductionReady #AIFounder #LaunchStudio #Manifera
