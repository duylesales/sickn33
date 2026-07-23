🚨 A subcontractor noticed the sequential invoice number in his address bar, changed it by one digit out of idle curiosity — and found himself looking at a completely different client's invoice, billing rate and project details included. 🧾

AI and software engineering aren't the same job. One generates code that satisfies a described scenario. The other asks "what request wasn't described, and what does this code do if it receives that instead?" 🧠

❌ "Build an invoices page showing a user's history" reliably produces a page fetching by ID — satisfying the description completely
❌ This is the textbook insecure direct object reference: a resource fetched by predictable ID, without verifying the requester's claim to it
❌ The happy path works identically whether or not an ownership check exists — no visible symptom until someone requests an ID that isn't theirs
❌ Reviewing your own code for "does this do what I described" is structurally blind to this — the code does exactly what was described

✅ Add an explicit ownership check to every resource-fetching endpoint — confirm the record actually belongs to the requester
✅ Apply consistently across invoices, orders, documents, any per-user resource in the system
✅ Switching to random UUIDs helps obscure IDs but doesn't replace the actual ownership check

At **LaunchStudio**, this ownership-check audit is a core part of our production-readiness review. Backed by Manifera's 11+ years of enterprise software engineering discipline. 🛡️

His result: explicit ownership verification added to every per-user resource, closing the gap across the entire application. 🚀

👉 Talk to an engineer who understands AI-generated code: [Link to article]

#IndieHacker #LaunchStudio #Manifera #AISecure #SoftwareEngineering
