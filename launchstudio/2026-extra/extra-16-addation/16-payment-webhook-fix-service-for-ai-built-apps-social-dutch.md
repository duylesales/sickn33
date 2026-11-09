🎭 Ruben Hoekstra leidt een klein theatergezelschap in Leeuwarden en bouwde Zaalkaart met Lovable en Supabase om tickets te verkopen, met iDEAL-betalingen via Mollie. De verkoop liep goed tot de première van een populaire voorstelling. Toen ontdekte de zaalmanager stoelen die aan twee verschillende kopers waren toegewezen, en kopers die hadden betaald maar geen tickets hadden. 😳

De review vond twee systemen die tickets aanmaakten, en geen van beide vertrouwde de ander: 🧠

❌ Tickets aangemaakt op de redirectpagina, dus de browser te vroeg sluiten betekende geen ticket
❌ Een later toegevoegde webhook die opnieuw tickets aanmaakte zonder op dubbelingen te controleren
❌ Geen betaalstatus opgehaald bij Mollie, dus de handler vertrouwde elk verzoek
❌ E-mails verstuurd vóór het antwoord, met time-outs en nieuwe pogingen tijdens drukke verkoop

✅ Elke betaling opgehaald bij Mollie en vastgelegd op betaal-ID
✅ Tickets aangemaakt in één transactie die ook de stoelen vergrendelt
✅ E-mails naar een achtergrondtaak, en mislukte verwerking geeft een fout zodat Mollie het opnieuw probeert
✅ Een afstemming van de première plus een dagelijkse afstemmingstaak met meldingen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met het bouwen van betaal- en integratiesystemen, maken we betaalwebhooks geverifieerd, idempotent en gemonitord, tegen een vaste prijs. 🛠️

💡 Het resultaat: €2.100, vijf werkdagen. De volgende verkoopopening verwerkte in het eerste uur zo'n 900 tickets zonder één dubbel of ontbrekend ticket. 🚀

👉 Fixservice voor betaalwebhooks in apps gebouwd met AI: https://launchstudio.eu/nl/blog/payment-webhook-fix-service-for-ai-built-apps

#Webhooks #Mollie #Stripe #Lovable #AIFounder #LaunchStudio #Manifera
