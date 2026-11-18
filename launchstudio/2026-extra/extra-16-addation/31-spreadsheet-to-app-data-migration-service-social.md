🔍 Spot the duplicates (illustrative rows, but the problem was real)

Dorpsstraat 12, Zutphen · Jansen
Dorpstraat 12 · J. Jansen
Dorpsstr. 12A · Fam. de Vries

Same house? Same household? Same boiler?

Wouter Brouwer runs a heating installation company in Zutphen and built Ketelzorg with Lovable and Supabase to plan maintenance visits, record work done and send reminders to customers. It worked well in testing. But nine years of customer and visit history lived in twelve spreadsheets kept by different planners, plus a folder of scanned service reports. And the planners wouldn't switch until they could see a customer's history in the app.

What the analysis found:
• Around 6,300 customer rows, really about 4,100 households, because addresses appeared with different spellings and different occupants over the years
• Visit dates in four formats
• Boiler models typed freely, with dozens of variations
• Service contracts marked with cell colours

How LaunchStudio untangled it (9 business days, €3,100):
✓ Addresses normalised by postcode and house number, with proposed merges, and about 300 uncertain cases approved by Wouter's senior planner
✓ Boiler models mapped to a standard list
✓ Colour-coded contracts turned into a contract field, after confirmation
✓ Visits linked to households and installations
✓ Around 9,000 scanned reports matched to visits by date and address, and moved to private storage
✓ Import scripts run five times on staging until the numbers matched
✓ A reconciliation report listing 140 rejected rows, each with a reason

On a Friday afternoon, the spreadsheets were frozen. The final import ran in under an hour. On Monday, the planners worked in Ketelzorg only. Maintenance reminders now go out automatically, and nobody asks a colleague where a customer's history is anymore.

"The app was finished months ago. What made people actually use it was seeing nine years of history the moment they opened a customer." - Wouter Brouwer

https://launchstudio.eu/en/blog/spreadsheet-to-app-data-migration-service

#DataMigration #Excel #Supabase #Lovable #AIFounder #LaunchStudio #Manifera
