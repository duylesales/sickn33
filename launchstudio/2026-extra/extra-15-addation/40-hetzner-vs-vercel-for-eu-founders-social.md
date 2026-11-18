📐 BLUEPRINT: one video platform, four homes

Thomas Verhoeven built Coachclip with v0, Next.js and Supabase: sports coaches upload training videos, draw annotations and share feedback with players. Hosted entirely on Vercel, it worked beautifully for the first football and hockey clubs.

Then clubs uploaded more video, and the bill climbed fast, driven by bandwidth and long-running video processing in serverless functions that kept hitting timeouts.

Thomas thought about moving everything to a Hetzner server. Then he remembered: he had no experience running servers, and his co-founder was a former coach, not an engineer. A review added two more findings: videos were served through the application instead of from storage, and transcoding ran inside request handlers.

So LaunchStudio drew a hybrid (13 business days, €5,300):

🏠 HOME 1: Vercel, European region
The Next.js frontend, keeping fast deployments and previews.

🏠 HOME 2: EU object storage with a CDN
All videos, served through signed URLs, which took most of the bandwidth off the application.

🏠 HOME 3: A hardened Hetzner server in Germany
A background worker for transcoding. Deployed automatically from GitHub, SSH key access, firewall, automatic security updates, monitoring and alerts.

🏠 HOME 4: Supabase in Frankfurt
Still the database and authentication layer, with a job queue table coordinating the app and the worker.

THE RESULT
Infrastructure costs down roughly 65%. Video processing reliable, no more timeouts. Thomas keeps Vercel's convenience, and the Hetzner worker runs as part of LaunchStudio's managed hosting.

"I wanted cheap servers, but I didn't want to become a system administrator. The hybrid gave me the savings without the 3 a.m. alerts." - Thomas Verhoeven

Hetzner vs Vercel? Maybe both: https://launchstudio.eu/en/blog/hetzner-vs-vercel-for-eu-founders

#Hetzner #Vercel #CloudCosts #SportsTech #AIFounder #LaunchStudio #Manifera
