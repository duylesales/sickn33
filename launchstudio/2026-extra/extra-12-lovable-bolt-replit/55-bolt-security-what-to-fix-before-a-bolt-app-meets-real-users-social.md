🚨 Quinten Aardema built Leveranciersportaal with Bolt in a weekend - a portal where a food wholesaler's 90 suppliers submit price lists, certificates and delivery schedules. The wholesaler loved the demo and asked when it could go live. "Next week," he said. It worked. 😳

The pre-launch review found the service role key in the frontend, 23 endpoints with no supplier check - so any supplier could read every competitor's prices by changing one number - and certificates in a public bucket. Here's what to fix before a Bolt app meets real users: 🧠

❌ Unrestricted database keys shipped to the browser
❌ No authorisation: every logged-in user could see every record
❌ Validation only in the browser - negative prices and 1970 delivery dates accepted
❌ Public storage, unauthenticated routes, no rate limits, and an old preview still holding old keys

✅ The service role key rotated, with all data access behind server functions using an anon key and policies
✅ Row-level security on all nine tables and authorisation on all 23 endpoints
✅ Server-side schema validation on every input, a private certificate bucket with signed URLs
✅ Rate and size limits, timeouts, the old preview retired, and a one-page record of what was checked

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we tell you what a stranger can currently do with your Bolt project - and close it. 🔒

His result: two business days and €2,900 later, the portal launched a week late with 90 suppliers and has run for two years. That week's delay, he says, was the best decision in the project. 🚀

👉 What to fix before a Bolt app meets real users: https://launchstudio.eu/en/blog/bolt-security-what-to-fix-before-a-bolt-app-meets-real-users

#Bolt #AppSecurity #Prototyping #Supabase #LaunchStudio #Manifera
