🚨 Loes Vermaat ran the office of her family's roofing company in Gorinchem and built Tekenklaar with Cursor: small contractors send quotes and agreements that customers sign on their phones. 45 contractors, about 900 signed documents in year one. Then a customer disputed a €14,000 roofing contract, claiming the signed version had a lower price. Tekenklaar couldn't prove otherwise. 😳

The "signed PDF" was regenerated from the database every time it was opened - and the contractor had edited the price after signing. Signing links were sequential IDs that never expired. There was no identity check beyond holding the link, the timestamp came from the customer's browser, and signed PDFs sat in a public bucket. Here's what AI-generated code security means for e-signatures: 🧠

❌ A "signed" document that changes when the database changes
❌ Guessable, permanent signing links
❌ Browser timestamps and no identity verification
❌ Signed contracts in public storage

✅ Each document frozen as a PDF when sent, with its SHA-256 hash stored
✅ Random single-use signing tokens expiring after 14 days, email verification and optional SMS codes above a contractor-set threshold
✅ A server-side evidence trail with trusted timestamps, and signed documents locked - changes need a new signed version
✅ Private storage, a certificate page on every signed PDF, and an EU signing provider integrated for advanced signatures

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering and its cybersecurity roots, we build the evidence that makes a signature something you can rely on. ⚙️

Her result: €2,400, eight business days. The dispute was settled, two later disputes were resolved quickly with the evidence certificate, and Tekenklaar grew to 70 contractors. 🚀

👉 Building an AI contract signing app? AI generated code security for e-signatures: https://launchstudio.eu/en/blog/building-an-ai-contract-signing-app-ai-generated-code-security-for-e-signatures

#ESignature #eIDAS #AppSecurity #Cursor #LaunchStudio #Manifera
