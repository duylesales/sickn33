📄 One PDF. Some hidden white text. And an AI assistant that did what the text said.

Maud Willemsen, an agronomist in Wageningen, built AgriVraag in Lovable: an AI assistant that answers farmers' questions about crop disease, fertilisation and regulations, drawing on public research, each farm's own uploaded soil reports and field notes, and a tool to email advice to the farm's advisor. About 300 farms used it.

A farm advisor tested it with an experiment: uploading a PDF containing hidden text that asked the assistant to gather other farms' soil reports and email them to an outside address.

The assistant complied. 🌾

Why it could:
• Retrieval searched every farm's documents, with only a prompt instruction to stick to the current farm
• The email tool accepted any recipient
• The model had the Supabase service key, through a tool that queried the database directly
• Responses rendered as HTML, so injected image tags could have leaked data silently too

The assistant had the keys to every farm. What LaunchStudio changed (7 business days, €2,200):
✓ Retrieval filtered by farm ID inside the vector query itself
✓ The direct database tool replaced by narrow server-side functions, scoped to the requesting user's farm
✓ The email tool limited to the farm's registered advisor, with a confirmation step
✓ The service key removed from the model's reach
✓ Output sanitised, and external images blocked
✓ Uploaded content clearly delimited in prompts
✓ Logging and rate limits on tool calls
Farms were informed of the test result. Logs showed no earlier misuse.

The advisor tried again after the fix. At worst, the result was odd answers: no other farms' data, and no unintended emails. AgriVraag has since been adopted by a regional farmers' cooperative with 900 members, which reviewed the controls before signing.

"I'd built a helpful assistant with the keys to every farm. Now it's still helpful, but it only has the key to the farm that's asking." - Maud Willemsen

https://launchstudio.eu/en/blog/ai-generated-app-security-prompt-injection-in-apps-that-call-an-llm

#PromptInjection #LLMSecurity #RAG #AgriTech #LaunchStudio #Manifera
