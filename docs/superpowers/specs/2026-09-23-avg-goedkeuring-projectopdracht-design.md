# Ontwerp: AVG-proof goedkeuring projectopdracht

**Status:** ontwerp, ter review
**Datum:** 23 september 2026
**Context:** BKN-C01, C-cluster, praktijkopdracht 5
**Reikwijdte:** werkend voor één tutorgroep. Geen instellingsbreed beleid, geen vervanging van het
verwerkingsregister van de HAN.

## 1. Waarom dit ontwerp

Het huidige format *Goedkeuring projectopdracht* vraagt dertien identificerende velden: namen,
studentnummers, telefoonnummers en e-mailadressen van studenten, dezelfde vier van de
bedrijfsbegeleider, de naam van de proceseigenaar en de namen van alle overige stakeholders. Doel,
rechtsgrond, bewaartermijn en toegang zijn niet vastgelegd.

Tegelijk heeft de tutor twee legitieme belangen die persoonsgegevens vereisen:

1. **Beoordelen of de opdracht deugt**, langs de negen criteria uit de docentinstructie.
2. **Controleren of de opdracht echt bestaat**, als onderdeel van de examinering.

Dit ontwerp scheidt die twee. Het eerste belang vraagt geen enkel persoonsgegeven. Het tweede vraagt
er wel om, maar laat ze ontstaan in het kanaal in plaats van in een formulierveld.

## 2. Het uitgangspunt

> Een gegeven dat de gecontroleerde zelf invult, controleert niets.

Een telefoonnummer of e-mailadres dat een student op een formulier typt, is even verzinbaar als de
rest van dat formulier. Bewijskracht ontstaat pas bij een kanaal dat de student niet beheerst: een
bericht dat binnenkomt vanaf het domein van de opdrachtgever.

Daaruit volgt de hele opzet. De verificatie verhuist van het formulier naar de mail. Het formulier
houdt dan geen persoonsgegevens meer over, en de mail levert precies wat nodig is. Naam en zakelijk
adres staan in de kop, zonder dat iemand ze overschrijft.

## 3. De workflow

| Stap | Wie | Wat | Welke persoonsgegevens ontstaan | Waar blijven ze |
|---|---|---|---|---|
| 1 | Team | Vult het formulier in: proces, basisvraag, context, succescriteria, rollen | Geen | Bij het team |
| 2 | Team | Mailt het ingevulde formulier naar de opdrachtgever, tutor in de cc | Geen nieuwe | Mailbox tutor |
| 3 | Opdrachtgever | Antwoordt met *allen beantwoorden* vanaf het zakelijke adres | Naam, zakelijk e-mailadres, functie | Mailbox tutor, map per cohort |
| 4 | Tutor | Toetst het formulier aan de negen criteria en besluit | Geen | — |
| 5 | Tutor | Stuurt de bevestigingsmail door naar het Praktijkbureau; legt het besluit vast | Geen nieuwe | CRM Praktijkbureau |

Het formulier gaat via de cc wel naar de tutor, maar dat is ongevaarlijk: er staan geen
persoonsgegevens in. Dat is precies de winst van §5. Een formulier zonder persoonsgegevens mag
rondgestuurd worden; het oude format had dat niet gekund.

Wat de HAN bewaart, is het besluit en de contactgegevens in het CRM van het Praktijkbureau. Er
ontstaat geen lijst die een tutor zelf bijhoudt.

### Waarom de mail en niet het formulier

De bevestiging per mail doet drie dingen tegelijk die anders drie velden zouden kosten:

- ze toont dat de organisatie bestaat (domein);
- ze toont dat deze persoon de opdracht verstrekt (afzender en ondertekening);
- ze toont commitment (de opdrachtgever heeft er moeite voor gedaan).

## 4. Verwerkingen, doel, rechtsgrond en bewaartermijn

| Verwerking | Doel | Rechtsgrond (te bevestigen door FG) | Bewaartermijn |
|---|---|---|---|
| Bevestigingsmail opdrachtgever | Vaststellen dat de opdracht echt is; onderdeel van examinering | Taak van algemeen belang (examinering, WHW/OER) | Tot het cijfer definitief is en de beroepstermijn van zes weken is verstreken |
| Doorsturen bevestiging naar Praktijkbureau | Relatiebeheer met bedrijven die praktijkopdrachten leveren | Grondslag van het Praktijkbureau voor zijn CRM | Bewaartermijn van het CRM |
| Besluit goedkeuring | Verantwoorden dat de opdracht is getoetst | Taak van algemeen belang | Volgens de bewaartermijn voor examendocumenten |
| Formulier van het team (via cc) | Beoordelen of de opdracht deugt | Taak van algemeen belang | Met de mailmap, zelfde termijn |

De rechtsgrond is hier ingevuld als taak van algemeen belang, omdat examinering een wettelijke taak
van de instelling is en toestemming ongeschikt is in een afhankelijkheidsrelatie. **Dit is een
aanname die de privacycoördinator of FG moet bevestigen**; het is geen juridisch oordeel.

## 5. Het formulier

Het formulier bevat geen persoonsgegevens. Velden die dat wel deden, zijn vervangen of geschrapt.

| Was | Wordt | Reden |
|---|---|---|
| Namen, studentnummers, telefoon, e-mail studenten | Teamnummer | Identiteit staat vast in Brightspace en Osiris |
| Naam, functie, telefoon, e-mail bedrijfsbegeleider | Vervalt volledig | Naam, functie en adres staan in de mailkop en de ondertekening |
| Eigenaar van het proces: `<<naam>>` | Rol van de proceseigenaar | De rol bepaalt of iemand mag beslissen |
| Overige stakeholders, "noem namen" | Rollen plus beschikbaarheid ja/nee | Beschikbaarheid is wat de tutor toetst |

Het blok *Gegevens bedrijfsbegeleiders/opdrachtgever* verdwijnt dus in zijn geheel. Alles wat het
opleverde (wie het is, welke functie, welk adres) staat in de bevestigingsmail, waar de
opdrachtgever het zelf heeft neergezet in plaats van dat een student het overschrijft.

Verder ongewijzigd: bedrijfsnaam, branche, omvang, Lean-ervaring, basisvraag, context, QDC,
procesbeschrijving, succescriteria, randvoorwaarden en risico's. Dat zijn bedrijfsgegevens, geen
persoonsgegevens.

Toegevoegd: een instructieregel bij context en randvoorwaarden dat weerstand, reorganisaties en
metingen op proces- en groepsniveau worden beschreven, zonder herleidbaarheid naar individuen.

Het formulier krijgt de negen tutorcriteria als zichtbare toets, zodat het team vooraf weet waarop
beoordeeld wordt.

## 6. Mailsjabloon voor de opdrachtgever

Het team mailt het ingevulde formulier naar de opdrachtgever en zet de tutor in de cc. De
opdrachtgever antwoordt met *allen beantwoorden* vanaf het zakelijke adres, zodat het antwoord bij
beide partijen binnenkomt. Het sjabloon is de enige plek waar de omvang van binnenkomende gegevens
nog te sturen valt, en zegt daarom expliciet wat níét nodig is.

De mail vraagt om drie bevestigingen: dat de organisatie de opdracht verstrekt, welk proces het
betreft, en dat er tijd is voor vragen en metingen. Plus drie regels:

- het verzoek om te antwoorden vanaf het zakelijke adres en met de gebruikelijke ondertekening;
- de mededeling dat *namen van medewerkers niet nodig zijn; een functieaanduiding volstaat*;
- de mededeling dat de bevestiging intern wordt gedeeld met het Praktijkbureau van de HAN, dat de
  samenwerking met bedrijven bijhoudt.

Die laatste regel is de informatieplicht in één zin. Ze kost niets en voorkomt dat het doorsturen
achteraf als een verrassing landt.

Wie de opdrachtgever is en welke functie die heeft, hoeft niet gevraagd te worden: dat staat in de
afzender en de ondertekening. Vragen om iets wat er toch al staat, levert alleen een tweede kopie op.

## 7. Besluit en doorsturen

De tutor legt per team vast: teamnummer, bedrijfsnaam, basisvraag in één zin, datum en besluit
(akkoord, akkoord onder voorwaarde, afgewezen). Daar staat geen persoonsgegeven in.

De contactgegevens gaan naar het Praktijkbureau door de bevestigingsmail door te sturen. Dat is de
lichtste route: de mail bevat al wat nodig is, in de vorm waarin de opdrachtgever het zelf heeft
neergezet. Er hoeft niets overgetypt te worden en er ontstaat geen tussenlijst.

**Bewust genomen kortere weg.** Het Praktijkbureau heeft een vaste aanmeldroute voor bedrijven.
Deze workflow gebruikt die niet, maar stuurt de mail door. Dat is een pragmatische keuze voor de
eerste ronde. Blijkt het Praktijkbureau de aanmeldroute nodig te hebben, dan vervangt stap 5 het
doorsturen door die route; de rest van het ontwerp verandert daar niet van.

Na het doorsturen en het vastleggen van het besluit heeft de tutor de mail niet meer nodig voor
relatiebeheer, alleen nog als verificatiebewijs bij de examinering. Die termijn bepaalt hoe lang de
kopie in de mailbox blijft.

## 8. Aanpassing van blad 16 (werkboek)

Opdracht 4.2 *Teamstatus* vraagt nu om voornamen van alle teamleden en om contactpersoon, telefoon
en e-mail, en de facilitatorkaart instrueert de tutor daar een foto van te maken. Die foto is de
zwakste bewaarplek in de keten: buiten elk beheerd systeem, zonder termijn.

Nu de contactgegevens via de bevestigingsmail binnenkomen, hoeft de teamstatus er niet meer naar te
vragen. Wat overblijft is waarvoor het blad bedoeld was: zien welke teams een opdracht hebben, zodat
teams zonder opdracht op tijd hulp krijgen.

Wijzigingen:

- voornamen vervallen; teamnummer volstaat;
- contactpersoon, telefoonnummer en e-mailadres vervallen; die komen via de mail;
- blijft staan: teamnummer, organisatie gevonden (ja / in gesprek / nee), naam bedrijf, onderwerp
  van de opdracht, status van de goedkeuring.

Daarmee staat er geen persoonsgegeven meer op het blad, en wordt de foto-instructie op de
facilitatorkaart vanzelf onschadelijk: een foto van een teamnummer en een bedrijfsnaam is geen
verzameling persoonsgegevens. De instructie kan dus blijven zoals ze is.

Dit raakt zowel `Werkboek_intakegesprek_BKN-C01.html` als `Werkboek_intakegesprek_algemeen.html` en
de facilitatorkaart daarin.

## 9. Wat bewust niet wordt verzameld

Telefoonnummers van wie dan ook. Namen van medewerkers, stakeholders of proceseigenaren.
Studentnummers. Individuele prestatie- of verzuimgegevens. Gezondheidsgegevens. Opnames van
interviews. Gegevens over functioneren, conflicten of disciplinaire situaties.

Komt zulke informatie ongevraagd binnen in een mail, dan geldt: het besluit vastleggen, de mail
wissen.

## 10. Open punten

1. Bevestiging van de rechtsgrond door de privacycoördinator of FG.
2. De bewaartermijn voor examendocumenten binnen de HAN. De zes weken beroepstermijn is bekend, de
   archieftermijn niet geverifieerd.
3. Of het Praktijkbureau genoegen neemt met een doorgestuurde mail, of de vaste aanmeldroute wil
   zien. Bewust nu niet uitgezocht (zie §7); te toetsen na de eerste ronde.
4. Wat er gebeurt met het bestaande Excelbestand van het cluster zodra het CRM de contactgegevens
   houdt. Zolang beide bestaan, is het schaduwkopieprobleem niet opgelost.
5. Of een DPIA nodig is. Op het eerste gezicht niet: geen grootschalige of systematische monitoring,
   geen bijzondere categorieën. Dit is een inschatting, geen oordeel.

## 11. Acceptatiecriteria

1. Het formulier bevat geen veld dat om een naam, telefoonnummer of e-mailadres vraagt.
2. Elk gegeven dat de HAN bewaart, is terug te voeren op één van de twee doelen uit §1.
3. Van elk bewaard gegeven staat vast waar het staat, wie erbij kan en wanneer het weg moet.
4. De negen tutorcriteria zijn onverkort toetsbaar met het nieuwe formulier.
5. Het team kan de workflow doorlopen zonder een systeem dat nog ingericht moet worden.
6. De aanpassingen aan blad 16 laten de didactische functie van de teamstatus intact.
7. Na stap 5 van de workflow bestaat er geen door een tutor zelf bijgehouden lijst met
   contactgegevens meer.

## 12. Wat dit ontwerp niet oplost

Het regelt de goedkeuringsstap, niet het onderzoek dat erop volgt. Interviews, observaties en
procesmetingen tijdens het project leveren hun eigen risico's op. Daarvoor is een aparte
studentinstructie nodig. Die valt buiten de reikwijdte van deze spec, maar hoort wel op de agenda.
