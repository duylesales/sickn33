🎨 Kim Hoogendoorn heeft vanuit Amsterdam een klantportaal voor interieurontwerpers, gebouwd met Claude Code en Supabase: ontwerpers delen moodboards, offertes en facturen met klanten. Kim had een AI-reviewer voor pull requests, Dependabot en scannen op secrets, en controleerde de Supabase-advisor elke maand. Elk pull request kreeg doordachte opmerkingen. Geen kritieke waarschuwingen. Ze voelde zich zeker. ✅

Toen vroeg een grotere studio om een beveiligingsreview voordat ze 40 klanten zou aansluiten. Testen op basis van rollen vond wat geen enkele tool had gemeld: 🧠

❌ Een factuurpolicy, maanden geleden in het dashboard gemaakt, waarmee elke ingelogde gebruiker alle rijen kon lezen
❌ Pdf's van offertes in een openbare bucket
❌ Redirects na wachtwoordherstel die elke URL accepteerden
❌ Back-ups die nooit waren teruggezet

✅ Policies herschreven per ontwerper en klant
✅ Toegangstests die bij elke wijziging in de pipeline draaien
✅ Bestanden in privéopslag, beperkte redirects en een getest herstel
✅ Haar bestaande tools bleven staan, nu ondersteund door tests die de toegangsregels vastleggen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met het combineren van geautomatiseerde tooling en menselijke review voor klanten zoals Vodafone en TNO, dichten we de gaten die tools niet zien en laten we tests achter die uw regels beschermen. 🛠️

💡 Het resultaat: €2.000, vijf werkdagen. De studio sloot haar 40 klanten aan, en twee maanden later faalde een door AI gegenereerde wijziging die de policy zou hebben verruimd op de toegangstest. 🚀

👉 LaunchStudio versus AI-tools voor code review: https://launchstudio.eu/nl/blog/launchstudio-vs-ai-code-review-tools

#CodeReview #Beveiliging #ClaudeCode #Supabase #AIFounder #LaunchStudio #Manifera
