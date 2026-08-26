🔓 Priya's patiënt-intaketool voor zorgklinieken, gebouwd met **Bolt**, had RLS "aan" staan in Supabase — maar een pre-launch audit toonde aan dat de policies default-permissive waren ingesteld. Elke kliniek kon ongehinderd patiëntdata van andere klinieken inzien. 😨

Als uw multi-tenant AI SaaS alleen leunt op applicatiecode om klanten te scheiden, leidt één vergeten filter in één nieuw API-endpoint stilzwijgend tot een datalek. Een groen vinkje bij RLS in uw dashboard betekent niet automatisch dat er iets wordt beveiligd.

❌ RLS ingeschakeld met standaardregels die alles toestaan en niets afschermen
❌ Klantscheiding leunt 100% op ontwikkelaars die bij elke query handmatig een filter moeten toevoegen
❌ Geen security-tests — alleen tests op het 'happy path' waarbij nooit is geprobeerd in te breken

✅ RLS als onwrikbare basisbescherming (*fail-safe*), strikt gekoppeld aan tenant-ID en rol
✅ Applicatielogica als extra schil alleen voor uitzonderingen die dat écht vereisen
✅ Adversarial penetratietests die bewijzen dat cross-tenant toegang 100% onmogelijk is

Bij **LaunchStudio** lossen we exact dit type productieproblemen al sinds 2014 op via Manifera, verspreid over 160+ projecten. 🛡️

Adversarial testing bevestigde nul ongeautoriseerde toegang over kliniekgrenzen heen (€4.100 (Enterprise Hardening Pakket) — voltooid in 13 werkdagen). 🚀

👉 Ontdek hoe we dit hebben opgelost: [Link to article]

#LaunchStudio #Manifera #AISaaS #RowLevelSecurity #MultiTenant
