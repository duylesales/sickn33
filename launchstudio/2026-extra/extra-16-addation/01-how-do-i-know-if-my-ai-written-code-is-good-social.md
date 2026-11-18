🧪 She couldn't read the code. So she tested what it did.

Nadia Visser built Huisartsplanner with Lovable and Supabase: a scheduling tool for GP assistants to manage call-back lists and appointment slots. A seed investor was interested and planned a technical review. Before they looked, Nadia ran her own tests.

TEST: The two-account test
❌ An assistant at one practice opened another practice's call-back list by changing an ID in the URL.

TEST: The error test
❌ Saving a slot without a connection showed "saved." Nothing was stored.

TEST: A look around GitHub
❌ No README, no tests, two date libraries, a 2,800-line component file, and a Supabase service role key in an early commit.

TEST: Ask the AI to explain its own access control
❌ Lovable described policies that didn't exist on several tables.

What LaunchStudio did next (9 business days, €3,300):
✓ A structured review confirming and expanding the findings
✓ Row Level Security per practice on all tables, with negative authorisation tests
✓ Honest error handling, with retries for unsaved changes
✓ The exposed key rotated and removed from history
✓ One date library, the large component split, and a README for setup, testing and deployment
✓ CI checks for types, tests, secrets and dependencies
✓ Project instructions with the architecture and security rules for future Lovable sessions

Three weeks later, the investor's technical adviser reviewed the repository. The report listed only minor findings, and the round closed. Nadia now reruns her six behaviour tests before every major release.

"I couldn't read the code, but I could test what it did. That told me enough to know I needed help before anyone else found the problems." - Nadia Visser

👉 Six tests any founder can run on their AI-written code: https://launchstudio.eu/en/blog/how-do-i-know-if-my-ai-written-code-is-good

#AICode #Lovable #Supabase #CodeQuality #AIFounder #LaunchStudio #Manifera
