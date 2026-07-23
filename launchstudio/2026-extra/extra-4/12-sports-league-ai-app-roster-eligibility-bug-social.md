🚨 A team manager built his matchday roster, unaware a player was serving a one-game ban. The app clearly showed a red "suspended" badge on that player's profile — but the roster-builder screen never checked it. He played the full match. The opposing club filed a protest and the league overturned a result the team had won on the pitch. 😳

A badge is a display feature. Blocking the action is a business-logic feature. Shipping one without the other is easy to miss — because the demo never builds a roster with an ineligible player. 🧠

❌ Cursor generated a suspension badge on the profile page, but the roster-builder pulled from the full player list without cross-referencing it
❌ Eligibility isn't one rule — suspensions, transfer windows, and age-group limits all interact, and none of them were enforced at submission
❌ The gap is invisible until a real season with real disciplinary history tests it — which is exactly what happened
❌ Once a suspended player is confirmed to have played, most leagues apply an automatic forfeit, no matter what happened on the pitch

✅ A live eligibility check at the moment of roster submission, not just at profile display time
✅ Validation against suspension dates, transfer status, and age-group rules for the specific competition and matchday
✅ Block the submission outright with a specific reason, so the manager isn't left guessing

At **LaunchStudio**, we review the actual data flow between your database and your user-facing actions — not just the interface — specifically to catch "display is right, enforcement isn't" gaps like this. Backed by Manifera's 120+ engineers across 160+ delivered projects. 🛡️

Kaylee's result: CompetitieBeheer now blocks ineligible players at the point of roster submission across every pilot league, and no club has faced a forfeit due to eligibility oversight since the fix shipped. 🚀

👉 Building league or roster software? Talk to an engineer who understands AI-generated code before your league finds the gap for you: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #SportsTech #BuiltWithCursor
