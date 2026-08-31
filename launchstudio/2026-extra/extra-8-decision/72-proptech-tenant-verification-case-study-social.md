🚨 The moment his app stored a single passport scan or salary statement, it legally became a GDPR data processor — with breach notification duties, impact assessments, and liability he had no way to meet. So he built a system designed to never hold the data at all. 😳

Tenant screening needed identity and income verification. It didn't need to become a compliance liability. Here's the architecture that solved both: 🧠

❌ The Lovable prototype stored passport scans and payslips in a flat Supabase bucket — no encryption at rest, no deletion policy, no access audit trail
❌ Landlords were asking tenants to email sensitive PDFs — insecure, and tenants understandably reluctant
❌ Storing the underlying documents meant DPIAs, 72-hour breach notification, and full data-subject-access-request handling
❌ "Compliance" felt like it meant hiring a lawyer and writing a 50-page privacy policy

✅ Tenants redirected to a certified KYC provider's hosted flow — HuurCheck receives only a result, never the documents
✅ Database stores only outcome, timestamp, reference ID, and confidence score — no passport images, no salary figures
✅ Verification records auto-delete 90 days after lease start, with tenant self-service deletion available anytime
✅ Full audit trail of every event logged with zero personal data inside it

At **LaunchStudio**, backed by Manifera engineers who design systems to avoid holding sensitive data in the first place, the safest data really is the data you never keep. 🔍

His result: 187 tenant verifications for 34 landlords across three cities in three months — zero sensitive documents ever stored on his infrastructure. 🚀

👉 Tell us what sensitive data your prototype handles and we'll show you what doesn't need to be stored: [Link to article]

#LaunchStudio #Manifera #GDPR #DataMinimization #VibeCoding #PropTech #SaaSFounders
