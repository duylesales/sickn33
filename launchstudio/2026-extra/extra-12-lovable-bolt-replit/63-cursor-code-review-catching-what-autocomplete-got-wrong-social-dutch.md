🚨 Sleutelbeheer van Dennis Vermaat houdt voor 17 vastgoedbeheerders en woningcorporaties bij wie welke sleutel van welk gebouw heeft. Hij vroeg Cursor om te veranderen hoe verlopen sleuteltoewijzingen werkten. Schone code, het werkte toen hij testte, geaccepteerd. Zeven weken later bleek uit een routinereview dat dezelfde wijziging een rechtencontrole had omgedraaid - waardoor aannemers met beperkte toegang elke sleutelhouder konden zien, inclusief privéadressen. 😳

De versie die hij testte gedroeg zich identiek. Alleen de diff had het laten zien. Zo reviewt u code die plausibel is in plaats van zichtbaar kapot:

❌ Het afgewerkte bestand lezen in plaats van de diff - ongevraagde wijzigingen worden onzichtbaar
❌ Alleen het pad testen dat u veranderde (een beheerder die de eigen organisatie bekijkt)
❌ Een assistent vragen "review dit" - hij vindt wat fout is, niet wat ontbreekt
❌ Geen tests op autorisatie, dus een omgedraaide rechtencontrole glipt er stil doorheen

✅ De conditie gecorrigeerd, met een test die de rechten voor beide rollen controleert
✅ Zeven weken aan wijzigingen gereviewd - nog twee ongevraagde aanpassingen gevonden
✅ Autorisatietests op de twaalf endpoints die sleuteldata blootstellen
✅ Eén wijziging tegelijk, diff gelezen vóór accepteren, elke sessie op een weggooibare branch

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zijn we de tweede lezer op de wijzigingen die ertoe doen: geld, rechten, verwijderen, uitgaande berichten en schema. ⚙️

💡 Het resultaat: € 2.300, twee werkdagen. Logs bevestigden dat er geen misbruik was - en in het jaar daarna vingen diffs nog vier ongevraagde aanpassingen op, waarvan twee met ernstige gevolgen. 🚀

👉 Codereview in Cursor: opvangen wat autocomplete fout deed: https://launchstudio.eu/nl/blog/cursor-code-review-catching-what-autocomplete-got-wrong

#CodeReview #Cursor #AICoding #AppSecurity #LaunchStudio #Manifera
