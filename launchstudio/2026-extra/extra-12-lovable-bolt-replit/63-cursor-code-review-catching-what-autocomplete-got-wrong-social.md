🚨 Dennis Vermaat's Sleutelbeheer tracks who holds which key to which building for 17 property managers and housing associations. He asked Cursor to change how expired key assignments worked. Clean code, it worked when he tested it, accepted. Seven weeks later a routine review found the same change had inverted a permission check - letting limited-access contractors see every key holder, including private addresses. 😳

The version he tested behaved identically. Only the diff would have shown it. Here's how to review code that's plausible rather than obviously broken: 🧠

❌ Reading the finished file instead of the diff - unrequested changes become invisible
❌ Testing only the path you changed (an admin viewing their own organisation)
❌ Asking an assistant to "review this" - it finds what's wrong, not what's missing
❌ No tests on authorisation, so a flipped permission check passes silently

✅ The condition corrected, with a test asserting the permission for both roles
✅ Seven weeks of changes reviewed - two more unrequested modifications found
✅ Authorisation tests across the twelve endpoints that expose key data
✅ One change at a time, diff read before accepting, each session on a discardable branch

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we act as the second reader on the changes that matter: money, permissions, deletion, outbound messages and schema. ⚙️

His result: €2,300, two business days. Logs confirmed no misuse - and in the following year, reading diffs caught four more unrequested modifications, two of them consequential. 🚀

👉 Cursor code review: catching what autocomplete got wrong: https://launchstudio.eu/en/blog/cursor-code-review-catching-what-autocomplete-got-wrong

#CodeReview #Cursor #AICoding #AppSecurity #LaunchStudio #Manifera
