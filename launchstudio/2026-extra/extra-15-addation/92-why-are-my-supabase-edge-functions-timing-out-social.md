🏭 One worker doing everything, or an assembly line?

Joost van Leeuwen built Huurcheck with Lovable and Supabase: property managers upload commercial lease contracts, and an AI model flags unusual clauses, indexation terms and notice periods. Pilots with three property management firms went well, with short contracts.

Then one firm uploaded 60 long leases for its annual review. Nearly every analysis timed out.

THE ONE-WORKER SETUP
One Edge Function, while the user waited:
1. Extract the text from the PDF
2. Send the whole contract to the AI model in one request
3. Wait for a long structured answer
4. Run a second AI call to summarise it
And for batches, loop over all 60 files in that same single call.

Long contracts broke the wall-clock limit. Scanned PDFs pushed text extraction over the CPU limit. And one failure stopped the rest of the batch.

THE ASSEMBLY LINE (LaunchStudio, 9 business days, €3,200)
STATION 1: Each upload creates a job per contract and answers immediately
STATION 2: A queue takes contracts one at a time
STATION 3: Text extraction as its own step, with scanned PDFs sent to a dedicated OCR service
STATION 4: The contract split into sections, analysed in parallel with timeouts and retries
STATION 5: A final step that combines the results
QUALITY CONTROL: Failed contracts retried twice, then flagged for manual review with the reason
DISPATCH: Progress per contract in the interface, and an email when the batch is done

The result: the 60-lease batch finished in about 25 minutes without a single timeout. Batches of up to 300 contracts have run reliably since, and two of the pilot firms became paying customers on annual plans.

"My function tried to do a day's work in one breath. Splitting it into jobs made it boring, and boring is exactly what my customers wanted." - Joost van Leeuwen

https://launchstudio.eu/en/blog/why-are-my-supabase-edge-functions-timing-out

#Supabase #EdgeFunctions #AIEngineering #PropTech #AIFounder #LaunchStudio #Manifera
