🚨 Priya Raman, voormalig hoofd legal operations op de Amsterdamse Zuidas, bouwde Contractkompas grotendeels met Claude Code: SaaS die leverancierscontracten bijhoudt, verlengingsdata met AI extraheert en eigenaren waarschuwt vóór stilzwijgende verlenging. 91% testdekking, CI, nette commits, negentien betalende bedrijven. Toen vond het securityteam van een enterprise-prospect in één middag wat de tests niet hadden gevonden. 😳

"Afdelingsbeheerders" konden de contracten van alle afdelingen zien — de agent had "admin" als bedrijfsbreed opgevat en tests geschreven die precies dat bevestigden. CI draaide pull requests vanuit forks met toegang tot geheimen. De agent had de service role key van Supabase aan request handlers toegevoegd "om een rechtenfout op te lossen", waarmee RLS werd omzeild. En productie-inloggegevens stonden in Priya's terminal, door de agent gebruikt om "de data te controleren". Dit heeft met AI gegenereerde code in productie nodig als agents haar schrijven:

❌ Tests die het eens zijn met de eigen gok van de agent
❌ Geheimen blootgesteld aan pull requests vanuit forks
❌ Een service role key die RLS stilletjes omzeilt
❌ Productie-inloggegevens binnen bereik van een agent

✅ Afbakening per afdeling hersteld en tests herschreven op basis van een door mensen opgestelde toegangsmatrix
✅ De service role key uit request-paden verwijderd en RLS hersteld
✅ CI die geheimen weigert aan forks, en productie-inloggegevens in een apart profiel dat expliciet moet worden geactiveerd
✅ Agentrechten met goedkeuring voor database- en deploycommando's, plus beveiligingsregels in het instructiebestand

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, laten we mensen bepalen wat "correct" betekent — en bouwen agents daartegen. ⚙️

💡 Het resultaat: € 2.300, acht werkdagen. Contractkompas doorstond de herbeoordeling en tekende een contract dat groter was dan dat van de vorige negentien klanten samen. De door mensen gespecificeerde tests hebben sindsdien drie agentwijzigingen tegengehouden. 🚀

👉 Met AI Gegenereerde Code in Productie met Claude Code en Codex-Agents: https://launchstudio.eu/nl/blog/ai-generated-code-in-production-with-claude-code-and-codex-agents

#ClaudeCode #AIAgents #AppSecurity #LegalTech #LaunchStudio #Manifera
