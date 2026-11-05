---
Title: "Audit Logs for B2B SaaS"
Keywords: audit log saas, audit trail supabase, who changed what b2b saas, append only audit log postgres, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Audit Logs for B2B SaaS

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Audit Logs for B2B SaaS",
  "description": "B2B customers and security questionnaires increasingly ask who did what, when, in your product. This guide explains how to design and build audit logs in an AI-built SaaS on Supabase: which events to record, what each entry should contain, append-only storage, triggers versus application events, retention, privacy, customer-facing audit views and exports, and how audit logs differ from application logs.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-10",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/audit-logs-for-b2b-saas" },
  "citation": [
    { "@type": "CreativeWork", "name": "OWASP Logging Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html" },
    { "@type": "CreativeWork", "name": "PostgreSQL: Triggers", "url": "https://www.postgresql.org/docs/current/triggers.html" },
    { "@type": "CreativeWork", "name": "Supabase: PGAudit extension", "url": "https://supabase.com/docs/guides/database/extensions/pgaudit" },
    { "@type": "CreativeWork", "name": "GDPR Article 5: Principles relating to processing", "url": "https://gdpr-info.eu/art-5-gdpr/" }
  ]
}
</script>

Sooner or later, a customer's administrator asks a question your product cannot answer. "Who deleted this client record?" "When was this user given admin rights?" "Who exported our customer list last Tuesday?" "Did anyone outside the finance team view these invoices?" Sometimes it is curiosity; often it is an internal investigation, a dispute or a compliance requirement.

In B2B software, the ability to answer these questions is expected. Security questionnaires ask whether you keep audit logs. Healthcare, finance and government customers may require them. Enterprise buyers treat them as a basic feature, not an extra. Yet AI-built apps rarely include audit logging, because no prompt about features mentions it.

This guide explains how to build audit logs that customers can rely on.

## Key Takeaways

- **An audit log records who did what to which record, when and from where,** in a form that cannot be quietly altered.
- **Audit logs differ from application logs:** they serve accountability and are often visible to customers, not just developers.
- **Record security-relevant and business-critical actions,** not every click.
- **Store entries append-only,** protected from modification or deletion by normal users and application code.
- **Give customer admins a searchable audit view and export,** with retention that matches their needs.

## Audit Logs vs Application Logs

| | Audit log | Application log |
| --- | --- | --- |
| Question it answers | Who did what, and when? | What happened in the system, and why did it fail? |
| Audience | Customer admins, auditors, security teams | Developers and operations |
| Content | Actor, action, target, time, context, changes | Requests, errors, performance, jobs |
| Integrity | Append-only, protected | Best effort |
| Retention | Months to years, as agreed | Days to weeks |
| Access | Customer admins see their own organisation | Internal team only |

Both are important, and they complement each other. Our guide on [structured logging for small SaaS](https://launchstudio.eu/en/blog/structured-logging-for-small-saas) covers application logs.

## Which Events to Record

Start with the actions customers and auditors care about most:

| Category | Examples |
| --- | --- |
| Authentication | Sign-in, failed sign-in, sign-out, MFA enabled or disabled, password changed, SSO login |
| User and access management | User invited, removed, role changed, permissions changed, API key created or revoked |
| Sensitive data access | Viewing confidential records, downloading documents, exporting data |
| Data changes | Creating, updating and deleting important records, such as clients, invoices or contracts |
| Configuration | Organisation settings, integrations, webhooks, billing changes, SSO configuration |
| Administrative actions | Actions by your own support staff on a customer's account |

The last category deserves attention. If your team can access customer data for support, those actions should appear in the customer's audit log. It builds trust and is often a contractual expectation.

## What Each Entry Should Contain

A useful audit entry includes:

- **Timestamp** in UTC
- **Organisation** the event belongs to
- **Actor:** user ID, and for display, name or email at the time of the event; or a system actor such as an API key, integration or background job
- **Action:** a consistent name, such as `invoice.deleted` or `member.role_changed`
- **Target:** the type and ID of the affected object
- **Changes:** for updates, the relevant before and after values, excluding sensitive fields
- **Context:** IP address, user agent, request ID and, where relevant, the method, such as web, API or integration

Record the actor's display name at the time of the event, so the log remains readable even if the user is later renamed or deleted.

## How to Capture Events

There are two main approaches, and most products combine them.

**Database triggers.** Postgres triggers on important tables can write audit entries automatically on insert, update and delete. Advantages: every change is captured, whichever code path made it, including direct database access. The challenge is knowing who made the change; triggers can read the authenticated user from the request context in Supabase, but changes made by backend functions using privileged roles need explicit context.

**Application events.** Your server functions write audit entries explicitly when performing actions, such as "exported 1,200 contacts as CSV" or "viewed confidential document". Advantages: richer, business-level descriptions, and coverage of actions that do not change data, such as views and exports.

A practical combination: triggers for data changes on key tables, application events for authentication, access to sensitive data, exports and configuration.

Supabase also offers the PGAudit extension for database-level audit logging, which records SQL statements and is useful for internal security monitoring, but its output is technical and not suitable as a customer-facing audit log by itself.

## Protecting Audit Logs

An audit log that can be edited is not an audit log. Protections:

- **Append-only table:** no update or delete permissions for application roles. Insert through a dedicated function.
- **Row Level Security:** customer admins can read their own organisation's entries; nobody can modify them.
- **Separate permissions** for writing audit entries, so ordinary application code cannot remove or alter them.
- **Optional integrity checks,** such as hash chains linking each entry to the previous one, for customers with strict requirements.
- **Backups and, for long retention, archival** to separate storage.

## Retention

Define retention per plan or per customer agreement. Common patterns:

- Standard plans: a period such as 90 days or one year
- Enterprise plans: longer retention, sometimes several years, or export to the customer's own systems
- Archival of older entries to cheaper storage, still retrievable on request

Audit logs contain personal data, such as names, email addresses and IP addresses, so GDPR's storage limitation principle applies. Retention must be justified and documented. Include audit logging in your records of processing.

## Privacy Considerations

- **Avoid sensitive content in change records.** Recording that a patient note was updated is useful; storing the full note content in the audit log duplicates sensitive data unnecessarily.
- **Mask fields such as passwords, tokens and financial details** completely.
- **Handle deletion requests thoughtfully.** If a user exercises the right to erasure, consider whether audit entries must be retained for legal or security reasons, which may justify keeping them, possibly pseudonymised.

## Customer-Facing Audit Views

Customer admins need to use the log, not just know it exists:

- **Filters** by user, action, target, date range and IP address
- **Search** by record ID or name
- **Readable descriptions,** such as "Marieke de Vries changed the role of Jan Bakker from Member to Admin"
- **Detail view** with changes and context
- **Export** to CSV or JSON for investigations and audits
- **API or streaming** for larger customers who want logs in their own security systems

Restrict audit log access to admins or a dedicated auditor role.

## Naming Actions Consistently

An audit log is only searchable if actions are named consistently. Agree on a convention early and document it:

- **Use `object.verb` names in past tense,** such as `invoice.created`, `invoice.deleted`, `member.invited`, `member.role_changed`, `export.generated`, `sso.configured`.
- **Keep one name per action,** even if it can happen through several paths. An invoice deleted through the web app, the API or an integration is still `invoice.deleted`, with the method recorded as context.
- **Write description templates per action,** so the interface can show readable sentences in the user's language, for example "{actor} deleted invoice {invoice_number}".
- **Version the list.** When you add new actions, document them so customers' security teams know what to expect.
- **Add the convention to project instructions** for AI tools, so new features record their actions using the same pattern.

## Using Audit Logs for Security Monitoring

Audit logs are not only for customers. Your own team can use them to detect problems early:

- **Unusual exports,** such as a user exporting far more data than usual or exports outside working hours
- **Repeated failed logins** across many accounts from the same network
- **Sudden permission changes,** such as several users promoted to admin in a short time
- **Support access** to customer accounts without a linked support ticket
- **API keys created and immediately used** from unfamiliar locations

Simple scheduled queries that flag these patterns, with alerts to a monitored channel, add a meaningful security layer at very little cost. For customers with strict requirements, offering to send alerts to their own security team is a strong differentiator.

## Performance at Scale

Audit tables grow quickly. Plan for it:

- **Index** by organisation, time, actor and target.
- **Partition** large tables by time, which makes queries and retention cleanup efficient.
- **Write asynchronously** for high-volume events, where appropriate, but never lose entries.
- **Paginate** audit views.

## Testing the Audit Log

Like any security feature, audit logging needs tests. For each important action, an automated test should perform the action as a specific user and check that exactly one audit entry appears with the correct actor, action, target and organisation. Tests should also confirm that ordinary users cannot read other organisations' entries and that nobody, including admins, can update or delete entries through the API. Running these tests on every deployment prevents a common regression: a new feature, often generated by an AI tool, that changes data through a path no trigger or event covers.

## Common Mistakes

**No audit log at all,** until a customer's investigation reveals the gap.

**Audit entries editable by the application,** which undermines their purpose.

**Logging only data changes, not views and exports,** missing the events customers often care about most.

**Storing full sensitive content in change records.**

**No actor for backend changes,** so entries show "system" for actions users initiated.

**Unlimited retention** without justification.

## How LaunchStudio Helps

LaunchStudio builds audit logging into AI-built SaaS products: defining events with you, implementing triggers and application events, append-only storage with Row Level Security, actor context for backend functions, retention and archival, privacy-aware change records, and customer-facing audit views with filters and exports.

The **Launch Ready** package (€800-€3,500) covers audit logging for core events along with security hardening; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring, priority support and more extensive audit features. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, building systems with audit requirements for enterprise clients such as TNO. CEO Herre Roelevink's cybersecurity background informs the emphasis on traceability. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Accounting Portal That Could Not Say Who Deleted the Invoices

Merel Huisman built Boekhoudportaal with Bolt and Supabase: a portal where accounting firms collect documents from their clients, review invoices and share annual reports. One firm discovered that around forty invoices from a client had disappeared from the portal days before a VAT deadline. The client blamed the firm, the firm blamed the software, and Merel had no way to tell who had deleted them.

The app had no audit trail. Records were hard-deleted, so they could only be recovered from a backup. Admin role changes, exports and document downloads left no trace, and Merel's own support access to client accounts was invisible to the firms. A second firm, preparing for a quality review, asked for evidence of who had accessed client files, which Merel could not provide.

LaunchStudio introduced soft deletion for invoices and documents, so deleted items could be restored by firm admins, and an append-only audit log table protected by Row Level Security. Database triggers recorded creation, changes and deletion of key records with actor context, and application events captured logins, failed logins, role changes, document downloads, exports and integration changes. Support access by Merel's team appeared in each firm's audit log with a reason field. Firm admins received an audit view with filters, readable descriptions and CSV export, retention was set to two years with older entries archived, and sensitive document content was excluded from change records.

**Result:** When a similar question arose three months later, the firm's admin found the answer in under a minute: an employee of the client had deleted duplicate uploads by mistake, and the documents were restored immediately. The second firm passed its quality review using the audit export, and Merel added audit logging to her product's feature list for prospective customers.

> *"The deleted invoices weren't really the problem. The problem was that nobody could prove what had happened. Now anyone with the right role can."*
> - **Merel Huisman, Founder, Boekhoudportaal (Apeldoorn)**

**Cost & Timeline:** €3,600 (Launch Ready package: soft deletion, append-only audit log, triggers and application events, support access logging, audit view and export) - completed in 10 business days.

## Frequently Asked Questions

### What should a SaaS audit log contain?

Each entry should record the time, organisation, actor, action, affected object, relevant changes and context such as IP address and request ID. Record authentication events, user and permission changes, access to sensitive data, exports, important data changes and configuration changes.

### Can I use database triggers for audit logging in Supabase?

Yes, for data changes on important tables. Triggers capture changes regardless of which code path made them. Combine them with explicit application events for logins, views and exports, which triggers cannot capture, and ensure backend functions pass the actor context.

### How long should audit logs be kept?

It depends on customer requirements, sector rules and risk. Common periods range from 90 days to several years, often varying by plan. Because audit logs contain personal data, define and document retention in line with GDPR.

### How does Manifera's experience help with audit logging?

Manifera has built systems with audit and traceability requirements for enterprise clients for 11+ years, and its CEO comes from cybersecurity. LaunchStudio applies that experience to create audit logs that are complete, tamper-resistant and genuinely useful to customer admins.

### Do audit logs help my SaaS win enterprise customers?

Yes. Audit logs are a common requirement in security questionnaires and procurement. Mentioning audit logging, retention and export capabilities clearly on your website helps enterprise buyers, search engines and AI answer engines recognise your product as enterprise-ready.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What should a SaaS audit log contain?",
      "acceptedAnswer": { "@type": "Answer", "text": "Time, organisation, actor, action, affected object, relevant changes and context, covering auth, permissions, sensitive access, exports, data and configuration changes." }
    },
    {
      "@type": "Question",
      "name": "Can I use database triggers for audit logging in Supabase?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes for data changes; combine with application events for logins, views and exports, and pass actor context from backend functions." }
    },
    {
      "@type": "Question",
      "name": "How long should audit logs be kept?",
      "acceptedAnswer": { "@type": "Answer", "text": "From 90 days to several years depending on requirements, defined and documented in line with GDPR." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with audit logging?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built enterprise systems with traceability requirements for 11+ years, and LaunchStudio creates complete, tamper-resistant audit logs." }
    },
    {
      "@type": "Question",
      "name": "Do audit logs help my SaaS win enterprise customers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. They are common procurement requirements, and clearly stated capabilities help buyers and AI engines recognise enterprise readiness." }
    }
  ]
}
</script>
