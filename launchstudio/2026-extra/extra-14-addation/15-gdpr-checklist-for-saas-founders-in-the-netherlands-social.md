Q&A with a healthcare group's privacy officer, and the answers a founder needed to give 🏥

Hanna Vos, a former recruiter in Amsterdam, built Vacaturely with Cursor: applicant tracking for small and mid-sized Dutch employers, with job pages, candidate pipelines and interview scheduling. Five small companies used it happily, and never asked a thing. Then a healthcare group with 1,200 employees wanted to sign. Its privacy officer sent 60 questions and asked for a verwerkersovereenkomst.

Q: How are customers' data kept apart?
Before: In application code, not database policies, and one export endpoint skipped the check.
After: Row Level Security with organisation membership, and the export endpoint fixed.

Q: How are CVs stored?
Before: A bucket with long-lived public links.
After: Private storage with short-lived signed URLs.

Q: Which sub-processors do you use?
Before: An email provider, an error tracker and an AI CV-summary feature, never listed.
After: A sub-processor list with locations, and the AI provider under a processor agreement with training disabled.

Q: What happens to our data when the contract ends?
Before: Deleting an organisation left candidates' data behind.
After: Organisation-level deletion at contract end.

Q: Can you show who exported or deleted data?
After: Audit logging for exports and deletions.

LaunchStudio did this in 13 business days, for €4,200, including a security measures summary. Hanna's lawyer drafted the verwerkersovereenkomst using those facts.

The privacy officer approved Vacaturely after one round of follow-ups. Hanna now reuses the same document pack for every new customer, and procurement takes days instead of weeks.

"Small customers never asked. The first big one asked everything at once, and I needed real answers, not reassuring ones." - Hanna Vos

https://launchstudio.eu/en/blog/gdpr-checklist-for-saas-founders-in-the-netherlands

#GDPR #AVG #B2BSaaS #Cursor #LaunchStudio #Manifera
