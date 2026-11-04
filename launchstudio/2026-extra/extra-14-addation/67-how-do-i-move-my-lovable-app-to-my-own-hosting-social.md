🚨 Saskia Hoogland runs a flower shop in Delft and built Bloemenbus in Lovable for same-day bouquet delivery. On the morning of Valentine's Day, she published a small change to the delivery window picker - and it broke checkout on every iPhone. On the busiest morning of her year, she couldn't undo it. 😳

Fixing it by prompting took two hours during her biggest sales day. That was the last time she published straight to customers. Here's what she was missing: 🧠

❌ Publishing straight from Lovable to her live domain
❌ No one-click rollback to the previous version
❌ No preview environment to test a change first
❌ No staging, so every change went directly to customers

✅ The app moved to Vercel, deploying from her GitHub repository
✅ Staging and production branches, with a preview deployment for every change
✅ Rewrites and environment variables configured, plus Supabase and Mollie URLs updated
✅ The domain switched with no downtime - and Saskia still edits in Lovable

At **LaunchStudio**, backed by Manifera - which deploys on Vercel, Netlify, AWS, Azure and DigitalOcean for clients - we make releases controlled and reversible. 🛠️

💡 Her result: €1,100, three business days. On Mother's Day, the next big peak, a preview deployment caught a layout problem before it went live, with one-click rollback ready if needed. 🚀

👉 Still publishing your Lovable app straight to customers? Here's how to move to your own hosting: https://launchstudio.eu/en/blog/how-do-i-move-my-lovable-app-to-my-own-hosting

#Lovable #Vercel #Hosting #DevOps #LaunchStudio #Manifera
