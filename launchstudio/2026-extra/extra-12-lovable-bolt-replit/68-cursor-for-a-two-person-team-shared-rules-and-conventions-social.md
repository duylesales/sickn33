👥 One repository. Two products in it.

                     FOUNDER A's HALF        FOUNDER B's HALF
Area                 declarations and        practice admin and
                     insurer integration     reporting
Date library         one                     a different one
Forms                one approach            another approach
Validation           one library             a second library
Errors               thrown                  returned as values
Table names          plural                  singular
Can the other
founder work here?   no                      no

Steven Doornekamp and his co-founder built Zorgdeclaratie together in Cursor: declaration handling between allied health practices and insurers, used by 52 practices. They split the work and ran in parallel for four months, with no rules file and no review. A week of illness stopped half the product. 🏥

What forced the issue: a declaration period calculated with one date library in one half and the other library in the other half. At the end of December, the two disagreed about week numbers. 60 declarations went out with the wrong period, and two insurers rejected them.

One product again (LaunchStudio, 3 business days, €3,100):
✓ A rules file written together in an afternoon, from the code: one library per job (dates, forms, validation, errors), naming conventions, patterns, and five rules never to break
✓ The losing libraries removed and converted in shared areas, with the rest marked as exceptions to converge over time
✓ Date handling unified, and the week-number bug fixed with a test written from the insurer specification
✓ Pull requests with a five-minute diff review by the other founder
✓ One vocabulary (declaration, practice, insurer, period), replacing three sets of synonyms

The 60 declarations were resubmitted. The bigger change, in Steven's view: both of them now work in either half. He found that out when his co-founder was away for two weeks and the product kept moving.

"We had one repository and two products in it. Neither of us could work in the other's half, and a date library disagreement at the end of December got sixty declarations rejected." - Steven Doornekamp

https://launchstudio.eu/en/blog/cursor-for-a-two-person-team-shared-rules-and-conventions

#Cursor #SmallTeams #CodeReview #AICoding #LaunchStudio #Manifera
