📄 Two versions of the same quote

VERSION A: the day the customer signed
Price: based on that day's price table
Status: accepted

VERSION B: the same quote, reopened after a price increase
Price: based on the new price table
Status: still says accepted

Both came from the same app. Both were "correct" when they were generated. 🎨

Erik Boersma runs a painting company in Hengelo with five painters and built Verfofferte in Bolt: painters measure rooms on a tablet, the app calculates paint, hours and price, generates a PDF quote, and customers accept online. Invoices followed from accepted quotes.

After a price increase, the cracks showed:
• PDFs were regenerated from current price tables every time they were opened
• One invoice showed a different total from the quote the customer had signed, which led to a dispute
• Invoice numbers came from a client-side counter, and two invoices shared a number
• Every PDF sat in a public bucket

What LaunchStudio changed (7 business days, €2,150):
✓ Accepted quotes and issued invoices frozen as immutable records
✓ PDF generation moved into an edge function that renders each document once
✓ Invoice numbers from a database sequence
✓ Documents in private storage with signed links
✓ Credit notes for corrections

Now there's only ever one version. Disputes about changing prices stopped, the duplicate invoice was fixed with a credit note, and Erik's accountant accepted the new invoice series without remarks.

"The customer signed one price and received another. Both came from my app, and both were 'correct' at the moment they were generated." - Erik Boersma

https://launchstudio.eu/en/blog/how-do-i-generate-pdf-invoices-in-my-ai-built-app

#Invoicing #Bolt #Supabase #BTW #LaunchStudio #Manifera
