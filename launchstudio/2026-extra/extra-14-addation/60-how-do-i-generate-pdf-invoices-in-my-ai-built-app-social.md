🚨 Erik Boersma runs a painting company in Hengelo and built Verfofferte in Bolt: painters measure rooms on a tablet, the app calculates paint, hours and price, and customers accept a PDF quote online. Then he raised his prices - and customers who reopened an already-accepted quote suddenly saw the new prices. One invoice didn't match the quote the customer had signed. 😳

The customer signed one price and received another. Both came from his app, and both were "correct" when they were generated. Here's why: 🧠

❌ PDFs regenerated from current price tables every time someone clicked download
❌ Invoice numbers from a counter in the browser - two invoices shared a number
❌ Accepted quotes and issued invoices never frozen as records
❌ Every PDF stored in a public bucket

✅ Accepted quotes and issued invoices frozen as immutable records
✅ PDF generation moved to an edge function that renders each document once
✅ Invoice numbers assigned by a database sequence
✅ Documents moved to private storage with signed links, plus credit notes for corrections

At **LaunchStudio**, backed by Manifera's 11+ years of document and billing systems, we treat invoices as records, not views - numbered in the database and corrected only by credit notes. 🛠️

💡 His result: €2,150, seven business days. Disputes about changing prices stopped, the duplicate invoice was fixed with a credit note, and his accountant accepted the new invoice series without remarks. 🚀

👉 Generating invoices and quotes in your AI-built app? Here's how to make them immutable, private and compliant: https://launchstudio.eu/en/blog/how-do-i-generate-pdf-invoices-in-my-ai-built-app

#Invoicing #Bolt #Supabase #BTW #LaunchStudio #Manifera
