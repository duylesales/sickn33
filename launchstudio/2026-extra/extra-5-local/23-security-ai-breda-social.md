🍽️ TODAY'S MENU at TableTuned, Breda

STARTER
A reservation and staff-scheduling tool for independent restaurants around Breda's Ginnekenmarkt district. Elise van Dongen built it in Cursor in about ten focused days. Six restaurants were using it within a month.

MAIN COURSE (not on the menu)
A seventh restaurant's manager, evaluating the tool, changed a reservation ID in the URL out of curiosity. Out came another restaurant's full guest list, phone numbers included.
He reported it instead of exploiting it. But the exposure had been live for the entire month.

KITCHEN NOTES
The reservations table ran on a default Supabase setup with no row-level security. Nobody had ever locked it down to restaurant-specific access.

THE CHEF'S CORRECTION (LaunchStudio, 5 business days, €1,300)
• Proper tenant isolation for every restaurant
• Rate limiting on the public booking endpoint
• Stripe keys moved out of client-side code into a secured backend function

DESSERT
TableTuned relaunched with verified tenant isolation. Elise now leads her sales conversations with the security audit, instead of hoping the topic doesn't come up.

"The scariest part wasn't the bug. It was realizing I had no way of finding it myself. Now I know exactly what was fixed and why." - Elise van Dongen

Serving guest data from an AI-built app? Check the kitchen first: https://launchstudio.eu/en/blog/23-security-ai-breda

#AINativeFounder #LaunchStudio #Manifera #SecurityAudit #Breda
