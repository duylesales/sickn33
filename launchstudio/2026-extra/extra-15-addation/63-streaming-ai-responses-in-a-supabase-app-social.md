👻 The assistant that kept talking to an empty room

The user asked for a long policy draft. The words began to stream in. Then the user navigated away.

The assistant didn't notice. It kept writing, all the way to the end, for nobody. And every word was billed.

Sarah Lindeman built Beleidsassistent with Lovable and Supabase. It helps HR managers at small and medium companies draft and explain workplace policies on leave, remote work and expenses, based on Dutch employment rules and the company's own handbook. Customers loved how responses streamed in. Then the AI bill arrived.

The review found more ghosts in the house:
• The frontend called the model provider directly, with an API key in the bundle (rotated immediately)
• The company handbook was loaded by an ID from the client, using a privileged key, so any user could pull another company's handbook into the prompt
• Answers were saved from the browser after streaming, so closed tabs left conversations empty
• The Markdown renderer allowed raw HTML
• Behind the CDN in production, streams sometimes arrived all at once after twenty seconds

The exorcism (LaunchStudio, 8 business days, €3,100):
🕯️ All AI calls moved into an edge function that checks the session and monthly usage limits
🕯️ The handbook loaded with the user's identity, so Row Level Security applies
🕯️ Server-sent events, with the client's abort signal passed through to the provider, and capped output length
🕯️ Final answers, token usage and status saved server-side, with interrupted answers retryable without extra credits
🕯️ Explicit error events, a renderer without raw HTML, adjusted CDN and compression settings, and rate limits per user and company

First month: AI costs down roughly 45% while usage kept growing. First tokens in under a second. The cross-company handbook exposure closed before any customer noticed.

"Streaming made the assistant feel magical. It also made it very easy to pay for answers nobody was reading, and to show the wrong company's handbook." - Sarah Lindeman

https://launchstudio.eu/en/blog/streaming-ai-responses-in-a-supabase-app

#AIStreaming #Supabase #LLM #HRTech #AIFounder #LaunchStudio #Manifera
