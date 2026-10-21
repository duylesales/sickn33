🚨 Pieter Hofstede left a large Eindhoven tech company to start SensaGrow: wireless sensors measuring temperature, humidity and CO₂ in commercial greenhouses. The hardware was carefully engineered. The customer dashboard was built in Cursor in about three weeks. Five Westland growers piloted 340 sensors — then a cooperative wanted to roll out 2,000. 😳

Its IT consultant asked for a security overview. Every sensor shared one API key compiled into firmware, the ingestion endpoint trusted any device_id, growers could read each other's data through the API, and the ventilation-override command had no role check or audit log. Here's what hardware startups must fix before taking the dashboard to production: 🧠

❌ One shared device key — extract it once, impersonate every sensor
❌ One database row per reading: 40 million rows and 20-second charts
❌ Tenant separation only in the interface
❌ Device commands with no roles, limits or audit trail

✅ Per-device tokens with a revocation list, rolled out via the next firmware update
✅ A queue with batched, idempotent ingestion
✅ TimescaleDB with hourly and daily rollups
✅ Row level security per grower, and ventilation overrides limited to admins with confirmation, value limits and an audit trail

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering — including industrial and energy hardware clients — we engineer the dashboard with the same care as the device. ⚙️

His result: €4,200, fifteen business days. SensaGrow passed the cooperative's security review and began the 2,000-sensor rollout. Charts load in under a second, and ingestion handles 60+ readings per second with no dropped data. 🚀

👉 AI app to production in Eindhoven: hardware startups and their dashboards: https://launchstudio.eu/en/blog/ai-app-to-production-in-eindhoven-hardware-startups-and-their-dashboards

#IoT #Eindhoven #Brainport #AppSecurity #LaunchStudio #Manifera
