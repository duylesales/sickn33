🚨 Thijs Hendriks built Dossierdesk with Lovable and Supabase: a portal where an immigration law firm's clients upload documents, follow their application and message their lawyer. Around 220 clients used it. Then new clients started calling: the portal showed a white screen after login. 😳

Existing clients were fine, and Thijs couldn't reproduce it. One screenshot of the console told the story: Cannot read properties of null (reading 'case_number'). Here's why apps show a blank white screen: 🧠

❌ A dashboard assuming every client already had a case record
❌ Reloading any sub-page returning a 404 on the live host
❌ Blank pages after each deploy when old JavaScript chunks disappeared
❌ No error boundaries and no monitoring

✅ Empty states, with a welcome page for new clients waiting for their case
✅ A rewrite rule so sub-pages reload correctly
✅ One automatic reload on failed chunk loads
✅ Error boundaries and Sentry - which caught two more crashes in the first week

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we turn total failures into contained, reported ones. 🛠️

The result: €1,900, 5 business days. No blank-screen reports since, support calls about the portal dropped from several a week to almost none, and new clients now finish uploads in their first session. 🚀

👉 Is your app showing a white screen? Here's how to find the real error: https://launchstudio.eu/en/blog/why-does-my-app-show-a-blank-white-screen

#React #Lovable #ErrorMonitoring #LegalTech #AIFounder #LaunchStudio #Manifera
