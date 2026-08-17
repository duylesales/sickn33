🚨 Lukas Reindl's Vienna agency almost took a client's "PatientPing" physiotherapy scheduling app live under their own name — until a pre-launch review found the scheduling API was handing full patient records, including phone numbers and therapist notes, to any authenticated user, not just the assigned therapist. 😳

A basic functional test found nothing wrong. It took a real security review to find the actual risk. 🧠

❌ The scheduling API returned complete patient records to any authenticated user, not just the therapist assigned to that patient
❌ No rate limiting on the appointment-booking endpoint, leaving it open to being spammed with fake bookings
❌ A leftover internal debugging endpoint from Bolt's build process was still reachable in production and dumped the raw appointments table on request

✅ Added role-based authorization so therapists can only query their own assigned patients
✅ Stripped internal notes out of every API response reaching the frontend
✅ Added rate limiting to the booking flow and closed the exposed debugging endpoint

At **LaunchStudio**, white-label security reviews for agencies inheriting AI-built client work are standard practice — Manifera's engineers, trusted by organizations like Vodafone, TNO, and CFLW, coordinate delivery through the Singapore team on Tras Street. 🛡️

Lukas's result: the fix shipped under his agency's own branding — his client never knew a specialist partner had been involved. 🚀

👉 Taking on client AI prototypes under your own agency's name? Know this checklist first: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #WhiteLabel #AppSecurity
