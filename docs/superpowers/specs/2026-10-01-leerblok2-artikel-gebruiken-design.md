# Ontwerp: leerblok 2, een artikel gebruiken als meer dan een kennisbron

**Status:** ontwerp, ter review
**Datum:** 1 oktober 2026
**Product:** hybride e-learning A3 (repository `hanbedrijfskunde/a3-learning`), leerblok 2
**Na akkoord:** vastleggen in LRD (nieuwe versie), ADR (B101, B102), BLUEPRINT en BUILDPLAN; daarna bouwen.

## 1. Doel

Na het vinden en beoordelen van een artikel leert de student het artikel te gebruiken als bron van
meer dan kennis: van **theorie** (modellen, begrippen, definities), van **methode** (hoe data
verzameld en verwerkt zijn) en van **presentatie** (hoe de uitkomst getoond wordt). Wat hij eruit
haalt, neemt hij mee naar zijn eigen A3. IMRAD (Wu, 2011) wijst hem waar hij moet kijken.

Studenten zullen AI gebruiken om artikelen te ontleden. Dat mag; de e-learning begeleidt het zo dat
de student het artikel zelf blijft openen en controleren.

Basis is een oefening uit het afstudeertraject (drie artikelen; per artikel theoretisch kader,
dataverzameling en -verwerking, compilatie en visualisatie; afsluitende reflectie). Die is hier
verkleind tot één artikel per student binnen 15 minuten.

## 2. Besluiten uit het gesprek

| Vraag | Keuze van de auteur | Afgewezen |
|---|---|---|
| Ruimte | Binnen de 45 minuten van leerblok 2 (NFR-07) | eigen leerblok; richttijd omhoog |
| Aantal artikelen | Eén artikel per student in de toepassing | team verdeelt artikelen; drie korte |
| AI | AI mag; bij elk antwoord een vindplaats die de student zelf heeft nagekeken | eerst zelf dan AI (dubbele tijd); AI alleen als leesmaatje |
| Indeling | Aanpak A: nieuwe taak 4.2 na het beoordelen | B: beoordelen en ontleden in één taak (EV-04 verandert, loopt niet gelijk met werkboek 4.1); C: ontleden als optionele verdieping (dan geen doel van het leerblok) |
| Oefening | Duo; twee verschillende fictieve mini-artikelen, daarna vergelijken | beiden hetzelfde artikel |
| Werkboek week 5 | Alleen de e-learning; werkboek en draaiboek blijven gelijk | ook werkboek en draaiboek (geen 15 minuten vrij in het werkcollege) |

## 3. Nieuwe indeling van leerblok 2

Titel: **Zoeken, beoordelen en gebruiken**. Eindigt met: **Een beoordeeld en ontleed artikel**.

| Taak | Titel | Vorm | Richttijd | Bewijs | Verandering |
|---|---|---|---|---|---|
| 3.1 | Zoektermen | Team | 5 | — | geen |
| 3.2 | Wedstrijd: vind een goede bron | Team | 10 | EV-03 | geen (oefening in duo's blijft, B100) |
| 4.1 | Is de bron betrouwbaar? | Team | 10 | EV-04 | één keuzeveld „Soort bron” erbij; één zin in de stof |
| 4.2 | Haal meer uit je artikel | Duo, dan alleen | 15 | **EV-12** | nieuw |
| 4.3 | Stelling over AI | Alleen | 5 | EV-05 | was 4.2; nieuwe stelling |

Samen 45 minuten, zonder speling.

## 4. Taak 4.2 „Haal meer uit je artikel”

### 4.1 Waarom (concept)

„Een artikel vertelt je wat er bekend is. Maar je kunt er meer uit halen: een begrip voor je analyse,
een manier om data te verzamelen, en een manier om je uitkomst te laten zien. IMRAD wijst je waar je
dat vindt.”

### 4.2 Klaar als (concept)

„je bij Inleiding, Methode en Resultaten van je artikel hebt opgeschreven wat de auteur doet, waar dat
staat en of je het meeneemt, en in een korte alinea hebt opgeschreven wat je meeneemt naar je A3.”

### 4.3 Stof

- **Figuur `imrad`** (eigen SVG, in een nieuw `js/figuren-lb2.js`, alleen geladen als de data hem
  gebruikt, zoals B97): de IMRAD-zandloper. I van breed naar smal, M en R smal, D van smal naar breed.
  Per deel de vraag van het deel (Waarom? Hoe precies? Wat gevonden? Wat betekent het?) en wat jij
  eruit haalt: I → theorie, M → methode, R → presentatie, D → betekenis en beperkingen. Geen tekst of
  figuur overgenomen uit Wu (2011); het artikel wordt alleen geciteerd.
- **Alinea 1:** wat IMRAD is en waarom bijna elk onderzoeksartikel zo is opgebouwd (Wu, 2011).
- **Alinea 2:** lees niet van voor naar achter: eerst de samenvatting, dan de figuren en tabellen,
  dan de methode, daarna de rest.
- **Alinea 3:** AI mag helpen. Gebruik de prompt bij deze taak. Een AI-tool kan een citaat of een
  methode verzinnen; geef daarom bij elk antwoord een vindplaats die je zelf in het artikel hebt
  teruggevonden.

### 4.4 Oefening (duo, oefencasus webshop X)

Twee fictieve mini-artikelen van ongeveer 250 woorden, met IMRAD-kopjes, zichtbaar gemarkeerd als
fictief (zoals de fictieve bronkaart, MD-15), beide over klanttevredenheid bij webshops:

- **Artikel 1, sterk in theorie.** Bouwt op een bestaand, echt model van klanttevredenheid (bijv. het
  disconfirmatiemodel: verwachting tegenover ervaring) en definieert de begrippen; methode summier
  (een paar interviews); resultaten in lopende tekst.
- **Artikel 2, sterk in methode en presentatie.** Weinig theorie; een enquête onder klanten met een
  heldere steekproef en analyse; de uitkomst in één staafdiagram (eigen SVG) met de kernboodschap in
  de titel.

Het echte model in artikel 1 wordt met bron genoemd en staat in het bronregister; de artikelen zelf
staan als fictief in `bronnen-2.json`.

Velden:

| Veld | Type | Inhoud |
|---|---|---|
| `artikel` | keuze | Artikel 1 / Artikel 2 |
| `theorie` | tekst | I: waar komt de theorie vandaan? |
| `theorieWaar` | lijst | vindplaats: Inleiding / Methode / Resultaten / Discussie |
| `methode` | tekst | M: hoe zijn de data verzameld en verwerkt? |
| `methodeWaar` | lijst | vindplaats |
| `presentatie` | tekst | R: in welke vorm staat de uitkomst? |
| `presentatieWaar` | lijst | vindplaats |
| `vergelijking` | lang | samen: welk artikel levert jullie het meest voor theorie, voor methode en voor presentatie? |

Elk veld heeft een hint met vindplaats (SX-13, B85, TK-19). Het modelantwoord geeft beide artikelen
en een voorbeeldvergelijking en verschijnt pas na eigen werk: `modelNa: ["theorie", "methode",
"presentatie", "vergelijking"]` (B100). De keuze van het artikel alleen toont het model niet.

### 4.5 Toepassing (alleen, eigen artikel)

- `titel` (afgeleid van 4.1, `b1titel`) en `soort` (afgeleid van 4.1). Is het geen onderzoeksartikel,
  dan een melding: „Kies voor deze taak een artikel met een methode en resultaten. Dat mag ook een
  andere bron uit 3.2 zijn.” Een eigen titelveld laat de student dan een ander artikel invullen.
- Per deel I, M en R drie velden: **Wat doet de auteur?** (lang, 1–2 zinnen), **Vindplaats** (tekst:
  sectie of pagina), **Neem ik dit mee?** (keuze ja / deels / nee) met **waarom** (tekst, één zin).
- **Dit neem ik mee naar mijn A3** (lang): een korte alinea over theorie, methode en presentatie samen.
- **AI-begeleiding:** keuze „Heb je AI gebruikt?” (nee / om te begrijpen / om te ontleden). Bij „om
  te ontleden” verschijnt een kopieerbare prompt (vast, met de titel ingevuld) en het vinkje „Ik heb
  elk citaat en elke vindplaats zelf in het artikel teruggevonden.”

Concept van de prompt:

> „Ik lees dit artikel: [titel]. Geef voor de Inleiding, de Methode en de Resultaten apart: (1) in één
> of twee zinnen wat de auteurs daar doen; (2) één letterlijk citaat dat dat laat zien, met
> paginanummer. Bij de Inleiding: welke modellen, begrippen of definities gebruiken ze, en van wie
> komen die? Bij de Methode: hoe verzamelden en verwerkten ze de data? Bij de Resultaten: in welke vorm
> tonen ze de uitkomst (tabel, grafiek, model)? Verzin niets. Staat iets niet in het artikel, zeg dat
> dan.”

### 4.6 Bewijs EV-12 „Ontleed artikel” (LUK 1 · Gebruikt en beoordeelt bronnen)

| Controle | Soort | Regel |
|---|---|---|
| `imr-ingevuld` | A | I, M en R hebben elk een antwoord |
| `imr-vindplaats` | A | elke vindplaats is ingevuld en ziet eruit als een sectie of pagina (sectienaam als Inleiding, Introduction, Methode, Method(s), Resultaten, Results, Discussie, Discussion, Conclusie; of p./pp./pagina/blz. met een getal; of § met een getal) |
| `imr-meenemen` | A | bij I, M en R een keuze ja/deels/nee |
| `oogst-zinnen` | B | de alinea voor de A3 heeft minstens drie zinnen |
| `ai-geverifieerd` | A | bij AI „om te ontleden”: het vinkje staat |

Compleet: alle controles ok. Bijna: alleen soort B mist of één controle van soort A. Nog niet: anders.
(De precieze statusregel volgt het bestaande patroon in `js/status.js`.)

## 5. Andere wijzigingen

- **4.1:** keuzeveld `b1soort` „Soort bron” (onderzoeksartikel / vakartikel / anders), telt niet mee
  voor EV-04. Stofzin: „Kies voor 4.2 een onderzoeksartikel, met methode en resultaten.”
- **4.3 (was 4.2):** stelling „Je kunt een artikel prima door AI laten ontleden.” Kant en argument,
  EV-05, controles ongewijzigd. Hint verwijst naar eigen werk bij 4.2.
  *Gevolg:* het werkcollege (dia 24, werkboek) houdt de oude stelling over AI en inspiratiemateriaal
  (B17). Studenten zien in het lokaal en online dus twee stellingen. `docent-deel1.json` (d1-09) gaat
  naar taak 4.3 en de docentgids noemt het verschil.
- **Omzetting bij hernummeren:** EV-05-records hangen aan het bewijs-ID, maar `klaar:`, `oefening:`,
  `invoer:` en `positie:` hangen aan het taaknummer. Bij het laden van leerblok 2 zet de site eenmalig
  de metasleutels van 4.2 om naar 4.3 als er een EV-05-record bestaat en nog geen EV-12-record, en past
  het `taak`-veld van het EV-05-record aan. Getest met een dossier van vóór de wijziging.
- **Terugblik leerblok 3** (`terugblik.json`, LRD 8.5): vraag „Noem de vier delen van IMRAD, en wat
  haal je uit I, M en R?”; de meenemen-kaart noemt EV-12.
- **Leerblok-overzicht** (`leerblokken.json`): titel, `afgerondBewijs`, `bewijsonderdelen` met EV-12.
- **Bronnen:** Wu (2011) en de bron van het model in artikel 1 in `bronnen-2.json`; de twee
  mini-artikelen als `fictief: true`.
- **Dossierschema:** EV-12 als nieuw bewijsonderdeel; schemabeschrijving en docentpagina bijwerken.

## 6. Documenten

- **LRD:** nieuwe versie: FR-eis voor taak 4.2, EV-12 in de bewijstabel, AC voor de vindplaatscontrole
  en de omzetting, risico „AI-citaten die niet kloppen”, NFR-07-tabel met de nieuwe tijden.
- **ADR:** B101 (nieuwe indeling, met de afgewezen aanpakken B en C en de andere afwijzingen uit §2),
  B102 (AI-begeleiding met verplichte vindplaats en vinkje).
- **BLUEPRINT:** nieuwe LB-regels voor 4.2, EV-12-regel, aanpassing LB-8 (stelling), bijlage A.
- **BUILDPLAN:** nieuwe fase met een eind dat een tester kan proberen.

## 7. Toetsing (PAMS + KISS, kort)

- **Purpose:** de oogst gaat expliciet naar de eigen A3 (theorie voor de analyse, methode voor de
  diagnose, presentatie voor het vel).
- **Autonomy:** eigen artikel, eigen keuze wat mee te nemen, AI toegestaan; „Ik ken dit al” bij de
  oefening blijft.
- **Mastery:** eerst geleid oefenen op korte artikelen met modelantwoord, dan transfer; vindplaats als
  direct controleerbare maat.
- **Social:** duo-oefening met twee verschillende artikelen en een gezamenlijke vergelijking.
- **KISS:** D zonder eigen vraag; één artikel per student; één prompt; afgewezen alternatieven in §2.

## 8. Testen

- Inhoudscontrole (`tools/content-check.mjs`) slaagt, inclusief hints, `modelNa`, figuur en bronnen.
- Unit-tests per controle (3 goede en 3 zwakke voorbeelden, QA-2), voor de vindplaatsregel en voor de
  omzetting 4.2 → 4.3.
- Statustests voor EV-12 (Compleet, Bijna, Nog niet) en de AI-route.
- Gewichtscontrole (PF-4) voor leerblok 2 met de nieuwe figuren.
- Doorloop in de browser: oefening in duo, toepassing met en zonder AI, melding bij vakartikel.
