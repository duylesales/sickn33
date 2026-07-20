---
Title: "AI in IT Security: Why Founders Still Need a Human Review"
Keywords: ai in it security, security ai, ai secure, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# AI in IT Security: Why Founders Still Need a Human Review

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI in IT Security: Why Founders Still Need a Human Review",
  "description": "A myth-busting look at what AI in IT security actually automates versus what still requires human judgment, using a weak password policy in a home cleaning services app as the concrete case.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-07-29",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/ai-in-it-security-why-founders-still-need-a-human-review"
  }
}
</script>

Discussions of AI in IT security tend to focus on impressive, automated threat-detection capabilities — genuinely useful tools, but not the layer where most founder-built prototypes actually run into trouble. The trouble tends to show up somewhere much more basic: a signup form that happily accepts a password like "12345," because nothing in the original feature description ever specified it shouldn't.

## Myth: Weak Password Acceptance Is an Oversight AI Tools Would Naturally Catch

**Reality:** an AI coding tool generating a signup form implements exactly what was described — "let a user create an account with an email and password" — and if password strength requirements weren't part of that description, there's no independent judgment being applied to add them anyway. The tool isn't failing to notice a weak password policy; it simply wasn't asked to enforce one.

## Myth: Users Choosing Weak Passwords Is Primarily the User's Own Fault and Risk

**Reality:** while individual password choice is ultimately a user's decision, a platform accepting trivially weak passwords without any minimum requirement bears real responsibility too — particularly because a compromised account on a home-services platform can expose scheduling details, addresses, and payment information that affects real, physical safety, not just an abstract inconvenience.

## Myth: Credential Stuffing Only Threatens Large, High-Profile Platforms

**Reality:** credential stuffing attacks — automated attempts using passwords leaked from unrelated past breaches — are run indiscriminately against any reachable login form, regardless of platform size or fame, precisely because attackers know many people reuse passwords across services, making even a small, obscure platform a viable target for exactly this kind of automated attempt.

## Myth: A Minimum Password Length Requirement Alone Solves This

**Reality:** length alone doesn't prevent trivially weak but technically "long enough" choices, nor does it address the credential-stuffing risk of a genuinely strong but previously breached password being reused — a complete approach also considers checking against known-breached password databases and, ideally, encouraging or requiring additional protection like two-factor authentication for higher-risk actions.

## Myth: Adding Proper Password Policy Is a Major, Disruptive Change

**Reality:** implementing a sensible minimum strength requirement and checking against known-breached password lists is a well-established, narrowly scoped technical addition — it doesn't require touching the rest of a signup flow's design or user experience beyond the specific password field's validation logic.

## Getting This Right Without Overcomplicating Signup

A proper fix balances meaningful protection with a signup experience that doesn't frustrate genuine users unnecessarily — clear, specific password requirements communicated upfront, rather than vague rejection messages after the fact. [LaunchStudio](https://launchstudio.eu/en/) implements exactly this kind of balanced password policy as part of its authentication hardening work, backed by Manifera's 11+ years of experience building secure, user-friendly signup flows.

Manifera's authentication policy implementation is delivered through the Ho Chi Minh City development center on Pho Quang Street, with client conversations handled through the Amsterdam headquarters at Herengracht 420.

[Describe your product to us — we respond within one business day](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: The Account Login That Anyone Could Guess

Yara, a former cleaning service coordinator turned founder in Zeist, built SchoonBij, an AI-assisted home cleaning services booking app built with Lovable, connecting households with vetted independent cleaners and storing home addresses and scheduling details.

A concerned early user mentioned in passing that she'd used "cleaning123" as her password purely because the signup form accepted it without complaint, and asked, half-joking, whether that was actually safe. LaunchStudio's review confirmed the signup form had no password strength requirement whatsoever, and found several existing accounts using similarly trivial, easily guessable passwords.

**Result:** LaunchStudio implemented a clear minimum password strength requirement communicated upfront during signup, along with a check against known-breached password lists, and prompted existing users with weak passwords to update them, closing the exposure without disrupting SchoonBij's straightforward signup experience.

> *"She asked me almost jokingly if that was safe, and I genuinely didn't have a confident answer. It made me realize I'd never actually thought about what our signup form would and wouldn't allow."*
> — **Yara Smit, Founder, SchoonBij (Zeist)**

**Cost & Timeline:** €1,500 (password policy implementation and breach-list checking) — completed in 5 business days.

---

## Frequently Asked Questions

### Would an identity security specialist consider this a low-priority gap compared to more "technical" vulnerabilities?

No — weak password acceptance is consistently treated as a foundational, high-priority item in authentication security reviews specifically because it's the most direct, common entry point for account compromise, regardless of how much more technically involved other categories of vulnerability might sound.

### Does requiring a stronger password actually meaningfully reduce risk, or do determined attackers get around it easily?

It meaningfully reduces risk against the most common, high-volume attack methods — automated credential stuffing and simple guessing — even though it doesn't make an account literally unbreakable against a sufficiently determined, targeted attacker, which is exactly why it's one layer of protection among several, not a complete solution on its own.

### Manifera has implemented authentication systems across many different products — does that variety help strike the right balance for a specific product like SchoonBij's?

Yes, since the right balance between security and signup friction genuinely differs by context, and having implemented this trade-off across many different products helps calibrate a policy that's appropriately protective for a home-services platform without introducing unnecessary friction that would discourage genuine, often less technical users from signing up at all.

### CEO Herre Roelevink has described the founder economy as needing the same baseline rigor larger organizations have always required — does password policy fit that description?

Yes, directly — minimum password strength requirements have been standard practice at larger, security-conscious organizations for a long time, and Roelevink's stated view is bringing that same baseline expectation to founder-built products by default, rather than treating it as something only bigger companies need to bother with.

### Should a founder building with an AI coding tool proactively specify password requirements in their original prompt, or is that something to fix afterward regardless?

Proactively specifying it in the original prompt can help and is a reasonable habit to build, but relying entirely on remembering to specify every such requirement across every feature is fragile — a dedicated review afterward remains valuable as a systematic check regardless of how carefully a founder tries to prompt for it upfront.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is weak password acceptance a low-priority security gap?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, it's consistently treated as foundational and high-priority since it's the most direct entry point for account compromise."
      }
    },
    {
      "@type": "Question",
      "name": "Does requiring a stronger password meaningfully reduce risk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, against common attack methods, though it's one layer of protection among several, not a complete solution alone."
      }
    },
    {
      "@type": "Question",
      "name": "Does experience across many products help calibrate the right password policy balance?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, the right balance between security and friction genuinely differs by context and product audience."
      }
    },
    {
      "@type": "Question",
      "name": "Does password policy fit the baseline-rigor-for-founders framing the CEO describes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, minimum password strength has long been standard at larger organizations and should extend to founder products."
      }
    },
    {
      "@type": "Question",
      "name": "Should founders proactively specify password requirements when prompting AI tools?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It helps, but relying solely on remembering to prompt for it is fragile compared to a systematic later review."
      }
    }
  ]
}
</script>
