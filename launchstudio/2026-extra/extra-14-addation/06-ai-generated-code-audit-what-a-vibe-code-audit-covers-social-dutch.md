🚨 Pieter-Jan Claes, HR-consultant in Gent, bouwde Startdag met Lovable en Cursor: onboardingsoftware waarmee bedrijven nieuwe medewerkers contracten en beleid laten ondertekenen. Een Nederlands uitzendbureau met 300 plaatsingen per jaar wilde het uitrollen - na een onafhankelijke beveiligingsreview. 😳

De app doorstond elke demo. De audit vond elf problemen, waarvan drie kritiek. Dit verborg "er zag niets fout uit":

❌ Ondertekende contracten in een openbare storage bucket met voorspelbare bestandsnamen
❌ Een RLS-policy waarmee elke ingelogde gebruiker de documenten van alle bedrijven kon opvragen
❌ Een admin-endpoint dat een is_admin-waarde uit de browser vertrouwde
❌ Geen bewaarregels, en een e-mailprovider buiten de EU zonder gedocumenteerde grondslag voor doorgifte

✅ Privébucket met ondertekende, verlopende URL's
✅ RLS-policies herschreven rond het lidmaatschap van een bedrijf
✅ Admincontroles verplaatst naar de server
✅ Bewaarregels plus gedocumenteerde verwerkers en datalocaties voor de privacyfunctionaris van het bureau

Bij **LaunchStudio**, ondersteund door Manifera's engineering met beveiliging voorop en 11+ jaar levering, krijgt u met een vibe code audit geprioriteerde bevindingen, oplossingen en een samenvatting die u met klanten kunt delen. 🛠️

💡 Het resultaat: €5.400, veertien werkdagen. De hertest bevestigde dat elke kritieke en hoge bevinding was opgelost, het uitzendbureau tekende voor twee jaar, en de auditsamenvatting is nu een vaste bijlage in zijn verkoopgesprekken. 🚀

👉 Gebouwd met Lovable, Bolt, Cursor, v0 of Replit? Lees wat een vibe code audit omvat: https://launchstudio.eu/nl/blog/ai-generated-code-audit-what-a-vibe-code-audit-covers

#VibeCoding #AISecurity #CodeAudit #AVG #LaunchStudio #Manifera
