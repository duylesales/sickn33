🔎 Spot the bugs. How many can you find?

Screen 1: "Jouw taken vandaag"
Screen 2: "Your tasks today"
Date: 03/04
Date: 04-03
Hours worked: 7.5
Hours worked: 7,5
Password reset email: English, always

(Illustrative, but every type of bug here was real.)

Dennis Brouwer built Schoonrooster with Bolt and Supabase: a scheduling tool for cleaning companies, where planners assign cleaners to locations and cleaners see their tasks on their phones. Many cleaners preferred English. Planners and clients expected Dutch. And a Belgian customer asked about French.

The app mixed languages unpredictably, depending on how each prompt had been written. Dates switched between month-day-year and day-month-year. Hours showed with a dot in some reports and a comma in others. Invoice totals sometimes failed to parse when planners typed a Dutch decimal comma.

The answers (LaunchStudio, 11 business days, €3,700):
✓ react-i18next with Dutch and English translation files
✓ Around 640 strings extracted into a feature-based key structure
✓ A glossary of cleaning and scheduling terms, reviewed by Dennis and a customer
✓ Dates, hours and amounts formatted with Intl APIs per user language, and number input that accepts Dutch commas
✓ A language preference on every profile, with auth and notification emails sent in that language
✓ PDF reports in the organisation's chosen language
✓ /nl/ and /en/ paths with hreflang on the marketing site
✓ Project instructions requiring translation keys for every new string

The result: cleaners use English, planners and clients use Dutch, and nobody is confused. Support questions about dates and hours dropped sharply. French later took just a translation file and a review.

"My app spoke three languages by accident. Now it speaks two on purpose, and adding a third was easy." - Dennis Brouwer

https://launchstudio.eu/en/blog/multilingual-saas-dutch-and-english-i18n-for-ai-built-apps

#i18n #Localization #SaaS #CleaningIndustry #AIFounder #LaunchStudio #Manifera
