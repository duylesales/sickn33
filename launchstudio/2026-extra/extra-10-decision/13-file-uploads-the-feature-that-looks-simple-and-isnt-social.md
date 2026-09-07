🚨 Nadia reused her portfolio-upload component for ID verification on Craftlink. It quietly gave every artisan's ID document a public, guessable URL. 😳

File uploads look like a few lines of code — until the file isn't what its extension claims: 🧠

❌ The bucket backing "portfolio photos" was public by default — fine for photos, a data exposure once reused for ID documents
❌ Filenames and `Content-Type` headers aren't a security boundary — both are strings the uploader fully controls
❌ An unset size limit meant a 380MB file renamed `photo.jpg` could hang a serverless function for minutes
❌ Nothing checked the actual file bytes, so a handful of malformed uploads sat unflagged in the same bucket

✅ Split flows onto separate storage paths so a public bucket for photos never touches private documents
✅ Validate by magic bytes — the file's real first bytes — not the filename or client-reported MIME type
✅ Move verification documents behind private, expiring signed URLs scoped to admin review only
✅ Serve uploads from a separate origin with `Content-Disposition: attachment` so nothing executes by accident

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we catch the public-bucket-by-default pattern before a stranger with a guessed URL does. 📁

Her result: verification documents are no longer publicly reachable under any URL, and the portfolio upload — genuinely fine to keep public — was left completely untouched. 🚀

👉 Check whether your upload flow is quietly public: [Link to article]

#IndieHacker #AICoding #ProductionReady #SaaS #LaunchStudio #Manifera
