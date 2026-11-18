```
  // request: change how expired key assignments are handled
+ ...the requested expiry change...
- if (canViewKeyList(user, building))
+ if (!canViewKeyList(user, building))
```
(Illustrative diff. The inverted check is real.)

That's the kind of thirty-second read that would have caught it.

Dennis Vermaat built Sleutelbeheer in Cursor: key and access management for property managers and housing associations, tracking who holds which key to which building, for 17 organisations. He asked for one change, to expired key assignments. The code came back clean, well named, and readable. He tested the feature, it worked, and he accepted it without reading the diff carefully. 🔑

The same change had also inverted an unrelated condition in that file: the check on whether a key holder may view a building's key list.

The path he tested, an administrator viewing their own organisation, behaved identically. The path he didn't test let a contractor with limited access see every key holder for every building the organisation managed, private addresses included.

It surfaced seven weeks later in a routine review. No evidence anyone used it, confirmed from logs.

The review, applied backwards and forwards (LaunchStudio, 2 business days, €2,300):
✓ The condition corrected, with a test asserting the permission for both roles
✓ Every change from those seven weeks reviewed, which found two more unrequested modifications: a default retention value changed, and an import removed that had silently disabled a validation
✓ Authorisation tests across the twelve endpoints that expose key data
✓ One change at a time, diff read before accepting
✓ A written checklist covering five failure categories
✓ Each session's work on its own branch, so it can be thrown away

In the year that followed, reading diffs caught four more unrequested modifications, two of which would have been consequential. Dennis says the habit mattered more than the fix.

"I asked it to change how expiry worked. It also inverted a permission check in the same file, and the version I tested behaved identically. The diff would have taken me thirty seconds." - Dennis Vermaat

https://launchstudio.eu/en/blog/cursor-code-review-catching-what-autocomplete-got-wrong

#CodeReview #Cursor #AICoding #AppSecurity #LaunchStudio #Manifera
