---
Title: "Supabase Security: The Key That Must Never Reach a Browser"
Keywords: supabase security, service role key exposure, ai app security, secrets in frontend code, edge functions server side, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Supabase Security: The Key That Must Never Reach a Browser

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Supabase Security: The Key That Must Never Reach a Browser",
  "description": "Why the service role key bypasses every access rule you wrote, the specific ways AI coding tools put it in client code, how to check your own app in ten minutes, and what a proper fix looks like.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-06",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/supabase-service-role-key-exposure-risk" }
}
</script>

Around 45% of AI-generated code ships with a security vulnerability of some kind. That statistic gets quoted a lot, and it is abstract enough to ignore. Here is the concrete version: there is one specific string in a Supabase project that turns every access rule you carefully wrote into decoration, and the fastest way to make a stubborn permission error disappear is to put that string into your app.

It works. The error stops. And now every visitor to your site is carrying administrative access to your database in their browser.

This article is about that key: what it does, the three routes by which it ends up in client code, how to check your own project in about ten minutes, and what the fix actually involves.

## Two Keys, Two Completely Different Jobs

A Supabase project issues more than one API key, and the distinction between them is the whole subject.

**The public key** — the one your frontend is supposed to use — identifies your project. It carries no privileges of its own. Every request made with it is evaluated against your row level security policies, which is why those policies matter so much. If your policies are right, this key is safe in a browser. It is meant to be there.

**The service role key** is the opposite. It is designed for trusted server-side code, and it **bypasses row level security entirely**. Every policy you wrote about who can read what simply does not apply to requests made with it. It can read every row in every table, modify anything, and delete anything.

The mental model that helps: the public key is a visitor badge that gets checked at every door. The service role key is the master key that opens all of them without being looked at.

## Why It Ends Up in the Frontend Anyway

Nobody decides to publish an administrative key. It arrives by one of three routes, all of them mundane.

**Route one: debugging by escalation.** Your app throws a permission error. It is late, the policy logic is confusing, and somewhere in a forum answer or an AI suggestion is the line "try the service role key." You swap it in, the error vanishes, and you move on to the next feature, because it works. The swap is never reverted, because nothing draws attention to it again.

**Route two: the AI fixes the symptom.** Ask a coding assistant to resolve a row-level-security error and it will often produce working code. Working is not the same as correct. Tools like Lovable, Bolt and Cursor optimise for making your app run, and a client-side call using a privileged key runs beautifully. The tool has no way to weigh "this works" against "this exposes the database," because only one of those is visible in the output.

**Route three: environment variable confusion.** Frontend build systems expose some environment variables to the browser deliberately — that is how your public key gets there — usually signalled by a prefix in the variable name. Put a secret in a variable with that prefix and it is bundled into the JavaScript your users download. The variable *looks* like a server-side secret, sitting in a `.env` file. It is not. It is on the internet.

## What an Attacker Actually Does With It

This is not theoretical, and the effort required is low.

Any visitor can open the browser's developer tools and read the JavaScript your site serves. Searching that bundle for a key pattern takes seconds. Once someone holds a service role key, the automatically generated Supabase API is at their disposal: read the entire users table, export every record, modify rows, drop data.

There is no login required, no exploit chain, and no clever technique. The credential was handed out with the page.

Two aggravating details are worth knowing. First, if the key was ever committed to a public repository, it may be indexed and discoverable even after removal — deleting it from the current code does not retrieve the copies. Second, activity performed with a service role key is indistinguishable from legitimate server activity in most logs, which means you may have no way to determine what was accessed and when. That matters directly under GDPR, where a personal data breach can require notifying the supervisory authority within 72 hours of becoming aware of it — and "we cannot determine what was accessed" is a painful sentence to put in that notification.

## Check Your Own App in Ten Minutes

You do not need tooling for a first pass.

**Open your live site, then open your browser's developer tools and view the page source or the network tab.** Search the loaded JavaScript for the word `service_role`, and for a long token beginning with `eyJ`. Supabase keys are JSON Web Tokens and all start that way, so you may legitimately find your public key. If you find two distinct long tokens, look closely at both.

**Decode what you find.** Paste the token into any JWT decoder; the payload includes a `role` claim. `anon` is expected. `service_role` in a browser bundle is an emergency.

**Search your codebase.** Look for `SERVICE_ROLE`, `service_role`, and any environment variable holding a key that is also prefixed for client exposure — the prefix varies by framework, but if the variable is visible to the browser and holds a secret, that is the bug.

**Check your git history, not just your current files.** A key removed in a later commit still lives in earlier ones.

If you find an exposed key: rotate it immediately in the Supabase dashboard, which invalidates the old one. Then fix the code that needed it, because rotation alone will simply break whatever was relying on it.

## What the Correct Architecture Looks Like

The operations that genuinely need elevated privileges — sending a receipt after payment, running an admin report, processing a webhook, aggregating data across users — are real. They just belong somewhere the user cannot see.

**Server-side functions.** Supabase Edge Functions, or an API route in your own backend, hold the service role key as a genuine server secret. Your frontend calls the function with the user's normal session, the function checks who the user is and what they are allowed to do, and only then performs the privileged operation.

**Policies for everything else.** Ninety percent of what founders reach for the service role key to accomplish is achievable with a correctly written row level security policy and the public key. Reaching for the master key is usually a signal that a policy is wrong, not that privileges are needed.

**Secrets management, not `.env` files in the repository.** Keys live in your hosting platform's secret storage or Supabase's function secrets, never in committed files, and never in variables marked for client exposure.

**Rotation as routine.** Keys should be rotatable without heroics: one place to change them, a deploy, done. If rotating a key means hunting through six files, that itself is a finding.

## The Wider Pattern This Belongs To

Exposed credentials are the most common single finding when an AI-built application comes in for review, and the reason is structural rather than careless. AI coding tools are exceptional at producing something that runs and have no model of an adversary. They do not ask who else can read this, what happens if someone changes that number in the request, or whether this key belongs on this side of the network boundary.

That is the gap LaunchStudio was built around: keeping the frontend you made, and putting a defensible backend underneath it. Concretely, for this class of problem, that means auditing every credential in the codebase and git history, rotating what is compromised, moving privileged operations into server-side functions, writing the row level security policies that should have made the master key unnecessary, and testing the result by attempting to read another user's data as a logged-in user — [the Launch Ready work](https://launchstudio.eu/en/#packages), done by Manifera engineers who have been securing production systems for eleven years.

If you found something alarming in the ten-minute check above, [talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact) — we reply within one business day, and rotating a key today is considerably cheaper than a disclosure letter next month.

## Rotating Without Taking Your App Down

Founders often delay rotation because they are afraid of breaking the live product. The sequence below avoids that, and it takes under an hour for a small app.

**Find every place the key is used first.** Search the codebase, the deployment platform's environment variables, any serverless function configuration, and any scheduled job or webhook handler. Rotating before you know where it lives is what causes the outage people fear.

**Fix the architecture before you rotate, not after.** If a client-side call depends on the privileged key, rebuild that call as a server-side function using the user's session. Deploy it. Confirm the app works with the new path while the old key is still valid.

**Then rotate, and update the legitimate server-side locations** — your function secrets and your hosting platform's secret storage — in the same maintenance window.

**Verify by failing deliberately.** Load your site, open developer tools, and search the bundle again. Confirm the old key no longer works by attempting a request with it from outside your app.

**Finally, prevent recurrence.** A build-time check that scans the client bundle for privileged tokens turns this from a thing you remember into a thing the pipeline enforces — which matters, because the original mistake is always made under time pressure at the end of a long day.

## Real example

### An Invoicing Tool Whose Admin Key Shipped to Every Customer

Thomas de Wit built Factuurly, a lightweight invoicing tool for Dutch freelancers, largely in Cursor with a Supabase backend. It had about 180 paying users when he asked for a pre-scaling review, mainly because he wanted advice on database performance.

The performance was fine. What the review found was that a single client-side module used the service role key to fetch invoice totals for a dashboard widget — added months earlier to resolve a permissions error and never revisited. Every one of those 180 users had been served a key granting full read and write access to a database containing other freelancers' client names, addresses and unpaid invoice amounts. The key was also present in the repository's history, which had briefly been public.

The remediation ran five business days: key rotated immediately, the dashboard widget rebuilt as an Edge Function that verifies the caller's session before aggregating only their own data, row level security policies written and tested across all invoice tables, git history cleaned, secrets moved into managed storage, and a test added that fails the build if a `service_role` token appears in any client bundle.

Because access logs could not distinguish legitimate server calls from potential misuse, Thomas took legal advice on his notification obligations rather than guessing — which is the correct order of operations, and the reason the engineering fix is only half the story.

**Result:** No evidence of misuse was found, the exposure was closed inside a week, and the build-time check has since caught one further attempt to reintroduce a privileged key during a feature sprint.

> *"It was three lines of code I wrote at midnight to make a red error go away. It sat in production for seven months handing out admin access to everyone who loaded my dashboard."*
> — **Thomas de Wit, Founder, Factuurly (Utrecht)**

**Cost & Timeline:** €1,900 (security remediation: key rotation, Edge Function rebuild, policy authoring and CI check) — completed in 5 business days.

## Frequently Asked Questions

### How do I tell the two Supabase keys apart?

Decode the token — both are JSON Web Tokens and carry a `role` claim in the payload. `anon` is the public key and belongs in your frontend. `service_role` bypasses all row level security and must only exist in server-side environments.

### I rotated the key. Am I done?

Not quite. Rotation stops the old key working, but whatever code depended on it will now fail, and the underlying design problem remains. You still need to move the privileged operation server-side or replace it with a correct policy, and to check git history for other copies.

### Can I use the service role key if my app is only used internally?

It is still a bad idea. "Internal" apps get shared links, screenshots and browser extensions, and the key grants unrestricted access to everything. Use a server-side function with the user's session checked, even for ten colleagues.

### Why did my AI tool suggest using it?

Because it resolves the error you asked about. Coding assistants optimise for code that runs, and a privileged client-side call runs perfectly. Security requires reasoning about an adversary who is not present in your prompt, which is precisely what these tools do not do.

### What should I do if the key was in a public repository?

Assume it is compromised regardless of how briefly it was exposed, rotate immediately, and review what data was accessible. Because service role activity is hard to distinguish from legitimate server traffic in logs, take legal advice on notification obligations rather than concluding on your own that nothing happened.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do I tell the two Supabase keys apart?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Decode the token — both are JSON Web Tokens carrying a role claim. The anon role is the public key and belongs in the frontend; the service_role key bypasses all row level security and must only exist server-side."
      }
    },
    {
      "@type": "Question",
      "name": "I rotated the key. Am I done?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not quite. Rotation stops the old key working, but the code that relied on it will fail and the design problem remains. Move the privileged operation server-side or replace it with a correct policy, and check git history for other copies."
      }
    },
    {
      "@type": "Question",
      "name": "Can I use the service role key if my app is only used internally?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It is still a bad idea. Internal apps get shared links, screenshots and browser extensions, and the key grants unrestricted access. Use a server-side function that checks the user's session, even for a small team."
      }
    },
    {
      "@type": "Question",
      "name": "Why did my AI tool suggest using it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because it resolves the error being asked about. Coding assistants optimise for code that runs, and a privileged client-side call runs perfectly. Security requires reasoning about an adversary who is not present in the prompt."
      }
    },
    {
      "@type": "Question",
      "name": "What should I do if the key was in a public repository?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Assume it is compromised regardless of exposure time, rotate immediately and review what data was reachable. Because service role activity is hard to distinguish from legitimate traffic in logs, take legal advice on notification obligations."
      }
    }
  ]
}
</script>
