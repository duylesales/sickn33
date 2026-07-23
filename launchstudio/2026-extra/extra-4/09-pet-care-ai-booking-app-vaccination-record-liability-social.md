🚨 A dog with an expired vaccination record got booked into a group daycare session alongside a dozen other dogs — through Fenne Wouters' own app, DierenAgenda. The certificate had expired in the weeks between signup and this booking. Nothing flagged it, because the eligibility check had only ever run once, at initial approval. 😳

An app that checks vaccination status once at signup looks fully compliant in a demo — upload, approve, book — while having zero mechanism to catch a certificate that expires between visit one and visit twelve. 🧠

❌ Cursor built exactly what was asked: a field to upload a vaccination document at onboarding, plus an approval checkbox — nothing that re-checks it later
❌ The expiry date never got compared against the calendar on any subsequent booking
❌ Kennel cough and parvovirus spread fast in shared spaces, and daycare operators carry real liability for letting an unvaccinated animal into a group setting
❌ The app implied "this dog is cleared," forever, from a single moment in time — which simply wasn't true

✅ Move the vaccination-expiry check from a one-time signup gate to a validation that runs against the booking date on every new booking
✅ Add an expiry-aware status indicator to the operator's dashboard so staff see certificate status at a glance
✅ Send automated owner reminders 14 days before a certificate's expiry, so re-uploads happen before they become a blocker

At **LaunchStudio**, this is exactly the kind of silent logic gap Manifera's 120+ engineers look for — not just "does it crash," but "does the app's behavior actually match what the business needs to be true." 🛡️

Her result: every new booking is now validated against current, non-expired vaccination records, giving daycare operators a real-time compliance view instead of a static signup-day snapshot. 🚀

👉 Not sure if your booking app re-checks time-sensitive credentials? Walk through a technical review first: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #PetTech #AILiability
