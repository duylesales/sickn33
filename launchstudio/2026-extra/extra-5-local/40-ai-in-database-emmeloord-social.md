🏗️ SURVEYOR'S REPORT: Perceelbeheer, Emmeloord

PROPERTY
A land parcel management tool tracking soil data, crop history and lease agreements for farmers across the Noordoostpolder.

OWNER
Gijs Veenstra, a polder farmer with a software background. He wrote most of the application logic himself in Bolt, but let the AI generate the initial database schema and never went back to review its structure.

INSPECTION
Scope: the foundation (the database schema)
Common defects checked: 4
Defects found: 3

DEFECT 1: MISSING SUPPORT
The parcels table had a foreign key to farmers with no index. Once test data crossed a few thousand rows, lookups slowed noticeably.

DEFECT 2: UNLOCKED DOORS
Parcel IDs were sequential integers, exposed directly in the API. A farmer could guess a neighboring parcel's ID and view lease details that weren't theirs.

DEFECT 3: NO BUILDING RECORDS
No migration history at all. Every schema change had been applied ad hoc through the AI chat interface.

REPAIRS (LaunchStudio, 8 business days, €1,550)
• Missing indexes added
• Parcel identifiers migrated to non-sequential UUIDs, with authorization checks at the query level
• A version-controlled migration workflow using Prisma

CONDITION AFTER REPAIR
3,000+ parcels across the Noordoostpolder, with query responses under 100ms. Schema updates now ship without risking data integrity.

"I'd never actually designed a production database schema before - I just let the AI figure it out and assumed it knew what it was doing. It didn't, not really." - Gijs Veenstra

Get your AI database surveyed: https://launchstudio.eu/en/blog/ai-in-database-emmeloord

#AINativeFounder #LaunchStudio #Manifera #Emmeloord #DatabaseDesign
