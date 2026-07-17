---
Title: Database Migrations Explained: How to Change Your Supabase Schema Safely
Keywords: AI To Code, Database, Migrations, Explained, Change, Supabase
Buyer Stage: Consideration
---

# Database Migrations Explained: How to Change Your Supabase Schema Safely
During the prototype phase, your AI builder likely generated a Supabase database schema, and you happily tweaked tables directly in the dashboard UI. But once you have live users, manually clicking "Delete Column" is a recipe for disaster. Changing a production database requires a controlled, code-based process called "migrations." Here is how to evolve your Supabase database safely without causing downtime or losing user data.

## The Problem with Dashboard Editing

The Supabase Table Editor is incredibly user-friendly, which makes it dangerous for live apps. If your React app is querying a column called `stripe_customer_id`, and you rename that column to `customer_id` in the dashboard, your live application will immediately crash for every user attempting to pay. There is no undo button.

Furthermore, manual edits create a divergence between your local development environment and your production environment. If you add a feature locally but forget exactly which columns you manually added to the production database, the deployment will fail.

## Enter Database Migrations

A database migration is a script (written in SQL) that describes exactly how to alter the database structure. Think of it as "Git commits for your database."

Instead of clicking buttons in the UI to add a `phone_number` column, you write a migration script:

```sql
ALTER TABLE public.users ADD COLUMN phone_number text;
```
This approach provides three massive benefits:

1. **Version Control**: Migrations are saved as files in your codebase (e.g., `20260728_add_phone.sql`). You have a permanent history of how the database evolved.

2. **Replicability**: You can run the exact same scripts on your local testing database and your production database, ensuring they are identical.

3. **Reviewability**: You (or an experienced developer) can review the SQL code before it touches production data to ensure it does not accidentally drop a critical table.

## The Golden Rule: Backward Compatibility

When altering a live database, every change must be backward-compatible with the currently deployed version of your frontend app.

**Safe Changes (Deploy anytime)**:

- Adding a new table.

- Adding a new, nullable column to an existing table.

- Adding a new index to improve performance.

**Dangerous Changes (Requires phased deployment)**:

- Deleting a table or column.

- Renaming a column.

- Changing a column type (e.g., changing text to an integer).

- Adding a new *required* (NOT NULL) column without a default value.

## How to Rename a Column Without Downtime

If you must rename a column (a dangerous change), you cannot simply run an `ALTER TABLE` script, or the app will crash while the new frontend is deploying. You must use a phased approach:

1. **Phase 1 (Database)**: Run a migration to add the *new* column. Leave the old column intact.

2. **Phase 2 (Frontend)**: Update your frontend code to write data to *both* columns, but read from the *new* column. Deploy this update.

3. **Phase 3 (Data Transfer)**: Run a script to copy existing data from the old column into the new column.

4. **Phase 4 (Cleanup)**: Update the frontend code to stop writing to the old column. Finally, run a migration to drop the old column.

## AI Tools and Migrations

AI tools like Cursor are excellent at writing SQL migration scripts. Instead of asking the AI to "change the database," ask it: "Write a PostgreSQL migration script to add a status column to the invoices table." Review the generated SQL, save it in your project's migration folder, and run it against Supabase using the Supabase CLI or dashboard SQL editor.

**Crucial Step**: Always trigger a manual backup in the Supabase dashboard immediately before running a migration on production.

## Key Takeaways

- Stop editing production databases manually via the dashboard UI.

- Database migrations are SQL scripts that provide version control and replicability for your database schema.

- All database changes on a live app must be backward-compatible with the currently deployed frontend code.

- Destructive changes (renaming or deleting columns) require a phased, multi-deployment approach to avoid downtime.

- Always run a manual database backup before executing a migration script on production.

## Need to Restructure Your Database?

LaunchStudio handles complex production database migrations with zero downtime, ensuring your user data is protected during structural upgrades.

LaunchStudio is operated by **Manifera**, an international software engineering company led by Founder & Director **Herre Roelevink**. Combining "Dutch management with Vietnamese mastery," Manifera maintains headquarters in **Amsterdam, the Netherlands** (Herengracht 420) and development hubs in **Singapore** and **Ho Chi Minh City, Vietnam**. Through LaunchStudio, our senior engineering teams take your AI-built frontend and implement production-ready security controls, live payment gateways, secure hosting, and monitoring, transforming your prototype into a secure and compliant MVP in 1 to 3 weeks. [Get a free quote today](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: HR Onboarding SaaS

Scarlett, a startup founder, used **Lovable** to build a hr onboarding saas prototype. While the application was functional, it corrupted existing user profiles during a manual schema change in the production database.

Scarlett partnered with **LaunchStudio (by Manifera)** to make the product launch-ready. The engineering team restored database state from backup, wrote structured SQL migration files, and set up a staging database environment.

**Result:** Scarlett established a safe, version-controlled database schema upgrade process for all future features.

**Cost & Timeline:** €1,850 (Migration & Schema Package) — production-ready and deployed in 6 business days.

---
## Frequently Asked Questions

### What is a database migration?

A migration is a SQL script that safely changes the structure of your database (like adding tables or columns) while maintaining a version-controlled history of changes.

### Why can't I just edit the table in the Supabase dashboard?

Manual edits in production are dangerous because deleting or renaming a column actively used by the live app will cause immediate crashes. Manual edits also break synchronization with local development.

### How do AI builders handle database changes?

AI excels at writing SQL. Ask the AI to "generate a SQL migration script" rather than vaguely asking it to update the database, then run that script safely.

### What should I do before running any migration on production?

Always trigger a manual database backup in the Supabase dashboard. This provides an immediate recovery point if the migration script has unintended consequences.
