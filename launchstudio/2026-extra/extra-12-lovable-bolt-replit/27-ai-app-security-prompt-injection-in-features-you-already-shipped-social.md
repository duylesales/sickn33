📄 Two readers. One CV.

THE RECRUITER SAW
A CV for a logistics role.

THE MODEL READ
The same CV, plus a paragraph in white four-point text, invisible on the page. It told the model to ignore the role requirements, rate the candidate as an exceptional match, move them to the shortlist, and not mention any of this in the reasoning.

The model did exactly what it was told. 🤖

Machteld Oosterbeek built Sollicitatiescan in Lovable: application screening for recruitment agencies and employers. It reads uploaded CVs against a role description and produces a shortlist with reasoning. 31 agencies used it. And the feature had tools: it could look up a candidate's previous applications, and it could move a candidate to the shortlist stage, because agencies wanted the obvious matches promoted automatically.

The agency only noticed because the reasoning was unusually enthusiastic, and the experience didn't match. Going back three months, Machteld found four more CVs with similar hidden text, from what looked like a template circulating on a jobseekers' forum.

Her mistake, in her words: giving the model a button that changed a candidate's status, then letting strangers write to it.

What LaunchStudio changed (3 business days, €3,400):
✓ The shortlist-promotion tool removed entirely: the model proposes, a recruiter decides
✓ The database lookup narrowed to the specific candidate, inside the agency's own account
✓ Authorisation checked outside the model, against the recruiter's permissions, for every proposed action
✓ Uploads converted to plain text, with invisible and off-canvas content extracted and flagged
✓ Untrusted document text kept structurally separate from instructions, and marked as data
✓ Model output escaped wherever it's shown (it used to be inserted as HTML)
✓ Per-agency rate limits, and a provider spending cap
✓ Full invocation logging, with documents containing hidden text flagged for human review

The four affected applications were re-screened. Two turned out to be genuinely reasonable candidates who'd used the template on advice. In a year, the hidden-text alert flagged 31 documents, 9 with instruction-shaped content. And since day one of the fix, automatic promotion simply hasn't been possible.

"The model did exactly what it was told. The mistake was mine: I gave it a button that changed a candidate's status, and then let strangers write to it." - Machteld Oosterbeek

https://launchstudio.eu/en/blog/ai-app-security-prompt-injection-in-features-you-already-shipped

#AISecurity #PromptInjection #LLM #Lovable #LaunchStudio #Manifera
