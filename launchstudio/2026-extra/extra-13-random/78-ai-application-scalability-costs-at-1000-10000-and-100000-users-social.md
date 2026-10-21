🚨 Mees van Rijn, a former office manager in Amsterdam, built Lunchlijst on Replit: companies let employees order lunch from local caterers, with one monthly invoice per company. In a year it grew from 1,200 to about 14,000 users across 90 companies. Revenue grew roughly tenfold. Infrastructure costs grew about twenty-five-fold — to €2,300 a month. 😳

The cost review traced it to five habits: the menu page polled every five seconds for every open tab; caterer photos were served at full camera resolution; an AI "lunch suggestion" called a language model on every page load; the order-history query had no index and forced a bigger database tier; and logs captured every request body, menus included. Here's what AI application scalability really costs at 1,000, 10,000 and 100,000 users: 🧠

❌ Polling from every open tab
❌ Full-resolution images on every page
❌ An LLM call on every page load
❌ Missing indexes and bloated logs

✅ Polling replaced by filtered real-time updates
✅ Images resized and cached through a CDN
✅ AI suggestions on demand, cached daily per company
✅ Indexes and pagination, trimmed logging, monthly invoicing in background jobs — and a cost-per-active-user dashboard

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make sure each new customer makes you more profitable, not less. ⚙️

His result: €3,600 over twelve business days, plus €49/month. Monthly infrastructure fell to about €520 while users kept growing, cost per active user dropped ~80%, and Lunchlijst passed 20,000 users with infrastructure under 5% of revenue. 🚀

👉 AI application scalability costs at 1,000, 10,000 and 100,000 users: https://launchstudio.eu/en/blog/ai-application-scalability-costs-at-1000-10000-and-100000-users

#Scalability #CloudCosts #Replit #SaaS #LaunchStudio #Manifera
