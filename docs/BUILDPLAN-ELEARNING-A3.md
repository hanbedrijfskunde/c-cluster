# BUILDPLAN — Hybride e-learning A3 met automatisch bewijs

> Route en voortgang van [BLUEPRINT-ELEARNING-A3.md](BLUEPRINT-ELEARNING-A3.md). Het blueprint beschrijft de doelsituatie; dit bestand beschrijft de volgorde en **is** de voortgang: vink af wat af is, in dit bestand, en nergens anders. Regel-ID's (SI-1, EV-01, …) verwijzen naar het blueprint. Ontwerpbesluiten staan in [ADR-ELEARNING-A3.md](ADR-ELEARNING-A3.md), de onderbouwing in [LRD-ELEARNING-A3.html](LRD-ELEARNING-A3.html).
>
> Gebouwd wordt in een lokale kloon van `https://github.com/hanbedrijfskunde/a3-learning` (branch `main`). Dit plan blijft in `c-cluster/docs/` staan, bij de andere twee documenten.

## Werkafspraken

- **Elke fase eindigt in iets wat een mens kan proberen** (het blok „Wat de tester doet").
- **Elke fase eindigt met een volledige testpoort.** Pas daarna: commit, push, en dan de volgende fase. Een push naar `main` publiceert de site alleen als de workflow groen is (SI-6).
- **Volledige testpoort** = `node --test tests/` (unittests), `node tools/content-check.mjs`, `node tools/link-check.mjs`, een volledige doorloop van alle bestaande pagina's op de gepubliceerde URL zonder consolefout (SI-3), en 0 verzoeken naar andere domeinen in de netwerktrace (PR-1). Elke fase voegt daar haar eigen punten aan toe.
- **Verificatie per regel.** Bij elke fase staat welke regels ze claimt; die worden gecontroleerd met de verificatiemethode uit het blueprint. Sluit de fase niet met een regel die je alleen hebt gelezen.
- **Sabotagetest.** Elke nieuwe controle en elke nieuwe test wordt eenmaal gesaboteerd (breek het gedrag, zie de test falen, herstel). Een test die niet kan falen telt niet.
- **Bevindingen terug in de documenten, in dezelfde wijziging.** Verandert er iets aan het doel: BLUEPRINT (eigen commit in c-cluster) en, bij een ontwerpkeuze, ADR (nieuwe regel onderaan). Verandert er iets aan route of stand: dit bestand.
- **Commitberichten** noemen de regel-ID's die de commit realiseert, bijvoorbeeld `EV-01: controle op drie velden (BW-8)`.
- **Volgorde binnen een fase:** eerst het contract (schema, bestandsformaat, API), dan de invulling. Een subtask is één handeling, bij voorkeur één bestand, met het verwachte resultaat erbij.

## Voortgang

- [ ] Fase 0 — Repository, licentie en lege publicatie
- [ ] Fase 1 — Kern: schema, controles en statusregel (met controlelab)
- [ ] Fase 2 — Leerblok 1 als dunne doorsnede (EV-01, EV-02)
- [ ] Fase 3 — Dossier: export, import en verificatie
- [ ] Fase 4 — De Wissel en de feedbacklog (EV-09)
- [ ] Fase 5 — Proefsessie met 2–3 gebruikers en bijstelling
- [ ] Fase 6 — Leerblok 2 en de bronnenpagina (EV-03 t/m EV-05)
- [ ] Fase 7 — Terugblik en werken met tussenpozen
- [ ] Fase 8 — Huisstijl, toegankelijkheid, responsive en offline
- [ ] Fase 9 — Docentmodus: mechaniek en deel 1
- [ ] Fase 10 — Leerblok 3 en docentmodus deel 2 (EV-06 t/m EV-08)
- [ ] Fase 11 — Leerblok 4: verbanden, reflectie en afronding (EV-10, EV-11)
- [ ] Fase 12 — Media: mechaniek, twee video's en twee spellen
- [ ] Fase 13 — Media: de overige video's en spellen
- [ ] Fase 14 — Afdrukken, documentatie en eindcontrole
- [ ] Fase 15 — Pilot in een werkcollege en kalibratie

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

---

## Fase 0 — Repository, licentie en lege publicatie

**Doel.** Een lege maar echt gepubliceerde site, met de poorten die alle latere fasen bewaken.
**Wat de tester doet.** Opent `https://hanbedrijfskunde.github.io/a3-learning/`, klikt door 8 stubpagina's zonder 404 en ziet licentie en naamsvermelding onderaan. Duwt daarna een testcommit met een falende test naar een aparte branch en ziet dat de workflow rood wordt en niets publiceert.
**Spec.** SI-1 (stubs), SI-2, SI-3, SI-4, SI-5, SI-6, SI-7, SI-8, LI-4, LI-5, PR-1.

### Subtasks
- [ ] 0.1 Kloon de lege repository lokaal. Verwacht: map `a3-learning/` met alleen `.git`.
- [ ] 0.2 Voeg `LICENSE` toe met de volledige tekst van CC BY-SA 4.0 (LI-4). Verwacht: 1 bestand, de tekst begint met „Attribution-ShareAlike 4.0 International".
- [ ] 0.3 Voeg `.nojekyll` toe (leeg) en `README.md` met wat de site is, de licentie en een verwijzing naar de docentgids (SI-5). Verwacht: README noemt „docentgids".
- [ ] 0.4 Maak 8 stubpagina's met relatieve links naar elkaar: `index.html`, `leerblok-1.html` t/m `leerblok-4.html`, `dossier.html`, `verificatie.html`, `docent.html` (SI-1, SI-3). Verwacht: elke pagina bereikbaar in ≤ 2 klikken vanaf `index.html`.
- [ ] 0.5 Voeg op elke stub een voettekst toe met licentie-aanduiding, naamsvermelding en link naar de licentietekst (LI-5), en een `pilot`-banner die aan of uit staat via `data/config.json` (SI-8). Verwacht: banner zichtbaar bij `"pilot": true`, weg bij `false`.
- [ ] 0.6 Maak `tools/link-check.mjs`: controleert dat alle interne links resolven en dat er 0 absolute interne links zijn. Verwacht: exit 0 op de stubs.
- [ ] 0.7 Maak `tools/content-check.mjs` als skelet dat exit 0 geeft op lege `data/`. Verwacht: exit 0.
- [ ] 0.8 Maak `tests/smoke.test.mjs` met één test die de 8 pagina's inleest. Verwacht: `node --test tests/` groen.
- [ ] 0.9 Schrijf `.github/workflows/pages.yml`: bij elke push `node --test tests/`, `content-check`, `link-check`; alleen publiceren als alle drie slagen; faalmelding noemt de falende controle (SI-6, SI-7). Verwacht: 3 stappen met eigen naam.
- [ ] 0.10 Zet GitHub Pages aan (bron: GitHub Actions) in de repository-instellingen. Verwacht: Pages-instelling toont „GitHub Actions".

### Testpoort
- [ ] Volledige testpoort (lokaal: `python3 -m http.server` en doorloop).
- [ ] Sabotage SI-6: op branch `test/rood` een falende test pushen; workflow rood, geen publicatie (0 nieuwe deploys).
- [ ] Sabotage link-check: een absolute interne link toevoegen; `link-check` faalt.
- [ ] Netwerktrace op de gepubliceerde URL: 0 verzoeken naar andere domeinen (PR-1).
- [ ] Elke geclaimde regel gecontroleerd met de methode uit het blueprint (SI-1 Test, SI-2 Demonstratie, SI-3 Test, SI-4 Inspectie, SI-5 Inspectie, SI-6 Test, SI-7 Test, SI-8 Test, LI-4 Inspectie, LI-5 Inspectie, PR-1 Test).

### Afsluiting
- [ ] commit `SI-1…SI-8, LI-4, LI-5: lege site met publicatiepoort`  - [ ] push  - [ ] overzicht afvinken

---

## Fase 1 — Kern: schema, controles en statusregel (met controlelab)

**Doel.** De pure logica die elk latere leerblok gebruikt: recordvorm, controlecontract, statusregel.
**Wat de tester doet.** Opent `controlelab.html`, plakt een bewijsrecord (JSON), kiest de uitkomsten van controles per soort A, B en C en ziet de status en de melding. Alle 27 combinaties van de statusregel zijn met een knop na te lopen.
**Spec.** RC-1, RC-2, RC-3, RC-4, BW-3, BW-4, BW-5, BW-8, BW-9, BW-11, BW-12, QA-2, QA-3.

### Subtasks
- [ ] 1.1 Schrijf `js/schema.js` met de recordvorm van §5 (13 velden) en een `valideer(record)` (RC-1). Verwacht: geldig record → `true`, record met 12 velden → foutmelding met het ontbrekende veld.
- [ ] 1.2 Voeg aan `schema.js` toe dat `luk` en `bc` uit een taakdefinitie komen en niet uit de invoer (RC-2) en dat `alias` of `naam` in `inhoud` wordt geweigerd (RC-3). Verwacht: 2 tests.
- [ ] 1.3 Leg de scheiding `inhoud` / `controles` vast in het schema (RC-4). Verwacht: record met controles binnen `inhoud` → afgewezen.
- [ ] 1.4 Schrijf `js/status.js` met `bepaalStatus(controles)` volgens de statusregel, „Nog niet" gaat voor „Bijna" gaat voor Compleet (BW-5). Verwacht: 27 combinaties (3 soorten × 3 resultaten) geven de tabel uit §5.
- [ ] 1.5 Schrijf `js/checks/core.js` met het controlecontract `(invoer, context) → { id, soort, resultaat, melding }` en hulpfuncties `veldGevuld`, `minWoorden`, `keuzeUitLijst`, `eindigtOp` (BW-8, BW-9). Verwacht: zuiver, 0 netwerkaanroepen (test met een geblokkeerde `fetch`).
- [ ] 1.6 Verbied in `core.js` inhoudelijk oordelen: soort C telt alleen woorden en zinnen (BW-11). Verwacht: 1 test die bevestigt dat controles van soort C alleen `telWoorden` en `telZinnen` aanroepen.
- [ ] 1.7 Schrijf `tests/status.test.mjs` en `tests/core.test.mjs` met per controle 3 goede en 3 zwakke voorbeelden (QA-2). Verwacht: 6 voorbeelden per helper, allemaal groen.
- [ ] 1.8 Breid `tools/content-check.mjs` uit: elke taak in `data/leerblok-*.json` heeft LUK-koppeling, „klaar als", ≥ 1 controle en modelantwoord (QA-3), en elk bewijsonderdeel heeft ≥ 1 LUK-onderdeel (BW-12). Verwacht: op een testfixture met 4 ontbrekende onderdelen → 4 fouten.
- [ ] 1.9 Maak `controlelab.html` (alleen voor de tester; niet gelinkt vanaf `index.html`, wel in de sitemap van `README.md`). Verwacht: plakken van een record toont status en controles.
- [ ] 1.10 Toon in het controlelab de statussen als tekst naast kleur en zonder score (BW-3, BW-4). Verwacht: 0 getallen als score in de UI.

### Testpoort
- [ ] Volledige testpoort.
- [ ] Sabotage BW-5: draai de voorrang om (Bijna gaat voor „Nog niet"); minstens 1 van de 27 combinaties faalt.
- [ ] Sabotage BW-8: laat een controle `fetch` aanroepen; de test faalt.
- [ ] Sabotage QA-3: haal een „klaar als" uit de fixture; `content-check` faalt met de taak in de melding.
- [ ] Tester loopt in het controlelab alle 27 combinaties na en vergelijkt met §5.
- [ ] Geclaimde regels met hun methode gecontroleerd (RC-1…RC-3 Test, RC-4 Inspectie, BW-3 Test, BW-4 Inspectie, BW-5 Test, BW-8 Test, BW-9 Test, BW-11 Inspectie, BW-12 Test, QA-2 Test, QA-3 Test).

### Afsluiting
- [ ] commit `RC-1…RC-4, BW-3…BW-12, QA-2, QA-3: schema, controlecontract, statusregel`  - [ ] push  - [ ] overzicht afvinken

---

## Fase 2 — Leerblok 1 als dunne doorsnede (EV-01, EV-02)

**Doel.** Van begin tot eind één leerblok waarmee het contract van de site vastligt: start, taak, controle, opslag, afsluiten.
**Wat de tester doet.** Opent de site, vult alias, teamnummer, vraagstuk en waarom-zin in (of kiest „nog geen scherp vraagstuk"), doet taak 2.1 en 2.2 op de oefencasus en op het eigen vraagstuk, ziet live wat er ontbreekt, herlaadt de pagina en vindt alles terug, sluit het leerblok af en ziet de status. „Wis alles" leegt de browseropslag.
**Spec.** ST-1, ST-2, ST-6, TK-1…TK-10, TK-15…TK-18, LB-1, LB-2, LB-3, LB-4, EV-01, EV-02, BW-1, BW-2, BW-6, BW-7, DS-1, RC-5, RC-6, QA-1.

### Subtasks
- [ ] 2.1 Leg het formaat van `data/leerblok-1.json` vast (taak, nummer, waarom, klaar als, richttijd, oefencasus, modelantwoord, controles, LUK-koppeling, verdieping) en beschrijf het in `README.md` (QA-1). Verwacht: één voorbeeldtaak valideert tegen het formaat.
- [ ] 2.2 Schrijf `js/store.js`: `get`, `save` (met `versie + 1` en behoud van eerdere versies), `versions`, `clear` (RC-5, RC-6, ST-6, DS-1). Verwacht: na 5 opslagen 5 versies en `versie` loopt 1…5.
- [ ] 2.3 Vul `data/leerblok-1.json` met taken 1.1, 2.1, 2.2: de teksten uit het werkboek; **ontbrekende „Waarom" en „Klaar als" (alleen 2.1 heeft een „Klaar als") voor de auteur schrijven en laten goedkeuren** voordat ze de site in gaan (TK-2). Verwacht: 3 taken, elk met waarom en „klaar als", door de auteur bevestigd.
- [ ] 2.4 Schrijf `js/leerblok.js`: bouwt de pagina uit het datafile met het vaste ritme van vijf stappen (TK-18) en toont per taak nummer, waarom, tijd en „klaar als" (TK-2). Verwacht: 3 taken, alle vier elementen zichtbaar.
- [ ] 2.5 Bouw de startpagina-invoer: alias of voornaam, teamnummer, vraagstuk in één zin, waarom-zin, of „nog geen scherp vraagstuk"; privacytekst ≤ 100 woorden op `index.html` (ST-1, ST-2). Verwacht: 4 velden + 1 keuze, 0 andere persoonsgegevensvelden.
- [ ] 2.6 Bouw de oefen/toepassen-scheiding: aparte oefenversie met modelantwoord dat pas verschijnt na ≥ 1 ingevuld veld, herhaalbaar (≥ 10×) en overslaanbaar met één klik (TK-3, TK-5, TK-6, TK-7). Verwacht: modelantwoord verborgen bij leeg veld; overslaan verandert 0 statussen.
- [ ] 2.7 Zorg dat alleen de toepassing als bewijsrecord wordt opgeslagen (TK-4). Verwacht: 0 records met oefencasus-inhoud.
- [ ] 2.8 Schrijf `js/checks/lb1.js` met de controles van EV-01 en EV-02 uit het blueprint (soort A en B) en de bouwer van LB-2 (drie velden, zes kapitalen, live voorbeeld ≤ 1 s) en LB-3 (drie zoekvragen, frame-keuzelijst, één model uit 4, veld „wat mis je"); teamkeuze en eigen verantwoording apart (LB-4). Verwacht: alle controles hebben 3 goede en 3 zwakke voorbeelden.
- [ ] 2.9 Verbind de controles met de invoer: resultaat ≤ 1 s na de laatste toetsaanslag, één zin per niet-`ok`-controle, statustekst en, bij Compleet, de zin „Aanwezig en consistent…" en, bij „Nog niet", de lijst met een link naar het modelantwoord (BW-1, BW-2, BW-6, BW-7). Verwacht: meetbare vertraging ≤ 1 s.
- [ ] 2.10 Bouw de knop „klaar", de zin „mijn volgende stap" en de aanbevolen volgorde zonder slot; blokkeer niemand bij overschrijding van de richttijd (TK-1, TK-8, TK-9, TK-10). Verwacht: „klaar" werkt bij ≤ 50 % van de richttijd; 0 blokkades bij 150 %.
- [ ] 2.11 Bouw het afsluitscherm met status per bewijsonderdeel, volgende stap en de melding „bewaar je dossier"; de afgerond-regel en doorgaan zonder afronden (TK-15, TK-16, TK-17). Verwacht: 4 testprofielen geven het verwachte resultaat.
- [ ] 2.12 Toon de vier leerblokken op de startpagina met richttijd en afgerond bewijs (LB-1) en voeg de verdiepingstaak van leerblok 1 toe (nog zonder invloed op de status). Verwacht: 4 leerblokken op `index.html`.
- [ ] 2.13 Bouw „wis alles" met één bevestiging (ST-6). Verwacht: 0 items van de site in localStorage, sessionStorage en IndexedDB.
- [ ] 2.14 Laat `content-check` de eerste 3 taken valideren. Verwacht: groen.

### Testpoort
- [ ] Volledige testpoort, met leerblok 1 als extra doorloop op de gepubliceerde URL.
- [ ] Sabotage TK-6: maak het modelantwoord direct zichtbaar; de test faalt.
- [ ] Sabotage TK-4: sla oefencasus-invoer op als bewijs; de test faalt.
- [ ] Tester doorloopt: start → 2.1 → 2.2 → afsluitscherm → herladen → alles aanwezig → „wis alles" → leeg.
- [ ] DS-1: 0 verloren velden na herladen.
- [ ] Geclaimde regels met hun methode gecontroleerd; TK-2 als Test tegen de werkboektekst.

### Afsluiting
- [ ] commit `Leerblok 1: doorsnede met start, EV-01, EV-02, opslag en afsluiten`  - [ ] push  - [ ] overzicht afvinken

---

## Fase 3 — Dossier: export, import en verificatie

**Doel.** Wat de student inlevert en wat de docent nakijkt, zonder server.
**Wat de tester doet.** Exporteert een dossier (JSON en afdrukbare pagina), wijzigt één teken in het JSON-bestand, leest beide bestanden in op `verificatie.html` en ziet „gewijzigd na export" bij de gewijzigde en niets bij de ongewijzigde. Importeert het dossier in een schoon browserprofiel. Leest vijf testdossiers tegelijk in.
**Spec.** DS-2…DS-12, BW-13, PR-2.

### Subtasks
- [ ] 3.1 Schrijf `data/luk.json` met de 13 onderdelen van §4.3 (dekking, bewijs) en toon ze op `dossier.html` met de eigen status (BW-13). Verwacht: 13 rijen; onderdelen met EV-01/02 tonen de status uit het dossier.
- [ ] 3.2 Schrijf `js/dossier.js`: export als JSON met records (nieuwste versie en aantal eerdere), alias, teamnummer, e-learningversie (DS-5) en een SHA-256 over de inhoud via `crypto.subtle` (DS-6). Verwacht: controlesom van 64 hexadecimale tekens.
- [ ] 3.3 Bouw de afdrukbare pagina per leeruitkomst (LUK 1, 2, 5) met status per bewijsonderdeel, inhoud en controlesom onderaan (DS-7). Verwacht: 3 pagina's.
- [ ] 3.4 Bouw import met controle op schemaversie 1.x (DS-3, DS-4). Verwacht: 0 verschillen tussen records vóór export en na import.
- [ ] 3.5 Toon de melding „bewaar je dossier" na elk leerblok en na elke 10 wijzigingen (DS-2). Verwacht: 1 melding per 10 wijzigingen.
- [ ] 3.6 Bouw de verificatiepagina: lokaal inlezen, controlesom herberekenen, „gewijzigd na export" bij afwijking (DS-8), geen uitgaande verzoeken (DS-10). Verwacht: 1 gewijzigd teken → melding; ongewijzigd → geen melding.
- [ ] 3.7 Laat de verificatiepagina meerdere dossiers tegelijk inlezen met een tabel per student en per leeruitkomst, ontbrekende onderdelen bovenaan (DS-9). Verwacht: 5 dossiers, 11 bewijsonderdelen en 3 leeruitkomsten per student.
- [ ] 3.8 Bouw „Mijn stand": per bewijsonderdeel alleen de status, groot, zonder inhoud (DS-11). Verwacht: 0 inhoudsvelden.
- [ ] 3.9 Meld geblokkeerde browseropslag en bied direct export aan (DS-12). Verwacht: in een privévenster 1 melding en 1 exportknop ≤ 1 s na laden.
- [ ] 3.10 Maak 5 testdossiers in `tests/fixtures/` (waaronder 1 met gewijzigde inhoud). Verwacht: 5 bestanden.
- [ ] 3.11 Schrijf `tests/dossier.test.mjs` voor SHA-256, import en verificatie. Verwacht: groen.

### Testpoort
- [ ] Volledige testpoort.
- [ ] Sabotage DS-8: rond de controlesom af zodat een gewijzigd teken niet opvalt; de test faalt.
- [ ] Netwerktrace tijdens export en verificatie: 0 uitgaande verzoeken met dossierinhoud (DS-10, PR-2).
- [ ] Tester: export → wijzig 1 teken → verificatie → melding; import in schoon profiel → alles terug.
- [ ] Geclaimde regels met hun methode gecontroleerd.

### Afsluiting
- [ ] commit `DS-2…DS-12, BW-13: dossier, import en verificatiepagina`  - [ ] push  - [ ] overzicht afvinken

---

## Fase 4 — De Wissel en de feedbacklog (EV-09)

**Doel.** Feedback geven en ontvangen zonder server.
**Wat de tester doet.** Twee testers (twee browsers) wisselen een wisselblok via het klembord, leggen „ik zie / ik mis / ik vraag me af" vast en ontvangen de feedback terug. Een letterlijke kopie van het wisselblok in de eigen EV-01 geeft „let op".
**Spec.** LB-14, EV-09, WS-1, WS-3…WS-11, ST-7.

### Subtasks
- [ ] 4.1 Schrijf `js/wissel.js` met `maakWisselblok(records)` (onderzoeksvraag en zoekvragen, zonder alias) (WS-1). Verwacht: 0 aliassen in het blok, 1 klik naar klembord.
- [ ] 4.2 Bouw plakken van het wisselblok van een wisselpartner met de rollen teamgenoot, medestudent en coach (WS-3). Verwacht: 3 rollen geaccepteerd.
- [ ] 4.3 Bouw de feedbacklog: ik zie, ik mis, ik vraag me af, rol, actie, status; onbeperkt regels (LB-14, WS-4). Verwacht: 6 velden, ≥ 10 regels.
- [ ] 4.4 Laat de feedback via het klembord terugkomen en als ontvangen en gegeven verschijnen in EV-09 (WS-5). Verwacht: 1 ontvangen en 1 gegeven regel na een uitwisseling.
- [ ] 4.5 Schrijf de controles van EV-09 in `js/checks/lb4.js` (alleen de EV-09-controles) en de kopiecontrole voor EV-01 en EV-02 (WS-7, EV-09). Verwacht: 0 tekens verschil → `let op`, status Bijna.
- [ ] 4.6 Laat EV-09 op Bijna staan zolang er geen feedback is, ook na ≥ 14 dagen (WS-8). Verwacht: test met aangepaste tijdstempels.
- [ ] 4.7 Voeg de flow voor de post-its van andere teams toe met de rol „ander team" en één teamactie (WS-6). Verwacht: zichtbaar op de dossierpagina naast individuele feedback.
- [ ] 4.8 Toon de privacytekst bij de Wissel met het klembord als kanaal, ≤ 60 woorden (WS-10). Verwacht: 1 tekst in de flow.
- [ ] 4.9 Toon een herinnering bij een actie die ≥ 7 dagen dezelfde status heeft (WS-11). Verwacht: 1 herinnering na 7 dagen, 0 bij 6 dagen.
- [ ] 4.10 Toon de Wissel pas na de eerste versie van EV-02 (ST-7). Verwacht: in de eerste 4 schermen van leerblok 1 zichtbaar 0 Wissel-elementen.
- [ ] 4.11 Bevestig dat de Wissel zonder server werkt (WS-9). Verwacht: 0 verzoeken met wisselblokinhoud.

### Testpoort
- [ ] Volledige testpoort.
- [ ] Sabotage WS-7: schakel de kopiecontrole uit; de test faalt.
- [ ] Tester met 2 browsers: uitwisseling, kopiecontrole, feedback terug (AC-23).
- [ ] Geclaimde regels met hun methode gecontroleerd (WS-2 valt in fase 11).

### Afsluiting
- [ ] commit `WS-1, WS-3…WS-11, LB-14, EV-09: Wissel en feedbacklog`  - [ ] push  - [ ] overzicht afvinken

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
- [ ] 6.1 Vul `data/leerblok-2.json` met taken 3.1, 3.2, 4.1, 4.2 uit het werkboek; **ontbrekende „Waarom" en „Klaar als" voor de auteur schrijven en laten goedkeuren** (TK-2). Verwacht: 4 taken volledig, goedgekeurd.
- [ ] 6.2 Schrijf `js/checks/lb2.js` met de controles van EV-03, EV-04, EV-05 (operatoren, `https://` of `doi.org`, jaar in APA gelijk aan jaarveld, 5 oordelen met toelichting). Verwacht: 3 goede en 3 zwakke voorbeelden per controle.
- [ ] 6.3 Bouw de zoektermentabel, het zoekstringveld met operatorcontrole en de keuze route A/B (LB-5). Verwacht: 1 tabel, 1 veld, 2 routes.
- [ ] 6.4 Bouw de promptgenerator met waarschuwing bij woorden uit de „niet noemen"-lijst (LB-6). Verwacht: 0 gemiste woorden in 6 testprompts.
- [ ] 6.5 Bouw de bronlog met AAOCC-oordelen, twee verificatievinkjes bij route B, besluit, APA-veld met formaatcontrole en meerdere bronnen (LB-7). Verwacht: ≥ 2 bronnen invoerbaar.
- [ ] 6.6 Bouw de stelling met keuze en argument (LB-8). Verwacht: 2 kanten, 1 argumentveld.
- [ ] 6.7 Zet de bronnen van het LRD (bijlage A, literatuurregels) om naar `data/bronnen-1.json` en `-2.json` in APA, 7e editie, met „ongepubliceerd document" waar geen openbare publicatie bestaat (BR-3). Verwacht: elke bron met auteur, jaar, titel en link waar die bestaat.
- [ ] 6.8 Schrijf `bronnen.html`: alle bronnen alfabetisch met werkende link (BR-1, BR-2) en in-tekstverwijzingen `(Auteur, jaar)` die naar de bronregel klikken (BR-4). Verwacht: 100 % van de verwijzingen klikt door.
- [ ] 6.9 Breid `content-check` uit: faalt bij een verwijzing zonder bronregel of een bronregel zonder citatie (BR-5). Verwacht: 0 wezen.
- [ ] 6.10 Breid `link-check` uit met een controle op alle DOI's en URL's uit de bronnen, en laat de workflow die bij elke publicatie draaien (BR-6). Verwacht: dode link → workflow rood.
- [ ] 6.11 Markeer fictieve bronkaarten als „fictief" in de datafiles voor het later te bouwen spel (voorbereiding MD-15). Verwacht: veld `fictief: true` waar van toepassing.

### Testpoort
- [ ] Volledige testpoort, inclusief link-check op alle DOI's.
- [ ] Sabotage BR-5: voeg een verwijzing zonder bronregel toe; `content-check` faalt.
- [ ] Sabotage BR-6: zet een DOI op een niet-bestaande waarde; de workflow faalt.
- [ ] Tester doorloopt leerblok 2 en klikt 3 verwijzingen door.
- [ ] Geclaimde regels met hun methode gecontroleerd (BR-1 Test, BR-2 Test, BR-3 Inspectie, BR-4 Test, BR-5 Test, BR-6 Test).

### Afsluiting
- [ ] commit `LB-5…LB-8, EV-03…EV-05, BR-1…BR-6: leerblok 2 en bronnenpagina`  - [ ] push  - [ ] overzicht afvinken

---

## Fase 7 — Terugblik en werken met tussenpozen

**Doel.** Elk leerblok vanaf 2 begint met ophalen, vergelijken en toepassen, en de site overleeft de pauze.
**Wat de tester doet.** Zet met testprofielen de tijdstempels van het dossier op 1 uur, 1 dag, 5 dagen en 14 dagen terug en opent leerblok 2 (en de stubs van 3 en 4). Ziet steeds de juiste terugblik. Maakt de browseropslag leeg en ziet een importaanbod.
**Spec.** TP-1…TP-11.

### Subtasks
- [ ] 7.1 Leg `data/terugblik.json` vast en vul het met de kaarten van LRD 8.5 (drie blokken: items, twee kennisvragen, transfervraag). Verwacht: 3 kaarten, 2 kennisvragen per kaart.
- [ ] 7.2 Schrijf `js/terugblik.js` met `pauzeInDagen(dossier)` uit de tijdstempels (TP-6). Verwacht: 0 dagen afwijking van het verschil tussen de tijdstempels.
- [ ] 7.3 Voeg `bandbreedte(pauze)` toe: < 2 uur / < 2 dagen / 2–13 dagen / ≥ 14 dagen (TP-7). Verwacht: 4 profielen (1 uur, 1 dag, 5 dagen, 14 dagen) geven de verwachte terugblik.
- [ ] 7.4 Bouw het scherm „Vorige keer" dat achtereenvolgens de dossiercontrole, de terugblik met meenemen-kaart en de transfervraag toont (TP-11, TP-1). Verwacht: 1 scherm, 3 onderdelen in vaste volgorde, terugblik ≤ 15 min.
- [ ] 7.5 Bouw ophalen vóór de kaart: ≥ 3 punten en 2 kennisvragen, pas dan de kaart met items en eigen bewijsstukken (TP-2, TP-3). Verwacht: kaart 0× zichtbaar vóór 3 punten of „ik weet het nog".
- [ ] 7.6 Bouw de transfervraag van twee zinnen met één gekozen item (TP-4) en „ik weet het nog" met één klik zonder bewijsrecord (TP-5). Verwacht: 0 bewijsrecords uit de terugblik.
- [ ] 7.7 Log pauze in dagen en „gedaan" of „overgeslagen" in het dossier (TP-8). Verwacht: 2 velden per leerblok vanaf 2.
- [ ] 7.8 Bouw de dossiercontrole met importaanbod en lijst van ontbrekende bewijsonderdelen (TP-9). Verwacht: na leegmaken 1 aanbod en 1 lijst, 0 verloren gegevens na import.
- [ ] 7.9 Voeg het veld voor aanbevolen week en dag toe aan de leerblokdata (TP-10). Verwacht: 4 velden, 0 blokkades.
- [ ] 7.10 Maak `tests/terugblik.test.mjs` met de 4 profielen en de grenzen 2 uur, 2 dagen en 14 dagen. Verwacht: groen.

### Testpoort
- [ ] Volledige testpoort.
- [ ] Sabotage TP-2: toon de kaart vóór het ophalen; de test faalt.
- [ ] Sabotage TP-7: verwissel twee bandbreedtes; de test faalt.
- [ ] Tester met aangepaste tijdstempels doorloopt de 4 profielen (AC-39, AC-40).
- [ ] Geclaimde regels met hun methode gecontroleerd. Open punt A-5 (pauze tussen 1 en 2 dagen) is beslist en vastgelegd in ADR.

### Afsluiting
- [ ] commit `TP-1…TP-11: terugblik en tussenpozen`  - [ ] push  - [ ] overzicht afvinken

---

## Fase 8 — Huisstijl, toegankelijkheid, responsive en offline

**Doel.** De site ziet eruit als onderdeel van het C-cluster en werkt voor iedereen op elk apparaat.
**Wat de tester doet.** Opent de site op een telefoon (360 px), doet leerblok 1 met alleen het toetsenbord, met een schermlezer, en zet het netwerk uit na het laden.
**Spec.** TG-1…TG-5, PF-1…PF-5, QA-6.

### Subtasks
- [ ] 8.1 Pas `css/site.css` aan naar de HAN-huisstijl (accent `#E50056`, zwart, wit, dikke randen) uit de zusterdocumenten (QA-6). Verwacht: 100 % van de pagina's gebruikt de tokens.
- [ ] 8.2 Zet contrast op ≥ 4,5:1 voor alle tekst en toon statussen ook als tekst (TG-3, TG-4). Verwacht: 3 statussen elk met tekst.
- [ ] 8.3 Maak alle invoer met het toetsenbord bedienbaar en geef focus een zichtbare rand (TG-2). Verwacht: leerblok 1 zonder muis in te vullen en te bewaren.
- [ ] 8.4 Voeg labels en landmarks toe voor schermlezers (TG-5, TG-1). Verwacht: 0 onbereikbare velden in leerblok 1.
- [ ] 8.5 Maak de pagina's responsive vanaf 360 px (PF-1). Verwacht: 0 px horizontale scroll, alle velden van 4 leerblokken invulbaar.
- [ ] 8.6 Zorg dat een geladen leerblok zonder netwerk blijft werken (PF-3). Verwacht: 0 netwerkverzoeken tijdens 45 min gebruik.
- [ ] 8.7 Houd elke pagina ≤ 300 kB zonder video (PF-4). Verwacht: meting per pagina.
- [ ] 8.8 Toon de richttijd van 45 min per leerblok inclusief media (PF-5). Verwacht: 4 pagina's met 45 min.
- [ ] 8.9 Test in de twee laatste versies van Chrome, Safari, Firefox en Edge (PF-2). Verwacht: 4 × 2 zonder functieverlies.
- [ ] 8.10 Draai Lighthouse (toegankelijkheid) op alle pagina's (TG-1). Verwacht: score ≥ 95 op 100 % van de pagina's.

### Testpoort
- [ ] Volledige testpoort.
- [ ] Sabotage TG-3: zet één tekst op lage contrast; de contrastcontrole faalt.
- [ ] Lighthouse ≥ 95 op alle pagina's; 360 px zonder horizontale scroll; toetsenbordtest leerblok 1; schermlezertest leerblok 1; offlinetest.
- [ ] Geclaimde regels met hun methode gecontroleerd.

### Afsluiting
- [ ] commit `TG-1…TG-5, PF-1…PF-5, QA-6: huisstijl en toegankelijkheid`  - [ ] push  - [ ] overzicht afvinken

---

## Fase 9 — Docentmodus: mechaniek en deel 1

**Doel.** De docent leidt deel 1 (90 min) van het werkcollege met alleen de docentmodus.
**Wat de tester doet.** Een docent opent `docent.html?modus=docent`, start deel 1, ziet de stapkaart per onderdeel en de klok, schuift een onderdeel op en ziet de resterende tijd opnieuw berekend, opent een docentkaart en een verborgen modelantwoord, en drukt de docentkaarten van deel 1 af.
**Spec.** DM-1…DM-9, DM-10, DM-11, DM-14…DM-17, PR-3, PR-4.

### Subtasks
- [ ] 9.1 Leg het formaat van `data/docent-deel1.json` vast (onderdeel, klok, taaknummer, materiaal, laptop open/dicht, dia's, wat de docent doet, kernboodschap, rondloopvragen, als het anders loopt). Verwacht: één voorbeeldonderdeel valideert.
- [ ] 9.2 Vul `data/docent-deel1.json` met de 11 onderdelen van deel 1 uit LRD 8.2 en het draaiboek. Verwacht: 11 onderdelen.
- [ ] 9.3 Maak `js/docent/kies.js`: de docentmodus kiesbaar bij de start of met een adres-toevoeging, zonder inloggen, op dezelfde contentbestanden (DM-1, DM-2). Verwacht: 0 accounts; 1 wijziging in een modelantwoord verschijnt in beide weergaven.
- [ ] 9.4 Bouw de stapkaart met 7 elementen (taaknummer, opdracht, „klaar als", tijd, materiaal, dia's, laptop open/dicht) (DM-3). Verwacht: 7 elementen per kaart.
- [ ] 9.5 Bouw `js/docent/klok.js`: klok per deel vanaf 0:00, aftelling per onderdeel, start, pauze, reset (DM-4). Verwacht: afwijking ≤ 1 s over 10 min.
- [ ] 9.6 Toon de tijd als richttijd zonder blokkade (DM-5) en, voor een ronde, de gallery walk-tijden van 2 × 4 min en 2 min lezen (DM-6; die tijden gelden voor deel 2, de klok kent ze al). Verwacht: 0 blokkades bij 100 % van de richttijd.
- [ ] 9.7 Bouw de docentkaart met 4 elementen (wat de docent doet, kernboodschap, rondloopvragen, als het anders loopt) en de verborgen modelantwoorden en veelgemaakte fouten (DM-7, DM-8). Verwacht: modelantwoorden 0× zichtbaar vóór de klik.
- [ ] 9.8 Bouw overslaan, verschuiven en tijd aanpassen met herberekening van de resterende tijd (DM-9). Verwacht: resterende tijd = som van resterende onderdelen ± 1 s na overslaan van 2 onderdelen.
- [ ] 9.9 Bouw het programmaoverzicht met wat klaar is en wat komt en een veld voor de begintijden uit het rooster (DM-10). Verwacht: 1 overzicht, begintijden invulbaar.
- [ ] 9.10 Bouw de afdruk van de docentkaarten van een deel als draaiboek (DM-11) en de terugblik-kaart per leerblok uit `data/terugblik.json` (DM-14). Verwacht: afdruk deel 1 bevat 100 % van de onderdelen, tijden en rondloopvragen van het scherm; 3 terugblik-kaarten.
- [ ] 9.11 Zorg dat de docentmodus na het laden zonder netwerk werkt (DM-15). Verwacht: 15 min zonder netwerk zonder foutmelding.
- [ ] 9.12 Stel de stapkaart in op tekst ≥ 28 px bij 1280 × 720 en contrast ≥ 4,5:1 (DM-16). Verwacht: meting.
- [ ] 9.13 Houd beoordelingsinformatie uit de data (DM-17) en bevestig dat de docentmodus geen studentgegevens bewaart en geen koppeling met studentapparaten heeft (PR-3, PR-4). Verwacht: 0 studentgegevens in opslag; 0 verbindingen.

### Testpoort
- [ ] Volledige testpoort.
- [ ] Sabotage DM-9: laat de herberekening de overgeslagen tijd meetellen; de test faalt.
- [ ] Sabotage DM-8: toon modelantwoorden direct; de test faalt.
- [ ] Docent leidt een proefrun van 10 minuten van deel 1 zonder het draaiboek (voorbereiding AP-4). Notities in het testrapport.
- [ ] Leesbaarheid vanaf de achterste rij in een lokaal (DM-16).
- [ ] Geclaimde regels met hun methode gecontroleerd.

### Afsluiting
- [ ] commit `DM-1…DM-17, PR-3, PR-4: docentmodus met deel 1`  - [ ] push  - [ ] overzicht afvinken

---

## Fase 10 — Leerblok 3 en docentmodus deel 2 (EV-06 t/m EV-08)

**Doel.** Het vraagstuk plaatsen: stakeholders, VPC, BMC, TOM-model en conclusies.
**Wat de tester doet.** Doet leerblok 3 met een eigen vraagstuk: stakeholdertabel tekent zich op het invloed/belang-raster, register van feit en aanname, conclusies. Een docent leidt deel 2 in de docentmodus.
**Spec.** LB-9…LB-13, EV-06, EV-07, EV-08, DM-18, LI-3.

### Subtasks
- [ ] 10.1 Vul `data/leerblok-3.json` met taken 5.1, 6.1, 7.1, 8.1, 9.1, 9.2; ontbrekende „Waarom" en „Klaar als" door de auteur laten goedkeuren (TK-2). Verwacht: 6 taken volledig.
- [ ] 10.2 Schrijf `js/checks/lb3.js` met de controles van EV-06, EV-07, EV-08. Verwacht: 3 goede en 3 zwakke voorbeelden per controle.
- [ ] 10.3 Bouw de stakeholdertabel met automatisch raster (LB-9). Verwacht: 4 kwadranten, ≥ 5 stakeholders getekend.
- [ ] 10.4 Bouw de checklists en foto-vinkjes voor de vier producten (LB-10). Verwacht: 4 producten, 4 vinkjes.
- [ ] 10.5 Bouw het TOM-model V1 volgens TOM³ met 3 lagen × 4 kolommen = 12 cellen (LB-11) met een eigen samenvatting en bronvermelding als „ongepubliceerd document" (LI-3, BR-3). Verwacht: 12 cellen; 0 zinnen ≥ 8 woorden gelijk aan de bron (Analyse).
- [ ] 10.6 Bouw het feit/aanname-register met koppeling aan een zoekvraag en aan een VPC/BMC/TOM-onderdeel (LB-12). Verwacht: ≥ 3 beweringen met 3 velden.
- [ ] 10.7 Bouw de conclusies met controle tegen de stakeholderlijst en de herziene onderzoeksvraag (LB-13). Verwacht: 3 conclusies, 1 herziene vraag.
- [ ] 10.8 Voeg de samenhangcontroles EV-01→EV-06, EV-07→EV-02 en EV-08→EV-06 toe aan `checks/lb3.js` (deel van BW-10). Verwacht: 3 testen groen.
- [ ] 10.9 Voeg `data/bronnen-3.json` toe (VPC, BMC, TOM³-verwijzing). Verwacht: `content-check` groen op wezen.
- [ ] 10.10 Vul `data/docent-deel2.json` met de 8 onderdelen en 3 pauzes van deel 2 uit LRD 8.2 (DM-18). Verwacht: 19 onderdelen in totaal met deel 1 (11 + 8), plus 3 pauzes.
- [ ] 10.11 Verifieer met de auteur dat het college hetzelfde TOM-model gebruikt als de opdrachtomschrijving en vraag bij Westmoreland de publicatiegegevens (open punt A-1). Verwacht: antwoord of een expliciet uitstel, vastgelegd in ADR.

### Testpoort
- [ ] Volledige testpoort.
- [ ] Sabotage EV-06: haal de gebruiker uit EV-01 uit de stakeholderlijst; de samenhangcontrole faalt.
- [ ] Tester doorloopt leerblok 3 op een eigen vraagstuk.
- [ ] Docent leidt een proefrun van deel 2.
- [ ] Geclaimde regels met hun methode gecontroleerd.

### Afsluiting
- [ ] commit `LB-9…LB-13, EV-06…EV-08, DM-18: leerblok 3 en docentmodus deel 2`  - [ ] push  - [ ] overzicht afvinken

---

## Fase 11 — Leerblok 4: verbanden, reflectie en afronding (EV-10, EV-11)

**Doel.** Synthese ontdekken, reflecteren en alles bij elkaar in het dossier.
**Wat de tester doet.** Doet taak 9.4: trekt lijnen tussen user story, VPC en zes kapitalen, markeert kapitalen, noemt een spanning met een stakeholder, schrijft de synthese. Doet de STARR-reflectie, kopieert naar A3 vak 1 en kiest bij een tweede profiel „voorlopig vraagstuk" en „opnieuw doen".
**Spec.** LB-15, LB-16, LB-17, EV-10, EV-11, VB-1…VB-10, WS-2, TK-11…TK-14, ST-3, ST-4, ST-5, BW-10, LI-2.

### Subtasks
- [ ] 11.1 Vul `data/leerblok-4.json` met taak 9.4 en de reflectietaak; ontbrekende „Waarom" en „Klaar als" door de auteur laten goedkeuren. Verwacht: taken volledig.
- [ ] 11.2 Bouw de verbanden-kaart met drie kolommen en zes kapitalen (VB-1) in `js/verbanden.js`. Verwacht: 3 kolommen, 6 kapitalen.
- [ ] 11.3 Bouw de oefencasus met 3 open vragen en het modelvoorbeeld pas na een eigen poging (VB-2). Verwacht: 0 modelvoorbeelden vóór ≥ 1 getrokken lijn.
- [ ] 11.4 Bouw het trekken van lijnen met 3 typen en één zin (VB-3) en het automatisch tekenen tussen de kolommen zonder ingebedde afbeeldingen van Strategyzer of IIRC (VB-10, LI-2). Verwacht: ≥ 6 lijnen in een testprofiel; 0 ingebedde afbeeldingen van beide bronnen.
- [ ] 11.5 Bouw open plekken als vraag, nooit als antwoord (VB-4). Verwacht: 0 antwoorden in een leeg en een half ingevuld voorbeeld.
- [ ] 11.6 Bouw de markering van kapitalen (VB-5) en de spanning met een stakeholder uit EV-06 (VB-6). Verwacht: 6 kapitalen, 3 markeringen; ≥ 1 spanning.
- [ ] 11.7 Bouw de synthese-alinea (≤ 5 zinnen) met chips uit ≥ 2 modellen en 3 antwoorden op „wat laat dit model niet zien" (VB-7). Verwacht: alle drie de elementen gecontroleerd.
- [ ] 11.8 Zet taak 9.4 als zelfstandige taak van 20 min zonder plek in het werkcollegeprogramma (VB-9). Verwacht: 0 onderdelen in `docent-deel2.json`.
- [ ] 11.9 Schrijf `js/checks/lb4.js` (aanvullend) voor EV-10 en EV-11 en de samenhangcontroles EV-11→EV-01 en EV-11→EV-06 (BW-10). Verwacht: 5 samenhangcontroles in totaal.
- [ ] 11.10 Neem de lijst van verbanden op in het wisselblok en het A3-tekstblok (WS-2, VB-8). Verwacht: alle verbanden uit EV-11 aanwezig.
- [ ] 11.11 Bouw het STARR-sjabloon (LB-15) en de zin „wat ik hiermee aan mijn A3 heb" naast de waarom-zin (TK-11). Verwacht: 5 delen, 1 keuzelijst, 2 zinnen naast elkaar.
- [ ] 11.12 Bouw „kopieer naar A3 vak 1" met datumlog (LB-16, LB-17). Verwacht: 4 onderdelen in het klembord; 1 datum per actie.
- [ ] 11.13 Toon het zwakste onderdeel op de dossierpagina (TK-12). Verwacht: klopt met 3 testprofielen.
- [ ] 11.14 Voltooi de verdiepingstaken (4 in totaal) en zorg dat ze de status en de richttijd niet raken (TK-13, TK-14). Verwacht: 4 verdiepingstaken, 0 statuswijzigingen.
- [ ] 11.15 Bouw het voorlopig vraagstuk: label `voorlopig`, „opnieuw doen" met één klik en oude en nieuwe versie zichtbaar (ST-3, ST-4, ST-5). Verwacht: 100 % van de records na de keuze `voorlopig: true`.
- [ ] 11.16 Voeg `data/bronnen-4.json` toe (Mayer, Osterwalder, IIRC, e.a.). Verwacht: `content-check` groen.
- [ ] 11.17 Draai `content-check` op alle 11 bewijsonderdelen (BW-12, QA-3). Verwacht: 11 van 11 volledig.

### Testpoort
- [ ] Volledige testpoort.
- [ ] Sabotage VB-4: toon het ontbrekende verband als antwoord; de test faalt.
- [ ] Sabotage BW-10: verbreek de koppeling EV-11→EV-06; de samenhangcontrole faalt.
- [ ] Testprofielen: pilotstudent met eigen vraagstuk; profiel „voorlopig vraagstuk" (AC-21); profiel met leeg dossier (AC-40).
- [ ] Geclaimde regels met hun methode gecontroleerd.

### Afsluiting
- [ ] commit `VB-1…VB-10, EV-10, EV-11, LB-15…LB-17, ST-3…ST-5, TK-11…TK-14: leerblok 4`  - [ ] push  - [ ] overzicht afvinken

---

## Fase 12 — Media: mechaniek, twee video's en twee spellen

**Doel.** De drie routes per leerblok werken en de eerste twee video's en spellen staan erin. Begint met de spellen die het meest opleveren (Bronnen-detective, Waarde-simulator).
**Wat de tester doet.** Opent leerblok 2 en leerblok 4, kiest tekst, video of spel en komt telkens uit bij dezelfde „klaar als"-regel. Speelt een spel met alleen het toetsenbord. Een docent start video en spel vanaf de stapkaart.
**Spec.** MD-1, MD-2, MD-3, MD-5, MD-6, MD-7, MD-9, MD-10, MD-11, MD-13, MD-14, MD-15, MD-16.

### Subtasks
- [ ] 12.1 Schrijf `js/media.js`: tekst als standaard, twee kleine knoppen, laatste keuze onthouden (MD-2). Verwacht: 3 routes met dezelfde „klaar als".
- [ ] 12.2 Schrijf de uitlegteksten (≤ 300 woorden) voor leerblok 2 en 4 met voorbeeld en modelantwoord (MD-3). Verwacht: ≤ 300 woorden per leerblok.
- [ ] 12.3 Bouw het spel Bronnen-detective (zes fictieve bronkaarten, feedback per keuze, toetsenbord, tekstversie, geen score) (MD-9, MD-10, MD-13, MD-15). Verwacht: 0 muisacties voor een volledige doorloop; 100 % fictieve kaarten gemarkeerd.
- [ ] 12.4 Bouw de simulatie Waarde-simulator (drie beslissingen, voorspellen, effect op zes kapitalen) met dezelfde eisen (MD-9, MD-10, MD-13). Verwacht: 1 tekstversie, feedback per keuze.
- [ ] 12.5 Maak video V2 en V4 (≤ 3 min, ≤ 20 MB) met ondertitels (WebVTT) en transcript, zonder autoplay, laden na klik, op dezelfde site (MD-5, MD-6, MD-7). Verwacht: 2 hulpmiddelen per video; 0 verzoeken naar andere domeinen bij afspelen.
- [ ] 12.6 Zorg dat geen spel of simulatie bewijs oplevert (MD-11). Verwacht: 0 bewijsrecords uit een spel.
- [ ] 12.7 Plaats video's van derden als gewone link (MD-14). Verwacht: 0 ingebedde frames.
- [ ] 12.8 Laat de docentmodus video en spel starten vanaf de stapkaart (DM-13 komt in fase 13 af voor alle vier). Verwacht: 2 stapkaarten spelen af zonder verzoeken naar andere domeinen.
- [ ] 12.9 Toon in leerblok 1 twee kijktips als gewone link, met bron, duur en taal: Bureau Tromp (4:38, Nederlands) als instap en het MIT OpenCourseWare-fragment 0:44 tot 4:09 (Engels) als verdieping. Zet de gegevens in de datafile van leerblok 1 (MD-16, MD-14). Verwacht: 2 links, 2 van 2 met duur en taal, 0 ingebedde frames.

### Testpoort
- [ ] Volledige testpoort.
- [ ] Sabotage MD-6: zet autoplay aan; de test faalt.
- [ ] Sabotage MD-11: laat een spel een bewijsrecord schrijven; de test faalt.
- [ ] Netwerktrace tijdens afspelen: 0 verzoeken naar andere domeinen (MD-7).
- [ ] Toetsenbordtest en tekstversie per spel.
- [ ] Geclaimde regels met hun methode gecontroleerd.

### Afsluiting
- [ ] commit `MD-1…MD-16 (deel): mediamechaniek, V2, V4, Bronnen-detective, Waarde-simulator, kijktips`  - [ ] push  - [ ] overzicht afvinken

---

## Fase 13 — Media: de overige video's en spellen

**Doel.** Alle vier de leerblokken hebben video en spel.
**Wat de tester doet.** Doorloopt elk leerblok in elke route (tekst, video, spel) en controleert per video ondertitels, transcript en duur.
**Spec.** MD-4, MD-8, MD-12, DM-13.

### Subtasks
- [ ] 13.1 Maak video V1 en V3 (≤ 3 min, ≤ 20 MB) met ondertitels en transcript (MD-4). Verwacht: 4 video's in totaal, elk ≤ 3 min en ≤ 20 MB.
- [ ] 13.2 Bouw het spel Vraagslijper (drie rondes, feedback per veld) (MD-8). Verwacht: ≤ 5 min.
- [ ] 13.3 Bouw het spel Stakeholder-radar (invloed en belang, feedback per keuze) (MD-8). Verwacht: ≤ 5 min.
- [ ] 13.4 Controleer dat alle 4 spellen ≤ 5 min duren (MD-8). Verwacht: 4 gemeten tijden.
- [ ] 13.5 Doorloop alle vier de leerblokken zonder video of spel (MD-12). Verwacht: 4 leerblokken afgerond.
- [ ] 13.6 Laat de stapkaart voor elk onderdeel met een video of spel dat afspelen of starten zonder verzoeken naar andere domeinen (DM-13). Verwacht: alle bestaande stapkaarten getest.

### Testpoort
- [ ] Volledige testpoort.
- [ ] Sabotage MD-4: voeg een video van 4 min toe; de mediacontrole faalt.
- [ ] Doorloop van elk leerblok in elke route (AC-30).
- [ ] Geclaimde regels met hun methode gecontroleerd.

### Afsluiting
- [ ] commit `MD-4, MD-8, MD-12, DM-13: overige media`  - [ ] push  - [ ] overzicht afvinken

---

## Fase 14 — Afdrukken, documentatie en eindcontrole

**Doel.** Alles wat een docent of student naast de site nodig heeft, en een regressiecontrole op het hele blueprint.
**Wat de tester doet.** Drukt werkboek en draaiboek van een deel af en legt ze naast de site. Leest de docentgids en de studentintroductie als iemand die de site nog nooit zag.
**Spec.** DM-12, DL-1, DL-2, DL-4, QA-4, QA-5, LI-1, SI-1.

### Subtasks
- [ ] 14.1 Bouw de afdruk van het werkboek van een deel uit de contentbestanden met dezelfde nummers en „klaar als"-regels (DM-12). Verwacht: 100 % van de nummers en regels gelijk aan de site.
- [ ] 14.2 Maak `css/print.css` voor werkboek en draaiboek. Verwacht: afdruk zonder afgesneden tekst op A4.
- [ ] 14.3 Schrijf de docentgids (≤ 2 pagina's A4, 5 onderwerpen) (DL-1). Verwacht: 5 onderwerpen.
- [ ] 14.4 Schrijf de studentintroductie (≤ 1 pagina A4, 3 onderwerpen) (DL-2). Verwacht: 3 onderwerpen.
- [ ] 14.5 Schrijf de beschrijving van schema 1.0 (DL-4). Verwacht: 13 velden beschreven.
- [ ] 14.6 Controleer alle teksten in het Nederlands en de Engelse vaktermen met uitleg van één zin bij het eerste voorkomen (QA-4, QA-5). Verwacht: 100 % van de termen met ≤ 1 zin uitleg.
- [ ] 14.7 Controleer dat er geen kopieën van derden in de repository staan (LI-1). Verwacht: 0 kopieën van Brightspace-materiaal, PhoneVentures-handleidingen, slides of opgeslagen pagina's van derden.
- [ ] 14.8 Draai de regressiecontrole over alle regels van het blueprint: elke regel heeft een fase en een uitgevoerde verificatie (zie bijlage). Verwacht: 0 regels zonder afgevinkte verificatie.

### Testpoort
- [ ] Volledige testpoort, aangevuld met SI-1 (8 onderdelen ≤ 2 klikken), SI-3 (volledige doorloop) en PR-1 (netwerktrace).
- [ ] Vergelijking afdruk en scherm voor deel 1 en deel 2 (AC-18, AC-25).
- [ ] Iemand die de site nog nooit zag leest docentgids en studentintroductie en voert de eerste taak uit zonder uitleg.
- [ ] Geclaimde regels met hun methode gecontroleerd.

### Afsluiting
- [ ] commit `DM-12, DL-1, DL-2, DL-4, QA-4, QA-5, LI-1: afdrukken en documentatie`  - [ ] push  - [ ] overzicht afvinken

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

## Open punten die de route raken

- **A-1** TOM³-bron zonder openbare publicatie: opgevraagd in subtask 10.11, gebruikt in fase 10.
- **A-5** Pauzeband tussen 1 en 2 dagen (TP-7): beslissen vóór fase 7.
- **A-11** Het werkboek heeft slechts 3 van 15 „Klaar als"-regels en 6 „Waarom"-regels, terwijl TK-2 100 % eist: de ontbrekende regels schrijft de auteur en keurt ze goed in subtask 2.3, 6.1, 10.1 en 11.1.
