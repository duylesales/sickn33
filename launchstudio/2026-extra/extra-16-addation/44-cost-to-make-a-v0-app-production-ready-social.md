🎬 A film set for home energy

Sophie Meijer's dashboard looked like a finished street. Polished screens showing each home's energy use, recommended improvements and available subsidies. A regional housing cooperative wanted to offer it to 400 members.

Behind the front doors:
🎭 Most screens used sample arrays inside the components
🎭 There were no logins
🎭 The only real data was a contact form, sending emails through a key visible in the browser

Sophie runs an energy advice business in Groningen and built Woningwatt with v0. Everyone loved the demo. Nobody knew the numbers were made up.

Building the real street behind the set (LaunchStudio, 8 business days, €2,900):
🏗️ A data model for homes, meter readings, recommendations, subsidies and advisors, in Supabase in an EU region, with Row Level Security
🏗️ All eleven screens connected to real queries through server actions, with session and ownership checks, server-side validation, and proper loading and error states
🏗️ Magic link login for homeowners, and a separate role for advisors to update recommendations
🏗️ A CSV import for the cooperative's meter readings
🏗️ The contact form moved to a server action, and the exposed key rotated
🏗️ Deployment on Vercel with a custom domain, separate preview and production environments, email authentication, backups and monitoring

The cooperative onboarded 400 members in its first month. And the screens they saw were exactly the ones from the original demo, now showing each member's real home. Sophie still designs new screens in v0, and connects them to the documented data layer.

"Everyone loved the demo. Nobody knew the numbers were made up. Now the same screens show each member's real home." - Sophie Meijer

https://launchstudio.eu/en/blog/cost-to-make-a-v0-app-production-ready

#v0 #Vercel #NextJS #Supabase #AIFounder #LaunchStudio #Manifera
