🚨 Mehmet Kaya, a former market-research analyst in Tilburg, built Formlab with Cursor: a survey tool for small research agencies. Eight agencies were paying when a client's IT team ran a routine security check before approving it internally. It found two problems within an hour. 😳

A respondent could submit an answer containing a script tag — and because the dashboard rendered answers as raw HTML, it ran in every agency staff member's browser. And any workspace member could make themselves owner by adding "role": "owner" to a request. Here's the input validation gap in AI-generated code: 🧠

❌ Polished validation in the browser, none on the server
❌ API handlers saving whatever the request body contained (mass assignment)
❌ dangerouslySetInnerHTML used to keep answer formatting (stored XSS)
❌ Nothing to stop a future Cursor edit from removing a fix

✅ Strict Zod schemas on all 34 API routes, shared with the frontend
✅ Raw HTML replaced by a sanitised Markdown renderer with basic formatting only
✅ A Content Security Policy blocking inline scripts as a safety net
✅ A rejection test per route in CI — plus stored answers scanned and cleaned

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we treat validation as a system at every server boundary, not a per-form patch. ⚙️

His result: €1,350, five business days. Formlab passed the client's follow-up check two weeks later — and three sister companies subscribed. The CI tests have since caught two regressions from AI-generated edits. 🚀

👉 AI-generated code security: the input validation gap: https://launchstudio.eu/en/blog/ai-generated-code-security-the-input-validation-gap

#AppSecurity #Cursor #TypeScript #OWASP #LaunchStudio #Manifera
