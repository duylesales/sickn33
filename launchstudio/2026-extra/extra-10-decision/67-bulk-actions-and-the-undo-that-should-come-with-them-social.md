🚨 Tomas's recruiter filtered to 43 dormant contacts, ticked select-all, and hit delete. Select-all had actually grabbed every contact id the frontend had loaded — 214 records, including active clients on other pages. 😳

Founders ship bulk actions as a checkbox column and a delete button. Here's why that's the riskiest control in most products: 🧠

❌ Select-all was ambiguous — it looked like it meant the 43 filtered rows and actually meant every id the page had loaded
❌ "Are you sure?" told her nothing about the real number about to be affected
❌ The deletion ran inside the request, timed out at 180 of 214 records, and she clicked delete again on what remained
❌ Related notes and placement history vanished through cascade rules nobody had reviewed

✅ State the exact count in words before any destructive action: "Delete 214 clients?" not "Are you sure?"
✅ Default to soft deletion with a recovery window instead of permanent removal
✅ Run bulk operations in the background, in batches, with honest partial-failure reporting
✅ Check authorisation per record, not once per request, so a modified request can't reach another account's data

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build bulk operations that can survive a misjudged click. 🗑️

His result: soft delete with a 30-day recovery window, explicit page-versus-filter selection with the count stated, and one-click undo on any bulk operation. 🚀

👉 See what a safe bulk delete actually needs: https://launchstudio.eu/en/blog/bulk-actions-and-the-undo-that-should-come-with-them

#SaaS #ProductSafety #IndieHacker #FounderLife #LaunchStudio #Manifera
