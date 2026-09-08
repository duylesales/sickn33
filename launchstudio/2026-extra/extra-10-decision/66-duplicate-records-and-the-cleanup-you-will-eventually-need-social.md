🚨 Marijke's product told her she had 1,847 clients. A customer complained about receiving the same quote twice at different prices — and the review found she actually had about 1,100 real companies. 😳

Founders assume a check that looks for duplicates before inserting will actually prevent them. Here's why it doesn't: 🧠

❌ A lookup-then-insert check in the browser does nothing for two requests arriving milliseconds apart — both find nothing, both write
❌ 60% of her 1,847 records were double-submitted forms on mobile connections, where the frontend check never had a chance
❌ "Jansen BV", "Jansen B.V.", and "jansen bv" were three separate records for one company
❌ Because clients were referenced by quotes and invoices, no duplicate could simply be deleted — some companies had their history split across four records

✅ Add a real unique constraint in the database — the only thing that serialises simultaneous writes reliably
✅ Warn on likely-but-uncertain matches ("a similar client already exists") instead of blocking or ignoring them
✅ Disable the submit button on click and give each submission an identifier the server recognises
✅ Build a merge function that repoints every invoice, note, and attachment to the surviving record

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we fix duplicate data at the database layer before it quietly corrupts every number you report. 🔗

Her result: account-scoped unique constraints, double-submit protection, fuzzy warnings on similar names, and a merge tool that cleaned 747 duplicate records over two days. 🚀

👉 Find out what's actually inflating your customer count: https://launchstudio.eu/en/blog/duplicate-records-and-the-cleanup-you-will-eventually-need

#SaaS #DataQuality #IndieHacker #FounderLife #LaunchStudio #Manifera
