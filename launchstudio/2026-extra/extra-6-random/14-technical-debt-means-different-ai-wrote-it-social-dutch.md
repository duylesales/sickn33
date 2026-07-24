🐛 Nina Bosch bouwde ArchiefKoppel, een documentbeheer-SaaS voor juridische en administratieve kantoren, met Cursor. Ze loste een bug in toegangsrechten op, bracht de update uit en ging verder — totdat weken later een klant precies dezelfde bug meldde in een ander deel van het product. 😳

Door AI gegenereerde technische schuld heeft geen beslissingsspoor — niemand koos ervoor, dus niemand let erop. 🧠

❌ Cursor had bijna-identieke logica voor toegangscontrole geïmplementeerd in acht verschillende bestanden in plaats van in één gedeelde functie
❌ Elk bestand zag er op zichzelf lokaal netjes, goed benoemd en redelijk uit
❌ Nina loste de bug één keer op, bevestigde het, bracht het uit — en het was nog steeds overal elders kapot
❌ Niemand had reden om op duplicatie te controleren, omdat niemand bewust koos om de logica te dupliceren

✅ Zoek systematisch naar bijna-identieke functies door de hele codebase heen, niet bestand voor bestand
✅ Consolideer gedupliceerde logica in één gedeelde, gezaghebbende functie
✅ Voeg een patroon toe om vergelijkbare duplicatie in toekomstige door AI gegenereerde code op te vangen

Bij **LaunchStudio**, gesteund door de engineers van Manifera gevestigd in Amsterdam en daarbuiten, beoordelen we door AI gegenereerde codebases specifiek op dit structurele patroon voordat we productiewerk aanbevelen. 🛡️

ArchiefKoppel heeft nu één gezaghebbende bron voor toegangslogica in plaats van acht, en Nina heeft een herhaalbaar proces om dit patroon voortaan op te sporen. 🚀

👉 Vermoedt u dat uw door AI gebouwde product verborgen duplicatie heeft? Praat met een engineer die door AI gegenereerde code begrijpt: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #TechnicalDebt #CodeQuality
