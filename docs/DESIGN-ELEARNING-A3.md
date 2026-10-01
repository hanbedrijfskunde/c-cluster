# DESIGN — A3 e-learning (HAN Bedrijfskunde, C-cluster)

Ontwerprichtlijn voor de studentkant van `hanbedrijfskunde/a3-learning`. Gebaseerd op de UX-review van 30 september 2026. Doelgroep: hbo-studenten Bedrijfskunde, gewend aan Instagram, TikTok en games.

Dit document beschrijft **hoe de site moet voelen en werken**. De bestaande eisen blijven gelden: toegankelijkheid (TG-*), privacy (PR-*), gewicht (PF-4), geen score of ranglijst (BW-4, X-3) en modelantwoord pas na eigen poging (TK-6).

Het toetsbare deel van deze richtlijn staat als SX-1 t/m SX-16 in [BLUEPRINT-ELEARNING-A3.md](BLUEPRINT-ELEARNING-A3.md) §6.17; bij verschil gaat het blueprint voor. De besluiten staan in [ADR-ELEARNING-A3.md](ADR-ELEARNING-A3.md) B73 t/m B81, de bouwvolgorde in [BUILDPLAN-ELEARNING-A3.md](BUILDPLAN-ELEARNING-A3.md) fase 16 t/m 19.

---

## 1. Kernidee

> **Eén ding per scherm. Laat zien wat je hebt opgebouwd, niet wat nog ontbreekt.**

De inhoud en didactiek zijn sterk. Het probleem zit in structuur, tempo en feedback. De huisstijl (zwart, wit, magenta, harde randen) blijft zoals hij is: hij past bij deze doelgroep.

## 2. Ontwerpprincipes

1. **Focus boven overzicht.** Een taak krijgt het hele scherm. Het overzicht is één tik verwijderd, niet doorlopend eromheen.
2. **Groei zichtbaar maken.** Voortgang toon je als de A3 die zich vult, niet als een lijst statussen. Elke afgeronde stap levert iets zichtbaars op.
3. **Neutraal beginnen.** Wat nog niet gedaan is, is „Te doen” en grijs. Rood en magenta gebruik je alleen als iets echt aandacht nodig heeft, en pas na een actie.
4. **Studententaal, geen systeemtaal.** Geen EV-codes, geen „bewijsonderdeel”, geen „richttijd”. Noem het resultaat: „Je onderzoeksvraag”.
5. **Harde schaduw = aantikbaar.** De 3D-schaduw van 3–5 px staat alleen op knoppen en kaarten die je kunt aantikken. Informatie krijgt een rand of vlak, geen schaduw.
6. **Mobiel eerst.** Ontwerp vanaf 360 px. Het bureaublad krijgt een tweede kolom, geen extra inhoud.
7. **Eerlijk benoemen.** Is iets een formulier met keuzes, noem het dan geen „spel”. Wil het „spel” heten, dan moet het ook als spel werken (zie §7.4).
8. **Een model staat in beeld én in tekst.** Een model is alles met een ruimtelijke vorm: assen, vakken of lagen (invloed/belang-raster, VPC, BMC, TOM³, six capitals, het A3-vel). Waar de stof een model noemt, staat de figuur erbij, en de tekst ernaast legt hem uit. Een voorbeeld staat ín die figuur; een opdracht met een model laat de student in de figuur werken, niet in een tabel ernaast (SX-15, ADR B92 en B95). Een lijst of ezelsbruggetje (AAOCC, STARR, 3xC) is geen model.

## 3. Tokens

Alle kleuren staan in `:root` van `css/site.css`, en nergens anders (`tests/toegankelijk.test.mjs`). De bestaande tokens blijven; nieuw is gemarkeerd met ➕.

### Kleur

| Token | Waarde | Gebruik |
|---|---|---|
| `--accent` | `#E50056` | Primaire actie, actieve stap, huidige positie. Hooguit één accentvlak per scherm. |
| `--accent-donker` | `#B8004A` | Hover op accentknop; accenttekst op wit. |
| `--zwart` | `#000000` | Tekst, randen, voltooide segmenten. |
| `--wit` | `#FFFFFF` | Achtergrond. |
| `--grijs` | `#F2F2F0` | Vlakken, lege segmenten, oefenzone. |
| `--grijs-tekst` | `#454545` | Metatekst. |
| `--roze` | `#FFD9E6` | Invulplekken in een format (`<gebruiker>`), rij-markering. |
| `--fout` | `#B0003F` | Foutmelding, alleen na een actie. |
| `--groen` / `--oker` | `#1A7F37` / `#B7791F` | Alleen onderstreping bij status, nooit tekst (TG-4). |
| ➕ `--link` | `#000000` | Linkkleur (nu valt `a` terug op browserblauw). |
| ➕ `--link-hover` | `#B8004A` (= `--accent-donker`) | Hover op link. Als hex: `tools/contrast-check.mjs` leest alleen hexwaarden. |
| ➕ `--leeg` | `#F2F2F0` (= `--grijs`) | Achtergrond van „Te doen”-status en lege voortgangssegmenten. |

### Typografie

Stapel blijft `--f` (Avenir Next → systeemletters). Geen externe fonts (PF-4).

| Rol | Mobiel | Bureaublad | Gewicht |
|---|---|---|---|
| Schermtitel | 28 px / 1.1 | 40 px / 1.05 | 800 |
| Taaktitel | 23 px / 1.15 | 28 px | 800 |
| Tussenkop | 18 px | 20 px | 700 |
| Lopende tekst | 16 px / 1.55 | 17 px | 400 |
| Label / eyebrow | 12 px, kapitalen, spatiëring .06em | idem | 700 |
| Meta | 13–14 px, `--grijs-tekst` | idem | 400 |

Nooit kleiner dan 13 px voor inhoud. Kaartjes op het verbanden-bord gaan van 13 px naar **15 px**.

### Ruimte, rand en schaduw

- Spatiëring in stappen van 4: `4 · 8 · 12 · 16 · 24 · 32 · 48`. Tussen groepen gebruik je `gap`, geen marges.
- Rand: `--rand: 3px` voor componenten, 2 px binnen componenten.
- Schaduw: `3px 3px 0` op knoppen, `5px 5px 0` op tikbare kaarten, `8px 8px 0` hooguit één keer per scherm (hero). Nooit een kaart-in-kaart met twee schaduwen.
- Hoeken: recht (0). Uitzondering: chips (`border-radius: 1rem`).
- Aanraakdoel: minimaal 44 × 44 px (al in CSS).

## 4. Informatiearchitectuur

### Menu (student)

```
Start · Leerblokken · Dossier · Bronnen
```

- **Verificatie** en **Docent** gaan uit het hoofdmenu naar de footer („Voor docenten”).
- Mobiel: vaste **tabbalk onderin** met deze vier items; het actieve item heeft onderin een balk van 5 px in `--accent`.
- Bureaublad: horizontale navigatie bovenin, vast bij scrollen.
- De pilotbalk wordt een kleine chip naast het logo, geen volle magenta balk.

### Pagina's en routes

| Scherm | Doel | Hoofdactie |
|---|---|---|
| Start (eerste bezoek) | Uitleggen wat het oplevert, profiel aanmaken | „Start met je vraagstuk” |
| Start (terugkerend) | Verder waar je was | „Ga verder” |
| Leerblok-overzicht | Taken in dit blok, wat het oplevert | Eerste open taak |
| Taak | Eén taak in vier stappen | Afhankelijk van de stap |
| Afsluiten leerblok | Laten zien wat de A3 erbij kreeg | „Kopieer naar mijn A3” |
| Dossier | Stand, export, afdruk | „Bewaar je dossier” |
| Bronnen | Lijst | — |

URL-schema voor de taakweergave (werkt samen met de bestaande id's): `leerblok-1.html#taak-2.1` en `#taak-2.1/oefenen`. Terug naar het overzicht: `leerblok-1.html`.

## 5. Schermen

### 5.1 Start — eerste bezoek

- Bovenaan: één zin wat de student hier aan de A3 overhoudt, en één knop.
- Daarna het profiel **één veld per scherm**: alias → teamnummer → vraagstuk → waarom-zin. Voortgang in stappen (●●○○).
- Valideren pas **na het verlaten van een veld** of bij „Verder”. Nooit foutmeldingen op een leeg formulier.
- De privacytekst staat bij het eerste veld, in gewone taal, uitklapbaar.

### 5.2 Start — terugkerend

Van boven naar beneden:

1. Begroeting met alias, en de kop „Zo staat je A3-vak 1”. Geen percentage (BW-4).
2. **A3-vak 1 in vier delen** (B75): Onderzoeksvraag en zoekvragen · Bronnen · Plaatsing · Verbanden en reflectie, één per leerblok. Gevulde delen zijn `--accent`, lege alleen rand. Onderschrift: „2 van de 4 delen van vak 1 staan”. De e-learning vult alleen vak 1 (X-15); vak 2 t/m 8 tonen we niet.
3. **Verder-kaart** (zwart vlak, witte tekst): taaknummer, titel, „Leerblok 1 · stap 3 van 4 · nog ± 10 min”, accentknop „Ga verder”.
4. Vier leerblokregels, elk met een segmentbalk (één segment per taak). Meta: „2 van 3” of „te doen”.

Geen EV-codes, geen richttijdtabel.

### 5.3 Taak (kernscherm)

```
┌──────────────────────────────┐
│ ← Leerblok 1     Taak 2 van 3 │  vaste kop
│ ▬▬▬▬ ▬▬▬▬ ▬▬▬▬ ░░░░           │  segmentbalk: stappen van deze taak
│ Waarom · Stof · Oefenen · Toep.│  stappenrij, huidige onderstreept
├──────────────────────────────┤
│ [2.1]  Alleen · 10 min        │
│ Taaktitel                     │
│ …inhoud van de huidige stap…  │
│ Klaar als  ☑ ☑ ☐              │
├──────────────────────────────┤
│ [Hint]  [ Primaire actie    ] │  vaste voet
└──────────────────────────────┘
```

- **Vier stappen** per taak (TK-18, B76): Waarom → Stof → Oefenen → Toepassen. „Klaar” en de volgende stap sluiten Toepassen af; de verdieping verschijnt daarna en is geen segment. Elke stap past zo veel mogelijk in één scherm; langere stof wordt opgesplitst in kaarten die je doorveegt of doorklikt.
- **Segmentbalk**: voltooid = `--zwart`, actief = `--accent`, open = `--grijs`. 6 px hoog, 3 px tussenruimte.
- **Klaar-als als live checklist**: elk criterium uit `klaarAls` is een regel met een vakje. Vinkt af zodra de bijbehorende controle (soort A) slaagt. Criteria die niet automatisch te controleren zijn, vinkt de student zelf af.
- **Vaste voet**: één primaire knop (accent, volle breedte min secundaire knop). Tekst per stap: „Verder” → „Naar oefenen” → „Check en zie modelantwoord” → „Bewaar in dossier”.
- **Modelantwoord** verschijnt na „Check” als uitklappend paneel met de kop „Zo zou het kunnen”. Presenteer het als beloning, niet als correctie.
- **Format-blokken** (user story): invulplekken tonen met `--roze`-achtergrond.
- **Routekeuze** (Tekst · Video · Spel) staat in de stap „Stof” als drie grote tegels, niet als kleine knopjes.

### 5.4 Afsluiten leerblok

- Volledig `--accent`-scherm, witte tekst: het enige volvlak magenta in het blok.
- Kop: „Deel 1 van je A3-vak 1 staat.” (na leerblok 4: „Je A3-vak 1 staat.”)
- A3-vak 1 in vier delen (wit, harde schaduw) met het zojuist gevulde deel in zwart.
- Citaat van de eigen onderzoeksvraag in een zwart vlak.
- Afgevinkte resultaten in gewone taal.
- Knoppen: **„Kopieer naar mijn A3”** (wit, primair), „Door naar leerblok 2” (omlijnd).
- De bewaarmelding (dossier exporteren) staat hier als tweede regel, niet als losse waarschuwing.

### 5.5 Dossier

- „Mijn stand” als A3-vak 1 in vier delen plus resultatenlijst in gewone taal. EV-codes alleen in de export en de docentweergave.
- Tegels: „Te doen” neutraal (`--leeg`), „Bijna” oker, „Compleet” groen: alleen als onderstreping van 8 px, de statustekst blijft zwart (TG-4).
- Export is de primaire actie; import en afdrukken zijn secundair.

## 6. Componenten

### Knop

| Variant | Stijl |
|---|---|
| Primair | `--accent`, witte tekst, 3 px zwarte rand, `3px 3px 0` schaduw |
| Secundair | wit, zwarte tekst, 3 px rand, `3px 3px 0` schaduw |
| Omlijnd op accent | transparant, witte tekst, 3 px witte rand |
| Actief (`:active`) | schaduw weg, `translate(3px,3px)`, voelt als indrukken |

Maximaal één primaire knop per scherm.

### Kaart

- **Tikbaar**: 3 px rand + `5px 5px 0` schaduw, hover `--grijs`, active indrukken.
- **Informatief**: 3 px rand, géén schaduw; of `--grijs` vlak zonder rand.
- Nooit meer dan één kaartniveau diep.

### Status

| Status | Tekst | Stijl |
|---|---|---|
| Te doen | „Te doen” | `--leeg` vlak, geen onderstreping |
| Bijna | „Bijna” | onderstreping `--oker` |
| Compleet | „Compleet” + ✓ | onderstreping `--groen` |

„Nog niet” vervalt.

### Segmentbalk

Flex/grid met `gap: 3px`, segmenten 6 px hoog. Altijd met een tekstalternatief (`aria-label="Taak 2 van 3, stap 3 van 4"`).

### A3-vak 1

Grid 2 × 2 (bureaublad: 4 × 1), `gap: 4px`, delen met 2 px rand. Labels (Onderzoeksvraag en zoekvragen, Bronnen, Plaatsing, Verbanden en reflectie) in 12 px vet. Gevuld = `--accent` (op start) of `--zwart` (op het afsluitscherm). Tekstalternatief: „2 van 4 delen van A3-vak 1 gevuld”.

### Invoerveld

- Label altijd zichtbaar (bestaand).
- **Placeholder als zinstarter** voor lange velden (bijv. STARR: „Tijdens de gallery walk merkte ik…”). De placeholder is nooit het antwoord.
- Zachte teller bij lange velden („± 2–4 zinnen”), geen harde limiet.
- Foutmelding pas na `blur` of indienen, onder het veld, in `--fout`.

### Bestandkiezer

Voor het terugzetten van een dossier (dossier, terugblik) en het inlezen op de verificatiepagina. Nooit de kale browserknop: die zegt „Choose file” en „No file chosen” in de taal van de browser, en na het inlezen weer „No file chosen”.

```
┌─────────────────────────────────────────┐
│ ┌───┐  Kies je dossierbestand            │
│ │ ↑ │  Klik of sleep het hierheen · .json │
│ └───┘  Gekozen: dossier-lisa.json        │
└─────────────────────────────────────────┘▌
 ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
```

- Een **brede secundaire knop** over de volle breedte: wit, 3 px rand, `3px 3px 0` schaduw. Geen kaartschaduw van 5 px: de kiezer staat meestal in een kaart (één kaartniveau diep). De primaire knop van het scherm blijft „Bewaar je dossier”.
- Links een zwart vierkant van 48 px met een witte pijl omhoog; rechts de titel (18 px, 800), met daaronder de hulpregel (14 px, `--grijs-tekst`).
- Hulpregel: op een telefoon „Tik om te kiezen · .json”, met muis „Klik of sleep het hierheen · .json” (`@media (hover:hover) and (pointer:fine)`).
- Na de keuze een derde regel in het vet: „Gekozen: ‹bestandsnaam›”, of „Gekozen: 3 bestanden”. Is het geen .json, dan staat daar in `--fout`: „Dat is geen .json-bestand. Kies een dossierbestand.” De uitkomst van het inlezen staat onder de knop, zoals nu.
- Toestanden: hover `--grijs` en het vierkant wordt `--accent`; slepen: `--roze` vlak, rand gestreept, vierkant `--accent`; indrukken als elke knop; focus: de focusrand van 4 px om de hele knop.
- Onder de motorkap blijft het echte `<input type="file">` staan, onzichtbaar (`sr-only`) maar focusbaar, in het `<label>`. Toetsenbord, schermlezer en de bestandskiezer van de telefoon werken zo zonder extra ARIA.

### Stakeholderbord

Het invloed/belang-raster als figuur én als invoer (SX-16, ADR B96). Eén component op vier plekken bij taak 5.1: leeg als model in de stof, met het voorbeeld (controller en accountant) in de tekstroute, als modelantwoord (webshop X), en als werkblad bij oefenen en toepassen.

```
 Nog te plaatsen:  [Klanten · ext]  [+ Stakeholder toevoegen      ]
          INVLOED ↑ hoog
 ┌────────────────────────┬────────────────────────┐
 │ TEVREDEN HOUDEN        │ NAUW BETREKKEN   (roze)│
 │ [Accountant · ext]     │ [■ Controller · int]   │
 │                   ┌────┴─────┐                  │
 ├───────────────────┤vraagstuk ├──────────────────┤
 │                   └────┬─────┘                  │
 │ VOLGEN                 │ OP DE HOOGTE HOUDEN    │
 └────────────────────────┴────────────────────────┘
   laag                  BELANG →               hoog
```

- **Assen**: invloed verticaal (hoog boven), belang horizontaal (hoog rechts), met pijl en label. Vakken met 3 px rand; „Nauw betrekken” in `--roze`. Vaklabel als eyebrow (12 px, kapitalen).
- **Midden**: het vraagstuk als zwart label met witte tekst op het kruispunt van de assen, zoals op vel 1 van het werkboek. Leeg vraagstuk: „Je vraagstuk”, gestippeld.
- **Kaart**: naam plus „int” of „ext”. Intern is een zwart vlak met witte tekst, extern wit met zwarte rand. Status nooit alleen in vorm of kleur: de afkorting staat er altijd bij (TG-4). Tikbaar, dus `3px 3px 0` schaduw.
- **Bak** („Nog te plaatsen”) boven het raster, met het invoerveld „Stakeholder toevoegen” (Enter maakt een kaart). Bij toepassen staat de gebruiker uit leerblok 1 er als voorstel in, met de tekst „uit je onderzoeksvraag”. De student plaatst hem zelf, of haalt hem weg.
- **Plaatsen**: slepen naar een vak (muis en aanraking), of tik op de kaart en tik op een vak. Een opgepakte kaart krijgt een `--accent`-rand en de vakken tonen „Zet hier”. Toetsenbord: Enter pakt op, pijltjes verplaatsen (↑ meer invloed, → meer belang), Enter of Escape zet neer.
- **Details**: tik op een geplaatste kaart; onder het raster opent een paneel met naam, intern/extern (twee knoppen), „Hoe raakt het vraagstuk deze stakeholder?”, „Terug naar de bak” en „Verwijderen”. Geen popover: het paneel blijft in de leesvolgorde.
- **Maximaal 7** stakeholders (de rijen van het dossier). Bij 7 verdwijnt het invoerveld met de melding „Het bord is vol (7).”
- **Mobiel**: het raster blijft 2 × 2, ook op 360 px; kaarten tonen dan alleen naam en afkorting, 13 px.
- **Tekstweergave**: onder het raster een `<details>` „Het bord in tekst”, één zin per stakeholder (bestaand, `rasterTekst`), en een `role="status"`-regel die na elke zet zegt wat er gebeurde: „Klantenservice staat nu bij Op de hoogte houden.”
- **Vast bord** (stof, voorbeeld, modelantwoord): zelfde tekening, geen bak, geen invoer, kaarten niet tikbaar (geen schaduw).
- De gegevens blijven de velden `s1naam` … `s7belang`: dossier, controles, export en verificatie merken niets van het bord.

### Fieldset / keuzes

- Vraag als `legend` die niet over de opties heen valt: `legend { float:left; width:100%; } legend + * { clear:both; }`.
- Radio/checkbox als **tikbare rij** over de volle breedte (min. 44 px), niet als los rondje met label.

### Link

`a { color: var(--link); font-weight: 700; text-decoration-thickness: 3px; text-underline-offset: 3px; }` · `a:hover { color: var(--link-hover); }`

## 7. Interactiepatronen

### 7.1 Voortgang en beloning

- Na elke stap: segment vult (transitie 200 ms, `ease-out`).
- Na elke taak: kort bevestigingsmoment („Opgeslagen in je dossier” + ✓), 1,5 s, geen modaal venster.
- Na elk leerblok: het afsluitscherm (§5.4).
- **Geen** punten, badges, streaks, percentages of ranglijsten (BW-4, X-3). Het enige wat groeit is de eigen A3.

### 7.2 Feedback op invoer

- Controles van soort A draaien live (na 600 ms zonder typen) en vinken de klaar-als af.
- Een vraag gaat altijd over stof die ervoor is behandeld (TK-19); de hint zegt waar die stof staat.
- De stap stof legt uit en stelt geen vragen of opdrachten die oefenen of toepassen daarna stellen (ADR B88).
- Een hint staat achter een knop „Hint” (`<details>`), en toont steeds één aanwijzing. Geen mouse-over: op een telefoon bestaat hover niet (SX-13, ADR B83).
- Nooit meer dan één foutmelding tegelijk in beeld per veld.

### 7.3 Verbanden-bord (leerblok 4)

- Houden: tikken, verbinden, lijnen zien.
- Kaarttekst naar 15 px; lange kaarten klappen open bij tik.
- De lijst van tien „open plekken” wordt **één prompt tegelijk** boven het bord: „Verbind je pain met een kapitaal.” Na het leggen van een verband verschijnt de volgende.
- De tekstweergave van alle verbanden blijft (toegankelijkheid), in een `<details>`.

### 7.4 Spellen

Kies per spel één van twee:

- **Echt interactief**: keuzes als grote tikbare kaarten; direct zichtbaar effect (bijv. zes kapitalen als balken die op en neer gaan); korte feedback per keuze; tekstversie in `<details>` (bestaand).
- **Eerlijk benoemen**: noem het „Simulatie” of „Oefencasus” en ontwerp het als taakstap.

### 7.5 Video

- Voorkeur: docent op camera, **verticaal 9:16, 60–90 s**, ondertiteld. Het script ligt er al (`spreektekst`).
- Tot die er is: het label „Conceptvideo” laten staan (bestaand).
- Nooit autoplay, `preload="none"` (MD-5 t/m MD-7).

### 7.6 Beweging

- Duur 150–250 ms, `ease-out`. Alleen voor segmenten die vullen, knoppen die indrukken en panelen die openklappen.
- Respecteer `prefers-reduced-motion: reduce` (dan geen transities).

## 8. Taal

| Niet | Wel |
|---|---|
| EV-01: Nog niet | Je onderzoeksvraag · Te doen |
| Bewijsonderdeel | Resultaat / wat je bewaart |
| Richttijd: 10 min | ± 10 min |
| Eindigt met: … (EV-01, EV-02) | Na dit blok heb je: je onderzoeksvraag en je zoekvragen |
| Vul een alias in | Hoe wil je heten in je dossier? |
| Leerblok afsluiten | Klaar met dit blok |

Je-vorm, actief, kort. Knoppen beginnen met een werkwoord.

## 9. Toegankelijkheid (blijft gelden)

- Contrast tekst ≥ 4,5:1 (`tools/contrast-check.mjs`). Nieuwe tokens toevoegen aan `:root` zodat de test ze ziet.
- Status nooit alleen met kleur: altijd tekst erbij.
- Focusrand `4px solid var(--accent)` (bestaand).
- Sprongkoppeling, landmarks, zichtbare labels (bestaand).
- Vaste kop en voet mogen de focus niet verbergen: `scroll-padding-top` en `scroll-padding-bottom` op `html` gelijk aan hun hoogte.
- Stapnavigatie ook met toetsenbord; bij stapwissel de focus op de stapkop zetten.

## 10. Techniek en gewicht

- Gemeten met `tools/gewicht-check.mjs` (30-9-2026): gzip ruim binnen 300 kB (leerblok 3: 112,8 kB), maar de brongrens van 400 kB knelt: leerblok 4 zit op 384,0 kB. Sinds ADR B99 is de brongrens 500 kB; de gzip-grens van 300 kB blijft. Nieuwe UI-code daarom eerst in een eigen, dynamisch geladen module, en voor de taakweergave **per taak laden**: taakdata en stapcomponenten dynamisch importeren, net als nu `checks/lbN.js`.
- Geen frameworks of externe fonts toevoegen.
- De taakweergave is een extra laag boven de bestaande DOM-id's (`taak-<nr>`, `oefening-<nr>`, …); `sessie.js`, `store.js` en de controles blijven ongewijzigd.

## 11. Aanpak

De uitvoering staat in het BUILDPLAN: snel = fase 16, middel = fase 17, daarna een proefsessie (fase 18), structureel = fase 19; alles vóór de pilot (B78). De lijst hieronder is de oorspronkelijke indeling uit de review.

**Snel (± 1 dag)**
- [ ] Validatie pas na invoer op de startpagina
- [ ] Studentmenu naar 4 items; docent en verificatie naar de footer
- [ ] „Nog niet” → „Te doen” (neutraal)
- [ ] `--link` / `--link-hover` in `:root`, `a`-stijl toevoegen
- [ ] Legend-overlap fixen (taak 2.2)
- [ ] Zinstarters als placeholder bij STARR en lange velden

**Middel (1 sprint)**
- [ ] Vaste segmentbalk en stappenrij per taak
- [ ] Klaar-als als live checklist
- [ ] Afsluitscherm met A3-vak 1 in vier delen en „Kopieer naar mijn A3”
- [ ] EV-codes vervangen door gewone taal in de studentweergave
- [ ] Mobiele tabbalk

**Structureel**
- [ ] Per-taak laden (gewicht)
- [ ] Eén taak per scherm met vaste voet
- [ ] Spellen herontwerpen of hernoemen
- [ ] Verticale docentvideo's

## 12. Buiten scope

Docentmodus (`docent.html`), verificatie (`verificatie.html`) en controlelab: eigen doelgroep en context (projectie op 1280 × 720, stapkaarten ≥ 28 px). Die volgen hun eigen richtlijnen.
