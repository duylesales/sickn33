🚨 Ruud Schipper's Transportplanner manages transport orders for 26 regional hauliers, and their biggest shippers send orders automatically from their own systems. There was no real API - shippers called the Supabase REST endpoints directly, each with the service role key. Then an AI assistant renamed two columns during a refactor. 😳

Nine shippers' systems stopped creating orders. For two days, around 1,100 transport orders silently never arrived - and the service keys turned out to give every shipper full access to every haulier's data. Here's how to version an API your customers depend on: 🧠

❌ The database schema exposed as the "API", so a column rename broke customers
❌ The service role key handed to integrators
❌ No specification, no breaking-change check, no usage logs
❌ No idempotency, no deprecation policy, no changelog

✅ Service key rotated immediately; scoped, hashed API keys per organisation
✅ A dedicated /v1 API with an OpenAPI spec, envelopes, cursor pagination, UTC timestamps, stable error codes and idempotency keys
✅ A six-month compatibility layer for old field names, with Deprecation and Sunset headers and a migration guide
✅ Spec diffing and contract tests in CI that fail on breaking changes, plus signed, versioned webhooks and per-key usage logs

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build the API layer before your first integration customer starts depending on it. ⚙️

His result: €6,200, five business days. The orders were recreated within a day. Since then: fourteen API releases with zero breaking incidents, three risky pull requests blocked by CI, and two large shippers integrated in a week each without a single call. 🚀

👉 AI app architecture: versioning an API customers depend on: https://launchstudio.eu/en/blog/ai-app-architecture-versioning-an-api-customers-depend-on

#API #SoftwareArchitecture #SaaS #Supabase #LaunchStudio #Manifera
