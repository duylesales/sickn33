📝 ACCESSIBILITY TEST RESULT: Vergunningloket

Standard: WCAG 2.1 AA
First test: ❌ FAILED on 31 criteria
Retest: ✅ PASSED, no failures at level A or AA

Hanna Bakker, a former policy adviser, built Vergunningloket with v0 and Supabase: a portal that lets residents of small municipalities apply for event and terrace permits, upload documents and follow their application. A municipality in Drenthe wanted it, but procurement required WCAG 2.1 AA, confirmed by an external test before go-live.

EXAMINER'S NOTES, first test
• Document upload: a styled div that keyboard users couldn't reach
• Multi-step form: placeholders instead of labels, errors shown only as red outlines
• Focus outlines removed across the whole project
• The municipality's teal failed contrast on white
• The confirmation dialog let focus escape behind it
• "Document uploaded" and similar updates were silent for screen readers
• Every page had the same title, and Dutch pages were marked as English

REMEDIATION (LaunchStudio, 11 business days, €3,200)
✏️ An accessible file input and button pattern for uploads
✏️ Visible labels, autoComplete attributes and linked text errors on every step
✏️ Radix dialogs restored with correct focus handling, plus a :focus-visible style app-wide
✏️ A compliant teal in the design tokens
✏️ Live regions for uploads and step changes, unique page titles, the right language
✏️ Axe checks in the deployment pipeline, and accessibility rules in the v0 project instructions

AFTER THE RETEST
The municipality went live. Within the year, two neighbouring municipalities adopted Vergunningloket too, both citing the accessibility report.

"v0 made the portal look professional. Making it usable for every resident was the part that actually won the contract." - Hanna Bakker

https://launchstudio.eu/en/blog/wcag-accessibility-fixes-for-ai-built-apps

#WCAG #Accessibility #v0 #GovTech #AIFounder #LaunchStudio #Manifera
