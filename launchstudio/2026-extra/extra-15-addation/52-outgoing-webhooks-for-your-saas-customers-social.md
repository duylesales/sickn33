Unpopular opinion: "add webhooks" is never a one-line task. 🔗

Ilse Vermeer built Groothandelportaal with Cursor and Supabase: a B2B ordering platform where restaurants and shops order from food wholesalers. Wholesalers wanted orders sent automatically to their warehouse and accounting systems, so Ilse asked Cursor to add webhooks. The agent added a database trigger that called each wholesaler's URL directly whenever an order row changed.

It worked. Then it didn't:
• A slow warehouse system slowed order placement for that wholesaler's customers
• A warehouse system that was down made orders fail
• No signatures, so wholesalers couldn't verify where a webhook came from
• No retries, so events sent during outages vanished, and orders went missing in warehouses
• Payloads with full order rows, internal margin fields included
• A URL field that accepted any address, including internal ones, so the platform's own servers could be made to send requests into private networks (SSRF)

What it actually took (LaunchStudio, 13 business days, €5,100):
→ An events table written in the same transaction as each order change
→ A queue worker with short timeouts and exponential backoff over 24 hours
→ HMAC-SHA256 signatures with per-endpoint secrets, compatible with the Standard Webhooks spec
→ HTTPS required, URLs checked against private and metadata ranges at registration and at delivery, redirects off, worker isolated
→ Payloads with customer-facing order fields only
→ A settings screen with event selection, secret rotation, delivery logs and replay

Since then: order placement no longer depends on wholesalers' systems, no events have been lost, two wholesalers integrated within a week, and the SSRF risk was closed before anyone used it.

Quick self-test for your app: register a webhook URL pointing to localhost. If your app accepts it, you have the same open door.

"I thought webhooks were a single line of code. They turned out to be a small product of their own, with security risks I'd never have spotted." - Ilse Vermeer

https://launchstudio.eu/en/blog/outgoing-webhooks-for-your-saas-customers

#Webhooks #APIs #B2BSaaS #AppSecurity #AIFounder #LaunchStudio #Manifera
