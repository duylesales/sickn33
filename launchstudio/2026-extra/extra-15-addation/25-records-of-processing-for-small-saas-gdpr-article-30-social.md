🧹 Decluttering a SaaS: what to keep, fix or throw away

Jesse van Dam built Vacatureflow with Lovable and Supabase: an applicant tracking tool for small recruitment agencies in the Randstad, where recruiters store candidate profiles, CVs and interview notes and share shortlists with clients. Then a larger agency asked for his processing register and sub-processor list. He had neither.

Building the register was like opening every cupboard in the house.

FOUND IN THE CUPBOARDS
• Eleven external services, from email delivery and error tracking to an AI CV parser, several missing from the privacy policy
• The CV parser processing data in the US without a processing agreement
• An error tracker capturing full request bodies, candidate details included
• Candidate profiles never deleted, even years after a vacancy closed
• AI-generated form fields like date of birth and nationality, collected for no purpose

THROW AWAY 🗑️
• The unused fields
• Three services no longer needed

FIX 🔧
• CV parsing moved to an EU provider under a processing agreement, no training use
• Error tracking set to strip request bodies and personal data
• Candidate profiles anonymised automatically 12 months after last activity, unless the candidate consents to stay in the pool, with backups on the same cycle

KEEP AND LABEL 🏷️
• A technical data map of every table, field and service
• Documented security measures and sub-processors, which Jesse and his privacy adviser turned into controller and processor registers and a new privacy policy

The work: 9 business days, €2,800. Both registers went to the agency within two weeks, and the review was approved. Less data also meant lower storage and service costs, and the documents have been reused in four more customer reviews.

"I thought a processing register was paperwork. Building it showed me data I didn't need, services I'd forgotten and risks I hadn't seen." - Jesse van Dam

https://launchstudio.eu/en/blog/records-of-processing-for-small-saas-gdpr-article-30

#GDPR #AVG #Privacy #HRTech #AIFounder #LaunchStudio #Manifera
