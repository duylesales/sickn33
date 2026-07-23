🚨 Two caregivers swapped a shift between themselves inside Otto Jansen's ZorgAgenda. The visit stayed on the calendar exactly as before, just with a different name attached. When the substitute's swap fell through and the visit never actually happened, the family had no reason to check — their last notification had confirmed the visit was scheduled, and nothing since had told them otherwise. 😳

For most software, "if the booking works, the notifications work." In home-care scheduling, the notification isn't a layer on top of the visit — for the family checking their phone, it *is* the visit. 🧠

❌ Bolt built the core booking loop well — assign, confirm, calendar update — because that's exactly what was described
❌ A shift swap only reassigned a caregiver ID on an existing calendar entry — no new event fired, no new notification went out
❌ The app only treated initial booking and cancellation as notification-worthy; reassignment wasn't a recognized trigger
❌ A silent reassignment quietly turned into a visit that never happened, with the family none the wiser

✅ Treat every schedule mutation — not just the initial booking — as an event that can trigger a notification
✅ Add explicit rules for shift swaps, time changes, cancellations, and no-shows, each with their own notification
✅ Add a visit-completion confirmation step so families get a clear signal when a visit actually happens, not just when it's planned

At **LaunchStudio**, this is exactly what our CEO Herre Roelevink means when he says the hard part today isn't the idea — it's the architecture and security that make a product trustworthy at maturity. 🛡️

His result: families now receive a notification for every material change to a scheduled visit, closing the gap between what the calendar shows and what actually happened. 🚀

👉 Building trust-critical scheduling software? See how our review process works: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #ElderCareTech #AITrust
