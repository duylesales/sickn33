---
Title: Zero-Downtime Database Migrations for Evolving AI Prototypes
Keywords: Database, Migrations, Zero-Downtime, Postgres, SaaS
Buyer Stage: Decision
---

# Zero-Downtime Database Migrations for Evolving AI Prototypes

When iterating from a Lovable or Bolt prototype to a production SaaS, your database schema will change constantly. Taking the app offline for migrations is unacceptable.

## The Expand and Contract Pattern
To achieve zero-downtime migrations in PostgreSQL:
1. **Expand**: Add the new column/table. Your app still writes to the old column.
2. **Dual Write**: Update the app to write to both the old and new columns. Run a backfill script for existing data.
3. **Shift Reads**: Update the app to read from the new column.
4. **Contract**: Remove the old column in a final, safe migration.

This process requires discipline but ensures your AI users never experience 500 errors during deployments.
