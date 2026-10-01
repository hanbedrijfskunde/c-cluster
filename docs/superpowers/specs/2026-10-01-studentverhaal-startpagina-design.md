# Ontwerp: het verhaal voor studenten op de startpagina

**Status:** ontwerp, ter review
**Datum:** 1 oktober 2026
**Product:** hybride e-learning A3 (repository `hanbedrijfskunde/a3-learning`), startpagina `index.html`
**Na akkoord:** vastleggen in LRD 0.26 (FR-75, AC-51, noot onder Purpose in Deel 5; voor B118 ook FR-44, NFR-07, AC-08, de scope-regel en het weekprogramma), ADR (B113 en B118; B42 en B53 krijgen „deels vervangen door B118”), BLUEPRINT (ST-8, ST-9, DL-2, LB-1, PF-5, TK-14, Bijlage A en B) en DESIGN (§5.1, §5.2); daarna bouwen in a3-learning. De nummers zijn afgestemd met de parallelle sessies: B112, LRD 0.21, FR-74, AC-50 en SX-20 (infovenster metrokaart), B114 en LRD 0.23 (verdieping leerblok 4), B115 en LRD 0.25 (kijktip Yale), B117 (feit of aanname). LRD 0.22 en daarna 0.24 waren voor dit ontwerp gereserveerd; omdat 0.23 en 0.25 eerder klaar waren, wordt deze ronde op besluit van de auteur 0.26, zodat geen eerdere versie achteraf van inhoud verandert. 0.22 en 0.24 blijven ongebruikt.

**Uitbreiding (1 oktober 2026, verzoek van de auteur tijdens de uitvoering):** de studentintroductie krijgt een onderwerp over tijdsinzet en planning bij zelfstudie (§9), en de richttijd per leerblok volgt voortaan de taken (§10, B118), zodat de tijd die studenten lezen klopt.

## 1. Doel

Een student die de site opent, komt nu meteen bij het formulier „Begin met je eigen vraagstuk”. Waarom de e-learning bestaat, hoe je ermee werkt en wat je eraan overhoudt, staat nergens op de site. De docent krijgt dat verhaal wel, in de inleiding van de docentgids (B101). De studentintroductie (`docs/studentintroductie.html`, DL-2) is een bijsluiter: wat je doet, waar je gegevens staan, hoe je inlevert. DESIGN §5.1 vraagt al om „bovenaan één zin wat de student hier aan de A3 overhoudt, en één knop”; dat is niet gebouwd.

De startpagina krijgt daarom bovenaan hetzelfde verhaal als de docentgids, in de taal van de student en in de volgorde van de Golden Circle: eerst waarom, dan hoe, dan wat.

Purpose: de student leest eerst het probleem dat hij of zij deze week echt heeft (de vage vraag van de opdrachtgever), en pas daarna wat de site vraagt. Dat versterkt het zwakke punt dat het LRD zelf onder Purpose noemt: „Het is bewijs voor het portfolio” is een externe reden. Autonomy: het verhaal blokkeert niets; wie terugkomt, ziet het ingeklapt. KISS: geen nieuwe pagina, en de tekst staat in de data zoals alle andere studenttekst.

## 2. Besluiten uit het gesprek

| Vraag | Keuze van de auteur | Afgewezen |
|---|---|---|
| Waar staat het verhaal | Bovenaan de startpagina, bij een eerste bezoek boven het formulier; bij een terugkerend bezoek ingeklapt | een aparte pagina `welkom.html` als ingang (negende pagina en een klik extra; B80 wees een negende pagina al af); de studentintroductie herschrijven en de link prominenter maken (blijft een document waar je heen moet klikken, geen landing) |
| Vorm | Drie korte blokken met een vraag als kop, samen hoogstens 150 woorden; de Golden Circle bepaalt de volgorde maar wordt niet genoemd | de Golden Circle als figuur met drie ringen (een extra model dat niets met de A3 te maken heeft; noem je het, dan moet de figuur erbij, DESIGN-principe 8); één lopende alinea zonder koppen (de opbouw verdwijnt, wie scant slaat hem over) |
| Waarmee opent het waarom | Het probleem van de opdrachtgever: een vage vraag, het risico het verkeerde probleem op te lossen, de onderzoeksvraag die je op je A3 met de opdrachtgever bespreekt. Het portfolio komt als één zin in het blok „wat” | het portfolio als waarom (de externe reden die het LRD zwak noemt); beide even zwaar in het waarom (langer, de kern minder scherp) |
| Waar komt de voorlichting over tijd en planning | Een onderwerp „Tijd en planning” in de studentintroductie (DL-2 van 3 naar 4 onderwerpen, blijft 1 A4); het blok „wat” van het verhaal noemt de totale tijd en de linkregel noemt tijd, planning en inleveren (§9) | een vierde blok „Hoeveel tijd kost het?” in het verhaal (breekt waarom-hoe-wat en de grens van 150 woorden); alleen in de introductie (de student ziet op de startpagina niet hoeveel tijd het kost) |
| Welke tijd noemen we bij leerblok 3 | Gelijktrekken: de richttijd van elk leerblok is de som van zijn taken (leerblok 1 30 min, 3 105 min), op de kaart, in het verhaal en in de introductie hetzelfde getal (§10, B118) | eerlijk in de tekst en de kaart later (twee verschillende tijden op één startpagina); 45 minuten aanhouden en in de pilot meten (studenten in zelfstudie lopen bij leerblok 3 vrijwel zeker uit) |
| Waar staat de tekst | In `data/leerblokken.json` onder `start.verhaal`, getekend door `js/index-pagina.js` | vaste HTML in `index.html` (werkt zonder JavaScript, maar `index-pagina.js` maakt `main` leeg en de tekst staat dan als enige studenttekst buiten de data, buiten bereik van de contentcontrole en van de docent die teksten aanpast zonder code, docentgids §5) |

## 3. Wat de student ziet

### 3.1 Eerste bezoek

Onder de metrokaart (die `metro.js` buiten `main` zet, B110) en de h1, en boven „Begin met je eigen vraagstuk”:

```
┌─────────────────────────────────────────────────────────────┐
│ WAAR GAAT DIT OVER?                                  (h2)   │
│ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐          │
│ │ Waarom dit?  │ │ Hoe werk je? │ │ Wat heb je   │   (h3)   │
│ │ …            │ │ …            │ │ aan het eind?│          │
│ └──────────────┘ └──────────────┘ └──────────────┘          │
│ [ Start met je vraagstuk ]                                  │
│ Hoe je je werk bewaart en inlevert, lees je in de           │
│ introductie van één pagina.                                 │
└─────────────────────────────────────────────────────────────┘
```

- Een `<section id="verhaal" aria-labelledby="verhaal-kop">` met de kop „Waar gaat dit over?” als h2 in de bestaande `.eyebrow`-stijl.
- Drie blokken als `.kaart` (rand, geen schaduw: informatie, niet aantikbaar, SX-7), elk met een h3 en één alinea. Ze staan in een raster `repeat(auto-fit, minmax(14rem, 1fr))`: op een telefoon onder elkaar, op een breed scherm naast elkaar. Er komt geen nieuw breekpunt bij.
- Een gewone knop „Lees dit eerst voor je start” naar `docs/studentintroductie.html` (wit, harde schaduw), en daarnaast één accentknop „Start met je vraagstuk” (het label uit DESIGN §4). Toegevoegd op verzoek van de auteur tijdens de bouw; de accentknop blijft de hoofdactie. Een klik zet de focus in het veld `#start-alias`; de browser scrolt daar vanzelf naartoe.
- Daaronder een kleine regel met de link naar `docs/studentintroductie.html`: „Hoeveel tijd het kost, hoe je plant en hoe je inlevert, lees je in de introductie van één pagina.” Die vervangt de huidige regel „Nieuw hier? Lees de introductie van één pagina.” in de sectie `#start`.

### 3.2 Terugkerend bezoek

- Het verhaal wordt een ingeklapte `<details class="verhaal-details">` met de samenvatting „Waar gaat dit over?” en dezelfde drie blokken. Er staat geen knop in: wie terugkomt, heeft het formulier al gezien.
- Plaats: onder de vier leerblokken, boven „Jouw gegevens”. Wat bovenaan staat (Verder waar je was, A3-vak 1, de leerblokken; DESIGN §5.2) blijft daardoor op zijn plek.
- De samenvatting krijgt de opmaak van de bestaande `details`-samenvattingen op de site, met een hoogte van minstens 2,75rem (al geregeld voor `summary`).

### 3.3 Tekst

Geredigeerd met `redigeer-nederlandse-tekst` en `schrap-ai-taal` (0 meldingen); 140 woorden lopende tekst. Goedgekeurd door de auteur op 1 oktober 2026.

> **Waarom dit?**
> Je opdrachtgever komt met een vraagstuk dat nog vaag is. Begin je meteen aan een oplossing, dan los je misschien het verkeerde probleem op. Hier maak je van dat vraagstuk een onderzoeksvraag waar je team mee verder kan. Die bespreek je met je opdrachtgever op je A3.
>
> **Hoe werk je?**
> Bij elke taak oefen je eerst op een voorbeeld, webshop X. Daarna doe je dezelfde opdracht voor je eigen vraagstuk. Je ziet steeds wanneer je klaar bent, en de site controleert meteen of alles erin staat. Je hebt geen account nodig: alles blijft in deze browser.
>
> **Wat heb je aan het eind?**
> Je doet vier leerblokken, samen ongeveer 4½ uur. Daarna is het eerste vak van je A3 gevuld. Daarin staan je onderzoeksvraag, betrouwbare bronnen en de mensen en de organisatie rond je vraagstuk. En je hebt een dossier met al je werk, dat je inlevert voor je portfolio.

De 4½ uur is de som van de richttijden (30 + 45 + 105 + 45 = 225 min) plus drie terugblikken van hoogstens 15 min (45 min), afgerond op een half uur. Een test rekent dat na uit de data (§10), zodat de zin niet stil gaat afwijken als een richttijd verandert.

**Grenzen voor de tekst** (ook voor latere aanpassingen door een docent):

- Geen Wissel, verdieping, „Mijn stand” of „kopieer naar A3”: die zijn op de eerste schermen niet zichtbaar en worden er ook niet genoemd (ST-7, FR-66).
- Geen systeemtaal: geen LUK, BC, EV-codes, „bewijsonderdeel” of „richttijd” (DESIGN §8). Je-vorm, actief, kort.
- De Golden Circle, Sinek, WHY, HOW en WHAT worden niet genoemd.
- Hoogstens 150 woorden lopende tekst in de drie blokken samen, koppen en knop niet meegeteld.

## 4. Gedrag

**Open of ingeklapt.** Bij het laden van de pagina beslist `verhaalOpen(profiel, records)`:

- open (eerste bezoek) als het profiel leeg is (alias, teamnummer, vraagstuk en waarom-zin leeg, en „nog geen scherp vraagstuk” uit) **en** er geen enkel werkrecord is;
- anders ingeklapt (terugkerend).

De beslissing valt alleen bij het laden. Typen in het formulier bewaart het profiel bij elke toets (`bijwerken`); zou het verhaal daarop reageren, dan klapt het in bij het eerste teken en verspringt de pagina terwijl de student schrijft.

**Wis alles.** Na „Wis alles” blijft het verhaal in de stand waarin het stond, tot de pagina opnieuw laadt. Een live omschakeling is extra code voor een moment dat zelden voorkomt (KISS).

**Zonder JavaScript.** Geen verhaal; dat geldt nu al voor de hele startpagina. De `<noscript>`-melding blijft.

**Zonder opslag.** Valt `kiesOpslag` terug op geheugen, dan is het profiel bij elk laden leeg en staat het verhaal steeds open. Dat is juist: zo'n student begint elke keer opnieuw.

**Afdrukken.** Het verhaal mag op papier staan; `print.css` hoeft niets te verbergen.

## 5. Architectuur

Hetzelfde patroon als de rest van de startpagina: de beslissing zonder DOM is apart te testen, de tekst staat in de data.

| Eenheid | Rol | Hangt af van |
|---|---|---|
| `data/leerblokken.json` | Nieuw object `start.verhaal`: `{ "kop": "Waar gaat dit over?", "blokken": [{ "id": "waarom", "kop": "Waarom dit?", "tekst": "…" }, { "id": "hoe", … }, { "id": "wat", … }], "knop": "Start met je vraagstuk", "introductie": { "tekst": "Hoe je je werk bewaart en inlevert, lees je in de", "link": "introductie van één pagina" } }`. De pagina zet de link achter `tekst` en sluit af met een punt | `tools/content-check.mjs` (`controleerOverzicht`) controleert de vorm, de woordgrens en de verboden termen; `tests/taal.test.mjs` leest alleen `data/leerblok-N.json`, dus die controle zit in content-check |
| `js/weergave.js` | `verhaalOpen(profiel, records)` → `true` of `false`. Geen DOM. | — |
| `js/index-pagina.js` | Tekent het verhaal: open als `<section id="verhaal">` vóór `#start`, ingeklapt als `<details class="verhaal-details">` na `#blokken`. Haalt de regel „Nieuw hier?” uit `#start`. | `weergave.js`, `profiel.js` (`leesProfiel`), `afgerond.js` (`leesRecords`), `dom.js` (`h`) |
| `css/site.css` | Een nieuw blok `.verhaal` (raster van de drie kaarten, ruimte rond de knop) en `.verhaal-details`. Niet in het metroblok onderaan (dat wijzigt de sessie van B112). | — |

De pagina laadt geen nieuw bestand: `data/leerblokken.json` wordt al geladen. Er komen ongeveer 1,5 kB tekst en code bij; de gewichtscontrole blijft ruim binnen 300 kB gzip.

**Foutgevallen.** Ontbreekt `start.verhaal` in de data, dan tekent de pagina geen verhaal en werkt de rest gewoon. De content-check meldt het ontbrekende object als fout, zodat het niet ongemerkt live gaat.

## 6. Toegankelijkheid en kleine schermen

- Kopstructuur: h1 (pagina) → h2 „Waar gaat dit over?” → drie h3. In de ingeklapte versie is de samenvatting de toegang; de h3's staan erin.
- De knop is een `<button type="button">` met de bestaande `.knop .knop-accent`, minstens 2,75rem hoog. Na de klik staat de focus in `#start-alias` (zichtbaar met de focusrand van 4 px).
- Op 360 px staan de blokken onder elkaar, zonder horizontaal scrollen; lange woorden breken af (`overflow-wrap:anywhere` geldt al voor h2, h3 en p).
- Contrast en kleur: alleen bestaande tokens (zwart, wit, accent). Geen beweging.

## 7. Testen

- **Beslissing** (`tests/weergave.test.mjs`): leeg profiel en geen records → open; alleen een alias → ingeklapt; alleen „nog geen scherp vraagstuk” aangevinkt → ingeklapt; leeg profiel met één record → ingeklapt; profiel met spaties alleen → open.
- **Data** (`controleerOverzicht` in `tools/content-check.mjs`, getest in `tests/content-check.test.mjs`; de drie fixtures met een eigen `leerblokken.json` krijgen het verhaal erbij): `start.verhaal.blokken` heeft precies drie blokken met de id's `waarom`, `hoe`, `wat` in die volgorde; hoogstens 150 woorden lopende tekst; geen van de termen Wissel, verdieping, Mijn stand, kopieer naar A3, LUK, BC, EV-, bewijsonderdeel, richttijd, Golden Circle, Sinek.
- **Pagina** (browsercheck met Playwright, op een lokale server): bij lege opslag staat `#verhaal` vóór `#start` en is het open; met een opgeslagen profiel is er geen `#verhaal`-sectie maar een gesloten `.verhaal-details` na `#blokken`; de knop zet de focus in `#start-alias`; op 360 px geen horizontale scroll; de regel „Nieuw hier?” staat niet meer in `#start`.
- **Introductie** (`tests/docs.test.mjs`, DL-2): vier onderwerpen in de volgorde wat je doet, tijd en planning, gegevens, exporteren en inleveren; hoogstens 550 woorden; in „Tijd en planning” staat voor elk leerblok „± N min” met N uit `data/leerblokken.json`, en de totale tijd. De afdruk uit Chrome is 1 pagina A4.
- **Tijd** (§10): richttijd = som van de taken voor elk leerblok, in `leerblokken.json` en in `leerblok-N.json`; de totale tijd in het blok „wat” en in de introductie is gelijk aan (som richttijden + som terugblik), afgerond op een half uur; de terugblikpagina noemt de richttijd van het eigen leerblok.
- **Bestaande controles**: ST-7 (geen Wissel, verdieping, „Mijn stand” of „kopieer naar A3” op de eerste schermen), de taalcontrole, de content-check en de gewichtscontrole blijven groen.

## 8. Buiten scope

- De andere drie onderwerpen van de studentintroductie blijven zoals ze zijn. De overlap tussen „Wat je doet” en het blok „Hoe werk je?” is klein en bewust: de introductie is voor wie het op papier wil hebben.
- De taken van leerblok 3 inkorten tot 45 minuten. B118 maakt de tijd eerlijk; of leerblok 3 korter moet, is een didactische vraag voor na de pilot (AC-08).
- De docentmodus en de draaiboeken: hun tijden (deel 1 90 min, deel 2 145 min) staan los van de richttijd per leerblok en veranderen niet.
- Een omrekening van minuten naar uren op de leerblokkaart: die blijft „± 105 min” tonen (DESIGN §8: „± 10 min”).
- Een andere h1 voor de startpagina („De A3 en je vraag: start”).
- Het profiel één veld per scherm (DESIGN §5.1, tweede punt). Dat is een losse wijziging.
- Een video of figuur bij het verhaal.

## 9. Tijd en planning in de studentintroductie

De studentintroductie (`docs/studentintroductie.html`) krijgt een tweede onderwerp, tussen „Wat je doet” en „Waar je gegevens staan”. DL-2 gaat van 3 naar 4 onderwerpen en van hoogstens 450 naar hoogstens 550 woorden; de introductie blijft 1 A4 (gemeten met de afdruk van Chrome, zoals in B72). Tekst, geredigeerd met beide skills (0 meldingen), goedgekeurd door de auteur op 1 oktober 2026:

> **2. Tijd en planning**
>
> De vier leerblokken kosten samen ongeveer 4½ uur:
>
> - Leerblok 1: ± 30 min
> - Leerblok 2: ± 45 min, plus hoogstens 15 min terugblik
> - Leerblok 3: ± 105 min, plus hoogstens 15 min terugblik
> - Leerblok 4: ± 45 min, plus hoogstens 15 min terugblik
>
> Werk je zelfstandig? Zet elk leerblok als een afspraak in je agenda. Leerblok 3 kun je over twee keer verdelen: de site onthoudt bij welke taak je was. Bij elk leerblok staat wanneer het in het programma aan de beurt is; heb het dan af. Begin op tijd, zodat er tussen twee leerblokken een paar dagen zit. Het volgende leerblok begint met een terugblik: je schrijft uit je hoofd op wat je nog weet. Zo onthoud je het beter.

Het advies volgt uit het ontwerp: de terugblik is gebouwd op spreiden en ophalen (LRD 2.8); bij een pauze van 2 tot en met 13 dagen krijgt de student de volledige terugblik (`data/terugblik.json`, band „volledig”). „De site onthoudt bij welke taak je was” is „Verder waar je was” (DESIGN §5.2), in dezelfde browser.

De introductie heeft onderaan een knop „Start” naar `../index.html`; op papier staat die niet. Om op 1 A4 te blijven heeft `docs/gids.css` voor de afdruk iets krappere witruimte (lijsten .3rem, koppen .8rem, compacte voettekst); de goedgekeurde tekst blijft ongewijzigd.

Op de startpagina noemt het blok „Wat heb je aan het eind?” de totale tijd (§3.3) en luidt de linkregel: „Hoeveel tijd het kost, hoe je plant en hoe je inlevert, lees je in de introductie van één pagina.”

## 10. De richttijd volgt de taken (B118)

**Wat er mis is.** B68 (punt 6) zag het al: de werkboektijden van leerblok 3 tellen teamwerk aan de muur mee, en de ijking stond voor de pilot gepland. De auteur kiest toch voor de som van de taken: een student in zelfstudie plant liever te ruim dan te krap, en de pilot (AC-08) blijft de tijd ijken. Elk leerblok heet „± 45 min” (B42, FR-44, NFR-07, PF-5), en `content-check` eist dat. Maar de taken van leerblok 3 tellen volgens het werkboek op tot 105 minuten (5.1, 6.1, 7.1 en 8.1 elk 20, 9.1 15, 9.2 10), en deel 2 van het werkcollege duurt 145 minuten. Leerblok 1 telt op tot 30 minuten. Een student in zelfstudie die op 45 minuten plant, loopt bij leerblok 3 een uur uit.

**Regel.** De richttijd van een leerblok is de som van de richttijden van zijn taken; de verdieping telt niet mee (TK-14). De terugblik van hoogstens 15 minuten komt er vanaf leerblok 2 bovenop (B53). Nu: leerblok 1 30 min, 2 45 min, 3 105 min, 4 45 min; samen 225 min, met terugblikken hoogstens 270 min (4½ uur).

**Eén bron.** De taken in `data/leerblok-N.json` zijn de bron. Het veld `richttijd` bovenaan `leerblok-N.json` en de `richttijd` per leerblok in `leerblokken.json` volgen die som; `content-check` controleert dat (in `controleerMap`, waar beide bestanden samenkomen) in plaats van „precies 45”. Wie een taaktijd aanpast, krijgt dus een fout tot de richttijd mee is aangepast.

**Wat er verandert.**

| Waar | Wijziging |
|---|---|
| `data/leerblokken.json` | richttijd leerblok 1 → 30, leerblok 3 → 105 |
| `data/leerblok-1.json`, `data/leerblok-3.json` | veld `richttijd` bovenaan → 30 en 105 (geen taken) |
| `tools/content-check.mjs` | `richttijd !== 45` vervalt; nieuw: richttijd = som van de taken, en overzicht = leerblokbestand |
| `js/terugblik-pagina.js` | „bovenop de 45 min van het leerblok” → de richttijd van dat leerblok |
| tests | PF-5 (`toegankelijk`), LB-1 (`weergave`, `content-check`) en TK-14 (`lb4`) toetsen de som in plaats van 45 |
| `docs/docentgids.html` | „Vier leerblokken van 45 minuten” → de vier tijden en de terugblik |
| LRD | FR-44, NFR-07, AC-08 („1,25 keer de richttijd van dat leerblok”), de scope-regel, het weekprogramma (Deel 8) en de andere vermeldingen van „45 min” |
| BLUEPRINT | LB-1, PF-5 en TK-14: „45 min” → „de som van de taken” |
| ADR | B118; B42 en B53 krijgen in de statuskolom „deels vervangen door B118” |

De leerblokkaart en de kop van de leerblokpagina tonen de richttijd al uit de data („± 105 min”); daar verandert geen code.
