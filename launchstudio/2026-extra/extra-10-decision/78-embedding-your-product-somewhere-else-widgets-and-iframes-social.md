🚨 Milan Novak's booking widget worked perfectly on every site he tested. It failed for roughly a third of real visitors, and he had no way to know until salons started complaining. 😳

An embed running on someone else's website meets failure modes your own testing will never reproduce: 🧠

❌ A cookie remembering partial bookings was a third-party cookie in that context — blocked outright in Safari and Firefox, a third of his market's mobile visitors
❌ The script inserted elements directly into the page, and one salon's own CSS made the submit button invisible for six weeks before anyone reported it
❌ Four customer sites had layout conflicts nobody caught during testing on just two WordPress sites
❌ The public key had no domain restriction, so a copied snippet was creating bookings in an unrelated account

✅ Use a small script that creates a sandboxed iframe — one-line install, dynamic sizing, isolated from the host page's CSS
✅ Avoid depending on cookies entirely; keep state in the URL or in server-side sessions keyed by a token
✅ Restrict every public key to the domains the customer registers, since the key is visible in page source
✅ Version the loader URL and treat each version as permanent — you can't take back a snippet pasted on a thousand sites

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build embeds that behave on real customer websites, not just the one you tested on. 🧩

His result: a versioned iframe loader with domain-restricted keys and account-tagged error reporting, eliminating the CSS conflicts and the blocked-cookie failures entirely. 🚀

👉 See what your embed actually does on someone else's site: [Link to article]

#WebDev #SaaS #Embed #IndieHacker #LaunchStudio #Manifera
