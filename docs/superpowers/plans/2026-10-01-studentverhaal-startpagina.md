# Verhaal voor studenten op de startpagina — uitvoeringsplan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bovenaan de startpagina van de e-learning A3 staat een verhaal voor studenten in drie blokken (waarom, hoe, wat): open bij een eerste bezoek boven het formulier, ingeklapt daarna onder de vier leerblokken.

**Architecture:** De tekst staat in `data/leerblokken.json` onder `start.verhaal` en wordt bewaakt door `controleerOverzicht` in `tools/content-check.mjs`. Een pure functie `verhaalOpen(profiel, records)` in `js/weergave.js` beslist bij het laden of het verhaal open staat; `js/index-pagina.js` tekent een `<section id="verhaal">` of een `<details class="verhaal-details">`. Documentatie (ADR B113, LRD 0.24, BLUEPRINT ST-8 en ST-9, DESIGN §5.1 en §5.2, BUILDPLAN) in c-cluster-1.

**Tech Stack:** statische site, vanilla ES-modules, JSON-content, `node --test`, `tools/content-check.mjs`, `tools/gewicht-check.mjs`, `tools/link-check.mjs`. Geen DOM in de tests (pure functies en broncode); de pagina wordt in de browser gecontroleerd met de Playwright-tools (`mcp__plugin_playwright_playwright__*`) op een lokale server.

**Spec:** `docs/superpowers/specs/2026-10-01-studentverhaal-startpagina-design.md` (repository c-cluster-1). Besluit: ADR B113. Regels: BLUEPRINT ST-8, ST-9; LRD FR-75, AC-51; DESIGN §5.1, §5.2.

**Werkmappen:** code in `/Users/witoldtenhove/Documents/HAN/a3-learning/.worktrees/studentverhaal` (branch `studentverhaal`); documentatie in `/Users/witoldtenhove/Documents/HAN/c-cluster-1/.worktrees/studentverhaal` (branch `studentverhaal`). Paden in taak 2 en 6 (documenten) zijn relatief aan de c-cluster-1-worktree, in taak 3 tot en met 5 aan de a3-learning-worktree. Twee andere sessies werken in dezelfde repo's (metrokaart-info, verdieping leerblok 4): werk nooit in de gedeelde werkmappen, gebruik nooit `git add -A` of `git commit -a`, en push niet zonder opdracht van de auteur.

## Global Constraints

- Nummers: ADR **B113**, LRD **0.24** (0.22 blijft ongebruikt; 0.23 is van B114), **FR-75**, **AC-51**, BLUEPRINT **ST-8** (Must) en **ST-9** (Should). Niet gebruiken: B112, B114, B115, FR-74, AC-50, SX-20, MD-18, LRD-bronnen S20 en S21. Staat er bij taak 2 op origin/main al een LRD-versie ≥ 0.24 (B115 claimde 0.25), neem dan het eerstvolgende vrije nummer, pas de teksten in taak 2 daarop aan en meld het de andere sessies; zet een ronde nooit tussen twee bestaande versies.
- Drie blokken met id's `waarom`, `hoe`, `wat`, in die volgorde; elk een kop (een vraag) en één alinea.
- Hoogstens **150 woorden** lopende tekst in de drie blokken samen (koppen, knop en introductieregel tellen niet mee).
- Verboden in de tekst van het verhaal (ST-7, DESIGN §8, B113): Wissel, verdieping, Mijn stand, kopieer naar A3, LUK, BC, `EV-`, bewijsonderdeel, richttijd, Golden Circle, Sinek.
- Knoplabel „Start met je vraagstuk” (DESIGN §4); de knop zet de focus in `#start-alias`.
- Eerste bezoek = bij het laden zijn alias, teamnummer, vraagstuk en waarom-zin leeg (na trimmen), „nog geen scherp vraagstuk” is uit, en er is geen enkel werkrecord. De stand wordt alleen bij het laden bepaald.
- Ingeklapt: `<details class="verhaal-details">` met samenvatting „Waar gaat dit over?”, na `#blokken` en vóór `#gegevens`, zonder knop.
- Informatiekaarten: `.kaart` (rand, geen schaduw, SX-7). Raster `repeat(auto-fit, minmax(14rem, 1fr))`; geen nieuw breekpunt. Geen kleurcode buiten `:root` (`tests/toegankelijk.test.mjs`).
- 0 px horizontale scroll op 360 px. PF-4: ≤ 300 kB gzip en ≤ 500 kB bron per pagina.
- `js/weergave.js` importeert `js/profiel.js` niet (anders laden bronnen en terugblik via `metro-model.js` er `checks/core.js` bij).
- `css/site.css`: het nieuwe blok staat direct na de regels van `.verder-kaart`, niet in het metroblok onderaan.
- Tekst in de UI en in commentaar is Nederlands, in de toon van de bestaande code.
- Commits eindigen met `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## Review Focus

1. Een student typt bij een eerste bezoek in het formulier (elke toets bewaart het profiel): het verhaal blijft open staan en de pagina verspringt niet. Broncode-test in taak 5, stap 1, en doorloop in taak 5, stap 6.
2. Na de klik op „Start met je vraagstuk” op een telefoon van 360 px: het aliasveld staat in beeld, niet onder de vaste kop of de tabbalk onderin. Doorloop in taak 5, stap 6.
3. Een docent past de tekst aan op GitHub en maakt hem te lang, haalt een blok weg of noemt „de Wissel”: content-check faalt, zodat de site niet wordt bijgewerkt. Test in taak 3.
4. `start.verhaal` ontbreekt in de data (oude kopie, verkeerde bewerking): de startpagina werkt verder zonder verhaal, zonder foutmelding. Broncode-test in taak 5, stap 1.
5. Een terugkerende student die alleen „nog geen scherp vraagstuk” aanvinkte, of alleen een teamnummer invulde: het verhaal staat ingeklapt. Test in taak 4.

---

### Task 0: Werkruimte

**Files:** geen wijzigingen; alleen worktrees.

- [ ] **Step 1: Maak de worktrees**

```bash
cd /Users/witoldtenhove/Documents/HAN/a3-learning && git fetch -q && git worktree add .worktrees/studentverhaal -b studentverhaal origin/main
cd /Users/witoldtenhove/Documents/HAN/c-cluster-1 && git fetch -q && git worktree add .worktrees/studentverhaal -b studentverhaal main && git -C .worktrees/studentverhaal rebase origin/main
```

De c-cluster-1-branch start van de lokale `main`, omdat spec en plan daar staan; de rebase zet ze bovenop origin/main.

- [ ] **Step 2: Controleer de basis**

```bash
cd /Users/witoldtenhove/Documents/HAN/a3-learning/.worktrees/studentverhaal && node --test 2>&1 | tail -4 && node tools/content-check.mjs | tail -3
```

Verwacht: `fail 0` en 0 fouten. (`tests/werkboek.test.mjs` slaat over, omdat het werkboek niet naast de worktree staat; dat is normaal.)

---

### Task 1: Definitieve tekst, goedgekeurd door de auteur

**Files:**
- Modify (c-cluster-1-worktree): `docs/superpowers/specs/2026-10-01-studentverhaal-startpagina-design.md` (§3.3)

**Interfaces:**
- Produces: de goedgekeurde tekst als JSON-object `verhaal` (vorm in taak 3, stap 3). Taak 2 (status van B113) en taak 3 (data) gebruiken hem.

- [ ] **Step 1: Redigeer de concepttekst**

Bron: spec §3.3 plus de kop „Waar gaat dit over?”, de knop „Start met je vraagstuk” en de regel „Hoe je je werk bewaart en inlevert, lees je in de introductie van één pagina.” Pas eerst de skill `redigeer-nederlandse-tekst` toe, daarna `schrap-ai-taal`. Doelgroep: eerstejaars hbo-studenten Bedrijfskunde, op hun telefoon.

- [ ] **Step 2: Controleer de grenzen**

Tel de woorden van de drie alinea's samen:

```bash
node -e "const t=process.argv.slice(1).join(' ');console.log(t.trim().split(/\s+/).length)" "<alinea waarom>" "<alinea hoe>" "<alinea wat>"
```

Verwacht: ≤ 150. Zoek in alle teksten op de verboden termen uit Global Constraints: 0 treffers.

- [ ] **Step 3: Leg de tekst voor aan de auteur en wacht**

Toon de auteur de kop, de drie blokken (kop en alinea), de knop en de introductieregel, met het woordaantal. Ga pas verder na een expliciet akkoord. Verwerk wijzigingen en herhaal stap 2.

- [ ] **Step 4: Zet de goedgekeurde tekst in de spec en commit**

Vervang in §3.3 van de spec de concepttekst door de goedgekeurde tekst, en de zin „Samen 140 woorden lopende tekst. De definitieve tekst gaat vóór het bouwen door … voorgelegd.” door „Samen N woorden lopende tekst. Goedgekeurd door de auteur op 1 oktober 2026.” (N = het aantal uit stap 2).

```bash
cd /Users/witoldtenhove/Documents/HAN/c-cluster-1/.worktrees/studentverhaal
git add docs/superpowers/specs/2026-10-01-studentverhaal-startpagina-design.md
git commit -m "Spec studentverhaal: tekst goedgekeurd door de auteur

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 2: Ontwerpdocumenten (ADR, LRD, BLUEPRINT, DESIGN)

**Files (c-cluster-1-worktree):**
- Modify: `docs/ADR-ELEARNING-A3.md` (kop, nieuwe rij onderaan)
- Modify: `docs/LRD-ELEARNING-A3.html` (versie, Purpose in Deel 5, FR-tabel, AC-tabel)
- Modify: `docs/BLUEPRINT-ELEARNING-A3.md` (§6.2, Bijlage A, Bijlage B)
- Modify: `docs/DESIGN-ELEARNING-A3.md` (§5.1, §5.2)

**Interfaces:**
- Consumes: de goedgekeurde tekst uit taak 1 (alleen voor de status van B113).
- Produces: FR-75, AC-51, ST-8, ST-9, B113, waar de code en de tests naar verwijzen.

- [ ] **Step 1: ADR — kop en B113**

Eerst: `git fetch -q && git rebase origin/main` in de worktree, en `grep -o '<dd>0\.[0-9]*' docs/LRD-ELEARNING-A3.html` (verwacht `0.23`; zie Global Constraints als het hoger is). Vervang in de kop van het ADR `versie 0.23` door `versie 0.24`. Voeg onderaan de tabel, direct na de rij `| B114 | …`, deze rij toe:

```markdown
| B113 | 1-10-2026 | 40 | De startpagina krijgt bovenaan een verhaal voor studenten in drie blokken met een vraag als kop, in de volgorde waarom, hoe, wat (FR-75, ST-8, ST-9). Het waarom opent met het probleem van de opdrachtgever: een vage vraag, het risico het verkeerde probleem op te lossen, en de onderzoeksvraag die je op je A3 met de opdrachtgever bespreekt. Het portfolio staat als één zin in het blok „wat”. Samen hoogstens 150 woorden, zonder Wissel, verdieping, „Mijn stand”, „kopieer naar A3”, LUK-, BC- of EV-codes, en zonder de Golden Circle te noemen. Bij een eerste bezoek (bij het laden een leeg profiel en geen werk) staat het verhaal open boven het formulier, met de knop „Start met je vraagstuk” die de focus in het aliasveld zet; daarna staat het ingeklapt onder de vier leerblokken. De stand wordt alleen bij het laden bepaald. De tekst staat in `data/leerblokken.json` onder `start.verhaal`; de contentcontrole bewaakt vorm, woordgrens en termen. De link naar de studentintroductie staat onder de knop en vervangt de regel „Nieuw hier?” | Verzoek van de auteur: de site had geen inleiding voor studenten, terwijl de docentgids dat verhaal wel heeft (B101); DESIGN §5.1 vroeg al om een zin en een knop bovenaan, die nooit gebouwd zijn. Het LRD noemt „bewijs voor het portfolio” zelf een externe reden (Deel 5, Purpose). Afgewezen: (a) een aparte pagina `welkom.html` als ingang (negende pagina en een klik extra, zie B80); (b) de studentintroductie herschrijven en de link prominenter maken (blijft een document waar je heen moet klikken); (c) de Golden Circle als figuur (een extra model zonder verband met de A3; DESIGN-principe 8 eist dan een figuur); (d) één alinea zonder koppen (de opbouw verdwijnt, wie scant slaat hem over); (e) het portfolio als waarom; (f) vaste HTML in `index.html` (tekst buiten de data en buiten de contentcontrole). LRD 0.22 was voor dit besluit gereserveerd; omdat 0.23 (B114) eerder klaar was, is dit 0.24 | Verzoek van de auteur; uitwerking Claude | Aangenomen; tekst goedgekeurd door de auteur (1-10-2026) |
```

- [ ] **Step 2: LRD — versie**

In `<dd>0.23 · 1 oktober 2026 (` wordt `0.23` → `0.24`. Vervang aan het eind van dezelfde regel

```
0.23: verdieping van leerblok 4 met de zes kapitalen van Mitsubishi Corporation, B114)</dd>
```

door

```
0.23: verdieping van leerblok 4 met de zes kapitalen van Mitsubishi Corporation, B114; 0.24: verhaal voor studenten op de startpagina, B113)</dd>
```

- [ ] **Step 3: LRD — Purpose in Deel 5**

Vervang

```html
      <p><em>Zwak:</em> „Het is bewijs voor het portfolio" blijft een externe reden. Het waarom blijft één zin per student; het team bespreekt die pas met de opdrachtgever, buiten de e-learning.</p></div>
```

door

```html
      <p><em>Zwak:</em> „Het is bewijs voor het portfolio" blijft een externe reden. Daarom opent de startpagina met de reden van de opdrachtgever, een vage vraag die eerst een onderzoeksvraag moet worden; het portfolio staat daar pas in het laatste blok (FR-75). Het waarom blijft één zin per student; het team bespreekt die pas met de opdrachtgever, buiten de e-learning.</p></div>
```

- [ ] **Step 4: LRD — FR-75**

Voeg direct na de rij die begint met `    <tr><td class="n">FR-74</td>` (de laatste rij vóór `  </table></div>` van 7.1) in:

```html
    <tr class="sub"><td colspan="3">Inleiding voor studenten (B113)</td></tr>
    <tr><td class="n">FR-75</td><td>toont op de startpagina een verhaal in drie blokken met een vraag als kop, in de volgorde waarom (het probleem van de opdrachtgever), hoe (werken aan het eigen vraagstuk, eerst een voorbeeld, „klaar als”, alles in de browser) en wat (vier leerblokken, A3-vak 1 en een dossier voor het portfolio), samen hoogstens 150 woorden; bij een eerste bezoek open boven de startinvoer met één knop naar het eerste veld, daarna ingeklapt onder de leerblokken</td><td class="m">B113, FR-02, FR-66</td></tr>
```

- [ ] **Step 5: LRD — AC-51**

Voeg direct na de rij die begint met `    <tr><td class="n">AC-50</td>` in:

```html
    <tr class="sub"><td colspan="3">Inleiding voor studenten (B113)</td></tr>
    <tr><td class="n">AC-51</td><td>Wie de site voor het eerst opent, ziet boven het formulier drie blokken in de volgorde waarom, hoe, wat, samen hoogstens 150 woorden en zonder Wissel, verdieping, „Mijn stand”, „kopieer naar A3” of codes; „Start met je vraagstuk” zet de cursor in het aliasveld. Wie terugkomt met een profiel of werk, ziet het verhaal ingeklapt onder de vier leerblokken.</td><td>test en doorloop op 360 px (FR-75)</td></tr>
```

- [ ] **Step 6: BLUEPRINT — ST-8 en ST-9**

Voeg in §6.2 direct na de regel die begint met `| <a id="st-7"></a>ST-7 |` in:

```markdown
| <a id="st-8"></a>ST-8 | Bij een eerste bezoek (bij het laden een leeg profiel en geen werk) moet de startpagina boven de startinvoer een verhaal tonen in drie blokken met een vraag als kop, in de volgorde waarom, hoe, wat, met één knop die de focus in het eerste veld van de startinvoer zet. | Must | 3 blokken in die volgorde; ≤ 150 woorden lopende tekst; 0 keer Wissel, verdieping, „Mijn stand", „kopieer naar A3", LUK, BC, `EV-`, bewijsonderdeel, richttijd, Golden Circle of Sinek; 1 knop; na de klik focus op het aliasveld | Test + inspectie (doorloop op 360 px) |
| <a id="st-9"></a>ST-9 | Bij een terugkerend bezoek (bij het laden een profiel of werk) moet het verhaal ingeklapt onder het overzicht van de leerblokken staan. | Should | 0 open blokken bij het laden; 1 samenvatting „Waar gaat dit over?" na het leerblokoverzicht; de stand verandert niet tijdens het typen | Test + inspectie |
```

- [ ] **Step 7: BLUEPRINT — Bijlage A en B**

In Bijlage A, na `| FR-74 | SX-20 |`: `| FR-75 | ST-8, ST-9 |`. In Bijlage B, na `| AC-50 | SX-20 |`: `| AC-51 | ST-8, ST-9 |`.

- [ ] **Step 8: DESIGN — §5.1 en §5.2**

In §5.1 vervang `- Bovenaan: één zin wat de student hier aan de A3 overhoudt, en één knop.` door:

```markdown
- Bovenaan: het verhaal in drie blokken met een vraag als kop, in de volgorde waarom, hoe, wat (ADR B113, ST-8), en één knop „Start met je vraagstuk” die de focus in het eerste veld zet. Het waarom begint bij de vage vraag van de opdrachtgever, niet bij het portfolio. Informatiekaarten met rand en zonder schaduw; op de telefoon onder elkaar, op een breed scherm naast elkaar. Daaronder de link naar de introductie van één pagina.
```

In §5.2 voeg na punt 4 (`4. Vier leerblokregels, …`) toe:

```markdown
5. Het verhaal, ingeklapt: één samenvatting „Waar gaat dit over?” onder de leerblokregels (ST-9). Wie hem openklapt, ziet de drie blokken en de link naar de introductie, zonder knop.
```

- [ ] **Step 9: Controleer en commit**

```bash
cd /Users/witoldtenhove/Documents/HAN/c-cluster-1/.worktrees/studentverhaal
grep -c "B113" docs/ADR-ELEARNING-A3.md docs/LRD-ELEARNING-A3.html docs/DESIGN-ELEARNING-A3.md
grep -n "FR-75\|AC-51" docs/LRD-ELEARNING-A3.html docs/BLUEPRINT-ELEARNING-A3.md
grep -n 'id="st-8"\|id="st-9"' docs/BLUEPRINT-ELEARNING-A3.md
```

Verwacht: B113 in alle drie; FR-75 drie keer in het LRD (rij in 7.1, de Purpose-noot, de verificatie van AC-51) en één keer in het BLUEPRINT (Bijlage A); AC-51 één keer in het LRD en één keer in het BLUEPRINT (Bijlage B); ST-8 en ST-9 elk één anker. Open het LRD in de browser en kijk of de twee tabellen heel zijn.

```bash
git add docs/ADR-ELEARNING-A3.md docs/LRD-ELEARNING-A3.html docs/BLUEPRINT-ELEARNING-A3.md docs/DESIGN-ELEARNING-A3.md
git commit -m "ADR B113; LRD 0.24; FR-75, AC-51, ST-8, ST-9: verhaal voor studenten op de startpagina (LRD, ADR, BLUEPRINT, DESIGN)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 3: Het verhaal in de data, met contentcontrole

**Files (a3-learning-worktree):**
- Modify: `tools/content-check.mjs` (`controleerOverzicht`, direct na de regel met `de privacytekst moet 1 tot en met 100 woorden hebben`; constanten direct boven `export function controleerOverzicht`)
- Modify: `data/leerblokken.json` (nieuw object `start.verhaal`)
- Modify: `tests/fixtures/content-goed/leerblokken.json`, `tests/fixtures/content-concept/leerblokken.json`, `tests/fixtures/content-vier-fouten/leerblokken.json`
- Test: `tests/content-check.test.mjs` (nieuwe test direct na de test `LB-1/ST-1/ST-2: het overzicht heeft 4 leerblokken …`)

**Interfaces:**
- Consumes: de goedgekeurde tekst uit taak 1.
- Produces: `overzicht.start.verhaal` met de vorm `{ kop: string, blokken: [{ id: 'waarom'|'hoe'|'wat', kop: string, tekst: string }] (precies 3, in die volgorde), knop: string, introductie: { tekst: string, link: string } }`. Exports `VERHAAL_BLOKKEN`, `VERHAAL_MAX_WOORDEN`, `VERHAAL_VERBODEN` uit `tools/content-check.mjs`.

- [ ] **Step 1: Schrijf de falende test**

In `tests/content-check.test.mjs`, direct na de test `LB-1/ST-1/ST-2: …`:

```js
test('ST-8: het verhaal van de startpagina heeft drie blokken waarom, hoe, wat, ≤ 150 woorden en geen verboden termen', () => {
  assert.deepEqual(controleerOverzicht(overzicht()), []);
  const geen = overzicht(); delete geen.start.verhaal;
  assert.match(controleerOverzicht(geen).join('\n'), /mist start\.verhaal/);
  const volgorde = overzicht(); volgorde.start.verhaal.blokken.reverse();
  assert.match(controleerOverzicht(volgorde).join('\n'), /precies de blokken waarom, hoe en wat/);
  const twee = overzicht(); twee.start.verhaal.blokken.pop();
  assert.match(controleerOverzicht(twee).join('\n'), /precies de blokken waarom, hoe en wat/);
  const leeg = overzicht(); leeg.start.verhaal.blokken[1].tekst = ' ';
  assert.match(controleerOverzicht(leeg).join('\n'), /verhaalblok hoe mist kop of tekst/);
  const lang = overzicht(); lang.start.verhaal.blokken[2].tekst = Array(151).fill('woord').join(' ');
  assert.match(controleerOverzicht(lang).join('\n'), /hoogstens 150/);
  for (const term of ['de Wissel', 'een verdieping', 'Mijn stand', 'Kopieer naar A3', 'LUK 1', 'BC1', 'EV-01', 'je bewijsonderdeel', 'de richttijd', 'de Golden Circle', 'Sinek']) {
    const v = overzicht(); v.start.verhaal.blokken[0].tekst += ` ${term}.`;
    assert.match(controleerOverzicht(v).join('\n'), /hoort niet op het eerste scherm/, term);
  }
  const knop = overzicht(); knop.start.verhaal.knop = '';
  assert.match(controleerOverzicht(knop).join('\n'), /mist kop, knop of de regel naar de introductie/);
  const link = overzicht(); delete link.start.verhaal.introductie.link;
  assert.match(controleerOverzicht(link).join('\n'), /mist kop, knop of de regel naar de introductie/);
});
```

- [ ] **Step 2: Draai de test en zie hem falen**

Run: `node --test tests/content-check.test.mjs 2>&1 | grep -A3 "ST-8"`
Expected: FAIL; de eerste `deepEqual` faalt niet (er is nog geen controle), maar `/mist start\.verhaal/` vindt niets.

- [ ] **Step 3: Zet het verhaal in de data**

Gebruik de goedgekeurde tekst uit taak 1. Hieronder de concepttekst; vervang de waarden door de goedgekeurde. Het script zet `verhaal` als eerste sleutel in `start` en houdt de opmaak van het bestand (2 spaties, regeleinde aan het eind):

```bash
cd /Users/witoldtenhove/Documents/HAN/a3-learning/.worktrees/studentverhaal
node -e '
const fs = require("fs");
const p = "data/leerblokken.json";
const o = JSON.parse(fs.readFileSync(p, "utf8"));
const verhaal = {
  kop: "Waar gaat dit over?",
  blokken: [
    { id: "waarom", kop: "Waarom dit?", tekst: "Je opdrachtgever komt met een vraag die nog vaag is. Begin je meteen aan een oplossing, dan los je misschien het verkeerde probleem op. Hier maak je van die vage vraag een onderzoeksvraag waar je team mee verder kan. Die bespreek je met je opdrachtgever op je A3." },
    { id: "hoe", kop: "Hoe werk je?", tekst: "Je werkt aan je eigen vraagstuk. Elke taak laat het eerst zien met een voorbeeld, webshop X. Daarna doe je hetzelfde voor jouw vraag. Bij elke taak staat wanneer je klaar bent, en de site kijkt meteen mee. Je hebt geen account nodig: alles blijft in deze browser." },
    { id: "wat", kop: "Wat heb je aan het eind?", tekst: "Vier leerblokken van ongeveer 45 minuten. Daarna staat het eerste vak van je A3: je onderzoeksvraag, betrouwbare bronnen en een beeld van wie er bij je vraagstuk betrokken zijn. En je hebt een dossier met al je werk, dat je inlevert voor je portfolio." }
  ],
  knop: "Start met je vraagstuk",
  introductie: { tekst: "Hoe je je werk bewaart en inlevert, lees je in de", link: "introductie van één pagina" }
};
o.start = { verhaal, ...o.start };
fs.writeFileSync(p, JSON.stringify(o, null, 2) + "\n");
'
git diff --stat data/leerblokken.json
```

Expected: alleen `data/leerblokken.json` gewijzigd, ± 20 regels erbij, 0 regels eraf.

- [ ] **Step 4: Schrijf de controle**

In `tools/content-check.mjs`, direct boven `/** Controleert data/leerblokken.json: …`:

```js
/** Het verhaal bovenaan de startpagina (ST-8, ADR B113): drie blokken in deze volgorde. */
export const VERHAAL_BLOKKEN = Object.freeze(['waarom', 'hoe', 'wat']);
export const VERHAAL_MAX_WOORDEN = 150;
/** Wat niet op het eerste scherm hoort: onderdelen die pas later aan de beurt zijn (ST-7), systeemtaal (DESIGN §8) en het model achter de opbouw (B113). */
export const VERHAAL_VERBODEN = Object.freeze([/wissel/i, /verdieping/i, /mijn stand/i, /kopieer naar a3/i, /\bLUK\b/, /\bBC\d*\b/, /\bEV-/, /bewijsonderdeel/i, /richttijd/i, /golden circle/i, /sinek/i]);
```

In `controleerOverzicht`, direct na de regel `if (woorden === 0 || woorden > 100) fout(…(ST-2)`);`:

```js
  const verhaal = inhoud?.start?.verhaal;
  if (!verhaal) fout('mist start.verhaal, het verhaal bovenaan de startpagina (ST-8)');
  else {
    const vb = Array.isArray(verhaal.blokken) ? verhaal.blokken : [];
    const ids = vb.map((b) => b?.id).join(',');
    if (ids !== VERHAAL_BLOKKEN.join(',')) fout(`het verhaal moet precies de blokken waarom, hoe en wat hebben, in die volgorde (ST-8), niet ${ids}`);
    vb.forEach((b, i) => { if (!gevuld(b?.kop) || !gevuld(b?.tekst)) fout(`verhaalblok ${b?.id ?? i + 1} mist kop of tekst (ST-8)`); });
    if (!gevuld(verhaal.kop) || !gevuld(verhaal.knop) || !gevuld(verhaal.introductie?.tekst) || !gevuld(verhaal.introductie?.link)) {
      fout('het verhaal mist kop, knop of de regel naar de introductie (ST-8)');
    }
    const n = vb.map((b) => (typeof b?.tekst === 'string' ? b.tekst : '')).join(' ').trim().split(/\s+/).filter(Boolean).length;
    if (n > VERHAAL_MAX_WOORDEN) fout(`het verhaal heeft ${n} woorden lopende tekst, hoogstens ${VERHAAL_MAX_WOORDEN} (ST-8)`);
    const teksten = [verhaal.kop, verhaal.knop, verhaal.introductie?.tekst, verhaal.introductie?.link, ...vb.flatMap((b) => [b?.kop, b?.tekst])].filter((t) => typeof t === 'string');
    for (const re of VERHAAL_VERBODEN) {
      const treffer = teksten.map((t) => t.match(re)?.[0]).find(Boolean);
      if (treffer) fout(`het verhaal noemt „${treffer}”; dat hoort niet op het eerste scherm (ST-7, ST-8, DESIGN §8)`);
    }
  }
```

Pas ook de JSDoc-kop van `controleerOverzicht` aan: `… en de startinvoer (ST-1, ST-2).` → `… de startinvoer (ST-1, ST-2) en het verhaal (ST-8).`

- [ ] **Step 5: Draai de test**

Run: `node --test tests/content-check.test.mjs 2>&1 | tail -6`
Expected: de ST-8-test slaagt; andere tests in dit bestand kunnen nu falen op de fixtures (stap 6).

- [ ] **Step 6: Fixtures bijwerken**

```bash
node -e '
const fs = require("fs");
const verhaal = JSON.parse(fs.readFileSync("data/leerblokken.json", "utf8")).start.verhaal;
for (const m of ["content-goed", "content-concept", "content-vier-fouten"]) {
  const p = `tests/fixtures/${m}/leerblokken.json`;
  const o = JSON.parse(fs.readFileSync(p, "utf8"));
  o.start = { verhaal, ...o.start };
  fs.writeFileSync(p, JSON.stringify(o, null, 2) + "\n");
}
'
```

- [ ] **Step 7: Alles groen**

Run: `node --test 2>&1 | tail -4 && node tools/content-check.mjs | tail -3`
Expected: `fail 0`; content-check 0 fouten (de bestaande waarschuwingen blijven). In het bijzonder `formaat: de vier fouten van QA-3 …` telt nog precies 4.

- [ ] **Step 8: Commit**

```bash
git add tools/content-check.mjs data/leerblokken.json tests/content-check.test.mjs tests/fixtures/content-goed/leerblokken.json tests/fixtures/content-concept/leerblokken.json tests/fixtures/content-vier-fouten/leerblokken.json
git commit -m "B113, ST-8: verhaal voor de startpagina in de data (waarom, hoe, wat) met contentcontrole op volgorde, 150 woorden en termen die niet op het eerste scherm horen

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 4: `verhaalOpen` — eerste bezoek of terugkerend

**Files (a3-learning-worktree):**
- Modify: `js/weergave.js` (nieuwe export direct vóór `export function bouwIndexModel`)
- Test: `tests/weergave.test.mjs` (import uitbreiden; nieuwe test direct na de test `SX-2: bij het laden staat er geen melding; …`)

**Interfaces:**
- Consumes: een genormaliseerd profiel zoals `leesProfiel(store)` het geeft (`{ alias, teamnummer, vraagstuk, waaromZin: string (getrimd), voorlopig: boolean }`) en records zoals `leesRecords(store, ids)` ze geeft (`{ [id]: record | null | undefined }`).
- Produces: `verhaalOpen(profiel = {}, records = {}) → boolean` (`true` = open, eerste bezoek).

- [ ] **Step 1: Schrijf de falende test**

Breid de import in `tests/weergave.test.mjs` uit:

```js
import { bouwTaakModel, bouwIndexModel, bouwAfsluitModel, oefenModel, modelZichtbaar, verhaalOpen, STAPPEN, BEWAARMELDING } from '../js/weergave.js';
```

Voeg direct na de test `SX-2: …` toe:

```js
test('ST-8/ST-9: het verhaal staat alleen open bij een eerste bezoek (leeg profiel, geen werk)', () => {
  const leeg = normaliseerProfiel({});
  assert.equal(verhaalOpen(leeg, {}), true);
  assert.equal(verhaalOpen(leeg, { 'EV-01': undefined, 'EV-02': null }), true, 'ids zonder record tellen niet');
  assert.equal(verhaalOpen(normaliseerProfiel({ alias: '   ' }), {}), true, 'alleen spaties is leeg');
  assert.equal(verhaalOpen(undefined, undefined), true, 'zonder opslag: open');
  assert.equal(verhaalOpen(normaliseerProfiel({ alias: 'Kim' }), {}), false);
  assert.equal(verhaalOpen(normaliseerProfiel({ teamnummer: '7' }), {}), false, 'alleen een teamnummer');
  assert.equal(verhaalOpen(normaliseerProfiel({ voorlopig: true }), {}), false, 'alleen „nog geen scherp vraagstuk”');
  assert.equal(verhaalOpen(leeg, { 'EV-01': rec('bijna') }), false, 'werk zonder profiel');
});

test('ST-8: weergave.js laadt profiel.js niet mee (bronnen en terugblik gebruiken weergave.js via metro-model.js)', () => {
  const bron = readFileSync(resolve(root, 'js/weergave.js'), 'utf8');
  assert.doesNotMatch(bron, /from '\.\/profiel\.js'/);
});
```

- [ ] **Step 2: Draai de test en zie hem falen**

Run: `node --test tests/weergave.test.mjs 2>&1 | grep -B1 -A3 "ST-8/ST-9"`
Expected: FAIL met „verhaalOpen is not a function” (of een SyntaxError op de import).

- [ ] **Step 3: Schrijf de functie**

In `js/weergave.js`, direct vóór `export function bouwIndexModel`:

```js
/**
 * Staat het verhaal van de startpagina open (eerste bezoek) of ingeklapt (ST-8, ST-9, ADR B113)? Open zolang de student
 * niets heeft ingevuld en geen werk heeft. De startpagina vraagt dit alleen bij het laden: typen in het formulier bewaart
 * het profiel bij elke toets, en het verhaal mag dan niet inklappen.
 * @param {{alias?: string, teamnummer?: string, vraagstuk?: string, waaromZin?: string, voorlopig?: boolean}} profiel zoals leesProfiel het geeft
 * @param {Record<string, object|null|undefined>} records zoals leesRecords ze geeft
 */
export function verhaalOpen(profiel = {}, records = {}) {
  const ingevuld = Object.values(profiel).some((v) => v === true || (typeof v === 'string' && v.trim() !== ''));
  return !ingevuld && !Object.values(records).some(Boolean);
}
```

- [ ] **Step 4: Draai de test**

Run: `node --test tests/weergave.test.mjs 2>&1 | tail -4`
Expected: `fail 0`.

- [ ] **Step 5: Commit**

```bash
git add js/weergave.js tests/weergave.test.mjs
git commit -m "B113, ST-8, ST-9: verhaalOpen beslist bij het laden of het verhaal open staat (leeg profiel en geen werk)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 5: Het verhaal op de startpagina

**Files (a3-learning-worktree):**
- Modify: `js/index-pagina.js` (import, beslissing na `const profiel = leesProfiel(store);`, regel „Nieuw hier?” weg, verhaal tekenen vóór `const gegevens`, volgorde in `main.append`)
- Modify: `css/site.css` (nieuw blok direct na `.verder-kaart .knop-accent { … }`)
- Modify: `README.md` (de alinea die begint met `` `data/leerblokken.json` bevat de startinvoer``)
- Test: `tests/weergave.test.mjs` (broncode-test direct na de tests van taak 4)

**Interfaces:**
- Consumes: `verhaalOpen` (taak 4), `overzicht.start.verhaal` (taak 3), bestaande `leesProfiel`, `leesRecords`, `h`, `invoer.alias`.
- Produces: in de DOM `#verhaal` (section, eerste bezoek) of `.verhaal-details` (details, terugkerend); knop `#verhaal button.knop-accent`.

- [ ] **Step 1: Schrijf de falende broncode-test**

In `tests/weergave.test.mjs`, na de tests van taak 4:

```js
test('ST-8/ST-9: de startpagina beslist één keer, bij het laden, en werkt zonder verhaal in de data', () => {
  const bron = readFileSync(resolve(root, 'js/index-pagina.js'), 'utf8');
  assert.equal((bron.match(/verhaalOpen\(/g) ?? []).length, 1, 'één beslissing');
  assert.ok(bron.indexOf('verhaalOpen(') < bron.indexOf('const bijwerken'), 'vóór er iets bewaard kan worden');
  assert.match(bron, /if \(verhaal && eersteBezoek\)/, 'zonder start.verhaal geen verhaal en geen fout');
  assert.match(bron, /invoer\.alias\.focus\(\)/, 'de knop zet de focus in het aliasveld');
  assert.doesNotMatch(bron, /Nieuw hier\?/, 'de oude introductieregel is weg');
  assert.match(bron, /\.filter\(Boolean\)\)/, 'main.append krijgt geen null');
});
```

- [ ] **Step 2: Draai de test en zie hem falen**

Run: `node --test tests/weergave.test.mjs 2>&1 | grep -A3 "beslist één keer"`
Expected: FAIL op „één beslissing” (0 in plaats van 1).

- [ ] **Step 3: Pas `js/index-pagina.js` aan**

(a) Commentaarkop, eerste regel: `// Startpagina: startinvoer (ST-1), …` → `// Startpagina: het verhaal (ST-8, ST-9), startinvoer (ST-1), …`

(b) Import:

```js
import { bouwIndexModel, verhaalOpen } from './weergave.js';
```

(c) Direct na `const profiel = leesProfiel(store);`:

```js
  // ST-8, ST-9: open of ingeklapt ligt vast bij het laden; bijwerken() bewaart het profiel bij elke toets.
  const eersteBezoek = verhaalOpen(profiel, leesRecords(store, alleIds));
```

(d) In `start1` de regel weghalen:

```js
    h('p', { class: 'klein' }, 'Nieuw hier? Lees de ', h('a', { href: 'docs/studentintroductie.html' }, 'introductie van één pagina'), '.'),
```

(e) Direct vóór `const gegevens = h('section', { id: 'gegevens', …`:

```js
  // ---- het verhaal (ST-8, ST-9, ADR B113): waarom, hoe, wat. Bij een eerste bezoek open boven het formulier, daarna
  // ingeklapt onder de leerblokken. Ontbreekt het in de data, dan werkt de pagina zonder.
  const verhaal = overzicht.start.verhaal;
  const verhaalBlokken = () => h('div', { class: 'verhaal-blokken' },
    verhaal.blokken.map((b) => h('div', { class: 'kaart verhaal-blok' }, h('h3', {}, b.kop), h('p', {}, b.tekst))));
  const naarIntroductie = () => h('p', { class: 'klein' }, `${verhaal.introductie.tekst} `,
    h('a', { href: 'docs/studentintroductie.html' }, verhaal.introductie.link), '.');
  let verhaalEl = null;
  if (verhaal && eersteBezoek) {
    verhaalEl = h('section', { id: 'verhaal', class: 'verhaal', 'aria-labelledby': 'verhaal-kop' },
      h('h2', { id: 'verhaal-kop', class: 'eyebrow' }, verhaal.kop),
      verhaalBlokken(),
      h('button', { type: 'button', class: 'knop knop-accent', onclick: () => invoer.alias.focus() }, verhaal.knop),
      naarIntroductie());
  } else if (verhaal) {
    verhaalEl = h('details', { class: 'verhaal-details' }, h('summary', {}, verhaal.kop), verhaalBlokken(), naarIntroductie());
  }
```

(f) Vervang `main.append(h1, verder, a3, start1, blokken, gegevens);` door:

```js
  main.append(...[h1, verder, a3, eersteBezoek ? verhaalEl : null, start1, blokken, eersteBezoek ? null : verhaalEl, gegevens].filter(Boolean));
```

- [ ] **Step 4: CSS**

In `css/site.css`, direct na `.verder-kaart .knop-accent { margin-top:.5rem; border-color:var(--wit); }`:

```css
/* het verhaal bovenaan de startpagina (ST-8, ST-9, ADR B113): informatie, dus rand en geen schaduw (SX-7) */
.verhaal { margin:1rem 0 1.5rem; }
.verhaal-blokken { display:grid; grid-template-columns:repeat(auto-fit, minmax(14rem, 1fr)); gap:.75rem; margin:.5rem 0 1rem; }
.verhaal-blok { margin:0; }
.verhaal-blok h3 { margin:0 0 .4rem; }
.verhaal-blok p { margin:0; }
.verhaal-details { margin:1.5rem 0; }
.verhaal-details > summary { cursor:pointer; font-weight:700; min-height:2.75rem; display:flex; align-items:center; }
```

- [ ] **Step 5: Tests en controles**

```bash
node --test 2>&1 | tail -4
node tools/content-check.mjs | tail -2
node tools/gewicht-check.mjs | grep -i "index\|fout"
node tools/link-check.mjs | tail -2
```

Expected: `fail 0`; 0 fouten; index binnen 300 kB gzip en 500 kB bron; 0 kapotte links.

- [ ] **Step 6: Doorloop in de browser**

Start een server in de worktree (achtergrond): `python3 -m http.server 8765 --directory /Users/witoldtenhove/Documents/HAN/a3-learning/.worktrees/studentverhaal`. Gebruik de Playwright-tools. Elk punt heeft een verwachte uitkomst; noteer per punt geslaagd of niet.

1. Venster 360 × 800 (`browser_resize`). Ga naar `http://localhost:8765/index.html`, voer `localStorage.clear()` uit (`browser_evaluate`) en herlaad.
2. Evalueer:
   ```js
   () => { const v = document.querySelector('#verhaal'), s = document.querySelector('#start');
     return { verhaal: !!v, voorStart: !!(v && s && (v.compareDocumentPosition(s) & Node.DOCUMENT_POSITION_FOLLOWING)),
       koppen: [...document.querySelectorAll('#verhaal h3')].map((x) => x.textContent),
       details: !!document.querySelector('.verhaal-details'), nieuwHier: document.body.textContent.includes('Nieuw hier?'),
       scroll: document.documentElement.scrollWidth, metroBovenMain: !!document.querySelector('body > nav.metro + main, body > nav.metro ~ main') }; }
   ```
   Verwacht: `verhaal: true`, `voorStart: true`, drie koppen in de volgorde waarom, hoe, wat, `details: false`, `nieuwHier: false`, `scroll` ≤ 360, `metroBovenMain: true`.
3. Klik op „Start met je vraagstuk”. Evalueer `() => { const a = document.activeElement, r = a.getBoundingClientRect(); return { id: a.id, top: r.top, bottom: r.bottom, hoogte: innerHeight }; }`. Verwacht: `id: 'start-alias'`, `top` ≥ 0 en `bottom` ≤ `hoogte` − 72 (boven de tabbalk onderin). Maak een schermafbeelding.
4. Typ „Kim” in het aliasveld. Evalueer `() => !!document.querySelector('#verhaal')`. Verwacht: `true` (niets klapt in tijdens het typen).
5. Herlaad. Evalueer `() => { const d = document.querySelector('.verhaal-details'), b = document.querySelector('#blokken'); return { sectie: !!document.querySelector('#verhaal'), details: !!d, open: d?.open, naBlokken: !!(d && b && (b.compareDocumentPosition(d) & Node.DOCUMENT_POSITION_FOLLOWING)), knop: !!d?.querySelector('button') }; }`. Verwacht: `sectie: false`, `details: true`, `open: false`, `naBlokken: true`, `knop: false`.
6. Klap de samenvatting open: drie blokken en de link naar `docs/studentintroductie.html` zichtbaar; de link opent de introductie.
7. Kies „Wis alles” en bevestig. Verwacht: geen fout in de console; het verhaal blijft ingeklapt tot je herlaadt; na herladen staat het open boven het formulier.
8. Venster 1280 × 800, lege opslag, herlaad. Evalueer `() => [...document.querySelectorAll('.verhaal-blok')].map((x) => Math.round(x.getBoundingClientRect().top))`. Verwacht: drie gelijke waarden (naast elkaar). Maak een schermafbeelding.
9. `browser_console_messages`: geen fouten op de startpagina.

Vind je een fout: schrijf eerst een test die hem vangt (broncode of pure functie), herstel, en herhaal het punt.

- [ ] **Step 7: README**

Vervang in `README.md` het begin van de alinea `` `data/leerblokken.json` bevat de startinvoer (velden, privacytekst) en de vier leerblokken voor `index.html` `` door:

```markdown
`data/leerblokken.json` bevat het verhaal van de startpagina (`start.verhaal`: waarom, hoe, wat, ≤ 150 woorden, ST-8, ADR B113; open bij een eerste bezoek, daarna ingeklapt onder de leerblokken, `verhaalOpen` in `js/weergave.js`), de startinvoer (velden, privacytekst) en de vier leerblokken voor `index.html`
```

De rest van de alinea blijft staan.

- [ ] **Step 8: Commit**

```bash
git add js/index-pagina.js css/site.css README.md tests/weergave.test.mjs
git commit -m "B113, ST-8, ST-9: verhaal op de startpagina (waarom, hoe, wat): open boven het formulier bij een eerste bezoek met de knop naar het aliasveld, daarna ingeklapt onder de leerblokken; regel Nieuw hier? vervangen

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 6: BUILDPLAN en afronding

**Files (c-cluster-1-worktree):**
- Modify: `docs/BUILDPLAN-ELEARNING-A3.md` (nieuwe sectie direct vóór `## Bijlage — Dekking van de blueprintregels per fase`)

- [ ] **Step 1: Aanvulling in het BUILDPLAN**

Voeg direct vóór `## Bijlage — Dekking van de blueprintregels per fase` in (na een eventuele aanvulling van B114):

```markdown
## Aanvulling — Verhaal voor studenten op de startpagina (1-10-2026, op verzoek van de auteur)

Spec: `docs/superpowers/specs/2026-10-01-studentverhaal-startpagina-design.md`; plan: `docs/superpowers/plans/2026-10-01-studentverhaal-startpagina.md`. Besluit: ADR B113.

- [x] Tekst van het verhaal (waarom, hoe, wat) geredigeerd en goedgekeurd door de auteur.
- [x] `start.verhaal` in `data/leerblokken.json` met contentcontrole: drie blokken in volgorde, ≤ 150 woorden, geen termen die niet op het eerste scherm horen (ST-8).
- [x] `verhaalOpen` in `js/weergave.js` met tests: open bij een leeg profiel zonder werk, anders ingeklapt (ST-9).
- [x] Verhaal op de startpagina, de regel „Nieuw hier?” vervangen; doorloop in de browser op 360 en 1280 px (9 punten uit het plan).
```

Zet een vinkje alleen bij wat echt af is; noem een gevonden en herstelde fout in één zin achter het laatste punt, zoals bij de metrokaart.

- [ ] **Step 2: Commit**

```bash
cd /Users/witoldtenhove/Documents/HAN/c-cluster-1/.worktrees/studentverhaal
git add docs/BUILDPLAN-ELEARNING-A3.md
git commit -m "BUILDPLAN: aanvulling verhaal voor studenten op de startpagina (B113)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

- [ ] **Step 3: Eindcontrole**

```bash
cd /Users/witoldtenhove/Documents/HAN/a3-learning/.worktrees/studentverhaal && node --test 2>&1 | tail -4 && node tools/content-check.mjs | tail -2 && git log --oneline origin/main..HEAD
cd /Users/witoldtenhove/Documents/HAN/c-cluster-1/.worktrees/studentverhaal && git log --oneline origin/main..HEAD
```

Expected: `fail 0`, 0 fouten; in a3-learning drie commits (taak 3, 4, 5); in c-cluster-1 spec, plan, eventueel de spec-tekst (taak 1), documenten (taak 2) en BUILDPLAN (taak 6).

- [ ] **Step 4: Overdracht**

Meld de andere sessies (c-cluster-1-72, c-cluster-1-ab) dat B113 klaarstaat op de branches `studentverhaal`. Push niet. Gebruik de skill `superpowers:finishing-a-development-branch` om met de auteur te kiezen hoe het naar `main` gaat (in beide repo's eerst `git rebase origin/main` in de worktree, dan pas pushen).

---

## Uitbreiding na akkoord van de auteur (1 oktober 2026)

Spec §9 (tijd en planning in de studentintroductie) en §10 (B118: de richttijd volgt de taken) kwamen tijdens de uitvoering op verzoek van de auteur erbij. Deze sectie gaat vóór de taken hierboven waar ze verschillen.

**Gewijzigde Global Constraints.**
- LRD-versie **0.26** (besluit van de auteur; 0.22 en 0.24 blijven ongebruikt). ADR **B113** en **B118**. B42 en B53 krijgen in de statuskolom „Deels vervangen door B118”.
- Richttijd per leerblok = som van `richttijd.minuten` van de taken in `data/leerblok-N.json` (verdieping telt niet): 30, 45, 105, 45. De terugblik (`terugblik` in `leerblokken.json`, 15 voor leerblok 2–4) komt erbovenop.
- Totale tijd = Σ richttijd + Σ terugblik = 270 min, afgerond op een half uur: „ongeveer 4½ uur”. Eén functie `totaleTijdTekst(overzicht)` in `tools/content-check.mjs` rekent dat uit; het verhaal en de introductie worden ertegen getoetst.
- Goedgekeurde teksten: spec §3.3 (verhaal; blok „wat” begint met „Je doet vier leerblokken, samen ongeveer 4½ uur.”) en spec §9 (introductie). Linkregel: tekst „Hoeveel tijd het kost, hoe je plant en hoe je inlevert, lees je in de”, link „introductie van één pagina”.
- Studentintroductie: 4 onderwerpen (wat je doet, tijd en planning, gegevens, exporteren en inleveren), ≤ 550 woorden, afdruk 1 pagina A4.

**Volgorde van uitvoering:** 2 → 2b → 3 → 4 → 5 → 5b → 6.

### Aanvulling op Task 2 (documenten)

Naast stap 1–8, in dezelfde commit; overal **0.26** in plaats van 0.24 (kop van ADR en LRD, versieregel „0.25: … B115; 0.26: verhaal voor studenten op de startpagina en richttijd volgens de taken, B113 en B118”).

- [ ] **2.A ADR B118** onderaan, na B113:

```markdown
| B118 | 1-10-2026 | 40 | De richttijd van een leerblok is de som van de richttijden van zijn taken; de verdieping telt niet mee (TK-14) en de terugblik van hoogstens 15 minuten komt er vanaf leerblok 2 bovenop (B53). Nu: leerblok 1 30 min, 2 45 min, 3 105 min, 4 45 min; samen 225 min, met terugblikken hoogstens 270 min. De taken in `data/leerblok-N.json` zijn de bron; `content-check` eist dat de richttijd in het leerblokbestand en in `leerblokken.json` gelijk is aan die som, in plaats van precies 45 (FR-44, NFR-07, LB-1, PF-5). De terugblikpagina noemt de richttijd van het eigen leerblok. De studentintroductie krijgt het onderwerp „Tijd en planning” met de tijden per leerblok en planningsadvies voor zelfstudie (DL-2, B113) | Verzoek van de auteur: studenten krijgen voorlichting over de tijdsinzet, en die moet kloppen. Leerblok 3 heette 45 min terwijl de taken volgens het werkboek 105 min tellen; B68 (punt 6) wees dat al aan (het werkboek telt teamwerk aan de muur mee) en legde de ijking bij de pilot. Een student in zelfstudie plant liever te ruim dan te krap; de pilot (AC-08) blijft de tijd ijken. Afgewezen: (a) eerlijk in de voorlichting en de leerblokkaart later (twee tijden voor hetzelfde blok op één startpagina); (b) 45 min aanhouden tot de pilot (studenten lopen bij leerblok 3 vrijwel zeker uit); (c) een eigen schatting voor leerblok 3 (dan geen controleerbare regel meer) | Verzoek van de auteur; uitwerking Claude | Aangenomen |
```

- [ ] **2.B ADR B42 en B53:** vervang in hun statuskolom ` Aangenomen ` door ` Aangenomen; deels vervangen door B118 (richttijd per leerblok volgt de taken) `. Controleer eerst met `grep -n "^| B42 \|^| B53 " docs/ADR-ELEARNING-A3.md` wat er nu staat; laat andere statustekst staan en voeg de zin achteraan toe.
- [ ] **2.C LRD, B118** (zoek op de aangehaalde tekst; regel 119, de versiegeschiedenis „0.7: vier leerblokken van 45 minuten”, blijft staan):
  - Scope: „van vier leerblokken van 45 minuten met twee gebruiksvormen” → „van vier leerblokken (samen ongeveer 4 uur, met de terugblikken 4½ uur) met twee gebruiksvormen”.
  - 3.x: „gebundeld in vier leerblokken van 45 minuten (FR-44, B42)” → „gebundeld in vier leerblokken (FR-44, B42, B118)”.
  - Begrippen: „een van de vier eenheden van 45 minuten van de e-learning (8.1)” → „een van de vier eenheden van de e-learning, elk met een eigen richttijd (8.1)”.
  - Overal „bovenop de 45 minuten van het leerblok” en „bovenop de 45 minuten” → „bovenop de richttijd van het leerblok” (6.x, FR-62, 8.x, risicotabel).
  - FR-44: „toont de student vier leerblokken van 45 minuten (” → „toont de student vier leerblokken („ blijft; voeg achter „met per leerblok de richttijd” toe: „ (de som van de richttijden van de taken, B118)”; bronkolom `B42, 3.2` → `B42, B118, 3.2`.
  - NFR-07: „Elk leerblok heeft een richttijd van 45 minuten op de pagina, inclusief” → „Elk leerblok heeft op de pagina een richttijd die de som is van de richttijden van zijn taken (nu 30, 45, 105 en 45 minuten, B118), inclusief”.
  - Deel 8: „Programma: vier leerblokken van 45 minuten, en het werkcollege” → „Programma: vier leerblokken en het werkcollege”; „De e-learning heeft vier leerblokken van 45 minuten (richttijd, inclusief media).” → „De e-learning heeft vier leerblokken; de richttijd van een leerblok is de som van zijn taken, inclusief media (30, 45, 105 en 45 minuten, B118).”
  - Tabel weekprogramma: richttijd leerblok 1 `45` → `30`, leerblok 3 `45 + 15` → `105 + 15`.
  - AC-08: „binnen 1,25 keer de richttijd van 45 minuten” → „binnen 1,25 keer de richttijd van dat leerblok”.
  - Controle: `python3 -c "import re;t=re.sub(r'<[^>]+>','',open('docs/LRD-ELEARNING-A3.html').read());print([m.start() for m in re.finditer('45 min',t)])"` geeft alleen nog de versiegeschiedenis.
- [ ] **2.D BLUEPRINT, B118 en DL-2:**
  - SMART-tabel: „binnen 1,25 × de richttijd van 45 min” → „binnen 1,25 × de richttijd van dat leerblok”; „Richttijd 45 min per leerblok (+ ≤ 15 min terugblik vanaf leerblok 2)” → „Richttijd per leerblok = som van de taken: 30, 45, 105, 45 min (+ ≤ 15 min terugblik vanaf leerblok 2)”.
  - §3 Componenten: „vier leerblokken van 45 min met taken” → „vier leerblokken met taken”.
  - TK-14 criterium: „0 minuten in de richttijd van 45 min” → „0 minuten in de richttijd”.
  - LB-1 criterium: „4 leerblokken van 45 min;” → „4 leerblokken, elk met een richttijd gelijk aan de som van de taken (30, 45, 105, 45 min);”.
  - TP-1: „bovenop de 45 min van het leerblok” → „bovenop de richttijd van het leerblok”.
  - PF-3: „tijdens 45 min gebruik” → „tijdens het gebruik van een geladen leerblok (≥ 45 min)”.
  - PF-5: eis „Elk leerblok moet een richttijd van 45 min op de pagina tonen, inclusief media.” → „Elk leerblok moet op de pagina een richttijd tonen die gelijk is aan de som van de richttijden van zijn taken, inclusief media.”; criterium „45 min;” → „richttijd = som van de taken (B118);”.
  - DL-2: eis → „Er moet een studentintroductie zijn over wat je doet, tijd en planning, waar je gegevens staan en hoe je exporteert en inlevert.”; criterium → „≤ 1 pagina A4; 4 onderwerpen; ≤ 550 woorden; de tijd per leerblok gelijk aan de data”.
- [ ] **2.E DESIGN §5.1**: in het punt over de linkregel staat al „de link naar de introductie van één pagina”; voeg toe: „(„Hoeveel tijd het kost, hoe je plant en hoe je inlevert, lees je in de introductie van één pagina.”)”.

Commitbericht: `ADR B113, B118; LRD 0.26; FR-44, FR-75, NFR-07, AC-08, AC-51, ST-8, ST-9, LB-1, PF-5, TK-14, DL-2: verhaal voor studenten op de startpagina, richttijd volgens de taken (LRD, ADR, BLUEPRINT, DESIGN)`.

### Task 2b: De richttijd volgt de taken op de site (B118)

**Files (a3-learning-worktree):** `tools/content-check.mjs`, `data/leerblokken.json`, `data/leerblok-1.json`, `data/leerblok-3.json`, de fixtures in `tests/fixtures/content-*/`, `js/terugblik-pagina.js`, `tests/content-check.test.mjs`, `tests/toegankelijk.test.mjs`, `tests/weergave.test.mjs`, `tests/lb4.test.mjs`, `tests/terugblik.test.mjs`.

**Interfaces — Produces:** `controleerRichttijden(overzicht, blokken) → string[]` en `totaleTijdTekst(overzicht) → string` (bv. `'4½ uur'`) uit `tools/content-check.mjs`.

- [ ] **Step 1: falende tests.** In `tests/content-check.test.mjs` (import uitbreiden met `controleerRichttijden, totaleTijdTekst`), direct na de test `LB-1/ST-1/ST-2 …`:

```js
test('B118: de richttijd van een leerblok is de som van zijn taken, in het leerblokbestand en in het overzicht', () => {
  const blokken = [1, 2, 3, 4].map((n) => JSON.parse(readFileSync(resolve(root, `data/leerblok-${n}.json`), 'utf8')));
  assert.deepEqual(controleerRichttijden(overzicht(), blokken), []);
  assert.deepEqual(blokken.map((b) => b.richttijd), [30, 45, 105, 45]);
  const fout = structuredClone(blokken); fout[2].richttijd = 45;
  assert.match(controleerRichttijden(overzicht(), fout).join('\n'), /leerblok-3\.json: richttijd 45 min, maar de taken tellen op tot 105 min/);
  const o = overzicht(); o.leerblokken[0].richttijd = 45;
  assert.match(controleerRichttijden(o, blokken).join('\n'), /leerblokken\.json: leerblok 1 heeft richttijd 45 min, maar de taken tellen op tot 30 min/);
});

test('B118: de totale tijd is de som van richttijden en terugblikken, afgerond op een half uur', () => {
  assert.equal(totaleTijdTekst(overzicht()), '4½ uur');
  const o = overzicht(); o.leerblokken[2].richttijd = 45;
  assert.equal(totaleTijdTekst(o), '3½ uur');
  o.leerblokken[2].richttijd = 75;
  assert.equal(totaleTijdTekst(o), '4 uur');
});
```

Pas in `tests/toegankelijk.test.mjs` de test `PF-5: …` aan: naam „PF-5: elk leerblok toont zijn richttijd, de som van de taken zonder verdieping (B118)”; vervang `for (const b of overzicht.leerblokken) assert.equal(b.richttijd, 45, …)` door

```js
  for (const b of overzicht.leerblokken) {
    const blok = JSON.parse(lees(`data/leerblok-${b.nummer}.json`));
    assert.equal(b.richttijd, blok.taken.reduce((s, t) => s + t.richttijd.minuten, 0), `leerblok ${b.nummer}`);
  }
```

In `tests/weergave.test.mjs`, test `LB-1/TK-1: …`: naam „… vier leerblokken met hun richttijd …”; vervang `assert.ok(m.every((b) => b.richttijdTekst.startsWith('45 min')));` door `assert.deepEqual(m.map((b) => Number.parseInt(b.richttijdTekst, 10)), [30, 45, 105, 45]);`. In `tests/lb4.test.mjs`, test `TK-14: …`: naam „… 0 minuten in de richttijd door een verdiepingstaak …” en voeg toe `assert.equal(blok4.richttijd, 45);`. In `tests/terugblik.test.mjs` een nieuwe test:

```js
test('B118: de terugblik noemt de richttijd van het eigen leerblok, geen vaste 45 min', () => {
  const bron = readFileSync(resolve(root, 'js/terugblik-pagina.js'), 'utf8');
  assert.doesNotMatch(bron, /bovenop de 45 min/);
  assert.match(bron, /bovenop de \$\{richttijd\} min van het leerblok/);
});
```

(Gebruik in `tests/terugblik.test.mjs` de bestaande `root` of definieer `const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');` als die ontbreekt.)

- [ ] **Step 2: zie ze falen.** `node --test tests/content-check.test.mjs tests/toegankelijk.test.mjs tests/weergave.test.mjs tests/lb4.test.mjs tests/terugblik.test.mjs 2>&1 | grep -E "^not ok|fail "`. Verwacht: B118-tests falen (functies ontbreken, richttijden 45), PF-5 en LB-1 falen op leerblok 1 en 3.

- [ ] **Step 3: content-check.** In `controleerOverzicht`: vervang `if (b.richttijd !== 45) fout(\`leerblok ${i + 1} moet een richttijd van 45 min hebben\`);` door `if (!Number.isInteger(b.richttijd) || b.richttijd <= 0) fout(\`leerblok ${i + 1} mist een richttijd in hele minuten (LB-1)\`);`. Voeg direct na `controleerOverzicht` toe:

```js
/** B118: de richttijd van een leerblok is de som van de richttijden van zijn taken, zonder verdieping (PF-5, LB-1). */
export function controleerRichttijden(overzicht, blokken) {
  const fouten = [];
  for (const blok of blokken) {
    const som = (blok.taken ?? []).reduce((s, t) => s + (t.richttijd?.minuten ?? 0), 0);
    if (blok.richttijd !== som) fouten.push(`leerblok-${blok.leerblok}.json: richttijd ${blok.richttijd} min, maar de taken tellen op tot ${som} min (B118, PF-5)`);
    const lb = overzicht?.leerblokken?.find((b) => b.nummer === blok.leerblok);
    if (lb && lb.richttijd !== som) fouten.push(`leerblokken.json: leerblok ${blok.leerblok} heeft richttijd ${lb.richttijd} min, maar de taken tellen op tot ${som} min (B118, LB-1)`);
  }
  return fouten;
}

/** De totale tijd van de vier leerblokken met terugblikken, afgerond op een half uur: „4½ uur” (B113, B118). */
export function totaleTijdTekst(overzicht) {
  const min = (overzicht?.leerblokken ?? []).reduce((s, b) => s + (b.richttijd ?? 0) + (b.terugblik ?? 0), 0);
  const halven = Math.round(min / 30);
  return `${Math.floor(halven / 2)}${halven % 2 ? '½' : ''} uur`;
}
```

In `controleerMap` vervang `else { const o = lees('leerblokken.json'); if (o) fouten.push(...controleerOverzicht(o)); }` door `else { const o = lees('leerblokken.json'); if (o) fouten.push(...controleerOverzicht(o), ...controleerRichttijden(o, blokken)); }`. Werk het commentaar bovenaan (`"richttijd": 45`) bij naar `"richttijd": 30`.

- [ ] **Step 4: data en fixtures.**

```bash
node -e '
const fs = require("fs");
const zet = (dir) => {
  const op = (p) => fs.existsSync(p) ? JSON.parse(fs.readFileSync(p, "utf8")) : null;
  const schrijf = (p, o) => fs.writeFileSync(p, JSON.stringify(o, null, 2) + "\n");
  const ov = op(`${dir}/leerblokken.json`);
  for (const n of [1, 2, 3, 4]) {
    const p = `${dir}/leerblok-${n}.json`; const b = op(p); if (!b) continue;
    const som = b.taken.reduce((s, t) => s + (t.richttijd?.minuten ?? 0), 0);
    if (b.richttijd !== som) { b.richttijd = som; schrijf(p, b); }
    const lb = ov?.leerblokken.find((x) => x.nummer === n); if (lb) lb.richttijd = som;
  }
  if (ov) schrijf(`${dir}/leerblokken.json`, ov);
};
for (const d of ["data", "tests/fixtures/content-goed", "tests/fixtures/content-concept", "tests/fixtures/content-vier-fouten"]) zet(d);
'
git diff --stat
```

Controleer vooraf dat `data/leerblok-N.json` 2-spatie-JSON is (`node -e 'const t=require("fs").readFileSync("data/leerblok-3.json","utf8");console.log(t===JSON.stringify(JSON.parse(t),null,2)+"\n")'` → `true`); zo niet, pas dan alleen de regel `"richttijd": 45` met de hand aan. Let op: de fixture „vier fouten” mag precies 4 fouten houden.

- [ ] **Step 5: terugblikpagina.** In `js/terugblik-pagina.js`, in `vorigeKeerSectie` direct na `const vorig = leerblok - 1;`: `const richttijd = overzicht.leerblokken.find((b) => b.nummer === leerblok)?.richttijd;` en in `tekenKop`: `bovenop de 45 min van het leerblok` → `bovenop de ${richttijd} min van het leerblok`.

- [ ] **Step 6: alles groen.** `node --test 2>&1 | tail -4 && node tools/content-check.mjs | tail -1`. Verwacht `fail 0`, content-check ok.

- [ ] **Step 7: commit.** `git add` van precies de gewijzigde bestanden uit „Files”; bericht: `B118, PF-5, LB-1: richttijd per leerblok is de som van de taken (leerblok 1 30 min, leerblok 3 105 min); content-check controleert dat in plaats van precies 45; terugblik noemt de eigen richttijd`.

### Aanpassing van Task 3 (verhaal in de data)

- Gebruik in stap 3 de goedgekeurde tekst uit spec §3.3 en de nieuwe linkregel (Global Constraints hierboven).
- Voeg in stap 4 aan de verhaalcontrole toe (na de woordtelling): `const wat = vb.find((b) => b?.id === 'wat'); if (wat && !String(wat.tekst).includes(\`ongeveer ${totaleTijdTekst(inhoud)}\`)) fout(\`het blok „wat” noemt niet de totale tijd „ongeveer ${totaleTijdTekst(inhoud)}” (B118, ST-8)\`);` (`totaleTijdTekst` staat na taak 2b in hetzelfde bestand; een functiedeclaratie is overal in de module bruikbaar).
- Voeg in stap 1 aan de test toe: `const tijd = overzicht(); tijd.leerblokken[2].richttijd = 45; assert.match(controleerOverzicht(tijd).join('\n'), /noemt niet de totale tijd „ongeveer 3½ uur”/);`

### Task 5b: Tijd en planning in de studentintroductie; docentgids

**Files (a3-learning-worktree):** `docs/studentintroductie.html`, `docs/docentgids.html`, `tests/docs.test.mjs`.

- [ ] **Step 1: falende test.** Vervang in `tests/docs.test.mjs` `'docs/studentintroductie.html': 450` door `550`, en de test `DL-2: …` door:

```js
test('DL-2: de studentintroductie heeft 4 onderwerpen (wat je doet, tijd en planning, gegevens, exporteren en inleveren) en hoogstens 550 woorden', () => {
  const html = lees('docs/studentintroductie.html');
  const h2 = koppen(html, 2);
  assert.equal(h2.length, 4);
  assert.match(h2[0], /wat je doet/i);
  assert.match(h2[1], /tijd en planning/i);
  assert.match(h2[2], /gegevens/i);
  assert.match(h2[3], /exporteren en inleveren/i);
  assert.ok(woorden(html) <= MAX_WOORDEN['docs/studentintroductie.html'], `${woorden(html)} woorden`);
  assert.match(html, /Dossier exporteren \(JSON\)/, 'de knopnaam van de site staat er letterlijk in');
  assert.match(html, /Wis alles/);
});

test('DL-2, B118: „Tijd en planning” noemt de richttijd van elk leerblok en de totale tijd uit de data', () => {
  const html = lees('docs/studentintroductie.html');
  const h2 = koppen(html, 2);
  const tijd = html.slice(html.indexOf(h2[1]), html.indexOf(h2[2]));
  const overzicht = JSON.parse(lees('data/leerblokken.json'));
  for (const b of overzicht.leerblokken) assert.match(tijd, new RegExp(`Leerblok ${b.nummer}: ± ${b.richttijd} min`), `leerblok ${b.nummer}`);
  assert.match(tijd, new RegExp(`ongeveer ${totaleTijdTekst(overzicht)}`));
});
```

Importeer `totaleTijdTekst` uit `../tools/content-check.mjs`. Controleer eerst hoe `lees`, `koppen` en `woorden` in dat bestand heten (ze bestaan al).

- [ ] **Step 2: zie hem falen.** `node --test tests/docs.test.mjs 2>&1 | grep -E "^not ok|fail "` → de twee DL-2-tests falen (3 koppen, geen „Tijd en planning”).

- [ ] **Step 3: tekst.** Voeg in `docs/studentintroductie.html` na de sectie `<h2>1. Wat je doet</h2>…` (vóór `<h2>2. Waar je gegevens staan</h2>`) in, en hernummer de volgende koppen naar 3 en 4:

```html
<h2>2. Tijd en planning</h2>
<p>De vier leerblokken kosten samen ongeveer 4½ uur:</p>
<ul>
<li>Leerblok 1: ± 30 min</li>
<li>Leerblok 2: ± 45 min, plus hoogstens 15 min terugblik</li>
<li>Leerblok 3: ± 105 min, plus hoogstens 15 min terugblik</li>
<li>Leerblok 4: ± 45 min, plus hoogstens 15 min terugblik</li>
</ul>
<p>Werk je zelfstandig? Zet elk leerblok als een afspraak in je agenda. Leerblok 3 kun je over twee keer verdelen: de site onthoudt bij welke taak je was. Bij elk leerblok staat wanneer het in het programma aan de beurt is; heb het dan af. Begin op tijd, zodat er tussen twee leerblokken een paar dagen zit. Het volgende leerblok begint met een terugblik: je schrijft uit je hoofd op wat je nog weet. Zo onthoud je het beter.</p>
```

- [ ] **Step 4: docentgids.** In `docs/docentgids.html`: „Vier leerblokken van 45 minuten: 1 De A3 en je vraag, 2 Zoeken, beoordelen en gebruiken, 3 Het vraagstuk plaatsen, 4 Verbinden en reflecteren.” → „Vier leerblokken: 1 De A3 en je vraag (30 min), 2 Zoeken, beoordelen en gebruiken (45 min), 3 Het vraagstuk plaatsen (105 min), 4 Verbinden en reflecteren (45 min).”

- [ ] **Step 5: groen en 1 A4.** `node --test 2>&1 | tail -4`. Daarna de afdruk: `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf=<workspace>/intro.pdf "file://$PWD/docs/studentintroductie.html"` en `mdls -name kMDItemNumberOfPages <workspace>/intro.pdf` (of `python3 -c` met een telling van `/Type /Page`). Verwacht: 1 pagina. Meer dan 1: kort de tekst in overleg in (taak 5b is dan niet af) en noteer een Ruling.

- [ ] **Step 6: commit.** `git add docs/studentintroductie.html docs/docentgids.html tests/docs.test.mjs`; bericht: `B113, B118, DL-2: studentintroductie krijgt Tijd en planning (tijd per leerblok uit de data, planningsadvies voor zelfstudie); docentgids noemt de vier richttijden`.

### Aanpassing van Task 6

In de aanvulling in het BUILDPLAN komen ook: „- [x] Richttijd per leerblok volgt de taken (B118): data, content-check, terugblik, tests.” en „- [x] Studentintroductie: Tijd en planning, 1 A4 (DL-2).” Voeg achter punt (5) van de Afwijkingen bij fase 10 (de zin „De werkboektijden van de zes taken tellen op tot 105 min terwijl het leerblok 45 min heet (ADR B68, kalibreren in fase 15).”) toe: „Opgelost met B118 (1-10-2026): de richttijd van leerblok 3 is nu 105 min; de pilot ijkt hem.”
