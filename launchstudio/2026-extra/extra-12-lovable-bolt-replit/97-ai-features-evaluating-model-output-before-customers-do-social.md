📋 CHANGELOG, one release (illustrative wording; the changes are real)

• Switched to a newer, cheaper model. One-line configuration change. Cost savings.
• Tidied the summarisation code. Prompt shortened.

What the changelog didn't say: the shortened prompt had lost a paragraph telling the model to always include every statement about risk or safety.

Nothing errored.

Linda Smits built Intakeverslag in Lovable: AI summaries of intake conversations for neighbourhood social care teams in 19 municipalities. A social worker records or uploads the conversation, the product drafts a structured summary, and the worker edits and confirms it. 🤝

Three weeks after the release, a team lead noticed a summary had left out a child's statement about violence at home, clearly present in the recording. A review found the same pattern in other summaries, plus two that mentioned a sibling who didn't exist. Social workers had been editing, but under time pressure, and trusting the draft.

The next entries in the changelog (LaunchStudio, 5 business days, €5,200):
• Added an evaluation set of 120 anonymised intake conversations, built with two team leads, annotated with the risk statements that must appear and the people who exist
• Added deterministic checks for schema, length, language, and names not in the transcript
• Added a model-graded check per required risk statement, validated against the annotations first
• Added a CI gate running the evaluation on any change to prompts, models or the pipeline. Model versions pinned
• Added structured output with a required risk_indicators field, each with a supporting quote from the transcript
• Restored the prompt paragraph, documented with the reason it exists
• Production now blocks summaries with names not in the transcript
• Risk indicators highlighted for the social worker to confirm explicitly
• Edit tracking per summary; logs kept 30 days with redaction, documented for privacy officers

Measured on the evaluation set: the cheaper model with the short prompt missed at least one risk statement in 14% of conversations. The restored prompt with structured output, on the original model, brought that below 2%. The gate has since rejected two candidate models that regressed. Invented names in production: zero. Heavily edited summaries fell by about a third.

"We changed one line to save money and a tidy-up removed one paragraph. Nothing errored. The summaries just started leaving out the things that mattered most." - Linda Smits

https://launchstudio.eu/en/blog/ai-features-evaluating-model-output-before-customers-do

#AI #LLM #AIQuality #ResponsibleAI #LaunchStudio #Manifera
