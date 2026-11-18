🍷 TASTING NOTES: Wijnkring's Airtable base, vintage "it grew"

Daan Bosman runs a wine subscription club in Nijmegen with about 1,800 members. Members, boxes, wines, suppliers and deliveries all lived in Airtable. A Lovable member portal read and wrote through the Airtable API, and fourteen automations handled box assembly, payment reminders and delivery notifications.

NOSE
Slow. Several seconds per page, and rate limit errors on Monday mornings, when members change their box preferences.

PALATE
Inconsistent. The region field held four different spellings of Bordeaux. Stock counts went negative when two members picked the last bottles at the same time.

FINISH
Unpleasant. After a misconfigured filter, one member saw another member's delivery address.

PAIRING REQUESTED
Mollie SEPA direct debit, which needs reliable payment records.

THE SOMMELIER'S WORK (LaunchStudio, 13 business days, €5,600)
• A Postgres schema on Supabase in Frankfurt, with lookup tables for regions and grapes, join tables for box contents, and money stored as integer cents
• Migration scripts that normalised values, merged 63 duplicate members and kept the original member numbers
• Row Level Security, so members see only their own data
• Stock deductions in transactions, so the last bottle can't be sold twice
• Label images in private storage, and the fourteen automations rebuilt as edge functions and scheduled jobs with alerts
• The Lovable portal reconnected, plus an admin screen for assembling boxes

VERDICT
Record counts verified for every table. Pages load in well under a second, stock hasn't gone negative since, and Mollie SEPA went live the following month.

"Airtable was perfect when the club was a hobby. Once members trusted us with their addresses and bank details, I needed a database that would refuse to accept mistakes." - Daan Bosman

https://launchstudio.eu/en/blog/airtable-to-supabase-migration-moving-a-no-code-backend-to-postgres

#Airtable #Supabase #Postgres #Ecommerce #AIFounder #LaunchStudio #Manifera
