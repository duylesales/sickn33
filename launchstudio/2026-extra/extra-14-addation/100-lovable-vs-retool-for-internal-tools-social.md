🚨 Ivo Ramaker runs Fietsabonnement, a bike subscription service in Amsterdam with about 2,000 subscribers. For his five-person support team, he built an internal panel in Lovable - fast, using the service role key so the panel could "see everything". Every agent could view and edit any subscriber, export all data and issue refunds, with no record of who did what. 😳

He built the support panel for speed. He hadn't noticed he'd also built the most dangerous screen in his company. Here's what that panel allowed: 🧠

❌ The service role key in the panel, bypassing all access rules
❌ Every agent able to view and edit every subscriber's details and payment status
❌ Unrestricted data exports and refunds
❌ No audit trail of who did what

✅ The service role key removed, with staff roles (agent, senior agent, admin) in a roles table
✅ RLS policies written for staff access
✅ Refunds and exports moved into edge functions limited to senior roles
✅ An audit log of sensitive actions with a review screen, plus MFA for all staff

At **LaunchStudio**, backed by Manifera's 11+ years of enterprise back-office systems, we treat internal tools as high-risk: least privilege, logging and MFA - whether you build in Lovable or Retool. 🛠️

💡 His result: €2,600, seven business days. The team kept a fast, custom panel, Ivo can see who issued every refund and export, and two months later the audit log resolved a customer dispute in minutes. 🚀

👉 Lovable or Retool for your internal tools? Here's how to choose - and keep them safe: https://launchstudio.eu/en/blog/lovable-vs-retool-for-internal-tools

#Lovable #Retool #InternalTools #Supabase #LaunchStudio #Manifera
