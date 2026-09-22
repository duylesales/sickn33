---
Title: "AI Generated Code Security: The Input Validation Gap, Explained"
Keywords: ai generated code security, input validation, xss in ai code, cursor security, ai security vulnerabilities, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI Generated Code Security: The Input Validation Gap, Explained

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Generated Code Security: The Input Validation Gap, Explained",
  "description": "Why AI generated code so often validates input in the browser but not on the server, what that enables — mass assignment, stored XSS, oversized payloads — and a practical pattern for closing the gap with schema validation at every boundary.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-11",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-generated-code-security-the-input-validation-gap" }
}
</script>

Ask Cursor to build a signup form and you will get polished validation: a red border when the email is malformed, a strength meter on the password, a disabled submit button until everything is filled in. Look at the API route that receives the form and, very often, you will find it trusts whatever arrives. That asymmetry — careful in the browser, trusting on the server — is one of the most consistent patterns in AI generated code security, and it is the root of several vulnerability classes at once.

This article is for founders who can read code and want to understand why the gap exists, what it enables, and how to close it systematically rather than endpoint by endpoint.

## Why AI Generated Code Security Has This Gap

AI coding tools respond to what you can see. When you prompt for a form, you are describing a user experience, and the model produces one. Frontend validation is visible in the preview; you can test it by typing a bad email. Server-side validation is invisible in a demo — the frontend never sends bad data, so the server's lack of checks never shows.

There is also a training-data effect. Tutorials and example repositories frequently show frontend validation in detail and leave the API as a minimal "save the body to the database" handler for brevity. The model learns that shape.

The result: the browser acts as the only gatekeeper. But the browser is not yours. Anyone can send requests directly to your API with a tool like curl or the browser's developer console, bypassing every check the frontend performs.

## What the Gap Enables

**Mass assignment.** If the API takes the request body and writes it straight to the database, a user can add fields the form never showed. Signing up with `"role": "admin"` or updating a profile with `"plan": "enterprise"` works if the server does not restrict which fields are accepted. This is especially common with ORMs and Supabase client calls that accept whole objects.

**Stored cross-site scripting (XSS).** If user text — a comment, a project name, a bio — is saved without validation and later rendered without escaping, a script placed in it runs in other users' browsers. React escapes by default, but AI-generated code often uses `dangerouslySetInnerHTML` to render formatted text, or passes content into Markdown renderers configured to allow raw HTML.

**Type confusion.** A field expected to be a number arrives as a string, an array or an object. Loosely typed handlers accept it, and downstream logic behaves unpredictably — a quantity of `"-5"`, a price of `{}`, a date of `"yesterday"`.

**Oversized payloads.** Without size limits, one request can carry megabytes of text into a field meant for a name, bloating the database or crashing a function that processes it.

**Injection in less obvious places.** SQL injection is rarer with modern ORMs, but AI-generated code still builds raw queries for search and reporting features, and passes user input into shell commands, file paths or prompts sent to language models.

## The Pattern That Closes It

The fix is not to sprinkle checks into every handler. It is to define, once per endpoint, exactly what the server accepts — and reject everything else before any logic runs.

In a TypeScript stack, a schema library such as Zod makes this concise:

```typescript
import { z } from "zod";

const UpdateProfile = z.object({
  displayName: z.string().trim().min(1).max(80),
  bio: z.string().max(500).optional(),
  timezone: z.string().max(64),
}).strict(); // rejects any field not listed, e.g. "role" or "plan"

export async function POST(req: Request) {
  const parsed = UpdateProfile.safeParse(await req.json());
  if (!parsed.success) {
    return Response.json({ error: "Invalid input" }, { status: 400 });
  }
  // only parsed.data reaches the database
}
```

Three details matter. `.strict()` turns mass assignment from a vulnerability into a validation error. Length limits handle oversized payloads. And only the parsed result — never the raw body — is passed onwards.

The same schema can be shared with the frontend so both sides agree, which also removes a class of bugs where the browser allows something the server later rejects.

## Output Is the Other Half

Validation on input reduces risk; escaping on output removes it. Even with good validation, treat stored user text as untrusted wherever it is displayed:

- Prefer normal JSX rendering, which escapes by default.
- If you must render HTML or Markdown, sanitise it with a maintained library such as DOMPurify and a strict allow-list of tags.
- Set a Content Security Policy header that blocks inline scripts, so a missed escape does not become a working attack.

The [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) and its companion on XSS prevention are concise, practical references.

## Where to Look in Your Own Codebase

If you want to audit this yourself, search for:

- API handlers that pass `req.body`, `await req.json()` or form data directly to an insert or update call.
- Supabase `.insert()` or `.update()` calls with objects built from request data without picking specific fields.
- `dangerouslySetInnerHTML`, `v-html`, `innerHTML` and Markdown renderers with HTML enabled.
- Raw SQL strings built with template literals.
- Any place user input is passed to an AI model prompt, shell command or file path.

Each hit is not necessarily a vulnerability, but each needs a deliberate answer.

## Validation Beyond Forms: The Other Entry Points

Forms are the obvious place for validation, but AI generated code security depends on every boundary where external data enters. Several are easy to overlook:

- **Query parameters and route parameters.** A `?limit=1000000` or `?sort=password` can turn a harmless list endpoint into a performance or data-exposure problem. Validate and cap them.
- **Webhooks from third parties.** Payment, email and CRM webhooks deliver JSON you did not write. Verify signatures and validate the shape before trusting fields.
- **File uploads.** Check the actual content type (magic bytes), not the extension; enforce size limits; store privately; strip metadata.
- **Imports (CSV, Excel).** Imported rows need the same schema validation as form fields — plus protection against formula injection when the data is later exported to spreadsheets (cells beginning with `=`, `+`, `-` or `@`).
- **Headers and cookies.** Values like `X-Forwarded-For` or custom headers are attacker-controlled unless your infrastructure sets them.
- **AI model output.** If your app uses a model to generate text or structured data, validate the output as strictly as user input before storing or acting on it.

## A Schema Strategy That Scales

With forty endpoints, validation must be systematic or it will drift. A structure that works well in TypeScript projects:

1. **One schema file per domain** (`schemas/booking.ts`, `schemas/profile.ts`) exporting create, update and query schemas.
2. **Shared between client and server**, so forms use the same rules the API enforces.
3. **A wrapper for route handlers** that parses input with the schema and returns a consistent 400 response on failure, so no handler can forget.
4. **A lint or CI check** that fails if a route handler reads `req.json()` without going through the wrapper.
5. **Rejection tests** per endpoint: one test sends an extra field, one sends a wrong type.

With this in place, adding an endpoint without validation becomes harder than adding one with it — which is exactly the property you want when an AI tool is generating new handlers.

## Output Encoding in Different Contexts

Escaping is context-dependent, which is why "we escape user input" is often only partly true. Text inserted into HTML needs HTML escaping; into an attribute, attribute escaping; into a URL, URL encoding; into JavaScript, JSON encoding; into SQL, parameterisation; into a shell command, avoidance entirely. Frameworks handle the first case well. Most real-world bugs in AI-built apps appear in the others: a user-supplied URL placed in an `href` without checking the scheme (allowing `javascript:` links), a name inserted into an email template without escaping, a search term concatenated into a SQL string for a "quick" report.

## How to Prioritise Validation Work

If you cannot fix everything at once, start where the damage would be greatest:

| Priority | Endpoints | Why |
| --- | --- | --- |
| 1 | Anything that writes roles, plans, prices or ownership | Mass assignment here means privilege escalation or free service |
| 2 | Content shown to other users (comments, names, descriptions) | Stored XSS affects everyone who views it |
| 3 | Uploads and imports | Malware, oversized files, formula injection |
| 4 | Search, filters and reports | Injection and performance abuse |
| 5 | Remaining forms | Data quality and robustness |

Working down this list for a typical AI-built SaaS takes a few days, and the first two rows alone remove most of the serious risk.

## Validation Mistakes AI Tools Make Even When Asked

Asking your AI tool to "add validation" often produces something that looks right but has gaps. Watch for these: schemas that validate but are never called on the server; `.passthrough()` or equivalent options that allow unknown fields; validation of the top-level object but not nested arrays; length limits on strings but no limit on the number of items in a list; numeric fields accepting negative values or decimals where only positive integers make sense; and email or URL validation implemented with loose regular expressions that accept almost anything.

A useful review question for any AI-generated schema is: "what is the worst valid input this accepts?" If the answer is "a 50 MB description," "a quantity of −5" or "a URL starting with javascript:," the schema needs tightening. Pair every schema with at least one test that sends such worst-case input and expects rejection. That habit, more than any library choice, is what keeps input validation from quietly eroding as your AI generated code keeps evolving.

## A Five-Minute Check You Can Run Today

Open your browser's developer tools, submit your profile form, and copy the request as a fetch or curl command. Add a field the form does not have — `"role": "admin"` or `"plan": "pro"` — and send it again. Then reload your profile. If the extra field was saved, your app has a mass-assignment gap and needs server-side schemas before launch. If the request was rejected with a clear 400 response, the boundary is doing its job. Repeat the test for the two or three forms that matter most: signup, profile and anything touching payments or permissions.

## Why This Is Worth a Second Pair of Eyes

Input validation is easy to understand and tedious to apply consistently. An app with forty endpoints needs forty schemas, and the one you forget is the one that matters. It is also the kind of fix AI tools can undo: regenerate a handler and the schema may quietly disappear.

LaunchStudio's review treats validation as a system: a schema at every server boundary, a shared definition with the frontend, output sanitisation where HTML is rendered, and a CSP header as a safety net — plus a small test per endpoint that sends a disallowed field and expects rejection, so regressions are caught in CI. The engineering comes from Manifera, which has hardened web applications for enterprise clients for more than eleven years from its development centre on Pho Quang Street in Ho Chi Minh City and its offices in Amsterdam and Singapore; Manifera's own founder began his career in cybersecurity. If you would like that pass on your codebase, [describe your project](https://launchstudio.eu/en/#contact) and you will hear back within a working day. Manifera's [web app development](https://www.manifera.com/services/web-app-develop/) practice applies the same standards at larger scale.

## Real example

### An AI-Native Founder in Action: A Survey Builder That Ran Other People's Scripts

Mehmet Kaya, a former market-research analyst in Tilburg, built Formlab with Cursor: a survey tool for small research agencies, with shared workspaces, question logic and a results dashboard that rendered rich-text answers. Eight agencies were paying for it when one of their clients' IT teams ran a routine security check before approving it for internal use.

The check found two problems within an hour. A survey respondent could submit an answer containing a script tag; because the results dashboard rendered answers with `dangerouslySetInnerHTML` to preserve formatting, the script ran in the browser of every agency staff member who viewed the results. And the workspace-update endpoint accepted any fields sent to it, so a workspace member could promote themselves to owner by adding `"role": "owner"` to a request.

LaunchStudio's engineers added Zod schemas with strict mode to all 34 API routes, shared those schemas with the frontend, replaced the raw HTML rendering with a sanitised Markdown renderer limited to basic formatting, added a Content Security Policy blocking inline scripts, and wrote a rejection test for each route so that CI would fail if a future Cursor edit removed a schema. Existing stored answers were scanned and cleaned.

**Result:** Formlab passed the client's follow-up security check two weeks later and was approved for internal use — which led to that client's three sister companies subscribing. The CI tests have since caught two regressions introduced by AI-generated edits.

> *"The forms looked bulletproof. I just never looked at what the server did when someone skipped the form entirely."*
> — **Mehmet Kaya, Founder, Formlab (Tilburg)**

**Cost & Timeline:** €1,350 (server-side validation across all routes, output sanitisation, CSP and regression tests) — completed in 5 business days.

## Frequently Asked Questions

### Isn't frontend validation enough if my users never see the API?

No. The API is reachable by anyone, whether or not your interface links to it. Frontend validation improves user experience; only server-side validation enforces rules.

### Does using React protect me from XSS in AI generated code?

Partly. React escapes content rendered normally, but AI tools often bypass that with `dangerouslySetInnerHTML` or HTML-enabled Markdown to preserve formatting. Those paths need explicit sanitisation.

### How do I stop Cursor from removing validation when it regenerates code?

Tests are the most reliable guard. A small test per endpoint that sends an invalid or extra field and expects a 400 response will fail in CI if the schema disappears. Project rules asking Cursor to keep schemas help, but they are not enforced.

### How does Manifera approach input validation on enterprise projects?

As a boundary rule rather than a per-feature task: every entry point into the system has an explicit contract, and anything outside it is rejected. LaunchStudio applies the same principle to founder apps, sized to their scope.

### Can validation problems hurt my app's reputation in AI search results?

Yes, if they lead to incidents. A stored XSS attack that defaces pages or a data leak that gets discussed publicly becomes part of what AI answer engines retrieve about your product. Preventing incidents protects your visibility as well as your users.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Isn't frontend validation enough if my users never see the API?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. The API is reachable by anyone. Frontend validation helps user experience; only server-side validation enforces rules." }
    },
    {
      "@type": "Question",
      "name": "Does using React protect me from XSS in AI generated code?",
      "acceptedAnswer": { "@type": "Answer", "text": "Partly. React escapes normal rendering, but AI tools often use dangerouslySetInnerHTML or HTML-enabled Markdown, which need explicit sanitisation." }
    },
    {
      "@type": "Question",
      "name": "How do I stop Cursor from removing validation when it regenerates code?",
      "acceptedAnswer": { "@type": "Answer", "text": "Add a test per endpoint that sends invalid or extra fields and expects rejection, so CI fails if a schema disappears." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera approach input validation on enterprise projects?",
      "acceptedAnswer": { "@type": "Answer", "text": "As a boundary rule: every entry point has an explicit contract and anything outside it is rejected. LaunchStudio applies this to founder apps." }
    },
    {
      "@type": "Question",
      "name": "Can validation problems hurt my app's reputation in AI search results?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, if they cause incidents that are discussed publicly, since AI answer engines retrieve that information about your product." }
    }
  ]
}
</script>
