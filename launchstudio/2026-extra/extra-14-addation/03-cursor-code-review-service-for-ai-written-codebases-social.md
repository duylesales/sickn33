Imagine a warehouse with two kinds of doors. 🚪

The new doors check your badge before they open. The old doors don't check anything. They just have a sign that says "staff only," and they rely on you not reading it.

That was Stocklane.

Valentina Rossi, an Italian supply chain analyst living in Breda, spent four months building Stocklane with Cursor: stock management for small wholesalers, with purchase orders, multi-warehouse inventory and supplier portals. She's a capable developer, and she'd written tests for most features. Three wholesalers were piloting it.

Before signing the first annual contract, the client's IT manager asked for proof of a security review. Valentina didn't have one. LaunchStudio's review found:
• Newer routes checked on the server that a warehouse belonged to the user's company
• Six older routes, generated early on, just relied on the frontend hiding buttons. Any logged-in user could call them with another company's warehouse ID.
• A supplier portal token that never expired
• A catch block that marked failed purchase order emails as "sent"
• And two tests that asserted the insecure behaviour of the old routes, so the tests passed

Valentina fixed the medium and low items herself, with Cursor and the review's guidance. LaunchStudio fixed the rest (13 business days, €3,400, for a review of roughly 28,000 lines plus critical fixes):
✓ One server-side authorisation helper on every door, old and new
✓ Expiry on supplier tokens
✓ Honest email error handling
✓ The misleading tests rewritten
✓ A summary and fix confirmation for the IT manager

The annual contract was signed three weeks after the review began. And Valentina's CI pipeline now fails any new route that skips the helper.

"I trusted my code because I'd tested it. The review showed me I'd tested what I expected, not what an attacker would try." - Valentina Rossi

https://launchstudio.eu/en/blog/cursor-code-review-service-for-ai-written-codebases

#Cursor #CodeReview #AppSec #SaaS #LaunchStudio #Manifera
