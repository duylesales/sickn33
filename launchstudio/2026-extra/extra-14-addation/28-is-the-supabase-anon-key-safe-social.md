🔑 A visitor badge and a master key look alike from a distance.

The anon key is the visitor badge. It's meant to be in your app's code. What it opens depends on your Row Level Security policies.

The service role key is the master key. It opens everything, ignores every policy, and should never leave the server.

Olivier Maes's festival app had the master key in the bundle.

Olivier coordinates volunteers for a music festival near Leuven and built Shiftwissel with Bolt and Supabase: volunteers pick shifts, swap them with each other and get their wristband details. About 600 volunteers signed up in two weeks.

Then a volunteer with a development background sent a message: the app's JavaScript contained a key whose decoded role was service_role. Bolt had used it to make "swap shift" work, because the anon key's policies didn't let one volunteer update another's shift. With that key, anyone could read every volunteer's phone number and address, or delete the entire shift schedule.

What LaunchStudio did (4 business days, €1,350):
⏱️ The key rotated within the hour
🔍 Logs checked for unusual access: nothing beyond the volunteer's own test
✓ Swap logic moved into an edge function that checks both volunteers agreed
✓ RLS on every table: volunteers read only their own details and the public shift schedule
✓ A staging project for future changes

During the festival, Shiftwissel handled about 1,100 shift swaps without incident. Olivier told volunteers openly about the fix, and the organisers adopted the app for the next year.

"The anon key was in the code because it should be. The other key was in the code because the AI needed a shortcut. I didn't know there was a difference." - Olivier Maes

https://launchstudio.eu/en/blog/is-the-supabase-anon-key-safe

#Supabase #AppSecurity #Bolt #Events #LaunchStudio #Manifera
