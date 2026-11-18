📋 VACANCIES: three jobs, one candidate hired for all of them

JOB 1: Classify the area of law in a new client inquiry
JOB 2: Extract the key facts
JOB 3: Draft a first reply in Dutch

Hugo Verheij built Intakehulp with Lovable and Supabase for small law firms, and gave all three jobs to the same large model, through a US endpoint, called from four edge functions with slightly different code.

The performance review wasn't great:
• Costs high compared with the subscription price
• Responses that sometimes took over twenty seconds
• A law firm's privacy officer asking where inquiries were processed, whether they were retained and which agreement covered them, and Hugo couldn't answer precisely
• Then the provider announced the retirement of his model version, and he had no way to check whether a newer one would behave the same

So LaunchStudio ran proper interviews (12 business days, €4,800):
🧪 An evaluation set of 120 anonymised inquiries, with expected classifications, extracted facts and approved reply drafts
🧪 The result: a smaller, cheaper model did jobs 1 and 2 just as accurately. Job 3 benefited from a larger model.

Then the onboarding:
→ All AI calls behind one provider abstraction, configured per task
→ Structured outputs validated against schemas, with timeouts, retries and cost logging
→ Both models processed in EU regions through a cloud platform, no training use, limited retention
→ A fallback model for drafting outages

The new team's numbers: AI cost per inquiry down about 70%, processing time from around 18 seconds to 5, and privacy approval from a one-page processing statement. When the old model version was retired, Hugo changed a setting and reran the evaluation set in an afternoon.

"I had chosen the most famous model for everything. Testing showed that the right model depended on the task, and that the real asset was being able to switch." - Hugo Verheij

https://launchstudio.eu/en/blog/choosing-an-llm-api-for-an-eu-saas-openai-anthropic-or-mistral

#LLM #AIEngineering #GDPR #LegalTech #AIFounder #LaunchStudio #Manifera
