# Ontwerp: het verhaal voor studenten op de startpagina

**Status:** ontwerp, ter review
**Datum:** 1 oktober 2026
**Product:** hybride e-learning A3 (repository `hanbedrijfskunde/a3-learning`), startpagina `index.html`
**Na akkoord:** vastleggen in LRD 0.24 (FR-75, AC-51, noot onder Purpose in Deel 5), ADR (B113), BLUEPRINT (ST-8, ST-9, Bijlage A en B) en DESIGN (§5.1, §5.2); daarna bouwen in a3-learning. De nummers zijn afgestemd met twee parallelle sessies: B112, LRD 0.21, FR-74, AC-50 en SX-20 zijn van het infovenster bij de metrokaart, B114 en LRD 0.23 van de verdieping in leerblok 4. LRD 0.22 was voor dit ontwerp gereserveerd, maar 0.23 was eerder klaar; deze ronde wordt 0.24, zodat 0.23 achteraf niet van inhoud verandert. 0.22 blijft ongebruikt.

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
- Eén accentknop „Start met je vraagstuk” (het label uit DESIGN §4). Een klik zet de focus in het veld `#start-alias`; de browser scrolt daar vanzelf naartoe.
- Daaronder een kleine regel met de link naar `docs/studentintroductie.html`. Die vervangt de huidige regel „Nieuw hier? Lees de introductie van één pagina.” in de sectie `#start`.

### 3.2 Terugkerend bezoek

- Het verhaal wordt een ingeklapte `<details class="verhaal-details">` met de samenvatting „Waar gaat dit over?” en dezelfde drie blokken. Er staat geen knop in: wie terugkomt, heeft het formulier al gezien.
- Plaats: onder de vier leerblokken, boven „Jouw gegevens”. Wat bovenaan staat (Verder waar je was, A3-vak 1, de leerblokken; DESIGN §5.2) blijft daardoor op zijn plek.
- De samenvatting krijgt de opmaak van de bestaande `details`-samenvattingen op de site, met een hoogte van minstens 2,75rem (al geregeld voor `summary`).

### 3.3 Concepttekst

Samen 140 woorden lopende tekst. De definitieve tekst gaat vóór het bouwen door `redigeer-nederlandse-tekst` en `schrap-ai-taal` en wordt aan de auteur voorgelegd.

> **Waarom dit?**
> Je opdrachtgever komt met een vraag die nog vaag is. Begin je meteen aan een oplossing, dan los je misschien het verkeerde probleem op. Hier maak je van die vage vraag een onderzoeksvraag waar je team mee verder kan. Die bespreek je met je opdrachtgever op je A3.
>
> **Hoe werk je?**
> Je werkt aan je eigen vraagstuk. Elke taak laat het eerst zien met een voorbeeld, webshop X. Daarna doe je hetzelfde voor jouw vraag. Bij elke taak staat wanneer je klaar bent, en de site kijkt meteen mee. Je hebt geen account nodig: alles blijft in deze browser.
>
> **Wat heb je aan het eind?**
> Vier leerblokken van ongeveer 45 minuten. Daarna staat het eerste vak van je A3: je onderzoeksvraag, betrouwbare bronnen en een beeld van wie er bij je vraagstuk betrokken zijn. En je hebt een dossier met al je werk, dat je inlevert voor je portfolio.

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
- **Bestaande controles**: ST-7 (geen Wissel, verdieping, „Mijn stand” of „kopieer naar A3” op de eerste schermen), de taalcontrole, de content-check en de gewichtscontrole blijven groen.

## 8. Buiten scope

- De studentintroductie (`docs/studentintroductie.html`, DL-2) blijft zoals ze is: het praktische A4 over gegevens, bewaren en inleveren. De overlap met het blok „Hoe werk je?” is klein en bewust: de introductie is voor wie het op papier wil hebben.
- Een andere h1 voor de startpagina („De A3 en je vraag: start”).
- Het profiel één veld per scherm (DESIGN §5.1, tweede punt). Dat is een losse wijziging.
- Een video of figuur bij het verhaal.
