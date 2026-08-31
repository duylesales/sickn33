🚨 "By the way, I can see your OpenAI key in the page source." A beta tester said it in passing. Three weeks of exposure had already cost $340 in unauthorized charges he didn't know about. 😳

Press F12. Search "sk_" or "key" across your loaded files. If you find a live credential, so can everyone else who's ever visited your site. 🧠

❌ `NEXT_PUBLIC_` and `VITE_` prefixes bundle whatever they're attached to straight into the browser — visible to anyone
❌ AI tools see a credential used in a frontend component and decide it needs to be public — technically consistent, catastrophically wrong
❌ Stripe secret keys, OpenAI keys, database connection strings, email API keys all turn up exposed in AI-generated frontend bundles
❌ Automated bots scan public repos and deployed apps continuously — a leaked key can be exploited within minutes to hours

✅ Sensitive API calls moved server-side, behind a Supabase Edge Function the frontend calls instead
✅ The OpenAI key held only in server-only environment variables — never bundled, never visible
✅ Full audit catching three more exposed credentials: a SendGrid key, a database admin password, a webhook signing secret
✅ Fixed in 3 business days for less than the cost of the unauthorized charges themselves

At **LaunchStudio**, backed by Manifera engineers who've found exposed keys in the majority of AI-generated codebases they've reviewed, the check takes minutes and the fix is fast. 🔍

His result: $340 in OpenAI charges was the total cost of the lesson — zero credentials left exposed after the restructure. 🚀

👉 Send us your repository and we'll tell you which credentials are visible right now: [Link to article]

#LaunchStudio #Manifera #APIKeySecurity #VibeCoding #IndieHacker #MVPSecurity #CursorAI
