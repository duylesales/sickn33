🚨 Linda Smits's Intakeverslag drafts AI summaries of intake conversations for neighbourhood social care teams in 19 municipalities. To cut costs, the model was switched to a cheaper version with a one-line change - and in the same release, an AI assistant "tidied" the prompt, removing the paragraph telling it to always include risk and safety statements. 😳

Three weeks later, a team lead spotted a summary that left out a child's statement about violence at home. Others had the same gap - and two mentioned a sibling who didn't exist. Nothing had errored. Here's how to evaluate AI output before your customers do: 🧠

❌ A model swap and a prompt edit shipped with no quality check at all
❌ No definition of what a "good" summary must contain
❌ No check that names in the output actually appear in the input
❌ Social workers under time pressure trusting the draft

✅ An evaluation set of 120 anonymised conversations, annotated with the risk statements that must appear
✅ Deterministic checks plus a validated model-graded check per risk statement - gating every prompt or model change in CI, with models pinned
✅ Structured output with a required risk_indicators field, each backed by a quote from the transcript
✅ Production validation blocking invented names, explicit risk confirmation, edit tracking and privacy-conscious 30-day logging

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we set this up for AI features customers have started to rely on. ⚙️

Her result: €5,200, five business days. Missing risk statements dropped from 14% to under 2%, invented names went to zero, the gate later rejected two regressing models - and heavy edits by social workers fell by about a third. 🚀

👉 AI features: evaluating model output before customers do: https://launchstudio.eu/en/blog/ai-features-evaluating-model-output-before-customers-do

#AI #LLM #AIQuality #ResponsibleAI #LaunchStudio #Manifera
