🚧 There's an old parable about a fence across a road. A reformer wants it gone because he can't see the point. The wise answer: find out why it was put there first. Then you may take it down.

An AI session doesn't ask why. It sees the fence and tidies it away.

Pieter-Jan Osseweijer built Subsidieaanvraag in Cursor: grant application administration for agricultural advisers and their clients, around 900 applications a year for 26 advisory firms. A session tidying the validation code removed a condition that looked redundant: a check rejecting applications where the parcel area exceeded a threshold relative to the registered holding. No comment, no test, nothing in the code explaining it. 🌾

The reason it existed: a provincial authority had rejected 40 applications the previous year for exactly that mismatch, and the check was added to catch it before submission.

The removal went unnoticed for two months. 31 applications went in with the mismatch and were rejected, several after that round's deadline. For four farms, that meant missing a funding window entirely.

Writing down why the fences are there (LaunchStudio, 3 business days, €2,500):
✓ The check restored, with a comment on what it prevents and a test derived from the authority's published rules
✓ A decisions log, seeded with fourteen entries he could still reconstruct, such as why applications are immutable after submission, why provincial rules are stored as data and not code, and why one provider was chosen for document generation
✓ A README for setup and environments, which had never existed
✓ A conventions file: patterns, naming, four inviolable rules
✓ An operations page: the nightly submission job, backups, restore procedure, provider contacts
✓ Comments on six more pieces of code that looked unnecessary and weren't, each pointing to its decision entry
✓ Generated reference documentation for the endpoints

No checks have been removed since. The decisions log gets read more than expected: twice by an adviser asking why the product behaves a certain way, once by a provincial authority, and repeatedly by Pieter-Jan himself.

"A session removed a check that looked pointless. It was pointless unless you knew that forty applications had been rejected for exactly that reason the year before, and nothing in my product knew that." - Pieter-Jan Osseweijer

https://launchstudio.eu/en/blog/cursor-and-documentation-keeping-a-codebase-explainable

#Documentation #Cursor #AICoding #SoftwareEngineering #LaunchStudio #Manifera
