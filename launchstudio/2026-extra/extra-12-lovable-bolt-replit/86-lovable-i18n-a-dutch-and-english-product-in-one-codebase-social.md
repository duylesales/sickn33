🚨 Thijs Wolterink's Kinderopvangplanner handles rosters and parent communication for 21 childcare locations - around 1,600 children. When two Amsterdam locations asked for English for expat parents, he asked Lovable to "add English". Four months later, one parent arrived for a settling-in session a month early. 😳

The English screen showed the date in Dutch order - the 4th of March read as the 3rd of April. That was just one symptom of a language bolted on with 140 inline conditions. Here's how to run a Dutch and English product from one codebase: 🧠

❌ A language toggle with Dutch and English strings side by side across 38 screens
❌ Nine newer screens with no English at all
❌ Dates and numbers formatted by hand instead of by the user's locale
❌ Emails in the organisation's language, and three different English words for "group"

✅ A translation library, with all 201 strings extracted into keyed Dutch and English files
✅ Sentences built from fragments rewritten whole; dates, times and amounts formatted per locale
✅ A language preference per parent for emails, and a 14-term glossary fixed in both languages
✅ AI-drafted English reviewed by a native speaker, plus a CI check that blocks deploys with missing keys

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we prepare Dutch products for their first international customers - without doubling every future change. ⚙️

His result: €2,900, three business days. The CI check blocked four incomplete deploys the next quarter, and three more Amsterdam locations signed within two months. 🚀

👉 Lovable i18n: a Dutch and English product in one codebase: https://launchstudio.eu/en/blog/lovable-i18n-a-dutch-and-english-product-in-one-codebase

#Lovable #Internationalisation #SaaS #NoCode #LaunchStudio #Manifera
