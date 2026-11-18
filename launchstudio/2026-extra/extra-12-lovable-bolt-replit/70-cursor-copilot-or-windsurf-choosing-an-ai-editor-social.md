🛠️ Three months, four AI editors, plenty of comparison articles. The product didn't noticeably improve.

Here's what got blamed on the tools, and what was actually going on.

BLAMED: "The tool loses my work."
ACTUALLY: No repository for the first two months. Work was lost twice.

BLAMED: "Every tool writes inconsistent code."
ACTUALLY: No conventions file, so each tool picked its own style, which made the tools look inconsistent.

BLAMED: "It keeps changing things I didn't ask for."
ACTUALLY: Changes accepted without reading the diff, so unrequested edits piled up.

BLAMED: "The output is too big to control."
ACTUALLY: Broad requests like "improve the scheduling logic", then several turns correcting large changes.

BLAMED: "I can't trust what it produces."
ACTUALLY: No tests, so there was no way to tell whether an accepted change had broken something.

Emiel Vrieze built Keuringsplanner in Cursor: inspection scheduling for lift and installation inspection companies, 22 companies, around 14,000 assets. Each time something frustrated him, he switched, reasoning a better tool would produce better results. ⚙️

Fixing the actual causes (LaunchStudio, 2 business days, €2,200):
✓ A repository with history and a branch per change
✓ A conventions file written from the existing code: patterns, naming, chosen libraries, four inviolable rules, the product's vocabulary
✓ 34 tests covering authorisation across 19 endpoints, the inspection interval calculations and one end-to-end flow
✓ A practice: commit before each session, read diffs, one request at a time
✓ A decision to stay on one tool for three months before reconsidering

He stayed with the editor he happened to be using. Over the next quarter he shipped four features he couldn't finish during the three months of switching. By his account, the conventions file changed the output more than any change of tool.

"I switched four times looking for a tool that would produce consistent code. The inconsistency was mine - I had never written down what consistent meant." - Emiel Vrieze

https://launchstudio.eu/en/blog/cursor-copilot-or-windsurf-choosing-an-ai-editor

#Cursor #GitHubCopilot #Windsurf #AICoding #LaunchStudio #Manifera
