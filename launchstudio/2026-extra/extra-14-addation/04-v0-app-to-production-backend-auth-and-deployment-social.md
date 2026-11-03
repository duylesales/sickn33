🚨 Jelle Terpstra organises small concerts in Nijmegen and built Zaalvol in v0: ticket sales, door check-ins and payouts for venues under 300 seats. Venue owners wanted to start immediately. Then you looked closer: every number in the dashboard came from placeholder arrays. 😳

v0 makes interfaces look real. What it leaves open is everything underneath. Here's what Zaalvol was missing: 🧠

❌ No real schema - sold tickets never reached the guest list
❌ A hand-made Stripe Payment Link with no connection back to the app
❌ Mapbox and Stripe secret keys inside client components
❌ Door scanning that froze the queue on weak venue wifi

✅ A Supabase schema in Frankfurt for venues, shows, ticket types and orders
✅ Supabase Auth with venue-owner and door-staff roles
✅ Stripe Checkout with a signed webhook that creates tickets on payment
✅ Secrets moved to server actions and offline-tolerant scanning with background sync

At **LaunchStudio**, powered by Manifera's 11+ years of web engineering, we keep every v0 component and build the app underneath it. 🧩

His result: €5,900, fifteen business days. Zaalvol sold ~2,300 tickets across 41 shows in its first two months, with door check-ins under two seconds per scan. 🚀

👉 What your v0 UI still needs before real customers arrive: https://launchstudio.eu/en/blog/v0-app-to-production-backend-auth-and-deployment

#v0 #Vercel #NextJS #Ticketing #LaunchStudio #Manifera
