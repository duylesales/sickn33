🚨 A build error blocked his launch. An AI coding assistant's fix made it go away instantly. What actually happened: his secret API key got bundled directly into public-facing JavaScript, visible to anyone who viewed his site's source — for months. 🔓

Next.js blends frontend and backend in one project. That convenience is exactly what makes the boundary easy to blur. 🧠

❌ `NEXT_PUBLIC_` explicitly means "bundled into client code, visible to anyone" — not a generic fix for a build error
❌ An unprefixed secret referenced in client-side code fails at build time — tempting to "fix" by just adding the prefix
❌ An API call needing a secret key, written client-side instead of through a server-side API route, forces the exposure
❌ A broadly-marked client component can pull server-only logic, including secret references, into the client bundle

✅ Search every environment variable reference: genuinely public and correctly prefixed, or server-side only — never both
✅ Build your app and inspect the actual compiled client bundle for anything sensitive-looking
✅ This is structurally different from hardcoded secrets in source — a secret stored correctly, exposed by where it's referenced
✅ If exposed, rotate the credential — the same principle as any other exposed secret

At **LaunchStudio**, we specifically review Next.js apps for this server-client boundary issue, checking source and the compiled bundle. Backed by Manifera's production Next.js experience. 🛡️

His result: the exposed key rotated immediately, the call restructured through a proper server-side route. 🚀

👉 Get your Next.js app checked for secrets crossing the server-client boundary: [Link to article]

#IndieHacker #LaunchStudio #Manifera #NextJS #AISecure
