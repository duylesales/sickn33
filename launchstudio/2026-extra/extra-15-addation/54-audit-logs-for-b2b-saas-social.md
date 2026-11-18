⚖️ THE CASE OF THE FORTY MISSING INVOICES

THE FACTS
Around forty invoices from a client vanished from Boekhoudportaal, days before a VAT deadline. Boekhoudportaal, built by Merel Huisman with Bolt and Supabase, is where accounting firms collect documents from clients, review invoices and share annual reports.

THE ACCUSATIONS
The client blamed the accounting firm.
The firm blamed the software.
The software had nothing to say.

THE PROBLEM WITH THE EVIDENCE
There wasn't any.
• No audit trail
• Records hard-deleted, recoverable only from a backup
• Admin role changes, exports and document downloads left no trace
• Merel's own support access to client accounts was invisible to the firms

A second firm, preparing for a quality review, asked for proof of who had accessed client files. Merel couldn't provide it.

THE REMEDY (LaunchStudio, 10 business days, €3,600)
• Soft deletion for invoices and documents, so firm admins can restore them
• An append-only audit log, protected by Row Level Security
• Database triggers recording creation, changes and deletion of key records, with who did it
• Application events for logins, failed logins, role changes, downloads, exports and integration changes
• Support access by Merel's team visible in each firm's log, with a reason field
• An audit view with filters, readable descriptions and CSV export
• Two-year retention with archiving, and sensitive document content kept out of change records

THE NEXT HEARING, THREE MONTHS LATER
A similar question came up. The firm's admin found the answer in under a minute: an employee of the client had deleted duplicate uploads by mistake. The documents were restored on the spot. The second firm passed its quality review with the audit export.

CLOSING STATEMENT
"The deleted invoices weren't really the problem. The problem was that nobody could prove what had happened. Now anyone with the right role can." - Merel Huisman

https://launchstudio.eu/en/blog/audit-logs-for-b2b-saas

#AuditLogs #Compliance #FinTech #B2BSaaS #AIFounder #LaunchStudio #Manifera
