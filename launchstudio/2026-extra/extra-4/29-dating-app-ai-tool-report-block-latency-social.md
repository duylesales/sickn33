🚨 A user reported being harassed by a match on MatchLokaal, blocked him immediately — and then told Lotte Andriessen his profile was still showing up in her search results minutes later, with his old messages still sitting visible in her inbox. She had no way to know from her side whether the block had actually worked. 😳

A user who taps "block" believes it's instant and total. In a lot of AI-built apps, that's not what actually happens. 🧠

❌ The block action only updated the messaging permission table synchronously — search indexing and message visibility ran on a delayed background job
❌ Blocking a user isn't one action, it's several: messaging, search visibility, profile access, and message history, each its own piece of logic
❌ An AI tool implements whichever piece the prompt emphasized most — usually "stop them messaging me" — and leaves the rest to catch up later
❌ The exploit window matters most for the person most likely watching it closely: someone who's just been reported and knows it

✅ Treat a block as a single synchronous operation updating every surface before confirming success to the user
✅ Audit every read path that could still surface a blocked user — search, recommendations, shared groups, activity feeds
✅ Add an internal test suite verifying all safety actions apply synchronously before any new feature can ship

At **LaunchStudio**, we treat trust and safety features like block, report, and mute with the same rigor as payment or authentication code — because getting them wrong has real consequences for real people. Backed by Manifera's enterprise access-control work for clients like Vodafone and TNO. 🛡️

Lotte's result: MatchLokaal's block action is now fully instant and complete across every part of the app, with regression tests to keep it that way. 🚀

👉 Running a dating, community, or social app with block/report features? Get a free safety-surface audit: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #TrustAndSafety #DatingApp
