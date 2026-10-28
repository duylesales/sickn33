🚨 Jolanda Smeets, who runs a small accountancy practice in Venray, built Aangiftebox in Lovable: clients get a checklist for their tax return, upload documents from their phones, answer questions and approve the final return. Four more North Limburg firms joined - about 2,100 households. Then a client noticed she could open another household's annual income statement by changing a number in the download URL. 😳

Documents - with BSNs on nearly every page - sat in a public bucket. Mobile uploads failed and clients re-sent photos, creating duplicates. On the busiest April evening the portal froze for an hour. Staff at all five firms could see all clients, approvals were a checkbox that could be re-ticked after edits, and nothing was ever deleted. Here's what taking an accountancy portal from AI prototype to production requires: 🧠

❌ Tax documents with BSNs at public URLs
❌ Uploads that fail on mobile data
❌ Every firm's staff seeing every client
❌ Approvals not tied to a fixed document

✅ Private storage with signed links and malware scanning, plus resumable uploads with duplicate detection
✅ Firm, team and client separation with row level security, and MFA for staff and as a client default
✅ Approvals recorded against a frozen PDF with server timestamps, and retention rules per document type
✅ Connection pooling and background processing, load-tested at three times the April peak - with the exposure assessed and reported on advice

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make your portal at least as careful as the shoebox your clients used to bring. ⚙️

Her result: €3,400 over twelve business days, plus €49/month. The next tax season ran without outages or cross-client access, and Aangiftebox added six more firms. 🚀

👉 AI prototype to production for accountancy firms: client documents at year-end: https://launchstudio.eu/en/blog/ai-prototype-to-production-for-accountancy-firms-client-documents-at-year-end

#Accountancy #TaxSeason #DataProtection #Lovable #LaunchStudio #Manifera
