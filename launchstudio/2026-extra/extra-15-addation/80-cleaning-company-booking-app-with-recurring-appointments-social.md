🛒 Shopping list (illustrative)
- Milk
- Bread
- Alarm code for the client's home
- Key safe code
- Eggs

That's how the founder herself described it: the app was treating clients' alarm codes like a shopping list.

Sandra Pijnenburg runs a cleaning company in Breda with around 40 cleaners serving households and small offices. She built Poetsplanner with Bolt and Supabase: clients book recurring cleaning, cleaners see their schedule on their phones, and clients pay monthly. It replaced a paper schedule and a lot of phone calls.

At around 350 households, the cracks showed:
• Alarm and key safe codes in plain text, in a notes field every cleaner could see, and in the daily schedule email
• A full year of visits generated when each schedule was created, so a switch from weekly to fortnightly left weekly visits in the system, and cleaners sometimes turned up at the wrong homes
• After summer time started, many visits showed an hour later than agreed
• Invoices based on the schedule, not on completed visits, so skipped visits were billed

The fix (LaunchStudio, 14 business days, €5,700):
🔐 Access codes in an encrypted field, visible only to the assigned cleaner on the day of the visit and to two office staff, with every view logged
🔐 Codes removed from emails and exports, and clients advised to change any codes that had been exposed
🔁 Recurrence rules with exceptions, generated for a rolling eight weeks, with a clear choice between changing one visit or all future ones
🕐 Times stored with the Europe/Amsterdam time zone
🧹 Assignment that prefers the regular cleaner, with substitute suggestions during absence
💶 Billing on completed visits, monthly SEPA direct debit through Mollie, and late cancellations charged per the terms

Wrong-address visits and time confusion disappeared. Invoice disputes dropped sharply. Two office clients signed larger contracts after reviewing the new handling of access codes, and Sandra can now answer exactly who viewed a client's access information.

"My clients trust us with their homes. The app was treating their alarm codes like a shopping list." - Sandra Pijnenburg

https://launchstudio.eu/en/blog/cleaning-company-booking-app-with-recurring-appointments

#CleaningBusiness #Scheduling #DataSecurity #SEPA #AIFounder #LaunchStudio #Manifera
