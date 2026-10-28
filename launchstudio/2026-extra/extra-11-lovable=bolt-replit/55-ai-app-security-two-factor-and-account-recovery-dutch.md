---
Titel: "Beveiliging van AI-Apps: Twee-Factor-Authenticatie en Accountherstel"
Trefwoorden: ai app beveiliging, supabase beveiliging, twee factor authenticatie saas, accountherstelcodes, support gedreven accountovername, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Beveiliging van AI-Apps: Twee-Factor-Authenticatie en Accountherstel

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Beveiliging van AI-Apps: Twee-Factor-Authenticatie en Accountherstel",
  "description": "Een tweede factor toevoegen is het eenvoudige gedeelte. Accountherstel is waar accountovernames daadwerkelijk plaatsvinden en waar oprichters die supportvragen beantwoorden de zwakste schakel vormen. Wat je moet bouwen, in welke volgorde en hoe je het test.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-27",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-app-security-two-factor-and-account-recovery" }
}
</script>

Er bestaat een vorm van accountovername die geen greintje technische kennis vereist. Iemand stuurt een e-mail naar de oprichter, meldt dat hij zijn telefoon kwijt is en geen toegang meer heeft tot zijn account, klinkt sympathiek en gestrest, verstrekt een stukje informatie dat openbaar vindbaar of makkelijk te raden is, en vraagt om hulp om weer binnen te komen. De oprichter - behulpzaam, drukbezet en opererend in een vroege fase waarin elke klant telt - helpt de gebruiker direct weer op weg.

Dat is statistisch gezien de meest waarschijnlijke manier waarop een account in jouw applicatie zal worden gekaapt. En het staat volkomen los van welke geavanceerde cryptografische authenticatie je hebt gebouwd. Dat is de kern van dit artikel: tweeledige verificatie (2FA/MFA) zonder een doordachte herstelprocedure voegt geen beveiliging toe, maar creëert simpelweg een support-inbox met een achterdeur.

## Wanneer een Tweede Factor Noodzakelijk Wordt

Niet direct op dag één voor een eenvoudig consumentenproduct, maar aanzienlijk sneller dan oprichters verwachten in de volgende scenario's:

**Je product verwerkt bedrijfskritische gegevens.** Financiële administratie, medische dossiers, persoonsgegevens, of intellectueel eigendom dat in handen van een concurrent enorme schade aanricht.

**Accounts beheren geldstromen.** Uitbetalingen, facturen, terugbetalingen, of betaalinstellingen waarbij een overname direct leidt tot financieel verlies.

**Je klanten zijn zakelijke organisaties.** B2B- en overheidsinkopers verwachten MFA als harde basiseis; het staat steevast als een ja/nee-vraag op elke inkoop- en securityvragenlijst.

**Gebruikers hebben beheerdersrechten (admin-rollen).** Zelfs als gewone eindgebruikers het niet verplicht nodig hebben, moeten administrators dat wél - de accounts die data van alle andere gebruikers kunnen inzien of manipuleren verdienen prioriteit.

Een verstandige fasering voor een startend product: maak MFA optioneel voor alle gebruikers, stel het verplicht voor beheerdersrollen, en bied zakelijke klanten de optie om het voor hun hele organisatie af te dwingen.

## De Methoden, en Wat Ze Jouw Gebruikers Kosten

**Authenticator-apps (TOTP)** die tijdgebaseerde zescijferige codes genereren (zoals Google Authenticator of 1Password). Het rationele uitgangspunt: gratis, werkt volledig offline zonder mobiel bereik, en wordt ondersteund door elke moderne wachtwoordmanager.

**Passkeys (FIDO2 / WebAuthn)**, die gebruikmaken van de biometrie (Touch ID, Face ID) of pincode van het apparaat. De allerbeste gebruikerservaring en steeds breder ondersteund, met de kanttekening dat herstel en gebruik over meerdere apparaten zorgvuldig ontworpen moeten worden.

**E-mailcodes.** Zeer zwak als tweede factor wanneer hetzelfde e-mailadres ook gebruikt wordt voor wachtwoordherstel. Immers: wie toegang heeft tot de mailbox, omzeilt direct beide factoren. Beter dan niets, maar niet iets wat je met een gerust hart aan een zakelijke klant presenteert.

**Sms-verificatie.** Breed begrepen door consumenten, maar technisch de minst betrouwbare optie wegens het risico op SIM-swapping en onderschepte berichten. Acceptabel als secundaire optie, maar nooit als enige beschikbare methode.

**Hardware-beveiligingssleutels (YubiKey).** Uiterst veilig, maar voor de meeste B2B SaaS-apps in deze fase een stap te ver.

Voor een Nederlandse B2B-app biedt de combinatie van authenticator-apps met passkeys als upgrade-pad de ideale balans voor vrijwel elke zakelijke eis.

## Herstel Is het Moeilijkste Gedeelte - en Waar Het Om Draait

Elke tweede factor creëert een nieuwe manier waarop legitieme gebruikers zichzelf kunnen buitensluiten. Smartphones vallen in het water, worden vervangen, gereset of gestolen - dagelijks, door betalende klanten die niets verkeerd hebben gedaan.

Jouw herstelontwerp bepaalt je werkelijke beveiligingsniveau, want een aanvaller zoekt altijd de route van de minste weerstand. Als jouw herstelprocedure neerkomt op "mail ons en wij zetten MFA voor je uit", dan is je tweede factor louter een visuele illusie en is je échte beveiligingsmechanisme het onderbuikgevoel van degene die om 09:00 uur 's ochtends de supportmail leest.

**Back-up herstelcodes** vormen het standaardantwoord: een set van eenmalig bruikbare codes die eenmalig worden getoond bij het activeren, en die de gebruiker veilig moet opslaan. Dit werkt uitstekend, mits je afdwingt dat de gebruiker bevestigt ze te hebben opgeslagen, en mits je ze waterdicht valideert bij gebruik.

**Een tweede geregistreerd apparaat** of een reserve-passkey. Veruit de prettigste optie voor gebruikers die meerdere toestellen bezitten; moedig dit direct aan bij de installatie.

**Een geverifieerde fallback**, zoals een bevestigd nood-e-mailadres of een beheerder binnen dezelfde klantorganisatie die de MFA-status van zijn collega kan resetten. Dit is buitengewoon krachtig voor B2B SaaS: de IT-beheerder van de klant wordt het herstelpunt in plaats van jouw eigen supportdesk.

Wat absoluut géén herstelroute mag zijn: geheime vragen met eenvoudig te achterhalen antwoorden ("Wat was je eerste school?"), of een informeel chatgesprek met jou.

## De Support-Gedreven Accountovername

Dit verdient een strikte interne procedure, omdat het de meest voorkomende reële dreiging is en sociale manipulatie ('social engineering') inspeelt op jouw bereidheid om klanten te helpen.

Leg vooraf schriftelijk vast welk onweerlegbaar bewijs vereist is om handmatig toegang te herstellen. Informatie die uitsluitend de echte accounteigenaar kan bezitten: een specifiek recent factuurnummer, een bankoverschrijvingskenmerk, bevestiging vanaf een geverifieerd alternatief domein, of schriftelijke toestemming van de hoofdbeheerder van het bedrijf. Hanteer deze controle zonder uitzondering, ook wanneer de beller gefrustreerd is, zich voordoet als de directeur, of roept dat er een dringende deadline is - dat zijn exact de psychologische drukmiddelen die aanvallers hanteren.

Twee aanvullende beveiligingsregels: bevestig nooit informatie over een account aan iemand wiens identiteit niet sluitend vaststaat, inclusief de vraag óf het account überhaupt bestaat. En wanneer een account handmatig wordt hersteld, stuur dan direct een notificatie naar het oorspronkelijke e-mailadres in je database, zodat een eventuele overname direct alarm slaat bij het echte slachtoffer.

Voor zakelijke B2B-software is de schoonste oplossing om accountherstel volledig naar de klant te delegeren: hun interne beheerder reset de collega, en jij blijft volledig buiten schot.

## Wat Je Moet Bouwen, in de Juiste Volgorde

**Een soepele activatieflow,** waarbij een QR-code wordt gescand, de herstelcodes eenmalig worden getoond en de gebruiker expliciet moet bevestigen deze te hebben opgeslagen.

**Eenmalige herstelcodes,** die na één keer gebruiken ongeldig worden, direct vervallen zodra nieuwe codes worden gegenereerd, en cryptografisch even zorgvuldig worden gecontroleerd als een wachtwoord.

**Apparaatbeheer,** zodat gebruikers een lijst zien van gekoppelde apparaten en deze zelfstandig kunnen intrekken - precies hoe iemand bij vermoeden van misbruik een verdacht apparaat verwijdert.

**Opnieuw inloggen (re-authenticatie) bij gevoelige acties.** Het uitschakelen van 2FA, het wijzigen van het e-mailadres, het aanpassen van IBAN-uitbetalingsgegevens of het verwijderen van het account. Een bestaande actieve sessie is voor deze handelingen onvoldoende, want sessies worden regelmatig onbeheerd achtergelaten op laptops.

**Automatische notificaties bij beveiligingsgebeurtenissen.** 2FA ingeschakeld, uitgeschakeld, nieuw apparaat toegevoegd, herstelcode gebruikt, wachtwoord gewijzigd. Altijd verzonden naar het oorspronkelijk geregistreerde e-mailadres, zelfs wanneer de actie door de gebruiker zelf werd uitgevoerd.

Die laatste maatregel is technisch eenvoudig en goud waard: het is dé manier waarop een legitieme gebruiker direct ontdekt dat iemand anders in zijn account rommelt.

## Zakelijke Klanten en Organisatie-brede Verplichting

Zodra je software verkoopt aan het mkb of enterprise-klanten, verschuift de vraag van "kunnen we 2FA aanzetten?" naar "kunnen we 2FA verplichten voor ons hele team?".

In de praktijk vereist dat een instelling op organisatieniveau: de hoofdbeheerder kan MFA verplicht stellen voor alle medewerkers binnen dat account, heeft inzicht in wie het al heeft geactiveerd, en kan een respijtperiode (grace period van bijvoorbeeld 14 dagen) instellen zodat medewerkers niet massaal op maandagochtend buitengesloten worden.

Dit is een overzichtelijke functionaliteit die disproportioneel vaak terugkomt in B2B-aanbestedingen, en het hebben ervan maakt het verschil tussen een soepel verkooptraject en een afwijzing.

## Wat Je Beslist Níet Moet Doen

**Maak het niet op dag één voor iedereen verplicht** zonder een beproefde herstelprocedure, tenzij je houdt van een overspoelde helpdesk.

**Vertrouw niet op e-mail als tweede factor** wanneer datzelfde e-mailadres ook gebruikt wordt om het wachtwoord te resetten.

**Schakel 2FA nooit handmatig uit op verzoek** zonder je strikte bewijsprocedure te volgen.

**Sla re-authenticatie niet over** bij acties die de beveiliging van het account wijzigen.

**Ga de cryptografische code niet zelf programmeren;** gebruik beproefde, gecertificeerde libraries voor je stack - dit is typisch het domein waar AI-gegenereerde code subtiele logicafouten introduceert die pas bij een audit aan het licht komen.

## Je Eigen Implementatie Testen

Een half uur testen legt de meeste gebreken direct bloot:

Activeer een tweede factor en controleer of je er bij de volgende inlogpoging netjes om wordt gevraagd. Gebruik één van je herstelcodes, en probeer daarna exact dezelfde code nogmaals - hij móét falen. Genereer een nieuwe set herstelcodes en controleer of de oude direct ongeldig zijn. Probeer 2FA uit te schakelen en kijk of het systeem je dwingt opnieuw je wachtwoord in te voeren. Pas je e-mailadres aan en controleer of je oude mailbox een waarschuwingsmail ontvangt. Log in op een tweede browser, verwijder die sessie via de eerste browser, en controleer of de tweede sessie onmiddellijk stopt. Controleer tot slot je inbox: heeft elk van deze stappen een beveiligingsnotificatie opgeleverd?

Elk afwijkend gedrag is een actiepunt, en vrijwel altijd betreft het een ontbrekende controle of configuratie in plaats van een complete herbouw.

## Een Betrouwbare Implementatie Neerzetten

Dit is typisch een onderdeel waar door AI gegenereerde code op het oog compleet oogt, maar de cruciale helft weglaat: de activatie werkt meestal wel, maar accountherstel ontbreekt volledig en re-authenticatie bij gevoelige acties is nergens te bekennen.

LaunchStudio richt het complete traject in als onderdeel van het klaarmaken van AI-apps voor productie: tweeledige verificatie gebouwd op beproefde standaarden voor jouw backend, robuuste herstelcodes die correct invalideren, apparaatbeheer, re-authenticatie bij gevoelige instellingen, automatische beveiligingsnotificaties, organisatie-brede verplichting voor zakelijke klanten, en een waterdichte supportprocedure voor noodgevallen - zonder de interface die je in Lovable hebt gebouwd aan te tasten.

De engineers zijn van Manifera: elf jaar ervaring met enterprise-authenticatie voor klanten als Vodafone, TNO en CFLW, vanuit Amsterdam en Ho Chi Minhstad. [Praat met een engineer die AI-gegenereerde code begrijpt](https://launchstudio.eu/nl/#contact), of bekijk wat het [Launch Ready pakket](https://launchstudio.eu/nl/#packages) inhoudt.

## Uitrollen Zonder Je Gebruikers Buitensluiten

MFA introduceren bij een bestaand gebruikersbestand leidt bij een verkeerde aanpak direct tot een piek aan supportvragen. Een gefaseerde uitrol voorkomt dit:

**Begin optioneel, met een duidelijke melding.** Bied het aan, leg kort uit wat het beschermt, en laat early adopters instappen. Zij halen de eventuele onduidelijkheden uit je activatieflow vóórdat iedereen ermee te maken krijgt.

**Stel het vervolgens verplicht voor beheerders.** De accounts met de meeste rechten verdienen de eerste bescherming, en die groep is klein genoeg om persoonlijk te begeleiden.

**Bied daarna de optie aan zakelijke klanten,** met een instelbare respijtperiode zodat medewerkers twee weken de tijd krijgen om hun apparaat te koppelen.

**Communiceer vooraf, niet pas op de dag zelf.** Een heldere e-mail een week van tevoren waarin staat wat er verandert, waarom, en wat medewerkers moeten doen bij een nieuw toestel, voorkomt paniekreacties.

## Echt voorbeeld

### Een Accountovername Die Binnenkwam via het Contactformulier

Erik Vlietstra runde Salarisplan in Lovable: een tool voor salarisvoorbereiding gebruikt door elf administratiekantoren rond Zwolle, waarin personeelsgegevens en betaalbatches voor hun cliënten werden beheerd.

Tweeledige verificatie was zes maanden eerder toegevoegd en functioneerde technisch prima. Accountherstel was echter nooit ontworpen: het installatiescherm toonde herstelcodes, maar dwong niet af dat gebruikers ze opsloegen. Wanneer iemand zijn telefoon kwijtraakte, schakelde Erik de tweede factor handmatig uit na wat heen-en-weer gemail.

In maart ontving hij een e-mail van iemand die beweerde salarisadministrateur te zijn bij een van de aangesloten kantoren. Ze schreef dat ze een nieuw toestel had en met spoed toegang nodig had wegens de naderende verloningsdeadline. Het bericht bevatte de echte bedrijfsnaam, noemde de juiste salarisdatum (die openbaar te herleiden was) en voerde de druk flink op. Erik schakelde de tweede factor uit en stuurde een resetlink.

Het was de administrateur niet. De aanvaller logde in, paste de IBAN-rekeningnummers van twee werknemers aan, en de fraude werd pas de volgende ochtend ontdekt tijdens de interne controle van het accountantskantoor zelf, vóórdat de betalingen daadwerkelijk werden klaargezet bij de bank.

Zes werkdagen werk volgden: herstelcodes opnieuw geïmplementeerd met verplichte opslagbevestiging en strikt eenmalig gebruik; apparaatbeheer toegevoegd; re-authenticatie vereist voor het uitschakelen van 2FA, het wijzigen van het e-mailadres en het aanpassen van bankgegevens; automatische e-mailnotificaties geactiveerd bij elke beveiligingswijziging; organisatiedwingend beleid ingebouwd zodat kantooreigenaren 2FA kunnen verplichten; accountherstel verplaatst naar de hoofdbeheerder van het kantoor in plaats van Erik; en een strikte bewijsprocedure vastgelegd voor uitzonderingen die de helpdesk bereiken.

**Resultaat:** er werd geen cent gestolen, het accountantskantoor bleef klant nadat open kaart werd gespeeld over het incident, en twee latere herstelverzoeken werden soepel afgehandeld door de beheerders van de kantoren zelf zonder dat Erik eraan te pas kwam.

> *"Mijn techniek werkte prima. De achterdeur was ikzelf, op een drukke dinsdagochtend, terwijl ik behulpzaam probeerde te zijn voor iemand die klonk alsof ze een zware dag had."*
> - **Erik Vlietstra, Oprichter, Salarisplan (Zwolle)**

**Kosten & Doorlooptijd:** € 2.700 (herstelcodes, apparaatbeheer, re-authenticatie, beveiligingsnotificaties, organisatieregels en supportprocedure) - afgerond in 6 werkdagen.

## Veelgestelde vragen

### Wanneer heeft een startende SaaS-app twee-factor-authenticatie nodig?

Zodra de applicatie privacygevoelige of bedrijfskritische data bevat, wanneer accounts betalingen kunnen autoriseren, wanneer zakelijke klanten erom vragen, of specifiek voor accounts met beheerdersrechten. Het optioneel aanbieden en verplicht stellen voor beheerders is een uitstekende eerste stap.

### Welke tweede factor kan ik het beste aanbieden?

Authenticator-apps (TOTP) zijn de meest betrouwbare en universele standaard - gratis, offline bruikbaar en breed ondersteund - met passkeys als moderne upgrade. E-mailcodes zijn onveilig wanneer e-mail ook gebruikt wordt voor wachtwoordresets, en sms brengt risico's met zich mee rond SIM-swapping.

### Wat is de meest voorkomende manier waarop accounts gekaapt worden?

Via de helpdesk. Een aanvaller neemt contact op met de oprichter, beweert zijn telefoon kwijt te zijn, voert sociale druk uit, en wordt vervolgens 'geholpen' met een handmatige reset. Een strikte, schriftelijk vastgelegde bewijsprocedure is je primaire verdediging.

### Hoe hoort een veilige herstelprocedure eruit te zien?

Eenmalig bruikbare herstelcodes die bij activatie verplicht worden opgeslagen, een tweede geregistreerd toestel waar mogelijk, en voor B2B-applicaties een interne bedrijfsbeheerder bij de klant die zijn eigen collega's kan resetten - wat jou volledig uit de risicocirkel haalt.

### Voor welke acties moet een gebruiker opnieuw zijn inloggegevens invoeren?

Het uitschakelen van de tweede factor, het wijzigen van het geregistreerde e-mailadres, het aanpassen van uitbetalings- of bankrekeningnummers, en het definitief verwijderen van het account. Een actieve browsersessie is hiervoor onvoldoende, omdat sessies in de praktijk vaker worden achtergelaten dan dat wachtwoorden worden gekraakt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wanneer heeft een startende SaaS-app twee-factor-authenticatie nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Bij gevoelige of financiële data, bij zakelijke klanteisen, of voor beheerdersrollen. Optioneel voor iedereen en verplicht voor admins is een logische start."
      }
    },
    {
      "@type": "Question",
      "name": "Welke tweede factor kan ik het beste aanbieden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Authenticator-apps als betrouwbare standaard, aangevuld met passkeys. E-mailcodes zijn zwak als e-mail ook wachtwoorden herstelt; sms kent risico's."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de meest voorkomende manier waarop accounts gekaapt worden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Via support: iemand claimt een verloren toestel en wordt te goeder trouw geholpen. Een strikte bewijsregel voor herstel is de echte verdediging."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe hoort een veilige herstelprocedure eruit te zien?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Eenmalige herstelcodes, een tweede toestel, en voor B2B-software een beheerder bij de klant die collega's kan resetten buiten jouw helpdesk om."
      }
    },
    {
      "@type": "Question",
      "name": "Voor welke acties moet een gebruiker opnieuw zijn inloggegevens invoeren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "2FA uitschakelen, e-mailadres wijzigen, bank- of uitbetalingsgegevens aanpassen en het account verwijderen."
      }
    }
  ]
}
</script>
