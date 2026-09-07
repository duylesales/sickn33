🚨 Thijs's contract review tool had two happy firms trying it informally. Then a third firm sent a security questionnaire, and the honest answers to it were uncomfortable. 😳

A good product and a reviewed product are not the same thing — here's what the questionnaire actually found: 🧠

❌ Contracts stored in a single Supabase bucket, readable by any authenticated firm user regardless of which matter they were staffed on
❌ Contract text sent straight to a general-purpose AI API with no confirmation it excluded training on submitted data
❌ "Delete" only set a hidden flag — the file and database row stayed intact indefinitely
❌ "We follow standard GDPR practices" is not an answer to a firm asking whether a breach waives privilege

✅ Restructure storage around per-matter access policies, not one flat firm-wide permission
✅ Switch to an API configuration with contractually confirmed no-training terms, documented for reuse
✅ Implement genuine hard-deletion with a retention window that covers backups
✅ Prepare EU hosting, encryption specifics and a sub-processor list before the questionnaire arrives, not during it

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build the confidentiality controls a firm's 60-page questionnaire is actually testing for. ⚖️

His result: Clausio passed its first full firm security review on resubmission, then reused the same documentation package to pass its next two firm reviews without extra engineering work. 🚀

👉 See what a law firm's security review will actually ask you: [Link to article]

#LegalTech #DataSecurity #StartupFounders #GDPR #LaunchStudio #Manifera
