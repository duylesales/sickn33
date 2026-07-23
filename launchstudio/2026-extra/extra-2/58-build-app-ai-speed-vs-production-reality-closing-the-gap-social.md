🚨 Months after ending a partnership, a farm partner discovered — purely by chance, checking an old bookmark — that a link they'd "revoked" through the app's interface still displayed their current, live availability and schedule. "Finding out by accident that it had quietly kept working this entire time was a pretty unsettling discovery." 🔗

Build-app-AI speed gets a "share this with a link" feature working in an afternoon. Genuinely missing one detail: what happens after someone decides they don't want that link active anymore. 🧠

❌ Building a "revoke" button that removes a link from your own visible list is the straightforward, directly visible part of the feature
❌ Making that action actually invalidate the link server-side is a separate, additional step that doesn't automatically come bundled
❌ Clicking "revoke" and confirming the link disappears from your list looks completely successful — because it IS, from the interface's perspective
❌ A link shared temporarily with a business partner carries a reasonable expectation that access ends when the relationship does

✅ Ensure a revoke action actually invalidates the underlying link server-side
✅ Test by confirming a previously valid link genuinely stops granting access immediately after revocation, not merely disappearing from a list view
✅ This applies to any feature offering shareable links with a revocation option — documents, calendars, dashboards

At **LaunchStudio**, we test exactly this scenario as part of our access-control review. Backed by Manifera's 11+ years with secure sharing and access-revocation systems. 🛡️

Her result: genuine server-side link invalidation implemented, confirmed to stop working immediately upon revocation — across every partner's shared links. 🚀

👉 Talk to an engineer who understands AI-generated code: [Link to article]

#IndieHacker #LaunchStudio #Manifera #AISecure #SoftwareEngineering
