🗓️ SIX MONTHS OF A KEY IN THE BUNDLE

MARCH
Jelmer Ottevanger is building Inkoopportaal with Lovable: a purchasing portal where 19 wholesalers publish price lists and around 300 retailers place orders. An AI session hits a Row Level Security error while writing an admin report. Its fix: use the Supabase service role key. Because the report runs in the browser, the key gets a public prefix. The report works. Nobody looks at it again.

APRIL TO AUGUST
The key that can read every wholesaler's pricing is in every JavaScript bundle the site serves.

SEPTEMBER
Jelmer reads an article much like this one, opens his own site's source, and searches for the variable name.

THAT SAME EVENING (LaunchStudio, 1 business day, €1,700)
✓ The service role key rotated at Supabase, before anything else
✓ The admin report rewritten as a server-side function with proper authorisation, using the anon key and policies like the rest of the app
✓ The whole deployed bundle searched for other secrets, finding an email provider key that got there the same way
✓ Both credentials rotated, and access logs reviewed with Supabase support: no unexpected usage in the period
✓ Three separate environment sets, since staging had been sharing production's database and email credentials
✓ An example file committed, with a startup check for eleven required variables
✓ Preview deployments given their own values, behind access protection
✓ A pre-deploy check that scans the built output for known secret patterns, and fails the build

SIX WEEKS LATER
A new AI session tried to reference a server-side key from browser code. Same mistake, same reason. The build scan blocked it.

No evidence the key was ever used, which Jelmer calls luck, not a result.

"It worked, so I never looked at it again. The key that can read every wholesaler's pricing had been sitting in a file anyone could download for six months." - Jelmer Ottevanger

https://launchstudio.eu/en/blog/lovable-hosting-environment-variables-across-three-environments

#Secrets #DevOps #Supabase #Lovable #LaunchStudio #Manifera
