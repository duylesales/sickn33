🚨 Gijs Kramer bouwde Evenementenhub met Bolt en Supabase: organisatoren verkopen tickets, publiceren programma's en delen foto's. De omzet groeide gestaag - maar de Supabase-rekening groeide sneller en werd een van zijn grootste kostenposten. Hij had twee keer compute geüpgraded en overwoog een andere provider. 😳

Maar slechts een deel van de rekening kwam van productie. Waarom een Supabase-rekening blijft groeien: 🧠

❌ Vier andere betaalde projecten: twee oude prototypes, staging en een demo, één met PITR
❌ Evenementfoto's op volle grootte die het grootste deel van de egress veroorzaakten
❌ Een requestlogtabel bij elke paginaweergave, gegroeid tot tientallen gigabytes
❌ Een realtime-subscription die steeds opnieuw verbond, een falende webhook die duizenden keren per dag herhaald werd, en botaanmeldingen

✅ Oude prototypes verwijderd, de demo gepauzeerd en staging verkleind zonder add-ons
✅ Foto's verkleind met varianten en via een CDN geserveerd
✅ De logtabel gearchiveerd en verwijderd ten gunste van de logs van het platform
✅ Realtime en webhook gerepareerd, Turnstile bij aanmelden en queries geïndexeerd zodat productie kleiner kon

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zoeken we uit waar u echt voor betaalt voordat u van provider wisselt. 🛠️

💡 Het resultaat: €2.400, 6 werkdagen. De maandelijkse Supabase-rekening daalde met zo'n 60% terwijl het gebruik groeide, pagina's werden sneller - en Gijs bleef bij Supabase. 🚀

👉 Groeit uw Supabase-rekening sneller dan uw omzet? Dit is waarom: https://launchstudio.eu/nl/blog/why-does-my-supabase-bill-keep-growing

#Supabase #CloudCosts #EventTech #FinOps #AIFounder #LaunchStudio #Manifera
