🕗 A MONDAY MORNING, clock by clock

SUNDAY EVENING
Dennis Vos asks his AI tool to "add a column for the mechanic's name." Errors appear. He accepts several follow-up suggestions.

MONDAY MORNING
Around 70 garages use Garageplanner, Dennis's SaaS for car repair garages in Zoetermeer, built with Lovable and Supabase, for appointments and invoices. They open it and see empty schedules. Dennis tries four more prompts. Each one makes it worse.

08:40
Dennis contacts LaunchStudio. After a short call, he invites the team to Supabase and the GitHub repository.

THE DIAGNOSIS
One Sunday suggestion had replaced the appointments table's policy with one that referenced the new column incorrectly, so every query returned nothing. A later prompt had renamed a column the invoice function depended on. Price for stabilisation, agreed upfront: €950.

10:15
✓ The policy restored from the migration history
✓ The column rename reverted
✓ The deployment rolled back to Saturday's version
✓ Two garages confirm that schedules and invoices work again

MONDAY AFTERNOON
The mechanic column is added properly, through a migration, on a new staging environment.

TWO WEEKS LATER
The incident report recommended staging, access tests and project instructions for Lovable. Dennis implemented them in a €2,200 Launch Ready project.

SINCE THEN
A similar prompt mistake was caught by the tests on staging.

Total time garages went without schedules: about ninety minutes. Dennis sent a short apology and explanation. No garage cancelled.

"Every prompt I tried made it worse. The fix was to stop, roll back and look at what had actually changed. I needed someone calm to do that with me." - Dennis Vos

https://launchstudio.eu/en/blog/emergency-fix-service-when-your-ai-built-app-is-down

#AppDown #IncidentResponse #Lovable #Supabase #AIFounder #LaunchStudio #Manifera
