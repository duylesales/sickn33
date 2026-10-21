🚨 Renske Bouhuijs built Zwemlesplanner with Bolt — lesson scheduling and attendance for swimming schools. Three schools signed up within a month at €45/month each. For five months, the whole business ran on a Bolt preview link that parents bookmarked. 😳

Then, in one week: the preview went down for hours during a platform incident, with nothing she could do. And a school asked for her company website before renewing. It didn't exist. Here's how to go from preview link to a real address: 🧠

❌ The product living entirely inside a prototyping tool
❌ An exported project carrying live database credentials
❌ One shared environment — she'd been testing against live data during lesson hours
❌ No domain, no email authentication, no rollback, no monitoring

✅ Code exported to her own repository, with leaked credentials removed and rotated
✅ Deployed from a branch push, functions pinned to the database's region — removing a noticeable delay
✅ Three separate environments, with staging protected and kept out of search
✅ A .nl domain with SSL and a canonical redirect, SPF/DKIM/DMARC before the first email, a rollback timed at 35 seconds, and uptime monitoring

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we put your Bolt project on your own address — usually in a day. 🌐

Her result: one business day and €1,900 later, all three schools renewed and two more joined within a quarter. And the environment split ended the risky habit of testing against live data. 🚀

👉 Bolt deployment: from preview link to a real address: https://launchstudio.eu/en/blog/bolt-deployment-from-preview-link-to-a-real-address

#Bolt #Deployment #Hosting #Startup #LaunchStudio #Manifera
