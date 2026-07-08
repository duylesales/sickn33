🏗️ "Should we use microservices?"

The most expensive question in software architecture.

In 2020: "Microservices for everything!"
In 2026: "It depends." (finally)

**The uncomfortable truth:**

Every company you admire started as a monolith:
→ Shopify — monolith serving billions
→ Stack Overflow — 100M users, one .NET app
→ Basecamp — $100M business, single Rails app

**The hidden costs nobody shows at conferences:**

15 microservices = 15 CI/CD pipelines + 15 Dockerfiles + 15 monitoring setups

Infrastructure team to maintain this: **€200K-€400K/year**

Before you write a single line of business logic.

**The decision matrix:**

👥 1-15 engineers → **Monolith** (just do it)
👥 10-40 engineers → **Modular Monolith** (best of both worlds)
👥 30+ engineers → **Microservices** (now it makes sense)

**The Modular Monolith: the 2026 sweet spot**

One deployable unit. Clear internal boundaries. Modules communicate through interfaces, not network calls.

When a module actually needs independent scaling? Extract it.

Planned evolution > Big-bang rewrite.

**Three signals it's time to decompose:**

🚨 Teams wait 2+ days to deploy because of each other
🚨 CI build exceeds 20 minutes
🚨 A bug in notifications crashes billing

See all three? Extract the worst module first.

Instagram had 13 employees and 30M users before decomposing their monolith.

Ship first. Optimise later.

#SoftwareArchitecture #Microservices #Monolith #CTO #Engineering #Manifera #SystemDesign
