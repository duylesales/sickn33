🌩️ MONDAY MORNING FORECAST for Bonnetjesbot

Expected: a peak of receipts from last week
Chance of provider rate limiting: high
Chance of a partial outage: it happened once, for two hours

Maarten Oosterhuis built Bonnetjesbot with Bolt and Supabase: employees photograph receipts, and an AI model extracts supplier, date, amount and VAT for expense claims. Monday mornings were the busiest time, and several times the storm hit. Uploads failed with an error. Employees had to retake photos later. Some gave up.

Why it hit so hard:
⛈️ The model was called synchronously during upload, with no timeout, no retries and no alternative
⛈️ A failed extraction threw away the uploaded image
⛈️ There was no record of which receipts were waiting
⛈️ Support heard about problems from customers

The storm shelter (LaunchStudio, 9 business days, €3,500):
☂️ Upload separated from extraction: receipts saved to private storage straight away, marked pending
☂️ Extraction from a queue, with a timeout and exponential backoff with jitter that respects rate limit headers
☂️ A circuit breaker that switches to a secondary model from another provider, processed in the EU under the same data commitments, after repeated failures
☂️ If both are down, jobs wait in the queue and process automatically on recovery
☂️ Output validated against a schema, retried once, then sent to manual entry with prefilled fields
☂️ A clear status per receipt, a notification when extraction completes, and alerts to Maarten when errors or queue length rise

THE NEXT STORM
A Monday morning rate-limit episode. Employees noticed nothing, except receipts taking a minute longer. Over the next quarter: no receipt lost, and zero tickets about failed uploads.

"I used to dread Monday mornings. Now the queue absorbs the peak and the fallback absorbs the outages." - Maarten Oosterhuis

https://launchstudio.eu/en/blog/ai-feature-fallbacks-when-the-model-api-is-down

#AIReliability #LLM #Resilience #FinTech #AIFounder #LaunchStudio #Manifera
