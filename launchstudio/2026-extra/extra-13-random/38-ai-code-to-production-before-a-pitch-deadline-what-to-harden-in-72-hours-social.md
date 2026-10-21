🚨 Max Kuipers, a former chef in Amsterdam, built Groentegilde in Bolt: households subscribe to weekly veg boxes from farms around Amsterdam, pick pickup points and skip weeks. He was selected for an accelerator demo day — with investors who, the organisers warned, "like to sign up live". He had 72 hours. 😳

The triage found the Mollie live key in the frontend bundle, home addresses of his 60 pilot households readable by any logged-in user, an admin page for farm order lists with no authentication, and the app running on a Bolt preview URL that changed every time he edited anything. Here's what to harden when AI code goes to production before a pitch deadline: 🧠

❌ A live payment key in the browser
❌ Real customers' addresses exposed to anyone with an account
❌ An admin page open to the internet
❌ A demo on a URL that could change mid-pitch

✅ The Mollie key rotated and payment creation moved server-side, with test mode and a visible banner for the demo
✅ Household-level access on subscriptions and addresses
✅ The admin page locked behind server-side roles
✅ A separate demo database with fictional households, his own domain with SSL and an uptime check — and a code freeze 18 hours before the pitch

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make your app safe for exactly the people who'll click it on demo day — then finish the job properly. ⚙️

His result: €1,900, three days. Three panel members signed up live without incident, Max answered the data-protection question specifically, and Groentegilde got a pre-seed offer. Full hardening followed two weeks later. 🚀

👉 AI code to production before a pitch deadline: what to harden in 72 hours: https://launchstudio.eu/en/blog/ai-code-to-production-before-a-pitch-deadline-what-to-harden-in-72-hours

#DemoDay #Pitch #Startups #Bolt #LaunchStudio #Manifera
