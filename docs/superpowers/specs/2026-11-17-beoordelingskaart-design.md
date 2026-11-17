# Ontwerp: beoordelingskaart voor PRAKOP01-Toets01

**Status:** ontwerp, ter review
**Datum:** 17 november 2026
**Product:** lokaal hulpmiddel van tutor 2 voor de tussentijdse beoordeling van Praktijkopdracht 5 (C-cluster), groepen G1 en G3
**Basis:** prototype „Ontwerp B – Kaart” (`inbox/beoordeling-tutor2/ontwerpen/ontwerp-b-kaart.html`, niet in git), gekozen uit drie prototypes
**Na akkoord:** implementatieplan in `docs/superpowers/plans/`, daarna bouwen in `inbox/beoordeling-tutor2/` (niet in git, bevat studentwerk)

## 1. Doel

De tutor beoordeelt per student of die zich ontwikkelt naar de vereiste beheersing van de leeruitkomsten. Het oordeel zelf is summatief en staat in Handin: één uitspraak, **Voldaan** of **Niet voldaan**, met een optionele toelichting en een vinkje „gezien door 2e beoordelaar”. Dit hulpmiddel levert de onderbouwing van dat oordeel:

1. **Voor de tutor:** per student een formulier waarin per beoordelingscriterium al de relevante tekstfragmenten klaarstaan, met document en pagina, zodat beoordelen vooral wegen is en niet zoeken.
2. **Voor de student:** een bijlage bij het Handin-oordeel die per criterium laat zien waar het oordeel op steunt, in het eigen werk, en die uitnodigt om verder te denken met socratische vragen richting het eindassessment (PRAKOP01-Toets02, 4 januari 2027).
3. **Voor de collega's:** een kalibratieoverzicht, zodat oordelen tussen tutoren vergelijkbaar worden en de 2e beoordelaar kan zien waarop het oordeel rust.

Purpose: de student ziet wat het oordeel betekent en wat de volgende stap naar januari is. Autonomy: de student kiest zelf met welk criterium en welke vraag hij of zij begint; de tutor houdt het oordeel in eigen hand (het hulpmiddel stelt voor, de tutor beslist). Mastery: elk niveau is te herleiden tot fragmenten uit het eigen werk, met de rubrictekst van het niveau erboven ernaast. Social: teamcriteria worden één keer per team beoordeeld en gelden voor alle teamleden; kalibratie met collega's is ingebouwd. KISS: geen server, geen accounts, geen terugkoppelkanaal; de antwoorden van de student gaan mee in diens eigen eindportfolio (afgewezen alternatief: antwoorden laten terugsturen naar de tutor, wat hosting of mail en dus persoonsgegevens buiten de eigen computer vraagt).

## 2. Besluiten uit het gesprek

| Vraag | Keuze van de auteur | Afgewezen |
|---|---|---|
| Vorm | Ontwerp B „Kaart”: rubricbord met fragmentkaartjes die de tutor naar een niveau sleept; de student ziet per criterium een route en een groeiende denkkaart | A „Dossier” (drie kolommen, toetsenbord-eerst, briefvorm); C „Stapel” (kaartenstapel per criterium, 3D-landschap voor de student) |
| Aard van het oordeel | Summatief. Uitkomst: Voldaan / Niet voldaan in Handin | formatieve tussenstand (zo waren de prototypes geschreven) |
| Wie beslist | De tutor alleen; het hulpmiddel rekent geen Voldaan/Niet voldaan uit | een beslisregel die het oordeel uit de niveaus afleidt |
| Kalibratie | Met collega-tutoren; de 2e beoordelaar zet in Handin „gezien” | tweede beoordelaar die zelfstandig oordeelt |
| Wat de student krijgt | In Handin: Voldaan/Niet voldaan plus een korte toelichting. Als bijlage: het studentformulier als pdf (de toelichting in detail) | alleen de Handin-tekst; een gehoste link |
| Bezorging | Een pdf-bijlage in Handin, één per student, gemaakt met afdrukken naar pdf vanuit de studentweergave van het hulpmiddel | een HTML-bijlage (Handin accepteert alleen pdf); een link naar een gehoste pagina (studentwerk buiten de eigen computer) |
| Terugkoppeling van antwoorden | Geen. De student neemt de vragen mee naar de eindreflectie voor Toets02 | antwoorden terugsturen naar de tutor; een interactieve denkkaart (kan niet in een pdf) |
| Minimumeisen portfolio | Tellen al bij Toets01 | alleen informatie richting januari |
| Tijdpad | Beoordelen begint op 17 november 2026. Eerst het bord, het oordeel en de Handin-tekst; de pdf-bijlage en het kalibratieoverzicht daarna | alles in één keer opleveren |
| Persoonsgegevens | Alleen voornamen; geen achternaam, klas, studentnummer of e-mail. Pdf's in de viewer zijn kopieën waarin achternamen zijn vervangen | volledige namen; originele pdf's in de viewer |
| Socratische vragen | Bewerkbaar en per student te kiezen door de tutor | vaste vragen uit het databestand (zo werkt het prototype) |
| Volgende stap per criterium | Eigen feed-forward-tekst van de tutor per criterium | automatisch de rubrictekst van het volgende niveau (zo werkt het prototype) |

## 3. Wat er gebeurt, van inlevering tot Handin

```
 Handin-download ──► 1. Voorbereiden ──► 2. Beoordelen ──► 3. Kalibreren ──► 4. Afronden
 (inbox/quick-win)    (Claude, per groep)   (tutor, op de kaart)  (met collega's)    (Handin + bijlage)
```

### 3.1 Voorbereiden (Claude, per groep)

Deze stap hoort bij het implementatieplan: het zijn taken voor Claude, per groep, met dezelfde controles als in §7 *(keuze van de bouwer, na review)*.

- Inleveringen per team in een map zetten, met alleen voornamen in bestands- en mapnamen (zoals al gedaan voor G1 en G3).
- Per document een viewer-pdf maken: docx-kopie waarin achternamen, klascodes, studentnummers en e-mailadressen zijn vervangen, daarna met LibreOffice naar pdf. Paginanummers in het hulpmiddel volgen deze pdf.
- Per groep een databestand vullen (zelfde vorm als `ontwerpen/data.js`, uitgebreid zoals in §5):
  - teamdocumenten en per student de persoonlijke documenten;
  - per criterium voorgeselecteerde fragmenten: letterlijk citaat, document, pagina, signaal (sterk / twijfel / ontbreekt), een notitie voor de tutor en een voorgestelde zin voor de student;
  - de portfolio-checklist per student (aantallen per minimumeis, met pagina);
  - per criterium drie tot vijf socratische vragen die op het werk van dit team of deze student ingaan.
- Studenten zonder inlevering staan in de lijst met status „geen inlevering”, zonder fragmenten.

### 3.2 Beoordelen (tutor)

Het rubricbord van het prototype blijft de kern: rijen per criterium (BC1, BC2 teamdeel; BC5 persoonlijk), banen per niveau (In ontwikkeling / Op niveau / Boven niveau), fragmentkaartjes in een D3-krachtsimulatie. Slepen, pijltjestoetsen en klikken werken zoals in het prototype; een klik opent de lade met het citaat, de pdf op de juiste pagina, de notitie en „noem in feedback”.

Nieuw ten opzichte van het prototype:

- **Twee teksten per fragment.** De notitie is voor de tutor en komt nooit bij de student. De zin voor de student is apart en bewerkbaar.
- **Feed-forward per criterium.** Een eigen tekstveld „Volgende stap richting januari”. Leeg is toegestaan; dan toont het studentformulier niets op die plek.
- **Vragen kiezen en bewerken.** Per criterium ziet de tutor de voorgestelde vragen, kan er een uitzetten, de tekst aanpassen of een eigen vraag toevoegen.
- **Het oordeel.** Onder het bord een keuze Voldaan / Niet voldaan. Een toelichting is verplicht bij Niet voldaan, en bij Voldaan terwijl een criterium op In ontwikkeling staat of een minimumeis niet gehaald is.
- **Niveau per criterium** *(keuze van de bouwer, na review)*. Zoals in het prototype: het hulpmiddel stelt een niveau voor uit het zwaartepunt van de geplaatste kaartjes (afgerond gemiddelde van de banen); de tutor kan het met één klik overschrijven. Het studentformulier toont alleen het uiteindelijke niveau, niet het voorstel.
- **Teamcriteria één keer** *(keuze van de bouwer, na review)*. Alles van BC1 en BC2 is teamniveau: niveau, plaatsing van kaartjes, „noem in feedback”, zinnen voor de student, feedback, feed-forward, bespreekpunten en de socratische vragen bij BC1 en BC2. Bij een teamlid staan ze al ingevuld met een slotje („teamoordeel”); wijzigen kan alleen in de teamweergave. Een open bespreekpunt op BC1 of BC2 houdt de status „klaar” tegen voor het hele team. Alleen BC5, de checklist, het eindoordeel en de vragen bij BC5 zijn per student. Elke student beantwoordt de teamvragen wel zelf, in de eigen bijlage.
- **Checklist.** De minimumeisen van het portfolio (6 reflectieverslagen, 6 feedbackmomenten met bewijs, 3 reflecties op feedback, 3 ontwikkelpunten met elk 3 acties, eindreflectie) als waffle per eis, met de pagina waar het staat. Deze eisen tellen bij Toets01. Wat niet gehaald is, staat rood naast het eindoordeel. Per eis kan de tutor aanzetten dat die bij Toets01 nog niet geldt; standaard staat dat alleen aan bij de eindreflectie *(keuze van de bouwer: de eindreflectie gaat over het hele semester)*.

### 3.3 Kalibreren (tutor met collega's)

- Per criterium en per eindoordeel kan de tutor **„bespreken”** aanzetten, met een korte reden.
- **Kalibratieoverzicht** (één pagina, printbaar): per student per criterium het niveau, de twee of drie fragmenten waarop het rust (citaat en pagina), de niet gehaalde minimumeisen, het eindoordeel en de bespreekpunten. Alleen voornamen.
- De tutor zet per team (BC1, BC2) en per student (BC5, eindoordeel) expliciet de stap **„gekalibreerd”** *(keuze van de bouwer, na review)*. Wijzigt daarna een niveau of het eindoordeel, dan vraagt het hulpmiddel om een reden. Die reden is alleen voor de tutor.
- Een student krijgt pas de status „klaar” als alle bespreekpunten zijn afgevinkt.

### 3.4 Afronden (tutor)

Per student, alleen bij status „klaar”:

1. **Handin-tekst:** drie tot vier zinnen voor het veld „Eventuele toelichting”: het oordeel, de sterkste onderbouwing, de minimumeisen die ontbreken, wat nodig is voor januari, en de verwijzing naar de bijlage. Bewerkbaar, met een knop „kopieer”.
2. **Studentbijlage (pdf):** de studentweergave van het hulpmiddel, afgedrukt naar pdf (A4). Het hulpmiddel stelt de bestandsnaam voor, met groep en voornaam (bijv. `G3-<voornaam>-toelichting-Toets01.pdf`). Zie §4.

De tutor zet Voldaan/Niet voldaan zelf in Handin. Daarna zet hij in het hulpmiddel de status op „verstuurd”.

## 4. Het studentformulier (pdf-bijlage)

Volgorde van boven naar onder:

1. **Kop:** „Je beoordeling PRAKOP01-Toets01”, voornaam, groep, datum, tutor (voornaam).
2. **Het oordeel:** Voldaan of Niet voldaan, groot, met de Handin-zin („Uit de voortgang en de tussentijdse resultaten blijkt dat je je ontwikkelt naar de vereiste beheersing van de leeruitkomsten”) en de toelichting van de tutor.
3. **Per criterium een route** met de drie niveaus; de halte van het gegeven niveau is gemarkeerd met „jouw niveau” (niet „jij staat hier”). Daarbij:
   - teamcriteria gemarkeerd als „teamoordeel, geldt voor jullie hele team”;
   - de lichtjes: fragmenten die de tutor noemde, met de zin voor de student en „Teamdeel, p. 8” als tekst (geen link: de student heeft het eigen document);
   - de rubrictekst van het gegeven niveau;
   - de feed-forward van de tutor, als die is ingevuld.
4. **Minimumeisen portfolio:** de checklist als waffle per eis, met wat gehaald is en wat ontbreekt (met pagina). Ontbrekende eisen staan ook in de toelichting bij het oordeel.
5. **Denk verder:** de denkkaart van het prototype, als stilstaand beeld: per criterium een tak met de gekozen vragen als knooppunten, in socratische volgorde (verheldering, aanname, bewijs, perspectief, gevolg, de vraag zelf), verbonden aan het fragment of criterium waar ze over gaan. Daaronder dezelfde vragen als genummerde lijst met hun type. Bovenaan staat dat de vragen niet meetellen voor dit oordeel en bedoeld zijn om in de eindreflectie (Toets02) op terug te komen.

Opmaak: A4 staand, `@media print`, zwart-wit leesbaar (kleur als extra, niet als enige drager), elk criterium op een eigen pagina als het niet past. Geen interactie nodig om de pdf te begrijpen.

## 5. Data

Eén databestand per groep (`data-G1.js`, `data-G3.js`), vorm als `ontwerpen/data.js`, met deze uitbreidingen:

- `team` per groep met teamleden (voornamen) en teamdocumenten; `studenten[]` met voornaam, team, status en persoonlijke documenten.
- per fragment: `zinStudent` naast `notitie`; `doc` verwijst naar een document van het team of van een student.
- `checklist` per student.
- `socratisch` per criterium, met `bc`, `type`, `vraag`, en bij BC5 de student waarvoor de vraag is.

Invoer van de tutor (posities, niveaus, oordeel, teksten, bespreekpunten, statussen) staat in localStorage van het hulpmiddel, met een knop **„exporteer werkbestand”** (JSON) en **„importeer werkbestand”**, zodat werk niet verloren gaat als de browseropslag wordt gewist.

## 6. Techniek

- Eén HTML-bestand voor het hulpmiddel van de tutor, plus de databestanden en viewer-pdf's ernaast; HAN-huisstijl (accent `#E50056`, zwart-wit, dikke randen met harde schaduw), systeemlettertypen.
- D3 7.9.0 en Motion 11.11.13 van de CDN.
- De tutor opent het hulpmiddel via een lokale server (`python3 -m http.server` in de map, gestart vanuit een eigen terminal), omdat de pdf-viewer en de databestanden via file:// in de app-browser niet laden.
- De studentweergave toont alleen de gegevens van die ene student en het eigen team; de tutor maakt er met de afdrukfunctie van de browser een pdf van.
- `prefers-reduced-motion`: geen krachtsimulatie-animatie, geen opgloeien; alles blijft bruikbaar.

## 7. Testen

- Het hulpmiddel opent zonder consolefouten met de data van G1 en van G3.
- Elke paginaverwijzing opent de viewer-pdf op een pagina waarop het citaat staat (steekproef van tien per groep, met `pdftotext`).
- Geen achternamen, klascodes, studentnummers of e-mailadressen in databestanden, viewer-pdf's en studentbijlagen (grep op de bekende achternamen uit de oorspronkelijke download).
- De pdf van de studentweergave is leesbaar op A4 en op een telefoon, de denkkaart staat er volledig op, en er staat niets in dat alleen met klikken te zien is.
- Een notitie van de tutor verschijnt nergens in de studentbijlage.
- Het teamoordeel op BC1 en BC2 is bij alle teamleden gelijk.

## 8. Beantwoord na review (17 november 2026)

1. De minimumeisen van het portfolio tellen al bij Toets01 (§3.2).
2. Handin accepteert alleen pdf; de bijlage is een pdf (§3.4, §4).
3. Het beoordelen begint vandaag; het plan levert eerst het bord, het oordeel en de Handin-tekst (§2, Tijdpad).

## 9. Buiten scope

- Het oordeel invoeren in Handin (blijft handwerk van de tutor).
- Andere groepen dan G1 en G3, en Toets02.
- Studenten zonder inlevering beoordelen: het hulpmiddel toont ze, maar maakt geen formulier.
- Automatisch fragmenten zoeken binnen het hulpmiddel: dat doet Claude in de voorbereiding.
