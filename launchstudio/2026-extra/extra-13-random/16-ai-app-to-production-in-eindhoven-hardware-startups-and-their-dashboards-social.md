📋 SPEC SHEET: SensaGrow

HARDWARE (a year of careful engineering)
✓ Wireless sensors for temperature, humidity and CO₂ in commercial greenhouses
✓ Built by Pieter Hofstede, an electrical engineer who left a large Eindhoven tech company

DASHBOARD (about three weeks in Cursor, with Next.js and Supabase)
✗ Every sensor using the same API key, compiled into firmware
✗ An ingestion endpoint accepting any device_id in a request
✗ One row per request in a single table of 40 million rows, so growers' weekly charts took up to twenty seconds
✗ Growers able to see each other's greenhouse data through the API
✗ A ventilation-override command with no role check and no audit log

Five growers in the Westland were piloting 340 sensors. A larger cooperative wanted 2,000. Its IT consultant asked for a security overview, and Pieter asked LaunchStudio for a review before answering.

From the customer's point of view, the dashboard was the product.

DASHBOARD, REVISED (Launch & Grow, 15 business days, €4,200, plus €49/month)
✓ Per-device tokens issued at provisioning, with a revocation list, rolled out in the next firmware update and the shared key retired after a transition window
✓ Ingestion rebuilt around a queue, with batched, idempotent writes
✓ Readings moved to TimescaleDB, with hourly and daily rollups
✓ Tenant separation enforced with Row Level Security
✓ Ventilation overrides limited to grower-admin roles, with confirmation, value limits and an audit trail

THE RESULT
SensaGrow passed the cooperative's security review and started a 2,000-sensor rollout. Weekly charts load in under a second, and ingestion has handled peaks above 60 readings per second without dropped data.

"I'd spent a year making the sensor trustworthy and three weeks on the thing that decided who could read it. The dashboard was the product, from the customer's point of view." - Pieter Hofstede

https://launchstudio.eu/en/blog/ai-app-to-production-in-eindhoven-hardware-startups-and-their-dashboards

#IoT #Eindhoven #Brainport #AppSecurity #LaunchStudio #Manifera
