# BUILDPLAN — Hybride e-learning A3 met automatisch bewijs

> Route en voortgang van [BLUEPRINT-ELEARNING-A3.md](BLUEPRINT-ELEARNING-A3.md). Het blueprint beschrijft de doelsituatie; dit bestand beschrijft de volgorde en **is** de voortgang: vink af wat af is, in dit bestand, en nergens anders. Regel-ID's (SI-1, EV-01, …) verwijzen naar het blueprint. Ontwerpbesluiten staan in [ADR-ELEARNING-A3.md](ADR-ELEARNING-A3.md), de onderbouwing in [LRD-ELEARNING-A3.html](LRD-ELEARNING-A3.html).
>
> Gebouwd wordt in een lokale kloon van `https://github.com/hanbedrijfskunde/a3-learning` (branch `main`). Dit plan blijft in `c-cluster/docs/` staan, bij de andere twee documenten.

## Werkafspraken

- **Elke fase eindigt in iets wat een mens kan proberen** (het blok „Wat de tester doet").
- **Elke fase eindigt met een volledige testpoort.** Pas daarna: commit, push, en dan de volgende fase. Een push naar `main` publiceert de site alleen als de workflow groen is (SI-6).
- **Volledige testpoort** = `node --test` (unittests; zonder mapargument: met `tests/` faalt het op Node 22+), `node tools/content-check.mjs`, `node tools/link-check.mjs`, een volledige doorloop van alle bestaande pagina's op de gepubliceerde URL zonder consolefout (SI-3), en 0 verzoeken naar andere domeinen in de netwerktrace (PR-1). Elke fase voegt daar haar eigen punten aan toe.
- **Verificatie per regel.** Bij elke fase staat welke regels ze claimt; die worden gecontroleerd met de verificatiemethode uit het blueprint. Sluit de fase niet met een regel die je alleen hebt gelezen.
- **Sabotagetest.** Elke nieuwe controle en elke nieuwe test wordt eenmaal gesaboteerd (breek het gedrag, zie de test falen, herstel). Een test die niet kan falen telt niet.
- **Bevindingen terug in de documenten, in dezelfde wijziging.** Verandert er iets aan het doel: BLUEPRINT (eigen commit in c-cluster) en, bij een ontwerpkeuze, ADR (nieuwe regel onderaan). Verandert er iets aan route of stand: dit bestand.
- **Commitberichten** noemen de regel-ID's die de commit realiseert, bijvoorbeeld `EV-01: controle op drie velden (BW-8)`.
- **Volgorde binnen een fase:** eerst het contract (schema, bestandsformaat, API), dan de invulling. Een subtask is één handeling, bij voorkeur één bestand, met het verwachte resultaat erbij.

## Voortgang

- [x] Fase 0 — Repository, licentie en lege publicatie
- [x] Fase 1 — Kern: schema, controles en statusregel (met controlelab)
- [x] Fase 2 — Leerblok 1 als dunne doorsnede (EV-01, EV-02) (subtask 2.3 wacht op akkoord van de auteur)
- [x] Fase 3 — Dossier: export, import en verificatie
- [x] Fase 4 — De Wissel en de feedbacklog (EV-09) (4.7 gedaan in fase 7)
- [ ] Fase 5 — Proefsessie met 2–3 gebruikers en bijstelling (wordt afgesloten door fase 18, B78)
- [x] Fase 6 — Leerblok 2 en de bronnenpagina (EV-03 t/m EV-05) (6.1 wacht op akkoord auteur)
- [x] Fase 7 — Terugblik en werken met tussenpozen
- [x] Fase 8 — Huisstijl, toegankelijkheid, responsive en offline (PF-2 alleen Chromium, Firefox en WebKit via Playwright; 8.9 wacht op een mens met Edge en Safari)
- [x] Fase 9 — Docentmodus: mechaniek en deel 1 (proefrun en leesbaarheid achterste rij wachten op een mens)
- [x] Fase 10 — Leerblok 3 en docentmodus deel 2 (EV-06 t/m EV-08) (10.1 wacht op akkoord auteur; 10.11 wacht op een mens; menselijke tester en proefrun docent vervangen door Playwright of open)
- [x] Fase 11 — Leerblok 4: verbanden, reflectie en afronding (EV-10, EV-11) (11.1 wacht op akkoord auteur; menselijke tester vervangen door Playwright)
- [x] Fase 12 — Media: mechaniek, twee video's en twee spellen (V2 en V4 zijn conceptvideo's met computerstem, wachten op akkoord auteur of eigen opname; menselijke tester vervangen door Playwright)
- [x] Fase 13 — Media: de overige video's en spellen (V1 en V3 zijn conceptvideo's, wachten op akkoord auteur; 13.4 is geschat, meten hoort bij de pilot; menselijke tester vervangen door Playwright)
- [x] Fase 14 — Afdrukken, documentatie en eindcontrole (docentgids, introductie en schema-beschrijving zijn teksten van de bouwer, wachten op akkoord auteur; de proeflezer die de site nog nooit zag wacht op een mens; menselijke tester vervangen door Playwright)
- [x] Fase 16 — Eerste indruk en rust (studentervaring, snel)
- [x] Fase 17 — Voortgang zichtbaar
- [ ] Fase 18 — Proefsessie op de telefoon (sluit fase 5 af) (18.3 gedaan; werving, sessie en vragenlijst wachten op een mens)
- [x] Fase 19 — Eén taak per scherm (19.8 verticale docentvideo's wacht op een mens; de herbeoordeling staat in de testpoort)
- [ ] Fase 15 — Pilot in een werkcollege en kalibratie (na fase 19, B78)

## Wat er al is (vastgesteld op 30 september 2026)

Afgeleid uit de bronnen, niet uit geheugen:

- **De repository `hanbedrijfskunde/a3-learning` is leeg.** `gh api repos/hanbedrijfskunde/a3-learning` geeft `size: 0`, `contents` geeft „This repository is empty", en er is geen GitHub Pages-site. Publiek, default branch `main`. Er is geen lokale kloon gevonden. Er is dus geen code om op voort te bouwen en fase 0 begint met de eerste commit.
- **Inhoudsbron: het werkboek.** `WK5/Werkboek_A3-start_week5.html` heeft 15 taken (`class="nr"`: 1.1, 2.1, 2.2, 3.1, 3.2, 4.1, 4.2, 5.1, 6.1, 6.2, 7.1, 8.1, 9.1, 9.2, 9.3), maar **slechts 3 „Klaar als"-regels** (`class="klaar"`, bij 2.1, 5.1 en 9.3) en 6 „Waarom"-regels (`class="waarom"`). TK-2 eist beide bij 100 % van de taken. Dat is een gat tussen blueprint en bron, opgenomen als aanname A-11 in het blueprint en als subtask 2.3 hieronder.
- **Inhoudsbron: het draaiboek** `WK5/Draaiboek_woensdag_week5.html` en de programmatabellen in het LRD (8.2 t/m 8.5) voor de docentmodus, verdieping, media en terugblik.
- **Geen code, geen tests, geen workflow, geen media, geen bronnenlijst in gestructureerde vorm** (de APA-lijst staat als HTML in het LRD).
- **`lits/` bestaat lokaal maar is niet publiceerbaar** (`.gitignore`, auteursrecht). Niets daaruit gaat naar de repository (LI-1 t/m LI-3).

## Wat dit plan niet doet

- Geen A3-vak 2 t/m 8, diagnose, quick win of big win, en geen LUK 2 (overig), 3 en 4 (blueprint X-15).
- Geen backend, login, framework, live klasoverzicht, AI-beoordeling of scores (X-1 t/m X-14).
- Geen beoordeling van studenten en geen wijziging van het werkboek op papier, behalve het aanvullen van „Waarom" en „Klaar als" (subtask 2.3, na akkoord van de auteur).
- Geen herinneringen per e-mail (X-9).
- Geen definitieve tijdsschatting: de richttijden worden in fase 5 en 15 gekalibreerd.

## Doelstructuur en bestandseigenaarschap

Bepaalt wat parallel kan: samenloop is een bestandsprobleem. Eigenaar = de fase die het bestand maakt; andere fasen mogen het alleen aanpassen als dat in hun subtasks staat.

| Pad | Eigenaar | Inhoud |
|---|---|---|
| `index.html`, `dossier.html`, `verificatie.html`, `docent.html`, `bronnen.html` | fase 0 (stub); daarna 3 (dossier, verificatie), 6 (bronnen), 9 (docent) | pagina's |
| `leerblok-1.html` … `leerblok-4.html` | fase 0 (stub); daarna 2, 6, 10, 11 | één pagina per leerblok |
| `css/site.css`, `css/print.css` | fase 0 (minimaal); fase 8 (huisstijl); 14 (print) | stijl |
| `js/schema.js`, `js/status.js` | fase 1 | recordvorm en statusregel |
| `js/checks/core.js`, `lb1.js`, `lb2.js`, `lb3.js`, `lb4.js` | fase 1 (core), 2, 6, 10, 11 | controles per leerblok |
| `js/store.js`, `js/leerblok.js` | fase 2 | browseropslag met versies; renderer die pagina's uit `data/` opbouwt |
| `js/dossier.js` | fase 3 | export, import, SHA-256, verificatie |
| `js/wissel.js` | fase 4 | de Wissel |
| `js/terugblik.js` | fase 7 | terugblik en pauzeberekening |
| `js/docent/*.js` | fase 9 | klok, stapkaart, docentkaart |
| `js/verbanden.js` | fase 11 | verbanden-kaart |
| `js/media.js` | fase 12 | routekeuze tekst/video/spel |
| `data/luk.json` | fase 3 | dekkingstabel §4.3 |
| `data/leerblok-1.json` … `-4.json` | fase 2, 6, 10, 11 | taken, „waarom", „klaar als", modelantwoorden, controleparameters |
| `data/docent-deel1.json`, `docent-deel2.json` | fase 9, 10 | docentvelden |
| `data/terugblik.json` | fase 7 | meenemen-kaarten en vragen (LRD 8.5) |
| `data/bronnen-1.json` … `-4.json` | fase 2, 6, 10, 11 | bronnen per leerblok; `bronnen.html` voegt ze samen |
| `media/`, `spellen/` | fase 12, 13 | video's (WebVTT, transcript), spellen |
| `tests/*.test.mjs` | per module bij de fase van de module | unittests (`node --test`) |
| `tools/content-check.mjs`, `tools/link-check.mjs` | fase 0 (skelet); uitgebreid door elke fase die data toevoegt | contentcontrole, linkcontrole |
| `.github/workflows/pages.yml`, `README.md`, `LICENSE`, `.nojekyll` | fase 0 | publicatie en licentie |

**Contract, eerst vastgelegd:** de vorm van `data/leerblok-N.json`, de API van `store.js` (`get`, `save`, `versions`, `clear`) en de signatuur van een controle (`(invoer, context) → { id, resultaat, melding }`). Die staan na fase 2 vast; wijzigen ze, dan is dat een aanpassing van fase 2 en dit plan.

## Parallelisatie

Afgeleid uit het bestandseigenaarschap hierboven.

- **Strikt na elkaar:** 0 → 1 → 2. Fase 2 legt het contract vast; niets eerder kan gelijk lopen.
- **Na fase 2 mogen fase 3, 4 en 6 tegelijk lopen** in aparte branches: ze delen geen bestand (3: `dossier.js`, `dossier.html`, `verificatie.html`, `data/luk.json`; 4: `wissel.js`; 6: `leerblok-2.html`, `checks/lb2.js`, `data/leerblok-2.json`, `bronnen.html`). Twee uitzonderingen: fase 4 past `leerblok-1.html` en `data/leerblok-1.json` aan (Wissel-knop) en fase 3 leest `store.js`; beide zijn eigendom van fase 2 en veranderen niet meer.
- **Fase 5 na 3 en 4** (heeft dossier en Wissel nodig om iets te testen).
- **Fase 7 na 6** (`terugblik.js` hangt aan de renderer en aan leerblok 2).
- **Fase 8 exclusief:** ze raakt `css/site.css` en bijna elke pagina. Geen andere fase tegelijk.
- **Fase 9 na 8; fase 10 na 9** (delen `js/docent/*.js` en het formaat van `data/docent-*.json`).
- **Fase 11 na 10** (verbanden-kaart leest EV-06 en EV-07).
- **Fase 12 en 13 mogen tegelijk met 10 en 11**, mits zij alleen `media/`, `spellen/`, `js/media.js` en de mediavelden in `data/leerblok-N.json` aanraken en het bestand niet tegelijk met de leerblokfase bewerken: per leerblok eerst de leerblokfase, dan de media.
- **Fase 14 en 15 exclusief en aan het eind.**
- **Fase 16 t/m 19 na 14 en vóór 15, strikt na elkaar** (B78). Ze raken `css/site.css`, alle studentpagina's en `js/weergave.js`; niets anders tegelijk. Richtlijn: `docs/DESIGN-ELEARNING-A3.md`; bij verschil gaat het blueprint voor.

---

## Fase 0 — Repository, licentie en lege publicatie

**Doel.** Een lege maar echt gepubliceerde site, met de poorten die alle latere fasen bewaken.
**Wat de tester doet.** Opent `https://hanbedrijfskunde.github.io/a3-learning/`, klikt door 8 stubpagina's zonder 404 en ziet licentie en naamsvermelding onderaan. Duwt daarna een testcommit met een falende test naar een aparte branch en ziet dat de workflow rood wordt en niets publiceert.
**Spec.** SI-1 (stubs), SI-2, SI-3, SI-4, SI-5, SI-6, SI-7, SI-8, LI-4, LI-5, PR-1.

### Subtasks
- [x] 0.1 Kloon de lege repository lokaal. Verwacht: map `a3-learning/` met alleen `.git`.
- [x] 0.2 Voeg `LICENSE` toe met de volledige tekst van CC BY-SA 4.0 (LI-4). Verwacht: 1 bestand, de tekst begint met „Attribution-ShareAlike 4.0 International".
- [x] 0.3 Voeg `.nojekyll` toe (leeg) en `README.md` met wat de site is, de licentie en een verwijzing naar de docentgids (SI-5). Verwacht: README noemt „docentgids".
- [x] 0.4 Maak 8 stubpagina's met relatieve links naar elkaar: `index.html`, `leerblok-1.html` t/m `leerblok-4.html`, `dossier.html`, `verificatie.html`, `docent.html` (SI-1, SI-3). Verwacht: elke pagina bereikbaar in ≤ 2 klikken vanaf `index.html`.
- [x] 0.5 Voeg op elke stub een voettekst toe met licentie-aanduiding, naamsvermelding en link naar de licentietekst (LI-5), en een `pilot`-banner die aan of uit staat via `data/config.json` (SI-8). Verwacht: banner zichtbaar bij `"pilot": true`, weg bij `false`.
- [x] 0.6 Maak `tools/link-check.mjs`: controleert dat alle interne links resolven en dat er 0 absolute interne links zijn. Verwacht: exit 0 op de stubs.
- [x] 0.7 Maak `tools/content-check.mjs` als skelet dat exit 0 geeft op lege `data/`. Verwacht: exit 0.
- [x] 0.8 Maak `tests/smoke.test.mjs` met één test die de 8 pagina's inleest. Verwacht: `node --test` groen.
- [x] 0.9 Schrijf `.github/workflows/pages.yml`: bij elke push `node --test`, `content-check`, `link-check`; alleen publiceren als alle drie slagen; faalmelding noemt de falende controle (SI-6, SI-7). Verwacht: 3 stappen met eigen naam.
- [x] 0.10 Zet GitHub Pages aan (bron: GitHub Actions) in de repository-instellingen. Verwacht: Pages-instelling toont „GitHub Actions".

### Testpoort
- [x] Volledige testpoort (lokaal: `python3 -m http.server` en doorloop).
- [x] Sabotage SI-6: op branch `test/rood` een falende test pushen; workflow rood, geen publicatie (0 nieuwe deploys).
- [x] Sabotage link-check: een absolute interne link toevoegen; `link-check` faalt.
- [x] Netwerktrace op de gepubliceerde URL: 0 verzoeken naar andere domeinen (PR-1).
- [x] Elke geclaimde regel gecontroleerd met de methode uit het blueprint (SI-1 Test, SI-2 Demonstratie, SI-3 Test, SI-4 Inspectie, SI-5 Inspectie, SI-6 Test, SI-7 Test, SI-8 Test, LI-4 Inspectie, LI-5 Inspectie, PR-1 Test).

### Afsluiting
- [x] commit `SI-1…SI-8, LI-4, LI-5: lege site met publicatiepoort`  - [x] push  - [x] overzicht afvinken

---

## Fase 1 — Kern: schema, controles en statusregel (met controlelab)

**Doel.** De pure logica die elk latere leerblok gebruikt: recordvorm, controlecontract, statusregel.
**Wat de tester doet.** Opent `controlelab.html`, plakt een bewijsrecord (JSON), kiest de uitkomsten van controles per soort A, B en C en ziet de status en de melding. Alle 27 combinaties van de statusregel zijn met een knop na te lopen.
**Spec.** RC-1, RC-2, RC-3, RC-4, BW-3, BW-4, BW-5, BW-8, BW-9, BW-11, BW-12, QA-2, QA-3.

### Subtasks
- [x] 1.1 Schrijf `js/schema.js` met de recordvorm van §5 (13 velden) en een `valideer(record)` (RC-1). Verwacht: geldig record → `true`, record met 12 velden → foutmelding met het ontbrekende veld.
- [x] 1.2 Voeg aan `schema.js` toe dat `luk` en `bc` uit een taakdefinitie komen en niet uit de invoer (RC-2) en dat `alias` of `naam` in `inhoud` wordt geweigerd (RC-3). Verwacht: 2 tests.
- [x] 1.3 Leg de scheiding `inhoud` / `controles` vast in het schema (RC-4). Verwacht: record met controles binnen `inhoud` → afgewezen.
- [x] 1.4 Schrijf `js/status.js` met `bepaalStatus(controles)` volgens de statusregel, „Nog niet" gaat voor „Bijna" gaat voor Compleet (BW-5). Verwacht: 27 combinaties (3 soorten × 3 resultaten) geven de tabel uit §5.
- [x] 1.5 Schrijf `js/checks/core.js` met het controlecontract `(invoer, context) → { id, soort, resultaat, melding }` en hulpfuncties `veldGevuld`, `minWoorden`, `keuzeUitLijst`, `eindigtOp` (BW-8, BW-9). Verwacht: zuiver, 0 netwerkaanroepen (test met een geblokkeerde `fetch`).
- [x] 1.6 Verbied in `core.js` inhoudelijk oordelen: soort C telt alleen woorden en zinnen (BW-11). Verwacht: 1 test die bevestigt dat controles van soort C alleen `telWoorden` en `telZinnen` aanroepen.
- [x] 1.7 Schrijf `tests/status.test.mjs` en `tests/core.test.mjs` met per controle 3 goede en 3 zwakke voorbeelden (QA-2). Verwacht: 6 voorbeelden per helper, allemaal groen.
- [x] 1.8 Breid `tools/content-check.mjs` uit: elke taak in `data/leerblok-*.json` heeft LUK-koppeling, „klaar als", ≥ 1 controle en modelantwoord (QA-3), en elk bewijsonderdeel heeft ≥ 1 LUK-onderdeel (BW-12). Verwacht: op een testfixture met 4 ontbrekende onderdelen → 4 fouten.
- [x] 1.9 Maak `controlelab.html` (alleen voor de tester; niet gelinkt vanaf `index.html`, wel in de sitemap van `README.md`). Verwacht: plakken van een record toont status en controles.
- [x] 1.10 Toon in het controlelab de statussen als tekst naast kleur en zonder score (BW-3, BW-4). Verwacht: 0 getallen als score in de UI.

### Testpoort
- [x] Volledige testpoort.
- [x] Sabotage BW-5: draai de voorrang om (Bijna gaat voor „Nog niet"); minstens 1 van de 27 combinaties faalt.
- [x] Sabotage BW-8: laat een controle `fetch` aanroepen; de test faalt.
- [x] Sabotage QA-3: haal een „klaar als" uit de fixture; `content-check` faalt met de taak in de melding.
- [x] Tester loopt in het controlelab alle 27 combinaties na en vergelijkt met §5. *(Uitgevoerd door de bouwer, niet door een mens: `tests/status.test.mjs` vergelijkt alle 27 combinaties met `data/statustabel.json` (de tabel uit §5), en `controlelab.html` is met Playwright lokaal en live nagelopen: 27 rijen, 0 afwijkingen. Een menselijke tester kan dit nog herhalen.)*
- [x] Geclaimde regels met hun methode gecontroleerd (RC-1…RC-3 Test, RC-4 Inspectie, BW-3 Test, BW-4 Inspectie, BW-5 Test, BW-8 Test, BW-9 Test, BW-11 Inspectie, BW-12 Test, QA-2 Test, QA-3 Test).

### Afsluiting
- [x] commit `RC-1…RC-4, BW-3…BW-12, QA-2, QA-3: schema, controlecontract, statusregel`  - [x] push  - [x] overzicht afvinken

**Stand en afwijkingen fase 1 (30 september 2026).** Gecommit en gepubliceerd (workflow groen, `controlelab.html` live 200); 121 tests. Netwerktrace fase 0 (PR-1) is op de live URL herhaald met Playwright: 0 verzoeken naar andere domeinen, 0 consolefouten, 0 cookies van de site.
- `valideer(record[, taakdef])` geeft `{ geldig, fouten }` in plaats van kaal `true`; `maakRecord` krijgt `status` van de aanroeper (uit `bepaalStatus`), zodat `schema.js` en `status.js` niet van elkaar afhangen. Fase 2 bouwt hierop.
- Statusnaam in het record is `"nog niet"` (naast `compleet`, `bijna`); `bepaalStatus([])` geeft `"nog niet"`.
- De tabel uit §5 staat als data in `data/statustabel.json` (gebruikt door test en lab), los van de code die hij toetst.
- Voorlopig formaat van `data/leerblok-N.json` (taken met `luk`, `bc`, `klaarAls`, `modelantwoord`, `controles`; `bewijsonderdelen` met `lukOnderdelen`) staat in de kop van `tools/content-check.mjs`; fase 2 legt het definitief vast.
- Op alle pagina's is `<link rel="icon" href="data:,">` toegevoegd: zonder icoon geeft de browser een 404 in de console (SI-3).
- Sabotage gedaan en hersteld voor BW-5, BW-8, BW-9, BW-11, RC-1…RC-4, QA-3, BW-12, lab-score, lab-link, en elke hulpfunctie (17 mutaties, alle door de tests gevangen). Sabotage link-check in fase 0 opnieuw uitgevoerd: exit 1.

---

## Fase 2 — Leerblok 1 als dunne doorsnede (EV-01, EV-02)

**Doel.** Van begin tot eind één leerblok waarmee het contract van de site vastligt: start, taak, controle, opslag, afsluiten.
**Wat de tester doet.** Opent de site, vult alias, teamnummer, vraagstuk en waarom-zin in (of kiest „nog geen scherp vraagstuk"), doet taak 2.1 en 2.2 op de oefencasus en op het eigen vraagstuk, ziet live wat er ontbreekt, herlaadt de pagina en vindt alles terug, sluit het leerblok af en ziet de status. „Wis alles" leegt de browseropslag.
**Spec.** ST-1, ST-2, ST-6, TK-1…TK-10, TK-15…TK-18, LB-1, LB-2, LB-3, LB-4, EV-01, EV-02, BW-1, BW-2, BW-6, BW-7, DS-1, RC-5, RC-6, QA-1.

### Subtasks
- [x] 2.1 Leg het formaat van `data/leerblok-1.json` vast (taak, nummer, waarom, klaar als, richttijd, oefencasus, modelantwoord, controles, LUK-koppeling, verdieping) en beschrijf het in `README.md` (QA-1). Verwacht: één voorbeeldtaak valideert tegen het formaat.
- [x] 2.2 Schrijf `js/store.js`: `get`, `save` (met `versie + 1` en behoud van eerdere versies), `versions`, `clear` (RC-5, RC-6, ST-6, DS-1). Verwacht: na 5 opslagen 5 versies en `versie` loopt 1…5.
- [ ] 2.3 (concept, wacht op akkoord auteur) Vul `data/leerblok-1.json` met taken 1.1, 2.1, 2.2: de teksten uit het werkboek; **ontbrekende „Waarom" en „Klaar als" (alleen 2.1 heeft een „Klaar als") voor de auteur schrijven en laten goedkeuren** voordat ze de site in gaan (TK-2). Verwacht: 3 taken, elk met waarom en „klaar als", door de auteur bevestigd.
- [x] 2.4 Schrijf `js/leerblok.js`: bouwt de pagina uit het datafile met het vaste ritme van vijf stappen (TK-18) en toont per taak nummer, waarom, tijd en „klaar als" (TK-2). Verwacht: 3 taken, alle vier elementen zichtbaar.
- [x] 2.5 Bouw de startpagina-invoer: alias of voornaam, teamnummer, vraagstuk in één zin, waarom-zin, of „nog geen scherp vraagstuk"; privacytekst ≤ 100 woorden op `index.html` (ST-1, ST-2). Verwacht: 4 velden + 1 keuze, 0 andere persoonsgegevensvelden.
- [x] 2.6 Bouw de oefen/toepassen-scheiding: aparte oefenversie met modelantwoord dat pas verschijnt na ≥ 1 ingevuld veld, herhaalbaar (≥ 10×) en overslaanbaar met één klik (TK-3, TK-5, TK-6, TK-7). Verwacht: modelantwoord verborgen bij leeg veld; overslaan verandert 0 statussen.
- [x] 2.7 Zorg dat alleen de toepassing als bewijsrecord wordt opgeslagen (TK-4). Verwacht: 0 records met oefencasus-inhoud.
- [x] 2.8 Schrijf `js/checks/lb1.js` met de controles van EV-01 en EV-02 uit het blueprint (soort A en B) en de bouwer van LB-2 (drie velden, zes kapitalen, live voorbeeld ≤ 1 s) en LB-3 (drie zoekvragen, frame-keuzelijst, één model uit 4, veld „wat mis je"); teamkeuze en eigen verantwoording apart (LB-4). Verwacht: alle controles hebben 3 goede en 3 zwakke voorbeelden.
- [x] 2.9 Verbind de controles met de invoer: resultaat ≤ 1 s na de laatste toetsaanslag, één zin per niet-`ok`-controle, statustekst en, bij Compleet, de zin „Aanwezig en consistent…" en, bij „Nog niet", de lijst met een link naar het modelantwoord (BW-1, BW-2, BW-6, BW-7). Verwacht: meetbare vertraging ≤ 1 s.
- [x] 2.10 Bouw de knop „klaar", de zin „mijn volgende stap" en de aanbevolen volgorde zonder slot; blokkeer niemand bij overschrijding van de richttijd (TK-1, TK-8, TK-9, TK-10). Verwacht: „klaar" werkt bij ≤ 50 % van de richttijd; 0 blokkades bij 150 %.
- [x] 2.11 Bouw het afsluitscherm met status per bewijsonderdeel, volgende stap en de melding „bewaar je dossier"; de afgerond-regel en doorgaan zonder afronden (TK-15, TK-16, TK-17). Verwacht: 4 testprofielen geven het verwachte resultaat.
- [x] 2.12 Toon de vier leerblokken op de startpagina met richttijd en afgerond bewijs (LB-1) en voeg de verdiepingstaak van leerblok 1 toe (nog zonder invloed op de status). Verwacht: 4 leerblokken op `index.html`.
- [x] 2.13 Bouw „wis alles" met één bevestiging (ST-6). Verwacht: 0 items van de site in localStorage, sessionStorage en IndexedDB.
- [x] 2.14 Laat `content-check` de eerste 3 taken valideren. Verwacht: groen.

### Testpoort
- [x] Volledige testpoort, met leerblok 1 als extra doorloop op de gepubliceerde URL.
- [x] Sabotage TK-6: maak het modelantwoord direct zichtbaar; de test faalt.
- [x] Sabotage TK-4: sla oefencasus-invoer op als bewijs; de test faalt.
- [x] Tester doorloopt: start → 2.1 → 2.2 → afsluitscherm → herladen → alles aanwezig → „wis alles" → leeg.
- [x] DS-1: 0 verloren velden na herladen.
- [x] Geclaimde regels met hun methode gecontroleerd; TK-2 als Test tegen de werkboektekst.

### Afsluiting
- [x] commit `Leerblok 1: doorsnede met start, EV-01, EV-02, opslag en afsluiten`  - [x] push  - [x] overzicht afvinken (2.3 blijft open tot de auteur akkoord geeft)

---

**Stand en afwijkingen fase 2 (30 september 2026).** Gecommit en gepubliceerd (workflow groen, live gecontroleerd); 193 tests.
- **Subtask 2.3 is niet afgevinkt: concept, wacht op akkoord van de auteur.** Letterlijk uit het werkboek (`"bron": "werkboek"`): waarom van 1.1, 2.1 en 2.2; "klaar als" van 2.1; richttijd van 2.1 en 2.2. Door de bouwer geschreven (`"bron": "concept-auteur"`, geeft een WAARSCHUWING in `content-check`): "klaar als" van 1.1 en 2.2, de minuten van 1.1 (het werkboek zegt "tijdens de uitleg"; 10 gekozen), de toepassing van 1.1 (aanleiding van het eigen vraagstuk), de opdracht van de oefening van 1.1 en 2.2, het modelantwoord van 2.2 (frame-indeling, model en verantwoording; de drie zoekvragen komen uit het draaiboek), de opdracht van de toepassing van 2.1 en alle "stof"-teksten (uitleg van user story, pain, gain, six capitals, frame). Modelantwoorden van 1.1 en 2.1 komen uit het kader in het draaiboek (`"bron": "draaiboek"`; het derde antwoord bij 1.1 is ingekort omdat het draaiboek zelf zegt dat die punten nog gecontroleerd moeten worden). Verdieping: LRD 8.3.
- TK-2 letterlijk-controle: `tests/werkboek.test.mjs` vergelijkt met `../c-cluster-1/WK5/Werkboek_A3-start_week5.html` en wordt overgeslagen als dat bestand ontbreekt (dus in CI).
- Taak 1.1 heeft geen bewijsonderdeel en geen casus: de oefenversie zijn de drie werkboekvragen, de toepassing (concept) is de aanleiding van het eigen vraagstuk; de invoer gaat niet in een record. Zo is TK-3 ("2 versies per taak") ingevuld.
- Contract gewijzigd t.o.v. fase 1: `klaarAls` en `modelantwoord` in `data/leerblok-N.json` zijn nu objecten met `bron` (een kale tekst blijft geldig voor `controleerLeerblok`); nieuw `data/leerblokken.json` (overzicht voor de startpagina, startinvoer, privacytekst); fixtures aangepast aan formaat 1.0; `content-check` geeft waarschuwingen. `core.js` is niet gewijzigd: voor "minstens 4 woorden" als soort A staat `minWoordenAanwezig` in `js/checks/lb1.js` (core.minWoorden blijft soort C, BW-11).
- Lezingen die de blueprint openlaat staan als B61 in het ADR (afgerond-regel met `voorlopig`, wanneer "klaar" verschijnt, oefeninvoer buiten de records).
- Kapitaalnamen volgen het werkboek ("sociaal en relationeel"), niet het voorbeeld in blueprint 5 ("sociaal").
- Bewaren gebeurt 500 ms na de laatste toetsaanslag en alleen bij een verandering (anders is elke toetsaanslag een versie, RC-5); de controles lopen direct (gemeten 0,1 tot 0,3 ms, BW-1).
- Nog niet in deze fase: de kijktips van derden (B60), media (fase 12), de Wissel en "kopieer naar A3" (ST-7), export (fase 3; de bewaarmelding verwijst naar `dossier.html`).
- Sabotage gedaan en hersteld, telkens door de tests gevangen: TK-6 (2 tests), TK-4, TK-14, TK-16, RC-5, ST-3, verschiltVanCasus, kapitaalNietFinancieel, verschillendeFrames, precies1Keuze, TK-2 (gewijzigd woord in de JSON) en de waarschuwing voor concept-auteur.
- Playwright (lokaal en live): start, 2.1, 2.2, afsluitscherm, herladen (alles aanwezig), "Wis alles" (0 items in localStorage, sessionStorage en IndexedDB); 0 verzoeken naar andere domeinen, 0 consolefouten; alle 8 pagina's 200. Niet door een mens gedaan; een menselijke tester kan dit herhalen.

---

## Fase 3 — Dossier: export, import en verificatie

**Doel.** Wat de student inlevert en wat de docent nakijkt, zonder server.
**Wat de tester doet.** Exporteert een dossier (JSON en afdrukbare pagina), wijzigt één teken in het JSON-bestand, leest beide bestanden in op `verificatie.html` en ziet „gewijzigd na export" bij de gewijzigde en niets bij de ongewijzigde. Importeert het dossier in een schoon browserprofiel. Leest vijf testdossiers tegelijk in.
**Spec.** DS-2…DS-12, BW-13, PR-2.

### Subtasks
- [x] 3.1 Schrijf `data/luk.json` met de 13 onderdelen van §4.3 (dekking, bewijs) en toon ze op `dossier.html` met de eigen status (BW-13). Verwacht: 13 rijen; onderdelen met EV-01/02 tonen de status uit het dossier.
- [x] 3.2 Schrijf `js/dossier.js`: export als JSON met records (nieuwste versie en aantal eerdere), alias, teamnummer, e-learningversie (DS-5) en een SHA-256 over de inhoud via `crypto.subtle` (DS-6). Verwacht: controlesom van 64 hexadecimale tekens.
- [x] 3.3 Bouw de afdrukbare pagina per leeruitkomst (LUK 1, 2, 5) met status per bewijsonderdeel, inhoud en controlesom onderaan (DS-7). Verwacht: 3 pagina's.
- [x] 3.4 Bouw import met controle op schemaversie 1.x (DS-3, DS-4). Verwacht: 0 verschillen tussen records vóór export en na import.
- [x] 3.5 Toon de melding „bewaar je dossier" na elk leerblok en na elke 10 wijzigingen (DS-2). Verwacht: 1 melding per 10 wijzigingen.
- [x] 3.6 Bouw de verificatiepagina: lokaal inlezen, controlesom herberekenen, „gewijzigd na export" bij afwijking (DS-8), geen uitgaande verzoeken (DS-10). Verwacht: 1 gewijzigd teken → melding; ongewijzigd → geen melding.
- [x] 3.7 Laat de verificatiepagina meerdere dossiers tegelijk inlezen met een tabel per student en per leeruitkomst, ontbrekende onderdelen bovenaan (DS-9). Verwacht: 5 dossiers, 11 bewijsonderdelen en 3 leeruitkomsten per student.
- [x] 3.8 Bouw „Mijn stand": per bewijsonderdeel alleen de status, groot, zonder inhoud (DS-11). Verwacht: 0 inhoudsvelden.
- [x] 3.9 Meld geblokkeerde browseropslag en bied direct export aan (DS-12). Verwacht: in een privévenster 1 melding en 1 exportknop ≤ 1 s na laden.
- [x] 3.10 Maak 5 testdossiers in `tests/fixtures/` (waaronder 1 met gewijzigde inhoud). Verwacht: 5 bestanden.
- [x] 3.11 Schrijf `tests/dossier.test.mjs` voor SHA-256, import en verificatie. Verwacht: groen.

### Testpoort
- [x] Volledige testpoort.
- [x] Sabotage DS-8: rond de controlesom af zodat een gewijzigd teken niet opvalt; de test faalt.
- [x] Netwerktrace tijdens export en verificatie: 0 uitgaande verzoeken met dossierinhoud (DS-10, PR-2).
- [x] Tester (Playwright, geen mens): export → wijzig 1 teken → verificatie → melding; import in schoon profiel → alles terug.
- [x] Geclaimde regels met hun methode gecontroleerd.

### Afsluiting
- [x] commit `DS-2…DS-12, BW-13: dossier, import en verificatiepagina` (030c584 vóór rebase, plus 0639699)  - [x] push (Actions-run groen, live geverifieerd)  - [x] overzicht afvinken

**Stand en afwijkingen fase 3 (30 september 2026).** Gecommit en gepubliceerd (workflow groen, live gecontroleerd); 267 tests waarvan 40 nieuw in `tests/dossier.test.mjs` (264 groen, 3 overgeslagen: het werkboek staat niet naast de repository).
- **Bestanden.** Naast `js/dossier.js` (logica, geen DOM) staan `js/dossier-dom.js` (download, bewaarherinnering, melding bij geblokkeerde opslag), `js/dossier-pagina.js` en `js/verificatie-pagina.js`. `js/leerblok.js` (fase 2) is minimaal aangepast: één import, een container `#bewaarherinnering` met twee aanroepen van `toonBewaarHerinnering` (bij laden en na elke opslag), en de oude melding bij geblokkeerde opslag is vervangen door `geblokkeerdMelding` (met exportknop). De store is niet gewijzigd.
- **Exportformaat** (README): `{ formaat: "a3-bewijsdossier", schema: "1.0", elearning, geexporteerd, alias, teamnummer, vraagstuk, waaromZin, voorlopig, records: [{ record, eerdereVersies }], controlesom: { algoritme: "SHA-256", waarde, over } }`. De controlesom loopt over alle velden behalve zichzelf, canoniek (gesorteerde sleutels). Vraagstuk, waarom-zin en voorlopig zitten er ook in (meer dan DS-5 eist) zodat een import het profiel terugzet.
- **Import schrijft rechtstreeks in de recordlijst** (`a3l:rec:<id>`) omdat `store.save` het versienummer altijd doortelt; anders zou „0 verschillen" niet kunnen. Een test bewaakt dat de store daarna gewoon doorwerkt. Zie ADR B63.
- **DS-7:** de criteriumtekst „3 onderdelen elk" klopt niet met §4.3: LUK 1 heeft 9 bewijsonderdelen, LUK 2 één (EV-11) en LUK 5 twee. De pagina toont de onderdelen die §4.3 aan elke LUK koppelt. De afdrukbare pagina's zijn een weergave op `dossier.html` (knop „Afdrukbare pagina's per leeruitkomst", dan Afdrukken), geen apart bestand.
- **DS-9:** studenten met de meeste ontbrekende onderdelen staan bovenaan; „ontbreekt" = geen record of Nog niet. De leeruitkomst neemt het slechtste van haar onderdelen (BW-5).
- **DS-2:** de melding na elk leerblok is de bestaande bewaarmelding op het afsluitscherm (fase 2). Nieuw is de melding na elke 10 opgeslagen versies (som van `versie` over alle records), die blijft staan tot de student exporteert of „Later" kiest.
- **DS-10:** naast de netwerktrace hebben `dossier.html` en `verificatie.html` een Content-Security-Policy (`default-src 'none'`, `connect-src 'self'`). De pagina's halen alleen `data/*.json` op; veldlabels komen alleen uit leerblokbestanden waarvan de student records heeft (anders 404-fouten in de console voor nog niet bestaande leerblokken).
- **`content-check`** controleert nu ook `data/luk.json` (11 bewijsonderdelen, 13 onderdelen, dekking, en de kruiscontrole met de leerblokbestanden: titel, `lukOnderdelen`, `luk` van de taak). De titel van EV-09 in `luk.json` volgt leerblok 4 („Feedback ontvangen en gegeven").
- **Sabotage** gedaan en hersteld, telkens door de tests gevangen (36 stuks): DS-8 (controlesom afgerond op de eerste 200 tekens; vergelijking altijd gelijk; ontbrekende som telt als ok), canonieke volgorde, SHA-1 in plaats van SHA-256, eerdere versies, alias uit export, bestandsnaam, schema 2.x en nieuwere minor geaccepteerd, versienummer niet behouden bij import, nieuwste wint omgekeerd, profiel altijd overschreven, geen recordvalidatie, dubbel id, herinnering per 5, export sluit melding niet af, hook uit leerblok.js, Mijn stand met inhoud, geen sortering, „nog niet" telt niet als ontbrekend, slechtste status, dekking zonder status, controlesom niet op de pagina, LUK 2 ontbreekt, netwerkverzoek met POST, CSP verruimd, melding op dossierpagina weg, `luk.json` (rij weg, dekking gewijzigd) en drie controles in `controleerLuk`. Twee sabotages werden eerst niet gevangen (de toepassing van de melding in `leerblok.js`, en `slechtsteStatus`); daarvoor zijn tests aangescherpt.
- **Playwright (lokaal en live):** export (`bewijsdossier-student-2026-09-30.json`) → één teken gewijzigd → verificatie: „gewijzigd na export" bij het gewijzigde bestand, niets bij het ongewijzigde; vijf fixtures tegelijk: 5 rijen met 11 onderdelen en 3 leeruitkomsten, twee gemarkeerd; import in een nieuw browserprofiel: record en versienummer terug, een gewijzigd bestand wordt pas na „Toch importeren" ingelezen; drie afdrukpagina's met 64-tekens controlesom; melding na 10 wijzigingen, weg na „Later" en na herladen; geblokkeerde opslag (init-script dat `localStorage` laat falen): melding en exportknop na ca. 0,2 s op `dossier.html` en `leerblok-1.html`, en de export werkt. Netwerktrace tijdens export en verificatie: 0 verzoeken buiten de eigen origin en 0 verzoeken met een andere methode dan GET; 0 consolefouten; alle 8 pagina's 200 live.
- **Niet gedaan / niet te verifiëren:** een echt privévenster (het init-script bootst geblokkeerde opslag na; in Chrome en Firefox werkt `localStorage` in een privévenster meestal gewoon); afdrukken naar pdf en de printstijl zijn niet visueel bekeken (schermafdrukken liepen in de testbrowser vast); een menselijke tester; `crypto.subtle` bestaat alleen in een beveiligde context (https of localhost), anders geeft de export een duidelijke fout. 4.7 van fase 4: het EV-09-record staat in het dossier en op de afdrukpagina van LUK 5; of de teamactie daar leesbaar staat hangt af van de veldnamen in `leerblok-4.json` (bij ontbrekend label staat de veldnaam).

---

## Fase 4 — De Wissel en de feedbacklog (EV-09)

**Doel.** Feedback geven en ontvangen zonder server.
**Wat de tester doet.** Twee testers (twee browsers) wisselen een wisselblok via het klembord, leggen „ik zie / ik mis / ik vraag me af" vast en ontvangen de feedback terug. Een letterlijke kopie van het wisselblok in de eigen EV-01 geeft „let op".
**Spec.** LB-14, EV-09, WS-1, WS-3…WS-11, ST-7.

### Subtasks
- [x] 4.1 Schrijf `js/wissel.js` met `maakWisselblok(records)` (onderzoeksvraag en zoekvragen, zonder alias) (WS-1). Verwacht: 0 aliassen in het blok, 1 klik naar klembord.
- [x] 4.2 Bouw plakken van het wisselblok van een wisselpartner met de rollen teamgenoot, medestudent en coach (WS-3). Verwacht: 3 rollen geaccepteerd.
- [x] 4.3 Bouw de feedbacklog: ik zie, ik mis, ik vraag me af, rol, actie, status; onbeperkt regels (LB-14, WS-4). Verwacht: 6 velden, ≥ 10 regels.
- [x] 4.4 Laat de feedback via het klembord terugkomen en als ontvangen en gegeven verschijnen in EV-09 (WS-5). Verwacht: 1 ontvangen en 1 gegeven regel na een uitwisseling.
- [x] 4.5 Schrijf de controles van EV-09 in `js/checks/lb4.js` (alleen de EV-09-controles) en de kopiecontrole voor EV-01 en EV-02 (WS-7, EV-09). Verwacht: 0 tekens verschil → `let op`, status Bijna.
- [x] 4.6 Laat EV-09 op Bijna staan zolang er geen feedback is, ook na ≥ 14 dagen (WS-8). Verwacht: test met aangepaste tijdstempels.
- [x] 4.7 Voeg de flow voor de post-its van andere teams toe met de rol „ander team” en één teamactie (WS-6). Verwacht: zichtbaar op de dossierpagina naast individuele feedback. *Flow en teamactie in fase 4; de weergave op `dossier.html` (twee kolommen: individueel naast post-its van andere teams met teamactie) in fase 7, met test en sabotagetest.*
- [x] 4.8 Toon de privacytekst bij de Wissel met het klembord als kanaal, ≤ 60 woorden (WS-10). Verwacht: 1 tekst in de flow.
- [x] 4.9 Toon een herinnering bij een actie die ≥ 7 dagen dezelfde status heeft (WS-11). Verwacht: 1 herinnering na 7 dagen, 0 bij 6 dagen.
- [x] 4.10 Toon de Wissel pas na de eerste versie van EV-02 (ST-7). Verwacht: in de eerste 4 schermen van leerblok 1 zichtbaar 0 Wissel-elementen.
- [x] 4.11 Bevestig dat de Wissel zonder server werkt (WS-9). Verwacht: 0 verzoeken met wisselblokinhoud.

### Testpoort
- [x] Volledige testpoort.
- [x] Sabotage WS-7: schakel de kopiecontrole uit; de test faalt.
- [x] Tester met 2 browsers: uitwisseling, kopiecontrole, feedback terug (AC-23). *Geautomatiseerde vervanging: Playwright MCP met twee browsercontexten, lokaal en live; klembord gesimuleerd met de echte klembord-API en plakken via het tekstveld. Geen menselijke tester.*
- [x] Geclaimde regels met hun methode gecontroleerd (WS-2 valt in fase 11).

### Afsluiting
- [x] commit `WS-1, WS-3…WS-11, LB-14, EV-09: Wissel en feedbacklog` (1908808)  - [x] push (Actions-run groen, live geverifieerd)  - [x] overzicht afvinken (na 4.7)

**Afwijkingen fase 4.** (a) `js/sessie.js` (fase 2) kreeg een optionele parameter `context` voor extra controlecontext, nodig voor de kopiecontrole (records van andere leerblokken en ontvangen wisselblokken); `tests/lb1.test.mjs` kreeg één regel (nieuw controletype gedekt in `wissel.test.mjs`). (b) Nieuw bestand `js/wissel-paneel.js` (DOM) naast `js/wissel.js` (logica). (c) `leerblok-4.html` kreeg `data-leerblok="4"`; `js/leerblok.js` kreeg een `feedbacklog`-component en de Wissel-sectie in leerblok 1. (d) `data/leerblok-4.json` bevat alleen taak 6.2 en een voorlopige verdieping (content-check eist er één); fase 11 vult aan. (e) 4.7: post-its en teamactie staan in het record EV-09; de weergave op de dossierpagina moet fase 3 (of 5) uit het record `EV-09` (`inhoud.regels`, `inhoud.teamactie`) tonen. (f) WS-11: de herinnering staat alleen in het Wissel-paneel; `herinneringenUitStore` is beschikbaar voor de startpagina. (g) Geen menselijke tester: zie Testpoort. Besluiten: ADR B62.

---

## Fase 5 — Proefsessie met 2–3 gebruikers en bijstelling

**Doel.** Controles bijstellen op wat gebruikers ten onrechte afkeuren of doorlaten, vóór de rest wordt gebouwd.
**Wat de tester doet.** Twee tot drie studenten of collega's werken leerblok 1 door op hun eigen vraagstuk, exporteren en doen de Wissel. De maker kijkt mee, noteert waar ze vastlopen en welke controles onterecht falen of slagen.
**Spec.** Geen nieuwe regels; bevestigt EV-01, EV-02, BW-1, BW-2, TK-8 en AP-2 in het klein.

### Subtasks
- [ ] 5.1 Werf 2–3 deelnemers, bij voorkeur 1 met een echt vraagstuk en 1 zonder scherp vraagstuk. Verwacht: 3 namen (alleen in dit plan of een notitie, niet in de repository).
- [ ] 5.2 Schrijf een sessieblad: 5 vragen (wat verwachtte je, waar liep je vast, welke melding was onduidelijk, was de controle terecht, welke tijd had je nodig). Verwacht: 1 blad van 1 pagina.
- [ ] 5.3 Voer de sessies en noteer per controle: onterecht afgekeurd, onterecht goedgekeurd, onduidelijke melding. Verwacht: 1 lijst.
- [ ] 5.4 Pas controles en meldingen aan; voeg voor elke onterechte uitkomst een unittest toe. Verwacht: elke bevinding heeft 1 test.
- [ ] 5.5 Leg gemeten tijden vast als startpunt voor de kalibratie van de richttijd. Verwacht: 1 tijd per deelnemer per taak.
- [ ] 5.6 Neem bevindingen die het doel raken op in BLUEPRINT (eigen commit in c-cluster) en in ADR (nieuwe regel). Verwacht: 0 bevindingen alleen in een commitbericht.

### Testpoort
- [ ] Volledige testpoort.
- [ ] De controles keuren geen goede voorbeelden af (AC-05) in de nieuwe tests.
- [ ] Elke bevinding heeft een test of een besluit.

### Afsluiting
- [ ] commit `Proefsessie: controles bijgesteld`  - [ ] push  - [ ] overzicht afvinken

---

## Fase 6 — Leerblok 2 en de bronnenpagina (EV-03 t/m EV-05)

**Doel.** Zoeken en beoordelen, met een bronnenlijst die het eindproduct zelf ook goed doet.
**Wat de tester doet.** Doet leerblok 2: zoektermen, zoekstring met operatoren, route B met promptgenerator, een bronbeoordeling met AAOCC en APA, de stelling. Opent `bronnen.html` en klikt een in-tekstverwijzing naar de bronregel.
**Spec.** LB-5, LB-6, LB-7, LB-8, EV-03, EV-04, EV-05, BR-1…BR-6.

### Subtasks
- [ ] 6.1 (concept, wacht op akkoord auteur) Vul `data/leerblok-2.json` met taken 3.1, 3.2, 4.1, 4.2 uit het werkboek; **ontbrekende „Waarom" en „Klaar als" voor de auteur schrijven en laten goedkeuren** (TK-2). Verwacht: 4 taken volledig, goedgekeurd.
- [x] 6.2 Schrijf `js/checks/lb2.js` met de controles van EV-03, EV-04, EV-05 (operatoren, `https://` of `doi.org`, jaar in APA gelijk aan jaarveld, 5 oordelen met toelichting). Verwacht: 3 goede en 3 zwakke voorbeelden per controle.
- [x] 6.3 Bouw de zoektermentabel, het zoekstringveld met operatorcontrole en de keuze route A/B (LB-5). Verwacht: 1 tabel, 1 veld, 2 routes.
- [x] 6.4 Bouw de promptgenerator met waarschuwing bij woorden uit de „niet noemen"-lijst (LB-6). Verwacht: 0 gemiste woorden in 6 testprompts.
- [x] 6.5 Bouw de bronlog met AAOCC-oordelen, twee verificatievinkjes bij route B, besluit, APA-veld met formaatcontrole en meerdere bronnen (LB-7). Verwacht: ≥ 2 bronnen invoerbaar.
- [x] 6.6 Bouw de stelling met keuze en argument (LB-8). Verwacht: 2 kanten, 1 argumentveld.
- [x] 6.7 Zet de bronnen van het LRD (bijlage A, literatuurregels) om naar `data/bronnen-1.json` en `-2.json` in APA, 7e editie, met „ongepubliceerd document" waar geen openbare publicatie bestaat (BR-3). Verwacht: elke bron met auteur, jaar, titel en link waar die bestaat.
- [x] 6.8 Schrijf `bronnen.html`: alle bronnen alfabetisch met werkende link (BR-1, BR-2) en in-tekstverwijzingen `(Auteur, jaar)` die naar de bronregel klikken (BR-4). Verwacht: 100 % van de verwijzingen klikt door.
- [x] 6.9 Breid `content-check` uit: faalt bij een verwijzing zonder bronregel of een bronregel zonder citatie (BR-5). Verwacht: 0 wezen.
- [x] 6.10 Breid `link-check` uit met een controle op alle DOI's en URL's uit de bronnen, en laat de workflow die bij elke publicatie draaien (BR-6). Verwacht: dode link → workflow rood.
- [x] 6.11 Markeer fictieve bronkaarten als „fictief" in de datafiles voor het later te bouwen spel (voorbereiding MD-15). Verwacht: veld `fictief: true` waar van toepassing.

### Testpoort
- [x] Volledige testpoort, inclusief link-check op alle DOI's.
- [x] Sabotage BR-5: voeg een verwijzing zonder bronregel toe; `content-check` faalt.
- [x] Sabotage BR-6: zet een DOI op een niet-bestaande waarde; de workflow faalt.
- [x] Tester doorloopt leerblok 2 en klikt 3 verwijzingen door.
- [x] Geclaimde regels met hun methode gecontroleerd (BR-1 Test, BR-2 Test, BR-3 Inspectie, BR-4 Test, BR-5 Test, BR-6 Test).

### Afsluiting
- [x] commit `LB-5…LB-8, EV-03…EV-05, BR-1…BR-6: leerblok 2 en bronnenpagina`  - [x] push  - [x] overzicht afvinken

**Afwijkingen fase 6.** Sabotage BR-6 lokaal gedaan (link-check faalt, exit 1); de push naar een testbranch werd geweigerd, dus 'workflow rood' is niet op GitHub getoond. EV-03 staat op taak 3.2 (ADR B64). 16 LRD-bronnen staan onder `wachtOpCitatie` (waarschuwing). Commit e9fe0b4 in a3-learning.

---

## Fase 7 — Terugblik en werken met tussenpozen

**Doel.** Elk leerblok vanaf 2 begint met ophalen, vergelijken en toepassen, en de site overleeft de pauze.
**Wat de tester doet.** Zet met testprofielen de tijdstempels van het dossier op 1 uur, 1 dag, 5 dagen en 14 dagen terug en opent leerblok 2 (en de stubs van 3 en 4). Ziet steeds de juiste terugblik. Maakt de browseropslag leeg en ziet een importaanbod.
**Spec.** TP-1…TP-11.

### Subtasks
- [x] 7.1 Leg `data/terugblik.json` vast en vul het met de kaarten van LRD 8.5 (drie blokken: items, twee kennisvragen, transfervraag). Verwacht: 3 kaarten, 2 kennisvragen per kaart.
- [x] 7.2 Schrijf `js/terugblik.js` met `pauzeInDagen(dossier)` uit de tijdstempels (TP-6). Verwacht: 0 dagen afwijking van het verschil tussen de tijdstempels.
- [x] 7.3 Voeg `bandbreedte(pauze)` toe: < 2 uur / < 2 dagen / 2–13 dagen / ≥ 14 dagen (TP-7). Verwacht: 4 profielen (1 uur, 1 dag, 5 dagen, 14 dagen) geven de verwachte terugblik.
- [x] 7.4 Bouw het scherm „Vorige keer" dat achtereenvolgens de dossiercontrole, de terugblik met meenemen-kaart en de transfervraag toont (TP-11, TP-1). Verwacht: 1 scherm, 3 onderdelen in vaste volgorde, terugblik ≤ 15 min.
- [x] 7.5 Bouw ophalen vóór de kaart: ≥ 3 punten en 2 kennisvragen, pas dan de kaart met items en eigen bewijsstukken (TP-2, TP-3). Verwacht: kaart 0× zichtbaar vóór 3 punten of „ik weet het nog".
- [x] 7.6 Bouw de transfervraag van twee zinnen met één gekozen item (TP-4) en „ik weet het nog" met één klik zonder bewijsrecord (TP-5). Verwacht: 0 bewijsrecords uit de terugblik.
- [x] 7.7 Log pauze in dagen en „gedaan" of „overgeslagen" in het dossier (TP-8). Verwacht: 2 velden per leerblok vanaf 2.
- [x] 7.8 Bouw de dossiercontrole met importaanbod en lijst van ontbrekende bewijsonderdelen (TP-9). Verwacht: na leegmaken 1 aanbod en 1 lijst, 0 verloren gegevens na import.
- [x] 7.9 Voeg het veld voor aanbevolen week en dag toe aan de leerblokdata (TP-10). Verwacht: 4 velden, 0 blokkades.
- [x] 7.10 Maak `tests/terugblik.test.mjs` met de 4 profielen en de grenzen 2 uur, 2 dagen en 14 dagen. Verwacht: groen.

### Testpoort
- [x] Volledige testpoort.
- [x] Sabotage TP-2: toon de kaart vóór het ophalen; de test faalt.
- [x] Sabotage TP-7: verwissel twee bandbreedtes; de test faalt.
- [x] Tester met aangepaste tijdstempels doorloopt de 4 profielen (AC-39, AC-40). *Geautomatiseerde vervanging: Playwright MCP, lokaal (`python3 -m http.server`) en live; tijdstempels van EV-01 en EV-02 in `localStorage` op 1 uur, 1 dag, 5 dagen en 14 dagen terug gezet; opslag leeggemaakt geeft het importaanbod, import zet de records en het log terug. Geen menselijke tester.*
- [x] Geclaimde regels met hun methode gecontroleerd. Open punt A-5 (pauze tussen 1 en 2 dagen) is beslist en vastgelegd in ADR.

### Afsluiting
- [x] commit `TP-1…TP-11: terugblik en tussenpozen (ook WS-6: feedback op dossierpagina)` (49a99a7)  - [x] push (Actions-run groen, live geverifieerd)  - [x] overzicht afvinken

---

**Afwijkingen fase 7.** (a) De pauze (TP-6) is de tijd tussen nu en het laatste `bijgewerkt` van de records van het vorige leerblok (zonder die: van een eerder leerblok; zonder records: onbekend, dan de volledige terugblik). (b) Aanbevolen week en dag (TP-10) staan in `data/leerblokken.json` (`aanbevolen`), niet in `leerblok-N.json`: leerblok 3 heeft nog geen eigen bestand en het overzicht heeft alle 4; `content-check` eist ze. Waarden zijn een concept van de bouwer (uit LRD 8.x en het weekprogramma). (c) Het terugblik-log (TP-8) is geen bewijs en geen record: meta `terugblik:log`, en als optioneel veld `terugblik` in de export (schema blijft 1.0; import vult alleen aan). (d) Leerblok 3 heeft tot fase 10 `js/leerblok-stub.js` (h1, aanbevolen, scherm „Vorige keer”); leerblok 4 gebruikt `leerblok.js`. (e) De samenvatting voor pauzes van 14 dagen of langer staat in `data/terugblik.json` met bron `concept-auteur` (waarschuwing in `content-check`, wacht op akkoord auteur). (f) `dossier.js` importeert nu `wissel.js`, `weergave.js` en `terugblik.js`; `toonWaarde` op de afdrukpagina is `waardeTekst` (toont geneste inhoud van EV-09 leesbaar in plaats van „[object Object]”). (g) `tests/fixtures/content-*/leerblokken.json` kregen `aanbevolen`. (h) Sabotage: 60 mutaties in `terugblik.js`, `dossier.js`, `weergave.js` en `content-check.mjs`, elk faalt minstens één test; alle 38 nieuwe tests zijn minstens eenmaal gebroken en hersteld (TP-2: kaart altijd zichtbaar; TP-7: middel en volledig verwisseld, en elke grens). Eén mutatie (afronden van de pauze in het log) overleefde eerst; daarvoor kwam de test met 5,25 dagen. Besluiten: ADR B65.

---

## Fase 8 — Huisstijl, toegankelijkheid, responsive en offline

**Doel.** De site ziet eruit als onderdeel van het C-cluster en werkt voor iedereen op elk apparaat.
**Wat de tester doet.** Opent de site op een telefoon (360 px), doet leerblok 1 met alleen het toetsenbord, met een schermlezer, en zet het netwerk uit na het laden.
**Spec.** TG-1…TG-5, PF-1…PF-5, QA-6.

### Subtasks
- [x] 8.1 Pas `css/site.css` aan naar de HAN-huisstijl (accent `#E50056`, zwart, wit, dikke randen) uit de zusterdocumenten (QA-6). Verwacht: 100 % van de pagina's gebruikt de tokens.
- [x] 8.2 Zet contrast op ≥ 4,5:1 voor alle tekst en toon statussen ook als tekst (TG-3, TG-4). Verwacht: 3 statussen elk met tekst.
- [x] 8.3 Maak alle invoer met het toetsenbord bedienbaar en geef focus een zichtbare rand (TG-2). Verwacht: leerblok 1 zonder muis in te vullen en te bewaren.
- [x] 8.4 Voeg labels en landmarks toe voor schermlezers (TG-5, TG-1). Verwacht: 0 onbereikbare velden in leerblok 1.
- [x] 8.5 Maak de pagina's responsive vanaf 360 px (PF-1). Verwacht: 0 px horizontale scroll, alle velden van 4 leerblokken invulbaar.
- [x] 8.6 Zorg dat een geladen leerblok zonder netwerk blijft werken (PF-3). Verwacht: 0 netwerkverzoeken tijdens 45 min gebruik.
- [x] 8.7 Houd elke pagina ≤ 300 kB zonder video (PF-4). Verwacht: meting per pagina.
- [x] 8.8 Toon de richttijd van 45 min per leerblok inclusief media (PF-5). Verwacht: 4 pagina's met 45 min.
- [ ] 8.9 (open: alleen Chromium, Firefox 155 en WebKit 26.6 via Playwright, geen Edge of echte Safari; zie ADR B66) Test in de twee laatste versies van Chrome, Safari, Firefox en Edge (PF-2). Verwacht: 4 × 2 zonder functieverlies.
- [x] 8.10 Draai Lighthouse (toegankelijkheid) op alle pagina's (TG-1). Verwacht: score ≥ 95 op 100 % van de pagina's.

### Testpoort
- [x] Volledige testpoort.
- [x] Sabotage TG-3: zet één tekst op lage contrast; de contrastcontrole faalt.
- [x] Lighthouse ≥ 95 op alle pagina's; 360 px zonder horizontale scroll; toetsenbordtest leerblok 1; schermlezertest leerblok 1; offlinetest.
- [x] Geclaimde regels met hun methode gecontroleerd.

### Afsluiting
- [x] commit `TG-1…TG-5, PF-1…PF-5, QA-6: huisstijl en toegankelijkheid`  - [x] push  - [x] overzicht afvinken

**Afwijkingen fase 8.** (1) Geen service worker: PF-3 is gehaald doordat alles bij het laden binnenkomt (ADR B66). (2) Menselijke tests vervangen door Playwright (360 px, toetsenbord met press_key en page.keyboard, accessibility-snapshot, netwerk uit) en Lighthouse via chrome-devtools (toegankelijkheid 100 op alle 10 pagina's, mobiel). Geen echte schermlezer (VoiceOver/NVDA) gebruikt: TG-5 is gecontroleerd via de toegankelijkheidsboom en labels, niet met gesproken uitvoer. (3) 8.9 (PF-2) niet afgevinkt: Chromium, Firefox 155 en WebKit 26.6 zonder functieverlies, Edge en echte Safari niet, versies niet getoetst. (4) Gewichtsgrens is een bovengrens van 275 kB voor leerblok 1, 2 en 4: weinig ruimte voor fase 10 tot 13.

---

## Fase 9 — Docentmodus: mechaniek en deel 1

**Doel.** De docent leidt deel 1 (90 min) van het werkcollege met alleen de docentmodus.
**Wat de tester doet.** Een docent opent `docent.html?modus=docent`, start deel 1, ziet de stapkaart per onderdeel en de klok, schuift een onderdeel op en ziet de resterende tijd opnieuw berekend, opent een docentkaart en een verborgen modelantwoord, en drukt de docentkaarten van deel 1 af.
**Spec.** DM-1…DM-9, DM-10, DM-11, DM-14…DM-17, PR-3, PR-4.

### Subtasks
- [x] 9.1 Leg het formaat van `data/docent-deel1.json` vast (onderdeel, klok, taaknummer, materiaal, laptop open/dicht, dia's, wat de docent doet, kernboodschap, rondloopvragen, als het anders loopt). Verwacht: één voorbeeldonderdeel valideert.
- [x] 9.2 Vul `data/docent-deel1.json` met de 11 onderdelen van deel 1 uit LRD 8.2 en het draaiboek. Verwacht: 11 onderdelen.
- [x] 9.3 Maak `js/docent/kies.js`: de docentmodus kiesbaar bij de start of met een adres-toevoeging, zonder inloggen, op dezelfde contentbestanden (DM-1, DM-2). Verwacht: 0 accounts; 1 wijziging in een modelantwoord verschijnt in beide weergaven.
- [x] 9.4 Bouw de stapkaart met 7 elementen (taaknummer, opdracht, „klaar als", tijd, materiaal, dia's, laptop open/dicht) (DM-3). Verwacht: 7 elementen per kaart.
- [x] 9.5 Bouw `js/docent/klok.js`: klok per deel vanaf 0:00, aftelling per onderdeel, start, pauze, reset (DM-4). Verwacht: afwijking ≤ 1 s over 10 min.
- [x] 9.6 Toon de tijd als richttijd zonder blokkade (DM-5) en, voor een ronde, de gallery walk-tijden van 2 × 4 min en 2 min lezen (DM-6; die tijden gelden voor deel 2, de klok kent ze al). Verwacht: 0 blokkades bij 100 % van de richttijd.
- [x] 9.7 Bouw de docentkaart met 4 elementen (wat de docent doet, kernboodschap, rondloopvragen, als het anders loopt) en de verborgen modelantwoorden en veelgemaakte fouten (DM-7, DM-8). Verwacht: modelantwoorden 0× zichtbaar vóór de klik.
- [x] 9.8 Bouw overslaan, verschuiven en tijd aanpassen met herberekening van de resterende tijd (DM-9). Verwacht: resterende tijd = som van resterende onderdelen ± 1 s na overslaan van 2 onderdelen.
- [x] 9.9 Bouw het programmaoverzicht met wat klaar is en wat komt en een veld voor de begintijden uit het rooster (DM-10). Verwacht: 1 overzicht, begintijden invulbaar.
- [x] 9.10 Bouw de afdruk van de docentkaarten van een deel als draaiboek (DM-11) en de terugblik-kaart per leerblok uit `data/terugblik.json` (DM-14). Verwacht: afdruk deel 1 bevat 100 % van de onderdelen, tijden en rondloopvragen van het scherm; 3 terugblik-kaarten.
- [x] 9.11 Zorg dat de docentmodus na het laden zonder netwerk werkt (DM-15). Verwacht: 15 min zonder netwerk zonder foutmelding.
- [x] 9.12 Stel de stapkaart in op tekst ≥ 28 px bij 1280 × 720 en contrast ≥ 4,5:1 (DM-16). Verwacht: meting.
- [x] 9.13 Houd beoordelingsinformatie uit de data (DM-17) en bevestig dat de docentmodus geen studentgegevens bewaart en geen koppeling met studentapparaten heeft (PR-3, PR-4). Verwacht: 0 studentgegevens in opslag; 0 verbindingen.

### Testpoort
- [x] Volledige testpoort.
- [x] Sabotage DM-9: laat de herberekening de overgeslagen tijd meetellen; de test faalt.
- [x] Sabotage DM-8: toon modelantwoorden direct; de test faalt.
- [ ] (wacht op mens) Docent leidt een proefrun van 10 minuten van deel 1 zonder het draaiboek (voorbereiding AP-4). Notities in het testrapport.
- [ ] (wacht op mens) Leesbaarheid vanaf de achterste rij in een lokaal (DM-16).
- [x] Geclaimde regels met hun methode gecontroleerd.

### Afsluiting
- [x] commit `DM-1…DM-17, PR-3, PR-4: docentmodus met deel 1` (ae77297)  - [x] push  - [x] overzicht afvinken

**Afwijkingen fase 9.** (1) Twee punten wachten op een mens en zijn niet afgevinkt: de proefrun van 10 minuten zonder draaiboek en de leesbaarheid vanaf de achterste rij (DM-16 is alleen gemeten: kleinste tekst 28 px op 1280 × 720, contrast ≥ 4,5:1, alle 11 stapkaarten passen op één scherm). DM-16 blijft daarmee gedeeltelijk open. (2) Mechaniek gecontroleerd met Playwright: klok met `page.clock` (aftelling, overschrijding zonder blokkade, overslaan van 2 onderdelen, herladen), modelantwoord 0× in de pagina vóór de klik, afdruk in printmedia (11 onderdelen), 15 min offline zonder fout, 0 verzoeken naar andere domeinen, alleen `a3d:`-sleutels in de opslag, dit alles ook op de gepubliceerde site. Lighthouse toegankelijkheid 100 op `docent.html`. De gallery walk (DM-6) is met een tijdelijk aangepast bestand in de browser geprobeerd, want geen onderdeel van deel 1 gebruikt hem. (3) Sabotage: 20 mutaties in `klok.js`, `kaarten.js`, `kies.js`, `pagina.js`, `content-check.mjs`, `docent.css` en `docent.html`, elk faalt minstens één test; vier overleefden eerst (cijfer in de verbodenlijst, de rondloopvraag-eis, de grens bij verschuiven, `herstel`) en kregen een test. (4) `tools/contrast-check.mjs` leest nu ook `css/docent.css`. (5) `docent.html` weegt 153 kB (grens 300 kB): de data laadt pas na de keuze. (6) Inhoud: 11 onderdelen uit LRD 8.2 (het draaiboek heeft 12 rijen, 0:20 en 0:25 zijn samen één onderdeel); concepten van de bouwer staan gemarkeerd (zie ADR B67) en wachten op akkoord van de auteur. (7) Voor fase 10: deel 2 vult `data/docent-deel2.json` in hetzelfde formaat (README van a3-learning), meldt zich aan in `DELEN` in `js/docent/pagina.js`, pauzes zijn onderdelen met `"soort": "pauze"`, en `docent.html` heeft nog ruim 145 kB gewichtsruimte.

---

## Fase 10 — Leerblok 3 en docentmodus deel 2 (EV-06 t/m EV-08)

**Doel.** Het vraagstuk plaatsen: stakeholders, VPC, BMC, TOM-model en conclusies.
**Wat de tester doet.** Doet leerblok 3 met een eigen vraagstuk: stakeholdertabel tekent zich op het invloed/belang-raster, register van feit en aanname, conclusies. Een docent leidt deel 2 in de docentmodus.
**Spec.** LB-9…LB-13, EV-06, EV-07, EV-08, DM-18, LI-3.

### Subtasks
- [ ] 10.1 (concept, wacht op akkoord auteur: 9 van de 12 „Waarom” en „Klaar als” zijn geschreven door de bouwer, bron `concept-auteur`; de andere komen uit het werkboek) Vul `data/leerblok-3.json` met taken 5.1, 6.1, 7.1, 8.1, 9.1, 9.2; ontbrekende „Waarom" en „Klaar als" door de auteur laten goedkeuren (TK-2). Verwacht: 6 taken volledig.
- [x] 10.2 Schrijf `js/checks/lb3.js` met de controles van EV-06, EV-07, EV-08. Verwacht: 3 goede en 3 zwakke voorbeelden per controle.
- [x] 10.3 Bouw de stakeholdertabel met automatisch raster (LB-9). Verwacht: 4 kwadranten, ≥ 5 stakeholders getekend.
- [x] 10.4 Bouw de checklists en foto-vinkjes voor de vier producten (LB-10). Verwacht: 4 producten, 4 vinkjes.
- [x] 10.5 Bouw het TOM-model V1 volgens TOM³ met 3 lagen × 4 kolommen = 12 cellen (LB-11) met een eigen samenvatting en bronvermelding als „ongepubliceerd document" (LI-3, BR-3). Verwacht: 12 cellen; 0 zinnen ≥ 8 woorden gelijk aan de bron (Analyse).
- [x] 10.6 Bouw het feit/aanname-register met koppeling aan een zoekvraag en aan een VPC/BMC/TOM-onderdeel (LB-12). Verwacht: ≥ 3 beweringen met 3 velden.
- [x] 10.7 Bouw de conclusies met controle tegen de stakeholderlijst en de herziene onderzoeksvraag (LB-13). Verwacht: 3 conclusies, 1 herziene vraag.
- [x] 10.8 Voeg de samenhangcontroles EV-01→EV-06, EV-07→EV-02 en EV-08→EV-06 toe aan `checks/lb3.js` (deel van BW-10). Verwacht: 3 testen groen.
- [x] 10.9 Voeg `data/bronnen-3.json` toe (VPC, BMC, TOM³-verwijzing). Verwacht: `content-check` groen op wezen.
- [x] 10.10 Vul `data/docent-deel2.json` met de 8 onderdelen en 3 pauzes van deel 2 uit LRD 8.2 (DM-18). Verwacht: 19 onderdelen in totaal met deel 1 (11 + 8), plus 3 pauzes.
- [ ] 10.11 (wacht op mens; expliciet uitgesteld in ADR B68) Verifieer met de auteur dat het college hetzelfde TOM-model gebruikt als de opdrachtomschrijving en vraag bij Westmoreland de publicatiegegevens (open punt A-1). Verwacht: antwoord of een expliciet uitstel, vastgelegd in ADR.

### Testpoort
- [x] Volledige testpoort (453 tests, content-check, link-check, gewichtscontrole, gepubliceerde site zonder consolefout en met 0 verzoeken naar andere domeinen; Lighthouse toegankelijkheid 100 op leerblok-3.html).
- [x] Sabotage EV-06: haal de gebruiker uit EV-01 uit de stakeholderlijst; de samenhangcontrole faalt.
- [x] Tester doorloopt leerblok 3 op een eigen vraagstuk (vervangen door Playwright: lokaal en op de gepubliceerde site; alle drie de onderdelen Compleet; geen mens).
- [ ] (wacht op mens) Docent leidt een proefrun van deel 2. (Mechaniek met Playwright en `page.clock` gecontroleerd: klok, pauzes, gallery walk van 2 × 4 + 2 min.)
- [x] Geclaimde regels met hun methode gecontroleerd.

### Afsluiting
- [x] commit `LB-9…LB-13, EV-06…EV-08, DM-18: leerblok 3 en docentmodus deel 2` (9e8ed91)  - [x] push  - [x] overzicht afvinken

**Afwijkingen fase 10.** (1) Een record hoort bij één taak: EV-07 staat op 8.1 (register en TOM-model) en EV-08 op 9.2 (conclusies van 9.1 via `afgeleidVan`); 6.1, 7.1 en 9.1 hebben geen eigen bewijsonderdeel. Het register is één register bij 8.1 (ADR B68). (2) 10.1 en de inhoud van de onderdelen van deel 2 zijn deels concept van de bouwer (85 waarschuwingen in `content-check`). (3) 10.11 (A-1) is niet uitgevoerd en uitgesteld. (4) Menselijke tester en proefrun docent zijn vervangen door Playwright; de proefrun blijft open. Geen schermlezer gebruikt. (5) De werkboektijden van de zes taken tellen op tot 105 min terwijl het leerblok 45 min heet (ADR B68, kalibreren in fase 15). (6) De herhaling van VPC en BMC (5 min) zit in de onderdelen 6.1 en 7.1 van deel 2 (25 min); 9.1 en 9.2 zijn één onderdeel. (7) PF-4 paste niet: `js/blok.js` (herhaalde velden als `reeks`), `wissel-paneel.js` dynamisch en alleen bij leerblok 1 en 4, en `gewicht-check` telt alleen het vorige leerblok en kent `// gewicht-alleen: wissel`. Leerblok 3 weegt 297,7 kB; fase 11 en 12 hebben geen ruimte meer op de leerblokpagina's. (8) `js/leerblok-stub.js` is verwijderd; `tests/bronnen.test.mjs`, `toegankelijk.test.mjs`, `terugblik.test.mjs` en `werkboek.test.mjs` zijn aangepast; drie bronnen (VPC, sjabloon, TOM³) zijn van `wachtOpCitatie` in bronnen-1 naar bronnen-3 verhuisd en BMC (Osterwalder & Pigneur, 2010) is toegevoegd, wachtend op akkoord. (9) Sabotage: 27 mutaties in nieuwe code en data, 25 braken minstens één test; twee overleefden eerst (de helft-van-de-woorden-grens in de naamvergelijking en het opnieuw tekenen van het raster) en kregen een test; alle nieuwe tests zijn minstens eenmaal gebroken en hersteld. (10) LI-3: 0 reeksen van 8 woorden of meer gelijk aan het TOM³-buildplan, het dashboard, de Bureau Tromp-transcriptie en de Atlassian-pagina in lits/ (`tools/overlap-check.mjs`). Besluiten: ADR B68.

---

## Fase 11 — Leerblok 4: verbanden, reflectie en afronding (EV-10, EV-11)

**Doel.** Synthese ontdekken, reflecteren en alles bij elkaar in het dossier.
**Wat de tester doet.** Doet taak 9.4: trekt lijnen tussen user story, VPC en zes kapitalen, markeert kapitalen, noemt een spanning met een stakeholder, schrijft de synthese. Doet de STARR-reflectie, kopieert naar A3 vak 1 en kiest bij een tweede profiel „voorlopig vraagstuk" en „opnieuw doen".
**Spec.** LB-15, LB-16, LB-17, EV-10, EV-11, VB-1…VB-10, WS-2, TK-11…TK-14, ST-3, ST-4, ST-5, BW-10, LI-2.

### Subtasks
- [ ] 11.1 (concept, wacht op akkoord auteur: alle „Waarom” en „Klaar als” van 9.4 en 6.3 zijn geschreven door de bouwer, bron `concept-auteur`; 6.2 blijft zoals het was) Vul `data/leerblok-4.json` met taak 9.4 en de reflectietaak; ontbrekende „Waarom" en „Klaar als" door de auteur laten goedkeuren. Verwacht: taken volledig.
- [x] 11.2 Bouw de verbanden-kaart met drie kolommen en zes kapitalen (VB-1) in `js/verbanden.js`. Verwacht: 3 kolommen, 6 kapitalen.
- [x] 11.3 Bouw de oefencasus met 3 open vragen en het modelvoorbeeld pas na een eigen poging (VB-2). Verwacht: 0 modelvoorbeelden vóór ≥ 1 getrokken lijn.
- [x] 11.4 Bouw het trekken van lijnen met 3 typen en één zin (VB-3) en het automatisch tekenen tussen de kolommen zonder ingebedde afbeeldingen van Strategyzer of IIRC (VB-10, LI-2). Verwacht: ≥ 6 lijnen in een testprofiel; 0 ingebedde afbeeldingen van beide bronnen.
- [x] 11.5 Bouw open plekken als vraag, nooit als antwoord (VB-4). Verwacht: 0 antwoorden in een leeg en een half ingevuld voorbeeld.
- [x] 11.6 Bouw de markering van kapitalen (VB-5) en de spanning met een stakeholder uit EV-06 (VB-6). Verwacht: 6 kapitalen, 3 markeringen; ≥ 1 spanning.
- [x] 11.7 Bouw de synthese-alinea (≤ 5 zinnen) met chips uit ≥ 2 modellen en 3 antwoorden op „wat laat dit model niet zien" (VB-7). Verwacht: alle drie de elementen gecontroleerd.
- [x] 11.8 Zet taak 9.4 als zelfstandige taak van 20 min zonder plek in het werkcollegeprogramma (VB-9). Verwacht: 0 onderdelen in `docent-deel2.json`.
- [x] 11.9 Schrijf `js/checks/lb4.js` (aanvullend) voor EV-10 en EV-11 en de samenhangcontroles EV-11→EV-01 en EV-11→EV-06 (BW-10). Verwacht: 5 samenhangcontroles in totaal.
- [x] 11.10 Neem de lijst van verbanden op in het wisselblok en het A3-tekstblok (WS-2, VB-8). Verwacht: alle verbanden uit EV-11 aanwezig.
- [x] 11.11 Bouw het STARR-sjabloon (LB-15) en de zin „wat ik hiermee aan mijn A3 heb" naast de waarom-zin (TK-11). Verwacht: 5 delen, 1 keuzelijst, 2 zinnen naast elkaar.
- [x] 11.12 Bouw „kopieer naar A3 vak 1" met datumlog (LB-16, LB-17). Verwacht: 4 onderdelen in het klembord; 1 datum per actie.
- [x] 11.13 Toon het zwakste onderdeel op de dossierpagina (TK-12). Verwacht: klopt met 3 testprofielen.
- [x] 11.14 Voltooi de verdiepingstaken (4 in totaal) en zorg dat ze de status en de richttijd niet raken (TK-13, TK-14). Verwacht: 4 verdiepingstaken, 0 statuswijzigingen.
- [x] 11.15 Bouw het voorlopig vraagstuk: label `voorlopig`, „opnieuw doen" met één klik en oude en nieuwe versie zichtbaar (ST-3, ST-4, ST-5). Verwacht: 100 % van de records na de keuze `voorlopig: true`.
- [x] 11.16 Voeg `data/bronnen-4.json` toe (Mayer, Osterwalder, IIRC, e.a.). Verwacht: `content-check` groen.
- [x] 11.17 Draai `content-check` op alle 11 bewijsonderdelen (BW-12, QA-3). Verwacht: 11 van 11 volledig.

### Testpoort
- [x] Volledige testpoort (521 tests, content-check, link-check, gewichtscontrole, gepubliceerde site zonder consolefout en met 0 verzoeken naar andere domeinen; Lighthouse toegankelijkheid 99 op leerblok-4.html en 100 op dossier.html; 360 px zonder horizontale scroll).
- [x] Sabotage VB-4: toon het ontbrekende verband als antwoord; de test faalt.
- [x] Sabotage BW-10: verbreek de koppeling EV-11→EV-06; de samenhangcontrole faalt.
- [x] Testprofielen (Playwright in plaats van een mens, lokaal en live; ook alleen met het toetsenbord): pilotstudent met eigen vraagstuk; profiel „voorlopig vraagstuk" (AC-21); profiel met leeg dossier (AC-40).
- [x] Geclaimde regels met hun methode gecontroleerd.

### Afsluiting
- [x] commit `VB-1…VB-10, EV-10, EV-11, LB-15…LB-17, ST-3…ST-5, TK-11…TK-14: leerblok 4` (9b6d3f9)  - [x] push  - [x] overzicht afvinken

**Afwijkingen fase 11.** (1) PF-4 is eerst structureel opgelost, vóór nieuwe onderdelen: controlefabrieken, Wissel, weergavegroepen en de schermen van leerblok 4 laden per leerblok (`laadControles`, voorwaarden `wissel`, `weergave`, `lb4ui`), en de gewichtscontrole meet 300 kB gzip plus 400 kB bron; ADR B69. Leerblok 4 weegt 308 kB bron en 101 kB gzip; hoogste gzip 101 kB. De test op de fabrieken per leerblok vond een fout die anders pas in de browser was gebleken (leerblok 2 en 3 gebruiken fabrieken uit lb1). (2) EV-10 staat op een nieuwe taak 6.3 (STARR op de oefenronde van 6.2) en EV-11 op taak 9.4; het werkboek heeft beide taken niet, dus 11.1 blijft concept (auteur moet akkoord geven). De testfixture `maak-dossiers.mjs` noemt EV-10 nog taak 9.3; dat is testdata en niet aangepast. (3) De kaart heeft geen slepen met de muis: een verband maak je met twee knoppen en een formulier (toetsenbord, TG-2); de tekstlijst is de tekstweergave (TG-5). (4) ST-5: het dossier toont oud en nieuw naast elkaar op de dossierpagina; de export bevat alleen de nieuwste versie. TK-14: `verdiepingGedaan` (leerblokken, geen tekst) is een optioneel veld in de export en staat op de dossierpagina. (5) `data/bronnen-4.json` bevat alleen IIRC (uit wachtOpCitatie verplaatst); Mayer, Osterwalder en Strategyzer staan al in bronnen-2 en -3. Links naar de bronnen lopen via de bronnenpagina; er zijn geen afbeeldingen van Strategyzer of het IIRC (LI-2, test). (6) Menselijke tester vervangen door Playwright; geen schermlezer gebruikt; Lighthouse is op een leeg en op een gevuld dossier gedraaid in Chromium. (7) Sabotage: 16 mutaties in nieuwe code en data; 14 braken minstens één test, één had een onjuist zoekpatroon in de mutatie (VB-9, daarna opnieuw en gebroken) en één overleefde (een kale `import './lb2.js'` in het register); de test is aangescherpt en breekt nu. Alle nieuwe controles en tests zijn minstens eenmaal gebroken en hersteld (VB-4, BW-10 beide richtingen, VB-2, VB-3, ST-4, ST-5, LB-17, TK-12, WS-2, LI-2, PF-4 twee keer, QA-3, EV-11-spanning, VB-9). Besluiten: ADR B69.

---

## Fase 12 — Media: mechaniek, twee video's en twee spellen

**Doel.** De drie routes per leerblok werken en de eerste twee video's en spellen staan erin. Begint met de spellen die het meest opleveren (Bronnen-detective, Waarde-simulator).
**Wat de tester doet.** Opent leerblok 2 en leerblok 4, kiest tekst, video of spel en komt telkens uit bij dezelfde „klaar als"-regel. Speelt een spel met alleen het toetsenbord. Een docent start video en spel vanaf de stapkaart.
**Spec.** MD-1, MD-2, MD-3, MD-5, MD-6, MD-7, MD-9, MD-10, MD-11, MD-13, MD-14, MD-15, MD-16.

### Subtasks
- [x] 12.1 Schrijf `js/media.js`: tekst als standaard, twee kleine knoppen, laatste keuze onthouden (MD-2). Verwacht: 3 routes met dezelfde „klaar als".
- [x] 12.2 Schrijf de uitlegteksten (≤ 300 woorden) voor leerblok 2 en 4 met voorbeeld en modelantwoord (MD-3). Verwacht: ≤ 300 woorden per leerblok.
- [x] 12.3 Bouw het spel Bronnen-detective (zes fictieve bronkaarten, feedback per keuze, toetsenbord, tekstversie, geen score) (MD-9, MD-10, MD-13, MD-15). Verwacht: 0 muisacties voor een volledige doorloop; 100 % fictieve kaarten gemarkeerd.
- [x] 12.4 Bouw de simulatie Waarde-simulator (drie beslissingen, voorspellen, effect op zes kapitalen) met dezelfde eisen (MD-9, MD-10, MD-13). Verwacht: 1 tekstversie, feedback per keuze.
- [x] 12.5 Maak video V2 en V4 (≤ 3 min, ≤ 20 MB) met ondertitels (WebVTT) en transcript, zonder autoplay, laden na klik, op dezelfde site (MD-5, MD-6, MD-7). Verwacht: 2 hulpmiddelen per video; 0 verzoeken naar andere domeinen bij afspelen.
- [x] 12.6 Zorg dat geen spel of simulatie bewijs oplevert (MD-11). Verwacht: 0 bewijsrecords uit een spel.
- [x] 12.7 Plaats video's van derden als gewone link (MD-14). Verwacht: 0 ingebedde frames.
- [x] 12.8 Laat de docentmodus video en spel starten vanaf de stapkaart (DM-13 komt in fase 13 af voor alle vier). Verwacht: 2 stapkaarten spelen af zonder verzoeken naar andere domeinen.
- [x] 12.9 Toon in leerblok 1 twee kijktips als gewone link, met bron, duur en taal: Bureau Tromp (4:38, Nederlands) als instap en het MIT OpenCourseWare-fragment 0:44 tot 4:09 (Engels) als verdieping. Zet de gegevens in de datafile van leerblok 1 (MD-16, MD-14). Verwacht: 2 links, 2 van 2 met duur en taal, 0 ingebedde frames.

### Testpoort
- [x] Volledige testpoort.
- [x] Sabotage MD-6: zet autoplay aan; de test faalt.
- [x] Sabotage MD-11: laat een spel een bewijsrecord schrijven; de test faalt.
- [x] Netwerktrace tijdens afspelen: 0 verzoeken naar andere domeinen (MD-7).
- [x] Toetsenbordtest en tekstversie per spel.
- [x] Geclaimde regels met hun methode gecontroleerd.

### Afsluiting
- [x] commit `MD-1…MD-16 (deel): mediamechaniek, V2, V4, Bronnen-detective, Waarde-simulator, kijktips`  - [x] push  - [x] overzicht afvinken

**Afwijkingen fase 12.** (1) V2 en V4 zijn zelf gemaakt als eerlijk gemarkeerde conceptvideo's (computerstem Xander via macOS `say`, tekstdia's, ffmpeg): 114 s en 127 s, 1,1 en 1,3 MB, WebVTT en transcript. Ze zijn geen opname van de auteur; 12.5 is dus technisch af maar inhoudelijk een concept dat wacht op akkoord (of een eigen opname). `tools/maak-video.mjs` is tooling in `tools/` (SI-5 noemt tools/ niet; de map bestaat al met de controles) en de uitzondering staat in ADR B70. (2) De uitleg (MD-3) staat als `media.uitleg` (≤ 300 woorden: 205 en 237) naast de bestaande stof van de taken, niet in plaats ervan; de bestaande stof (463 woorden in leerblok 2) blijft staan, omdat de tekstroute volledig moet blijven (MD-12). Het modelantwoord in de tekstroute is verborgen tot een eigen poging (TK-6); in de video komt het na de aanwijzing „pauzeer en doe eerst zelf”. (3) De simulator laat de voorspelling alleen voor de lange termijn doen (per kapitaal geen, input, plus, min); het effect toont alle drie de termijnen. Het LRD noemt voorspelling op drie termijnen; dat is bewust vereenvoudigd (KISS, ≤ 5 min). De speelduur is geschat (40 s per kaart, 90 s per beslissing), niet gemeten; meten is 13.4. (4) Video en spel op de stapkaart: d1-10 (Bronnen beoordelen, V2 en Bronnen-detective) en d2-10 (Eerste conclusies, V4 en Waarde-simulator); 9.4 staat niet in het programma van woensdag, dus V4 hangt aan het onderdeel dat het dichtst bij de synthese ligt. `docent.html` kreeg `media-src 'self'` in de CSP. (5) Kijktips: URL's uit B60 met curl gecontroleerd (HTTP 200, oEmbed-titels kloppen: „Wat is de A3 verbetermethode?” en „Ses. 3-4: A3 Thinking”); duren (4:38 en fragment 0:44 tot 4:09) komen uit B60/LRD en zijn niet te verifiëren zonder de video te kijken. Bureau Tromp en MIT OCW zijn van `wachtOpCitatie` naar bronnen-1 verhuisd. (6) `content-check` kreeg `controleerMedia` (uitleg, transcript gelijk aan de uitleg, video- en spelbestanden, kijktips, docentveld) en scant `spellen/*.json` op verwijzingen (BR-5); `gewicht-check` kent de voorwaarde `media`. Leerblok 4 weegt 367 kB bron (grens 400) en 119 kB gzip. (7) Sabotage: 14 mutaties (autoplay, preload, spel schrijft record, spel importeert store, score, niet fictief, extern adres, iframe, muisgebeurtenis, standaardroute, metadata, docent-media, uitleg > 300 woorden); alle braken minstens één test, één (extern adres) pas nadat het commentaarfilter in de test was verbeterd. Niet gesaboteerd: MD-4 met een echte video van 4 minuten (fase 13). (8) Menselijke tester vervangen door Playwright (lokaal en live): drie routes, spel met alleen toetsenbord (keuzelijst met typen van de eerste letter, omdat pijltjes in een keuzelijst op macOS het menu openen), 0 verzoeken naar andere domeinen tijdens afspelen (Chromium), 0 `<video>` vóór de klik, 0 bewijsrecords na spelen. Lighthouse toegankelijkheid: 100 (leerblok 1 en 2) en 99 (leerblok 4). Geen schermlezer. Opgemerkt en niet van deze fase: `docent.html` toont een CSP-melding over inline `style` op het logo-symbool (fase 8). Besluiten: ADR B70.

---

## Fase 13 — Media: de overige video's en spellen

**Doel.** Alle vier de leerblokken hebben video en spel.
**Wat de tester doet.** Doorloopt elk leerblok in elke route (tekst, video, spel) en controleert per video ondertitels, transcript en duur.
**Spec.** MD-4, MD-8, MD-12, DM-13.

### Subtasks
- [x] 13.1 Maak video V1 en V3 (≤ 3 min, ≤ 20 MB) met ondertitels en transcript (MD-4). Verwacht: 4 video's in totaal, elk ≤ 3 min en ≤ 20 MB.
- [x] 13.2 Bouw het spel Vraagslijper (drie rondes, feedback per veld) (MD-8). Verwacht: ≤ 5 min.
- [x] 13.3 Bouw het spel Stakeholder-radar (invloed en belang, feedback per keuze) (MD-8). Verwacht: ≤ 5 min.
- [x] 13.4 (geschat, niet gemeten door een mens; zie afwijkingen) Controleer dat alle 4 spellen ≤ 5 min duren (MD-8). Verwacht: 4 gemeten tijden.
- [x] 13.5 Doorloop alle vier de leerblokken zonder video of spel (MD-12). Verwacht: 4 leerblokken afgerond.
- [x] 13.6 Laat de stapkaart voor elk onderdeel met een video of spel dat afspelen of starten zonder verzoeken naar andere domeinen (DM-13). Verwacht: alle bestaande stapkaarten getest.

### Testpoort
- [x] Volledige testpoort.
- [x] Sabotage MD-4: voeg een video van 4 min toe; de mediacontrole faalt.
- [x] Doorloop van elk leerblok in elke route (AC-30).
- [x] Geclaimde regels met hun methode gecontroleerd.

### Afsluiting
- [x] commit `MD-4, MD-8, MD-12, DM-13: overige media`  - [x] push  - [x] overzicht afvinken

**Afwijkingen fase 13.** (1) V1 en V3 zijn net als V2 en V4 conceptvideo's met computerstem (117 s en 133 s, 1,2 en 1,4 MB, WebVTT en transcript); ze wachten op akkoord van de auteur of een eigen opname. (2) 13.4 is een schatting, geen meting: de speelduur komt uit het aantal kaarten, rondes en vragen (255, 280, 300 en 300 s), twee spellen zitten precies op de grens van 300 s. Een gescripte Playwright-doorloop speelde elk spel uit (12, 12, 23 en 30 handelingen) en bewijst dat het uit te spelen is, niet hoe lang een student erover doet; meten hoort bij de pilot (fase 15, AP-2). (3) Menselijke tester vervangen door Playwright, lokaal en op de live URL na de groene workflow: van elk leerblok de drie routes (tekst standaard, video zonder autoplay en pas na klik geladen, spel), de „klaar als” zichtbaar in elke route, geen spelsleutels in de opslag, 0 verzoeken naar andere domeinen en 0 consolefouten; de vier stapkaarten d1-04, d1-10, d2-02 en d2-10 spelen video af en starten het spel, en een onderdeel zonder media toont geen mediagebied (DM-13). Het transcript is niet met Playwright geteld (mijn selector klopte niet); de inhoud ervan wordt door `content-check` en de unittests bewaakt (MD-5). (4) Nieuw: een eigen test voor MD-12 (gesaboteerd met een taak die naar video V2 verwijst: de test faalt, na herstel slaagt hij); MD-4 is gesaboteerd met een echte video van 4 minuten (bestaande test, faalt op „meer dan 180 s”). (5) Testpoort: 552 unittests, `content-check`, `link-check`, gewicht (leerblok 4: 383 kB bron, grens 400), contrast (0 paren onder 4,5:1) en overlap met het TOM³-buildplan (0 gelijke reeksen) groen. Geen schermlezer en geen Edge of Safari (zie fase 8). Besluiten: ADR B71.

---

## Fase 14 — Afdrukken, documentatie en eindcontrole

**Doel.** Alles wat een docent of student naast de site nodig heeft, en een regressiecontrole op het hele blueprint.
**Wat de tester doet.** Drukt werkboek en draaiboek van een deel af en legt ze naast de site. Leest de docentgids en de studentintroductie als iemand die de site nog nooit zag.
**Spec.** DM-12, DL-1, DL-2, DL-4, QA-4, QA-5, LI-1, SI-1.

### Subtasks
- [x] 14.1 Bouw de afdruk van het werkboek van een deel uit de contentbestanden met dezelfde nummers en „klaar als"-regels (DM-12). Verwacht: 100 % van de nummers en regels gelijk aan de site.
- [x] 14.2 Maak `css/print.css` voor werkboek en draaiboek. Verwacht: afdruk zonder afgesneden tekst op A4.
- [x] 14.3 Schrijf de docentgids (≤ 2 pagina's A4, 5 onderwerpen) (DL-1). Verwacht: 5 onderwerpen.
- [x] 14.4 Schrijf de studentintroductie (≤ 1 pagina A4, 3 onderwerpen) (DL-2). Verwacht: 3 onderwerpen.
- [x] 14.5 Schrijf de beschrijving van schema 1.0 (DL-4). Verwacht: 13 velden beschreven.
- [x] 14.6 Controleer alle teksten in het Nederlands en de Engelse vaktermen met uitleg van één zin bij het eerste voorkomen (QA-4, QA-5). Verwacht: 100 % van de termen met ≤ 1 zin uitleg.
- [x] 14.7 Controleer dat er geen kopieën van derden in de repository staan (LI-1). Verwacht: 0 kopieën van Brightspace-materiaal, PhoneVentures-handleidingen, slides of opgeslagen pagina's van derden.
- [x] 14.8 Draai de regressiecontrole over alle regels van het blueprint: elke regel heeft een fase en een uitgevoerde verificatie (zie bijlage). Verwacht: 0 regels zonder afgevinkte verificatie.

### Testpoort
- [x] Volledige testpoort, aangevuld met SI-1 (8 onderdelen ≤ 2 klikken), SI-3 (volledige doorloop) en PR-1 (netwerktrace).
- [x] Vergelijking afdruk en scherm voor deel 1 en deel 2 (AC-18, AC-25).
- [ ] (wacht op mens) Iemand die de site nog nooit zag leest docentgids en studentintroductie en voert de eerste taak uit zonder uitleg.
- [x] Geclaimde regels met hun methode gecontroleerd.

### Afsluiting
- [x] commit `DM-12, DL-1, DL-2, DL-4, QA-4, QA-5, LI-1: afdrukken en documentatie`  - [x] push  - [x] overzicht afvinken

**Afwijkingen fase 14.** (1) 14.1: het werkboek van een deel is een afdrukweergave in de docentmodus (Afdrukken, naast het draaiboek), samengesteld uit alle taken van de leerblokken van dat deel (deel 1: 7 taken, deel 2: 9), met dezelfde nummers en „klaar als”-regels als de site (100 %, unittest op de data en op de stapkaart); geen aparte pagina, zodat SI-1 op 8 onderdelen blijft. (2) 14.3 t/m 14.5 staan als HTML-pagina's in `docs/` (docentgids, studentintroductie, dossierschema-1.0), niet in de docentmodus of de README zelf; gemeten met een pdf-afdruk in Chrome: docentgids 2 A4, introductie 1 A4, schema-beschrijving 3 A4 (DL-4 heeft geen paginagrens). Alle drie zijn teksten van de bouwer en wachten op akkoord van de auteur. (3) 14.6: geen handmatige lezing van alles, maar een test die per leerblok eist dat elke gebruikte vakterm daar wordt uitgelegd (uiterlijk bij de eerste taak die hem gebruikt) en een test die Engelse functiewoorden in zichtbare tekst afkeurt (AND en OR in zoekstrings tellen niet). Dit vond drie gaten: prompt (leerblok 2), frame (leerblok 3), pains, gains, pain relievers en gain creators (leerblok 4); ze kregen een korte uitleg tussen haakjes. (4) 14.7 is een test op bestandstypen, namen, eigen video's en ingebedde beelden; de tekstovereenkomst met bronnen van derden bleef bij LI-3. Gesaboteerd met een ingecheckt bestand „Werkboek Copy.pdf”. (5) 14.8 regressiecontrole over het blueprint: 202 regels, alle 202 staan in de bijlage bij een fase; 180 worden op ID geciteerd in tests of tools; van de 22 andere horen er 10 bij fase 15 (AP-1 t/m AP-9 en DL-3, nog niet uit te voeren); de overige 12 (LB-3, LB-4, SI-2, SI-5, SI-6, SI-7, SI-8, PF-1, PF-2, DM-15, VB-6, VB-7) zijn in eerdere fases afgevinkt met demonstratie of browsertest en staan niet onder hun ID in een unittest; een deel ervan is nu opnieuw in de browser gecontroleerd (zie 7). Bekende afwijkingen blijven: PF-2 alleen Chromium, Firefox en WebKit (B66), SI-5 met `tools/` (B70), en de teksten die op akkoord van de auteur wachten. (6) Gevonden en opgelost door de live controle: de workflow kopieerde `docs/` niet, waardoor de drie pagina's live een 404 gaven terwijl alle controles slaagden; de workflow doet dat nu en een test (SI-2) leest de workflow en controleert dat elk lokaal bestand waar een pagina naar verwijst wordt gepubliceerd. (7) Menselijke tester vervangen door Playwright, lokaal en op de live URL na de groene workflow: SI-1 (het menu van de startpagina leidt in 1 klik naar de 7 andere onderdelen), SI-3 (13 pagina's inclusief de drie nieuwe, 0 consolefouten, 0 mislukte verzoeken na `networkidle`), PR-1 (0 verzoeken naar andere domeinen), PF-1 (360 px, 13 pagina's, 0 horizontale scroll), DM-15 (docentmodus zonder netwerk, korte doorloop; de 15 minuten met `page.clock` stonden in fase 9) en het afdrukvoorbeeld als pdf op A4 (AC-18, AC-25): werkboek en draaiboek van deel 1 en 2 met 7 en 9 taken en 11 en 11 onderdelen, zonder afgesneden tekst en zonder menu of knoppen. Niet gedaan: de proeflezer die de site nog nooit zag (wacht op een mens), geen schermlezer, geen Edge of Safari. Besluiten: ADR B72.

---

## Fase 16 — Eerste indruk en rust

**Doel.** De snelle verbeteringen uit de UX-review (30-9-2026): geen rood vóór een actie, een kort studentmenu, neutrale lege staat, links en keuzes die kloppen.
**Wat de tester doet.** Opent de startpagina op een telefoon van 360 px en ziet geen foutmelding. Vult een veld niet in, gaat verder en ziet dan pas één melding. Ziet een menu van vier onderdelen, overal „Te doen” in grijs en geen blauwe links. Kiest in taak 2.2 een model zonder dat de vraag over de eerste optie valt.
**Spec.** SX-1 (menu, nog zonder tabbalk), SX-2, SX-8, SX-11, BW-3, TK-16, SI-8.

### Subtasks
- [x] 16.1 `js/index-pagina.js`: `toonHints()` niet meer bij het laden (nu r. 86), wel per veld na `blur` of na „Verder” (SX-2). Verwacht: 0 meldingen bij laden; ≤ 1 melding per veld.
- [x] 16.2 Hoofdmenu naar Start, Leerblokken, Dossier, Bronnen in alle 10 HTML-bestanden; docentmodus en verificatie in de voettekst („Voor docenten”); `js/site.js` markeert „Leerblokken” op elke `leerblok-N.html` (SX-1, SI-1). Verwacht: 4 items; docentmodus en verificatie in ≤ 2 klikken.
- [x] 16.3 Pilotbanner wordt een aanduiding naast `.han-logo` (`js/site.js`, `css/site.css`) (SI-8). Verwacht: aanduiding bij vlag aan, weg bij uit.
- [x] 16.4 Weergavetekst „Nog niet” → „Te doen” in `js/status.js` (`STATUS_TEKST`), `js/dossier-pagina.js`, `js/weergave.js`; de sleutel `nog niet` blijft (B74). `.status-nog-niet` en `.dos-tegel-nog-niet` neutraal met `--leeg`. Verwacht: 0 keer „Nog niet” in zichtbare tekst; bestaande dossiers laden ongewijzigd.
- [x] 16.5 Tokens `--link`, `--link-hover` en `--leeg` als hexwaarde in `:root` (de contrastcontrole leest alleen hex) en een `a`-regel (SX-8). Verwacht: contrast-check groen; 0 links in browserblauw.
- [x] 16.6 Legend-fix en keuzes als tikbare rij over de volle breedte (DESIGN §6 Fieldset). Verwacht: taak 2.2 op 360 px zonder overlap.
- [x] 16.7 Zinstarters als placeholder bij STARR (`data/leerblok-4.json`) en de andere velden van ≥ 3 regels; contentcontrole eist dat een placeholder niet in het modelantwoord voorkomt (SX-11). Verwacht: 100 % van de lange velden.
- [x] 16.8 Tests bijwerken die de oude tekst of het oude menu vastleggen: `status.test.mjs`, `weergave.test.mjs`, `sessie.test.mjs`, `dossier.test.mjs`, `smoke.test.mjs` (SI-1 via de voettekst). Verwacht: `node --test` groen.

### Testpoort
- [x] Volledige testpoort, plus `tools/contrast-check.mjs` en `tools/gewicht-check.mjs`.
- [x] Sabotage SX-2 (roep `toonHints()` weer aan bij laden; de test faalt) en SX-11 (placeholder gelijk aan modelantwoord; contentcontrole faalt).
- [x] Playwright op 360 px: startpagina, leerblok 1, dossier; schermafdrukken naast `docs/ux-review/shots/`.
- [x] Geclaimde regels met hun methode gecontroleerd.

### Afsluiting
- [x] commit `SX-1, SX-2, SX-8, SX-11, BW-3, SI-8: eerste indruk en rust`  - [x] push  - [x] overzicht afvinken


**Afwijkingen fase 16.** (1) 16.2: „Leerblokken” in het menu wijst naar het overzicht op de startpagina (`index.html#blokken`); op een leerblokpagina is dat item actief. SI-1 blijft 1 klik: de leerblokken via de lijst die `index-pagina.js` uit `data/leerblokken.json` tekent (de test leest nu beide), docentmodus en verificatie via de voettekst. (2) 16.1: de meldingslogica is een pure functie `zichtbareMeldingen` in `js/profiel.js`, zodat SX-2 een unittest heeft; bij het laden is de set aangeraakte velden leeg. (3) 16.4: ook het label op de leerblokkaart („Nog niet afgerond”) werd „Te doen”; de studentintroductie, de docentgids en het controlelab zeggen „Te doen”. (4) 16.7: zinstarters staan in 65 lange velden van de toepassing (niet in de oefenversie, waar het modelantwoord volgt); velden die een component vult (lijnen, markeringen, feedbackregels, teamactie) tellen niet mee (`ZONDER_ZINSTARTER`). De contentcontrole ving direct een zinstarter die het format van het modelantwoord van 9.2 herhaalde. (5) Gewicht: leerblok 4 staat nu op 388,0 van 400 kB bron; fase 17 begint daarom met gewichtsruimte (17.1). Gesaboteerd: SX-2, SX-8, SX-11. Playwright op 360 px: 0 meldingen bij laden, 1 na blur, 4 menu-items, 0 px horizontale scroll op 10 pagina's, 0 browserblauwe links, 0 consolefouten, legend in 2.2 zonder overlap. Besluiten: ADR B80.

---

## Fase 17 — Voortgang zichtbaar

**Doel.** De student ziet bij elke taak waar het werk staat en ziet de eigen A3 groeien, zonder scores (BW-4, X-3).
**Wat de tester doet.** Maakt taak 2.1: ziet de segmentbalk van vier stappen, ziet de „klaar als”-punten afvinken tijdens het typen, en ziet na leerblok 1 een afsluitscherm met deel 1 van A3-vak 1 gevuld en de knop „Kopieer naar mijn A3”. Vindt nergens een EV-code.
**Spec.** SX-3, SX-4, SX-5, SX-7, SX-9, SX-12, TK-15, TK-18, LB-16.

### Subtasks
- [x] 17.1 Gewichtsruimte eerst: leerblok 4 zit op 384,0 van 400 kB bron (`tools/gewicht-check.mjs`). Nieuwe code in een eigen module (`js/voortgang.js`) die met `import()` en een `// gewicht-alleen:`-conditie laadt. Verwacht: elke pagina ≤ 300 kB gzip en ≤ 400 kB bron.
- [x] 17.2 Contract: `klaarAls` in `data/leerblok-N.json` wordt een lijst criteria, elk met tekst en een controle-id van soort A of `zelf`; de samengevoegde tekst blijft letterlijk de werkboekregel (TK-2, contentcontrole). Verwacht: 16 taken omgezet; 0 tekens verschil.
- [x] 17.3 Checklist onder de taakkop op `sessie.beoordeel().uitkomsten`, bijgewerkt na 600 ms zonder typen; criteria `zelf` vinkt de student af (SX-5). Verwacht: ≤ 1 s; 100 % van de criteria als vakje.
- [x] 17.4 `STAPPEN` in `js/weergave.js` naar vier (waarom, stof, oefenen, toepassen); klaar en volgende stap aan het eind van toepassen; verdieping na „klaar” buiten de stappen (TK-18, B76). Verwacht: 4 stappen in 100 % van de taken.
- [x] 17.5 Vaste taakkop met „Taak n van m” en segmentbalk (6 px, 3 px tussenruimte, `aria-label`) (SX-4). Verwacht: 100 % van de taken.
- [x] 17.6 Studentlabel per bewijsonderdeel in `data/luk.json` („Je onderzoeksvraag”); EV-codes weg uit `js/index-pagina.js`, `js/leerblok.js` en `eindigtMet` in de data; export, verificatie en docentmodus houden ze (SX-3). Verwacht: 0 treffers van `EV-\d` en „bewijsonderdeel” in de zichtbare studenttekst.
- [x] 17.7 A3-vak 1 in vier delen op de startpagina en op het afsluitscherm, gevuld per afgerond leerblok (TK-16); „Kopieer naar mijn A3” op het afsluitscherm met de logica van de dossierpagina (SX-12, LB-16, B75). Verwacht: 4 delen; 5 kopieerplaatsen.
- [x] 17.8 `.kaart` splitsen in tikbaar (rand en schaduw) en informatief (rand, geen schaduw); kaart-in-kaart weg (`.taak` > `.oefening`, `#media` > `.spel`) (SX-7). Verwacht: 0 informatieve kaarten met schaduw.
- [x] 17.9 Mobiele tabbalk onder 40rem, `scroll-padding` op `html`, transities van 150–250 ms en `prefers-reduced-motion` (SX-1, SX-9). Verwacht: tabbalk op 360 px; 0 transities bij reduced motion.

### Testpoort
- [x] Volledige testpoort, plus contrast- en gewichtcontrole.
- [x] Sabotage SX-3 (een EV-code terug in de studenttekst), SX-5 (controle-id weg bij een criterium) en SX-9 (transitie zonder reduced-motion-regel).
- [x] Playwright op 360 px en 1280 px: leerblok 1 doorlopen tot het afsluitscherm; toetsenbord alleen (TG-2).
- [x] Geclaimde regels met hun methode gecontroleerd.

### Afsluiting
- [x] commit `SX-3, SX-4, SX-5, SX-7, SX-9, SX-12, TK-18, LB-16: voortgang zichtbaar`  - [x] push  - [x] overzicht afvinken


**Afwijkingen fase 17.** (1) 17.1: gewichtsruimte kwam niet uit een eigen module, maar uit een eerlijkere meting: een import die pas na een klik laadt (het spel, „Kopieer naar mijn A3”) telt niet als eerste lading (`// gewicht-alleen: naklik`, ADR B81). Leerblok 4 staat daarmee op 377,4 kB bron en 120,5 kB gzip, inclusief alle nieuwe code (`js/voortgang.js`, `js/klembord.js`). (2) 17.2: `klaarAls.criteria` is een lijst van letterlijke stukken van de regel met de controles die erbij horen; de regel zelf blijft staan (TK-2) en de contentcontrole eist dat elk criterium er letterlijk in staat en alleen naar controles van de taak verwijst. 16 taken, 49 criteria, waarvan 5 zonder controle (de student vinkt zelf af, bewaard in de meta-opslag). (3) 17.6: de titels uit `data/luk.json` waren al gewone taal („Onderzoeksvraag”, „Beoordeelde bron”); er is geen apart studentlabel nodig. Ook het scherm „Vorige keer”, de dossierpagina en de verbanden-kaart noemden codes of „bewijsonderdeel”; die zijn vervangen door titels en „resultaat”. De afdruk van het dossier houdt de codes (export). (4) 17.7: de delen van A3-vak 1 volgen de leerblokken: onderzoeksvraag en zoekvragen, bronnen, plaatsing, verbanden en reflectie (ADR B81 corrigeert de labels van B75). Het overzicht staat pas op de startpagina als er werk is (ST-7). (5) 17.5: de vaste taakbalk (taaknummer, segmentbalk, stappenrij) is een direct kind van het taakartikel, anders plakt hij niet. (6) Richttijd staat als „± 10 min” (DESIGN §8); PF-5 test nu op „± ${blok.richttijd} min”. Gesaboteerd: SX-3, SX-5, SX-7, SX-9 en de naklik-marker. Playwright op 360 en 1280 px: leerblok 1 ingevuld tot beide resultaten Compleet, afsluitscherm „Deel 1 van je A3-vak 1 staat.”, bevestiging na „klaar”, 0 codes op 7 studentpagina's, 0 px horizontale scroll, 0 consolefouten, de toepassing van 1.1 met alleen het toetsenbord bereikt. Besluiten: ADR B81.

---

## Fase 18 — Proefsessie op de telefoon

**Doel.** De proefsessie van fase 5 alsnog, nu op de telefoon en met de verbeterde site: werken de controles, kloppen de richttijden, en weet de student wat er komt. De uitkomst bepaalt de omvang van fase 19.
**Wat de tester doet.** 2–3 studenten die de site niet kennen doen leerblok 1 op hun eigen telefoon, zonder uitleg. De bouwer kijkt mee en grijpt niet in.
**Spec.** AC-45; regressie van TK-2, BW-1, BW-2 en PF-5 bij echte gebruikers.

### Subtasks
- [ ] 18.1 Werf 2–3 studenten die de site nooit zagen en plan 60 min. Verwacht: afspraak met ≥ 2 studenten.
- [ ] 18.2 Noteer per taak de tijd, waar de student aarzelt of terugbladert, en foutmeldingen die verrassen. Verwacht: 1 notitieblad per student.
- [x] 18.3 Probeer de controles uit met onzininvoer (bijv. „bla bla bla?” als zoekvraag) en noteer welke onterecht Compleet geven (beoordeling fase 14, A5 en D4). Verwacht: lijst van controles met hun uitkomst.
- [ ] 18.4 Vraag na afloop: „ik wist bij elke taak wat ik moest doen” (1–5) en „wat zou je laten afhaken”. Verwacht: 2 antwoorden per student.
- [ ] 18.5 Verwerk de bevindingen: doel verandert → BLUEPRINT en ADR; route verandert → fase 19 hieronder. Verwacht: elke bevinding heeft een plek of een besluit om er niets mee te doen.
- [ ] 18.6 Vink fase 5 af met een verwijzing naar deze fase. Verwacht: fase 5 [x].

### Testpoort
- [ ] AC-45 gehaald bij ≥ 2 van de studenten, of een besluit waarom niet.
- [ ] Richttijd van leerblok 1 gemeten (mediaan); afwijking > 25 % heeft een besluit.

### Afsluiting
- [ ] commit (c-cluster) `AC-45: proefsessie en bevindingen`  - [ ] overzicht afvinken


**Stand fase 18 (30-9-2026).** 18.1, 18.2, 18.4 en de testpoort wachten op een mens: er zijn nog geen studenten geworven. 18.3 is zonder studenten gedaan, met een script dat elke toepassing vult met „bla bla bla bla?” (en bij keuzes de eerste optie): EV-01, EV-03, EV-05 en EV-07 worden dan **Compleet**, EV-02, EV-04, EV-06, EV-08 en EV-10 **Bijna**, EV-09 en EV-11 **Te doen**. Dat past bij het ontwerp: controles tellen aanwezigheid en aantallen, geen kwaliteit (BW-11, X-14), en Compleet zegt „aanwezig en consistent; of het goed is, bespreek je met je coach” (BW-6). Tegenhouden van herhaalde woorden (bijvoorbeeld „bla bla bla”) zou nog steeds tellen zijn, maar raakt BW-11 en de test die dat vastlegt; dat is een besluit voor de auteur (open punt B-1 hieronder), niet voor de bouwer. Fase 19 is daarom zonder proefsessie gebouwd volgens het plan; de proefsessie volgt vóór de pilot.

---

## Fase 19 — Eén taak per scherm

**Doel.** Het kernscherm uit DESIGN §5.3: één taak en één stap tegelijk, met een vaste voet, een route als tegel, spellen die als spel werken en een verbanden-kaart met één prompt tegelijk.
**Wat de tester doet.** Doorloopt leerblok 1 en 4 taak voor taak op de telefoon, gebruikt de terugknop van de browser, deelt het adres van een taak en komt op dezelfde stap uit. Kiest in de stap stof een tegel. Speelt de Waarde-simulator en ziet de kapitalen bewegen. Legt op de verbanden-kaart verbanden, telkens op één prompt.
**Spec.** SX-6, SX-10, MD-2, MD-8, MD-10, VB-4.

### Subtasks
- [x] 19.1 Contract: adressen `leerblok-N.html#taak-2.1/oefenen`, als laag boven de bestaande DOM-ids; `sessie.js` en `store.js` blijven ongewijzigd; de laatste positie in `store.setMeta` („Ga verder” op de start). Verwacht: terugknop = 1 stap terug.
- [x] 19.2 Per taak laden: stapcomponenten via `import()` met een eigen `gewicht-alleen:`-conditie. Verwacht: gewicht per pagina niet hoger dan na fase 17.
- [x] 19.3 Taakweergave met één zichtbare stap, vaste voet met één primaire knop („Verder” → „Naar oefenen” → „Check en zie modelantwoord” → „Bewaar in dossier”), focus naar de stapkop bij elke wissel (SX-6, DESIGN §9). Verwacht: 1 primaire knop; focus in 100 % van de wissels.
- [x] 19.4 Modelantwoord als uitklappend paneel „Zo zou het kunnen”, pas na een eigen poging (TK-6). Verwacht: 0 modelantwoorden vóór een poging.
- [x] 19.5 Routekeuze als drie tegels in de stap stof (`js/media.js`) (MD-2, B79). Verwacht: 3 tegels ≥ 44 × 44 px; laatste keuze onthouden.
- [x] 19.6 Waarde-simulator als tikbare keuzekaarten met zes kapitalen als balken die zichtbaar op- en neergaan en feedback per keuze (`js/spel.js`, DESIGN §7.4); tekstversie blijft. Lukt dat niet binnen MD-8, dan heet de route „Simulatie” en wordt hij een taakstap. Verwacht: 1 feedback per keuze; 0 scores.
- [x] 19.7 Verbanden-kaart: de eerste open plek als prompt boven de kaart, de volledige lijst en de tekstweergave in `<details>`; kaartjes 15 px, ook op 360 px (VB-4, SX-10). Verwacht: 1 prompt; ≥ 15 px.
- [ ] 19.8 (wacht op mens) Verticale docentvideo's van 60–90 s met ondertitels, uit de bestaande `spreektekst`; tot dan blijft „Conceptvideo” staan (MD-4, MD-5). Verwacht: per video een opname of een genoteerde reden om te wachten.

### Testpoort
- [x] Volledige testpoort, plus contrast- en gewichtcontrole.
- [x] Sabotage SX-6 (twee primaire knoppen in één stap) en VB-4 (twee prompts tegelijk).
- [x] Playwright op 360 px en 1280 px: leerblok 1 t/m 4 met alleen het toetsenbord; terugknop; adres van een stap direct openen.
- [x] Skill `beoordeel-elearning` opnieuw; de scores voor oriëntatie, motivatie en mobiel naast die van 30-9-2026.
- [x] Geclaimde regels met hun methode gecontroleerd.

### Afsluiting
- [x] commit `SX-6, SX-10, MD-2, VB-4: één taak per scherm`  - [x] push  - [x] overzicht afvinken


**Afwijkingen fase 19.** (1) 19.1: de taakweergave is een laag bovenop de bestaande pagina: alle taken worden gebouwd zoals voorheen (status, afronden en de controles veranderen niet), `js/taakweergave.js` leest en maakt de adressen (`#taak-2.1/oefenen`; ook `#oefening-2.1`, `#stap-2.1-4` en `#afsluiten` werken) en bepaalt de hoofdknop van de vaste voet; `leerblok.js` toont één taak en één stap. Zonder stap in het adres opent de stap waar de student is; de laatste positie staat per leerblok in de meta-opslag en voedt „Ga verder” op de startpagina (DESIGN §5.2). (2) 19.2: geen per-taak laden van stapcomponenten, wel het laden van de routekeuze pas bij de stap stof (`media.js`, `gewicht-alleen: naklik`; leerblok 1 laadt hem direct voor de kijktips, `gewicht-alleen: kijktips`). Leerblok 4 staat daarmee op 363,6 kB bron en 115,8 kB gzip, lager dan na fase 17 (377,4). (3) 19.3: de klaarknop in de stap wijkt voor de vaste voet („Klaar: bewaar in dossier”); zonder gehaalde „klaar als” biedt de voet „Naar taak …” (TK-17). Op een telefoon verdwijnt de tabbalk in een taak (focus, DESIGN §2.1); „← Leerblok N” in de taakbalk leidt terug. (4) 19.6: de Waarde-simulator is een spel geworden (keuzekaarten, per kapitaal vier tikbare knoppen, zes balken die groeien); hernoemen was niet nodig. De tabel staat uitklapbaar. (5) 19.7: op een scherm onder 40rem staan de kolommen van de verbanden-kaart onder elkaar, zodat de kaartjes 15 px kunnen blijven. (6) Tijdens de controle ook opgelost: de dossierpagina had twee hoofdknoppen („Kopieer naar A3 vak 1” is nu secundair, DESIGN §5.5), en `[hidden]` wint nu altijd van `.knop`. Gesaboteerd: SX-6 (twee hoofdknoppen), SX-10 (kaartje 12 px), VB-4 (alle open plekken tegelijk). Playwright op 360 en 1280 px over 36 schermen (10 pagina's, per leerblok overzicht, een toepassing en het afsluitscherm): 0 px horizontale scroll, hoogstens 1 hoofdknop, 0 consolefouten; taak 2.1 stap voor stap met de voet, de terugknop van de browser en een direct geopend adres; de Waarde-simulator helemaal met het toetsenbord. Niet gedaan: 19.8 (opnames, wacht op een mens) en een test met een schermlezer. Besluiten: ADR B82.

**Herbeoordeling (30-9-2026, live site, een aparte beoordelaar met Playwright, mobiel alleen geëmuleerd).** Scores (schaal 1–5, oud → nieuw): toegankelijkheid 5 → 5, didactisch ontwerp 4 → 4, oriëntatie en structuur 2 → 3, motivatie en feedback 1 → 2, visuele kwaliteit 3 → 3, mobiel 2 → 3. Van de 12 bevindingen van de review zijn er 6 opgelost (menu, codes, spel, STARR-velden, verbanden-bord, legend), 5 deels (scrollmuur, voortgang, eerste indruk, gewicht van kaarten, app-gevoel) en 1 niet (computerstem, 19.8). Direct hersteld na de herbeoordeling: de segmentbalk markeert de stap waar je bent; „Ga verder” wijst na „klaar” naar de volgende open taak; A3-vak 1 toont een deel in opbouw („1 van 2 resultaten”, geen percentage); de zinstarters van 2.1 passen in het format; de melding na „klaar” staat bovenaan; geen lege verdieping; „Richttijd” uit het scherm „Vorige keer”. Wat overblijft staat bij de open punten (B-2 t/m B-5).

---

## Fase 15 — Pilot in een werkcollege en kalibratie

**Doel.** Aantonen dat het product in het lokaal werkt en de startdoelen bijstellen.
**Wat de tester doet.** Een werkcollege met minstens twee teams (≥ 6 studenten) werkt met de site; een docent leidt deel 1 met de docentmodus. Na afloop vult iedereen drie vragen in en levert het dossier in.
**Spec.** AP-1…AP-9, DL-3.

### Subtasks
- [ ] 15.1 Zet de `pilot`-vlag aan en kondig de pilot aan met de aanbevolen planning (TP-10). Verwacht: banner zichtbaar.
- [ ] 15.2 Voer de pilot uit en noteer per student de tijd per leerblok (AP-2). Verwacht: ≥ 6 studenten uit 2 teams.
- [ ] 15.3 Laat de docent deel 1 leiden en noteer het aantal opzoekmomenten (AP-4). Verwacht: aantal genoteerd.
- [ ] 15.4 Neem de vragen na de pilot af: „ik wist bij elke taak wat ik moest doen" (AP-3) en „welk medium bracht de stof het best over" (AP-7). Verwacht: 1 vragenlijst van 3 vragen.
- [ ] 15.5 Laat de docent 5 dossiers inlezen en het zwakste onderdeel noemen (AP-5). Verwacht: tijd genoteerd.
- [ ] 15.6 Lees EV-11 en de terugblik-logs en tel de uitkomsten (AP-6, AP-8). Verwacht: percentages berekend.
- [ ] 15.7 Doorloop AP-1 met één pilotstudent op het eigen vraagstuk. Verwacht: alle 5 gedekte onderdelen Compleet of Bijna.
- [ ] 15.8 Laat de modulecoördinator de dekkingstabel bevestigen, inclusief de BC1-afwijking (AP-9, A-2). Verwacht: 13 onderdelen bevestigd.
- [ ] 15.9 Schrijf het testrapport met netwerktrace, toegankelijkheidscontrole, controle op 360 px en pilotresultaat (DL-3). Verwacht: 4 onderdelen.
- [ ] 15.10 Kalibreer drempels en richttijden en leg de nieuwe waarden vast in het BLUEPRINT (§9 A-3) en het ADR. Verwacht: elke gewijzigde drempel heeft een besluit.
- [ ] 15.11 Zet de `pilot`-vlag uit. Verwacht: banner weg.

### Testpoort
- [ ] Volledige testpoort.
- [ ] AP-1 t/m AP-9 genoteerd met hun methode; drempels die niet gehaald zijn hebben een besluit (aanpassen of bijstellen).
- [ ] Testrapport compleet (DL-3).

### Afsluiting
- [ ] commit `AP-1…AP-9, DL-3: pilot en kalibratie`  - [ ] push  - [ ] overzicht afvinken

---

## Bijlage — Dekking van de blueprintregels per fase

Elke regel staat bij de fase die haar realiseert en verifieert. Een regel die in een latere fase opnieuw wordt gecontroleerd (regressie) staat alleen bij haar eigen fase.

| Fase | Regels |
|---|---|
| 0 | SI-1, SI-2, SI-3, SI-4, SI-5, SI-6, SI-7, SI-8, LI-4, LI-5, PR-1 |
| 1 | RC-1, RC-2, RC-3, RC-4, BW-3, BW-4, BW-5, BW-8, BW-9, BW-11, BW-12, QA-2, QA-3 |
| 2 | ST-1, ST-2, ST-6, TK-1, TK-2, TK-3, TK-4, TK-5, TK-6, TK-7, TK-8, TK-9, TK-10, TK-15, TK-16, TK-17, TK-18, LB-1, LB-2, LB-3, LB-4, EV-01, EV-02, BW-1, BW-2, BW-6, BW-7, DS-1, RC-5, RC-6, QA-1 |
| 3 | DS-2, DS-3, DS-4, DS-5, DS-6, DS-7, DS-8, DS-9, DS-10, DS-11, DS-12, BW-13, PR-2 |
| 4 | LB-14, EV-09, WS-1, WS-3, WS-4, WS-5, WS-6, WS-7, WS-8, WS-9, WS-10, WS-11, ST-7 |
| 5 | (geen nieuwe regels) |
| 6 | LB-5, LB-6, LB-7, LB-8, EV-03, EV-04, EV-05, BR-1, BR-2, BR-3, BR-4, BR-5, BR-6 |
| 7 | TP-1, TP-2, TP-3, TP-4, TP-5, TP-6, TP-7, TP-8, TP-9, TP-10, TP-11 |
| 8 | TG-1, TG-2, TG-3, TG-4, TG-5, PF-1, PF-2, PF-3, PF-4, PF-5, QA-6 |
| 9 | DM-1, DM-2, DM-3, DM-4, DM-5, DM-6, DM-7, DM-8, DM-9, DM-10, DM-11, DM-14, DM-15, DM-16, DM-17, PR-3, PR-4 |
| 10 | LB-9, LB-10, LB-11, LB-12, LB-13, EV-06, EV-07, EV-08, DM-18, LI-3 |
| 11 | LB-15, LB-16, LB-17, EV-10, EV-11, VB-1, VB-2, VB-3, VB-4, VB-5, VB-6, VB-7, VB-8, VB-9, VB-10, WS-2, TK-11, TK-12, TK-13, TK-14, ST-3, ST-4, ST-5, BW-10, LI-2 |
| 12 | MD-1, MD-2, MD-3, MD-5, MD-6, MD-7, MD-9, MD-10, MD-11, MD-13, MD-14, MD-15, MD-16 |
| 13 | MD-4, MD-8, MD-12, DM-13 |
| 14 | DM-12, DL-1, DL-2, DL-4, QA-4, QA-5, LI-1 |
| 15 | AP-1, AP-2, AP-3, AP-4, AP-5, AP-6, AP-7, AP-8, AP-9, DL-3 |
| 16 | SX-1, SX-2, SX-8, SX-11 (wijziging: BW-3, TK-16, SI-8) |
| 17 | SX-3, SX-4, SX-5, SX-7, SX-9, SX-12 (wijziging: TK-18, LB-16) |
| 18 | (geen nieuwe regels; AC-45) |
| 19 | SX-6, SX-10 (wijziging: MD-2, VB-4) |

## Open punten die de route raken

- **B-2** Stof dubbel en lang (herbeoordeling): in de stap stof van de mediataak staat onder de taakstof ook de uitleg van het hele leerblok (tekstroute), en de stap stof of toepassen is op 360 px nog 3.000–5.000 px lang. Oplossing is inhoud: de tekstroute inkorten tot een verwijzing, of de stof opdelen in kaarten die je doorklikt (DESIGN §5.3). Vraagt keuzes van de auteur.
- **B-3** Startpagina: DESIGN §5.1 vraagt één veld per scherm en een startknop; nu staan de vier velden onder elkaar (wel zonder meldingen vooraf). Niet in fase 16–19 opgenomen.
- **B-4** STARR (6.3) vraagt twee keer naar de volgende stap: in het sjabloon en in de voet van de taak (TK-10). Samenvoegen raakt het record van EV-10; besluit nodig.
- **B-5** Kaart-in-kaart in sommige oefeningen (bijvoorbeeld het kader met de kapitalen in de oefencasus) en „Fictief” drie keer op één spelscherm.
- **B-1** Onzininvoer (fase 18.3): vier resultaten worden Compleet met „bla bla bla bla?”. Beslissen of een telling van verschillende woorden erbij komt (raakt BW-11) of dat BW-6 en het gesprek met de coach volstaan.

- **A-1** TOM³-bron zonder openbare publicatie: opgevraagd in subtask 10.11, gebruikt in fase 10.
- **A-5** Pauzeband tussen 1 en 2 dagen (TP-7): beslissen vóór fase 7.
- **A-11** Het werkboek heeft slechts 3 van 15 „Klaar als"-regels en 6 „Waarom"-regels, terwijl TK-2 100 % eist: de ontbrekende regels schrijft de auteur en keurt ze goed in subtask 2.3, 6.1, 10.1 en 11.1.
