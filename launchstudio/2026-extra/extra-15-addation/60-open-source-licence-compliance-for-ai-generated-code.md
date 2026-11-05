---
Title: "Open-Source Licence Compliance for AI-Generated Code"
Keywords: open source licence compliance, agpl saas risk, sbom for startups, ai generated code licensing, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Open-Source Licence Compliance for AI-Generated Code

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Open-Source Licence Compliance for AI-Generated Code",
  "description": "AI-built apps depend on hundreds of open-source packages, and AI tools sometimes reproduce code from public repositories. This guide explains open-source licence types, why copyleft licences such as the AGPL matter for SaaS, attribution obligations, the risk of reproduced snippets, software bills of materials, licence scanning and what investors and enterprise customers ask about.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-16",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/open-source-licence-compliance-for-ai-generated-code" },
  "citation": [
    { "@type": "CreativeWork", "name": "Open Source Initiative: Licenses", "url": "https://opensource.org/licenses" },
    { "@type": "CreativeWork", "name": "GNU Affero General Public License v3", "url": "https://www.gnu.org/licenses/agpl-3.0.html" },
    { "@type": "CreativeWork", "name": "SPDX specification", "url": "https://spdx.dev/" },
    { "@type": "CreativeWork", "name": "CycloneDX specification", "url": "https://cyclonedx.org/" }
  ]
}
</script>

Every app built with Lovable, Bolt, v0, Cursor or Claude Code rests on open-source software. React, Tailwind, the Supabase client, date libraries, chart components, PDF generators: hundreds of packages, each with a licence that grants you rights under certain conditions. Most of these licences are permissive and easy to comply with. A few impose obligations that can matter a great deal for a commercial product.

AI tools add a second layer. They add packages without discussing licences, and they occasionally reproduce substantial fragments of code they saw during training, which may carry licence obligations of their own. For most founders, none of this is visible until an investor's technical due diligence, an acquirer or an enterprise customer's procurement team asks for a list of licences and a statement on how open-source obligations are met.

This guide explains the essentials. It is general information, not legal advice; for transactions or specific concerns, consult a lawyer familiar with software licensing.

## Key Takeaways

- **Open-source licences fall broadly into permissive and copyleft families.** Permissive licences mainly require attribution; copyleft licences can require sharing source code under certain conditions.
- **For SaaS, the AGPL deserves particular attention,** because its obligations can be triggered by offering software over a network, not only by distributing it.
- **Attribution obligations apply even to permissive licences,** typically by including licence texts and notices.
- **AI tools may reproduce licensed code snippets.** Some tools offer filters or references to reduce and flag this.
- **A software bill of materials and licence scanning** make compliance demonstrable to customers and investors.

## Licence Families

| Family | Examples | Key obligations | Typical risk for SaaS |
| --- | --- | --- | --- |
| Permissive | MIT, BSD, Apache 2.0, ISC | Keep copyright and licence notices; Apache 2.0 adds patent terms and notice requirements | Low, if notices are kept |
| Weak copyleft | LGPL, MPL 2.0, EPL | Changes to the licensed files or library must be shared under the same licence, in certain distribution scenarios | Moderate, depends on how used |
| Strong copyleft | GPL v2, GPL v3 | Distributing software that includes GPL code generally requires providing source under the GPL | Lower for pure SaaS backends, higher for distributed apps |
| Network copyleft | AGPL v3 | Similar to GPL, and also triggered when users interact with modified software over a network | Significant for SaaS |
| Source-available, non-open-source | Business Source License, Server Side Public License and others | Restrictions on commercial or competing use | Varies, read carefully |
| No licence | Code without a licence | No permission granted by default | High; avoid |

Note the last row. Code published without a licence is not free to use; by default, copyright law reserves all rights to the author.

## Why the AGPL Matters for SaaS

The GPL's obligations are mainly triggered by distribution: when you give software to others. A classic SaaS backend that runs on your servers is not distributed to users, which is why many SaaS companies historically used GPL-licensed components on servers without sharing their code.

The AGPL closes that gap. It requires that, if you modify AGPL-licensed software and let users interact with it over a network, you offer those users the source code of the modified version. Depending on how an AGPL component is integrated, this can have implications for your own code.

For founders, the practical approach is simple: **identify any AGPL components early** and decide whether to avoid them, isolate them as unmodified separate services or comply deliberately with legal advice. Investors and acquirers frequently flag AGPL dependencies in due diligence.

## Frontend Code Is Distributed

A detail often overlooked: JavaScript sent to users' browsers is distributed. Your React frontend, including bundled libraries, is downloaded by every visitor. Licence obligations that apply to distribution, such as including notices, therefore apply to frontend dependencies. Most frontend libraries are permissively licensed, but the attribution requirements still apply.

A common way to meet them is a generated third-party notices file or page listing packages and their licences, which build tools can produce.

## Attribution in Practice

Even MIT and Apache 2.0, the most common licences in the JavaScript ecosystem, require that copyright and licence notices are included with copies of the software. In practice:

- **Generate a licence report** of all dependencies as part of your build.
- **Publish a third-party notices page** or include a notices file accessible from your app, for example in an "About" or "Legal" section.
- **For Apache 2.0 components,** include any `NOTICE` files as required.
- **For mobile apps,** include notices in the app, as app stores and licences expect.

## AI-Reproduced Code Snippets

AI coding tools are trained on large amounts of public code. Most generated code is new combinations of common patterns, but tools occasionally reproduce longer passages that closely match existing code, which may be licensed under terms you have not considered.

Measures that reduce risk:

- **Use tool features designed for this.** Some AI coding assistants offer filters that block suggestions matching public code, or features that show references when suggestions resemble public code. Check your tools' settings.
- **Be cautious with large generated blocks** that look like complete implementations of well-known algorithms or libraries.
- **Prefer depending on a library** over having the AI reproduce its code inside your project, so licence terms are explicit.
- **Document your AI tool usage and settings,** which due diligence reviewers increasingly ask about.

## Other Assets: Fonts, Icons, Images and Data

Licences are not only about code. AI-built apps often include:

- **Fonts,** some with licences restricting embedding or modification
- **Icon sets,** typically permissive but with attribution requirements in some cases
- **Images and illustrations,** including AI-generated images, whose terms depend on the tool used
- **Datasets** for features such as postcode lookups or classification, with their own terms

Include these in your inventory.

## Software Bills of Materials

A software bill of materials, or SBOM, is a structured list of the components in your software, with versions and licences. Standard formats include SPDX and CycloneDX. SBOMs are increasingly requested by:

- Enterprise and public-sector customers in security and procurement assessments
- Investors and acquirers in technical due diligence
- Regulation, with the EU Cyber Resilience Act introducing requirements for products with digital elements, which may affect software companies depending on their products and timelines

Generating an SBOM is straightforward with build tools and scanners. Keeping it current is the important part: generate it automatically in your pipeline.

## Licence Scanning

Automated licence scanning tools check your dependencies and flag licences that conflict with your policy. A simple policy might be:

| Licence | Policy |
| --- | --- |
| MIT, BSD, ISC, Apache 2.0 | Allowed, with attribution |
| MPL 2.0, LGPL | Allowed with review of how they are used |
| GPL | Review required; avoid in distributed code |
| AGPL | Not allowed without explicit legal review |
| No licence or unknown | Not allowed |
| Source-available with commercial restrictions | Review required |

Run the scan in CI so new dependencies added by AI tools are checked automatically, and treat violations as build failures or required reviews.

## Customer Contracts and Licence Warranties

Licence questions do not only come from investors. B2B contracts often contain clauses that touch on open-source use:

- **Intellectual property warranties,** stating that your software does not infringe third-party rights
- **Open-source disclosure clauses,** requiring you to list components or notify the customer of copyleft use
- **Indemnities,** where you compensate the customer if a third party claims infringement
- **Source code escrow,** where a copy of your code is deposited with a third party, which makes the composition of that code, including dependencies, visible

Before signing, check whether you can honestly give the warranties requested. An up-to-date SBOM and licence report make that check quick. If a customer asks for warranties broader than your situation supports, negotiate them with your lawyer rather than accepting them unchanged.

## Keeping Compliance Current

Licence compliance is not a one-time clean-up. In AI-assisted development, new dependencies arrive every week. Sustainable practice means:

- **Automated scans on every pull request,** blocking disallowed licences
- **A regenerated SBOM on every release,** stored alongside release notes
- **A quarterly review** of exceptions and of dependencies whose licences changed in new versions, which occasionally happens when projects move to source-available licences
- **Clear ownership,** with one person responsible for the dependency policy

These habits take little time and make the next due diligence or procurement review routine rather than stressful.

## What Due Diligence Reviewers Ask

Investors, acquirers and enterprise customers commonly ask:

1. Do you have a list of all open-source components and their licences?
2. Do you use any copyleft components, particularly AGPL?
3. How do you meet attribution obligations?
4. Do you have a policy for approving new dependencies?
5. Which AI coding tools do you use, and with what settings?
6. Have you assessed whether AI-generated code reproduces licensed code?

Having an SBOM, a licence report, a written policy and a short note on AI tool usage turns these questions into a quick conversation. Our guide to the [technical due diligence data room](https://launchstudio.eu/en/blog/technical-due-diligence-data-room-for-ai-built-startups) covers the broader preparation.

## Common Mistakes

**Assuming open source means no obligations.** Even permissive licences require notices.

**Discovering an AGPL dependency during due diligence.** Late discoveries create negotiation problems.

**Copying code from public repositories without a licence.**

**No inventory of fonts, icons and images.**

**Licence checks done once, never repeated** as AI tools add new packages.

## How LaunchStudio Helps

LaunchStudio prepares AI-built apps for licence scrutiny: generating dependency and licence reports, identifying and replacing problematic dependencies, setting up automated licence scanning and SBOM generation in your pipeline, adding third-party notices to your app, writing a dependency policy and configuring AI tool settings and project instructions to reduce risk. We work alongside your lawyer for legal assessments.

The **Launch Ready** package (€800-€3,500) covers the review and pipeline setup along with security hardening and deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring and ongoing dependency maintenance. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate. For the security side of dependencies, see our article on [hallucinated packages and slopsquatting](https://launchstudio.eu/en/blog/hallucinated-packages-slopsquatting-in-ai-generated-code).

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, used to supplier assessments by enterprise clients such as Vodafone and TNO. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The AGPL Component Found Two Weeks Before Closing

Nina Postma built Roosterwijzer with Cursor and Supabase: a scheduling and workforce planning tool for childcare organisations, with a Next.js frontend and a separate reporting service. Two years in, with steady revenue, she agreed terms for an investment from a sector-focused fund, subject to technical due diligence.

The fund's reviewer asked for a licence inventory. Nina had none. A scan found over 900 packages in total. Most were permissively licensed, but the reporting service, partly generated by an agent, embedded a modified AGPL-licensed charting and reporting server that customers interacted with through the app. Two smaller packages had no licence at all, the frontend included no third-party notices, and a commercial font was embedded in PDF reports without a matching licence. The reviewer rated the AGPL issue as high priority, and the fund asked for a remediation plan before closing.

LaunchStudio replaced the modified AGPL component with a permissively licensed charting library and rebuilt the affected reports, preserving their layout. The two unlicensed packages were replaced with maintained alternatives, the commercial font was replaced with an openly licensed equivalent, and a third-party notices page was generated automatically at build time. Licence scanning and SBOM generation were added to the CI pipeline with a written dependency policy, and Cursor's project instructions listed approved libraries and asked for licence checks on new dependencies. Engineers documented the changes and AI tool settings for the reviewer.

**Result:** The reviewer closed the AGPL finding within two weeks, and the investment completed on the original terms. Roosterwijzer now includes its SBOM in responses to public-sector tenders, which childcare organisations' procurement teams increasingly request.

> *"I had never opened a licence file in my life. One embedded component nearly changed the terms of our funding round."*
> - **Nina Postma, Founder, Roosterwijzer (Hengelo)**

**Cost & Timeline:** €4,700 (Launch & Grow package: licence audit, AGPL component replacement, report rebuild, notices page, scanning, SBOM and dependency policy) - completed in 12 business days.

## Frequently Asked Questions

### Can I use open-source packages in a commercial SaaS?

Yes, most open-source licences allow commercial use. You must meet their conditions, such as keeping copyright and licence notices for permissive licences, and be careful with copyleft licences, particularly the AGPL, whose obligations can apply to software offered over a network.

### Why is the AGPL a concern for SaaS companies?

The AGPL requires that if you modify AGPL software and let users interact with it over a network, you offer them the source code of the modified version. Depending on integration, that can affect your own code, which is why investors and acquirers often flag AGPL dependencies.

### Who owns code generated by AI tools, and can it carry licence obligations?

Ownership depends on tool terms and applicable law, which is still developing. Generated code can occasionally reproduce existing licensed code. Using tool features that filter or reference matching public code, and preferring explicit dependencies, reduces that risk. Seek legal advice for significant transactions.

### How does Manifera's experience help with licence compliance?

Manifera has delivered software to enterprise clients with formal supplier and licence assessments for 11+ years. LaunchStudio applies that experience to make AI-built products demonstrably compliant, with inventories, policies and automated checks that hold up in due diligence.

### Does licence compliance affect my visibility with buyers?

Yes, for enterprise and public-sector buyers. Being able to provide an SBOM and licence policy quickly signals maturity in procurement, and publishing a third-party notices page and security information helps buyers, search engines and AI answer engines see your product as professionally managed.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I use open-source packages in a commercial SaaS?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, with conditions: keep notices for permissive licences and be careful with copyleft, especially AGPL." }
    },
    {
      "@type": "Question",
      "name": "Why is the AGPL a concern for SaaS companies?",
      "acceptedAnswer": { "@type": "Answer", "text": "Modified AGPL software offered over a network requires offering its source, which investors and acquirers often flag." }
    },
    {
      "@type": "Question",
      "name": "Who owns code generated by AI tools, and can it carry licence obligations?",
      "acceptedAnswer": { "@type": "Answer", "text": "It depends on tool terms and developing law; generated code can occasionally reproduce licensed code, so use filters and explicit dependencies and seek legal advice for transactions." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with licence compliance?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has delivered software under enterprise licence assessments for 11+ years, making AI-built products demonstrably compliant." }
    },
    {
      "@type": "Question",
      "name": "Does licence compliance affect my visibility with buyers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; quick SBOM and policy responses signal maturity, and public notices pages help buyers and AI engines." }
    }
  ]
}
</script>
