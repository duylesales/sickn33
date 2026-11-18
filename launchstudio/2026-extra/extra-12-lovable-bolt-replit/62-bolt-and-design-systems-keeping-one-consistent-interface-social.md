EXPECTATION: "These 34 inconsistencies are cosmetic."
REALITY: one of them was why students couldn't submit their forms. 🎨

Sanne de Rooij built Stagebureau with Bolt: internship placement administration for vocational colleges, used by 12 institutions to match around 3,000 students a year with host companies. Before a wider rollout, a college's communications officer reviewed the product and sent her a list of 34 inconsistencies.

The inventory behind the list:
• Eleven different greys for text
• Seven button styles across nine screens
• Four card treatments
• Spacing from 3 to 37 pixels, with no pattern
• Two screens in a different typeface, from a session where the tool reached for something else
• Three input designs, each handling validation errors its own way

That last one was the reality behind the expectation. One input design showed errors only in colour, with no text. That's an accessibility failure, and it's why two colleges had reported that students didn't understand why a form wouldn't submit.

From eleven greys to five steps (LaunchStudio, 2 business days, €2,600):
✓ Tokens: eight colours including one five-step grey scale, a spacing scale in multiples of four, three heading sizes and one body size, one radius, one shadow
✓ An accessible component library, styled with those tokens
✓ Button, input, card, dialog, table, badge and empty state standardised
✓ All nine screens converted, and the stray typeface removed
✓ Errors shown with text alongside colour, which fixed the colleges' complaint
✓ Every arbitrary colour and spacing value removed from the code, so only the defined ones are available
✓ Tokens and the component list written into the repository's conventions file

The communications officer's list shrank to two remaining items, both accepted. Two more colleges signed within the quarter. And the change Sanne values most: new AI sessions now produce screens that match. Before, every feature added a variant. Now they don't.

"I thought it was cosmetic. Then I found out that one of my three input designs showed errors in colour only, and that was why students at two colleges could not work out what was wrong with their forms." - Sanne de Rooij

https://launchstudio.eu/en/blog/bolt-and-design-systems-keeping-one-consistent-interface

#DesignSystems #Bolt #UXDesign #Accessibility #LaunchStudio #Manifera
