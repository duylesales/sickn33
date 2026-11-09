🔍 Nadia Visser built Huisartsplanner in Lovable: a scheduling tool for GP assistants to manage call-back lists and appointment slots. A seed investor was interested and planned a technical review. Nadia couldn't read code, so she tested what it did. 🧪

The very first test failed: an assistant at one practice could open another practice's call-back list just by changing an ID in the URL. 😳 Here's what her behaviour tests and a quick look at GitHub revealed: 🧠

❌ No access control between practices on several tables
❌ "Saved!" messages while nothing was stored offline
❌ A Supabase service role key in an early commit
❌ No README, no tests, a 2,800-line component file

✅ Row Level Security per practice, with negative tests
✅ Honest error handling with retries for unsaved changes
✅ Key rotated and removed from git history
✅ README, CI checks and project instructions for future Lovable sessions

At **LaunchStudio**, backed by Manifera's 11+ years of reviewing and maintaining codebases, we check AI-written code for what matters in production: security, correctness and maintainability. 🛠️

Her result: €3,300, nine business days. The investor's technical adviser found only minor issues three weeks later, and the round closed. 🚀

👉 Six tests any founder can run on their AI-written code: https://launchstudio.eu/en/blog/how-do-i-know-if-my-ai-written-code-is-good

#AICode #Lovable #Supabase #CodeQuality #AIFounder #LaunchStudio #Manifera
