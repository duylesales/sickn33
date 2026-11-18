1 click.
1 client record.
4 projects.
600+ tasks.
Around 1,200 photo references.
Every message with that client.
18 months of work, gone. 🏗️

Pieter Kuiper built Bouwplanner with Bolt and Supabase: planning for small construction and renovation companies, with projects, phases, tasks, photos and client communication. One morning, a project manager at a customer deleted a client record while trying to remove a duplicate. The schema used on delete cascade everywhere, so the deletion took everything connected to it.

2 days of engineering to recover: a point-in-time restore of the whole database to a copy, then manual extraction and reinsertion of the affected records.

0 safety nets elsewhere in the app: every delete was a hard delete, with no confirmation for big deletions, no audit trail and no undo.

The new numbers (LaunchStudio, 9 business days, €3,300):
2 new columns on key tables: deleted_at and deleted_by
6 record types now soft-deleted: clients, projects, phases, tasks, documents and messages
1 database function that soft-deletes a client and its related records in one transaction
RLS policies hiding deleted rows from regular queries
Cascades replaced by restrictive foreign keys, except for truly dependent data
Partial unique indexes, so items with the same name can be created again
1 trash view where admins restore items with their related data
1 confirmation summarising impact before big deletions
10 seconds to hit undo
60 days in the trash before a nightly job deletes permanently
Every deletion in the audit log

And the next six months:
~140 items restored from the trash by users themselves
0 support tickets needed for it
0 database restores
1 customer who lost data, now one of Pieter's references

"A single click shouldn't be able to erase a year and a half of someone's work. Now it can't, and when people make mistakes, they fix them themselves." - Pieter Kuiper

https://launchstudio.eu/en/blog/soft-delete-vs-hard-delete-in-saas

#SoftDelete #DataLoss #Supabase #ConstructionTech #AIFounder #LaunchStudio #Manifera
