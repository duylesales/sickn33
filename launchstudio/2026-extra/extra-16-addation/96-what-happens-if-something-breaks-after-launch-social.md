🔧 Two bugs after launch. Two different answers.

Ruud Veenstra runs Fietsfix from Groningen, a SaaS for bicycle repair shops built with Bolt and Supabase, used by around 50 shops for repair orders and customer notifications. After a Launch Ready project, everything ran smoothly, through the 48-hour window and the weeks after.

BUG #1: six weeks after launch
What happened: a shop owner noticed that repair orders created on the last day of the month were missing from the monthly invoice export.
How Ruud reported it: a screenshot and the dates.
The cause: in the export function LaunchStudio had rewritten during the project, a date comparison excluded the last day of the month for shops with a particular time zone setting.
Whose work: LaunchStudio's delivered work.
Cost: included.
The fix: made on staging, with a test covering month boundaries, released the next morning, and the affected exports regenerated.

BUG #2: two months after that
What happened: SMS notifications stopped.
The cause: Ruud had switched SMS providers himself, with his AI tool, and the new provider's webhook wasn't verified.
Whose work: new work.
Cost: a small fixed amount, quoted before starting, which Ruud accepted.
The fix: the new provider integrated properly.

Both resolved within one business day of being reported.

After that, Ruud moved to Launch & Grow, so alerts reach the team directly and small fixes fall within the monthly service.

"The first bug was theirs and they fixed it without discussion. The second was mine and they told me what it would cost before starting. That clarity is why I stayed." - Ruud Veenstra

https://launchstudio.eu/en/blog/what-happens-if-something-breaks-after-launch

#PostLaunch #Support #Bolt #SaaS #AIFounder #LaunchStudio #Manifera
