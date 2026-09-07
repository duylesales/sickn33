---
Title: "EdTech Prototypes: Launching Into Schools and the Minors Problem"
Keywords: edtech prototype compliance, student data protection EU, school procurement requirements, parental consent minors app, age verification edtech, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# EdTech Prototypes: Launching Into Schools and the Minors Problem

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "EdTech Prototypes: Launching Into Schools and the Minors Problem",
  "description": "A practical guide to the parental consent, age verification, and school procurement requirements that apply the moment an AI-built education product is used by minors, and why a prototype that impressed one teacher can still fail a school's data protection review. Helps non-technical founders decide what to fix before pitching a school.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-02-07",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/edtech-prototypes-launching-into-schools-and-the-minors-problem" }
}
</script>

Who is your actual customer: the child using the app, the teacher who found it, or the school that has to approve it? Most edtech founders answer this question wrong on their first pitch, and the wrong answer is expensive, because the school's data protection officer is going to ask it whether or not you've prepared an answer.

This distinction matters more in edtech than almost anywhere else, because your real buyer — the institution — has legal obligations toward the users of your product that neither you nor your users chose. A school signing off on a classroom app isn't just evaluating whether it's useful. It's accepting responsibility, on behalf of parents and a regulator, for what happens to the data of children who are, in the eyes of GDPR, a category the law explicitly asks controllers to protect with extra care.

## Why a Teacher Loving Your App Isn't the Same as a School Approving It

AI-native founders building edtech products often validate with a single enthusiastic teacher, get a class using the product informally, and assume institutional adoption will follow the same path — show it, they'll love it, they'll sign up. Schools rarely work that way for anything that touches student data. Individual teachers can pilot tools informally, but formal procurement, once it starts, typically routes through a data protection impact assessment, a review of where data is hosted and by whom, and in many EU countries a requirement that the school (not the vendor) remains the data controller, with your product acting only as a processor under a signed agreement.

This reframes the entire relationship. It's not "sell the school a subscription." It's "become an approved processor the school is willing to be accountable for." That's a materially different sales and product conversation, and most AI-generated prototypes are built with zero awareness that this second conversation exists at all.

## The Consent Problem That Doesn't Have a Simple Checkbox Answer

Under GDPR, a child below a certain age (member states can set this between 13 and 16, with 16 as the default absent a lower national rule) generally cannot give valid consent to data processing based on consent alone — a parent or guardian typically has to consent on the child's behalf when consent is the lawful basis being relied on. But most edtech products used inside a school don't actually rely on consent as their lawful basis at all: the processing is usually grounded in the school's own legal basis for educating the child (often public interest or a legal obligation, depending on the member state and school type), with your product processing data on the school's instruction as a processor.

This is the detail that trips up founders who build a "sign up with a parent's email" flow, assuming that solves consent, and then discover the school's DPO wants a data processing agreement instead — because inside an institutional context, individual parental consent per feature usually isn't the right mechanism, and building a consent-collection flow when what's actually needed is a signed processor agreement wastes real engineering time on the wrong problem. Which mechanism applies depends on the country, the school type, and exactly what data your product touches — genuinely a case where a specialist conversation with someone who knows the applicable national implementation is worth having before you build the onboarding flow, not after.

## Age Verification: The Feature Almost No Prototype Actually Has

If any part of your product is used directly by children outside a school-mediated context — a consumer learning app downloaded by a 10-year-old, a homework helper a teenager signs up for alone — you need a genuine age-assurance mechanism, not a birthdate field a child can type any number into. AI-generated onboarding flows almost universally implement the latter: a date-of-birth input with no verification behind it, which satisfies a form validation rule and nothing else.

Real age assurance is a spectrum, not a single implementation. For lower-risk products, a combination of self-declaration plus parental email verification (sending a confirmation link to a parent's address before activating a minor's account) is a reasonable, proportionate approach many edtech products use. For anything higher-risk — products involving direct messaging between users, public profiles, or content moderation gaps — regulators increasingly expect more robust age-assurance measures, and this is an area of EU digital regulation that continues to evolve, so treat any specific implementation as something to validate against current guidance rather than something this article can finalize for you.

## Data Residency and the School Procurement Checklist

EU schools and school boards increasingly ask a specific, answerable set of questions before approving a tool, and it's worth having written answers ready before the first procurement conversation rather than improvising them under a deadline. Where is student data physically hosted, and by whom? Is there a signed data processing agreement available, naming sub-processors? Is data deleted when a student leaves the school or graduates, and how quickly? Can the school export a student's full data on request? Is there a named contact for a data protection query?

Almost none of this exists by default in an AI-generated prototype. Hosting is wherever the AI tool's default deployment put it. There's no sub-processor list because nobody made one. There's no deletion workflow because "delete account" wasn't in the original prompt. Building these five answers — genuinely, not performatively — is usually a two-to-three-week engineering task, and it is the actual gate between a product a teacher likes and a product a school can legally purchase.

Larger school boards and municipal education authorities in the Netherlands and elsewhere increasingly run a shared procurement framework across multiple schools rather than approving vendors one school at a time, which means passing one board's review can open several schools at once — but it also means the review is typically more thorough than an individual school's, often including a formal privacy impact assessment template the board expects filled in with specifics, not marketing language. Founders who treat the first procurement review as a one-off hurdle sometimes discover the second school asks entirely different, harder questions because it sits under a different board with its own template. Asking early which framework, if any, a prospective school belongs to tells you which version of this checklist you're actually being measured against.

## What Changes in the Product Itself, Not Just the Paperwork

Beyond the compliance documentation, several product decisions change once minors are confirmed users. Data minimization becomes stricter in practice, not just in principle: a homework app doesn't need a child's home address, and collecting it "in case it's useful later" is precisely the kind of scope creep a school's DPO will flag immediately. Retention periods need explicit limits — student work and login history shouldn't persist indefinitely after a student leaves, and "we never delete anything" is a common but unacceptable default in AI-built prototypes where deletion was never implemented at all.

Communication features deserve particular scrutiny. If your product includes any messaging between students, or between students and adults who aren't their own teacher, that's a safeguarding surface, not just a feature — schools will ask how it's moderated, logged, and reportable, and "we haven't thought about it yet" ends most procurement conversations on the spot.

Account provisioning and offboarding also change shape. A consumer product lets anyone sign up and delete their own account whenever they like. A school-issued product usually needs bulk provisioning tied to the school's own roster (so a teacher isn't manually inviting thirty students one at a time every September) and bulk offboarding tied to the same roster when a class ends or a student transfers — a workflow almost no AI-generated prototype has, because it assumes individual, self-service signup as the only pattern that exists.

## Building the Case for a School Pilot Without Overbuilding First

None of this means a founder needs full institutional-grade compliance before writing a single line of code. A sensible sequence exists: validate the product's educational value informally with individual teachers first, using synthetic or clearly non-identifying data wherever possible during that phase. Once a teacher wants to bring it to their school formally, that's the trigger point — not before — to invest in the processor agreement, the hosting review, the retention policy and the deletion workflow, because that's the exact moment a school will ask for them.

Building this infrastructure speculatively, before any school has expressed real interest, risks spending a Launch Ready budget on compliance nobody asked for yet. Building it reactively, after a school's procurement officer has already asked and you have nothing, risks losing the deal to a slower-moving but better-prepared competitor. The right moment is the space between those two: when a specific school conversation has genuinely started.

## What LaunchStudio Builds and What a Specialist Needs to Confirm

LaunchStudio's engineers can implement the technical side of this properly: EU-region hosting, a real deletion and data-export workflow, retention limits enforced in the database rather than described in a policy document nobody reads, and a documented sub-processor list a school's DPO can actually review — all without rebuilding the classroom-facing product a teacher already likes. This is core Launch Ready territory, backed by Manifera's engineering team, most of whom have built systems for organisations with far stricter data-handling requirements than a single school ever will.

What we can't do, and what no development partner should claim to do, is tell you definitively which lawful basis applies in a specific EU member state, or draft the data processing agreement as a legal document a school will sign. That's a data protection lawyer's job, ideally one with specific experience in education. Get the technical foundation right first, and that legal conversation becomes a formality rather than a discovery process. [Describe your project](https://launchstudio.eu/en/#contact) and we'll reply within one business day with a clear view of what a school procurement review will actually ask you.

## Real example

### A Homework-Help App Discovers Its Real Customer Wasn't the Student

Iris Bakker built Huiswerkmaatje, an AI-assisted homework helper, in Lovable, and piloted it informally with two enthusiastic teachers and their classes in Rotterdam. When one teacher tried to bring it to her school's formal approval process, the school's data protection officer sent back a two-page questionnaire Iris had never seen before: hosting location, sub-processor list, retention policy, deletion process, and whether the product relied on parental consent or a processor agreement with the school.

The review found the prototype's Supabase project hosted outside the EU by default, no deletion workflow at all (accounts and homework history persisted indefinitely), no sub-processor list because nobody had assembled one, and an onboarding flow built entirely around collecting parental consent — the wrong mechanism, since the school needed a processor agreement instead, with the school itself remaining the data controller. The fix moved hosting to an EU region, built a genuine account-and-data deletion flow triggered by the school's own student information system, replaced the consent-collection onboarding with a lightweight parental notification screen, and produced the sub-processor list and a template data processing agreement the school's DPO could review directly.

**Result:** Huiswerkmaatje passed the school's procurement review on its second submission and is now used across four classes, with the completed compliance documentation reused for its second school pilot without rework.

> *"I built the app for the kids. I hadn't understood I also needed to build the paperwork for the school, and that the paperwork determined whether the kids ever got to use it at all."*
> — **Iris Bakker, Founder, Huiswerkmaatje (Rotterdam)**

**Cost & Timeline:** €2,900 (Launch Ready Package, EU hosting migration, deletion workflow and compliance documentation) — live in 14 business days.

## Frequently Asked Questions

### Does every edtech product need parental consent built in?

No — inside a school context, the school is usually the data controller relying on its own legal basis for educating the child, with your product acting as a processor under a signed agreement rather than collecting individual parental consent. Consumer-facing edtech used directly by children outside a school relationship is a different case and more often does need genuine parental consent or verified age-appropriate consent mechanisms.

### What's the actual age threshold for needing parental consent under GDPR?

GDPR sets 16 as the default digital consent age but allows EU member states to lower it to as young as 13 in national law, so the applicable threshold depends on which country's implementation applies to your users — this is genuinely a detail to confirm per market rather than assume.

### Can I use a school's existing student accounts (like Google Workspace for Education) instead of building my own login?

Often yes, and it's frequently the better decision — schools already trust and manage those accounts, and using single sign-on through a platform they've already vetted removes a whole category of your own authentication and data-handling burden. It does mean integrating with that provider's SSO correctly, which an AI-generated prototype rarely does out of the box.

### How long should we keep a student's data after they leave the school or stop using the product?

There's no universal number — it depends on the specific processing agreement with the school and applicable national rules — but "indefinitely by default" is the wrong answer nearly every AI-built prototype ships with. Build an explicit retention period into the schema and an actual deletion job, then confirm the specific duration with the school or a specialist.

### Should I wait until I have a signed school contract before doing any of this compliance work?

Start the technical groundwork — EU hosting, a deletion workflow, retention limits — as soon as a real school conversation begins, not after a contract is signed, because a school's procurement review typically happens before the contract, not after it. Waiting until signature means arriving at the review with nothing to show.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does every edtech product need parental consent built in?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Inside a school context, the school is usually the data controller relying on its own legal basis for educating the child, with your product acting as a processor under a signed agreement rather than collecting individual parental consent. Consumer-facing edtech used directly by children is a different case."
      }
    },
    {
      "@type": "Question",
      "name": "What's the actual age threshold for needing parental consent under GDPR?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "GDPR sets 16 as the default digital consent age but allows EU member states to lower it to as young as 13 in national law, so the applicable threshold depends on which country's implementation covers your users."
      }
    },
    {
      "@type": "Question",
      "name": "Can I use a school's existing student accounts instead of building my own login?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Often yes, and it's frequently the better decision. Schools already trust and manage those accounts, and single sign-on through an already-vetted platform removes a whole category of your own authentication and data-handling burden."
      }
    },
    {
      "@type": "Question",
      "name": "How long should we keep a student's data after they leave the school?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "There's no universal number; it depends on the specific processing agreement and applicable national rules. Build an explicit retention period into the schema and a real deletion job, then confirm the duration with the school or a specialist."
      }
    },
    {
      "@type": "Question",
      "name": "Should I wait until I have a signed school contract before doing any compliance work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Start the technical groundwork as soon as a real school conversation begins, because a procurement review typically happens before the contract is signed, not after."
      }
    }
  ]
}
</script>
