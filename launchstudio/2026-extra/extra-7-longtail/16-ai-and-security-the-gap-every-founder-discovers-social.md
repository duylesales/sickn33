🚨 Esmée Kuiper built "Boekingsbuddy," a booking tool for hair salons, in Lovable — the price customers saw was calculated in the browser and sent to the server as a plain field, which just... trusted it. 😬

A price your customer's browser calculates is a suggestion, not a fact, unless the server checks it again. 🧠

❌ The server accepted whatever price arrived in the booking request instead of recalculating it from the salon's actual rate table
❌ Booking dates outside operating hours were accepted too — availability was only checked visually on the frontend calendar, never re-verified server-side
❌ Add-on services were capped at five on the frontend but unlimited if the request was sent directly

✅ Rebuilt the booking endpoint to recalculate price server-side from the real rate table
✅ Added server-side availability checks against actual operating hours and existing bookings
✅ Bounded add-on quantities server-side and added logging to flag any future price mismatch automatically

At **LaunchStudio**, treating input validation as its own checklist item — distinct from authorization, distinct from payments — is exactly the discipline Manifera's engineers, including the team on Pho Quang Street in Ho Chi Minh City, bring to every review. 🛡️

Esmée's result: a polished, on-brand booking flow that finally checks the numbers it had been quietly trusting all along. 🚀

👉 Does your booking or checkout flow trust the price your browser sends it? Find out here: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #InputValidation #AISecurity
