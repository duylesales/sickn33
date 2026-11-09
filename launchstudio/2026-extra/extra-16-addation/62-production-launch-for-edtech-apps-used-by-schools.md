---
Title: "Production Launch for EdTech Apps Used by Schools"
Keywords: edtech app production launch, school app privacy netherlands, onderwijs verwerkersovereenkomst app, children data app security, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Production Launch for EdTech Apps Used by Schools

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Production Launch for EdTech Apps Used by Schools",
  "description": "A guide to launching an educational app built with Lovable, Bolt, v0, Cursor or Claude Code for use by Dutch schools: children's data under the GDPR, the education sector's privacy covenant and model processing agreement, school single sign-on, roles for pupils, teachers and parents, data minimisation, AI features, accessibility, procurement expectations and what LaunchStudio does to make such apps production ready.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-09-26",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/production-launch-for-edtech-apps-used-by-schools" },
  "citation": [
    { "@type": "CreativeWork", "name": "Privacyconvenant Onderwijs", "url": "https://www.privacyconvenant.nl/" },
    { "@type": "CreativeWork", "name": "Kennisnet: Privacy in het onderwijs", "url": "https://www.kennisnet.nl/privacy/" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens: Privacy op school", "url": "https://www.autoriteitpersoonsgegevens.nl/themas/onderwijs" },
    { "@type": "CreativeWork", "name": "W3C: Web Content Accessibility Guidelines (WCAG) 2.2", "url": "https://www.w3.org/TR/WCAG22/" }
  ]
}
</script>

Teachers and education professionals are among the most active builders with AI tools. A primary school teacher builds a reading practice app, a maths teacher builds a homework tracker, a learning specialist builds a tool for pupils with dyslexia, a former school leader builds a planning system for parent-teacher meetings. Many of these apps are genuinely useful, and schools want them.

Schools are also demanding customers. They process data about children, often including learning difficulties, behaviour notes and special support needs. Dutch schools work within a sector-wide privacy framework with standard agreements for suppliers, and they increasingly ask detailed questions about security, hosting and AI. A school board's privacy officer will look at your app very differently from an enthusiastic teacher.

This page explains what a production launch for an edtech app used by Dutch schools typically involves, what LaunchStudio does and where you need legal or privacy specialists. We are not lawyers; we work alongside them and make sure the app does what their advice requires.

## Key Takeaways

- **Children's data deserves extra care** under the GDPR, especially sensitive data about learning and support needs.
- **Dutch education uses a privacy covenant and a model processing agreement;** schools expect suppliers to work with them.
- **School single sign-on** and clear roles for pupils, teachers and parents are common requirements.
- **Data minimisation and AI caution** are central to privacy reviews.
- **Typical price: €2,500-€6,000 within Launch & Grow,** depending on roles, integrations and AI features.

## Why Schools Are Different Customers

| Aspect | Why it matters |
| --- | --- |
| Children's data | Children merit specific protection under the GDPR |
| Sensitive information | Learning difficulties, support plans and behaviour notes are highly sensitive |
| Sector framework | Schools and suppliers work with a sector privacy covenant and model agreement |
| School as controller | The school decides on processing; the supplier usually acts as processor |
| Many roles | Pupils, teachers, mentors, care coordinators, parents and administrators |
| Procurement | School boards ask about hosting, subprocessors, security and AI use |
| Accessibility | Public bodies and many schools expect accessible software |
| Seasonal use | Peaks at the start of the school year, around reports and exams |

## The Education Privacy Framework

Dutch schools, their sector councils and many suppliers of educational software have signed a privacy covenant for education, which sets out how suppliers handle pupil data. It includes a model processing agreement with a privacy annex in which the supplier describes what data is processed, for what purpose, where it is stored, which subprocessors are used and which security measures apply. Schools often ask suppliers to use this model, and organisations such as Kennisnet provide guidance for schools on privacy and digital security.

Whether you sign the covenant, and how you complete the agreement and annex, are legal and organisational choices, ideally made with a privacy specialist. Our role is to make sure the app supports what the annex describes, and to provide accurate technical information for it.

## Children's Data Under the GDPR

The GDPR recognises that children merit specific protection. In most school settings, the school is the controller and processes pupil data on a legal basis linked to its educational tasks, while the supplier processes data on the school's behalf. If your app also offers features directly to children or parents outside the school context, consent rules may apply; in the Netherlands, parental consent is generally required for children under 16 when consent is the legal basis for online services. Data about learning difficulties or support needs can be very sensitive even when it is not a special category in the legal sense. Treat it accordingly.

## What LaunchStudio Does for EdTech Apps

| Area | Typical work |
| --- | --- |
| Hosting | Database, storage and backups in an EU region, with documented subprocessors |
| School separation | Each school or board fully separated in the database |
| Roles | Pupils, teachers, mentors, care staff, parents and administrators with precise permissions |
| Class and group access | Teachers see their own classes; mentors see their mentees; parents see only their children |
| Single sign-on | Login through the school's identity provider or education SSO services where available |
| Data minimisation | Only data needed for the purpose; free-text fields reviewed for sensitive notes |
| Retention | Data removed or anonymised after the agreed period, for example after a pupil leaves |
| Export and deletion | Features for schools to export or delete pupil data |
| AI features | Minimised data to model providers, no training on pupil data where options exist, clear labelling |
| Audit logging | Records of access to sensitive information and administrative changes |
| Accessibility | Review and fixes against WCAG 2.2 AA for key journeys |
| Documentation | Input for the privacy annex, security overview and subprocessor list |

## Roles and Access in School Apps

Access rules in school apps are more complex than in most SaaS products. A teacher should see pupils in their classes, but not pupils in other classes. A mentor sees their mentees across subjects. A care coordinator sees support plans for pupils assigned to them. Parents see their own children, and in some families two parents have different access rights. Pupils see their own work and perhaps their group's. School administrators manage accounts but may not need to see learning content.

AI-generated apps often simplify this to "teacher" and "pupil", with teachers seeing everything. We model the real roles, enforce them in the database with Row Level Security and test them with accounts for each role. This is usually the most important part of an edtech production project.

## Single Sign-On for Schools

Schools prefer that pupils and staff log in with their existing school accounts rather than separate passwords, both for convenience and for control when pupils leave. Depending on the school, this may involve Microsoft or Google school accounts, or education-specific login services used in the Dutch sector. We assess which options your target schools use and implement the most relevant ones, with accounts created or matched on first login and removed or deactivated when the school removes them.

## AI Features in School Apps

AI features such as feedback on writing, practice questions, summaries for teachers or reading support can be valuable. They are also where privacy officers ask the most questions. Before launch, be clear about what pupil data is sent to which model provider, in which region, whether it is retained or used for training under the provider's terms, and how output is checked. Minimise data, avoid sending names or sensitive notes, label AI-generated content and keep teachers in control of anything that affects assessment. Some AI uses in education may fall into higher-risk categories under the EU AI Act, such as systems that determine access to education or evaluate learning outcomes; check with an adviser if your feature does something similar.

## Accessibility

Schools serve pupils with a wide range of needs, including visual impairments, dyslexia and motor difficulties. Public sector schools may need to meet accessibility requirements, and many expect suppliers to do the same. An accessibility review of key journeys against WCAG 2.2 AA, with fixes to shared components, is often part of an edtech production project or a separate service.

## Preparing for School Procurement

School boards typically ask for a completed processing agreement with privacy annex, a list of subprocessors and locations, a description of security measures, information about incident handling and notification, details of AI use and sometimes an accessibility statement. Larger boards may ask for a security questionnaire or a penetration test. A clear security overview and technical input for the annex make these steps much faster. Plan for school calendars: decisions are often made months before the start of a school year.

## Seasonal Peaks

School apps experience strong seasonal patterns: account creation for whole schools in late August and September, peaks around report periods and exams, quiet weeks during holidays. Bulk imports of pupils and classes, often from the school's administration system, need to work reliably. We test bulk onboarding, check performance at expected peak usage and plan releases outside the busiest weeks.

## What We Need From You

- A 15-minute intro call about your app, schools, roles and data
- Access to your repository, database, hosting and related services
- Any privacy, legal or procurement requirements you have received from schools
- Decisions on roles, retention periods and AI use, ideally with your privacy adviser
- A contact at a pilot school willing to test roles and onboarding

## Price and Timeline

| Scope | Typical app | Indicative price | Duration |
| --- | --- | --- | --- |
| Single-school tool | Teachers and pupils, limited data, no integrations | €2,500-€3,500 | 1-2 weeks |
| Multi-school platform | Several roles, parents, school separation, SSO, retention | €3,500-€5,000 | 2-3 weeks |
| Platform with AI and integrations | AI features, bulk imports, audit logging, accessibility work | €5,000-€6,000 or more within Launch & Grow | 3-4 weeks |

Edtech projects are usually delivered within Launch & Grow (€2,500-€7,500 plus €49 per month for ongoing care). Small tools without sensitive data may fit within Launch Ready (€800-€3,500). The quote is fixed after an assessment. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an indication.

## Not Included

We do not provide legal advice, sign the privacy covenant on your behalf, complete legal parts of processing agreements or determine AI Act classification. Integrations with specific school administration systems or education login services are scoped separately because they depend on the provider's requirements and approval processes. Formal accessibility certification and accredited penetration tests are outside the scope but can be prepared for.

## Working With Teachers as Founders

Many edtech founders are teachers or former teachers, and that is a strength: they understand classroom reality better than any software company. What they often lack is experience with the administrative side of selling to schools. A production project that combines secure roles, privacy documentation and procurement-ready answers lets teacher-founders focus on what they know best, while giving school boards the assurance they need.

## Why Founders Choose LaunchStudio

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, building software for organisations with strict data requirements, such as Vodafone and TNO. Manifera's CEO, Herre Roelevink, co-founded the cybersecurity company CyberDevOps, now CFLW Cyber Strategies. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at Manifera's development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore. Our engineers work with test data on staging wherever possible, and hosting stays in the EU regions you choose.

## Real example

### An AI-Native Founder in Action: The Reading App a School Board Almost Rejected

Annemiek Boersma is a remedial teacher in Assen who built Leesladder with Lovable and Supabase, an app where pupils practise reading at their level, teachers track progress and parents see weekly summaries. Her own school loved it, and a school board with eleven primary schools wanted to adopt it. The board's privacy officer sent the model processing agreement with its privacy annex and a list of questions.

The assessment found that the database was outside the EU, every teacher could see every pupil in the school, parents could open other children's progress pages by changing the address, free-text notes contained remarks about dyslexia and home situations, and the AI feedback feature sent pupils' full names and notes to a model provider. There was no retention policy and no way to remove a pupil's data when they left.

LaunchStudio quoted €4,600 within Launch & Grow. The project moved to an EU region, schools were separated and roles defined for teachers, remedial teachers, parents, pupils and administrators, enforced through Row Level Security and tested with accounts for each role. Parents could only see their own children, with support for two parents per child. Free-text notes were replaced with structured support categories plus an optional note visible only to remedial staff. The AI feature sent only the reading text and level, without names or notes. Login through the board's school accounts was added for staff and pupils, retention jobs removed data a year after a pupil left and schools could export or delete pupil data. Technical input for the privacy annex and a subprocessor list were prepared, and key journeys were checked for accessibility.

**Result:** The privacy officer approved Leesladder for all eleven schools after reviewing the completed annex. Around 1,400 pupils started using it after the autumn holiday, and two further school boards used the same documentation in their own reviews.

> *"I built the app for children who struggle with reading. The privacy officer reminded me that their data deserves the same care. Now it gets it."*
> - **Annemiek Boersma, Founder, Leesladder (Assen)**

**Cost & Timeline:** €4,600 (Launch & Grow package: EU migration, school and role separation, parent access, data minimisation, AI changes, school SSO, retention, export and deletion, accessibility checks and privacy documentation, plus €49 per month) - completed in 12 business days.

## Frequently Asked Questions

### What do Dutch schools require from edtech suppliers?

Schools commonly ask suppliers to work with the education sector's model processing agreement and privacy annex, describing data, purposes, hosting, subprocessors and security. Larger boards may add security questionnaires, accessibility statements and questions about AI use. A privacy adviser can help with the legal parts.

### What does it cost to make an edtech app production ready?

Technical production work typically costs €2,500 to €6,000 within Launch & Grow, depending on roles, school separation, SSO, AI features and integrations. Simple single-school tools may fit within Launch Ready. Legal advice is separate.

### Can my app use AI with pupil data?

It can, with care. Minimise the data sent to model providers, avoid names and sensitive notes, check providers' terms on retention and training, keep teachers in control and label AI output. Some uses that affect access or assessment may need further review under the EU AI Act.

### How does Manifera's experience help with edtech apps?

Manifera has built software for organisations with strict data requirements for 11+ years across 160+ projects with 120+ engineers, and its CEO co-founded a cybersecurity company. LaunchStudio applies that experience to roles, privacy and documentation for school apps.

### Does privacy compliance help SEO and AI visibility for edtech?

Yes, indirectly. School leaders and privacy officers search for information about how educational tools handle pupil data. Clear public pages about privacy, hosting, AI use and accessibility help search engines and AI answer engines describe your app accurately when schools compare tools.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What do Dutch schools require from edtech suppliers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Commonly the sector's model processing agreement and privacy annex, plus security, accessibility and AI questions." }
    },
    {
      "@type": "Question",
      "name": "What does it cost to make an edtech app production ready?",
      "acceptedAnswer": { "@type": "Answer", "text": "Typically €2,500-€6,000 within Launch & Grow for technical work." }
    },
    {
      "@type": "Question",
      "name": "Can my app use AI with pupil data?",
      "acceptedAnswer": { "@type": "Answer", "text": "With care: minimise data, check provider terms, keep teachers in control and label output." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with edtech apps?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has 11+ years with strict data requirements, and its CEO co-founded a cybersecurity company." }
    },
    {
      "@type": "Question",
      "name": "Does privacy compliance help SEO and AI visibility for edtech?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes indirectly, through clear public information for schools." }
    }
  ]
}
</script>
