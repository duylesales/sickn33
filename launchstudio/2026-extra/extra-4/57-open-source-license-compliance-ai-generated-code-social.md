🚨 Cursor suggested a routing optimization function, Vince Aarts accepted it because it worked, and moved on. What he didn't know: it closely mirrored code under a copyleft license — and it only became a problem the moment he started informal acquisition conversations. ⚖️

🧠 AI coding tools suggest code without attaching a license to it. Most of the time that's harmless. Sometimes it's a due diligence landmine sitting quietly in a "proprietary" codebase.

❌ Nothing in Cursor's interface indicated the suggestion's provenance, let alone what license governed it
❌ The product worked fine, users noticed nothing — the problem only surfaces when an acquirer's legal team runs a license scan
❌ A flagged copyleft dependency at that stage isn't a quick fix — it can stall or kill a deal while code gets rewritten under time pressure, lawyers watching
❌ `npm audit` catches declared dependencies but misses copied or closely-mirrored code that never went through a package manager at all

✅ Scan the actual codebase for patterns matching known open-source projects, not just package.json
✅ Check every dependency's license, including transitive ones several layers deep
✅ For genuine copyleft conflicts, write a clean-room replacement built from the underlying logic, not the flagged code

At **LaunchStudio**, license compliance reviews are a standard part of preparing a codebase for funding or acquisition, backed by Manifera's 160+ delivered projects for clients like Vodafone and TNO. 🛡️

His result: RouteBoard's codebase passed a subsequent informal license review with no flags — clean footing for any future acquisition conversation. 🚀

👉 Planning to raise or sell? Check your codebase's license posture first: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #IndieHacker #DueDiligence
