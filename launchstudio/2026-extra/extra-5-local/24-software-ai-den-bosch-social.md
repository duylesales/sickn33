BEFORE ➜ AFTER: CivicDesk, Den Bosch 🏛️

Thijs Verhoeven is a developer. He built CivicDesk, a citizen-request tracking tool for small municipalities, with v0 in about three weeks, and he could read every line of the generated backend. What he hadn't stress-tested: two staff members updating the same request at the same moment.

During a pilot with a small Noord-Brabant gemeente, exactly that happened.

BEFORE: Two people edit one citizen request at once, and nothing notices.
AFTER: Optimistic locking catches the conflict.

BEFORE: One staff member's status update silently overwrites the other's.
AFTER: Database-level constraints that v0's generated schema had left out.

BEFORE: No record of which change was lost.
AFTER: An audit log of every field change, with timestamp and user ID.

BEFORE: Unexplained data loss, which disqualifies government-adjacent software.
AFTER: CivicDesk passed its next municipal procurement review, with the audit trail named as meeting the record-keeping requirement.

Time: 7 business days. Cost: €1,600.

"I could read the code v0 gave me. What I couldn't see was what it hadn't accounted for. That's a different skill, and LaunchStudio had it." - Thijs Verhoeven

Building software for a gemeente with AI? Plan for two people clicking Save at once: https://launchstudio.eu/en/blog/24-software-ai-den-bosch

#AINativeFounder #LaunchStudio #Manifera #SoftwareArchitecture #DenBosch
