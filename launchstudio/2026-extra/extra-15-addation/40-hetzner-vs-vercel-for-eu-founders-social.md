🚨 Thomas Verhoeven built Coachclip with v0, Next.js and Supabase: sports coaches upload training videos, draw annotations and share feedback with players. Hosted entirely on Vercel, it worked beautifully - until clubs uploaded more video and the monthly bill climbed fast. 😳

Bandwidth and long video processing in serverless functions drove costs and timeouts. Thomas considered moving everything to Hetzner - but had never run a server. Here's how EU founders can choose between Hetzner and Vercel: 🧠

❌ Video files served through the application
❌ Transcoding inside request handlers, hitting timeouts
❌ A fast-rising bandwidth bill
❌ A full move to servers nobody on the team could run

✅ The Next.js frontend kept on Vercel with European functions
✅ Videos in EU object storage with a CDN and signed URLs
✅ Transcoding on a hardened Hetzner worker in Germany, deployed from GitHub with monitoring
✅ Supabase in Frankfurt with a job queue coordinating app and worker

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we give you the savings without the 3 a.m. alerts. 🛠️

His result: €5,300, 13 business days. Monthly infrastructure costs dropped by roughly 65%, video processing became reliable with no more timeouts, and the worker runs under LaunchStudio's managed hosting. 🚀

👉 Hetzner or Vercel for your EU SaaS? Here's how to decide: https://launchstudio.eu/en/blog/hetzner-vs-vercel-for-eu-founders

#Hetzner #Vercel #CloudCosts #SportsTech #AIFounder #LaunchStudio #Manifera
