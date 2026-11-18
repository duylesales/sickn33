🗓️ From "we need ISO 27001" to certified: one SaaS timeline

THE STARTING POINT
Wouter Jansen and his co-founder built Contractkompas in Lovable and Supabase: contract management for mid-sized companies, tracking renewal dates, obligations and approvals. After a year: 35 customers. Then two bigger prospects, a housing corporation and a regional hospital group, both required ISO 27001 within twelve months of signing.

STEP 1: GAP ANALYSIS
Their ISO consultant's verdict: fix the technical foundations before writing a single policy.
• One shared admin account, no MFA
• Logs not retained
• Backups never restored
• Deployments straight from Lovable to production
• Nobody could say which services processed customer data
Writing policies on top of that would have meant documenting controls that didn't exist.

STEP 2: FOUNDATIONS (LaunchStudio, 12 business days, €3,600)
• A named account with MFA for every staff member
• Admin authorisation moved into database roles with Row Level Security
• Audit logs for logins, permission changes and contract exports, with defined retention
• Point-in-time recovery with a recorded restore test
• Staging, plus GitHub-based deployments with code review
• Secrets in managed storage and rotated
• A system description and sub-processor register for the ISMS documentation

STEP 3: THE FOLLOWING MONTH
The ISMS evidence period begins.

STEP 4: NINE MONTHS LATER
Stage 2 audit passed. No major nonconformities in the technological controls. Certified within the window both prospects required.

"Our consultant was right: you can't certify security you don't have. Fixing the foundations first made the whole ISO project shorter." - Wouter Jansen

When should you start? https://launchstudio.eu/en/blog/iso-27001-for-early-stage-saas-when-to-start

#ISO27001 #InfoSec #B2BSaaS #Compliance #AIFounder #LaunchStudio #Manifera
