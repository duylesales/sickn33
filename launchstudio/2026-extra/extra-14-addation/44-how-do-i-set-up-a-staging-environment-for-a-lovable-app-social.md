🚨 Wessel Jansen runs a padel and squash centre in Hoorn and built Baanboeker in Lovable: members book courts, pay per session and join waiting lists. One Friday evening he asked Lovable to add a "bring a guest" option and hit publish. On Saturday morning - the busiest booking time - nobody could book. 😳

Publishing on a Friday night felt efficient. Losing Saturday morning showed him what efficient really costs. Here's what went wrong: 🧠

❌ A new guest field required in the database but never sent by the older mobile booking form
❌ No staging environment to test the change first
❌ No previous version to roll back to
❌ Four hours of lost bookings while he reverted by prompting

✅ A staging Supabase project with seeded test members and courts
✅ Vercel deployments for main (staging) and production
✅ Mollie in test mode on staging and schema changes moved into migrations
✅ A one-page release routine and one-click rollbacks through the host

At **LaunchStudio**, backed by Manifera's 160+ projects where separate environments are standard, we give every change a safe place to land before your customers see it. 🛠️

💡 His result: €1,250, four business days. Over the next three months Wessel shipped 14 changes through staging - two would have broken bookings, and both were caught before members noticed. 🚀

👉 Setting up staging for a Lovable app? Here's the practical setup and the 15-minute release routine: https://launchstudio.eu/en/blog/how-do-i-set-up-a-staging-environment-for-a-lovable-app

#Lovable #Staging #Supabase #DevOps #LaunchStudio #Manifera
