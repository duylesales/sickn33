🔴 INCIDENT REPORT: the migration that dropped the orders table

PRODUCT
Bloemenabonnement, built by Thomas Brink with Cursor and Supabase. Weekly fresh flower subscriptions for offices and homes in Utrecht.

TRIGGER
Thomas asked an agent to add a delivery note field. The agent decided to restructure the orders table and generated a migration that dropped and recreated it. Thomas ran it directly against production, on a Tuesday afternoon.

IMPACT
Around 14,000 past orders and the current week's deliveries, gone.

CONSTRAINTS
• Daily backups on a paid plan, but no point-in-time recovery
• The last backup from early that morning
• A full restore would have erased new orders, Mollie payments recorded by webhooks and several new subscriptions since then

FIRST INSTINCT
Restore everything, right now.

RESPONSE (LaunchStudio)
1. No full restore. The latest daily backup restored into a separate project.
2. The orders table, plus order lines deleted through a cascade, exported from it.
3. Orders created after the backup reconstructed from Mollie payment records and webhook logs, stored in a separate table.
4. Everything reinserted into production in a reviewed transaction, with counts checked per day and spot checks against delivery lists.
5. The delivery note field added properly, with an additive migration.

RECOVERY TIME
Within 18 hours. By the next morning, all historical orders and that week's deliveries were back. No customer missed a delivery.

PREVENTION (5 business days, €2,300 in total)
• Point-in-time recovery enabled
• Migrations through a reviewed pipeline with staging
• Destructive statements flagged automatically
• A documented, tested restore procedure

FOLLOW-UP
Dozens of migrations since, without incident.

"The agent was trying to be helpful. I learned that the database needs a gate between a good idea and production." - Thomas Brink

https://launchstudio.eu/en/blog/how-do-i-recover-deleted-data-in-supabase

#Supabase #Cursor #Backups #DataRecovery #AIFounder #LaunchStudio #Manifera
