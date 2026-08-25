🌐 Ines switched DNS herself to move her Bolt-built project management tool onto a custom domain — Google OAuth login broke for all 400 active users within 20 minutes.

"It's just DNS" is the assumption that breaks logins, payments, and email deliverability all at once.

❌ OAuth callback URLs still pointing at the old domain the moment DNS flips
❌ Stripe webhooks updated too early — or too late — silently dropping payment confirmations
❌ SPF/DKIM/DMARC records never configured, so password reset emails quietly bounce

✅ A staged migration with dual-domain support during the full DNS propagation window
✅ Webhook and OAuth cutover only after each is verified working on the new domain
✅ Old domain kept as a redirect, not deactivated, catching every lingering bookmark and link

At **LaunchStudio**, we've been executing exactly this kind of zero-downtime migration since 2014 through Manifera, across 160+ delivered projects. 🛡️

Ines's migration completed with zero login failures, zero missed webhooks, and no customer-visible downtime. (€1,400 — Launch Ready Package, migrated and verified in 5 business days.) 🚀

👉 See how we fixed it: [Link to article]

#LaunchStudio #Manifera #AISaaS #ZeroDowntime #Bolt
