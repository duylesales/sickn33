🧩 Riddle: on an English screen, what date is 04/03?

A Dutch reader says the 4th of March. An English-speaking reader may well say the 3rd of April.

One parent read it the second way and came to a settling-in session a month early. 📅

That was Kinderopvangplanner, the rostering and parent communication tool Thijs Wolterink built in Lovable for childcare organisations: 21 locations, around 1,600 children. Two Amsterdam locations asked for English for their expat parents, so he asked the tool to add it. The result was a language toggle, with conditions behind it on 140 pieces of text across 38 screens, each rendering Dutch or English inline.

Four months later, the two languages had drifted apart:
• Nine newer screens had no English at all
• Dates on the English screens followed the Dutch order
• Notification emails used the organisation's language, not the parent's
• The English used three words for "group": group, class and unit

Solving it for good (LaunchStudio, 3 business days, €2,900):
✓ A translation library, with all 140 strings plus 61 untranslated ones from the newer screens moved into keyed Dutch and English files
✓ Eleven sentences stitched from fragments rewritten as whole sentences with placeholders
✓ Every date, time and amount formatted through the user's locale, with months written out on the parent-facing schedule so nobody has to guess
✓ A language preference stored per parent and used for emails
✓ A glossary of fourteen terms agreed in both languages, including group, location, mentor and settling-in
✓ English drafted by the model, then reviewed by a native speaker in an afternoon
✓ A CI check comparing the key sets in both languages, blocking any deployment where they differ

The English version is complete and has stayed that way. In the next quarter, the CI check blocked four deployments that would have shipped untranslated screens. Three more Amsterdam locations signed within two months, two of them citing the English parent communication.

"One parent came a month early because we wrote the date the Dutch way on the English screen. That was the moment I stopped thinking of translation as words." - Thijs Wolterink

https://launchstudio.eu/en/blog/lovable-i18n-a-dutch-and-english-product-in-one-codebase

#Lovable #Internationalisation #SaaS #NoCode #LaunchStudio #Manifera
