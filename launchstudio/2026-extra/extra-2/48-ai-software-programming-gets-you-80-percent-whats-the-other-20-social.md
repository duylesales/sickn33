🚨 A coach noticed a client's shared, supposedly view-only career plan had been modified. The client insisted they'd only ever clicked around without realizing edits were even possible. Turned out the "view-only" restriction existed only in which buttons the interface showed — not in what the server actually allowed. 📝

"Cursor got you 80% of the way there" is a genuinely accurate observation. The remaining 20% concentrates in a specific, checkable list of permission edge cases. 🧠

❌ A "view-only" recipient's edit requests can still be processed and saved by the backend regardless of permission level — the interface hiding controls provides no real protection
❌ Some permission systems check access level only once, at page load, without re-verifying before processing the actual save request
❌ Inviting a real second account and confirming the interface hides edit controls looks completely correct — because it IS correct from the interface's view
❌ Coaching-adjacent shared documents often contain genuinely personal content — unauthorized modification is a real breach of trust, not just a technical inconvenience

✅ Re-verify permission level on every modifying request server-side, independent of what the interface displays
✅ Apply consistently across every shared or collaborative feature in the product
✅ This generalizes to any feature with multiple permission levels sharing access to the same resource — calendars, project boards, comments

At **LaunchStudio**, we test exactly this pattern as part of our access-control review. Backed by Manifera's 11+ years building permission systems for collaborative software. 🛡️

His result: server-side permission verification added to every document-update request — sharing configuration for coaches unchanged. 🚀

👉 Walk us through what you built — we'll respond within a business day: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #AISecure #VibeCoding
