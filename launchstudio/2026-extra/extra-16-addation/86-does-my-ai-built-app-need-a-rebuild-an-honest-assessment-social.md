🩺 TWO OPINIONS ON THE SAME CODE

FIRST OPINION (a development agency)
Diagnosis: "unmaintainable AI output"
Treatment: a full rebuild in a different framework
Recovery: about four months
Cost: about €24,000

SECOND OPINION (LaunchStudio)
Diagnosis: a data model that fits the business well, with instructors, students, lessons, packages and payments, all sensibly related. Plus five specific problems:
1. Loose policies letting instructors see each other's students
2. Payments confirmed on the redirect
3. Three duplicated versions of the lesson calendar
4. Missing indexes on the lessons table
5. No staging
And one area that really did have structural problems: a reporting module that calculated everything in the browser.

Treatment (9 business days, €3,300):
✓ Policies fixed, with tests
✓ Payments moved to verified webhooks, with reconciliation
✓ The calendar consolidated into one component
✓ Indexes added
✓ Staging and monitoring
✓ Only the reporting module rebuilt, with server-side queries
✓ The interface left exactly as instructors knew it

THE PATIENT
Rijlesagenda, built by Pim Hendriks in Apeldoorn with Lovable and Supabase over ten months, and used by around 150 driving instructors for lesson planning, student progress and Mollie payments. After a run of bugs, the first opinion recommended starting over.

RECOVERY
Bug reports dropped sharply the next month. The reporting page went from slow to instant. Pim kept building in Lovable, and estimates the second opinion saved him about €20,000 and four months.

"Two experts looked at the same code. One saw a rewrite. The other saw five problems and fixed them. My instructors never noticed anything except that the app got better." - Pim Hendriks

https://launchstudio.eu/en/blog/does-my-ai-built-app-need-a-rebuild-an-honest-assessment

#Rebuild #Refactor #Lovable #VibeCoding #AIFounder #LaunchStudio #Manifera
