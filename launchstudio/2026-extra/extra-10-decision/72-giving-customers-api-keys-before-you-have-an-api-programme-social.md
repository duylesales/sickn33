🚨 Daan Verhoeven generated an API key for a customer in five minutes flat. Eleven months and four customers later, one of those keys could have deleted an entire product catalogue. 😳

Handing out an API key feels like a five-minute favour — it's actually a permanent commitment you haven't priced in: 🧠

❌ All four keys were stored in plain text, so anyone with database access held working credentials to four customer accounts
❌ Keys carried no scope — one meant to update stock levels could just as easily delete products, change prices, or remove users
❌ With no rate limits, one customer's retry loop quietly generated around 40,000 requests an hour for three weeks
❌ Two of the four keys hadn't been used in over six months, from integrations nobody had bothered to revoke

✅ Hash keys like passwords, show the full key once at creation, and store only a short prefix for identification
✅ Default every key to read-only, and never let a key exceed the permissions of the account it belongs to
✅ Set a per-key rate limit with a lower ceiling on expensive endpoints, and return a clear 429 when it's hit
✅ Version the API path and commit in writing to notice before breaking changes

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we set up API key storage, scoping, and rate limits before that first key ever leaves your hands. 🔑

His result: all four keys hashed and rotated, scoped access in place, and the mysterious periodic slowness he'd been chasing separately simply disappeared. 🚀

👉 Find out what your first API key is really promising: [Link to article]

#API #SaaS #DevSecurity #IndieHacker #LaunchStudio #Manifera
