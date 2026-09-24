---
Title: "AI Generated Code Security in HR Tech: Salary Data and Employee Access"
Keywords: ai generated code security, hr tech security, salary data access, employee data gdpr, cursor hr app, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI Generated Code Security in HR Tech: Salary Data and Employee Access

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Generated Code Security in HR Tech: Salary Data and Employee Access",
  "description": "HR tools built with AI handle salaries, sick leave, performance notes and contracts. This decision guide covers the AI generated code security choices HR tech founders must make: role hierarchies, manager scope, sick-leave data, payslips, audit logs and offboarding.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-31",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-generated-code-security-in-hr-tech-salary-data-and-employee-access" }
}
</script>

In most SaaS products, a data leak between users is embarrassing. In HR software, a leak between colleagues is explosive. If one employee can see another's salary, sick-leave history or performance notes, the damage is not abstract; it lands in the office the next morning. That is why AI generated code security deserves particular care in HR tech — and why the default patterns of AI coding tools, which think in terms of "users" and "admins," are rarely good enough.

This guide walks through the decisions HR tech founders need to make before real employee data goes in.

## Decision 1: What Is Your Role Model?

AI-generated HR apps usually have two or three roles: employee, manager, admin. Real organisations are more nuanced:

- **Employee** — sees and edits their own data.
- **Manager** — sees certain data for their direct reports, perhaps their indirect reports.
- **HR** — sees most employee data, sometimes excluding certain fields.
- **Payroll** — sees salary and bank data, not performance notes.
- **Finance or owner** — sees aggregate costs, perhaps not individual details.
- **External** — an accountant, a payroll bureau or an occupational health service with narrow, specific access.

**The decision:** write down a matrix of roles against data categories (personal details, contract, salary, bank details, leave, sick leave, performance, documents) and enforce it on the server — ideally in the database with row-level and column-level policies. Interface-only restrictions are the most common critical finding in AI-built HR tools.

## Decision 2: What Is a Manager's Scope?

"Managers see their team" hides several decisions. Is the team defined by a reporting line, a department or a location? What happens when an employee moves teams — does the old manager lose access immediately? Can managers see their reports' salaries, or only approve leave? Do managers see other managers' teams?

AI-generated code often implements manager access as "anyone with the manager role sees everyone," because it is the simplest query. **The decision:** define scope precisely and derive it from data (reporting lines) rather than hard-coded lists.

## Decision 3: How Is Sick-Leave Data Handled?

Sick-leave information is sensitive, and health information is special category data under GDPR. In the Netherlands, employers are generally not permitted to register the nature or cause of an employee's illness; that information belongs with the occupational health service (arbodienst or company doctor). The Dutch data protection authority has published specific guidance on this.

AI-built HR apps frequently include a free-text "reason for absence" field that invites exactly the information employers should not record. **The decision:** record what is permitted (dates, expected duration, availability for work, relevant contact arrangements), remove or strictly limit free text, and restrict access to those who need it.

## Decision 4: How Are Payslips and Contracts Protected?

Payslips and contracts are typically stored as PDFs. In AI-built apps, they often sit in a public storage bucket with predictable file names — `payslip_2027_10_employee_42.pdf` — meaning anyone who guesses the pattern can download colleagues' payslips.

**The decision:** private storage, signed links that expire quickly, access checks per document, and unguessable identifiers. Consider whether documents should be encrypted at rest with separate keys.

## Decision 5: What Is Logged?

In HR, who looked at what is as important as who changed what. If an employee suspects a colleague in HR has been reading their file, the organisation needs to be able to check.

**The decision:** an audit log of access to sensitive categories (salary, sick leave, performance, documents), not only edits, retained for a defined period and reviewable by an appropriate person.

## Decision 6: What Happens at Offboarding?

When employees leave, their accounts must be deactivated immediately, and their data retained or deleted according to defined periods — payroll records have long legal retention requirements, while many other records should be deleted sooner. When managers leave, their access to former reports must end.

**The decision:** automate deactivation (ideally linked to the contract end date) and implement retention per data category.

## Decision 7: Multi-Tenant or Single-Tenant?

If your HR tool serves multiple companies, tenant separation is the first line of defence. A bug that exposes one company's salaries to another is existential. **The decision:** enforce tenant isolation in the database, test it automatically and treat any cross-tenant query as a critical defect.

## AI Generated Code Security: Implementation Notes for Technical Founders

- Use row-level security with policies based on the authenticated user's role and relationships, not on parameters sent by the client.
- Consider column-level restrictions or separate tables for highly sensitive fields like salary and bank details, so broad queries cannot accidentally include them.
- Never return full employee objects to the frontend "just in case"; select only what each view needs.
- Write automated tests that attempt forbidden access for each role — an employee reading a colleague's salary, a manager reading another team, one tenant reading another.

## A Role Matrix You Can Implement

AI generated code security in HR tools starts with writing down, in one table, who may do what with which data. A typical matrix for a small-business HR portal:

| Data category | Employee (self) | Manager (own team) | HR | Payroll | External accountant |
| --- | --- | --- | --- | --- | --- |
| Personal details | View, edit some | View name and contact | View, edit | View | — |
| Contract and salary | View own | — (policy-dependent) | View, edit | View | View aggregates |
| Bank details | Edit own | — | View | View | — |
| Leave balances | View own | View, approve | View, edit | View | — |
| Sick-leave dates | Report own | View dates for team | View, manage | — | — |
| Performance notes | View own finalised | Write, view team | View all | — | — |
| Documents (payslips, contracts) | View own | — | Upload, view | Upload | — |

Each cell becomes a policy in the database or a check in a server function, and each "—" becomes a negative test. The matrix is also the document a customer's HR director will want to review before signing.

## Implementing Row- and Column-Level Restrictions

Row-level security answers "which employees can you see?"; column-level concerns answer "which fields can you see about them?" In Postgres-based stacks such as Supabase, a practical pattern is:

- **Split sensitive fields into separate tables** — `employee_compensation`, `employee_bank_details`, `sickness_reports` — each with stricter policies than the main `employees` table.
- **Expose views or server functions per role** that return only the permitted fields, rather than letting the client select arbitrary columns.
- **Derive manager scope from reporting lines** stored in the database, and compute it in policies (for example with a helper function that returns the IDs of a manager's reports).
- **Deny by default**, then grant per role.

This design prevents the most common failure in AI-built HR tools: a generic "fetch employee" query that returns salary and bank details to anyone allowed to see the employee's name.

## Logging Reads, Not Just Writes

HR data requires knowing who looked, not only who changed. Log read access to compensation, bank details, sickness reports and performance notes with the viewer, the employee concerned, the category and the time. Store logs append-only, separate from the data, and make them reviewable by an appropriate person — often HR leadership or the data protection contact. Also consider alerts for unusual patterns, such as a manager viewing many employees outside their team or bulk downloads of payslips.

## Payslip Distribution Done Securely

Payslips are sensitive documents that arrive monthly for every employee, making them a frequent source of leaks. A secure flow uploads payslips into private storage with random identifiers, links each file to exactly one employee, notifies employees by email without attaching the file, requires login (ideally with MFA) to download, logs downloads and removes files according to a retention policy. Bulk uploads from payroll software should validate that every file matches the intended employee before publishing — a mis-assigned payslip is one of the most embarrassing incidents an HR tool can have.

## Offboarding and Retention by Category

When employees leave, different data has different lifespans. Payroll and tax-related records typically must be kept for years; many other records should be deleted after a shorter period; access for the departed employee should end immediately, while their former manager's access to their records should also be reviewed. Implement retention per category with scheduled jobs, and give HR a clear overview of what will be deleted when.

## Security Expectations From HR Customers

Companies buying an HR tool increasingly ask for MFA for all users with access to others' data, SSO for larger customers, EU hosting, a data processing agreement, a sub-processor list and evidence of access testing. Preparing these answers upfront — along with the role matrix — shortens sales cycles and demonstrates that the tool was designed for sensitive data rather than adapted after the fact.

## Testing the Matrix Continuously

The role matrix is only as good as its tests. For every cell marked "—," write a test that logs in as that role and attempts the access. Run the suite on every deployment. When an AI coding tool regenerates a query or adds a new screen, these tests are what catch a regression before an employee sees a colleague's salary.

## Special Care for Performance and Conflict Records

Performance reviews, warnings, complaints and conflict notes are among the most sensitive HR records. Restrict them to the employee, their direct manager and HR; distinguish drafts from finalised records, so managers' working notes are not accidentally visible; record who viewed each document; and set retention periods that match your customers' policies. Employees can request access to records about them, so write notes as if the employee may read them — factual, respectful and relevant.

## Integrating With Payroll and Time Tracking

HR portals often connect to payroll software and time-tracking systems. Each integration moves salary or attendance data between systems, so use dedicated service accounts with minimal scopes, encrypt data in transit, log each transfer and reconcile periodically so errors are caught before payday. When an integration fails, it should fail loudly — an alert to HR — rather than silently leaving payroll incomplete.

## What Happens When an HR Tool Leaks

The consequences of an HR data incident reach beyond the regulator: damaged trust between colleagues, possible claims from employees, and a customer who is unlikely to renew. That is why HR tools deserve stricter defaults than typical SaaS — MFA, read logging, separated sensitive data and continuous access testing — from the very first customer.

## Where LaunchStudio Fits

LaunchStudio's review of HR tools maps your role model against actual enforcement, then implements the gaps: database policies, manager scope from reporting lines, sick-leave data changes, private document storage, access logging, offboarding automation and tenant isolation tests. Your existing interface stays.

LaunchStudio is powered by Manifera, a software development company with 11+ years of experience and a security-rooted leadership: CEO Herre Roelevink co-founded CyberDevOps (now CFLW Cyber Strategies). Manifera's engineers work from Ho Chi Minh City with European contact at Herengracht 420, Amsterdam. For the wider team, see [Manifera's about page](https://www.manifera.com/about-us/); for the regulator's view on employee health data, see the [Autoriteit Persoonsgegevens](https://autoriteitpersoonsgegevens.nl/en).

If employee data is already in your system, [talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact) this week.

## Real example

### An AI-Native Founder in Action: A Leave Portal Where Every Manager Saw Every Salary

Laura Timmermans, an HR consultant in Ede, built Verlofbord with Cursor: a portal for small and medium-sized companies to manage leave requests, sick-leave reports and payslip distribution, with manager approvals. Fourteen companies with a combined 850 employees used it.

The problem surfaced when a team lead at a client company mentioned, in passing, a colleague's salary from a different department. Laura asked LaunchStudio to review. Every user with the manager role could query every employee in their company, including salaries and bank details, because the API filtered only by company. The sick-leave form had a free-text "reason" field, and employees had entered diagnoses. Payslips sat in a public bucket with predictable names. There was no access log. Employees who had left six months earlier still had active accounts, and managers retained access to former reports.

Over ten business days, the team implemented a role matrix enforced with row-level policies, manager scope derived from reporting lines, and salary and bank data moved to a separate table visible only to HR and payroll roles. The sick-leave "reason" field was removed, with existing entries deleted after the client companies were informed; the form now records only dates and availability. Payslips moved to private storage with signed links and random identifiers, an access log was added for sensitive categories, offboarding was tied to contract end dates, and automated tests now attempt forbidden access for each role and tenant on every deployment.

**Result:** Verlofbord's clients were informed transparently; none left, and two cited the response as a reason to stay. The tool has since grown to 23 companies, and the forbidden-access tests have blocked one regression introduced by a later Cursor edit.

> *"I built the tool to make HR easier for small companies. I nearly made it the reason one of them had the worst week in its history."*
> — **Laura Timmermans, Founder, Verlofbord (Ede)**

**Cost & Timeline:** €3,100 (Launch Ready package with role model, data restructuring, document security, logging and access tests) — completed in 10 business days.

## Frequently Asked Questions

### Can managers see their team's salaries in an HR app?

That is a business decision each company makes, but it should be explicit and enforced on the server. Many companies limit salary visibility to HR and payroll, with managers seeing only what they need to approve leave or expenses.

### Can an HR tool record why an employee is sick?

In the Netherlands, employers generally may not register the nature or cause of an illness; that belongs with the occupational health service. HR tools should record dates, expected duration and availability, not diagnoses.

### How do I test that my HR app's access control actually works?

Write automated tests that log in as each role and attempt forbidden actions — reading a colleague's salary, another team's leave, another tenant's data — and expect them to fail. Run them on every deployment.

### What does Manifera's security background add for HR tech?

HR data combines personal, financial and health information in a context where leaks cause immediate harm. Herre Roelevink's cybersecurity background and Manifera's enterprise experience shape an approach where access is modelled explicitly and tested continuously.

### Does strong data protection help an HR tool get found?

Yes. HR buyers research security carefully, and a clear, specific security page — describing roles, logging and data location — is the kind of content buyers and AI answer engines look for when comparing tools.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can managers see their team's salaries in an HR app?",
      "acceptedAnswer": { "@type": "Answer", "text": "It is a company decision but must be explicit and server-enforced; many limit salaries to HR and payroll." }
    },
    {
      "@type": "Question",
      "name": "Can an HR tool record why an employee is sick?",
      "acceptedAnswer": { "@type": "Answer", "text": "In the Netherlands employers generally may not register illness nature or cause; record dates, duration and availability instead." }
    },
    {
      "@type": "Question",
      "name": "How do I test that my HR app's access control actually works?",
      "acceptedAnswer": { "@type": "Answer", "text": "Automated tests per role attempting forbidden access, run on every deployment." }
    },
    {
      "@type": "Question",
      "name": "What does Manifera's security background add for HR tech?",
      "acceptedAnswer": { "@type": "Answer", "text": "An approach where access is modelled explicitly and tested continuously, shaped by cybersecurity and enterprise experience." }
    },
    {
      "@type": "Question",
      "name": "Does strong data protection help an HR tool get found?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Specific security pages are what HR buyers and AI answer engines look for when comparing tools." }
    }
  ]
}
</script>
