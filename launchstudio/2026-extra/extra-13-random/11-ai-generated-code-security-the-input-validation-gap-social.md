🚪 A survey tool with a well-guarded front door, and an open side door

THE FRONT DOOR: the form
Validated fields. Sensible limits. Everything looked bulletproof.

THE SIDE DOOR: the server
What happened when someone skipped the form and talked to the API directly?
• A survey respondent could submit an answer containing a script tag. The results dashboard rendered answers with dangerouslySetInnerHTML to keep formatting, so the script ran in the browser of every agency staff member who viewed the results.
• The workspace-update endpoint accepted any field sent to it. A member could promote themselves to owner by adding "role": "owner" to a request.

Mehmet Kaya, a former market-research analyst in Tilburg, built Formlab with Cursor: a survey tool for small research agencies, with shared workspaces, question logic and a results dashboard that renders rich-text answers. Eight agencies were paying. Then one client's IT team ran a routine security check before approving it for internal use, and found both side doors within an hour.

Locking the side door (LaunchStudio, 5 business days, €1,350):
✓ Zod schemas in strict mode on all 34 API routes, shared with the frontend
✓ Raw HTML rendering replaced by a sanitised Markdown renderer, limited to basic formatting
✓ A Content Security Policy that blocks inline scripts
✓ Existing stored answers scanned and cleaned
✓ A rejection test for every route, so CI fails if a future Cursor edit removes a schema

Formlab passed the client's follow-up check two weeks later and was approved for internal use, which led to that client's three sister companies subscribing too. And the CI tests have since caught two regressions from AI-generated edits.

"The forms looked bulletproof. I just never looked at what the server did when someone skipped the form entirely." - Mehmet Kaya

https://launchstudio.eu/en/blog/ai-generated-code-security-the-input-validation-gap

#AppSecurity #Cursor #TypeScript #OWASP #LaunchStudio #Manifera
