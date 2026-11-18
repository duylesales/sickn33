Lotte Brink thought the insurance form was paperwork. It turned out to be the first honest security review her product ever had. 📄

She built Huurdersportaal with Lovable and Supabase: a portal for small property managers where tenants report maintenance issues, upload documents and receive announcements. A housing association in Gelderland with around 3,000 homes wanted to use it. The contract required cyber insurance with a minimum insured amount, next to professional liability cover.

Her broker sent the insurer's application, and Lotte answered honestly. The answers came back as a conditional offer: a high premium, and several issues to fix within 60 days.

What the honest answers had revealed:
• No MFA on her hosting, domain registrar and database dashboards
• A former freelancer who still had access to the repository and the Supabase project
• Backups that had never been restored
• Dependencies untouched since the app was generated
• Email sent without DMARC

And a quick review found something the form hadn't even asked about: tenant documents, identity documents included, in a storage bucket any logged-in user could read.

So LaunchStudio got to work (8 business days, €2,900):
→ MFA on every critical service, named accounts instead of shared logins, the freelancer's access removed
→ Tenant documents in private storage, with per-tenant Row Level Security and signed links
→ Secrets scanned and rotated, dependencies updated, automated vulnerability alerts
→ SPF, DKIM and DMARC configured
→ A documented restore test, monitoring and alerts, and a one-page incident procedure

Lotte updated her application with evidence for every answer. The insurer removed the conditions and offered cover at a substantially lower premium. The housing association signed, and the same evidence pack now answers customer security questionnaires.

"The insurance form was the first honest security review my product ever had. Fixing what it found made the product safer and the policy cheaper." - Lotte Brink

https://launchstudio.eu/en/blog/cyber-insurance-for-small-saas-in-the-netherlands

#CyberInsurance #Cybersecurity #PropTech #SaaS #AIFounder #LaunchStudio #Manifera
