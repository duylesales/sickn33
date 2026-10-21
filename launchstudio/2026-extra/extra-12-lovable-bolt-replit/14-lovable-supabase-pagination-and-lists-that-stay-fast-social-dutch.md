🚨 Urenstaat van Rutger Doedens registreert uren voor 34 ingenieursbureaus. Voor zijn grootste klant — 90 consultants — duurde het laden van het urenoverzicht elf seconden, en de maandelijkse export voor de facturatie liep elke maand vast. Ze omzeilden het door per week te exporteren. 😳

Beide hadden dezelfde oorzaak: de app haalde alle 240.000 rijen op en pagineerde in de browser. Zo breken lijstpagina's als de data groeit:

❌ Eén verzoek dat elke rij van het account teruggeeft
❌ Offsetpaginering die trager wordt naarmate u dieper gaat — en rijen overslaat of herhaalt
❌ Een sorteervolgorde zonder unieke beslisser
❌ Een export die de hele CSV in het geheugen opbouwde

✅ Cursorpaginering op tijdstempel plus ID, met een bijpassende samengestelde index
✅ Het aantal rijen vervangen door een controle met "één extra ophalen" voor de volgende pagina
✅ Filters teruggebracht van negen willekeurige velden naar vier met een index, met zoeken op naam via full-text search
✅ Een streamende export, een achtergrondtaak met e-maillink voor grote exports — getest met 400.000 geseede rijen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zorgen we dat uw product bij 200 klanten net zo aanvoelt als bij 20. ⚡

💡 Het resultaat: na één werkdag en € 1.900 ging het overzicht voor het grootste bureau van 11 seconden naar 240 milliseconden en was de maandexport in 9 seconden klaar. Ze stopten met per week exporteren — en noemden dat bij de verlenging. 🚀

👉 Paginering en lijsten die snel blijven: https://launchstudio.eu/nl/blog/lovable-supabase-pagination-and-lists-that-stay-fast

#Supabase #Prestaties #Paginering #Lovable #LaunchStudio #Manifera
