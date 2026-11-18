1,200 ➜ 14,000 users in a year.
~10× revenue.
~25× infrastructure costs.
€2,300 a month.
5 habits in the code.
€520 a month after fixing them. 🥪

Mees van Rijn, a former office manager in Amsterdam, built Lunchlijst on Replit: companies let employees order lunch from local caterers, with one invoice per company per month. 90 companies, about 14,000 users. Every new company made the business a little less profitable, and Mees thought that was just what scaling felt like.

The five habits, found in LaunchStudio's cost review:
1 menu page polling for updates every five seconds, in every open tab
1 photo library of caterers' pictures, served at full camera resolution
1 AI "lunch suggestion," calling a language model on every page load
1 order history query with no index, forcing a much bigger database tier
1 logging setup capturing every request body, menus included, into the monitoring service

The fixes (Launch & Grow, 12 business days, €3,600, plus €49/month):
✓ Polling replaced by filtered real-time updates
✓ Images resized and cached via a CDN
✓ AI suggestions on demand, with daily caching per company
✓ Indexes and pagination
✓ Logging trimmed to what's actually needed
✓ Monthly invoicing moved to background jobs
✓ A dashboard showing cost per active user

The new numbers:
€520 a month, while users kept growing
~80% lower cost per active user
20,000+ users, with infrastructure well under 5% of revenue

"Every new company made us a little less profitable, and I thought that was just what scaling felt like. It was five fixable habits in the code." - Mees van Rijn

https://launchstudio.eu/en/blog/ai-application-scalability-costs-at-1000-10000-and-100000-users

#Scalability #CloudCosts #Replit #SaaS #LaunchStudio #Manifera
