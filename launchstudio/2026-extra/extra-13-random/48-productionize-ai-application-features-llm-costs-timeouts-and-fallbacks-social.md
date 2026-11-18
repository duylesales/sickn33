🚰 The AI feature was the product. It was also an open tap.

Month two:
OpenAI invoice: €3,400. More than four times revenue.

Ravi Sewdien, a former management consultant in Rijswijk, built Samenvattr with Cursor: a SaaS that transcribes meeting recordings and produces summaries and action lists with OpenAI's API, with a free tier of three meetings a month. About 1,200 users signed up in two months.

Where the water was running:
💧 The free-tier limit existed only in the interface. The API endpoint had no quota, and a handful of accounts uploaded dozens of long recordings a day, one clearly scripted.
💧 Long meetings went through one synchronous call that often exceeded the hosting time limit. Users saw an error, and the provider still charged for the tokens.
💧 A retry loop from development retried failed calls immediately, up to ten times.
💧 Summaries sometimes came back as malformed JSON, breaking the action-list screen.

Turning off the tap (LaunchStudio, 9 business days, €2,600):
✓ Processing moved to a background queue, with chunked transcription and summarisation
✓ Server-side quotas per plan, and rate limits per user and IP
✓ Capped exponential backoff instead of the retry loop
✓ A smaller model for routine summaries, the larger one only for paid "detailed" summaries
✓ Outputs validated against a schema, with a retry on failure
✓ Budget alerts and a per-user cost dashboard
✓ The privacy notice and the processing agreement with the provider updated

Model costs fell to about 18% of revenue while usage kept growing. Timeout errors disappeared, and the action-list screen hasn't broken on malformed output since. Within six months, Samenvattr reached 420 paying customers.

"The AI feature was the product. It was also a tap anyone could leave running on my credit card." - Ravi Sewdien

https://launchstudio.eu/en/blog/productionize-ai-application-features-llm-costs-timeouts-and-fallbacks

#LLM #OpenAI #AISaaS #CostControl #LaunchStudio #Manifera
