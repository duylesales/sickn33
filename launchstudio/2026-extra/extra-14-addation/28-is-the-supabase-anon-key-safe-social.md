🚨 Olivier Maes coordinates volunteers for a music festival near Leuven and built Shiftwissel with Bolt and Supabase: volunteers pick shifts, swap them and get their wristband details. About 600 signed up in two weeks. Then a volunteer with a development background sent him a message. 😳

The app's JavaScript contained a key whose decoded role was service_role. Bolt had used it as a shortcut to make shift swaps work. Here's what that meant: 🧠

❌ A master key that bypasses Row Level Security, shipped to every visitor's browser
❌ Anyone could read every volunteer's phone number and address
❌ Anyone could delete the entire shift schedule
❌ The anon key's policies never allowed swaps - so the AI took a shortcut

✅ The service role key rotated within the hour, logs checked - no access beyond the volunteer's own test
✅ Swap logic moved into an edge function that verifies both volunteers agreed
✅ RLS on every table: volunteers read only their own details and the public schedule
✅ A staging project for further changes

At **LaunchStudio**, backed by Manifera and its founder's cybersecurity background, secrets management comes first in every review - before any feature work. 🛠️

💡 His result: €1,350, four business days. Shiftwissel handled about 1,100 shift swaps during the festival without incident, and the organisers adopted it for the following year. 🚀

👉 Is the Supabase anon key safe in your frontend? Yes - but only if your RLS is right. Here's how to check: https://launchstudio.eu/en/blog/is-the-supabase-anon-key-safe

#Supabase #AppSecurity #Bolt #Events #LaunchStudio #Manifera
