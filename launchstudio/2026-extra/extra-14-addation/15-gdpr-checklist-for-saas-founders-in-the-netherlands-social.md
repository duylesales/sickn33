🚨 Hanna Vos, a former recruiter in Amsterdam, built Vacaturely with Cursor: an applicant tracking tool for Dutch employers. Five small companies used it happily. Then a healthcare group with 1,200 employees wanted to sign - and its privacy officer sent a 60-question questionnaire plus a request for a verwerkersovereenkomst. Hanna had neither. 😳

Small customers never asked. The first big one asked everything at once. Working through a GDPR checklist, she found: 🧠

❌ Customers separated in application code, with one export endpoint skipping the check
❌ Candidate CVs in a bucket with long-lived public links
❌ Email, error tracking and an AI CV-summary feature: sub-processors never listed
❌ Deleting a customer organisation left candidates' data behind

✅ Tenant isolation moved into Row Level Security with organisation membership
✅ Private CV storage with short-lived signed URLs, plus audit logging
✅ Organisation-level deletion at contract end, AI provider under a processor agreement with training disabled
✅ A sub-processor list with locations and a security summary for her lawyer to work from

At **LaunchStudio**, backed by Manifera's 11+ years of answering enterprise security questionnaires, we build the technical measures behind every document your customers ask for. 🛠️

💡 Her result: €4,200, thirteen business days. The privacy officer approved Vacaturely after one round of follow-up questions, and procurement for new customers now takes days, not weeks. 🚀

👉 Selling B2B SaaS in the Netherlands? Use this GDPR checklist before your first big prospect asks: https://launchstudio.eu/en/blog/gdpr-checklist-for-saas-founders-in-the-netherlands

#GDPR #AVG #B2BSaaS #Cursor #LaunchStudio #Manifera
