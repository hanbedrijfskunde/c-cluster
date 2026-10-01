# Leerblok 2: een artikel gebruiken (IMRAD) — uitvoeringsplan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Leerblok 2 van de e-learning A3 krijgt een nieuwe taak 4.2 „Haal meer uit je artikel”, waarin de student een onderzoeksartikel met IMRAD ontleedt en er theorie, methode en presentatie uit haalt voor zijn A3, met begeleid AI-gebruik en nieuw bewijs EV-12.

**Architecture:** Alles volgt bestaande patronen. Controles zijn zuivere fabrieken in `js/checks/lb2.js`; de schermindeling is een `weergave` in `data/leerblok-2.json` die `js/lb2-ui.js` tekent; figuren staan per leerblok in een eigen module (`js/figuren-lb2.js`, nieuw) die alleen laadt als de data ze gebruikt (PF-4, B97). De stelling verhuist van taak 4.2 naar 4.3; een eenmalige omzetting (`js/migratie.js`, nieuw) verplaatst de opslagsleutels die aan het taaknummer hangen.

**Tech Stack:** statische site, vanilla ES-modules, JSON-content, `node --test`, `tools/content-check.mjs`, `tools/link-check.mjs`, `tools/gewicht-check.mjs`. Geen build.

**Spec:** `docs/superpowers/specs/2026-10-01-leerblok2-artikel-gebruiken-design.md` (repository c-cluster-1). Lees het spec vóór je begint.

**Twee repositories:**
- `A3L` = `/Users/witoldtenhove/Documents/HAN/a3-learning` (de site; taken 1–6)
- `CC` = `/Users/witoldtenhove/Documents/HAN/c-cluster-1` (ontwerpdocumenten; taak 7)

## Global Constraints

- Taal van alle studenttekst: Nederlands, zinnen ≤ 20 woorden, geen AI-taal (`redigeer-nederlandse-tekst`, `schrap-ai-taal` vóór oplevering van teksten).
- Richttijd leerblok 2 blijft 45 minuten: 3.1 = 5, 3.2 = 10, 4.1 = 10, 4.2 = 15, 4.3 = 5 (NFR-07).
- Geen tekst of figuur uit `lits/` overnemen; Wu (2011) alleen citeren. De IMRAD-figuur is een eigen SVG.
- Modellen altijd als beeld (B92, B95, SX-15): IMRAD staat als figuur in de stof van 4.2.
- Een oefenvraag heeft een hint met `hintBron` die naar stof van deze of een eerdere taak wijst (SX-13, B85, TK-19); een hint verklapt het modelantwoord niet (geen gemeenschappelijk stuk van 15 tekens).
- Het modelantwoord van een oefening verschijnt pas na eigen werk (TK-6); bij 4.2 via `modelNa` als lijst velden (B100).
- Statusregel (`js/status.js`): soort A/B op `mist` → Te doen; soort C op `mist` of A/B op `let op` → Bijna; anders Compleet.
- PF-4: ≤ 300 kB gecomprimeerd en ≤ 500 kB ongecomprimeerd per pagina; 0 verwijzingen naar andere domeinen.
- Werkboek en draaiboek van week 5 blijven ongewijzigd (besluit van de auteur).
- ADR: alleen onderaan toevoegen; volgende nummers B101 en B102.
- Commit alleen de bestanden van de eigen taak (`git add <paden>`), nooit `git add -A`: in A3L staat nog niet-gecommit werk van B98–B100 (zie taak 0).
- Elke commit eindigt met `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## Review Focus

1. **Een student die de stelling al maakte, opent leerblok 2 na de update.** Verwacht: taak 4.3 staat op klaar met zijn oude argument; de nieuwe taak 4.2 is open; niets gaat verloren; tweede keer laden verandert niets. Test in taak 2 (`zetStellingOm` idempotent + volledige sleutelset).
2. **Vindplaats in vrije vorm** („p.4”, „blz 12”, „Methods section”, „§3.2”, „tabel 2”, „H3”, „pagina vier”). Verwacht: gangbare vormen met een getal of sectienaam tellen; vage tekst („ergens in het midden”) geeft *let op*, niet *mist*. Test in taak 1 (`isVindplaats`).
3. **Student kiest AI „om te ontleden” en vergeet het vinkje, of zet het vinkje en kiest daarna „nee”.** Verwacht: zonder vinkje Te doen; met „nee” telt een achtergebleven vinkje niet mee. Test in taak 1 (`aiGeverifieerd`).
4. **Bron uit 4.1 is geen onderzoeksartikel of 4.1 is leeg.** Verwacht: de spiegeltabel toont „—”, de hint wijst naar een ander artikel; de prompt gebruikt `anderArtikel` als dat is ingevuld, anders `b1titel`, anders de plek „[titel van je artikel]”. Test in taak 3 (`artikelPrompt`, `kiesTitel`).
5. **Smalle telefoon (360 px).** Verwacht: IMRAD-figuur en mini-artikelen zonder horizontale scroll; grafiek leesbaar. Test in taak 4 (bestaande 0-scroll-controle in `tests/toegankelijk.test.mjs` of `tests/beeld.test.mjs` uitbreiden) en doorloop in taak 6.

---

### Task 0: Openstaand werk vastleggen (vooraf, met akkoord van de auteur)

**Files:** geen nieuwe.

- [ ] **Step 1:** In A3L staat niet-gecommit werk van B98/B99 (TOM-bord, gewichtsgrens) en B100 (oefening 3.2). Vraag de auteur of dat eerst in eigen commits mag. Zo niet: stop, want taken 3–5 raken `js/leerblok.js`, `js/lb2-ui.js`, `tools/content-check.mjs` en `data/leerblok-2.json`.
- [ ] **Step 2:** Run `cd A3L && node --test 2>&1 | grep -E "^ℹ (pass|fail)"`. Verwacht: `fail 0`. Dit is de basislijn.

---

### Task 1: Controles voor EV-12

**Files:**
- Modify: `A3L/js/checks/lb2.js` (nieuwe functies vóór `export const FABRIEKEN`, en die lijst uitbreiden)
- Test: `A3L/tests/lb2.test.mjs`

**Interfaces:**
- Produces:
  - `isVindplaats(tekst: string): boolean`
  - `imradIngevuld({ id, velden: string[], labels: string[] })` → controle, soort A
  - `imradVindplaats({ id, velden, labels })` → controle, soort A
  - `imradMeenemen({ id, velden, labels, toegestaan = ['ja', 'deels', 'nee'] })` → controle, soort A
  - `aiGeverifieerd({ id, veld, aiVeld, waarde })` → controle, soort A
  - `artikelPrompt(titel: string): string`
  - `kiesTitel(waarden: object, ids: string[]): string` (eerste niet-lege waarde, getrimd; anders `''`)
  - constante `AI_ONTLEDEN = 'ja, om het te ontleden'`

- [ ] **Step 1: Schrijf de falende tests.** Voeg aan de import bovenaan `tests/lb2.test.mjs` toe: `isVindplaats, imradIngevuld, imradVindplaats, imradMeenemen, aiGeverifieerd, artikelPrompt, kiesTitel, AI_ONTLEDEN`. Voeg in het object `CONTROLES` (vóór de sluitende `};` op regel ~151) toe:

```js
  imradIngevuld: {
    controle: imradIngevuld({ id: 'i', velden: ['iWat', 'mWat', 'rWat'], labels: ['Inleiding', 'Methode', 'Resultaten'] }), soort: 'A',
    goed: [
      [{ iWat: 'Bouwt op Oliver.', mWat: 'Acht interviews.', rWat: 'In lopende tekst.' }, 'ok'],
      [{ iWat: 'Twee modellen.', mWat: 'Enquête, n = 300.', rWat: 'Eén tabel.' }, 'ok'],
      [{ iWat: 'Definitie van TOM.', mWat: 'Casestudy.', rWat: 'Een model als figuur.' }, 'ok'],
    ],
    zwak: [
      [{}, 'mist', 'Inleiding, Methode, Resultaten'],
      [{ iWat: 'x x x', mWat: '' }, 'mist', 'Methode, Resultaten'],
      [{ iWat: 'Ja.', mWat: 'Ja.', rWat: '   ' }, 'mist', 'Resultaten'],
    ],
  },
  imradVindplaats: {
    controle: imradVindplaats({ id: 'w', velden: ['iWaar', 'mWaar', 'rWaar'], labels: ['Inleiding', 'Methode', 'Resultaten'] }), soort: 'A',
    goed: [
      [{ iWaar: 'Inleiding', mWaar: 'Methode', rWaar: 'p. 7' }, 'ok'],
      [{ iWaar: 'Introduction, p. 2', mWaar: '§ 3.2', rWaar: 'Table 2' }, 'ok'],
      [{ iWaar: 'blz 3', mWaar: 'Methods', rWaar: 'figuur 1' }, 'ok'],
    ],
    zwak: [
      [{ iWaar: 'Inleiding', mWaar: '', rWaar: 'p. 7' }, 'mist', 'Methode'],
      [{ iWaar: 'ergens vooraan', mWaar: 'Methode', rWaar: 'p. 7' }, 'let op', 'Inleiding'],
      [{}, 'mist', 'Inleiding, Methode, Resultaten'],
    ],
  },
  imradMeenemen: {
    controle: imradMeenemen({ id: 'm', velden: ['iMee', 'mMee', 'rMee'], labels: ['Inleiding', 'Methode', 'Resultaten'] }), soort: 'A',
    goed: [
      [{ iMee: 'ja', mMee: 'deels', rMee: 'nee' }, 'ok'],
      [{ iMee: 'nee', mMee: 'nee', rMee: 'nee' }, 'ok'],
      [{ iMee: ['ja'], mMee: 'ja', rMee: 'deels' }, 'ok'],
    ],
    zwak: [
      [{}, 'mist', 'Inleiding, Methode, Resultaten'],
      [{ iMee: 'ja', mMee: 'misschien', rMee: 'ja' }, 'mist', 'Methode'],
      [{ iMee: 'ja', mMee: 'ja' }, 'mist', 'Resultaten'],
    ],
  },
  aiGeverifieerd: {
    controle: aiGeverifieerd({ id: 'a', veld: 'aiCheck', aiVeld: 'ai', waarde: AI_ONTLEDEN }), soort: 'A',
    goed: [
      [{ ai: 'nee' }, 'ok'],
      [{ ai: 'ja, om het te begrijpen' }, 'ok'],
      [{ ai: AI_ONTLEDEN, aiCheck: ['Ik heb elk citaat en elke vindplaats zelf in het artikel teruggevonden.'] }, 'ok'],
    ],
    zwak: [
      [{}, 'mist', 'AI'],
      [{ ai: AI_ONTLEDEN }, 'mist', 'teruggevonden'],
      [{ ai: AI_ONTLEDEN, aiCheck: [] }, 'mist', 'teruggevonden'],
    ],
  },
```

En onder de bestaande test `apaJaar leest het jaar uit een APA-regel`:

```js
test('EV-12: isVindplaats herkent sectienamen, pagina’s, paragrafen, tabellen en figuren', () => {
  for (const s of ['Inleiding', 'introductie', 'Introduction', 'Theoretisch kader', 'Literature review', 'Methode', 'methoden', 'Method',
    'Methods section', 'Methodology', 'Resultaten', 'Results', 'Bevindingen', 'Discussie', 'Discussion', 'Conclusie', 'Abstract',
    'Samenvatting', 'p. 4', 'p.4', 'pp. 4-6', 'pag. 12', 'pagina 3', 'blz 12', 'blz. 12', '§ 3.2', '§3', 'tabel 2', 'Table 1', 'figuur 1',
    'Fig. 3', 'sectie 2', 'section 4', 'H3', 'hoofdstuk 2']) assert.ok(isVindplaats(s), s);
  for (const s of ['', '   ', 'ergens vooraan', 'pagina vier', 'in het artikel', 'zie boven']) assert.ok(!isVindplaats(s), s);
});

test('EV-12: aiGeverifieerd negeert een achtergebleven vinkje als AI niet om te ontleden is gebruikt', () => {
  const c = aiGeverifieerd({ id: 'a', veld: 'aiCheck', aiVeld: 'ai', waarde: AI_ONTLEDEN });
  assert.equal(c({ ai: 'nee', aiCheck: ['x'] }).resultaat, 'ok');
});

test('EV-12: de artikelprompt vult de titel in, vraagt per deel een citaat met pagina en zegt „verzin niets”', () => {
  const p = artikelPrompt('Klanttevredenheid in webwinkels');
  assert.match(p, /^Ik lees dit artikel: Klanttevredenheid in webwinkels\. /);
  assert.match(p, /letterlijk citaat .*paginanummer/);
  assert.match(p, /Verzin niets\. Staat iets niet in het artikel, zeg dat dan\.$/);
  assert.match(artikelPrompt(''), /^Ik lees dit artikel: \[titel van je artikel\]\. /);
});

test('EV-12: kiesTitel neemt de eerste ingevulde titel', () => {
  assert.equal(kiesTitel({ anderArtikel: '  ', b1titel: 'A' }, ['anderArtikel', 'b1titel']), 'A');
  assert.equal(kiesTitel({ anderArtikel: 'B', b1titel: 'A' }, ['anderArtikel', 'b1titel']), 'B');
  assert.equal(kiesTitel({}, ['anderArtikel', 'b1titel']), '');
});
```

- [ ] **Step 2: Run en zie het falen.** `cd A3L && node --test tests/lb2.test.mjs 2>&1 | tail -5`. Verwacht: SyntaxError/does not provide an export named `isVindplaats`.

- [ ] **Step 3: Implementeer.** Voeg in `js/checks/lb2.js` toe, direct vóór `/** Fabrieken van dit bestand, op naam`:

```js
// ---------------------------------------------------------------- ontleed artikel (EV-12, ADR B101/B102)

export const AI_ONTLEDEN = 'ja, om het te ontleden';

const SECTIES = /\b(inleiding|introductie|introduction|theoretisch kader|theorie|literatuur(?:overzicht)?|literature review|background|achtergrond|methoden?|methodologie|method(?:s|ology)?|resultaten|results|bevindingen|findings|discussie|discussion|conclusies?|conclusions?|abstract|samenvatting)\b/i;
const MET_GETAL = /\b(p|pp|pag|pagina|blz|sectie|section|tabel|table|figuur|figure|fig|hoofdstuk|h)\.?\s*\d+/i;

/** Ziet de tekst eruit als een plek in een artikel: een sectienaam, of p./blz./§/tabel/figuur/sectie/hoofdstuk/H met een getal (EV-12). */
export function isVindplaats(t) {
  const s = tekst(t);
  return s !== '' && (SECTIES.test(s) || MET_GETAL.test(s) || /§\s*\d/.test(s));
}

/** Bij Inleiding, Methode en Resultaten staat wat de auteur doet (EV-12). */
export function imradIngevuld({ id, velden, labels }) {
  return (invoer) => {
    const mist = velden.filter((v) => tekst(invoer?.[v]) === '').map((v) => labels[velden.indexOf(v)]);
    if (mist.length > 0) return resultaat(id, 'A', 'mist', `Schrijf op wat de auteur doet bij: ${mist.join(', ')}.`);
    return resultaat(id, 'A', 'ok');
  };
}

/** Elke vindplaats is ingevuld (anders `mist`) en ziet eruit als een sectie of pagina (anders `let op`) (EV-12, B102). */
export function imradVindplaats({ id, velden, labels }) {
  return (invoer) => {
    const leeg = velden.filter((v) => tekst(invoer?.[v]) === '').map((v) => labels[velden.indexOf(v)]);
    if (leeg.length > 0) return resultaat(id, 'A', 'mist', `Geef de vindplaats (sectie of pagina) bij: ${leeg.join(', ')}.`);
    const vaag = velden.filter((v) => !isVindplaats(invoer?.[v])).map((v) => labels[velden.indexOf(v)]);
    if (vaag.length > 0) return resultaat(id, 'A', 'let op', `Noem een sectie of pagina, bijvoorbeeld „Methode” of „p. 4”, bij: ${vaag.join(', ')}.`);
    return resultaat(id, 'A', 'ok');
  };
}

/** Bij Inleiding, Methode en Resultaten is gekozen of de student het meeneemt (EV-12). */
export function imradMeenemen({ id, velden, labels, toegestaan = ['ja', 'deels', 'nee'] }) {
  return (invoer) => {
    const mist = velden.filter((v) => !toegestaan.includes([].concat(invoer?.[v] ?? [])[0])).map((v) => labels[velden.indexOf(v)]);
    if (mist.length > 0) return resultaat(id, 'A', 'mist', `Kies ${toegestaan.join(', ')} bij „Neem ik dit mee?” voor: ${mist.join(', ')}.`);
    return resultaat(id, 'A', 'ok');
  };
}

/** Is AI gebruikt om te ontleden, dan staat het controlevinkje (EV-12, B102). Geen keuze over AI: `mist`. */
export function aiGeverifieerd({ id, veld, aiVeld, waarde }) {
  return (invoer) => {
    const ai = [].concat(invoer?.[aiVeld] ?? [])[0];
    if (isLeeg(ai)) return resultaat(id, 'A', 'mist', 'Geef aan of je AI hebt gebruikt.');
    if (ai !== waarde) return resultaat(id, 'A', 'ok');
    if ([].concat(invoer?.[veld] ?? []).length === 0) {
      return resultaat(id, 'A', 'mist', 'Zoek elk citaat en elke vindplaats van de AI-tool zelf op in het artikel en zet het vinkje als je ze hebt teruggevonden.');
    }
    return resultaat(id, 'A', 'ok');
  };
}

/** De eerste ingevulde titel uit `ids` (eigen ander artikel gaat voor de bron uit 4.1), of ''. */
export const kiesTitel = (waarden, ids) => ids.map((id) => tekst(waarden?.[id])).find((t) => t !== '') ?? '';

/** De vaste prompt om een artikel met een AI-tool te ontleden (B102). */
export function artikelPrompt(titel) {
  return `Ik lees dit artikel: ${tekst(titel) || '[titel van je artikel]'}. `
    + 'Geef voor de Inleiding, de Methode en de Resultaten apart: (1) in één of twee zinnen wat de auteurs daar doen; '
    + '(2) één letterlijk citaat dat dat laat zien, met paginanummer. '
    + 'Bij de Inleiding: welke modellen, begrippen of definities gebruiken ze, en van wie komen die? '
    + 'Bij de Methode: hoe verzamelden en verwerkten ze de data? '
    + 'Bij de Resultaten: in welke vorm tonen ze de uitkomst (tabel, grafiek, model)? '
    + 'Verzin niets. Staat iets niet in het artikel, zeg dat dan.';
}
```

Vervang de export onderaan door:

```js
export const FABRIEKEN = {
  zoekOperator, termenPerBegrip, toolBijRouteB, promptZonderVerboden,
  bronGegevens, aaoccOordelen, aaoccToelichtingen, verificatieBijRouteB, apaFormaat, apaJaarGelijk, linkVorm, besluitGenomen,
  imradIngevuld, imradVindplaats, imradMeenemen, aiGeverifieerd,
};
```

Let op: `'H3'` en `'hoofdstuk 2'` matchen via `MET_GETAL` (`h` gevolgd door getal); `'pagina vier'` matcht niet (geen getal). Past een geval uit stap 1 niet, pas dan de regex aan, niet de test.

- [ ] **Step 4: Run.** `node --test tests/lb2.test.mjs 2>&1 | grep -E "^ℹ (pass|fail)"`. Verwacht: `fail 0`.
- [ ] **Step 5: Commit.**

```bash
cd A3L && git add js/checks/lb2.js tests/lb2.test.mjs
git commit -m "EV-12: controles voor het ontleden van een artikel (IMRAD), vindplaats en AI-vinkje (ADR B101, B102)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 2: Omzetting van de stelling (4.2 → 4.3)

**Files:**
- Create: `A3L/js/migratie.js`
- Modify: `A3L/js/leerblok.js` (in `start()`, direct nadat `store` is gemaakt en vóór de sessie wordt gemaakt; zoek `maakSessie(`)
- Test: `A3L/tests/migratie.test.mjs` (nieuw)

**Interfaces:**
- Consumes: `maakStore`, `geheugenOpslag` uit `js/store.js`; `maakRecord` uit `js/schema.js`.
- Produces: `zetStellingOm(store): boolean` (true als er iets is omgezet).

- [ ] **Step 1: Schrijf de falende test** `tests/migratie.test.mjs`:

```js
import test from 'node:test';
import assert from 'node:assert/strict';
import { maakStore, geheugenOpslag } from '../js/store.js';
import { maakRecord } from '../js/schema.js';
import { zetStellingOm } from '../js/migratie.js';

const ev5 = (taak) => maakRecord({
  taakdef: { id: 'EV-05', taak, leerblok: 2, luk: ['LUK 1'], bc: ['BC1'] },
  inhoud: { kant: 'voor', argument: 'Eén. Twee.' }, controles: [], status: 'compleet', versie: 1, bijgewerkt: '2026-10-01T10:00:00.000Z',
});

function oudeOpslag() {
  const store = maakStore(geheugenOpslag());
  store.save(ev5('4.2'));
  store.setMeta('klaar:4.2', { op: 'x' });
  store.setMeta('oefening:4.2', { invoer: { kant: 'tegen' }, overgeslagen: false, pogingen: 0 });
  store.setMeta('klaarals:4.2', [0]);
  store.setMeta('positie:2', { leerblok: 2, taak: '4.2', stap: 4, titel: 'Stelling' });
  return store;
}

test('B101: de stelling verhuist van 4.2 naar 4.3: record, klaar, oefening, klaar-als en positie', () => {
  const store = oudeOpslag();
  assert.equal(zetStellingOm(store), true);
  assert.equal(store.get('EV-05').taak, '4.3');
  assert.deepEqual(store.get('EV-05').inhoud, { kant: 'voor', argument: 'Eén. Twee.' });
  assert.deepEqual(store.getMeta('klaar:4.3'), { op: 'x' });
  assert.equal(store.getMeta('klaar:4.2'), undefined, 'de nieuwe taak 4.2 is niet klaar');
  assert.equal(store.getMeta('oefening:4.3').invoer.kant, 'tegen');
  assert.equal(store.getMeta('oefening:4.2'), undefined);
  assert.deepEqual(store.getMeta('klaarals:4.3'), [0]);
  assert.equal(store.getMeta('positie:2').taak, '4.3');
});

test('B101: de omzetting is idempotent en raakt een nieuwe opslag niet', () => {
  const store = oudeOpslag();
  zetStellingOm(store);
  const versies = store.versions('EV-05').length;
  assert.equal(zetStellingOm(store), false);
  assert.equal(store.versions('EV-05').length, versies);
  const leeg = maakStore(geheugenOpslag());
  assert.equal(zetStellingOm(leeg), false);
  const nieuw = maakStore(geheugenOpslag()); nieuw.save(ev5('4.3')); nieuw.setMeta('klaar:4.2', { op: 'y' });
  assert.equal(zetStellingOm(nieuw), false);
  assert.deepEqual(nieuw.getMeta('klaar:4.2'), { op: 'y' }, 'klaar van de nieuwe IMRAD-taak blijft staan');
});

test('B101: leerblok.js zet de stelling om voordat de sessie start', async () => {
  const { readFileSync } = await import('node:fs');
  const bron = readFileSync(new URL('../js/leerblok.js', import.meta.url), 'utf8');
  assert.ok(bron.indexOf('zetStellingOm(store)') > 0 && bron.indexOf('zetStellingOm(store)') < bron.indexOf('maakSessie('));
});
```

Controleer vooraf in `js/schema.js` of `maakRecord` de velden zoals hierboven verwacht (`taakdef`, `inhoud`, `controles`, `status`, `versie`, `bijgewerkt`); pas de hulpfunctie in de test aan op de echte handtekening als die afwijkt (zie `tests/sessie.test.mjs` voor een werkend voorbeeld). Controleer ook de echte `luk`/`bc`-waarden van EV-05 in `data/leerblok-2.json` en gebruik die.

- [ ] **Step 2: Run.** `node --test tests/migratie.test.mjs`. Verwacht: FAIL, module `../js/migratie.js` niet gevonden.
- [ ] **Step 3: Implementeer** `js/migratie.js`:

```js
// Eenmalige omzettingen van de opslag als de content verandert. Zuiver op de store; geen DOM.
//
// ADR B101: de stelling van leerblok 2 verhuisde van taak 4.2 naar 4.3; taak 4.2 is nu „Haal meer uit je artikel” (EV-12).
// Records hangen aan het bewijs-ID (EV-05), maar klaar, oefening, klaar-als, invoer en de positie hangen aan het taaknummer.
const OUD = '4.2';
const NIEUW = '4.3';
const PER_TAAK = ['klaar', 'oefening', 'klaarals', 'invoer'];

/** Zet een opslag van vóór B101 om. Alleen als EV-05 nog aan 4.2 hangt en er nog geen EV-12 is. Geeft true als er iets veranderde. */
export function zetStellingOm(store) {
  const ev5 = store.get('EV-05');
  if (!ev5 || ev5.taak !== OUD || store.get('EV-12')) return false;
  for (const soort of PER_TAAK) {
    const w = store.getMeta(`${soort}:${OUD}`);
    if (w === undefined) continue;
    if (store.getMeta(`${soort}:${NIEUW}`) === undefined) store.setMeta(`${soort}:${NIEUW}`, w);
    store.verwijderMeta(`${soort}:${OUD}`);
  }
  const positie = store.getMeta('positie:2');
  if (positie?.taak === OUD) store.setMeta('positie:2', { ...positie, taak: NIEUW });
  store.save({ ...ev5, taak: NIEUW });
  return true;
}
```

In `js/leerblok.js`: voeg bovenaan bij de imports `import { zetStellingOm } from './migratie.js';` toe, en in `start()` direct na de regel waar `store` wordt aangemaakt (zoek `maakStore(`) en vóór `maakSessie(`:

```js
  if (blok.leerblok === 2) zetStellingOm(store); // ADR B101: de stelling ging van 4.2 naar 4.3
```

Controleer dat `store` daar al bestaat; staat `maakSessie(` vóór het aanmaken van `store`, zet de regel dan direct na het aanmaken van `store`.

- [ ] **Step 4: Run.** `node --test tests/migratie.test.mjs && node --test 2>&1 | grep -E "^ℹ (pass|fail)"`. Verwacht: alles groen (de gewichtscontrole telt `migratie.js` mee; < 1 kB).
- [ ] **Step 5: Commit** `js/migratie.js js/leerblok.js tests/migratie.test.mjs` met bericht „B101: stelling van leerblok 2 omzetten van taak 4.2 naar 4.3”.

---

### Task 3: Weergave-onderdeel `artikelprompt`

**Files:**
- Modify: `A3L/js/lb2-ui.js` (commentaarblok bovenaan, import, `groepEl`)
- Test: `A3L/tests/weergave.test.mjs` of `A3L/tests/taakweergave.test.mjs` (bronteksttest, zoals die bestanden al doen)

**Interfaces:**
- Consumes: `artikelPrompt`, `kiesTitel` (taak 1).
- Produces: weergavegroep `{ artikelprompt: { titel: [veld-id, …] } }`: toont de prompt met de titel uit het eerste ingevulde veld (eigen veld of gespiegeld veld) en een knop „Kopieer de prompt”.

- [ ] **Step 1: Falende test** (bronteksttest; de DOM wordt in deze repo niet in Node getest). Voeg toe aan `tests/taakweergave.test.mjs`:

```js
test('B102: lb2-ui kent de groep artikelprompt: titel uit het eerste ingevulde veld, met kopieerknop', () => {
  const bron = readFileSync(resolve(root, 'js/lb2-ui.js'), 'utf8');
  assert.match(bron, /import \{[^}]*artikelPrompt[^}]*kiesTitel[^}]*\} from '\.\/checks\/lb2\.js'/);
  assert.match(bron, /if \(g\.artikelprompt\) doos\.append\(artikelPromptEl\(g\.artikelprompt\)\)/);
  assert.match(bron, /'Kopieer de prompt'/);
});
```

(Gebruik de `readFileSync`/`resolve`/`root` die in dat testbestand al bestaan; voeg ze toe zoals in `tests/lb2.test.mjs` als ze ontbreken.)

- [ ] **Step 2: Run** → FAIL.
- [ ] **Step 3: Implementeer** in `js/lb2-ui.js`:
  - Commentaarblok: voeg onder de regel van `promptgenerator?` toe:
    `//            artikelprompt?: { titel: [id] }      vaste prompt om een artikel met AI te ontleden, titel uit het eerste ingevulde veld (B102)`
  - Import: `import { bouwPrompt, verbodenWoorden, artikelPrompt, kiesTitel } from './checks/lb2.js';`
  - Binnen `bouwWeergave`, na de functie `promptEl`:

```js
  // B102: de vaste prompt bij taak 4.2. De titel komt uit een eigen veld of uit de spiegel van 4.1 (via lees()).
  function artikelPromptEl(a) {
    const tekstEl = h('p', { class: 'lb2-prompt' });
    const toon = () => { tekstEl.textContent = artikelPrompt(kiesTitel(lees(), a.titel)); };
    verversers.push(toon);
    const status = h('span', { class: 'klein', role: 'status' });
    const knop = h('button', { type: 'button', class: 'knop', onclick: async () => {
      try { await navigator.clipboard.writeText(tekstEl.textContent); status.textContent = ' Gekopieerd.'; }
      catch (e) { status.textContent = ' Kopiëren lukt hier niet; selecteer de tekst en kopieer hem zelf.'; }
    } }, 'Kopieer de prompt');
    return h('div', { class: 'lb2-generator' }, tekstEl, h('div', { class: 'lb2-generator-acties' }, knop, status));
  }
```

  - In `groepEl`, direct na `if (g.promptgenerator) doos.append(promptEl(g));`:
    `      if (g.artikelprompt) doos.append(artikelPromptEl(g.artikelprompt));`
  - `lees` is een `const` die later in `bouwWeergave` wordt gedefinieerd; `toon` roept hem pas aan via `verversers` (na de definitie). Controleer dat de eerste aanroep van `verversers.forEach` ná `const lees = …` staat (regel „het raster tekent de beginwaarden”); zo niet, roep `toon()` daar aan.
  - Spiegelwijzigingen (bewerken in 4.1) roepen `melding()` aan via `bron.luisteraars`; `melding` draait `verversers`, dus de prompt ververst mee.
  - Voeg in `css/site.css` bij de `lb2-generator`-regels toe: `.lb2-prompt { font-family:var(--fm); font-size:.875rem; background:var(--wit); border:2px solid var(--zwart); padding:.5rem; overflow-wrap:anywhere; }`

- [ ] **Step 4: Run** `node --test 2>&1 | grep -E "^ℹ (pass|fail)"` → groen (contrastcontrole: alleen tokens gebruikt).
- [ ] **Step 5: Commit** `js/lb2-ui.js css/site.css tests/taakweergave.test.mjs`, bericht „B102: vaste AI-prompt bij het ontleden van een artikel”.

---

### Task 4: Figuren van leerblok 2 (IMRAD en de twee mini-artikelen)

**Files:**
- Create: `A3L/js/figuren-lb2.js`
- Modify: `A3L/js/leerblok.js` (constante `FIGUREN_LB2`, dynamische import met `// gewicht-alleen: figurenlb2`, en `bouw({ met, taak })` bij oefening en stof)
- Modify: `A3L/tools/gewicht-check.mjs` (voorwaarde `figurenlb2`)
- Modify: `A3L/tools/content-check.mjs` (`FIGUUR_NAMEN` + controle op `oefening.artikelen`)
- Modify: `A3L/css/site.css` (stijl mini-artikel)
- Test: `A3L/tests/beeld.test.mjs`, `A3L/tests/gewicht.test.mjs`

**Interfaces:**
- Produces: `FIGUREN = { imrad: { bouw, na: 0 }, miniartikelen: { bouw, na: 0 } }` met `bouw({ met, taak })`.
- Dataformaat (taak 5 vult het): `taak.oefening.artikelen = [{ kop, citatie, secties: [{ kop, tekst }], grafiek? }]`, `grafiek = { titel, eenheid, rijen: [[label, getal]], laagste?: label }`.
- De IMRAD-figuur leest geen data; de vier delen en teksten staan in de module (zoals `VPC_VAKKEN` in figuren-lb3.js).

- [ ] **Step 1: Falende tests.** In `tests/beeld.test.mjs` (gebruik de helpers `lees`/`blok` die er al staan):

```js
test('B101 en SX-15: IMRAD staat als eigen figuur in de stof van 4.2: vier delen, zandloper, tekstalternatief, geen afbeelding van buiten', async () => {
  const bron = lees('js/figuren-lb2.js');
  assert.match(bron, /export const FIGUREN = \{ imrad: \{ bouw: imradFiguur, na: 0 \}, miniartikelen: \{ bouw: miniArtikelen, na: 0 \} \}/);
  for (const d of ['Inleiding', 'Methode', 'Resultaten', 'Discussie']) assert.match(bron, new RegExp(d));
  for (const d of ['theorie', 'methode', 'presentatie']) assert.match(bron, new RegExp(d));
  assert.match(bron, /role: 'img'/);
  assert.doesNotMatch(bron, /<img|src:/, 'eigen SVG, geen overgenomen figuur (lits/ blijft buiten)');
  assert.equal(blok(2).taken.find((t) => t.id === '4.2').stof.figuur, 'imrad');
  assert.equal(blok(2).taken.find((t) => t.id === '4.2').oefening.figuur, 'miniartikelen');
});
```

In `tests/gewicht.test.mjs`, in de test „leerblok.js laadt … dynamisch”, voeg toe:

```js
  assert.match(bron, /\/\/ gewicht-alleen: figurenlb2\n.*await import\('\.\/figuren-lb2\.js'\)/);
```

(De `blok(2)`-asserties falen tot taak 5; dat is de bedoeling. Zet in deze taak alleen de modules neer en controleer met de bronasserties; draai de `blok(2)`-regels opnieuw na taak 5.)

- [ ] **Step 2: Run** → FAIL.
- [ ] **Step 3: Implementeer** `js/figuren-lb2.js`:

```js
// De figuren van leerblok 2 (ADR B101): IMRAD als eigen zandloper (SX-15) en de twee fictieve mini-artikelen van de oefening bij
// taak 4.2. Alleen geladen op een pagina waarvan de data ze gebruikt (`// gewicht-alleen: figurenlb2` in leerblok.js, PF-4).
// De vorm van IMRAD volgt de bekende zandloper; niets is overgenomen uit Wu (2011), dat alleen geciteerd wordt.
import { h } from './dom.js';

const NS = 'http://www.w3.org/2000/svg';
const s = (tag, attrs = {}, ...kids) => {
  const el = document.createElementNS(NS, tag);
  for (const [k, v] of Object.entries(attrs)) el.setAttribute(k, v);
  for (const k of kids) el.append(k);
  return el;
};

/** De vier delen: naam, vraag van het deel, wat jij eruit haalt, en de vorm (breed→smal, smal, smal, smal→breed). */
export const IMRAD_DELEN = [
  ['Inleiding', 'Waarom dit onderzoek?', 'theorie: modellen, begrippen, definities', 'trechter'],
  ['Methode', 'Hoe precies?', 'methode: hoe data verzameld en verwerkt zijn', 'smal'],
  ['Resultaten', 'Wat gevonden?', 'presentatie: tabel, grafiek of model', 'smal'],
  ['Discussie', 'Wat betekent het?', 'betekenis en beperkingen', 'omgekeerd'],
];

const VORM = { trechter: '20,0 300,0 230,70 90,70', smal: '90,0 230,0 230,70 90,70', omgekeerd: '90,0 230,0 300,70 20,70' };

/** Figuur: de IMRAD-zandloper met per deel de vraag en wat jij eruit haalt (B101). */
export function imradFiguur({ met = (t) => t } = {}) {
  const svg = s('svg', { viewBox: '0 0 640 340', role: 'img', 'aria-labelledby': 'imrad-titel imrad-uitleg', class: 'imrad' },
    s('title', { id: 'imrad-titel' }, 'IMRAD: de vier delen van een onderzoeksartikel'),
    s('desc', { id: 'imrad-uitleg' }, IMRAD_DELEN.map(([d, v, w]) => `${d}: ${v} Jij haalt eruit: ${w}.`).join(' ')));
  IMRAD_DELEN.forEach(([deel, vraag, wat, vorm], i) => {
    const g = s('g', { transform: `translate(0, ${i * 82 + 8})` },
      s('polygon', { points: VORM[vorm], style: `fill:${i < 3 ? 'var(--wit)' : 'var(--grijs)'}; stroke:var(--zwart); stroke-width:3` }),
      s('text', { x: 160, y: 32, 'text-anchor': 'middle', style: 'font:700 18px var(--f)' }, deel),
      s('text', { x: 160, y: 54, 'text-anchor': 'middle', style: 'font:14px var(--f)' }, vraag),
      s('text', { x: 330, y: 42, style: `font:700 15px var(--f); fill:${i < 3 ? 'var(--accent-donker)' : 'var(--grijs-tekst)'}` }, `→ ${wat}`));
    svg.append(g);
  });
  return h('figure', { class: 'a3-vel' }, svg,
    h('figcaption', {}, h('p', {}, 'Figuur: IMRAD. De Inleiding begint breed bij wat al bekend is en wordt smal bij de eigen vraag. De Discussie gaat van de eigen uitkomst weer naar het brede beeld. Naar ', met('(Wu, 2011)'), '.')));
}

/** Een staafdiagram uit `grafiek.rijen`, de laagste staaf in accent; de titel draagt de kernboodschap. */
function grafiekEl(gr) {
  const max = Math.max(...gr.rijen.map(([, w]) => w));
  const hoog = gr.rijen.length * 34 + 10;
  const svg = s('svg', { viewBox: `0 0 400 ${hoog}`, role: 'img', 'aria-label': `${gr.titel}. ${gr.rijen.map(([l, w]) => `${l} ${String(w).replace('.', ',')}`).join(', ')}.`, class: 'mini-grafiek' });
  gr.rijen.forEach(([label, w], i) => {
    const y = i * 34 + 6;
    svg.append(
      s('text', { x: 0, y: y + 18, style: 'font:13px var(--f)' }, label),
      s('rect', { x: 110, y, width: Math.round((w / max) * 240), height: 24, style: `fill:${label === gr.laagste ? 'var(--accent)' : 'var(--zwart)'}` }),
      s('text', { x: 116 + Math.round((w / max) * 240), y: y + 18, style: 'font:700 13px var(--f)' }, String(w).replace('.', ',')));
  });
  return h('figure', { class: 'mini-figuur' }, h('figcaption', {}, h('strong', {}, gr.titel), gr.eenheid ? ` (${gr.eenheid})` : ''), svg);
}

/** De twee fictieve mini-artikelen van de oefening bij 4.2, naast elkaar op breed scherm, onder elkaar op de telefoon. */
export function miniArtikelen({ met = (t) => t, taak } = {}) {
  const artikelen = taak?.oefening?.artikelen ?? [];
  return h('div', { class: 'mini-artikelen' }, artikelen.map((a, n) => h('article', { class: 'mini-artikel', 'aria-labelledby': `mini-${n + 1}` },
    h('p', { class: 'klein fictief' }, 'Verzonnen artikel voor deze oefening'),
    h('h5', { id: `mini-${n + 1}` }, `Artikel ${n + 1} · `, a.kop),
    h('p', { class: 'klein' }, met(`(${a.citatie})`)),
    a.secties.map((sec) => [h('h6', {}, sec.kop), h('p', {}, met(sec.tekst)), sec.kop === 'Resultaten' && a.grafiek ? grafiekEl(a.grafiek) : null]))));
}

/** Na welke alinea van de stof een figuur staat (0 = de eerste). */
export const FIGUREN = { imrad: { bouw: imradFiguur, na: 0 }, miniartikelen: { bouw: miniArtikelen, na: 0 } };
```

In `js/leerblok.js`:
- Onder `const FIGUREN_LB3 = …`: `const FIGUREN_LB2 = ['imrad', 'miniartikelen'];`
- Na het `figurenlb1`-blok:

```js
  // gewicht-alleen: figurenlb2
  if (FIGUREN_LB2.some((n) => figuren.has(n))) Object.assign(FIGUREN, (await import('./figuren-lb2.js')).FIGUREN);
```

- Regel ~239: `FIGUREN[s3.oefening.figuur]?.bouw({ met }) ?? null,` → `FIGUREN[s3.oefening.figuur]?.bouw({ met, taak }) ?? null,` (de bestaande figuren negeren `taak`).

In `tools/gewicht-check.mjs`, naast de regel voor `figurenlb3`:

```js
    if (naam === 'figurenlb2') return ['imrad', 'miniartikelen'].some((n) => figuren.has(n));
```

en vul het commentaar op regel 11 aan met `figurenlb2`.

In `tools/content-check.mjs`:
- `FIGUUR_NAMEN` krijgt `'imrad', 'miniartikelen'`.
- Na de regel met `oefening.figuur … is onbekend`:

```js
    // B101: de mini-artikelen van de oefening bij 4.2: twee artikelen, elk met de vier IMRAD-secties in volgorde en een citatie.
    if (taak.oefening?.figuur === 'miniartikelen') {
      const art = taak.oefening.artikelen;
      if (!Array.isArray(art) || art.length !== 2) fout(wie, 'oefening.artikelen moet twee mini-artikelen hebben (B101)');
      else for (const [i, a] of art.entries()) {
        if (!gevuld(a?.kop) || !gevuld(a?.citatie)) fout(wie, `mini-artikel ${i + 1} mist kop of citatie`);
        const koppen = (a?.secties ?? []).map((x) => x?.kop);
        if (JSON.stringify(koppen) !== JSON.stringify(['Inleiding', 'Methode', 'Resultaten', 'Discussie'])) fout(wie, `mini-artikel ${i + 1} heeft niet de secties Inleiding, Methode, Resultaten, Discussie`);
        if ((a?.secties ?? []).some((x) => !gevuld(x?.tekst))) fout(wie, `mini-artikel ${i + 1} heeft een lege sectie`);
        if (a?.grafiek && !(gevuld(a.grafiek.titel) && Array.isArray(a.grafiek.rijen) && a.grafiek.rijen.every(([l, w]) => gevuld(l) && Number.isFinite(w)))) fout(wie, `de grafiek van mini-artikel ${i + 1} is onvolledig`);
      }
    }
```

In `css/site.css` (bij `.a3-vel`):

```css
.imrad { display:block; width:100%; height:auto; }
.mini-artikelen { display:grid; gap:1rem; grid-template-columns:repeat(auto-fit, minmax(16rem, 1fr)); margin:1rem 0; }
.mini-artikel { border:var(--rand) solid var(--zwart); background:var(--wit); padding:.75rem 1rem; font-size:.9375rem; }
.mini-artikel h5 { margin:.25rem 0; } .mini-artikel h6 { margin:.75rem 0 .25rem; font-size:.9375rem; }
.mini-artikel .fictief { font-weight:700; color:var(--grijs-tekst); margin:0; }
.mini-figuur { margin:.5rem 0; } .mini-grafiek { display:block; width:100%; height:auto; }
```

- [ ] **Step 4: Run** `node --test tests/gewicht.test.mjs` (groen) en `node --test tests/beeld.test.mjs` (alleen de `blok(2)`-regels falen nog: taak 5).
- [ ] **Step 5: Commit** `js/figuren-lb2.js js/leerblok.js tools/gewicht-check.mjs tools/content-check.mjs css/site.css tests/beeld.test.mjs tests/gewicht.test.mjs`, bericht „B101: IMRAD-figuur en mini-artikelen voor leerblok 2 (figuren-lb2.js, lui geladen)”.

---

### Task 5: Content van leerblok 2 en alle registers

Dit is één taak, omdat de tests pas weer groen worden als data, registers en tests samen kloppen.

**Files:**
- Modify: `A3L/data/leerblok-2.json` (titel, `eindigtMet`, 4.1, nieuwe 4.2, stelling → 4.3, `bewijsonderdelen`)
- Modify: `A3L/data/bronnen-2.json` (Wu 2011, Oliver 1980, fictief Visser & El Amrani 2021)
- Modify: `A3L/data/luk.json`, `A3L/data/leerblokken.json`, `A3L/data/terugblik.json`, `A3L/data/docent-deel1.json`
- Modify tests: `tests/lb2.test.mjs`, `tests/beeld.test.mjs`, `tests/docent.test.mjs`, `tests/dossier.test.mjs`, `tests/lb4.test.mjs`, `tests/terugblik.test.mjs`, `tests/afdruk.test.mjs`, en de fixtures die `leerblokken.json`/dossiers spiegelen (`tests/fixtures/*/leerblokken.json`, `tests/fixtures/maak-dossiers.mjs` en de dossiers die het maakt)

**Interfaces:**
- Consumes: fabrieken uit taak 1, `artikelprompt` uit taak 3, figuren uit taak 4.
- Produces: taak `4.2` met bewijs `EV-12`; taak `4.3` met bewijs `EV-05`.

- [ ] **Step 1: Leerblok.** In `data/leerblok-2.json`: `"titel": "Zoeken, beoordelen en gebruiken"`, `"eindigtMet": "Een beoordeeld en ontleed artikel"`.

- [ ] **Step 2: Taak 4.1.** Voeg in `toepassing.velden` direct na `b1link` toe:

```json
{ "id": "b1soort", "label": "Soort bron", "type": "keuze", "opties": ["onderzoeksartikel", "vakartikel", "anders"] }
```

Zet `b1soort` in de weergavegroep van bron 1 direct na `b1link` (zoek de groep met `b1link` in `toepassing.weergave`). Voeg aan `stof.alineas` als laatste alinea toe: `"Kies voor taak 4.2 een onderzoeksartikel: een artikel met een methode en resultaten."` Geen controle op `b1soort` (telt niet mee voor EV-04).

- [ ] **Step 3: Stelling → 4.3.** In het takenobject met `"id": "4.2"` (de stelling): `"id": "4.3"`; titel `"Stelling: \"Je kunt een artikel prima door AI laten ontleden.\""`; `waarom.tekst`: `"Studenten laten artikelen steeds vaker door AI samenvatten. Je hebt dat net zelf gedaan of juist niet. Als je een kant kiest en die onderbouwt, merk je wat jij ervan vindt en waarop dat rust."`, `waarom.bron`: `"concept-auteur"`. Pas de hint van het veld `kant` aan: `hintBron` wordt `[{"soort": "eigen werk", "vindplaats": "je ervaring bij taak 4.2, met of zonder AI"}, {"soort": "stof", "taak": "4.2", "vindplaats": "alinea 3"}]`. In `bewijsonderdelen`: `{ "id": "EV-05", "taak": "4.3", … }`. Zoek in de hele taak naar `4.2` en vervang verwijzingen naar zichzelf door `4.3`. Verplaats het object naar het einde van `taken`.

- [ ] **Step 4: Nieuwe taak 4.2** tussen 4.1 en 4.3. Kopieer de vaste sleutels (`luk`, `bc`, `bron`-velden) van taak 4.1 als sjabloon; inhoud:

```json
{
  "id": "4.2",
  "titel": "Haal meer uit je artikel",
  "vorm": "Duo, dan alleen",
  "bewijsonderdeel": "EV-12",
  "richttijd": { "tekst": "15 min", "minuten": 15, "bron": "concept-auteur" },
  "waarom": { "tekst": "Een artikel vertelt je wat er bekend is. Maar je kunt er meer uit halen: een begrip voor je analyse, een manier om data te verzamelen en een manier om je uitkomst te laten zien. IMRAD wijst je waar je dat vindt.", "bron": "concept-auteur" },
  "klaarAls": {
    "tekst": "je bij Inleiding, Methode en Resultaten van je artikel hebt opgeschreven wat de auteur doet, waar dat staat en of je het meeneemt, en in een korte alinea hebt opgeschreven wat je meeneemt naar je A3.",
    "bron": "concept-auteur",
    "criteria": [
      { "tekst": "bij Inleiding, Methode en Resultaten van je artikel hebt opgeschreven wat de auteur doet, waar dat staat en of je het meeneemt", "controles": ["imr-ingevuld", "imr-vindplaats", "imr-meenemen", "ai-geverifieerd"] },
      { "tekst": "in een korte alinea hebt opgeschreven wat je meeneemt naar je A3", "controles": ["oogst-gevuld", "oogst-zinnen"] }
    ]
  },
  "stof": {
    "bron": "concept-auteur",
    "opmerking": "Door de bouwer geschreven. IMRAD naar Wu (2011), alleen geciteerd; de figuur is een eigen tekening (ADR B101).",
    "figuur": "imrad",
    "alineas": [
      "Bijna elk onderzoeksartikel heeft vier delen: Inleiding, Methode, Resultaten en Discussie. Samen heet dat IMRAD (Wu, 2011). Elk deel beantwoordt een eigen vraag. Daardoor weet je waar je moet zoeken.",
      "Lees een artikel niet van voor naar achter. Begin met de samenvatting. Kijk dan naar de figuren en tabellen. Lees daarna de methode, en pas dan de rest.",
      "Je mag een AI-tool laten helpen. Gebruik dan de prompt bij deze taak. Een AI-tool verzint soms een citaat of een methode. Zoek daarom alles wat hij zegt zelf op in het artikel. Schrijf bij elk antwoord de vindplaats op: de sectie of de pagina."
    ]
  },
  "oefening": { "…": "zie step 5" },
  "modelantwoord": { "…": "zie step 5" },
  "toepassing": { "…": "zie step 6" },
  "controles": [ "…zie step 7" ]
}
```

(`…` zijn hier alleen verwijzingen naar de volgende stappen; in het bestand komt de volledige inhoud uit steps 5–7.) Controleer bij het invullen welke sleutels de andere taken hebben (`luk`, `bc`, `lukOnderdelen` …) en neem die over met LUK 1 · Gebruikt en beoordeelt bronnen.

- [ ] **Step 5: Oefening en modelantwoord van 4.2.**

```json
"oefening": {
  "opdracht": { "tekst": "Werk met een medestudent. Hieronder staan twee korte artikelen over klanttevredenheid bij webshops. Ze zijn verzonnen voor deze oefening. Kies ieder één artikel en beantwoord de drie vragen. Vergelijk daarna samen: welk artikel levert jullie het meest op? Werk je alleen? Doe dan beide artikelen.", "bron": "concept-auteur" },
  "figuur": "miniartikelen",
  "modelNa": ["theorie", "methode", "presentatie", "vergelijking"],
  "artikelen": [
    {
      "kop": "Verwachting en ervaring bij online winkelen",
      "citatie": "Visser & El Amrani, 2021",
      "secties": [
        { "kop": "Inleiding", "tekst": "Waarom zijn klanten van webshops tevreden of juist niet? Wij gebruiken het disconfirmatiemodel (Oliver, 1980). Volgens dat model vergelijkt een klant wat hij verwachtte met wat hij ervaart. Is de ervaring beter dan de verwachting, dan is hij tevreden. Is ze slechter, dan is hij ontevreden. Klanttevredenheid is dus het oordeel na die vergelijking. Verwachtingen komen uit eerdere aankopen, reclame en verhalen van anderen. Onze vraag: welke verwachtingen van webshopklanten worden het vaakst niet waargemaakt?" },
        { "kop": "Methode", "tekst": "We spraken acht klanten van drie webshops. Ze vertelden over hun laatste aankoop." },
        { "kop": "Resultaten", "tekst": "De meeste klanten noemden de levertijd. Ze hadden levering binnen een dag verwacht. Ook het retourneren viel tegen. Over de prijs was bijna niemand ontevreden." },
        { "kop": "Discussie", "tekst": "Webshops kunnen beter sturen op verwachtingen: beloof alleen wat je waarmaakt. Met acht klanten weten we niet hoe vaak dit voorkomt." }
      ]
    },
    {
      "kop": "Klanttevredenheid in webwinkels: een enquête onder 1.200 klanten",
      "citatie": "Bakker & De Vries, 2016",
      "secties": [
        { "kop": "Inleiding", "tekst": "Webshops willen weten waar ze de klanttevredenheid het best kunnen verbeteren. Wij onderzochten welke onderdelen van een bestelling klanten het laagst waarderen." },
        { "kop": "Methode", "tekst": "We stuurden een online enquête naar klanten van vijf Nederlandse webshops, een week na hun bestelling. 1.200 klanten vulden hem in, een respons van 24 procent. Ze gaven een cijfer van 1 tot 10 voor vijf onderdelen. We berekenden per onderdeel het gemiddelde. Met een variantieanalyse toetsten we of de verschillen toeval kunnen zijn." },
        { "kop": "Resultaten", "tekst": "Retourneren krijgt het laagste cijfer, betalen het hoogste. De verschillen zijn geen toeval (figuur 1)." },
        { "kop": "Discussie", "tekst": "Webshops winnen het meest met een eenvoudiger retour. We vroegen niet waarom klanten een laag cijfer gaven. Daarvoor is ander onderzoek nodig." }
      ],
      "grafiek": { "titel": "Figuur 1. Retourneren scoort het laagst", "eenheid": "gemiddeld cijfer, n = 1.200", "laagste": "Retourneren", "rijen": [["Betalen", 8.4], ["Website", 7.9], ["Verpakking", 7.6], ["Levertijd", 6.8], ["Retourneren", 6.1]] }
    }
  ],
  "velden": [
    { "id": "artikel", "label": "Welk artikel neem jij?", "type": "keuze", "opties": ["Artikel 1 · Visser & El Amrani", "Artikel 2 · Bakker & De Vries"], "hint": "Neem het artikel dat je medestudent niet neemt. Dan kunnen jullie straks vergelijken.", "hintBron": [{ "soort": "stof", "taak": "4.2", "vindplaats": "alinea 1" }] },
    { "id": "theorie", "label": "Inleiding: waar komt de theorie vandaan?", "type": "tekst", "hint": "Zoek een model, een begrip of een definitie, en de auteur van wie het komt.", "hintBron": [{ "soort": "stof", "taak": "4.2", "vindplaats": "figuur en alinea 1" }] },
    { "id": "theorieWaar", "label": "Vindplaats", "type": "lijst", "opties": ["Inleiding", "Methode", "Resultaten", "Discussie"], "hint": "In welk deel van het artikel zag je dit staan?", "hintBron": [{ "soort": "stof", "taak": "4.2", "vindplaats": "figuur" }] },
    { "id": "methode", "label": "Methode: hoe zijn de data verzameld en verwerkt?", "type": "tekst", "hint": "Wie deden er mee, hoeveel, en wat deden de auteurs daarna met de antwoorden?", "hintBron": [{ "soort": "stof", "taak": "4.2", "vindplaats": "figuur en alinea 2" }] },
    { "id": "methodeWaar", "label": "Vindplaats", "type": "lijst", "opties": ["Inleiding", "Methode", "Resultaten", "Discussie"], "hint": "In welk deel van het artikel zag je dit staan?", "hintBron": [{ "soort": "stof", "taak": "4.2", "vindplaats": "figuur" }] },
    { "id": "presentatie", "label": "Resultaten: in welke vorm staat de uitkomst?", "type": "tekst", "hint": "Staat de uitkomst in lopende tekst, een tabel, een grafiek of een model? Wat valt je op?", "hintBron": [{ "soort": "stof", "taak": "4.2", "vindplaats": "figuur en alinea 2" }] },
    { "id": "presentatieWaar", "label": "Vindplaats", "type": "lijst", "opties": ["Inleiding", "Methode", "Resultaten", "Discussie"], "hint": "In welk deel van het artikel zag je dit staan?", "hintBron": [{ "soort": "stof", "taak": "4.2", "vindplaats": "figuur" }] },
    { "id": "vergelijking", "label": "Samen: welk artikel levert jullie het meest voor theorie, voor methode en voor presentatie?", "type": "lang", "zinstarter": "Voor theorie … ; voor methode … ; voor presentatie …", "hint": "Leg jullie antwoorden naast elkaar. Elk artikel is sterk in iets anders.", "hintBron": [{ "soort": "stof", "taak": "4.2", "vindplaats": "figuur" }] }
  ]
},
"modelantwoord": {
  "bron": "concept-auteur",
  "opmerking": "Door de bouwer geschreven bij de twee verzonnen mini-artikelen (ADR B101).",
  "velden": {
    "theorie": "Artikel 1: het disconfirmatiemodel van Oliver (1980), verwachting tegenover ervaring, met een eigen definitie van klanttevredenheid. Artikel 2: geen model; alleen de vraag welk onderdeel het laagst scoort.",
    "theorieWaar": "Inleiding",
    "methode": "Artikel 1: acht gesprekken met klanten, zonder uitleg hoe die zijn verwerkt. Artikel 2: een enquête onder 1.200 klanten van vijf webshops, gemiddelden per onderdeel en een variantieanalyse.",
    "methodeWaar": "Methode",
    "presentatie": "Artikel 1: alleen lopende tekst. Artikel 2: een staafdiagram, gesorteerd van hoog naar laag, met de kernboodschap in de titel en de laagste staaf in kleur.",
    "presentatieWaar": "Resultaten",
    "vergelijking": "Voor theorie artikel 1: het model en de definitie kunnen we in onze analyse gebruiken. Voor methode artikel 2: een korte enquête met cijfers per onderdeel past ook bij ons vraagstuk. Voor presentatie artikel 2: één grafiek met de boodschap in de titel kunnen we op de A3 overnemen."
  }
}
```

Na het invullen: `node tools/content-check.mjs`. Meldt de controle dat een hint het modelantwoord verklapt (SX-13), herschrijf dan de hint, niet het modelantwoord.

- [ ] **Step 6: Toepassing van 4.2.**

```json
"toepassing": {
  "opdracht": { "tekst": "Ontleed nu je eigen artikel uit taak 4.1. Werk alleen. Schrijf bij elk deel op wat de auteur doet, waar dat staat en of je het meeneemt.", "bron": "concept-auteur" },
  "velden": [
    { "id": "b1titel", "label": "Titel (uit 4.1)", "type": "tekst", "afgeleidVan": "4.1" },
    { "id": "b1soort", "label": "Soort bron (uit 4.1)", "type": "tekst", "afgeleidVan": "4.1" },
    { "id": "anderArtikel", "label": "Ander artikel voor deze taak: auteur, jaar en titel (alleen als je bron uit 4.1 geen onderzoeksartikel is)", "type": "tekst" },
    { "id": "ai", "label": "Heb je AI gebruikt bij deze taak?", "type": "keuze", "opties": ["nee", "ja, om het te begrijpen", "ja, om het te ontleden"] },
    { "id": "aiCheck", "label": "Controle", "type": "meer", "opties": ["Ik heb elk citaat en elke vindplaats zelf in het artikel teruggevonden."] },
    { "id": "iWat", "label": "Wat doet de auteur in de Inleiding? Welke theorie, modellen of begrippen gebruikt hij, en van wie komen ze?", "type": "lang", "zinstarter": "De auteur bouwt op …" },
    { "id": "iWaar", "label": "Vindplaats (sectie of pagina)", "type": "tekst" },
    { "id": "iMee", "label": "Neem ik dit mee?", "type": "keuze", "opties": ["ja", "deels", "nee"] },
    { "id": "iWaarom", "label": "Waarom wel of niet?", "type": "tekst" },
    { "id": "mWat", "label": "Wat doet de auteur in de Methode? Hoe verzamelde en verwerkte hij de data?", "type": "lang", "zinstarter": "De auteurs verzamelden data door …" },
    { "id": "mWaar", "label": "Vindplaats (sectie of pagina)", "type": "tekst" },
    { "id": "mMee", "label": "Neem ik dit mee?", "type": "keuze", "opties": ["ja", "deels", "nee"] },
    { "id": "mWaarom", "label": "Waarom wel of niet?", "type": "tekst" },
    { "id": "rWat", "label": "Hoe toont de auteur de Resultaten? Tabel, grafiek, model of tekst, en wat valt op?", "type": "lang", "zinstarter": "De uitkomst staat in …" },
    { "id": "rWaar", "label": "Vindplaats (sectie of pagina)", "type": "tekst" },
    { "id": "rMee", "label": "Neem ik dit mee?", "type": "keuze", "opties": ["ja", "deels", "nee"] },
    { "id": "rWaarom", "label": "Waarom wel of niet?", "type": "tekst" },
    { "id": "oogst", "label": "Dit neem ik mee naar mijn A3: theorie, methode en presentatie samen", "type": "lang", "zinstarter": "Voor mijn A3 neem ik mee: …" }
  ],
  "weergave": {
    "groepen": [
      { "titel": "Je artikel (uit 4.1)", "afgeleidVan": "4.1", "kolommen": ["Titel", "Soort bron"], "velden": ["b1titel", "b1soort"], "hint": "Je vult dit in bij taak 4.1. Is het geen onderzoeksartikel, met een methode en resultaten? Kies dan een ander artikel uit 3.2 en vul het hieronder in." },
      { "velden": ["anderArtikel"] },
      { "titel": "AI", "velden": ["ai"] },
      { "titel": "Prompt voor de AI-tool", "alleenBij": { "veld": "ai", "waarde": "ja, om het te ontleden" }, "artikelprompt": { "titel": ["anderArtikel", "b1titel"] }, "velden": ["aiCheck"] },
      { "titel": "I · Inleiding: theorie", "velden": ["iWat", "iWaar", "iMee", "iWaarom"] },
      { "titel": "M · Methode: aanpak", "velden": ["mWat", "mWaar", "mMee", "mWaarom"] },
      { "titel": "R · Resultaten: presentatie", "velden": ["rWat", "rWaar", "rMee", "rWaarom"] },
      { "titel": "Dit neem ik mee naar mijn A3", "velden": ["oogst"] }
    ]
  }
}
```

- [ ] **Step 7: Controles van 4.2.**

```json
"controles": [
  { "id": "imr-ingevuld", "soort": "A", "type": "imradIngevuld", "velden": ["iWat", "mWat", "rWat"], "labels": ["Inleiding", "Methode", "Resultaten"] },
  { "id": "imr-vindplaats", "soort": "A", "type": "imradVindplaats", "velden": ["iWaar", "mWaar", "rWaar"], "labels": ["Inleiding", "Methode", "Resultaten"] },
  { "id": "imr-meenemen", "soort": "A", "type": "imradMeenemen", "velden": ["iMee", "mMee", "rMee"], "labels": ["Inleiding", "Methode", "Resultaten"] },
  { "id": "ai-geverifieerd", "soort": "A", "type": "aiGeverifieerd", "veld": "aiCheck", "aiVeld": "ai", "waarde": "ja, om het te ontleden" },
  { "id": "oogst-gevuld", "soort": "A", "type": "veldGevuld", "veld": "oogst", "label": "wat je meeneemt naar je A3" },
  { "id": "oogst-zinnen", "soort": "C", "type": "minZinnen", "veld": "oogst", "label": "wat je meeneemt naar je A3", "min": 3 }
]
```

Opmerking bij het spec (§4.6): het spec noemt de zinnencontrole soort B; de bestaande regel (BW-11) is dat tellen soort C is, en soort C op `let op` telt niet mee voor de status. Een te korte oogst geeft dus feedback maar houdt Compleet niet tegen; een lege oogst houdt hem wel tegen (`oogst-gevuld`, soort A). Leg dit vast in B101 (taak 7).

Voeg aan `bewijsonderdelen` toe (tussen EV-04 en EV-05): `{ "id": "EV-12", "taak": "4.2", "titel": "Ontleed artikel", "lukOnderdelen": ["LUK 1 · Gebruikt en beoordeelt bronnen"] }`.

- [ ] **Step 8: Bronnen.** In `data/bronnen-2.json`, op alfabetische plek (BR-1):

```json
{ "id": "oliver-1980", "citatie": "Oliver, 1980", "type": "artikel", "apa": "Oliver, R. L. (1980). A cognitive model of the antecedents and consequences of satisfaction decisions. *Journal of Marketing Research, 17*(4), 460–469.", "link": "https://doi.org/10.1177/002224378001700405" },
{ "id": "visser-el-amrani-2021", "citatie": "Visser & El Amrani, 2021", "type": "artikel", "fictief": true, "apa": "Visser, L. & El Amrani, S. (2021). Verwachting en ervaring bij online winkelen. *Tijdschrift voor Marketingonderzoek, 17*(2), 12–19. [Fictieve bron: verzonnen voor de oefening bij taak 4.2]" },
{ "id": "wu-2011", "citatie": "Wu, 2011", "type": "artikel", "apa": "Wu, J. (2011). Improving the writing of research papers: IMRAD and beyond. *Landscape Ecology, 26*(10), 1345–1349.", "link": "https://doi.org/10.1007/s10980-011-9674-3" }
```

Pas in de bestaande regel `bakker-de-vries-2016` de aanduiding aan naar `[Fictieve bron: verzonnen voor de oefeningen bij taak 4.1 en 4.2]`. Draai `node tools/link-check.mjs` (de twee DOI's moeten bestaan; meldt hij `onzeker`, controleer de DOI handmatig).

- [ ] **Step 9: Registers.**
  - `data/luk.json`: in `bewijsonderdelen` na EV-11: `{ "id": "EV-12", "titel": "Ontleed artikel" }`; in het onderdeel „LUK 1 · Gebruikt en beoordeelt bronnen”: `"bewijs": ["EV-03", "EV-04", "EV-12", "EV-05"]`.
  - `data/leerblokken.json`, leerblok 2: `"titel": "Zoeken, beoordelen en gebruiken"`, `"afgerondBewijs": "Een beoordeeld en ontleed artikel"`, `"bewijsonderdelen": ["EV-03", "EV-04", "EV-12", "EV-05"]`, `"el": "EL4, EL5, EL10"`.
  - `data/terugblik.json`, kaart `leerblok: 3`: voeg aan `items` toe `"De vier delen van IMRAD en wat je uit Inleiding, Methode en Resultaten haalt."` en `"Je ontlede artikel."`; voeg aan `kennisvragen` toe `"Noem de vier delen van IMRAD. Wat haal je uit de Inleiding, de Methode en de Resultaten?"`; vul `samenvatting.tekst` aan met: `" Daarna ontleedde je een onderzoeksartikel met IMRAD. Uit de Inleiding haalde je theorie, uit de Methode een aanpak en uit de Resultaten een manier van tonen."`
  - `data/docent-deel1.json`, onderdeel `d1-09`: `"taak": "4.3"`. Controleer of er een tekstveld is dat de stelling letterlijk noemt; laat de werkcollegetekst staan (het werkcollege houdt de oude stelling, B101).

- [ ] **Step 10: Tests bijwerken.** Draai `node --test 2>&1 | grep -B2 -A12 "✖"` en werk de vaste getallen bij. Verwachte wijzigingen:
  - `tests/lb2.test.mjs`: `blok.taken.length` 4 → 5; bewijsonderdelen `[['EV-03','3.2'],['EV-04','4.1'],['EV-12','4.2'],['EV-05','4.3']]`; de stellingtest (`taak('4.2')` → `taak('4.3')`); de LB-5/LB-7-weergavetest dekt nu ook 4.2 (afgeleide velden `b1titel`, `b1soort` moeten in 4.1 bestaan).
  - Nieuwe tests in `tests/lb2.test.mjs`:

```js
const EV12_GOED = {
  ai: 'nee', iWat: 'Bouwt op Oliver (1980).', iWaar: 'Inleiding', iMee: 'ja', iWaarom: 'Past bij onze analyse.',
  mWat: 'Enquête onder 300 klanten.', mWaar: 'p. 4', mMee: 'deels', mWaarom: 'Te groot voor ons.',
  rWat: 'Eén staafdiagram.', rWaar: 'Figuur 1', rMee: 'ja', rWaarom: 'Past op de A3.',
  oogst: 'Ik neem het model mee. Ik doe een kleine enquête. Ik toon de uitkomst in één grafiek.',
};
test('EV-12: volledig is Compleet; vage vindplaats Bijna; AI om te ontleden zonder vinkje Te doen; lege oogst Te doen', () => {
  const t = taak('4.2');
  assert.equal(status(t, EV12_GOED), 'compleet');
  assert.equal(status(t, { ...EV12_GOED, mWaar: 'ergens' }), 'bijna');
  assert.equal(status(t, { ...EV12_GOED, ai: 'ja, om het te ontleden' }), 'nog niet');
  assert.equal(status(t, { ...EV12_GOED, ai: 'ja, om het te ontleden', aiCheck: ['Ik heb elk citaat en elke vindplaats zelf in het artikel teruggevonden.'] }), 'compleet');
  assert.equal(status(t, { ...EV12_GOED, oogst: '' }), 'nog niet');
  assert.equal(status(t, { ...EV12_GOED, oogst: 'Alleen het model.' }), 'compleet', 'te kort: soort C, alleen feedback (BW-11)');
});
test('B101: de oefening van 4.2 toont het model pas na eigen werk, niet na alleen een artikelkeuze', () => {
  const t = taak('4.2');
  assert.equal(oefenModel(t, { invoer: { artikel: 'Artikel 1 · Visser & El Amrani' } }).modelZichtbaar, false);
  assert.equal(oefenModel(t, { invoer: { methode: 'acht gesprekken' } }).modelZichtbaar, true);
});
test('B101: richttijden van leerblok 2 zijn samen 45 minuten', () => {
  assert.deepEqual(blok.taken.map((t) => [t.id, t.richttijd.minuten]), [['3.1', 5], ['3.2', 10], ['4.1', 10], ['4.2', 15], ['4.3', 5]]);
});
```

  - `tests/beeld.test.mjs`: hintteller 60 → 68 (acht oefenvragen bij 4.2). Pas het commentaar aan: `// 4.2: acht oefenvragen bij de mini-artikelen (ADR B101); 3.2: acht (B100); 8.1: het TOM-bord en het niveau (B98)`.
  - `tests/dossier.test.mjs`, `tests/lb4.test.mjs`: aantal bewijsonderdelen 11 → 12; `ontbreekt`-lijsten krijgen `EV-12` op de plek die de volgorde uit `luk.json` geeft (draai de test en neem de volgorde over die de code geeft, mits EV-12 erin staat).
  - `tests/terugblik.test.mjs`: `EV`-tabel krijgt `'EV-12': ['4.2', 2]` en `'EV-05': ['4.3', 2]`; de verwachte `ontbrekend`-lijsten krijgen EV-12.
  - `tests/docent.test.mjs`: in de onderdelenlijst `'4.2'` → `'4.3'`; `stapkaartModel(… o.taak === '4.2')` → `'4.3'`.
  - `tests/afdruk.test.mjs`: werkboektaken eindigen op `'4.3'` in plaats van `'4.2'`.
  - Fixtures: `tests/fixtures/*/leerblokken.json` en `tests/fixtures/maak-dossiers.mjs` volgen dezelfde wijziging als `data/leerblokken.json`; draai daarna het script dat de dossiers maakt (zie de kop van `maak-dossiers.mjs`) zodat `tests/fixtures/dossiers/*.json` EV-05 op taak 4.3 hebben. Laat één fixture-dossier bewust op het oude nummer staan als de dossiertests import van oude dossiers testen; anders niet.
  - Hernoem in testnamen „4.2” naar „4.3” waar het over de stelling gaat.

- [ ] **Step 11: Run alles.** `node --test 2>&1 | grep -E "^ℹ (pass|fail)" && node tools/content-check.mjs | tail -1 && node tools/link-check.mjs | tail -1 && node tools/gewicht-check.mjs | grep -i "leerblok-2"`. Verwacht: `fail 0`, `content-check: ok`, `link-check: ok`, leerblok 2 onder beide grenzen.

- [ ] **Step 12: Taal.** Laat de nieuwe studentteksten (waarom, stof, opdrachten, mini-artikelen, hints, labels, modelantwoord, terugblik) door de skills `redigeer-nederlandse-tekst` en `schrap-ai-taal` gaan; pas aan in de JSON; draai step 11 opnieuw (`tests/taal.test.mjs` bewaakt de zinslengte).

- [ ] **Step 13: Commit** alle bestanden van deze taak met bericht „B101: leerblok 2 krijgt taak 4.2 Haal meer uit je artikel (EV-12); stelling naar 4.3”.

---

### Task 6: Doorloop in de browser en documentatie in de site

**Files:**
- Modify: `A3L/docs/docentgids.html`, `A3L/docs/dossierschema-1.0.html`, `A3L/docs/studentintroductie.html`, `A3L/README.md` (alleen waar leerblok 2 of de lijst bewijsonderdelen staat)
- Test: `A3L/tests/docs.test.mjs` (bestaande; draait mee)

- [ ] **Step 1: Docs.**
  - Docentgids: titel leerblok 2 → „Zoeken, beoordelen en gebruiken”; één zin: „Taak 4.2 (IMRAD) zit alleen in de e-learning, niet in het werkboek. De stelling in de e-learning (4.3) gaat over AI bij het ontleden van een artikel; in het werkcollege blijft de stelling over AI en inspiratiemateriaal.”
  - Dossierschema: EV-12 „Ontleed artikel” in de lijst met bewijsonderdelen, met de velden van taak 4.2.
  - Studentintroductie: alleen de titel van leerblok 2.
- [ ] **Step 2: Run** `node --test tests/docs.test.mjs` → groen.
- [ ] **Step 3: Doorloop.** Start `python3 -m http.server 8765` in A3L en open `http://localhost:8765/leerblok-2.html` (Playwright). Controleer en noteer:
  1. Stof 4.2 toont de IMRAD-figuur na alinea 1; op 360 px breed geen horizontale scroll (`document.documentElement.scrollWidth <= 360`).
  2. Oefening: twee mini-artikelen met het label „Verzonnen artikel”, grafiek met „Retourneren” in accent; artikelkeuze alleen toont geen model; na het invullen van `methode` verschijnt „Zo zou het kunnen”.
  3. Toepassing zonder 4.1: spiegeltabel met „—”; prompt met „[titel van je artikel]”. Vul in 4.1 een titel in: prompt toont die titel. Vul `anderArtikel` in: die gaat voor.
  4. AI „ja, om het te ontleden” toont de prompt en het vinkje; zonder vinkje status „Te doen”; met vinkje en alles ingevuld „Compleet”.
  5. Oude opslag: zet via de console `localStorage` met een EV-05-record op taak 4.2 en `klaar:4.2` (zie `tests/migratie.test.mjs` voor de vorm; prefix `a3l:`), herlaad: 4.3 klaar, 4.2 open.
  6. Geen fouten in de console.
- [ ] **Step 4: Commit** de docs, bericht „B101: docentgids, dossierschema en introductie bij leerblok 2”.

---

### Task 7: Ontwerpdocumenten (repository CC)

**Files:**
- Modify: `CC/docs/LRD-ELEARNING-A3.html`, `CC/docs/ADR-ELEARNING-A3.md`, `CC/docs/BLUEPRINT-ELEARNING-A3.md`, `CC/docs/BUILDPLAN-ELEARNING-A3.md`

- [ ] **Step 1: ADR** (onderaan, na B100):
  - **B101** · 1-10-2026 · 33 · Besluit: leerblok 2 heet „Zoeken, beoordelen en gebruiken” en krijgt taak 4.2 „Haal meer uit je artikel” (15 min, duo-oefening op twee fictieve mini-artikelen, toepassing alleen op het eigen artikel uit 4.1, IMRAD-figuur als eigen tekening naar Wu, 2011), met bewijs EV-12 (LUK 1 · Gebruikt en beoordeelt bronnen). De stelling wordt taak 4.3 met de tekst „Je kunt een artikel prima door AI laten ontleden” (EV-05); het werkcollege houdt de oude stelling. 4.1 krijgt het veld „Soort bron”. Opslag van vóór dit besluit wordt eenmalig omgezet (`js/migratie.js`). Een te korte oogst is soort C (BW-11) en geeft alleen feedback; het spec noemde soort B. Discussie krijgt geen eigen vraag. · Reden: op verzoek van de auteur: studenten leren een artikel te gebruiken als bron van theorie, methode en presentatie, verkleind uit een oefening van het afstudeertraject (drie artikelen → één; vier analyses → drie delen plus oogst). Afgewezen: (a) een eigen leerblok (programma wordt 5 × 45 min, sluit niet aan op week 5); (b) richttijd omhoog (strijdig met NFR-07); (c) beoordelen en ontleden in één taak (EV-04 verandert sterk, loopt niet gelijk met werkboek 4.1); (d) ontleden als verdieping (dan geen doel van het leerblok); (e) het team verdeelt artikelen en drie artikelen per student (te veel lees- en zoektijd); (f) in de oefening hetzelfde artikel voor beiden (dan zie je niet dat artikelen verschillend bruikbaar zijn); (g) ook werkboek en draaiboek (geen 15 minuten vrij in het werkcollege) · Verzoek van de auteur; spec 2026-10-01 · Aangenomen
  - **B102** · 1-10-2026 · 33 · Besluit: bij taak 4.2 mag AI helpen. De site geeft een vaste prompt die per IMRAD-deel om een samenvatting en een letterlijk citaat met paginanummer vraagt en zegt „verzin niets”. Bij elk deel noteert de student een vindplaats (sectie of pagina); de controle `imr-vindplaats` keurt vage plekken als *let op*. Wie AI gebruikte om te ontleden, zet het vinkje „Ik heb elk citaat en elke vindplaats zelf in het artikel teruggevonden” (anders Te doen). · Reden: studenten gaan dit met AI doen; de controle werkt met en zonder AI en sluit aan op de verificatievinkjes van 4.1. Afgewezen: eerst zelf, dan AI (dubbele tijd); AI alleen als leesmaatje (sluit niet aan op de praktijk) · Verzoek van de auteur · Aangenomen
- [ ] **Step 2: LRD** (versie 0.16 → 0.17 in de kop, met „0.17: artikel gebruiken (IMRAD)” in de versiereeks):
  - Leeruitkomsten: **EL10** „een onderzoeksartikel ontleden met IMRAD en eruit halen wat bruikbaar is voor het eigen onderzoek: theorie (modellen, begrippen, definities), methode (dataverzameling en -verwerking) en presentatie (vorm van de resultaten)”, met „zodat”-zin „de student een artikel gebruikt als meer dan een bron van kennis” en tag [Analyze / Conceptual]; de bundeling noemt leerblok 2 „Zoeken, beoordelen en gebruiken (EL4, EL5, EL10)”; de opmerking over oefencasus noemt EL10 bij de kennisdelen.
  - Bewijstabel: rij EV-12 (Ontleed artikel · LUK 1 · 4.2 · I, M en R met vindplaats en keuze, oogst · criteria uit taak 1 en 5); rij EV-05 → taak 4.3, oordeel over AI bij het ontleden van een artikel.
  - Requirements: **FR-70** „biedt in leerblok 2 taak 4.2: IMRAD als figuur, een duo-oefening op twee fictieve mini-artikelen met vergelijking, en een toepassing met per IMRAD-deel wat de auteur doet, de vindplaats en of de student het meeneemt, plus de oogst voor de A3 (EV-12)”; **FR-71** „biedt bij taak 4.2 een vaste AI-prompt en, bij AI-gebruik om te ontleden, een verplicht controlevinkje (B102)”; FR-14 → stelling over AI bij het ontleden van een artikel (taak 4.3).
  - NFR-07/programmatabel: leerblok 2 met 3.1 5, 3.2 10, 4.1 10, 4.2 15, 4.3 5.
  - Acceptatiecriteria: **AC-46** „Een vindplaats als ‚ergens vooraan’ geeft Bijna; ‚Methode’, ‚p. 4’ of ‚§ 3.2’ telt; AI om te ontleden zonder vinkje geeft Te doen (test)”; **AC-47** „Een opslag met de stelling op taak 4.2 wordt bij het laden omgezet naar 4.3 zonder verlies; de nieuwe taak 4.2 is open (test)”.
  - Risico's: „AI-citaten die niet kloppen” — mitigatie: vindplaats per deel, vinkje, stofalinea 3, stelling 4.3 laat de student erop reflecteren.
  - Terugblik (8.5): leerblok 3 noemt IMRAD en het ontlede artikel.
  - Bronnen: Wu (2011) en Oliver (1980).
- [ ] **Step 3: BLUEPRINT.**
  - LB-8 → „Leerblok 2 moet in taak 4.3 de stelling over AI bij het ontleden van een artikel bieden met een keuze en een argument (B101).”
  - Nieuw **LB-18** (Must): „Leerblok 2 moet in taak 4.2 IMRAD als figuur tonen en per deel Inleiding, Methode en Resultaten een antwoord, een vindplaats en een keuze over meenemen vragen, plus een oogst voor de A3.” · criterium „1 figuur met 4 delen; 3 × (antwoord, vindplaats, keuze); 1 oogstveld” · Test.
  - Nieuw **LB-19** (Must): „De oefening van taak 4.2 moet twee fictieve mini-artikelen bieden, elk met de vier IMRAD-secties, en een vergelijkingsveld voor het duo; het model verschijnt pas na eigen werk.” · „2 artikelen; 4 secties per artikel; 1 vergelijkingsveld; 0 modellen na alleen een artikelkeuze” · Test.
  - Nieuw **LB-20** (Should): „Bij taak 4.2 moet de site een vaste AI-prompt bieden en bij AI-gebruik om te ontleden een controlevinkje eisen.” · „1 prompt met titel; status Te doen zonder vinkje” · Test.
  - Nieuw **EV-12** in de bewijstabel: „Ontleedt een artikel (LUK 1) · 4.2 · Must · I, M en R elk met antwoord, vindplaats (sectie of pagina) en keuze; oogst ingevuld (≥ 3 zinnen als feedback); bij AI om te ontleden het vinkje · Test”. EV-05: taak 4.3.
  - Nieuw **RC-x** of in de bestaande opslagregels: „Bij het laden van leerblok 2 wordt opslag van vóór B101 omgezet (stelling 4.2 → 4.3) zonder verlies, idempotent.” Kies het eerstvolgende vrije nummer in die sectie.
  - Bijlage A: FR-70 → LB-18, LB-19, EV-12; FR-71 → LB-20; FR-14 → LB-8.
- [ ] **Step 4: BUILDPLAN.** Nieuwe sectie onderaan, vóór de bijlage: „## Aanvulling — Een artikel gebruiken (1-10-2026, op verzoek van de auteur)”, met afvinkregels voor taken 1–6 van dit plan, elk met wat een tester kan proberen (zie taak 6, step 3), en „Besluiten: ADR B101, B102”.
- [ ] **Step 5: Controle.** `grep -n "B101\|B102\|EV-12\|LB-18\|FR-70\|AC-46" CC/docs/*.md CC/docs/LRD-ELEARNING-A3.html | wc -l` > 10; open de LRD in de browser en kijk of de printstijl heel is.
- [ ] **Step 6: Commit** (alleen deze vier bestanden; let op: `ADR`, `BLUEPRINT` en `DESIGN` hadden al niet-gecommitte wijzigingen van B98–B100: vraag de auteur of die mee mogen of eerst apart), bericht „ADR B101, B102; LRD 0.17; LB-18–20, EV-12: een artikel gebruiken (IMRAD)”.
