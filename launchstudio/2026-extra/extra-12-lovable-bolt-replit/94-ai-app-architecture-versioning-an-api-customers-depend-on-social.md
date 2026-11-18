🀄 One domino tips, and the rest follow

An AI assistant renames pickup_date to pickup_at and weight to weight_kg, everywhere, database included. The new names are clearer.
➜ The frontend still works.
➜ Shippers' systems, calling the database's REST endpoints directly, start failing.
➜ They log the errors. Nobody watches those logs.
➜ For two days, around 1,100 transport orders that should have been planned are never created.
➜ Trucks don't arrive.
➜ Shippers phone the hauliers to ask why.
➜ The review finds the last domino: every shipper had been given the service role key, with full read and write access to every haulier's data.

Ruud Schipper built Transportplanner in Lovable: transport order management for 26 regional haulage companies. Several of their biggest shippers send orders automatically from their own systems. There was no API layer between them. 🚛

Putting a wall between the dominoes (LaunchStudio, 5 business days, €6,200):
✓ The service role key rotated at once, and every shipper given a scoped, hashed API key belonging to its haulier's organisation
✓ A dedicated /v1 API as edge functions, with an OpenAPI specification, generated docs, envelopes, cursor pagination, UTC timestamps and stable error codes
✓ Idempotency keys on order creation, so retries can't duplicate orders
✓ The old field names accepted for six months, with Deprecation and Sunset headers and a migration guide
✓ Usage logged per key, so any shipper still on old fields can be contacted directly
✓ Specification diffing and contract tests in CI that fail on any breaking change
✓ Signed, versioned webhooks for order status, with a delivery log
✓ A changelog

The 1,100 orders were recreated from the shippers' logs within a day, and no cross-haulier data access was found. Over the next year the API went through fourteen releases without a breaking incident; CI blocked three pull requests that would have broken it. Two large shippers integrated from the docs in about a week each, without calling Ruud.

"The assistant renamed two columns because the new names were clearer. They were - and nine shippers' systems stopped creating orders, and nobody noticed for two days." - Ruud Schipper

https://launchstudio.eu/en/blog/ai-app-architecture-versioning-an-api-customers-depend-on

#API #SoftwareArchitecture #SaaS #Supabase #LaunchStudio #Manifera
