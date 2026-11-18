🎬 Walk onto a film set and the street looks real. Shopfronts, signs, lit windows. Open a door and there's nothing behind it but scaffolding.

Jelle Terpstra's ticketing dashboard was a beautiful film set.

He organises small concerts in Nijmegen and built Zaalvol in v0: ticketing and guest lists for venues with under 300 seats, with sales per show, check-ins at the door and a payout overview. Venue owners he showed it to wanted to start right away.

Behind the doors:
🎭 Every number in the dashboard came from placeholder arrays
🎭 The checkout button opened a Stripe payment link Jelle had made by hand, with no connection back to the app, so sold tickets never reached the guest list
🎭 A Mapbox key and a Stripe secret key sat in client components
🎭 Two server actions that changed venue settings had no authorisation check at all
🎭 Door check-in only worked on strong wifi, because every scan waited for a full page reload

Building the real street behind the set (LaunchStudio, 15 business days, €5,900, plus €49/month managed hosting), keeping every v0 component:
🏗️ A schema for venues, shows, ticket types and orders, in Supabase in Frankfurt
🏗️ Supabase Auth with venue-owner and door-staff roles
🏗️ Authentication, validation and authorisation on every server action
🏗️ Stripe Checkout plus a signed webhook that creates tickets on payment
🏗️ All secrets moved server-side
🏗️ Optimistic door scanning with background sync, so a weak connection no longer holds up the queue

Zaalvol launched with three venues fifteen business days after the first call. First two months: about 2,300 tickets across 41 shows, with guests checked in at under two seconds per scan.

"v0 made it look real. LaunchStudio made it actually be real - same screens, completely different app underneath." - Jelle Terpstra

https://launchstudio.eu/en/blog/v0-app-to-production-backend-auth-and-deployment

#v0 #Vercel #NextJS #Ticketing #LaunchStudio #Manifera
