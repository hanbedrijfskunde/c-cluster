# Metrokaart van het leerblok — uitvoeringsplan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bovenaan elke studentpagina van de e-learning A3 staat een metrokaart van het leerblok: één lijn in de kleur van dat leerblok, een halte per taak, „hier” op de plek van de student, splitsingen die weer samenkomen, en overstappunten aan begin en eind.

**Architecture:** Drie nieuwe modules volgens het bestaande patroon (logica zonder DOM apart van de tekening): `js/metro-model.js` bepaalt kolommen en haltes met stand, naam en link uit de leerblokdata en de opslag; `js/metro-indeling.js` rekent daar pixels van; `js/metro.js` tekent een inline SVG en plaatst hem onder de kop van zeven pagina's. Splitsingen staan als veld `spoor` in de leerblokdata. De segmentbalk in de taakkop vervalt.

**Tech Stack:** statische site, vanilla ES-modules, JSON-content, inline SVG, `node --test`, `tools/content-check.mjs`, `tools/contrast-check.mjs`, `tools/gewicht-check.mjs`. Geen build, geen DOM in de tests (de tests lezen pure functies en broncode); de tekening wordt in de browser gecontroleerd (taak 7).

**Spec:** `docs/superpowers/specs/2026-10-01-metrokaart-design.md` (repository c-cluster-1). Besluit: ADR B110. Regels: BLUEPRINT SX-4, SX-18, SX-19; DESIGN §6 Metrokaart.

**Werkmappen:** code in `/Users/witoldtenhove/Documents/HAN/a3-learning/.worktrees/metrokaart` (branch `metrokaart`); documentatie in `/Users/witoldtenhove/Documents/HAN/c-cluster-1/.worktrees/metrokaart` (branch `metrokaart`). Alle paden in de taken zijn relatief aan de a3-learning-worktree, tenzij anders vermeld. Gebruik geen `git stash` (andere sessies werken in dezelfde repositories). Commit alleen de bestanden van de taak.

## Global Constraints

- Lijnkleuren als tokens in `:root` van `css/site.css`: `--lijn-1:#E50056; --lijn-2:#0063B2; --lijn-3:#00804A; --lijn-4:#C2410C`; elk ≥ 3:1 tegen wit (berekend 4,70 / 6,13 / 5,02 / 5,18). Geen kleurcode buiten `:root` (`tests/toegankelijk.test.mjs`).
- De kaart staat op 7 studentpagina's (`index.html`, `leerblok-1.html` … `leerblok-4.html`, `dossier.html`, `bronnen.html`), niet op `docent.html`, `verificatie.html`, `controlelab.html`.
- 0 px horizontale scroll op 360 px; tikvlak per halte een strook van de volle kaarthoogte (≥ 44 px) en tot halverwege de buren, ≥ 24 × 24 px, zonder overlap.
- Eén `aria-current="step"` op de kaart; elke halte een toegankelijke naam met taak en stand; kleur nooit de enige drager.
- Geen harde schaduw op de kaart (SX-7); beweging alleen het vullen van een halte, 200 ms, niet bij `prefers-reduced-motion` (SX-9). Labels ≥ 13 px (SX-10).
- Onder 28 px kolombreedte alleen labels van „hier” en de overstappunten.
- Studentpagina's tonen geen EV-codes (SX-3): de naam van een halte noemt taak en stap, nooit `EV-`.
- PF-4: ≤ 300 kB gzip en ≤ 500 kB bron per pagina; leerblokpagina's tellen alleen hun eigen leerblokbestand.
- Tekst in de UI en in commentaar is Nederlands, in de toon van de bestaande code.
- Commits eindigen met `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## Review Focus

1. Een opgeslagen positie die naar een taak verwijst die niet (meer) bestaat (zoals na de omzetting van B102): geen crash, „hier” op het beginpunt. Test in taak 3.
2. Lege of geblokkeerde opslag (geheugenopslag zonder records): de kaart tekent alle haltes open, met „hier” op het adres. Test in taak 3.
3. Een onbekend anker op een leerblokpagina (`#media`, `#wissel`): „hier” op het beginpunt, zoals het overzicht. Test in taak 3.
4. Een onbekende waarde voor de mediaroute in de opslag (`podcast`): telt als tekst. Test in taak 3.
5. Een breed scherm (1024 px) en het smalste geval (leerblok 3 met taak 5.1 open, 12 kolommen op 328 px): tikvlakken ≥ 24 px en zonder overlap, geen halte buiten de kaart. Test in taak 4.

---

### Task 1: Splitsingen als veld `spoor` in de data, met contentcontrole

**Files:**
- Modify: `tools/content-check.mjs` (constante bij de andere constanten rond regel 74–77; controle in de takenlus direct na de regel die begint met `if (Array.isArray(taak.bc)`)
- Modify: `data/leerblok-2.json` (taak 3.2 en 4.2)
- Test: `tests/metro.test.mjs` (nieuw)

**Interfaces:**
- Produces: veld `taak.spoor = { stappen: ('waarom'|'stof'|'oefenen'|'toepassen')[], veld: string, takken: { waarde: string, kort: string }[] }` in `data/leerblok-N.json`; export `SPOOR_STAPPEN` uit `tools/content-check.mjs`.

- [ ] **Step 1: Write the failing test**

Maak `tests/metro.test.mjs`:

```js
// Metrokaart van het leerblok (SX-4, SX-18, SX-19; ADR B110; DESIGN §6 Metrokaart).
import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { controleerFormaat, SPOOR_STAPPEN } from '../tools/content-check.mjs';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const lees = (p) => readFileSync(resolve(root, p), 'utf8');
const ruw = (n) => JSON.parse(lees(`data/leerblok-${n}.json`));

test('SX-19: taak 3.2 splitst in route A en B (oefenen en toepassen), taak 4.2 in artikel 1 en 2 (oefenen)', () => {
  const lb2 = ruw(2);
  const t32 = lb2.taken.find((t) => t.id === '3.2');
  assert.deepEqual(t32.spoor, { stappen: ['oefenen', 'toepassen'], veld: 'route',
    takken: [{ waarde: 'A · databank', kort: 'A' }, { waarde: 'B · AI-tool', kort: 'B' }] });
  const t42 = lb2.taken.find((t) => t.id === '4.2');
  assert.deepEqual(t42.spoor, { stappen: ['oefenen'], veld: 'artikel',
    takken: [{ waarde: 'Artikel 1 · Visser & El Amrani', kort: 'Art. 1' }, { waarde: 'Artikel 2 · Bakker & De Vries', kort: 'Art. 2' }] });
  assert.deepEqual(SPOOR_STAPPEN, ['waarom', 'stof', 'oefenen', 'toepassen']);
  for (const n of [1, 2, 3, 4]) assert.deepEqual(controleerFormaat(ruw(n), `leerblok-${n}.json`).fouten, [], `leerblok ${n}`);
});

test('SX-19: content-check keurt een spoor met een onbekende stap, een onbekend veld of een tak buiten de opties af', () => {
  const zet = (spoor) => { const b = ruw(2); b.taken.find((t) => t.id === '3.2').spoor = spoor; return controleerFormaat(b, 'leerblok-2.json').fouten; };
  const goed = ruw(2).taken.find((t) => t.id === '3.2').spoor;
  assert.match(zet({ ...goed, stappen: ['oefenen', 'pauze'] }).join('\n'), /taak 3\.2: spoor\.stappen/);
  assert.match(zet({ ...goed, veld: 'bestaatniet' }).join('\n'), /taak 3\.2: spoor\.veld bestaatniet bestaat niet/);
  assert.match(zet({ ...goed, takken: [goed.takken[0], { waarde: 'C · bibliotheek', kort: 'C' }] }).join('\n'), /staat niet in de opties van route/);
  assert.match(zet({ ...goed, takken: [goed.takken[0]] }).join('\n'), /spoor heeft 2 of 3 takken/);
  assert.match(zet({ ...goed, takken: [goed.takken[0], { waarde: 'B · AI-tool', kort: 'B-route-lang' }] }).join('\n'), /kort label van hoogstens 6 tekens/);
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `node --test tests/metro.test.mjs`
Expected: FAIL; `SPOOR_STAPPEN` is geen export (SyntaxError „does not provide an export named 'SPOOR_STAPPEN'”).

- [ ] **Step 3: Write minimal implementation**

In `tools/content-check.mjs`, onder de regel `export const VELDTYPEN = …`:

```js
/** De stappen waarin een taak kan splitsen op de metrokaart (SX-19, ADR B110). */
export const SPOOR_STAPPEN = Object.freeze(['waarom', 'stof', 'oefenen', 'toepassen']);
```

In de takenlus van `controleerFormaat`, direct na de regel die begint met `if (Array.isArray(taak.bc)`:

```js
    // SX-19 (ADR B110): een splitsing op de metrokaart. De takken zijn opties van een keuzeveld van de oefening of toepassing.
    if (taak.spoor !== undefined) {
      const sp = taak.spoor;
      const velden = [...(taak.oefening?.velden ?? []), ...(taak.toepassing?.velden ?? [])].filter((v) => v?.id === sp?.veld);
      const opties = new Set(velden.flatMap((v) => v.opties ?? []));
      if (!Array.isArray(sp?.stappen) || sp.stappen.length === 0 || !sp.stappen.every((s) => SPOOR_STAPPEN.includes(s))) {
        fout(wie, `spoor.stappen moet een lijst uit ${SPOOR_STAPPEN.join(', ')} zijn (SX-19)`);
      }
      if (velden.length === 0) fout(wie, `spoor.veld ${sp?.veld} bestaat niet in oefening of toepassing (SX-19)`);
      if (!Array.isArray(sp?.takken) || sp.takken.length < 2 || sp.takken.length > 3) fout(wie, 'spoor heeft 2 of 3 takken (SX-19)');
      else {
        for (const t of sp.takken) {
          if (velden.length > 0 && !opties.has(t?.waarde)) fout(wie, `spoor-tak ${JSON.stringify(t?.waarde)} staat niet in de opties van ${sp.veld} (SX-19)`);
          if (!gevuld(t?.kort) || t.kort.length > 6) fout(wie, 'spoor-tak mist een kort label van hoogstens 6 tekens (SX-19)');
        }
      }
    }
```

Voeg het veld toe aan de data (het bestand houdt zijn opmaak: `JSON.stringify(…, null, 2)` plus een regeleinde geeft exact het huidige bestand):

```bash
node -e '
const fs = require("fs"); const p = "data/leerblok-2.json"; const d = JSON.parse(fs.readFileSync(p, "utf8"));
const zet = (id, spoor) => { const t = d.taken.find((x) => x.id === id); const n = {}; for (const [k, v] of Object.entries(t)) { n[k] = v; if (k === "bewijsonderdeel") n.spoor = spoor; } Object.keys(t).forEach((k) => delete t[k]); Object.assign(t, n); };
zet("3.2", { stappen: ["oefenen", "toepassen"], veld: "route", takken: [{ waarde: "A · databank", kort: "A" }, { waarde: "B · AI-tool", kort: "B" }] });
zet("4.2", { stappen: ["oefenen"], veld: "artikel", takken: [{ waarde: "Artikel 1 · Visser & El Amrani", kort: "Art. 1" }, { waarde: "Artikel 2 · Bakker & De Vries", kort: "Art. 2" }] });
fs.writeFileSync(p, JSON.stringify(d, null, 2) + "\n");'
git diff --stat data/leerblok-2.json
```

Expected: `data/leerblok-2.json | 30 ++++` (alleen toevoegingen, geen andere regels gewijzigd).

- [ ] **Step 4: Run test to verify it passes**

Run: `node --test tests/metro.test.mjs && node tools/content-check.mjs`
Expected: 2 tests PASS; content-check eindigt met 0 fouten (waarschuwingen over `concept-auteur` mogen blijven).

- [ ] **Step 5: Commit**

```bash
git add tools/content-check.mjs data/leerblok-2.json tests/metro.test.mjs
git commit -m "B110, SX-19: splitsingen als veld spoor in de leerblokdata (3.2 route A/B, 4.2 artikel 1/2), met contentcontrole

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 2: Vier lijnkleuren als tokens, met contrastcontrole voor lijnen

**Files:**
- Modify: `css/site.css` (in `:root`, na de regel met `--grijs-tekst`)
- Modify: `tools/contrast-check.mjs` (constanten bovenaan; `controleerContrast`)
- Test: `tests/metro.test.mjs`

**Interfaces:**
- Produces: CSS-tokens `--lijn-1` … `--lijn-4`; exports `MINIMUM_GRAFISCH` (3) en `LIJNEN` uit `tools/contrast-check.mjs`.

- [ ] **Step 1: Write the failing test**

Voeg toe aan `tests/metro.test.mjs` (import bovenaan erbij):

```js
import { controleerContrast, tokensUit, contrast, LIJNEN, MINIMUM_GRAFISCH } from '../tools/contrast-check.mjs';

test('SX-18: vier lijnkleuren als token, elk minstens 3:1 tegen wit (WCAG 1.4.11), en in de contrastcontrole', () => {
  const tokens = tokensUit(lees('css/site.css'));
  assert.deepEqual(LIJNEN, ['--lijn-1', '--lijn-2', '--lijn-3', '--lijn-4']);
  assert.equal(MINIMUM_GRAFISCH, 3);
  assert.deepEqual(LIJNEN.map((t) => tokens[t]?.toUpperCase()), ['#E50056', '#0063B2', '#00804A', '#C2410C']);
  for (const t of LIJNEN) assert.ok(contrast(tokens[t], tokens['--wit']) >= 3, t);
  const { paren, fouten } = controleerContrast(root);
  assert.equal(paren.filter((p) => p.minimum === 3).length, 4, 'vier lijnparen met hun eigen minimum');
  assert.deepEqual(fouten, []);
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `node --test tests/metro.test.mjs`
Expected: FAIL; `LIJNEN` is geen export.

- [ ] **Step 3: Write minimal implementation**

`css/site.css`, in `:root` na de regel met `--grijs-tekst`:

```css
  --lijn-1:#E50056; --lijn-2:#0063B2; --lijn-3:#00804A; --lijn-4:#C2410C; /* metrolijn per leerblok, ≥ 3:1 op wit (SX-18, ADR B110) */
```

`tools/contrast-check.mjs`, onder `export const EXTRA_PAREN = …`:

```js
/** Lijnen en haltes van de metrokaart zijn grafische elementen: minstens 3:1 tegen wit (WCAG 1.4.11; SX-18, ADR B110). */
export const MINIMUM_GRAFISCH = 3;
export const LIJNEN = Object.freeze(['--lijn-1', '--lijn-2', '--lijn-3', '--lijn-4']);
```

In `controleerContrast`, direct na de regel `for (const [selector, fg, bg] of EXTRA_PAREN) …`:

```js
  for (const t of LIJNEN) {
    lijst.push(tokens[t] ? { selector: `metrokaart ${t} op wit`, fg: tokens[t], bg: tokens['--wit'], minimum: MINIMUM_GRAFISCH }
      : { selector: `metrokaart ${t}`, fout: 'token ontbreekt in :root' });
  }
```

en vervang in dezelfde functie de regel met `if (p.ratio < MINIMUM)` door:

```js
    const minimum = p.minimum ?? MINIMUM;
    if (p.ratio < minimum) fouten.push(`${p.selector}: ${p.fg} op ${p.bg} = ${p.ratio.toFixed(2)}:1 (minimaal ${minimum}:1)`);
```

- [ ] **Step 4: Run test to verify it passes**

Run: `node --test tests/metro.test.mjs tests/toegankelijk.test.mjs tests/contrast.test.mjs && node tools/contrast-check.mjs`
Expected: alles PASS; contrast-check meldt 0 onder het minimum.

- [ ] **Step 5: Commit**

```bash
git add css/site.css tools/contrast-check.mjs tests/metro.test.mjs
git commit -m "B110, SX-18: vier lijnkleuren als token, contrastcontrole 3:1 voor lijnen

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 3: Het model van de kaart (`js/metro-model.js`)

**Files:**
- Create: `js/metro-model.js`
- Test: `tests/metro.test.mjs`

**Interfaces:**
- Consumes: `stapStand`, `STAP_NAMEN`, `segmentLabel` (`js/voortgang.js`); `STAP_SLUGS`, `maakAdres` (`js/taakweergave.js`); `isIngevuld`, `oefenModel` (`js/weergave.js`); `isAfgerond`, `leesRecords` (`js/afgerond.js`); veld `taak.spoor` (taak 1).
- Produces:
  - `laatsteLeerblok(store) → { leerblok: 1|2|3|4, taak: string|null, stap: number|null }`
  - `taakStand(store, taak) → { stand: ReturnType<stapStand>, toepassing: object, oefening: object }`
  - `gekozenTak(spoor, toepassing, oefening) → string|null`
  - `metroModel({ blok, store, adres }) → { leerblok: number, kolommen: Kolom[], label: string, tekst: string }`, met `adres` = `{ soort: 'overzicht'|'afsluiten'|'taak'|'elders', taak?: string|null, stap?: number|null }`.
  - `Kolom = { soort: 'begin'|'eind'|'taak'|'stap'|'verdieping', label: string, spoor: string|null, overstap?: number|null, taak?: string, haltes: Halte[] }`
  - `Halte = { id: string, rij: -1|0|1, href?: string, stand?: 'af'|'hier'|'open', gestippeld?: boolean, naam?: string, label?: string, doorgang?: true }` (een `doorgang` is geen halte maar het doorgaande spoor naast de verdieping; zonder href en naam).
  - constanten `STAP_KORT`, `MEDIA_TAKKEN`, `RIJEN`.

- [ ] **Step 1: Write the failing test**

Voeg toe aan `tests/metro.test.mjs`:

```js
import { normaliseerBlok } from '../js/blok.js';
import { leesAdres } from '../js/taakweergave.js';
import { metroModel, laatsteLeerblok, gekozenTak, MEDIA_TAKKEN } from '../js/metro-model.js';

const blok = (n) => normaliseerBlok(ruw(n));
/** Opslag zonder browser: meta-sleutels en records (nieuwste per id). */
const nepStore = (meta = {}, records = {}) => ({ getMeta: (k) => meta[k], get: (id) => records[id] });
const alleHaltes = (m) => m.kolommen.flatMap((k) => k.haltes).filter((h) => !h.doorgang);
const hier = (m) => { const h = alleHaltes(m).filter((x) => x.stand === 'hier'); assert.equal(h.length, 1, 'precies één „hier”'); return h[0]; };
const kolom = (m, taak, soort) => m.kolommen.find((k) => k.taak === taak && (!soort || k.soort === soort));

test('SX-18: overzicht van leerblok 2: begin, vijf taken, de verdieping na 4.1 en het eind; „hier” op „Vorige keer”', () => {
  const m = metroModel({ blok: blok(2), store: nepStore(), adres: { soort: 'overzicht' } });
  assert.deepEqual(m.kolommen.map((k) => k.soort === 'taak' ? k.taak : k.soort),
    ['begin', '3.1', '3.2', '4.1', 'verdieping', '4.2', '4.3', 'eind']);
  assert.equal(hier(m).id, 'begin');
  assert.equal(m.kolommen[0].label, 'Vorige keer');
  assert.equal(m.kolommen[0].overstap, 1);
  assert.equal(m.kolommen.at(-1).overstap, 3);
  assert.equal(m.kolommen[0].haltes[0].href, 'leerblok-2.html#overzicht');
  assert.equal(m.kolommen.at(-1).haltes[0].href, 'leerblok-2.html#afsluiten');
  assert.equal(m.tekst, 'Leerblok 2 · Zoeken, beoordelen en gebruiken');
  for (const h of alleHaltes(m)) {
    assert.ok(h.naam && h.href, `${h.id} heeft naam en link`);
    assert.doesNotMatch(h.naam, /EV-\d/, 'SX-3: geen interne codes');
  }
});

test('SX-18: leerblok 1 begint bij „Start” zonder stompje; leerblok 4 eindigt bij „Dossier” zonder stompje', () => {
  const m1 = metroModel({ blok: blok(1), store: nepStore(), adres: { soort: 'overzicht' } });
  assert.equal(m1.kolommen[0].label, 'Start');
  assert.equal(m1.kolommen[0].overstap, null);
  assert.equal(m1.kolommen[0].haltes[0].href, 'index.html');
  const m4 = metroModel({ blok: blok(4), store: nepStore(), adres: { soort: 'afsluiten' } });
  assert.equal(m4.kolommen.at(-1).label, 'Dossier');
  assert.equal(m4.kolommen.at(-1).overstap, null);
  assert.equal(m4.kolommen.at(-1).haltes[0].href, 'dossier.html');
  assert.equal(hier(m4).id, 'eind');
  assert.deepEqual(m4.kolommen.slice(-2).map((k) => k.soort), ['verdieping', 'eind'], 'verdieping na 6.3, de laatste taak');
});

test('SX-4, SX-18: de huidige taak klapt open in vier stap-haltes; „hier” op de stap van het adres', () => {
  const m = metroModel({ blok: blok(2), store: nepStore(), adres: { soort: 'taak', taak: '3.1', stap: 2 } });
  const stappen = m.kolommen.filter((k) => k.soort === 'stap');
  assert.deepEqual(stappen.map((k) => k.label), ['W', 'S', 'O', 'T']);
  assert.ok(stappen.every((k) => k.taak === '3.1'));
  assert.equal(hier(m).id, '3.1-stof');
  assert.equal(stappen[2].haltes[0].href, 'leerblok-2.html#taak-3.1/oefenen');
  assert.equal(m.label, 'Taak 1 van 5, stap 1 van 4');
  assert.equal(m.tekst, 'Leerblok 2 · taak 1 van 5 · stap 2 van 4');
  const zonderStap = metroModel({ blok: blok(2), store: nepStore(), adres: { soort: 'taak', taak: '3.1', stap: null } });
  assert.equal(hier(zonderStap).id, '3.1-waarom', 'zonder stap in het adres: de stap waar de student is');
});

test('SX-19: route A/B in 3.2; zonder keuze beide vol; een keuze in de oefening maakt de andere tak gestippeld; de toepassing gaat voor', () => {
  const b = blok(2);
  let m = metroModel({ blok: b, store: nepStore(), adres: { soort: 'taak', taak: '3.2', stap: 3 } });
  const o = m.kolommen.find((k) => k.taak === '3.2' && k.label === 'O');
  assert.deepEqual(o.haltes.map((h) => [h.label, h.rij, h.gestippeld]), [['A', -1, false], ['B', 1, false]]);
  assert.equal(hier(m).id, '3.2-oefenen-A', 'zonder keuze de ring op de eerste tak');
  assert.equal(o.spoor, m.kolommen.find((k) => k.taak === '3.2' && k.label === 'T').spoor, 'oefenen en toepassen op dezelfde takken');
  m = metroModel({ blok: b, store: nepStore({ 'oefening:3.2': { invoer: { route: 'B · AI-tool' } } }), adres: { soort: 'overzicht' } });
  assert.deepEqual(kolom(m, '3.2').haltes.map((h) => [h.label, h.gestippeld]), [['A', true], ['B', false]]);
  const beide = nepStore({ 'oefening:3.2': { invoer: { route: 'B · AI-tool' } } }, { 'EV-03': { inhoud: { route: 'A · databank' } } });
  assert.equal(gekozenTak(b.taken.find((t) => t.id === '3.2').spoor, { route: 'A · databank' }, { route: 'B · AI-tool' }), 'A · databank');
  m = metroModel({ blok: b, store: beide, adres: { soort: 'overzicht' } });
  assert.deepEqual(kolom(m, '3.2').haltes.map((h) => h.gestippeld), [false, true]);
});

test('SX-19: 4.2 met artikel 2 in de oefening; tekst/video/spel alleen bij de opengeklapte mediataak', () => {
  const b = blok(2);
  let m = metroModel({ blok: b, store: nepStore({ 'oefening:4.2': { invoer: { artikel: 'Artikel 2 · Bakker & De Vries' } } }), adres: { soort: 'overzicht' } });
  assert.deepEqual(kolom(m, '4.2').haltes.map((h) => [h.label, h.gestippeld]), [['Art. 1', true], ['Art. 2', false]]);
  assert.equal(kolom(m, '4.1').haltes.length, 1, 'ingeklapt is de mediataak een gewone halte');
  m = metroModel({ blok: b, store: nepStore({ 'media:route:2': 'video' }), adres: { soort: 'taak', taak: '4.1', stap: 2 } });
  const stof = m.kolommen.find((k) => k.taak === '4.1' && k.label === 'S');
  assert.deepEqual(stof.haltes.map((h) => [h.label, h.rij, h.gestippeld]), [['T', -1, true], ['V', 0, false], ['S', 1, true]]);
  assert.equal(hier(m).id, '4.1-stof-V');
  m = metroModel({ blok: b, store: nepStore({ 'media:route:2': 'podcast' }), adres: { soort: 'taak', taak: '4.1', stap: 2 } });
  assert.equal(hier(m).id, '4.1-stof-T', 'een onbekende route telt als tekst (MD-2)');
  assert.deepEqual(MEDIA_TAKKEN.map((t) => t.waarde), ['tekst', 'video', 'spel']);
  assert.match(lees('js/media.js'), /`media:route:\$\{leerblok\}`/, 'dezelfde opslagsleutel als media.js');
});

test('SX-18: standen: klaar maakt een taak af en het begin geweest; verdieping gedaan is vol; alle bewijs telt maakt het eind af', () => {
  const b = blok(2);
  const meta = { 'klaar:3.1': { op: '2026-10-01T09:00:00Z' }, 'verdieping:2': { gedaan: true } };
  let m = metroModel({ blok: b, store: nepStore(meta), adres: { soort: 'taak', taak: '3.2', stap: 1 } });
  assert.equal(kolom(m, '3.1').haltes[0].stand, 'af');
  assert.equal(m.kolommen[0].haltes[0].stand, 'af');
  const v = m.kolommen.find((k) => k.soort === 'verdieping');
  assert.deepEqual(v.haltes.map((h) => h.doorgang ? 'doorgang' : [h.stand, h.gestippeld]), ['doorgang', ['af', false]]);
  assert.equal(v.haltes[1].href, 'leerblok-2.html#taak-4.1/toepassen');
  assert.equal(m.kolommen.at(-1).haltes[0].stand, 'open');
  const records = Object.fromEntries(['EV-03', 'EV-04', 'EV-12', 'EV-05'].map((id) => [id, { status: 'compleet' }]));
  m = metroModel({ blok: b, store: nepStore(meta, records), adres: { soort: 'taak', taak: '3.2', stap: 1 } });
  assert.equal(m.kolommen.at(-1).haltes[0].stand, 'af');
});

test('SX-18: buiten het leerblok de jongste positie, ingeklapt; zonder positie leerblok 1 met „hier” op het begin', () => {
  assert.deepEqual(laatsteLeerblok(nepStore()), { leerblok: 1, taak: null, stap: null });
  const store = nepStore({
    'positie:2': { taak: '3.2', stap: 3, bijgewerkt: '2026-10-01T10:00:00.000Z' },
    'positie:3': { taak: '6.1', stap: 2, bijgewerkt: '2026-10-01T11:00:00.000Z' },
    'positie:4': null,
  });
  const laatste = laatsteLeerblok(store);
  assert.deepEqual(laatste, { leerblok: 3, taak: '6.1', stap: 2 });
  let m = metroModel({ blok: blok(3), store, adres: { soort: 'elders', ...laatste } });
  assert.equal(m.kolommen.filter((k) => k.soort === 'stap').length, 0, 'buiten het leerblok klapt niets open');
  assert.equal(hier(m).id, '6.1');
  assert.equal(m.tekst, 'Leerblok 3 · laatst bij taak 6.1');
  m = metroModel({ blok: blok(3), store, adres: { soort: 'elders', taak: '4.2', stap: 1 } });
  assert.equal(hier(m).id, 'begin', 'een positie bij een taak die niet bestaat: „hier” op het begin');
});

test('SX-18: lege opslag en onbekende ankers: alles open, „hier” op het begin', () => {
  const b = blok(3);
  const adres = leesAdres('#wissel', b.taken.map((t) => t.id));
  const m = metroModel({ blok: b, store: nepStore(), adres });
  assert.equal(hier(m).id, 'begin');
  assert.ok(alleHaltes(m).every((h) => h.stand !== 'af'));
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `node --test tests/metro.test.mjs`
Expected: FAIL met „Cannot find module …/js/metro-model.js”.

- [ ] **Step 3: Write minimal implementation**

Maak `js/metro-model.js`:

```js
// Metrokaart van het leerblok (SX-18, SX-19; ADR B110; DESIGN §6 Metrokaart): welke kolommen en haltes de kaart heeft,
// met stand, label, toegankelijke naam en link. Puur: geen DOM, geen maten (die staan in metro-indeling.js).
import { stapStand, STAP_NAMEN, segmentLabel } from './voortgang.js';
import { STAP_SLUGS, maakAdres } from './taakweergave.js';
import { isIngevuld, oefenModel } from './weergave.js';
import { isAfgerond, leesRecords } from './afgerond.js';

/** Korte labels van de vier stap-haltes (TK-18). */
export const STAP_KORT = Object.freeze(['W', 'S', 'O', 'T']);
/** De drie routes in de stap stof van de mediataak (MD-2). */
export const MEDIA_TAKKEN = Object.freeze([
  { waarde: 'tekst', kort: 'T', naam: 'Tekst' },
  { waarde: 'video', kort: 'V', naam: 'Video' },
  { waarde: 'spel', kort: 'S', naam: 'Spel' },
]);
/** Rijen van de takken in één kolom: boven (-1), op (0) en onder (1) de hoofdlijn. */
export const RIJEN = Object.freeze({ 1: [0], 2: [-1, 1], 3: [-1, 0, 1] });
// Dezelfde sleutel als routeSleutel in js/media.js. media.js zelf laadt hier niet: te zwaar voor elke pagina (PF-4).
const mediaSleutel = (n) => `media:route:${n}`;
const STAND_TEKST = Object.freeze({ af: 'afgerond', hier: 'je bent hier', open: 'open' });
const stand3 = (af, hier) => (hier ? 'hier' : af ? 'af' : 'open');

/** Het leerblok waar de student het laatst werkte: de jongste `positie:N`; zonder positie leerblok 1 (SX-18). */
export function laatsteLeerblok(store) {
  let laatste = null;
  for (const n of [1, 2, 3, 4]) {
    const p = store.getMeta(`positie:${n}`);
    if (p?.bijgewerkt && (!laatste || p.bijgewerkt > laatste.bijgewerkt)) laatste = { leerblok: n, taak: p.taak ?? null, stap: p.stap ?? null, bijgewerkt: p.bijgewerkt };
  }
  return laatste ? { leerblok: laatste.leerblok, taak: laatste.taak, stap: laatste.stap } : { leerblok: 1, taak: null, stap: null };
}

/** Stand van één taak uit de opslag, zoals de taakkop hem berekent (js/leerblok.js, tekenVoortgang). */
export function taakStand(store, taak) {
  const toepassing = (taak.bewijsonderdeel ? store.get(taak.bewijsonderdeel)?.inhoud : store.getMeta(`invoer:${taak.id}`)) ?? {};
  const oefening = oefenModel(taak, store.getMeta(`oefening:${taak.id}`) ?? {});
  const stand = stapStand({
    gestart: isIngevuld(toepassing) || isIngevuld(oefening.invoer),
    geoefend: isIngevuld(oefening.invoer) || oefening.overgeslagen,
    oefeningAf: oefening.modelZichtbaar || oefening.overgeslagen,
    klaar: Boolean(store.getMeta(`klaar:${taak.id}`)?.op),
  });
  return { stand, toepassing, oefening: oefening.invoer };
}

/** De gekozen tak van een splitsing: eerst de toepassing, dan de oefening; een onbekende waarde telt als geen keuze. */
export function gekozenTak(spoor, toepassing = {}, oefening = {}) {
  for (const w of [toepassing[spoor.veld], oefening[spoor.veld]]) if (spoor.takken.some((t) => t.waarde === w)) return w;
  return null;
}

/** Eén halte op de hoofdlijn. */
function enkel({ id, naam, href, af, hier }) {
  const stand = stand3(af, hier);
  return { id, rij: 0, href, stand, gestippeld: false, naam: `${naam}, ${STAND_TEKST[stand]}` };
}

/** Haltes van een kolom met takken. De ring „hier” staat op de gekozen tak, zonder keuze op de eerste. */
function takHaltes(takken, keuze, { id, naam, href, af, hier }) {
  const ring = hier ? (takken.find((t) => t.waarde === keuze) ?? takken[0]).waarde : null;
  return takken.map((t, i) => {
    const stand = stand3(af, t.waarde === ring);
    return {
      id: `${id}-${t.kort}`, rij: RIJEN[takken.length][i], label: t.kort, href, stand,
      gestippeld: keuze !== null && t.waarde !== keuze,
      naam: `${naam}, ${t.naam ?? t.waarde}${t.waarde === keuze ? ' (gekozen)' : ''}, ${STAND_TEKST[stand]}`,
    };
  });
}

/**
 * Het model van de kaart voor één leerblok.
 * @param {object} p
 * @param {object} p.blok genormaliseerde leerblokdata (normaliseerBlok)
 * @param {{getMeta: Function, get: Function}} p.store
 * @param {{soort: 'overzicht'|'afsluiten'|'taak'|'elders', taak?: string|null, stap?: number|null}} p.adres
 *   `elders`: start, dossier of bronnen, met de laatste positie (laatsteLeerblok)
 */
export function metroModel({ blok, store, adres }) {
  const n = blok.leerblok;
  const pagina = `leerblok-${n}.html`;
  const ids = blok.taken.map((t) => t.id);
  const standen = new Map(blok.taken.map((t) => [t.id, taakStand(store, t)]));
  const gestart = [...standen.values()].some((s) => s.stand.stappen[0].stand === 'voltooid');
  const ev = (blok.bewijsonderdelen ?? []).map((e) => e.id);
  const afgerond = isAfgerond(ev, leesRecords(store, ev)).afgerond;
  const bewaard = store.getMeta(mediaSleutel(n));
  const route = MEDIA_TAKKEN.some((t) => t.waarde === bewaard) ? bewaard : 'tekst';
  const verdiepingGedaan = store.getMeta(`verdieping:${n}`)?.gedaan === true;
  const open = adres.soort === 'taak' && ids.includes(adres.taak) ? adres.taak : null;
  const elders = adres.soort === 'elders' && ids.includes(adres.taak) ? adres.taak : null;
  const kolommen = [];

  const beginHier = adres.soort === 'overzicht' || (adres.soort === 'elders' && !elders) || (adres.soort === 'taak' && !open);
  kolommen.push({ soort: 'begin', label: n === 1 ? 'Start' : 'Vorige keer', spoor: null, overstap: n > 1 ? n - 1 : null, haltes: [{
    id: 'begin', rij: 0, href: n === 1 ? 'index.html' : `${pagina}#overzicht`, stand: stand3(gestart, beginHier), gestippeld: false,
    naam: `${n === 1 ? 'Start' : `Vorige keer, overstap van leerblok ${n - 1}`}, ${beginHier ? STAND_TEKST.hier : gestart ? 'geweest' : 'open'}`,
  }] });

  for (const t of blok.taken) {
    const { stand, toepassing, oefening } = standen.get(t.id);
    const keuze = t.spoor ? gekozenTak(t.spoor, toepassing, oefening) : null;
    if (t.id === open) {
      const hierStap = adres.stap ?? stand.actief + 1;
      STAP_SLUGS.forEach((slug, j) => {
        const opSpoor = Boolean(t.spoor?.stappen.includes(slug));
        const media = !opSpoor && slug === 'stof' && blok.media?.taak === t.id;
        const takken = opSpoor ? t.spoor.takken : media ? MEDIA_TAKKEN : null;
        const kern = {
          id: `${t.id}-${slug}`, naam: `Taak ${t.id}, stap ${j + 1} van 4: ${STAP_NAMEN[j]}`,
          href: `${pagina}${maakAdres(t.id, j + 1)}`, af: stand.stappen[j].stand === 'voltooid', hier: j + 1 === hierStap,
        };
        kolommen.push({ soort: 'stap', taak: t.id, label: STAP_KORT[j], spoor: opSpoor ? `${t.id}:spoor` : media ? `${t.id}:media` : null,
          haltes: takken ? takHaltes(takken, media ? route : keuze, kern) : [enkel(kern)] });
      });
    } else {
      const kern = { id: t.id, naam: `Taak ${t.id}: ${t.titel}`, href: `${pagina}#taak-${t.id}`, af: stand.klaar, hier: t.id === elders };
      kolommen.push({ soort: 'taak', taak: t.id, label: t.id, spoor: t.spoor ? `${t.id}:spoor` : null,
        haltes: t.spoor ? takHaltes(t.spoor.takken, keuze, kern) : [enkel(kern)] });
    }
    // De verdieping is een zijtak, geen halte op de hoofdlijn (TK-13, TK-14): het doorgaande spoor loopt ernaast.
    if (blok.verdieping?.na === t.id) {
      kolommen.push({ soort: 'verdieping', label: '', spoor: null, haltes: [
        { id: 'doorgang', rij: 0, doorgang: true, gestippeld: false },
        { id: 'verdieping', rij: 1, label: '+', href: `${pagina}${maakAdres(t.id, 4)}`, stand: verdiepingGedaan ? 'af' : 'open',
          gestippeld: !verdiepingGedaan, naam: `Verdieping na taak ${t.id}, optioneel, ${verdiepingGedaan ? 'gedaan' : 'open'}` }] });
    }
  }

  const eindHier = adres.soort === 'afsluiten';
  kolommen.push({ soort: 'eind', label: n < 4 ? 'Afsluiten' : 'Dossier', spoor: null, overstap: n < 4 ? n + 1 : null, haltes: [{
    id: 'eind', rij: 0, href: n < 4 ? `${pagina}#afsluiten` : 'dossier.html', stand: stand3(afgerond, eindHier), gestippeld: false,
    naam: `${n < 4 ? `Afsluiten, overstap naar leerblok ${n + 1}` : 'Dossier, einde van de e-learning'}, ${eindHier ? STAND_TEKST.hier : afgerond ? 'leerblok afgerond' : 'open'}`,
  }] });

  const taakNr = open ? ids.indexOf(open) + 1 : null;
  const label = open ? segmentLabel(taakNr, ids.length, standen.get(open).stand) : `Leerblok ${n}: ${blok.titel}`;
  const tekst = open ? `Leerblok ${n} · taak ${taakNr} van ${ids.length} · stap ${adres.stap ?? standen.get(open).stand.actief + 1} van 4`
    : eindHier ? `Leerblok ${n} · afsluiten`
      : elders ? `Leerblok ${n} · laatst bij taak ${elders}`
        : `Leerblok ${n} · ${blok.titel}`;
  return { leerblok: n, kolommen, label, tekst };
}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `node --test tests/metro.test.mjs`
Expected: alle tests PASS (10).

- [ ] **Step 5: Commit**

```bash
git add js/metro-model.js tests/metro.test.mjs
git commit -m "B110, SX-18, SX-19: model van de metrokaart (haltes, takken, overstappunten, stand en links)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 4: De indeling in pixels (`js/metro-indeling.js`)

**Files:**
- Create: `js/metro-indeling.js`
- Test: `tests/metro.test.mjs`

**Interfaces:**
- Consumes: `metroModel` (taak 3).
- Produces: `metroIndeling(model, breedte) → { breedte, hoogte, kol, smal, haltes, labels, sporen }` met
  - `haltes[]`: de haltes van het model plus `{ kolom, soort, x, y, r, tik: { x, y, b, h } }` (geen doorgang)
  - `labels[]`: `{ tekst, x, y, anker: 'start'|'middle'|'end', soort: 'overstap'|'hier'|'kolom'|'tak' }`
  - `sporen[]`: `{ x1, y1, x2, y2, gestippeld, lijn }` (`lijn` = leerbloknummer van de kleur)
  - constanten `HOOGTE`, `Y_LIJN`, `RIJ`, `SMAL`, `TAK_LABEL`, `STRAAL`.

- [ ] **Step 1: Write the failing test**

Voeg toe aan `tests/metro.test.mjs`:

```js
import { metroIndeling, HOOGTE, Y_LIJN, RIJ } from '../js/metro-indeling.js';

/** Alle adressen van een leerblok: overzicht, afsluiten, elke taak met elke stap, en elders. */
const adressen = (b) => [{ soort: 'overzicht' }, { soort: 'afsluiten' }, { soort: 'elders', taak: b.taken[0].id, stap: 1 },
  ...b.taken.flatMap((t) => [1, 2, 3, 4].map((stap) => ({ soort: 'taak', taak: t.id, stap })))];
const keuzes = nepStore({ 'media:route:1': 'video', 'media:route:2': 'spel', 'oefening:3.2': { invoer: { route: 'B · AI-tool' } } });

test('SX-18: op 328, 600 en 1024 px elke halte binnen de kaart, tikvlakken ≥ 24 × 24 px en zonder overlap', () => {
  for (const n of [1, 2, 3, 4]) {
    const b = blok(n);
    for (const store of [nepStore(), keuzes]) {
      for (const adres of adressen(b)) {
        for (const breedte of [328, 600, 1024]) {
          const ind = metroIndeling(metroModel({ blok: b, store, adres }), breedte);
          const wie = `leerblok ${n} ${JSON.stringify(adres)} ${breedte}px`;
          assert.ok(HOOGTE >= 44, 'de kaart is minstens 44 px hoog');
          for (const h of ind.haltes) {
            assert.ok(h.x - h.r >= 0 && h.x + h.r <= breedte, `${wie}: ${h.id} binnen de breedte`);
            assert.ok(h.tik.b >= 24 && h.tik.h >= 24, `${wie}: tikvlak van ${h.id} is ${h.tik.b.toFixed(1)} × ${h.tik.h.toFixed(1)}`);
            assert.ok(h.tik.x >= 0 && h.tik.x + h.tik.b <= breedte + 1e-6 && h.tik.y >= 0 && h.tik.y + h.tik.h <= HOOGTE + 1e-6, `${wie}: tikvlak ${h.id} binnen de kaart`);
          }
          for (let i = 0; i < ind.haltes.length; i += 1) {
            for (let j = i + 1; j < ind.haltes.length; j += 1) {
              const a = ind.haltes[i].tik; const c = ind.haltes[j].tik;
              const ox = Math.min(a.x + a.b, c.x + c.b) - Math.max(a.x, c.x);
              const oy = Math.min(a.y + a.h, c.y + c.h) - Math.max(a.y, c.y);
              assert.ok(ox <= 0.01 || oy <= 0.01, `${wie}: ${ind.haltes[i].id} en ${ind.haltes[j].id} overlappen`);
            }
          }
          assert.equal(ind.labels.filter((l) => l.soort === 'hier').length, 1, `${wie}: één label „hier”`);
        }
      }
    }
  }
});

test('SX-18: het smalste geval, leerblok 3 met 5.1 open, heeft 12 kolommen; onder 28 px alleen labels van „hier” en de overstappunten', () => {
  const m = metroModel({ blok: blok(3), store: nepStore(), adres: { soort: 'taak', taak: '5.1', stap: 2 } });
  assert.equal(m.kolommen.length, 12);
  const smal = metroIndeling(m, 328);
  assert.equal(smal.smal, true);
  assert.ok(smal.labels.every((l) => l.soort === 'overstap' || l.soort === 'hier'));
  assert.deepEqual(smal.labels.filter((l) => l.soort === 'overstap').map((l) => [l.tekst, l.anker, l.x]), [['Vorige keer', 'start', 0], ['Afsluiten', 'end', 328]]);
  const breed = metroIndeling(m, 1024);
  assert.equal(breed.smal, false);
  assert.ok(breed.labels.some((l) => l.soort === 'kolom' && l.tekst === '6.1'));
  assert.ok(breed.labels.some((l) => l.soort === 'tak' && l.tekst === 'V'));
});

test('SX-19: takken liggen op ±18 px; dezelfde splitsing loopt parallel door; stompjes in de kleur van de vorige en volgende lijn', () => {
  const m = metroModel({ blok: blok(2), store: nepStore(), adres: { soort: 'taak', taak: '3.2', stap: 4 } });
  const ind = metroIndeling(m, 1024);
  const takA = ind.haltes.filter((h) => h.id.endsWith('-A'));
  assert.deepEqual(takA.map((h) => h.y), [Y_LIJN - RIJ, Y_LIJN - RIJ], 'tak A van oefenen en toepassen');
  const [o, t] = takA;
  assert.ok(ind.sporen.some((s) => s.x1 === o.x && s.x2 === t.x && s.y1 === o.y && s.y2 === t.y), 'tak A loopt recht door van O naar T');
  assert.deepEqual(ind.sporen.filter((s) => s.lijn !== 2).map((s) => s.lijn), [1, 3]);
  const lb1 = metroIndeling(metroModel({ blok: blok(1), store: nepStore(), adres: { soort: 'overzicht' } }), 600);
  assert.deepEqual(lb1.sporen.filter((s) => s.lijn !== 1).map((s) => s.lijn), [2], 'leerblok 1: alleen een stompje naar lijn 2');
  const v = metroIndeling(metroModel({ blok: blok(2), store: nepStore(), adres: { soort: 'overzicht' } }), 600);
  assert.ok(v.sporen.some((s) => s.gestippeld), 'de verdieping is gestippeld zolang ze niet gedaan is');
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `node --test tests/metro.test.mjs`
Expected: FAIL met „Cannot find module …/js/metro-indeling.js”.

- [ ] **Step 3: Write minimal implementation**

Maak `js/metro-indeling.js`:

```js
// Indeling van de metrokaart in pixels (SX-18, SX-19; DESIGN §6 Metrokaart; ADR B110). Puur: rekent uit het model van
// metro-model.js en een breedte waar elke halte, elk spoorstuk, elk label en elk tikvlak komt. Geen DOM.
//
// Elke kolom is even breed. Het tikvlak van een halte is een strook: de volle hoogte van de kaart en de breedte van de
// kolom; takken in één kolom delen de strook in de hoogte. Zo overlappen tikvlakken nooit (WCAG 2.5.8: ≥ 24 × 24 px).
export const HOOGTE = 96; // ≥ 44 px
export const Y_LIJN = 46;
export const RIJ = 18; // afstand van een tak tot de hoofdlijn
export const LABEL_BOVEN = 16; // labels van de overstappunten
export const LABEL_ONDER = 90; // taaknummers, stapletters en „hier”
export const SMAL = 28; // onder deze kolombreedte alleen de labels van „hier” en de overstappunten
export const TAK_LABEL = 56; // vanaf deze kolombreedte staan de korte labels van de takken naast hun halte
export const STRAAL = Object.freeze({ begin: 9, eind: 9, taak: 7, stap: 5, verdieping: 5 });

const yVan = (rij) => Y_LIJN + rij * RIJ;

/**
 * @param {ReturnType<import('./metro-model.js').metroModel>} model
 * @param {number} breedte in px
 */
export function metroIndeling(model, breedte) {
  const n = model.kolommen.length;
  const kol = breedte / n;
  const smal = kol < SMAL;
  const midden = (i) => kol * (i + 0.5);
  const haltes = [];
  const labels = [];
  const sporen = [];
  const lijn = (x1, y1, x2, y2, gestippeld, nr = model.leerblok) => sporen.push({ x1, y1, x2, y2, gestippeld: Boolean(gestippeld), lijn: nr });

  model.kolommen.forEach((k, i) => {
    const x = midden(i);
    const tikbaar = k.haltes.filter((h) => !h.doorgang).sort((a, b) => a.rij - b.rij);
    const hoogte = HOOGTE / tikbaar.length;
    tikbaar.forEach((h, j) => haltes.push({
      ...h, kolom: i, soort: k.soort, x, y: yVan(h.rij), r: STRAAL[k.soort] + (h.stand === 'hier' ? 2 : 0),
      tik: { x: kol * i, y: hoogte * j, b: kol, h: hoogte },
    }));
    if (k.soort === 'begin') labels.push({ tekst: k.label, x: 0, y: LABEL_BOVEN, anker: 'start', soort: 'overstap' });
    if (k.soort === 'eind') labels.push({ tekst: k.label, x: breedte, y: LABEL_BOVEN, anker: 'end', soort: 'overstap' });
    const hier = tikbaar.find((h) => h.stand === 'hier');
    if (hier) labels.push({ tekst: 'hier', x, y: LABEL_ONDER, anker: 'middle', soort: 'hier' });
    else if (!smal && k.label && k.soort !== 'begin' && k.soort !== 'eind') labels.push({ tekst: k.label, x, y: LABEL_ONDER, anker: 'middle', soort: 'kolom' });
    if (kol >= TAK_LABEL) {
      for (const h of tikbaar) {
        if (h.label) labels.push({ tekst: h.label, x: x + STRAAL[k.soort] + 4, y: yVan(h.rij) - STRAAL[k.soort] - 2, anker: 'start', soort: 'tak' });
      }
    }
  });

  const begin = model.kolommen[0];
  const eind = model.kolommen[n - 1];
  if (begin.overstap) lijn(0, Y_LIJN, midden(0), Y_LIJN, false, begin.overstap);
  for (let i = 0; i < n - 1; i += 1) {
    const a = model.kolommen[i];
    const b = model.kolommen[i + 1];
    const xa = midden(i);
    const xb = midden(i + 1);
    const xm = (xa + xb) / 2;
    if (a.spoor && a.spoor === b.spoor) {
      // dezelfde splitsing in twee opeenvolgende stappen: de takken lopen parallel door
      for (const h of a.haltes) {
        const g = b.haltes.find((x) => x.rij === h.rij);
        lijn(xa, yVan(h.rij), xb, yVan(g.rij), h.gestippeld || g.gestippeld);
      }
    } else {
      // splitsen en samenkomen halverwege twee kolommen
      for (const h of a.haltes) lijn(xa, yVan(h.rij), xm, Y_LIJN, h.gestippeld);
      for (const h of b.haltes) lijn(xm, Y_LIJN, xb, yVan(h.rij), h.gestippeld);
    }
  }
  if (eind.overstap) lijn(midden(n - 1), Y_LIJN, breedte, Y_LIJN, false, eind.overstap);
  return { breedte, hoogte: HOOGTE, kol, smal, haltes, labels, sporen };
}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `node --test tests/metro.test.mjs`
Expected: alle tests PASS (13).

- [ ] **Step 5: Commit**

```bash
git add js/metro-indeling.js tests/metro.test.mjs
git commit -m "B110, SX-18: indeling van de metrokaart in pixels (stroken als tikvlak, labels, sporen en stompjes)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 5: De tekening op zeven pagina's (`js/metro.js`, CSS, gewicht)

**Files:**
- Create: `js/metro.js`
- Modify: `css/site.css` (nieuw blok onderaan, vóór eventuele printregels niet nodig: `nav` staat al uit in `css/print.css`)
- Modify: `index.html`, `leerblok-1.html`, `leerblok-2.html`, `leerblok-3.html`, `leerblok-4.html`, `dossier.html`, `bronnen.html` (één regel)
- Modify: `tools/gewicht-check.mjs` (kopcommentaar en de lus over `data/…json`)
- Test: `tests/metro.test.mjs`

**Interfaces:**
- Consumes: `metroModel`, `laatsteLeerblok` (taak 3); `metroIndeling` (taak 4); `kiesOpslag`, `maakStore` (`js/store.js`); `normaliseerBlok` (`js/blok.js`); `leesAdres` (`js/taakweergave.js`); `h`, `wis` (`js/dom.js`).
- Produces: `tekenMetro(model, breedte) → SVGSVGElement`; luistert naar het documentevent `a3-voortgang` (taak 6 stuurt het).

- [ ] **Step 1: Write the failing test**

Voeg toe aan `tests/metro.test.mjs`:

```js
import { paginaBestanden, gewichten, GRENS, GRENS_BRON } from '../tools/gewicht-check.mjs';

const STUDENT = ['index.html', 'leerblok-1.html', 'leerblok-2.html', 'leerblok-3.html', 'leerblok-4.html', 'dossier.html', 'bronnen.html'];

test('SX-18: de kaart staat op de zeven studentpagina\'s en niet op docentmodus, verificatie en controlelab', () => {
  for (const p of STUDENT) assert.match(lees(p), /<script type="module" src="js\/metro\.js"><\/script>/, p);
  for (const p of ['docent.html', 'verificatie.html', 'controlelab.html']) assert.doesNotMatch(lees(p), /metro\.js/, p);
});

test('SX-18: de tekening heeft een lijst van links met aria-current, geen schaduw, beweging alleen zonder reduced motion', () => {
  const js = lees('js/metro.js');
  assert.match(js, /role: 'list'/);
  assert.match(js, /role: 'listitem'/);
  assert.match(js, /'aria-current': h\.stand === 'hier' \? 'step' : null/);
  assert.match(js, /'aria-hidden': 'true'/, 'sporen en labels zijn decoratief; de naam staat op de link');
  assert.match(js, /addEventListener\('a3-voortgang'/);
  const css = lees('css/site.css');
  const metro = css.slice(css.indexOf('/* ---- metrokaart'));
  assert.ok(metro.length > 0 && metro.includes('.metro-spoor'), 'blok .metro in site.css');
  assert.doesNotMatch(metro, /box-shadow|filter:\s*drop-shadow/, 'SX-7: geen schaduw');
  assert.match(metro, /transition:fill 200ms/, 'SX-9: vullen in 200 ms');
  assert.match(metro, /font-size:13px/, 'SX-10: labels 13 px');
});

test('PF-4: leerblokpagina\'s tellen alleen hun eigen leerblokbestand; start, dossier en bronnen tellen de vier', () => {
  const namen = (p) => paginaBestanden(root, p).map((f) => f.replace(`${root}/`, '')).filter((f) => /^data\/leerblok-\d\.json$/.test(f)).sort();
  assert.deepEqual(namen('leerblok-3.html'), ['data/leerblok-3.json']);
  for (const p of ['index.html', 'dossier.html', 'bronnen.html']) assert.deepEqual(namen(p), [1, 2, 3, 4].map((n) => `data/leerblok-${n}.json`), p);
  assert.ok(paginaBestanden(root, 'index.html').some((f) => f.endsWith('js/metro-indeling.js')));
  for (const g of gewichten(root)) assert.ok(g.gzip <= GRENS && g.bytes <= GRENS_BRON, `${g.pagina}: ${g.bytes} bytes, ${g.gzip} gzip`);
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `node --test tests/metro.test.mjs`
Expected: FAIL; geen `js/metro.js` in `index.html`.

- [ ] **Step 3: Write minimal implementation**

Maak `js/metro.js`:

```js
// Metrokaart bovenaan elke studentpagina (SX-18, SX-19; ADR B110; DESIGN §6 Metrokaart). Alleen DOM: het model staat in
// metro-model.js, de maten in metro-indeling.js. Tekent opnieuw bij een adreswissel, bij `a3-voortgang` (leerblok.js,
// media.js) en bij een andere breedte. Laadt de data niet, dan komt er geen kaart en werkt de pagina gewoon (spec §5).
import { h, wis } from './dom.js';
import { kiesOpslag, maakStore } from './store.js';
import { normaliseerBlok } from './blok.js';
import { leesAdres } from './taakweergave.js';
import { metroModel, laatsteLeerblok } from './metro-model.js';
import { metroIndeling } from './metro-indeling.js';

const SVG = 'http://www.w3.org/2000/svg';
/** Een SVG-element (h() in dom.js maakt HTML-elementen). */
function s(tag, attrs = {}, ...kinderen) {
  const el = document.createElementNS(SVG, tag);
  for (const [k, v] of Object.entries(attrs)) if (v !== undefined && v !== null && v !== false) el.setAttribute(k, v);
  for (const kind of kinderen.flat()) if (kind !== undefined && kind !== null) el.append(kind instanceof Node ? kind : document.createTextNode(String(kind)));
  return el;
}
const laad = async (pad) => (await fetch(new URL(pad, import.meta.url))).json();

/** De kaart als SVG: sporen en labels zijn decoratief, de haltes zijn links in een lijst. */
export function tekenMetro(model, breedte) {
  const ind = metroIndeling(model, breedte);
  const svg = s('svg', {
    class: 'metro-kaart', viewBox: `0 0 ${breedte} ${ind.hoogte}`, width: breedte, height: ind.hoogte,
    role: 'list', 'aria-label': model.label, style: `--lijn: var(--lijn-${model.leerblok})`,
  });
  for (const sp of ind.sporen) {
    svg.append(s('line', {
      x1: sp.x1, y1: sp.y1, x2: sp.x2, y2: sp.y2, 'aria-hidden': 'true',
      class: `metro-spoor${sp.gestippeld ? ' gestippeld' : ''}`, style: sp.lijn === model.leerblok ? null : `stroke: var(--lijn-${sp.lijn})`,
    }));
  }
  for (const l of ind.labels) {
    svg.append(s('text', { x: l.x, y: l.y, 'text-anchor': l.anker, class: `metro-label metro-label-${l.soort}`, 'aria-hidden': 'true' }, l.tekst));
  }
  for (const h of ind.haltes) {
    svg.append(s('a', {
      href: h.href, role: 'listitem', 'aria-label': h.naam, 'aria-current': h.stand === 'hier' ? 'step' : null,
      class: `metro-halte halte-${h.stand} halte-${h.soort}${h.gestippeld ? ' halte-niet-gekozen' : ''}`,
    },
    s('rect', { class: 'metro-tik', x: h.tik.x, y: h.tik.y, width: h.tik.b, height: h.tik.h }),
    s('circle', { cx: h.x, cy: h.y, r: h.r })));
  }
  return svg;
}

async function plaatsMetro() {
  const nummer = Number(document.body.dataset.leerblok) || null;
  const header = document.querySelector('body > header');
  if (!header) return;
  const { opslag } = kiesOpslag();
  const store = maakStore(opslag);
  const laatste = nummer ? null : laatsteLeerblok(store);
  const elders = laatste?.leerblok;
  // Leerblokpagina's lezen hun eigen bestand; start, dossier en bronnen dat van de laatste positie (tools/gewicht-check.mjs: ${elders}).
  const blok = normaliseerBlok(nummer ? await laad(`../data/leerblok-${nummer}.json`) : await laad(`../data/leerblok-${elders}.json`));
  const ids = blok.taken.map((t) => t.id);
  const adres = () => (nummer ? leesAdres(location.hash, ids) : { soort: 'elders', taak: laatste.taak, stap: laatste.stap });

  const doek = h('div', { class: 'metro-doek' });
  const regel = h('p', { class: 'metro-regel' });
  header.after(h('nav', { class: 'metro', 'aria-label': `Waar je bent in leerblok ${blok.leerblok}` }, doek, regel));
  let breedte = 0;
  function teken() {
    breedte = Math.floor(doek.clientWidth) || 328;
    const model = metroModel({ blok, store, adres: adres() });
    wis(doek).append(tekenMetro(model, breedte));
    regel.textContent = model.tekst;
  }
  teken();
  window.addEventListener('hashchange', teken);
  window.addEventListener('popstate', teken);
  document.addEventListener('a3-voortgang', teken);
  const opnieuw = () => { if (Math.floor(doek.clientWidth) !== breedte) teken(); };
  if (typeof ResizeObserver === 'function') new ResizeObserver(opnieuw).observe(doek); else window.addEventListener('resize', opnieuw);
}

plaatsMetro().catch(() => { /* zonder data of opslag geen kaart; de rest van de pagina werkt (spec §5) */ });
```

`css/site.css`, onderaan:

```css
/* ---- metrokaart (SX-18, SX-19; DESIGN §6 Metrokaart; ADR B110) ---- */
.metro { margin:.25rem 0 .75rem; }
.metro-doek { width:100%; }
.metro-kaart { display:block; max-width:100%; overflow:visible; }
.metro-spoor { stroke:var(--lijn); stroke-width:6; stroke-linecap:round; }
.metro-spoor.gestippeld { stroke-dasharray:6 4; stroke-linecap:butt; }
.metro-tik { fill:transparent; }
.metro-halte circle { fill:var(--wit); stroke:var(--lijn); stroke-width:3; transition:fill 200ms ease; }
.metro-halte.halte-af circle { fill:var(--lijn); }
.metro-halte.halte-hier circle { fill:var(--wit); stroke:var(--zwart); }
.metro-halte.halte-begin circle, .metro-halte.halte-eind circle { stroke:var(--zwart); stroke-width:4; }
.metro-halte.halte-begin.halte-af circle, .metro-halte.halte-eind.halte-af circle { fill:var(--zwart); }
.metro-halte:focus-visible .metro-tik { stroke:var(--accent); stroke-width:4; }
.metro-label { font-size:13px; fill:var(--grijs-tekst); }
.metro-label-hier, .metro-label-overstap { font-weight:700; fill:var(--zwart); }
.metro-regel { font-size:.8125rem; color:var(--grijs-tekst); margin:.25rem 0 0; }
```

Voeg in de zeven studentpagina's direct na `<script type="module" src="js/site.js"></script>` deze regel toe:

```html
<script type="module" src="js/metro.js"></script>
```

```bash
for p in index.html leerblok-1.html leerblok-2.html leerblok-3.html leerblok-4.html dossier.html bronnen.html; do
  sed -i '' 's#<script type="module" src="js/site.js"></script>#&\n<script type="module" src="js/metro.js"></script>#' "$p"
done
grep -c 'js/metro.js' index.html leerblok-1.html leerblok-2.html leerblok-3.html leerblok-4.html dossier.html bronnen.html
```

Expected: elk bestand `1`. (BSD-sed op macOS zet `\n` in de vervanging niet om; staat er een letterlijke `n`, gebruik dan de Edit-tool per bestand.)

`tools/gewicht-check.mjs`: voeg in het kopcommentaar, onder de regel over `import(\`./lb${n}.js\`)`, toe:

```js
//   data/leerblok-${elders}.json      het leerblok van de laatste positie (metrokaart, ADR B110): telt alle leerblokbestanden
//                                     op pagina's zonder leerblok (start, dossier, bronnen) en geen op een leerblokpagina
```

en in de lus over `data/…json`, vóór de laatste `else dataBestanden(…)`:

```js
      else if (sjabloon === '${elders}') { if (!nummer) dataBestanden(new RegExp(`^${voor}\\d${na}\\.json$`)).forEach((n) => set.add(resolve(datamap, n))); }
```

- [ ] **Step 4: Run test to verify it passes**

Run: `node --test && node tools/content-check.mjs && node tools/link-check.mjs && node tools/gewicht-check.mjs`
Expected: alle tests PASS; content-check en link-check 0 fouten; gewicht-check `ok` voor elke pagina (index rond 290 kB bron, leerblok-3 rond 450 kB bron, alle gzip < 150 kB).

- [ ] **Step 5: Commit**

```bash
git add js/metro.js css/site.css index.html leerblok-1.html leerblok-2.html leerblok-3.html leerblok-4.html dossier.html bronnen.html tools/gewicht-check.mjs tests/metro.test.mjs
git commit -m "B110, SX-18: metrokaart als SVG bovenaan de zeven studentpagina's; gewichtscontrole kent \${elders}

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 6: De kaart vervangt de segmentbalk; voortgang en mediaroute tekenen opnieuw

**Files:**
- Modify: `js/leerblok.js:15` (import), `:396-424` (taakkop)
- Modify: `js/media.js` (functie `toon` in `bouwMediaSectie`, rond regel 195)
- Modify: `tests/voortgang.test.mjs:68`
- Test: `tests/metro.test.mjs`

**Interfaces:**
- Consumes: `metro.js` luistert naar `a3-voortgang` (taak 5).
- Produces: `document.dispatchEvent(new CustomEvent('a3-voortgang', …))` vanuit `tekenVoortgang` (leerblok.js) en na het bewaren van een route (media.js).

- [ ] **Step 1: Write the failing test**

Voeg toe aan `tests/metro.test.mjs`:

```js
test('SX-4: de taakkop heeft geen segmentbalk meer; voortgang en routekeuze laten de kaart opnieuw tekenen', () => {
  const lb = lees('js/leerblok.js');
  assert.doesNotMatch(lb, /class: 'segmenten'/);
  assert.doesNotMatch(lb, /segmentLabel/, 'het tekstalternatief staat op de kaart (metro-model.js)');
  assert.match(lb, /dispatchEvent\(new CustomEvent\('a3-voortgang'/);
  assert.match(lees('js/media.js'), /dispatchEvent\(new CustomEvent\('a3-voortgang'/);
  assert.match(lees('js/metro-model.js'), /segmentLabel\(taakNr, ids\.length/);
});
```

Vervang in `tests/voortgang.test.mjs` regel 68:

```js
  assert.match(lees('js/leerblok.js'), /segmenten\.setAttribute\('aria-label', segmentLabel\(/);
```

door:

```js
  assert.match(lees('js/metro-model.js'), /segmentLabel\(/, 'SX-4: het tekstalternatief staat op de metrokaart (ADR B110)');
```

- [ ] **Step 2: Run test to verify it fails**

Run: `node --test tests/metro.test.mjs tests/voortgang.test.mjs`
Expected: FAIL in de nieuwe test („class: 'segmenten'” staat nog in leerblok.js).

- [ ] **Step 3: Write minimal implementation**

`js/leerblok.js`, regel 15: haal `segmentLabel` uit de import:

```js
import { klaarAlsLijst, stapStand, a3Stand } from './voortgang.js'; // fase 17: SX-5, SX-12; SX-4 staat op de metrokaart (B110)
```

Vervang:

```js
    // vaste kop: taaknummer in het leerblok, segmentbalk van de vier stappen en de stappenrij (SX-4)
    const segmenten = h('div', { class: 'segmenten', role: 'img' });
    const stappenRij = h('ol', { class: 'stappenrij' });
```

door:

```js
    // vaste kop: taaknummer in het leerblok en de stappenrij; de vier stappen staan als haltes op de metrokaart (SX-4, B110)
    const stappenRij = h('ol', { class: 'stappenrij' });
```

Vervang:

```js
      segmenten.setAttribute('aria-label', segmentLabel(taakNr, blok.taken.length, stand));
      tekenVoet();
      wis(segmenten);
      // DESIGN §5.3: voltooid zwart, de stap waar je bent in accent, de rest grijs
      const hierStap = adres.soort === 'taak' && adres.taak === id ? adres.stap : stand.actief + 1;
      stand.stappen.forEach((st, i) => segmenten.append(h('span', { class: `segment segment-${i + 1 === hierStap ? 'actief' : st.stand === 'voltooid' ? 'voltooid' : 'open'}` })));
      wis(stappenRij);
      // onderstreept is de stap die de student nu ziet; de segmenten tonen de voortgang
```

door:

```js
      document.dispatchEvent(new CustomEvent('a3-voortgang', { detail: { taak: id } })); // de metrokaart tekent opnieuw (metro.js)
      tekenVoet();
      wis(stappenRij);
      // onderstreept is de stap die de student nu ziet; de metrokaart toont de voortgang
```

En haal in `const kop = [ … ]` de regel `        segmenten,` weg.

`js/media.js`, in `toon` van `bouwMediaSectie`, direct na de regel met `if (bewaar) { try { bewaarRoute(…` :

```js
    if (bewaar) globalThis.document?.dispatchEvent(new CustomEvent('a3-voortgang')); // de metrokaart toont de gekozen route (SX-19)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `node --test && node tools/content-check.mjs && node tools/link-check.mjs`
Expected: alle tests PASS (de basis was 654 geslaagd en 5 overgeslagen, plus de nieuwe tests van `tests/metro.test.mjs`); 0 fouten.

- [ ] **Step 5: Commit**

```bash
git add js/leerblok.js js/media.js tests/voortgang.test.mjs tests/metro.test.mjs
git commit -m "B110, SX-4: metrokaart vervangt de segmentbalk in de taakkop; voortgang en routekeuze tekenen de kaart opnieuw

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 7: Controle in de browser, README en BUILDPLAN

**Files:**
- Modify: `README.md` (a3-learning; een alinea onder het contentcontract)
- Modify (c-cluster-1-worktree): `docs/BUILDPLAN-ELEARNING-A3.md` (nieuwe aanvulling vóór `## Bijlage — Dekking van de blueprintregels per fase`)

- [ ] **Step 1: Start een lokale server**

Run (achtergrond): `python3 -m http.server 8137 --directory /Users/witoldtenhove/Documents/HAN/a3-learning/.worktrees/metrokaart`

- [ ] **Step 2: Doorloop op 360 × 740 en 1280 × 800 (Playwright of Chrome DevTools)**

Controleer en noteer per punt ok of fout:

1. `index.html` (lege opslag): kaart van lijn 1 in magenta, „hier” bij „Start”; `document.documentElement.scrollWidth <= innerWidth`.
2. `leerblok-2.html`: lijn blauw; begin „Vorige keer” met magenta stompje, eind „Afsluiten” met groen stompje; de verdieping als gestippelde zijtak na 4.1.
3. Tik op halte 3.2 → taak 3.2 opent; de kaart klapt 3.2 open in W S O T; O en T liggen op twee takken A en B; de taakkop heeft geen segmentbalk meer.
4. In de oefening van 3.2 „B · AI-tool” kiezen → tak A gestippeld, B vol (zonder herladen).
5. Taak 4.1, stap stof: drie takken T V S; kies video → V vol, T en S gestippeld.
6. Tab door de kaart: focus volgt de lijn van links naar rechts, takken van boven naar beneden; focusrand zichtbaar; schermlezer-naam bevat taak en stand (inspecteer `aria-label`).
7. `leerblok-3.html#taak-5.1/stof` op 360 px: 12 kolommen, geen horizontale scroll, alleen „hier” en de overstaplabels.
8. Terug naar `dossier.html` en `bronnen.html`: lijn van het laatst geopende leerblok, „hier” op die taak.
9. `docent.html`, `verificatie.html`, `controlelab.html`: geen kaart.
10. Afdrukvoorbeeld van `dossier.html`: geen kaart op papier.
11. Met `prefers-reduced-motion: reduce` (emulatie): geen transitie op de haltes.

Bij een fout: los op in de taak die de code bezit, met eerst een test die hem vastlegt, en draai `node --test` opnieuw.

- [ ] **Step 3: README**

Voeg in `README.md` na het blok „Contract voor latere fasen” een alinea toe:

```markdown
## Metrokaart (ADR B110)

Bovenaan de zeven studentpagina's staat een metrokaart van één leerblok (SX-18, SX-19): `js/metro-model.js` (haltes, takken, stand en links, zonder DOM), `js/metro-indeling.js` (pixels: elke kolom even breed, het tikvlak is een strook van de volle hoogte) en `js/metro.js` (SVG onder de kop). Splitsingen staan in de leerblokdata als `"spoor": { "stappen": ["oefenen"], "veld": "artikel", "takken": [{ "waarde": "<optie>", "kort": "Art. 1" }, …] }`; content-check controleert dat de takken opties van het veld zijn. De verdieping (`verdieping.na`) en de mediataak (`media.taak`) komen er vanzelf op. De kaart tekent opnieuw bij een adreswissel en bij het event `a3-voortgang`. Start, dossier en bronnen tonen het leerblok met de jongste `positie:N`; de gewichtscontrole telt daar alle vier leerblokbestanden (`${elders}`).
```

- [ ] **Step 4: BUILDPLAN in c-cluster-1**

In `/Users/witoldtenhove/Documents/HAN/c-cluster-1/.worktrees/metrokaart/docs/BUILDPLAN-ELEARNING-A3.md`, direct vóór `## Bijlage — Dekking van de blueprintregels per fase`:

```markdown
## Aanvulling — Metrokaart (1-10-2026, op verzoek van de auteur)

Spec: `docs/superpowers/specs/2026-10-01-metrokaart-design.md`; plan: `docs/superpowers/plans/2026-10-01-metrokaart.md`. Besluit: ADR B110.

- [x] Veld `spoor` in de leerblokdata (3.2 route A/B, 4.2 artikel 1/2) met contentcontrole (SX-19).
- [x] Tokens `--lijn-1` … `--lijn-4` en contrastcontrole 3:1 voor lijnen (SX-18).
- [x] `js/metro-model.js` en `js/metro-indeling.js` met tests: stand, takken, overstappunten, „hier”; stroken ≥ 24 × 24 px zonder overlap op 328, 600 en 1024 px.
- [x] `js/metro.js` op de zeven studentpagina's; segmentbalk uit de taakkop (SX-4); gewichtscontrole kent `${elders}`.
- [x] Doorloop in de browser op 360 en 1280 px (11 punten uit het plan).
```

Vink alleen aan wat in stap 2 echt ok was; laat een punt open met de reden als het niet lukte.

- [ ] **Step 5: Eindcontrole en commits**

Run (a3-learning-worktree): `node --test && node tools/content-check.mjs && node tools/link-check.mjs && node tools/gewicht-check.mjs`
Expected: alles slaagt.

```bash
git add README.md
git commit -m "B110: README beschrijft de metrokaart

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
cd /Users/witoldtenhove/Documents/HAN/c-cluster-1/.worktrees/metrokaart
git add docs/BUILDPLAN-ELEARNING-A3.md docs/superpowers/plans/2026-10-01-metrokaart.md
git commit -m "BUILDPLAN: aanvulling metrokaart (B110)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

Stop de server. Niet mergen en niet pushen: dat beslist de auteur (superpowers:finishing-a-development-branch).
