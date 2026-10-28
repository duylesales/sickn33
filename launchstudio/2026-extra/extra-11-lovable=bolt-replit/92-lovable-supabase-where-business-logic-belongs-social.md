🚨 Carola Mudde's Declaratie handles about 1,400 expense claims a month for two municipalities, a housing foundation and four cultural organisations around Sittard and Geleen. All three business rules - approval above €500, receipts above €50, submit once - lived in the browser. 😳

Then eleven claims were submitted twice by a double-click, and eight were paid twice. Here's why business rules don't belong in a screen: 🧠

❌ A spreadsheet import that bypassed the screen - 60 claims imported without receipts
❌ No uniqueness, so a double-click on a slow connection meant a double payment
❌ Approval checked only in the interface - two claims edited after approval
❌ A database with no constraints: no foreign keys, every column nullable

✅ Rules written in plain language and confirmed by all seven organisations
✅ 214 violating rows found and corrected with each organisation
✅ Not-null, foreign key and uniqueness constraints, plus triggers for receipts and immutable approvals
✅ An append-only audit table, an import through the same validated path, and the schema as migrations

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we put business rules in the database, where every path to the data has to respect them. 🗄️

Her result: nine business days and €4,900 later - no duplicate or unsupported claims in fourteen months, the eight double payments recovered, and the audit trail is now what one municipality's accountant asks for every year end. 🚀

👉 Lovable + Supabase - where business logic belongs: https://launchstudio.eu/en/blog/lovable-supabase-where-business-logic-belongs

#Supabase #Lovable #Database #FinTech #LaunchStudio #Manifera
