---
Title: "Is the Supabase Anon Key Safe to Expose in My App?"
Keywords: is supabase anon key safe, supabase anon key public, supabase publishable key, supabase service role key, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: Technical Solo Founder / Indie Hacker
---

# Is the Supabase Anon Key Safe to Expose in My App?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Is the Supabase Anon Key Safe to Expose in My App?",
  "description": "The Supabase anon (publishable) key is designed to be public, but it is only safe when Row Level Security is correct. This article explains the difference between anon, publishable, service role and secret keys, what an attacker can do with each, and how to check your app.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-05",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/is-the-supabase-anon-key-safe" }
}
</script>

**Short answer:** yes, the Supabase anon key is designed to be public, and it is normal to see it in your app's frontend code. But it is only safe if your Row Level Security policies are correct. The anon key lets anyone talk to your database as an anonymous or logged-in user; RLS decides what they can actually do. The key that must never be exposed is the **service role key** (or the newer **secret key**), which bypasses RLS completely.

## The Keys, Side by Side

Supabase has used two generations of key naming. Both appear in current projects:

| Key | Also known as | Where it belongs | What it can do |
| --- | --- | --- | --- |
| anon key | publishable key (`sb_publishable_...`) | Browser, mobile apps | Whatever your RLS policies allow for anonymous or logged-in users |
| service role key | secret key (`sb_secret_...`) | Server only: edge functions, backend, CI | Everything, bypassing RLS |

The anon key is like the front door of a building with a reception desk. Everyone can walk in; the reception (RLS) decides where they may go. The service role key is a master key that opens every door without asking reception.

## What Someone Can Do With Your Anon Key

With your project URL and anon key, which anyone can find in your frontend, a person can:

- Call your database API directly, without your app's interface
- Sign up and log in as a user, if sign-ups are open
- Read, insert, update or delete rows **exactly as far as your RLS policies allow**
- Call database functions exposed to the anon or authenticated roles
- Access storage objects permitted by storage policies

If RLS is correct, this is harmless: they can do what any user of your app can do. If RLS is missing or too permissive, the anon key becomes the way in. That is why "the anon key leaked" is almost never the real problem. The real problem is RLS.

## What Someone Can Do With the Service Role Key

Everything. Read every table, change any row, delete data, create admin users, access all storage. If this key appears in your frontend, your repository or your logs, treat it as an incident:

1. Rotate or revoke the key in your Supabase project settings immediately
2. Move every operation that needed it into an edge function or backend
3. Check logs for unusual activity since the exposure
4. Consider whether a data breach notification is required under the GDPR

## How to Check Your App in Five Minutes

1. **Find the key in your frontend.** Open developer tools, search loaded scripts for `supabase` or your project URL. Note which key is there.
2. **Decode it if it is a JWT.** Legacy keys are JWTs; paste it into a JWT decoder and check the `role` claim. `anon` is fine. `service_role` is an emergency.
3. **If it starts with `sb_`,** check the prefix: `sb_publishable_` is fine in the browser, `sb_secret_` is not.
4. **Check RLS status.** In the Supabase dashboard, every table in exposed schemas should have RLS enabled.
5. **Test as a user.** Log in as two different users and try to read each other's data. Our [Lovable security self-test](https://launchstudio.eu/en/blog/is-my-lovable-app-secure) walks through this.

## Common Misunderstandings

**"I'll hide the anon key in an environment variable."** Environment variables prefixed for the frontend, such as `VITE_` or `NEXT_PUBLIC_`, are bundled into the browser code. They are configuration, not secrets. That is fine for the anon key and wrong for anything secret.

**"I'll put the service role key in the frontend just for the admin page."** The admin page's code is downloaded by every visitor. Use an edge function that checks the caller is an admin, then performs the privileged action server-side.

**"RLS is enabled, so I'm safe."** Enabled with a policy of `using (true)` protects nothing. What matters is what the policies say.

## Production Setup We Recommend

- Anon or publishable key in the frontend, service role or secret key only in server environments
- RLS enabled on every exposed table, with policies tested using real user sessions
- Privileged actions in edge functions that verify the caller
- Keys rotated whenever a team member with access leaves
- Secrets scanned out of the git history

LaunchStudio sets this up as part of Supabase production work, typically within a Launch Ready package between €800 and €3,500. LaunchStudio is powered by Manifera, a software development company with 11+ years of experience and a development centre in Ho Chi Minh City, coordinated with clients from Amsterdam. More on the team at [Manifera's about page](https://www.manifera.com/about-us/). Supabase's own explanation of [API keys](https://supabase.com/docs/guides/api/api-keys) is the authoritative reference.

## Real example

### An AI-Native Founder in Action: The Festival Volunteer App With a Master Key in the Bundle

Olivier Maes coordinates volunteers for a music festival near Leuven and built Shiftwissel with Bolt and Supabase: volunteers pick shifts, swap them with each other and receive their wristband details. About 600 volunteers signed up within two weeks.

A volunteer with a development background messaged Olivier: the app's JavaScript contained a key whose decoded role was `service_role`. Bolt had used it to make the "swap shift" feature work, because the anon key's policies did not allow one volunteer to update another's shift. With that key, anyone could read every volunteer's phone number and address, or delete the whole shift schedule.

LaunchStudio rotated the key within the hour and checked the logs for unusual access, finding none beyond the volunteer's own test. Engineers then moved the swap logic into an edge function that verified both volunteers had agreed, enabled RLS on all tables with policies letting volunteers read only their own details and the public shift schedule, and set up a staging project for further changes.

**Result:** Shiftwissel handled about 1,100 shift swaps during the festival without incident. Olivier informed volunteers about the fix transparently, and the festival's organisers adopted the app for the following year.

> *"The anon key was in the code because it should be. The other key was in the code because the AI needed a shortcut. I didn't know there was a difference."*
> - **Olivier Maes, Founder, Shiftwissel (Leuven)**

**Cost & Timeline:** €1,350 (key rotation, log review, edge function for swaps, RLS and staging) - completed in 4 business days.

## Frequently Asked Questions

### Should I hide the Supabase anon key?

No, you cannot meaningfully hide it, and you do not need to. Any key used by browser code is visible to users. The anon or publishable key is designed for this. Spend the effort on correct Row Level Security instead.

### What is the difference between the anon key and the publishable key?

They serve the same purpose. The publishable key (`sb_publishable_...`) is Supabase's newer key format, and the anon key is the legacy JWT-based equivalent. Both are safe in the browser with correct RLS. Their secret counterparts are the service role key and the secret key.

### What should I do if my service role key was exposed?

Rotate or revoke it immediately in the Supabase dashboard, move any code that used it to a server environment, review logs for suspicious activity and assess whether personal data was accessed. Under the GDPR, a reportable breach must be notified within 72 hours.

### Why does Manifera treat key handling as a priority in AI-built apps?

Because exposed secret keys turn every other security measure into decoration. Manifera's 11+ years of enterprise delivery, and Herre Roelevink's cybersecurity background, put secrets management at the top of every review, before any feature work.

### Can an exposed key affect how search engines treat my site?

Indirectly. A compromised database can be used to inject spam or malicious content into your pages, which can get your site flagged or de-indexed. Keeping secret keys off the frontend helps prevent that.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should I hide the Supabase anon key?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. Browser keys are always visible and the anon or publishable key is designed for that. Focus on correct Row Level Security." }
    },
    {
      "@type": "Question",
      "name": "What is the difference between the anon key and the publishable key?",
      "acceptedAnswer": { "@type": "Answer", "text": "Same purpose: the publishable key is the newer format, the anon key the legacy JWT. Their secret counterparts are the service role and secret keys." }
    },
    {
      "@type": "Question",
      "name": "What should I do if my service role key was exposed?",
      "acceptedAnswer": { "@type": "Answer", "text": "Rotate it immediately, move code using it server-side, review logs and assess personal data access; reportable GDPR breaches must be notified within 72 hours." }
    },
    {
      "@type": "Question",
      "name": "Why does Manifera treat key handling as a priority in AI-built apps?",
      "acceptedAnswer": { "@type": "Answer", "text": "Exposed secret keys nullify other security measures. Manifera's 11+ years of delivery and Herre Roelevink's cybersecurity background put secrets management first." }
    },
    {
      "@type": "Question",
      "name": "Can an exposed key affect how search engines treat my site?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirectly. A compromised database can inject spam or malicious content, leading to flagging or de-indexing." }
    }
  ]
}
</script>
