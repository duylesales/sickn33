🚨 Ilse Vermeer built Groothandelportaal with Cursor and Supabase: restaurants and shops order from food wholesalers online. Wholesalers wanted orders pushed to their warehouse systems, so Cursor added a database trigger that called each wholesaler's URL directly. 😳

When one warehouse system was slow, ordering slowed. When it was down, orders failed. And the URL field accepted internal addresses - an SSRF risk into private networks. Here's how to build outgoing webhooks for your SaaS customers: 🧠

❌ Order placement blocked by customers' slow systems
❌ No signatures and no retries, so orders went missing in warehouses
❌ Payloads including internal margin fields
❌ URLs that could reach internal networks

✅ An events table written in the same transaction, delivered by a queue worker
✅ Short timeouts and exponential backoff over 24 hours
✅ HMAC-SHA256 signatures compatible with Standard Webhooks
✅ HTTPS-only URLs checked against private ranges, customer-facing payloads, and logs with replay

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we treat webhooks as the small product they really are. 🛠️

Her result: €5,100, 13 business days. Ordering became independent of wholesalers' systems, no events have been lost since, and the SSRF risk was closed before it was ever exploited. 🚀

👉 Adding webhooks to your SaaS? Here's how to make them reliable and safe: https://launchstudio.eu/en/blog/outgoing-webhooks-for-your-saas-customers

#Webhooks #APIs #B2BSaaS #AppSecurity #AIFounder #LaunchStudio #Manifera
