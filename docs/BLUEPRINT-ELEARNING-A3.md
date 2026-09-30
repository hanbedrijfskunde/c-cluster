# BLUEPRINT — Hybride e-learning A3 met automatisch bewijs

> Afgeleid van `docs/LRD-ELEARNING-A3.html` (LRD versie 0.14, 30 september 2026). Dit document beschrijft de doelsituatie van het product: geen bouwvolgorde, geen fasering, geen voortgang. Bouwvolgorde en voortgang staan in het bouwplan (`BUILDPLAN-ELEARNING-A3.md`). Pedagogische onderbouwing en risico's blijven in het LRD; het besluitenregister (B1–B60) staat in `docs/ADR-ELEARNING-A3.md`; regels hier verwijzen daar niet naartoe maar zijn zelfstandig toetsbaar. Bijlage A koppelt elke LRD-eis aan de regels hieronder.

**Lezen.** Elke regel heeft een ID (prefix per onderwerp), een verplichtingsniveau (Must, Should, Could), een criterium met getal en eenheid, en een verificatiemethode (Test, Demonstratie, Inspectie, Analyse). „Moet" is de verplichting van het product, niet de volgorde van het werk. De statusnamen Compleet, Bijna en „Nog niet" zijn productterm en geen voortgangstaal.

---

## 1. Doel

| SMART | Doel |
|---|---|
| **S**pecifiek | Een statische e-learning op GitHub Pages met vier leerblokken en twee gebruiksvormen: zelfstandig (student) en werkcollege (docent-geleid). Studenten van Praktijkopdracht 5 (HBO Bedrijfskunde, C-cluster) oefenen er de A3 mee op het eigen vraagstuk en bouwen automatisch een bewijsdossier op voor leeruitkomst 1 (grotendeels), leeruitkomst 5 (deels) en de voorbereiding van leeruitkomst 2. Docenten gebruiken dezelfde site als docentmodus tijdens het werkcollege. |
| **M**eetbaar | 11 bewijsonderdelen (EV-01 t/m EV-11), elk met een automatische controle. 0 verzoeken naar andere domeinen tijdens een volledige doorloop. In een pilot rondt ≥ 80 % van de studenten elk leerblok af binnen 1,25 × de richttijd van 45 min. Een gewijzigd dossier wordt in 100 % van de gevallen gemeld als „gewijzigd na export". |
| **A**anpasbaar/haalbaar | Geen backend: alles blijft in de browser van de student, inhoud staat in datafiles, geen bouwstap. Bouwt op het bestaande werkboek van week 5 met „klaar als"-regels per taak, die op vorm te controleren zijn. Te onderhouden door één docent. |
| **R**elevant | Het portfolio vraagt 4 beroepsproducten, 6 reflectieverslagen, 6 feedbackmomenten en 3 ontwikkelpunten. Studenten verzamelen die achteraf, waarna feedback en eerste versies zijn verdwenen. De taken zijn het bewijs: wat de student invult om het eigen vraagstuk te onderzoeken, wordt met versie, tijd en controles bewaard. |
| **T**ijdvenster (werking) | Richttijd 45 min per leerblok (+ ≤ 15 min terugblik vanaf leerblok 2). Eerste lading ≤ 300 kB per pagina. Leerblok bruikbaar zonder netwerk na laden. Docent leidt deel 1 van het werkcollege (90 min) met ≤ 2 opzoekmomenten buiten de docentmodus. |

Elke regel in §6 t/m §7 dient dit doel; de dekking per onderdeel van het doel staat in §4.3.

---

## 2. Ontwerpprincipes (informatief)

Deze principes hebben geen eigen ID. Ze zijn de reden voor de regels en staan in het LRD Deel 2 uitgewerkt met bronnen.

| Principe | Wat het de regels oplegt | Regels |
|---|---|---|
| De taak is het bewijs (constructive alignment, evidence-centered design) | Elk bewijsonderdeel heeft claim, taak, vastlegging en controle; geen taak zonder LUK-koppeling | BW-12, EV-01–EV-11, QA-3 |
| Feedback beantwoordt: waar naartoe, hoe ga ik, wat nu | „Klaar als", directe controle, modelantwoord ná eigen poging, volgende stap | TK-2, TK-6, TK-10, BW-1, BW-2 |
| Geen puntenjacht | Drie statussen, dekkingsoverzicht, geen score | BW-3, BW-4, BW-13 |
| Geleid ontdekken | Open vragen, open plekken als vraag, model pas na eigen poging | VB-2, VB-4 |
| Spreiden en ophalen | Terugblik vóór overdracht, lengte volgt de pauze | TP-1–TP-9 |
| Autonomie en ruimte voor verschillen | Richttijd geen slot, overslaanbare oefening, verdieping, voorlopig vraagstuk | TK-5, TK-8, TK-9, TK-13, ST-3 |
| KISS als afwijzingen | Wat bewust niet wordt gebouwd | §8 |

---

## 3. Architectuur

```
contentbestanden (tekst, werkboekregels, modelantwoorden, LUK-koppeling,
                  controleparameters, docentvelden, bronnen)
        │  één bron, twee weergaven
        ├──► studentweergave ── leerblokken 1–4 ──► bewijsrecords ─┐
        │                                                          ▼
        │                                     browseropslag (alleen op het apparaat)
        │                                                          │ export door student
        │                                                          ▼
        ├──► dossierpagina  ◄── import ── dossier: JSON + SHA-256 + afdrukpagina
        │                                                          │ inlevering via Brightspace
        ├──► verificatiepagina (docent, leest dossiers lokaal) ◄───┘
        └──► docentmodus (beamer): stapkaart, klok, docentkaart, afdruk
```

**Componenten.** (1) Contentbestanden: één bron voor student, docent, werkboekafdruk en draaiboekafdruk. (2) Studentweergave: vier leerblokken van 45 min met taken in een vast ritme (waarom, stof en oefenen, toepassen, klaar en volgende stap, optionele verdieping). (3) Bewijsmotor: elke taak levert een bewijsrecord dat op een LUK-onderdeel ligt en deterministisch wordt gecontroleerd op aanwezigheid en samenhang. (4) Dossier: export, import en verificatie zonder server. (5) Docentmodus: tweede weergave van dezelfde content, zonder koppeling met studentapparaten. (6) Media: elk leerblok in tekst, video en spel of simulatie.

**Wat het bewijs is.** Een tijdgestempeld dossier van geoefende en toegepaste taken op het eigen vraagstuk, met versiegeschiedenis. **Wat het niet is:** een kwaliteitsoordeel, een vervanger van de beroepsproducten, of fraudebestendig. De controlesom toont wijziging na export; de tijdstempel van inlevering is die van Brightspace. De beoordeling van beroepsproducten blijft bij de docent.

**Controlesoorten.** A = aanwezig (veld gevuld, aantal woorden, keuze uit lijst). B = samenhang (wat op de ene plek staat klopt met een andere plek). C = onderbouwd (er staat een reden bij; alleen aantal woorden en zinnen wordt geteld). Resultaten: `ok`, `let op`, `mist`.

---

## 4. Leeruitkomsten en dekking

### 4.1 Leeruitkomsten van de e-learning

Tags naar Anderson & Krathwohl (2001): `[proces / kennis]`. LUK en BC verwijzen naar de leeruitkomsten en beoordelingscriteria van het C-cluster, niveau 2.

| # | Een student kan … | Bloom | LUK · BC | Leerblok |
|---|---|---|---|---|
| EL1 | uitleggen wat een A3 is en waarom ze iteratief met de opdrachtgever wordt besproken (drie C's, acht vakken, wat niet op één A3 past) | Understand / Conceptual | LUK 1 · BC1 | 1 |
| EL2 | een vage vraag omzetten in een onderzoeksvraag als user story: gebruiker, probleem of pain/gain, waardecreatie in zes kapitalen | Apply / Procedural | LUK 1 · BC1 | 1 |
| EL3 | de onderzoeksvraag opdelen in zoekvragen vanuit verschillende frames, één model kiezen (7S, Strategy Map, Six Capitals of TOM) en die keuze verantwoorden | Analyze / Conceptual | LUK 1 · BC1 | 1 |
| EL4 | een zoekstrategie opstellen (kernbegrippen, synoniemen, Engelse termen, operatoren) en daarmee bronnen vinden | Apply / Procedural | LUK 1 · BC1 | 2 |
| EL5 | een bron beoordelen op Authority, Accuracy, Objectivity, Currency en Coverage (AAOCC), een AI-bron aan de oorspronkelijke tekst controleren en de bron in APA vermelden | Evaluate / Conceptual | LUK 1 · BC1 | 2 |
| EL6 | het vraagstuk plaatsen ten opzichte van stakeholders (invloed, belang, intern/extern), klant (VPC), bedrijfsmodel (BMC) en TOM-model | Analyze / Conceptual | LUK 1 · BC1 | 3 |
| EL7 | in eigen analyseproducten feit en aanname onderscheiden en elke belangrijke aanname aan een zoekvraag koppelen | Evaluate / Metacognitive | LUK 1 · BC1 | 3 |
| EL8 | feedback op eigen werk ophalen en vastleggen (ik zie, ik mis, ik vraag me af), er een actie aan koppelen en erop reflecteren volgens STARR | Evaluate / Metacognitive | LUK 5 · BC5 | 4 |
| EL9 | de relaties tussen user story, value proposition canvas en zes kapitalen ontdekken, samenvoegen tot één beeld en aanwijzen wat elk model niet laat zien | Analyze → Create / Conceptual | LUK 1 · BC1 (bereidt LUK 2 voor) | 4 |

EL2, EL3, EL6, EL7 en EL9 staan op de eigen casus. EL1, EL4 en EL5 hebben ook een kennisdeel op de oefencasus (webshop X). Alleen toepassing op de eigen casus levert bewijs.

### 4.2 De vier leerblokken

| Leerblok | Richttijd (min) | Afgerond bewijs | EL |
|---|---|---|---|
| 1 · De A3 en je vraag | 45 | Onderzoeksvraag met zoekvragen en modelkeuze (EV-01, EV-02) | EL1–EL3 |
| 2 · Zoeken en beoordelen | 45 + ≤ 15 terugblik | Een beoordeelde bron in APA (EV-03, EV-04, EV-05) | EL4, EL5 |
| 3 · Het vraagstuk plaatsen | 45 + ≤ 15 terugblik | Plaatsing met conclusie en onderzoeksvraag (EV-06, EV-07, EV-08) | EL6, EL7 |
| 4 · Verbinden en reflecteren | 45 + ≤ 15 terugblik | Synthese met feedback en reflectie, en het dossier (EV-11, EV-09, EV-10) | EL9, EL8 |

Werkboeknummers per leerblok: 1 → 1.1, 2.1, 2.2; 2 → 3.1, 3.2, 4.1, 4.2; 3 → 5.1, 6.1, 7.1, 8.1, 9.1, 9.2; 4 → 9.4 en 6.2 (feedback). In het werkcollege vallen leerblok 1 en 2 in deel 1 (90 min) en leerblok 3 in deel 2 (145 min); leerblok 4 is zelfstandig werk. De inhoud van het werkcollegeprogramma (LRD 8.2), de verdiepingstaken (8.3), de media (8.4) en de terugblikkaarten (8.5) is de inhoudelijke bron voor de contentbestanden en wordt niet opnieuw in deze blueprint beschreven.

### 4.3 Dekking van de LUK

Een onderdeel telt als **gedekt** als er een bewijsonderdeel voor bestaat, **deels** als de e-learning er een stap van oefent en **buiten scope** als het niet in deze blueprint valt (§8).

| Onderdeel van de leeruitkomst (niveau 2) | Dekking | Bewijs |
|---|---|---|
| LUK 1 · Signaleert knelpunten in een intern proces | deels (probleemzin komt van buiten; wordt niet getoetst) | EV-01 |
| LUK 1 · Formuleert een onderzoeksvraag | gedekt | EV-01 |
| LUK 1 · Analyseert het probleem methodisch | deels (zoekvragen en zoekstrategie) | EV-02, EV-03 |
| LUK 1 · Stelt een onderbouwde diagnose | buiten scope | – |
| LUK 1 · Selecteert relevante theorieën en modellen en voegt ze samen | gedekt | EV-02, EV-11 |
| LUK 1 · Gebruikt en beoordeelt bronnen | gedekt | EV-03, EV-04, EV-05 |
| LUK 1 · Duidt achtergronden, oorzaken en ontwikkelingen | deels (achtergrond, geen oorzaken) | EV-07, EV-08 |
| LUK 1 · Betrekt stakeholders binnen en buiten het organisatieonderdeel | gedekt | EV-06 |
| LUK 1 · Ziet kansen en bedreigingen uit externe ontwikkelingen | deels (alleen via het frame „extern") | EV-02 |
| LUK 2 · Oog voor meervoudige waardecreatie | deels (zien, niet herontwerpen) | EV-11 |
| LUK 2 (overig), LUK 3 en LUK 4 | buiten scope | – |
| LUK 5 · Haalt feedback op en reflecteert erop | gedekt | EV-09, EV-10 |
| LUK 5 · Formuleert ontwikkelpunten en werkt er aantoonbaar aan | deels (actie en volgende stap) | EV-09, TK-10 |

De 13 onderdelen zijn 5 gedekt, 6 deels en 2 buiten scope. Regel BW-13 toont deze tabel aan de student met de eigen status.

---

## 5. Bewijsstatus en datamodel

**Statusregel (BW-5).** Per bewijsonderdeel:

| Status | Voorwaarde |
|---|---|
| Compleet | alle controles van soort A en B staan op `ok`; controles van soort C mogen op `let op` staan |
| Bijna | ≥ 1 controle van soort C op `mist`, of ≥ 1 controle van soort A of B op `let op` |
| Nog niet | ≥ 1 controle van soort A of B op `mist` |

Bij samenloop geldt: „Nog niet" gaat voor „Bijna", en „Bijna" gaat voor Compleet.

**Bewijsrecord (schema 1.0).**

```json
{
  "schema": "1.0",
  "id": "EV-01",
  "taak": "2.1",
  "leerblok": 1,
  "luk": [1],
  "bc": ["BC1"],
  "inhoud": { "gebruiker": "…", "pain": "…", "waarde": "…", "kapitalen": ["sociaal"] },
  "controles": [
    { "id": "velden-gevuld", "resultaat": "ok" },
    { "id": "niet-financieel-kapitaal", "resultaat": "ok" }
  ],
  "status": "compleet",
  "voorlopig": false,
  "versie": 3,
  "bijgewerkt": "2026-09-30T14:02:11+02:00",
  "elearning": "0.1.0"
}
```

**Dossier.** Twee bestanden uit dezelfde gegevens: `bewijsdossier-<alias>-<datum>.json` (alle records: nieuwste versie en het aantal eerdere versies, alias, teamnummer, e-learningversie, SHA-256 over de inhoud) en een afdrukbare pagina per leeruitkomst met de status per bewijsonderdeel, de ingevulde inhoud en de controlesom onderaan.

---

## 6. Functionele requirements

Elke regel is een anker (`id="xx-n"`). Een bewijsonderdeel (EV) telt als één verplichting met een controleset; de set is in het criterium opgesomd en wordt met een unittest per controle (3 goede en 3 zwakke voorbeelden) getoetst.

### 6.1 Site en publicatie (SI)

| ID | Eis | Prio | Criterium | Verificatie |
|---|---|---|---|---|
| <a id="si-1"></a>SI-1 | De site moet bestaan uit een startpagina, vier leerblokpagina's, een dossierpagina, een verificatiepagina en een docentmodus. | Must | 8 onderdelen; elk bereikbaar in ≤ 2 klikken vanaf de startpagina | Test |
| <a id="si-2"></a>SI-2 | De site moet worden gepubliceerd via GitHub Pages vanuit `https://github.com/hanbedrijfskunde/a3-learning` (branch `main`) op `https://hanbedrijfskunde.github.io/a3-learning/`. | Must | HTTP-status 200 op de URL; 1 publicatiebron | Demonstratie |
| <a id="si-3"></a>SI-3 | De site moet uitsluitend relatieve links gebruiken, zodat hij onder het subpad `/a3-learning/` werkt. | Must | 0 absolute interne links; 0 foutmeldingen (404 of console-fout) bij een volledige doorloop van 4 leerblokken, dossier, verificatie en docentmodus op de gepubliceerde URL | Test |
| <a id="si-4"></a>SI-4 | De site moet zonder bouwstap en zonder framework te publiceren en te lezen zijn. | Must | 0 bouwstappen tussen commit en publicatie van de site; 0 frameworks in de bestanden die de browser laadt | Inspectie |
| <a id="si-5"></a>SI-5 | De repository moet alleen de site (HTML, CSS, JavaScript, datafiles, media), een README met verwijzing naar de docentgids, een `.nojekyll`-bestand, een `LICENSE`-bestand, de workflow en de tests bevatten. | Should | 0 bestanden buiten deze 10 categorieën | Inspectie |
| <a id="si-6"></a>SI-6 | Bij elke push moet één GitHub Actions-workflow de unittests, de contentcontrole en de linkcontrole uitvoeren en alleen publiceren als alle drie slagen. | Must | 3 controles per push; 0 publicaties bij ≥ 1 falende controle | Test (testcommit op aparte branch) |
| <a id="si-7"></a>SI-7 | De workflow moet bij een falende controle melden welke controle faalt. | Should | 1 benoemde controle in de foutmelding per falende controle | Test |
| <a id="si-8"></a>SI-8 | Zolang de configuratie de vlag `pilot` aan heeft, moet elke pagina een banner „pilot" tonen. | Could | 100 % van de pagina's met banner bij vlag aan; 0 pagina's bij vlag uit | Test |

### 6.2 Start, profiel en privacytekst (ST)

| ID | Eis | Prio | Criterium | Verificatie |
|---|---|---|---|---|
| <a id="st-1"></a>ST-1 | De site moet bij de start uitsluitend vragen om een alias of voornaam, een teamnummer, een eigen vraagstuk in één zin en een waarom-zin, of de keuze „nog geen scherp vraagstuk". | Must | 4 invoervelden en 1 keuze; 0 andere velden met persoonsgegevens | Test |
| <a id="st-2"></a>ST-2 | De startpagina moet een privacytekst tonen die waarschuwt geen namen van opdrachtgevers of vertrouwelijke gegevens in te vullen. | Must | 1 tekst van ≤ 100 woorden op de startpagina | Inspectie |
| <a id="st-3"></a>ST-3 | Als de student „nog geen scherp vraagstuk" kiest, moet de site elk daarna gemaakt bewijsrecord het label `voorlopig` geven. | Must | 100 % van de records na die keuze heeft `voorlopig: true` | Test |
| <a id="st-4"></a>ST-4 | Wanneer de student na de afbakening van het vraagstuk een voorlopig bewijsonderdeel opnieuw wil doen, moet de site dat met één knop mogelijk maken. | Should | 1 klik tot een leeg toepassingsveld | Test |
| <a id="st-5"></a>ST-5 | Na „opnieuw doen" moet het dossier de oude en de nieuwe versie van het bewijsonderdeel naast elkaar tonen. | Should | 2 versies zichtbaar in het dossier | Test |
| <a id="st-6"></a>ST-6 | Wanneer de student na één bevestiging „wis alles" kiest, moet de site alle gegevens van de site uit de browseropslag verwijderen. | Must | 1 bevestiging; 0 items van de site in localStorage, sessionStorage en IndexedDB | Test |
| <a id="st-7"></a>ST-7 | De site moet onderdelen pas tonen op het moment dat ze aan de beurt zijn. | Should | In de eerste 4 schermen van leerblok 1 (alias, vraagstuk, waarom-zin, overzicht van vier leerblokken): 0 zichtbare elementen van Wissel, verdieping, „Mijn stand" en „kopieer naar A3"; „Mijn stand" en „kopieer naar A3" staan op 1 pagina (dossierpagina) | Test (schermafbeelding per stap) |

### 6.3 Taken en leerroute (TK)

| ID | Eis | Prio | Criterium | Verificatie |
|---|---|---|---|---|
| <a id="tk-1"></a>TK-1 | De site moet een aanbevolen volgorde van de leerblokken tonen zonder slot. | Must | 4 leerblokken direct te openen vanaf de startpagina; 0 voorwaarden | Test |
| <a id="tk-2"></a>TK-2 | De site moet bij elke taak het werkboeknummer, het waarom, de richttijd en de „klaar als"-regel tonen, letterlijk uit het werkboek. | Must | 100 % van de taken; 0 tekens verschil met de werkboektekst | Test (contentcontrole) |
| <a id="tk-3"></a>TK-3 | De site moet per taak een oefenversie op de oefencasus (webshop X) en een toepassing op het eigen vraagstuk gescheiden aanbieden. | Must | 2 versies per taak in 100 % van de taken | Inspectie |
| <a id="tk-4"></a>TK-4 | De site moet alleen de toepassing en de ingevulde controles als bewijs vastleggen. | Must | 0 bewijsrecords met inhoud uit de oefenversie | Test |
| <a id="tk-5"></a>TK-5 | De site moet de oefenversie met één klik „ik ken dit al" overslaanbaar maken zonder gevolg voor het bewijs. | Should | 1 klik; 0 wijzigingen in de status van bewijsonderdelen | Test |
| <a id="tk-6"></a>TK-6 | De site moet het modelantwoord van de oefenversie pas tonen nadat de student een eigen poging heeft ingevuld. | Must | 0 modelantwoorden zichtbaar vóór ≥ 1 ingevuld veld | Test |
| <a id="tk-7"></a>TK-7 | De site moet de student de oefenversie herhaald laten doen. | Should | ≥ 10 herhalingen achter elkaar zonder blokkade | Test |
| <a id="tk-8"></a>TK-8 | Zodra de „klaar als"-regel is gehaald, moet de site een knop „klaar" tonen waarmee de student doorgaat naar de volgende taak of een verdiepingstaak, ook vóór de richttijd en ook in het werkcollege. | Should | 1 klik van „klaar" naar volgende taak; werkt bij ≤ 50 % van de richttijd | Test |
| <a id="tk-9"></a>TK-9 | De site mag een student die de richttijd overschrijdt niet blokkeren. | Must | 0 blokkades bij 150 % van de richttijd, met lopende klok in de docentmodus | Test |
| <a id="tk-10"></a>TK-10 | De site moet na elke taak en bij het exporteren één zin „mijn volgende stap" vragen en bij het bewijsonderdeel opslaan. | Should | 1 zin van ≥ 3 woorden per taak; opgeslagen in 100 % van de records | Test |
| <a id="tk-11"></a>TK-11 | De site moet aan het eind van leerblok 4 vragen „wat ik hiermee aan mijn A3 heb" en die zin naast de waarom-zin uit leerblok 1 tonen. | Should | 2 zinnen naast elkaar op de dossierpagina | Demonstratie |
| <a id="tk-12"></a>TK-12 | De dossierpagina moet het zwakste onderdeel van het dekkingsoverzicht tonen. | Could | 1 onderdeel getoond; klopt met de statussen in 3 testprofielen | Test |
| <a id="tk-13"></a>TK-13 | De site moet in elk leerblok één optionele verdiepingstaak bieden, zichtbaar na „klaar". | Should | 4 verdiepingstaken (1 per leerblok) | Inspectie |
| <a id="tk-14"></a>TK-14 | De site moet verdiepingstaken buiten de status en de richttijd houden en in het dossier alleen „verdieping gedaan" vermelden. | Should | 0 statuswijzigingen door een verdiepingstaak; 0 minuten in de richttijd van 45 min | Test |
| <a id="tk-15"></a>TK-15 | De site moet elk leerblok afsluiten met een scherm dat de status van de bewijsonderdelen van dat leerblok toont, een volgende stap vraagt en de bewaarmelding toont. | Must | 4 afsluitschermen met 3 onderdelen (status, volgende stap, bewaarmelding) | Test |
| <a id="tk-16"></a>TK-16 | Een leerblok moet als „afgerond" gelden als elk bewijsonderdeel ervan Compleet of Bijna is of het label `voorlopig` heeft, en geen enkel onderdeel „Nog niet" is. | Must | 4 testprofielen geven het verwachte resultaat | Test |
| <a id="tk-17"></a>TK-17 | De site moet de student laten doorgaan zonder een leerblok af te ronden. | Must | 0 blokkades bij een leerblok dat niet is afgerond | Test |
| <a id="tk-18"></a>TK-18 | Elke taak moet dezelfde vijf stappen in dezelfde volgorde volgen: waarom, stof en oefenen, toepassen, klaar en volgende stap, optionele verdieping. | Should | 5 stappen in 100 % van de taken | Inspectie |

### 6.4 Leerblokken (LB)

| ID | Eis | Prio | Criterium | Verificatie |
|---|---|---|---|---|
| <a id="lb-1"></a>LB-1 | De site moet de student vier leerblokken tonen (1 De A3 en je vraag; 2 Zoeken en beoordelen; 3 Het vraagstuk plaatsen; 4 Verbinden en reflecteren) met per leerblok de richttijd en het afgeronde bewijs waarmee het eindigt. | Must | 4 leerblokken van 45 min; 9 uitkomsten (EL1–EL9) verdeeld volgens §4.2 | Inspectie |
| <a id="lb-2"></a>LB-2 | Leerblok 1 moet een bouwer voor de onderzoeksvraag bieden met drie velden, een keuze uit de zes kapitalen en een live voorbeeld van de samengestelde vraag. | Must | 3 velden; 6 kapitalen; voorbeeld bijgewerkt ≤ 1 s na een toetsaanslag | Test |
| <a id="lb-3"></a>LB-3 | Leerblok 1 moet drie zoekvragen bieden met een keuzelijst voor het frame (functioneel, intern/extern, theoretisch/empirisch), de keuze van één model uit 7S, Strategy Map, Six Capitals en TOM, en een veld „wat mis je met één frame". | Must | 3 zoekvragen; 3 frames; 4 modellen; 1 veld | Demonstratie |
| <a id="lb-4"></a>LB-4 | Leerblok 1 moet het team het model samen laten kiezen en elke student de teamkeuze en de eigen verantwoording laten vastleggen. | Should | 2 velden per student (teamkeuze, verantwoording) | Demonstratie |
| <a id="lb-5"></a>LB-5 | Leerblok 2 moet een zoektermentabel, een veld voor de zoekstring met controle op operatoren en een keuze tussen route A (databank) en route B (AI-tool) bieden. | Must | 1 tabel; 1 zoekstringveld; 2 routes | Demonstratie |
| <a id="lb-6"></a>LB-6 | Bij route B moet leerblok 2 een promptgenerator bieden die de zoekvraag invult en waarschuwt als een woord uit de door de student ingevulde „niet noemen"-lijst in de prompt staat. | Should | 1 waarschuwing per woord uit de lijst; 0 gemiste woorden in 6 testprompts | Test |
| <a id="lb-7"></a>LB-7 | Leerblok 2 moet een bronlog bieden met AAOCC-oordelen, twee verificatievinkjes bij route B, een besluit en een APA-veld met formaatcontrole, voor meerdere bronnen. | Must | 5 oordelen; 2 vinkjes; ≥ 2 bronnen invoerbaar | Test |
| <a id="lb-8"></a>LB-8 | Leerblok 2 moet de stelling over AI en inspiratiemateriaal bieden met een keuze en een argument. | Should | 2 kanten; 1 argumentveld | Demonstratie |
| <a id="lb-9"></a>LB-9 | Leerblok 3 moet een stakeholdertabel bieden die zich automatisch tekent op een invloed/belang-raster, met intern/extern per stakeholder. | Must | 4 kwadranten (H/L × H/L); ≥ 5 stakeholders getekend | Test |
| <a id="lb-10"></a>LB-10 | Leerblok 3 moet per product (stakeholdermap, VPC, BMC, TOM-model V1) een checklist en een vinkje „foto gemaakt" bieden. | Must | 4 producten; 4 vinkjes | Demonstratie |
| <a id="lb-11"></a>LB-11 | Het TOM-model V1 moet de TOM³-indeling volgen: drie lagen (strategisch, tactisch, operationeel) × vier kolommen (Methode, Mens, Machine, Informatie & Rapportage). | Must | 3 × 4 = 12 cellen; 0 andere TOM-modellen als keuze | Inspectie |
| <a id="lb-12"></a>LB-12 | Leerblok 3 moet een register bieden waarin de student kernbeweringen als feit of aanname labelt, aan een zoekvraag koppelt en aan het onderdeel van VPC, BMC of TOM waar ze bij horen. | Must | ≥ 3 beweringen met 3 velden (label, zoekvraag, onderdeel) | Test |
| <a id="lb-13"></a>LB-13 | Leerblok 3 moet de eerste conclusies (plaatsing ten opzichte van stakeholders, klant en organisatie) laten vastleggen met controle tegen de stakeholderlijst, plus een herziene onderzoeksvraag. | Must | 3 conclusies; 1 herziene vraag | Test |
| <a id="lb-14"></a>LB-14 | Leerblok 4 moet een feedbacklog bieden met ik zie, ik mis, ik vraag me af, rol van de gever, actie en status, waarin de student ontvangen én gegeven feedback vastlegt. | Must | 6 velden; ≥ 10 regels toe te voegen | Test |
| <a id="lb-15"></a>LB-15 | Leerblok 4 moet een STARR-sjabloon bieden met een keuzelijst voor het eigen gedrag en een volgende stap, optioneel gekoppeld aan een feedbackregel. | Must | 5 delen; 1 keuzelijst; 1 koppeling | Demonstratie |
| <a id="lb-16"></a>LB-16 | Op de dossierpagina moet een knop „kopieer naar A3 vak 1" onderzoeksvraag, zoekvragen, plaatsing en de waarom-zin uit leerblok 1 als tekstblok naar het klembord zetten. | Should | 4 onderdelen in het klembord; 1 klik | Test |
| <a id="lb-17"></a>LB-17 | De site moet bij „kopieer naar A3 vak 1" de datum van het kopiëren in het dossier loggen. | Could | 1 datum per kopieeractie | Test |

### 6.5 Bewijsmotor (BW)

| ID | Eis | Prio | Criterium | Verificatie |
|---|---|---|---|---|
| <a id="bw-1"></a>BW-1 | De site moet de controles van een bewijsonderdeel uitvoeren terwijl de student typt. | Must | Resultaat bijgewerkt ≤ 1 s na de laatste toetsaanslag | Test |
| <a id="bw-2"></a>BW-2 | De site moet per controle die niet `ok` is één zin tonen over wat ontbreekt. | Must | 1 zin per controle; 0 controles met alleen een kleur | Test |
| <a id="bw-3"></a>BW-3 | De site moet per bewijsonderdeel een van drie statussen tonen: Compleet, Bijna of „Nog niet". | Must | 3 statussen; elke status heeft tekst | Test |
| <a id="bw-4"></a>BW-4 | De site moet geen score, percentage, punt, badge of ranglijst tonen. | Must | 0 numerieke scores of ranglijsten in 100 % van de pagina's | Inspectie |
| <a id="bw-5"></a>BW-5 | De site moet de status van een bewijsonderdeel afleiden met de statusregel uit §5. | Must | 27 combinaties (3 soorten × 3 resultaten) geven de verwachte status | Test |
| <a id="bw-6"></a>BW-6 | Bij status Compleet moet de site melden: „Aanwezig en consistent. Of het goed is, bespreek je met je coach." | Should | 1 melding met die strekking bij 100 % van de Compleet-onderdelen | Inspectie |
| <a id="bw-7"></a>BW-7 | Bij status „Nog niet" moet de site de lijst van ontbrekende punten tonen met een link naar het modelantwoord van de oefencasus. | Should | 1 lijst en 1 link per onderdeel | Test |
| <a id="bw-8"></a>BW-8 | Elke controle moet een zuivere functie zijn die zonder netwerk een invoer ontvangt en `ok`, `let op` of `mist` teruggeeft. | Must | 0 netwerkverzoeken en 0 neveneffecten per aanroep | Test |
| <a id="bw-9"></a>BW-9 | Elke controle moet bij `let op` of `mist` een zin teruggeven die zegt wat ontbreekt. | Must | 1 zin bij 100 % van de niet-`ok`-resultaten | Test |
| <a id="bw-10"></a>BW-10 | Controles van soort B moeten samenhang tussen bewijsonderdelen toetsen. | Must | 5 samenhangcontroles: EV-01 → EV-06, EV-07 → EV-02, EV-08 → EV-06, EV-11 → EV-01, EV-11 → EV-06 | Test |
| <a id="bw-11"></a>BW-11 | Controles van soort C mogen alleen aantal woorden en zinnen tellen en geen kwaliteit van de reden beoordelen. | Must | 0 controles met een inhoudelijk oordeel | Inspectie |
| <a id="bw-12"></a>BW-12 | Elk bewijsonderdeel moet aan minstens één onderdeel van een LUK zijn gekoppeld. | Must | 11 van 11 onderdelen met ≥ 1 koppeling | Test (contentcontrole) |
| <a id="bw-13"></a>BW-13 | De site moet het dekkingsoverzicht van §4.3 tonen, bijgewerkt met de status van de student. | Must | 13 onderdelen met dekking en status | Demonstratie |

### 6.6 Bewijsrecord en versies (RC)

| ID | Eis | Prio | Criterium | Verificatie |
|---|---|---|---|---|
| <a id="rc-1"></a>RC-1 | Elk bewijsrecord moet een JSON-object zijn met de velden `schema`, `id`, `taak`, `leerblok`, `luk`, `bc`, `inhoud`, `controles`, `status`, `voorlopig`, `versie`, `bijgewerkt` en `elearning`. | Must | 13 velden; 100 % van de records valideert tegen schema 1.0 | Test |
| <a id="rc-2"></a>RC-2 | De site moet `luk` en `bc` uit het contentbestand van de taak halen en niet uit de invoer van de student. | Must | 0 records waarin `luk` of `bc` uit invoer komt | Test |
| <a id="rc-3"></a>RC-3 | Een bewijsrecord mag de naam of alias van de student niet bevatten. | Must | 0 records met een alias of naam | Test |
| <a id="rc-4"></a>RC-4 | De site moet in een record de invoer van de student (`inhoud`) gescheiden houden van het resultaat van de controles (`controles`). | Should | 2 gescheiden velden in 100 % van de records | Inspectie |
| <a id="rc-5"></a>RC-5 | Bij elke wijziging in een bewijsonderdeel moet de site een nieuwe versie opslaan en de vorige versies bewaren. | Must | Na 5 wijzigingen: 5 versies aanwezig; `versie` loopt op met 1 | Test |
| <a id="rc-6"></a>RC-6 | De student moet oudere versies van een bewijsonderdeel kunnen bekijken. | Should | 5 van 5 versies raadpleegbaar | Test |

### 6.7 Bewijsonderdelen (EV)

Elke regel: de site moet het onderdeel alleen als Compleet aanmerken als de genoemde controleset slaagt.

| ID | Onderdeel van de LUK (claim) · taak | Prio | Controleset (criterium) | Verificatie |
|---|---|---|---|---|
| <a id="ev-01"></a>EV-01 | Formuleert een onderzoeksvraag (LUK 1) · 2.1 | Must | 3 velden (gebruiker, probleem/pain/gain, waardecreatie) elk ≥ 4 woorden; ≥ 1 niet-financieel kapitaal; de vraag verschilt in ≥ 1 woord van de oefencasus | Test |
| <a id="ev-02"></a>EV-02 | Analyseert methodisch en selecteert een model (LUK 1) · 2.2 | Must | 3 zoekvragen met 3 verschillende frames; elke zoekvraag eindigt op een vraagteken; precies 1 model gekozen met een verantwoording van ≥ 1 zin; antwoord op „wat mis je met één frame" ingevuld | Test |
| <a id="ev-03"></a>EV-03 | Zoekt gericht naar bronnen (LUK 1) · 3.1, 3.2 | Must | Per kernbegrip ≥ 1 synoniem en ≥ 1 Engelse term; route A: ≥ 1 zoekoperator (aanhalingstekens, AND/OR/NOT, `*`, `?`); route B: 0 woorden uit de „niet noemen"-lijst in de prompt | Test |
| <a id="ev-04"></a>EV-04 | Beoordeelt een bron (LUK 1) · 4.1 | Must | Auteur, jaar, titel en link ingevuld; 5 AAOCC-oordelen elk met ≥ 1 zin toelichting; route B: 2 verificatievinkjes gezet; jaar in de APA-regel gelijk aan het jaar-veld; link begint met `https://` of `doi.org` | Test |
| <a id="ev-05"></a>EV-05 | Onderbouwt een oordeel over AI-bronnen (LUK 1) · 4.2 | Should | 1 kant gekozen; argument van ≥ 2 zinnen | Test |
| <a id="ev-06"></a>EV-06 | Betrekt stakeholders (LUK 1) · 5.1 | Must | ≥ 5 stakeholders, ≥ 1 intern en ≥ 1 extern; per stakeholder invloed, belang en relatie ingevuld; de gebruiker uit EV-01 staat in de lijst; vraagstuk in 1 zin | Test |
| <a id="ev-07"></a>EV-07 | Onderscheidt feit en aanname bij de achtergrond (LUK 1) · 6.1, 7.1, 8.1 | Must | ≥ 3 kernbeweringen elk als feit of aanname gelabeld en aan 1 onderdeel (klanttaak, pain, gain, product of dienst, pain reliever, gain creator, bouwsteen) gekoppeld; elk feit met ≥ 1 bron- of herkomstregel; elke aanname gekoppeld aan 1 zoekvraag uit EV-02 | Test |
| <a id="ev-08"></a>EV-08 | Plaatst het vraagstuk (LUK 1) · 9.1, 9.2 | Must | 3 antwoorden elk met ≥ 1 stakeholder uit EV-06; vergelijking van pain/gain en waarde met het VPC afgevinkt; onderzoeksvraag als feit of aanname gelabeld; foto-vinkje voor 4 producten gezet | Test |
| <a id="ev-09"></a>EV-09 | Haalt feedback op en geeft feedback (LUK 5) · 6.2, Wissel in leerblok 1 en 4 | Must | Ik zie, ik mis en ik vraag me af elk ingevuld; 1 actie met 1 status; ≥ 1 zelf gegeven feedbackregel; de eigen EV-01 en EV-02 zijn niet letterlijk gelijk aan het ontvangen wisselblok (0 tekens verschil = `let op`) | Test |
| <a id="ev-10"></a>EV-10 | Reflecteert op eigen handelen (LUK 5) · STARR | Must | 5 delen (situatie, taak, actie, resultaat, reflectie) ingevuld; reflectie noemt ≥ 1 gedragskeuze uit de keuzelijst en 1 volgende stap | Test |
| <a id="ev-11"></a>EV-11 | Verbindt modellen tot één beeld (LUK 1, bereidt LUK 2 voor) · 9.4 | Must | ≥ 6 verbanden met ≥ 2 verbandtypen, elk met ≥ 1 zin; elk deel van de user story (gebruiker, pain/gain, waarde) verbonden met ≥ 1 VPC-kaart; de kapitalen uit EV-01 verbonden met ≥ 1 gain, pain reliever of gain creator; ≥ 1 spanning met een stakeholder uit EV-06; synthese-alinea met kaarten uit ≥ 2 modellen; 3 antwoorden op „wat laat dit model niet zien"; niet letterlijk gelijk aan het ontvangen wisselblok | Test |

### 6.8 Dossier en verificatie (DS)

| ID | Eis | Prio | Criterium | Verificatie |
|---|---|---|---|---|
| <a id="ds-1"></a>DS-1 | De site moet gegevens automatisch in de browser opslaan. | Must | 0 verloren invoervelden na herladen van de pagina | Test |
| <a id="ds-2"></a>DS-2 | De site moet na elk leerblok en na elke tien wijzigingen de melding „bewaar je dossier" tonen. | Must | 4 meldingen (1 per leerblok) en 1 melding per 10 wijzigingen | Test |
| <a id="ds-3"></a>DS-3 | De site moet een eerder geëxporteerd dossier kunnen importeren. | Must | 0 verschillen tussen records vóór export en na import | Test |
| <a id="ds-4"></a>DS-4 | De site moet een dossier uit een eerdere 1.x-schemaversie kunnen importeren. | Must | 0 foutmeldingen bij een dossier uit elke eerdere 1.x-versie | Test |
| <a id="ds-5"></a>DS-5 | De site moet het dossier exporteren als JSON met alle bewijsrecords (nieuwste versie en het aantal eerdere versies), de alias, het teamnummer en de e-learningversie. | Must | 5 onderdelen aanwezig in 100 % van de exports | Test |
| <a id="ds-6"></a>DS-6 | De export moet een SHA-256-controlesom over de inhoud bevatten. | Must | 1 controlesom van 64 hexadecimale tekens | Test |
| <a id="ds-7"></a>DS-7 | De site moet het dossier ook exporteren als afdrukbare pagina per leeruitkomst, met status per bewijsonderdeel, ingevulde inhoud en de controlesom onderaan. | Must | 3 pagina's (LUK 1, 2 en 5) met 3 onderdelen elk | Inspectie |
| <a id="ds-8"></a>DS-8 | De verificatiepagina moet een dossier lokaal inlezen, de controlesom herberekenen en bij een afwijking „gewijzigd na export" melden. | Must | 1 gewijzigd teken → 1 melding (100 %); 0 meldingen bij een ongewijzigd bestand; test met 2 bestanden | Test |
| <a id="ds-9"></a>DS-9 | De verificatiepagina moet meerdere dossiers tegelijk inlezen en een tabel tonen met per student de status per bewijsonderdeel en per leeruitkomst, met de ontbrekende onderdelen bovenaan. | Must | ≥ 5 dossiers tegelijk; 11 bewijsonderdelen en 3 leeruitkomsten per student | Test |
| <a id="ds-10"></a>DS-10 | De verificatiepagina mag geen dossiergegevens uploaden. | Must | 0 uitgaande verzoeken met dossierinhoud | Test (netwerktrace) |
| <a id="ds-11"></a>DS-11 | De dossierpagina moet een scherm „Mijn stand" bieden met per bewijsonderdeel alleen de status, groot, zonder inhoud. | Should | 11 statussen; 0 inhoudsvelden | Demonstratie |
| <a id="ds-12"></a>DS-12 | Als de browseropslag is geblokkeerd, moet de site dat melden en direct export aanbieden. | Must | 1 melding en 1 exportknop ≤ 1 s na het laden in een privévenster | Test |

### 6.9 De Wissel (WS)

| ID | Eis | Prio | Criterium | Verificatie |
|---|---|---|---|---|
| <a id="ws-1"></a>WS-1 | In leerblok 1 en 4 moet de site een wisselblok met onderzoeksvraag en zoekvragen zonder alias naar het klembord kopiëren. | Should | 0 aliassen in het wisselblok; 1 klik | Test |
| <a id="ws-2"></a>WS-2 | In leerblok 4 moet het wisselblok ook de lijst van verbanden bevatten. | Should | 1 lijst met alle verbanden uit EV-11 | Test |
| <a id="ws-3"></a>WS-3 | De site moet de student het wisselblok van een wisselpartner (teamgenoot, medestudent of coach) laten plakken. | Should | 3 rollen van wisselpartner geaccepteerd | Test |
| <a id="ws-4"></a>WS-4 | De site moet de student „ik zie / ik mis / ik vraag me af" en één actie met een status laten vastleggen bij een ontvangen wisselblok. | Should | 3 tekstvelden, 1 actie, 1 status | Test |
| <a id="ws-5"></a>WS-5 | Feedback die via het klembord terugkomt moet bij de eerste student als ontvangen feedback in EV-09 verschijnen. | Should | 1 regel als ontvangen én 1 regel als gegeven in EV-09 na een uitwisseling van 2 testers | Test (2 browsers) |
| <a id="ws-6"></a>WS-6 | De site moet de post-its van andere teams na de gallery walk met de rol „ander team" en één teamactie op dezelfde wijze laten vastleggen. | Should | 1 rol „ander team"; 1 teamactie; zichtbaar op de dossierpagina naast individuele feedback | Test |
| <a id="ws-7"></a>WS-7 | Als de eigen EV-01, EV-02 of EV-11 letterlijk gelijk is aan het ontvangen wisselblok, moet de site „let op: dit is de tekst van je wisselpartner" melden. | Should | 0 tekens verschil → 1 melding; status blijft Bijna | Test |
| <a id="ws-8"></a>WS-8 | Zolang geen feedback is ontvangen, moet EV-09 op Bijna blijven, ook na ≥ 14 dagen. | Should | Status Bijna na 14 dagen zonder feedback; Compleet na ontvangst | Test (aangepaste tijdstempels) |
| <a id="ws-9"></a>WS-9 | De Wissel moet zonder server werken. | Must | 0 verzoeken met wisselblokinhoud naar de site of naar derden | Test (netwerktrace) |
| <a id="ws-10"></a>WS-10 | De privacytekst bij de Wissel moet het klembord noemen als kanaal waarlangs gegevens de browser verlaten. | Should | 1 tekst in de Wissel-flow; ≤ 60 woorden | Inspectie |
| <a id="ws-11"></a>WS-11 | Als een actie bij het openen van de site ≥ 7 dagen dezelfde status heeft, moet de site een herinnering tonen om de status te zetten. | Could | 1 herinnering na 7 dagen; 0 herinneringen bij 6 dagen | Test (aangepaste tijdstempels) |

### 6.10 Verbanden ontdekken (VB)

| ID | Eis | Prio | Criterium | Verificatie |
|---|---|---|---|---|
| <a id="vb-1"></a>VB-1 | Leerblok 4 moet als zelfstandige taak 9.4 een verbanden-kaart bieden met drie kolommen: de delen van de user story uit EV-01, de VPC-onderdelen uit EV-07 en de zes kapitalen (financieel, productie, intellectueel, menselijk, sociaal en relationeel, natuurlijk). | Must | 3 kolommen; 6 kapitalen | Demonstratie |
| <a id="vb-2"></a>VB-2 | De site moet de student eerst een oefencasus met drie open vragen laten doen en het modelvoorbeeld pas na een eigen poging tonen. | Must | 3 open vragen; 0 modelvoorbeelden zichtbaar vóór ≥ 1 getrokken lijn | Test |
| <a id="vb-3"></a>VB-3 | De student moet lijnen tussen kaarten kunnen trekken, elk met één van drie typen (hoort bij, leidt tot, gaat ten koste van) en één zin waarom. | Must | 3 typen; 1 zin per lijn; ≥ 6 lijnen in een testprofiel | Test |
| <a id="vb-4"></a>VB-4 | De site moet kaarten zonder lijn en kapitalen uit EV-01 zonder verband als open vraag tonen, zonder het ontbrekende verband als antwoord te geven. | Must | 100 % van de open plekken als vraag; 0 antwoorden in een leeg en een half ingevuld voorbeeld | Test |
| <a id="vb-5"></a>VB-5 | De site moet de student elk kapitaal laten markeren als input, uitkomst (+) of uitkomst (−). | Must | 6 kapitalen; 3 markeringen | Test |
| <a id="vb-6"></a>VB-6 | De site moet minstens één lijn „gaat ten koste van" (een spanning) vragen met de stakeholder uit EV-06 die dat merkt. | Must | ≥ 1 spanning; 1 stakeholder gekoppeld | Test |
| <a id="vb-7"></a>VB-7 | De site moet een synthese-alinea bieden van hoogstens vijf zinnen waarin de student kaarten uit minstens twee modellen als chips invoegt, en drie korte antwoorden op „wat laat dit model niet zien" voor user story, VPC en zes kapitalen. | Must | ≤ 5 zinnen; kaarten uit ≥ 2 modellen; 3 antwoorden | Test |
| <a id="vb-8"></a>VB-8 | De lijst van verbanden moet in het A3-tekstblok van LB-16 staan. | Should | 1 lijst met alle verbanden in het tekstblok | Test |
| <a id="vb-10"></a>VB-10 | De site moet de getrokken lijnen automatisch tussen de kolommen tekenen. | Should | 100 % van de lijnen getekend; 0 handmatige tekenacties | Test |
| <a id="vb-9"></a>VB-9 | Taak 9.4 moet een zelfstandige taak van 20 min richttijd zijn en geen blok in het werkcollege. | Should | 20 min richttijd; 0 onderdelen in het werkcollegeprogramma | Inspectie |

### 6.11 Terugblik en tussenpozen (TP)

| ID | Eis | Prio | Criterium | Verificatie |
|---|---|---|---|---|
| <a id="tp-1"></a>TP-1 | Elk leerblok vanaf 2 moet beginnen met een terugblik van hoogstens 15 min bovenop de 45 min van het leerblok. | Should | 3 leerblokken (2, 3, 4); ≤ 15 min; leerblok samen ≤ 60 min | Test |
| <a id="tp-2"></a>TP-2 | In de terugblik moet de site de student eerst uit het hoofd minstens drie punten uit het vorige leerblok laten opschrijven en twee kennisvragen laten beantwoorden voordat de meenemen-kaart zichtbaar is. | Should | 0 kaarten zichtbaar vóór ≥ 3 punten of „ik weet het nog"; 2 kennisvragen | Test |
| <a id="tp-3"></a>TP-3 | De site moet daarna de meenemen-kaart tonen met de belangrijkste items van het vorige leerblok en de eigen bewijsstukken uit dat leerblok. | Should | Items volgens LRD 8.5 voor 3 leerblokken; ≥ 1 eigen bewijsstuk | Test |
| <a id="tp-4"></a>TP-4 | De site moet de student in twee zinnen laten schrijven waar hij of zij dit nu gebruikt, met één item uit de kaart als startpunt van het leerblok. | Should | 2 zinnen; 1 item gekozen | Test |
| <a id="tp-5"></a>TP-5 | De student moet de terugblik met „ik weet het nog" kunnen overslaan, en de terugblik mag geen bewijs leveren. | Should | 1 klik; 0 bewijsrecords uit de terugblik | Test |
| <a id="tp-6"></a>TP-6 | De site moet de pauze tussen twee leerblokken in dagen berekenen uit de tijdstempels van het dossier. | Should | 0 dagen afwijking van het verschil tussen de tijdstempels | Test |
| <a id="tp-7"></a>TP-7 | De site moet de lengte van de terugblik aanpassen aan de pauze: < 2 uur alleen de transfervraag; ≥ 2 uur tot < 2 dagen de transfervraag en 1 kennisvraag (≈ 5 min); 2 tot 13 dagen de volledige terugblik (≤ 15 min); ≥ 14 dagen de volledige terugblik plus een tekstsamenvatting van het vorige leerblok. | Should | 4 bandbreedtes; 4 testprofielen (1 uur, 1 dag, 5 dagen, 14 dagen) tonen de verwachte terugblik | Test (aangepaste tijdstempels) |
| <a id="tp-8"></a>TP-8 | Het dossier moet de pauze in dagen en de vermelding „gedaan" of „overgeslagen" van de terugblik loggen. | Should | 2 velden per leerblok vanaf 2 | Test |
| <a id="tp-9"></a>TP-9 | Aan het begin van leerblok 2 tot en met 4 moet de site controleren of het dossier aanwezig is, anders een import aanbieden en de ontbrekende bewijsonderdelen van eerdere leerblokken melden. | Must | 3 leerblokken; na leegmaken van de opslag 1 importaanbod en 1 lijst met ontbrekende onderdelen; 0 verloren gegevens na import | Test |
| <a id="tp-10"></a>TP-10 | De contentbestanden moeten per leerblok een veld voor een aanbevolen week en dag bevatten dat de student als tekst ziet zonder dat het iets blokkeert. | Could | 4 velden; 0 blokkades | Test |
| <a id="tp-11"></a>TP-11 | Aan het begin van leerblok 2 tot en met 4 moet de site één scherm „Vorige keer" tonen met achtereenvolgens de dossiercontrole (TP-9), de terugblik met meenemen-kaart en de transfervraag. | Should | 1 scherm; 3 onderdelen in vaste volgorde | Demonstratie |

### 6.12 Media (MD)

| ID | Eis | Prio | Criterium | Verificatie |
|---|---|---|---|---|
| <a id="md-1"></a>MD-1 | Elk leerblok moet dezelfde stof in drie routes bieden: tekst, video en spel of simulatie. | Should | 4 leerblokken × 3 routes | Inspectie |
| <a id="md-2"></a>MD-2 | De site moet de tekst als standaard tonen met twee kleine knoppen voor video en spel of simulatie, de laatste keuze onthouden en elke route laten uitkomen bij dezelfde „klaar als"-regel en oefentaak. | Should | 1 standaardroute; 2 knoppen; 3 routes met dezelfde „klaar als" | Test |
| <a id="md-3"></a>MD-3 | De uitlegtekst per leerblok moet uit hoogstens 300 woorden bestaan, met een voorbeeld en het modelantwoord van de oefencasus. | Should | ≤ 300 woorden per leerblok; 1 voorbeeld | Inspectie |
| <a id="md-4"></a>MD-4 | Een eigen video moet hoogstens 3 min duren en hoogstens 20 MB groot zijn. | Should | ≤ 3 min; ≤ 20 MB per video; 4 video's (V1–V4) | Inspectie |
| <a id="md-5"></a>MD-5 | Een eigen video moet ondertitels (WebVTT) en een transcript hebben. | Must | 2 hulpmiddelen per video; 100 % van de video's | Inspectie |
| <a id="md-6"></a>MD-6 | Een eigen video mag niet automatisch starten en moet pas na een klik laden. | Must | 0 videoverzoeken vóór de klik; 0 autoplay | Test |
| <a id="md-7"></a>MD-7 | Eigen video's moeten op dezelfde site staan, zonder inbedding van derden. | Must | 0 verzoeken naar andere domeinen bij het afspelen | Test (netwerktrace) |
| <a id="md-8"></a>MD-8 | Een spel of simulatie moet hoogstens 5 min duren. | Should | ≤ 5 min; 4 spellen (Vraagslijper, Bronnen-detective, Stakeholder-radar, Waarde-simulator) | Inspectie |
| <a id="md-9"></a>MD-9 | Een spel of simulatie moet met alleen het toetsenbord te bedienen zijn en een tekstversie hebben. | Must | 0 muisacties voor een volledige doorloop; 1 tekstversie per spel | Test |
| <a id="md-10"></a>MD-10 | Een spel of simulatie moet bij elke keuze feedback geven en geen score of ranglijst tonen. | Must | 1 feedback per keuze; 0 scores | Test |
| <a id="md-11"></a>MD-11 | Een spel of simulatie moet deel uitmaken van de oefenversie en mag geen bewijs leveren. | Must | 0 bewijsrecords uit een spel | Test |
| <a id="md-12"></a>MD-12 | Elk leerblok moet volledig te doen zijn met alleen tekst. | Must | 4 leerblokken afgerond zonder video of spel | Test |
| <a id="md-13"></a>MD-13 | Spel en simulatie moeten in de browser zonder netwerk werken. | Should | 0 netwerkverzoeken tijdens het spelen | Test |
| <a id="md-14"></a>MD-14 | Video en achtergrond van derden (Bureau Tromp, MIT OpenCourseWare, Atlassian) moeten als gewone link verschijnen, zonder inbedding. | Must | 0 ingebedde frames van derden | Inspectie |
| <a id="md-15"></a>MD-15 | Elk spel en elke simulatie moet fictieve voorbeelden duidelijk als fictief markeren. | Should | 100 % van de fictieve bronkaarten met aanduiding „fictief" | Inspectie |
| <a id="md-16"></a>MD-16 | Leerblok 1 moet twee externe kijktips als gewone link tonen: Bureau Tromp (Nederlands) als instap en het MIT OpenCourseWare-fragment over de A3 als denkwijze als verdieping, elk met bron, duur en taal. | Should | 2 links; 2 van 2 met duur en taal; 0 ingebedde frames | Inspectie |

### 6.13 Bronnen (BR)

| ID | Eis | Prio | Criterium | Verificatie |
|---|---|---|---|---|
| <a id="br-1"></a>BR-1 | De site moet een bronnenpagina bieden met alle bronnen uit de contentbestanden in APA, 7e editie (Nederlandse conventies), alfabetisch. | Must | 100 % van de bronnen op de pagina; 0 volgordefouten | Test (contentcontrole) |
| <a id="br-2"></a>BR-2 | De bronnenpagina moet per bron een werkende DOI of URL als link tonen, waar die bestaat. | Must | 0 dode links | Test (linkcontrole) |
| <a id="br-3"></a>BR-3 | Een bron zonder openbare publicatie moet als „ongepubliceerd document" met de organisatie worden vermeld. | Must | 100 % van de niet-openbare bronnen zo vermeld | Inspectie |
| <a id="br-4"></a>BR-4 | Teksten, video's en spellen moeten bronnen tonen als in-tekstverwijzing (Auteur, jaar) die naar de bronnenpagina klikt. | Must | 100 % van de verwijzingen klikt naar een bronregel | Test |
| <a id="br-5"></a>BR-5 | De contentcontrole moet falen als een verwijzing geen bronregel heeft of een bronregel nergens wordt geciteerd. | Must | 0 verwijzingen zonder bronregel; 0 bronregels zonder citatie | Test |
| <a id="br-6"></a>BR-6 | De workflow moet bij elke publicatie alle DOI's en URL's op werking controleren. | Must | 100 % van de links gecontroleerd per publicatie | Test |

### 6.14 Licentie en auteursrecht (LI)

| ID | Eis | Prio | Criterium | Verificatie |
|---|---|---|---|---|
| <a id="li-1"></a>LI-1 | De site mag alleen eigen tekst en eigen afbeeldingen plus links bevatten. | Must | 0 kopieën van Brightspace-materiaal, PhoneVentures-handleidingen, slides van derden of opgeslagen pagina's van derden | Inspectie |
| <a id="li-2"></a>LI-2 | De site mag de afbeeldingen van het Strategyzer-canvas en het IIRC-waardecreatiemodel niet inbedden; ze moet de kolomindeling zelf tekenen en naar de bronnen linken. | Must | 0 ingebedde afbeeldingen van beide bronnen | Inspectie |
| <a id="li-3"></a>LI-3 | De site mag geen tekst uit het TOM³-buildplan kopiëren, alleen een eigen samenvatting met bronvermelding. | Must | 0 zinnen ≥ 8 woorden gelijk aan de bron | Analyse |
| <a id="li-4"></a>LI-4 | De repository moet onder Creative Commons BY-SA 4.0 vallen en een `LICENSE`-bestand met de licentietekst bevatten. | Must | 1 `LICENSE`-bestand met de tekst van CC BY-SA 4.0 | Inspectie |
| <a id="li-5"></a>LI-5 | Elke pagina moet de licentie-aanduiding en de naamsvermelding tonen met een link naar de licentietekst. | Must | 100 % van de pagina's met aanduiding, naamsvermelding en 1 link | Inspectie |

### 6.15 Privacy (PR)

| ID | Eis | Prio | Criterium | Verificatie |
|---|---|---|---|---|
| <a id="pr-1"></a>PR-1 | De site mag geen cookies, analytics, externe lettertypen of externe scripts gebruiken. | Must | 0 cookies; 0 verzoeken naar andere domeinen tijdens een volledige doorloop van 4 leerblokken | Test (netwerktrace) |
| <a id="pr-2"></a>PR-2 | Persoonsgegevens (alias, teamnummer, ingevulde teksten) mogen de browser alleen verlaten door de export of het klembord van de student. | Must | 0 uitgaande verzoeken met persoonsgegevens | Test (netwerktrace) |
| <a id="pr-3"></a>PR-3 | De docentmodus mag geen studentgegevens verwerken of bewaren. | Must | 0 studentgegevens in de opslag van het docentapparaat | Test |
| <a id="pr-4"></a>PR-4 | De docentmodus mag geen koppeling hebben met de apparaten van studenten. | Must | 0 verbindingen tussen docent- en studentapparaten | Test (netwerktrace) |

### 6.16 Docentmodus (DM)

De docentmodus is een tweede weergave van dezelfde contentbestanden, bedoeld voor de beamer. Een **onderdeel** is een stap van het draaiboek van 5 min of een veelvoud; een **leerblok** is een van de vier eenheden uit §4.2.

| ID | Eis | Prio | Criterium | Verificatie |
|---|---|---|---|---|
| <a id="dm-1"></a>DM-1 | De site moet een docentmodus bieden die bij de start of met een adres-toevoeging te kiezen is, zonder inloggen. | Must | 0 accounts; 1 keuze of 1 adres-toevoeging | Test |
| <a id="dm-2"></a>DM-2 | De docentmodus moet dezelfde contentbestanden gebruiken als de studentweergave. | Must | 0 gedupliceerde contentbestanden; 1 wijziging in een modelantwoord verschijnt in beide weergaven | Test |
| <a id="dm-3"></a>DM-3 | De docentmodus moet per onderdeel een projecteerbare stapkaart tonen met taaknummer, opdracht in groot lettertype, „klaar als", tijd, materiaal, de dia's van het slidedeck en de aanduiding „laptop open" of „laptop dicht". | Must | 7 elementen per stapkaart | Inspectie |
| <a id="dm-4"></a>DM-4 | De docentmodus moet een klok bieden die per deel vanaf 0:00 loopt, met een aftelling per onderdeel en de acties start, pauze en reset. | Must | 1 klok; 1 aftelling per onderdeel; 3 acties; afwijking ≤ 1 s over 10 min | Test |
| <a id="dm-5"></a>DM-5 | De klok moet de tijd als richttijd tonen en mag geen student of docent blokkeren. | Must | 0 blokkades bij overschrijding van 100 % van de richttijd | Test |
| <a id="dm-6"></a>DM-6 | Bij de gallery walk moet de klok twee rondes van 4 min en 2 min leestijd tonen. | Should | 2 × 4 min + 2 min = 10 min | Test |
| <a id="dm-7"></a>DM-7 | De docentmodus moet per onderdeel een docentkaart tonen met wat de docent doet, de kernboodschap, de rondloopvragen en „als het anders loopt". | Must | 4 elementen per docentkaart; 100 % van de onderdelen | Inspectie |
| <a id="dm-8"></a>DM-8 | De docentmodus moet modelantwoorden en veelgemaakte fouten pas tonen nadat de docent ze opent. | Must | 0 modelantwoorden zichtbaar vóór de klik | Test |
| <a id="dm-9"></a>DM-9 | De docent moet onderdelen kunnen overslaan, verschuiven en de tijd van een onderdeel aanpassen, waarna de klok de resterende tijd opnieuw uitrekent. | Must | Resterende tijd = som van resterende onderdelen ± 1 s na overslaan van 2 onderdelen | Test |
| <a id="dm-10"></a>DM-10 | De docentmodus moet per deel een programmaoverzicht tonen met wat klaar is en wat komt, en de docent de begintijden uit het rooster laten invullen. | Could | 1 overzicht; begintijden invulbaar per deel | Demonstratie |
| <a id="dm-11"></a>DM-11 | De docentmodus moet de docentkaarten van een deel als draaiboek kunnen afdrukken uit dezelfde contentbestanden. | Should | Afdruk deel 1 bevat 100 % van de onderdelen, tijden en rondloopvragen van het scherm | Inspectie |
| <a id="dm-12"></a>DM-12 | De site moet het werkboek van een deel kunnen afdrukken uit dezelfde contentbestanden, met dezelfde nummers en „klaar als"-regels. | Should | 100 % van de nummers en „klaar als"-regels gelijk aan de site | Inspectie |
| <a id="dm-13"></a>DM-13 | De stapkaart moet de bijbehorende video met ondertitels afspelen en het spel starten. | Should | 1 video en 1 spel per stapkaart waar bestaand; 0 verzoeken naar andere domeinen | Test |
| <a id="dm-14"></a>DM-14 | De docentmodus moet per leerblok een terugblik-kaart met de vragen uit LRD 8.5 tonen. | Should | 3 kaarten (leerblok 2, 3, 4) | Inspectie |
| <a id="dm-15"></a>DM-15 | De docentmodus moet na het laden zonder netwerk blijven werken. | Must | 0 foutmeldingen bij 15 min zonder netwerk | Test |
| <a id="dm-16"></a>DM-16 | De stapkaart moet leesbaar zijn vanaf de achterste rij van het lokaal. | Must | Tekst ≥ 28 px op 1280 × 720; contrast ≥ 4,5:1; 1 student op de achterste rij leest de opdracht voor | Test in het lokaal |
| <a id="dm-17"></a>DM-17 | De docentmodus mag geen beoordelingsdetails of toetsantwoorden bevatten. | Must | 0 beoordelingsdetails; alleen didactische aanwijzingen en modelantwoorden van de oefencasus | Inspectie |
| <a id="dm-18"></a>DM-18 | De docentmodus moet alle onderdelen van het werkcollege van woensdag bevatten. | Must | 19 onderdelen (11 in deel 1, 8 in deel 2) plus de 3 pauzes in deel 2 | Inspectie |

---

## 7. Non-functionele requirements

### 7.1 Toegankelijkheid (TG)

| ID | Eis | Prio | Criterium | Verificatie |
|---|---|---|---|---|
| <a id="tg-1"></a>TG-1 | Elke pagina moet voldoen aan WCAG 2.1 niveau AA. | Must | Lighthouse-score toegankelijkheid ≥ 95 op 100 % van de pagina's | Test |
| <a id="tg-2"></a>TG-2 | Leerblok 1 moet zonder muis in te vullen en te bewaren zijn. | Must | 0 muisacties voor een volledige doorloop | Test |
| <a id="tg-3"></a>TG-3 | Tekst moet een contrast hebben van minstens 4,5:1. | Must | ≥ 4,5:1 op 100 % van de tekstelementen | Test |
| <a id="tg-4"></a>TG-4 | De site mag geen informatie alleen in kleur geven. | Must | 3 statussen elk met tekst naast de kleur | Inspectie |
| <a id="tg-5"></a>TG-5 | De site moet met een schermlezer bruikbaar zijn. | Must | 0 onbereikbare invoervelden in leerblok 1 met een schermlezer | Test |

### 7.2 Prestaties en compatibiliteit (PF)

| ID | Eis | Prio | Criterium | Verificatie |
|---|---|---|---|---|
| <a id="pf-1"></a>PF-1 | De site moet responsive zijn van 360 px breed tot desktop. | Must | 0 px horizontale scroll op 360 px; alle velden van 4 leerblokken invulbaar | Test |
| <a id="pf-2"></a>PF-2 | De site moet werken in de twee laatste versies van Chrome, Safari, Firefox en Edge. | Must | 4 browsers × 2 versies zonder functieverlies | Test |
| <a id="pf-3"></a>PF-3 | Een leerblok moet na het laden zonder netwerk bruikbaar zijn. | Must | 0 netwerkverzoeken tijdens 45 min gebruik van een geladen leerblok, behalve videoklikken | Test |
| <a id="pf-4"></a>PF-4 | De eerste lading moet klein blijven. | Must | ≤ 300 kB per pagina zonder video; 0 afbeeldingen van derden | Test |
| <a id="pf-5"></a>PF-5 | Elk leerblok moet een richttijd van 45 min op de pagina tonen, inclusief media. | Must | 45 min; video ≤ 3 min; spel ≤ 5 min; verdieping telt niet mee | Inspectie |

### 7.3 Onderhoud en testbaarheid (QA)

| ID | Eis | Prio | Criterium | Verificatie |
|---|---|---|---|---|
| <a id="qa-1"></a>QA-1 | Alle teksten, werkboekregels, modelantwoorden, LUK-koppelingen en controleparameters moeten uit datafiles komen, zodat een docent ze zonder code kan aanpassen. | Must | 1 modelantwoord aangepast in 1 datafile verschijnt op de site zonder codewijziging (0 codebestanden bewerkt) | Demonstratie |
| <a id="qa-2"></a>QA-2 | Elke controle moet een unittest hebben met drie goede en drie zwakke voorbeelden. | Must | 6 voorbeelden per controle; 100 % geeft het verwachte resultaat en de verwachte melding | Test |
| <a id="qa-3"></a>QA-3 | De contentcontrole moet falen als een taak geen LUK-koppeling, „klaar als", controle of modelantwoord heeft. | Must | 4 ontbrekende onderdelen → 4 fouten; 11 van 11 bewijsonderdelen compleet in de content | Test (sabotagetest) |
| <a id="qa-4"></a>QA-4 | Alle tekst en documentatie moet in het Nederlands zijn, in het register van het werkboek. | Must | 100 % van de zichtbare teksten in het Nederlands, met Engelse vaktermen zoals in het werkboek | Inspectie |
| <a id="qa-5"></a>QA-5 | Engelse vaktermen (frame, pain, gain, fit, user story) moeten op de plek zelf in één zin worden uitgelegd. | Should | 100 % van de termen met ≤ 1 zin uitleg bij het eerste voorkomen | Inspectie |
| <a id="qa-6"></a>QA-6 | Het uiterlijk moet de HAN-huisstijl van de zusterdocumenten volgen. | Could | 100 % van de pagina's met de kleur `#E50056` als accent en het lettertype uit de huisstijl | Inspectie |

### 7.4 Documentatie en deliverables (DL)

| ID | Eis | Prio | Criterium | Verificatie |
|---|---|---|---|---|
| <a id="dl-1"></a>DL-1 | Er moet een docentgids zijn over het gebruik van de docentmodus (klok, stapkaart, onderdelen verschuiven, afdruk), wat het bewijs is en niet is, het inlezen van dossiers, de steekproef en het aanpassen van een modelantwoord. | Must | ≤ 2 pagina's A4; 5 onderwerpen | Inspectie |
| <a id="dl-2"></a>DL-2 | Er moet een studentintroductie zijn over wat je doet, waar je gegevens staan en hoe je exporteert en inlevert. | Must | ≤ 1 pagina A4; 3 onderwerpen | Inspectie |
| <a id="dl-3"></a>DL-3 | Er moet een testrapport zijn met netwerktrace zonder derden, toegankelijkheidscontrole, controle op 360 px en pilotresultaat. | Must | 4 onderdelen | Inspectie |
| <a id="dl-4"></a>DL-4 | Er moet een beschrijving van dossierschema 1.0 zijn. | Should | 13 velden beschreven | Inspectie |

### 7.5 Acceptatie in de pilot (AP)

Drempels zijn startdoelen die na de pilot worden gekalibreerd (aanname A-3). De pilot draait in een werkcollege met minstens twee teams.

| ID | Eis | Prio | Criterium | Verificatie |
|---|---|---|---|---|
| <a id="ap-1"></a>AP-1 | Een pilotstudent moet alle vier de leerblokken op het eigen vraagstuk kunnen doorlopen en een dossier exporteren waarin alle als „gedekt" gemarkeerde onderdelen van §4.3 Compleet of Bijna zijn. | Must | 5 gedekte onderdelen; 1 dossier | Demonstratie |
| <a id="ap-2"></a>AP-2 | De pilotstudenten moeten elk leerblok afronden binnen 1,25 × de richttijd. | Should | ≥ 80 % van ≥ 6 studenten uit 2 teams rondt elk leerblok af binnen 56 min | Test (tijdnotitie docent) |
| <a id="ap-3"></a>AP-3 | Pilotstudenten moeten bij elke taak weten wat ze moeten doen zonder uitleg van de docent. | Should | ≥ 80 % beaamt de stelling | Test (vraag na de pilot) |
| <a id="ap-4"></a>AP-4 | Een docent moet deel 1 (90 min) kunnen leiden met alleen de docentmodus en het slidedeck. | Should | ≤ 2 opzoekmomenten buiten de docentmodus | Test (pilot in het lokaal) |
| <a id="ap-5"></a>AP-5 | Een docent moet vijf dossiers kunnen inlezen en voor elk het zwakste onderdeel noemen. | Should | ≤ 10 min voor 5 dossiers | Test (getimed) |
| <a id="ap-6"></a>AP-6 | Pilotstudenten moeten bij „wat laat dit model niet zien" voor elk van de drie modellen iets noemen dat de docent verdedigbaar vindt. | Should | ≥ 70 % van de studenten | Analyse (lezing van EV-11) |
| <a id="ap-7"></a>AP-7 | Pilotstudenten moeten één medium noemen dat de stof voor hen het best overbracht. | Could | ≥ 70 % noemt 1 medium; verdeling over 3 media genoteerd | Test (vraag na de pilot) |
| <a id="ap-8"></a>AP-8 | Na een pauze van minstens vijf dagen moeten pilotstudenten aan het begin van het tweede leerblok uit het hoofd belangrijke items uit LRD 8.5 noemen. | Should | ≥ 70 % noemt ≥ 3 items | Analyse (terugblik-logs) |
| <a id="ap-9"></a>AP-9 | De modulecoördinator moet de dekkingstabel van §4.3 naast de LUK en BC in Brightspace leggen en de koppelingen bevestigen, inclusief de afwijking bij BC1. | Must | 13 onderdelen bevestigd; 1 afwijking benoemd | Inspectie |

---

## 8. Deliberate exclusies

Zo kan een lezer „niet in deze blueprint" van „nooit" onderscheiden. Het zijn de Won'ts; ze staan niet in de tabellen hierboven.

| ID | Uitsluiting | Aard |
|---|---|---|
| X-1 | Een backend, leerrecordsysteem (LRS, Firebase, Supabase) of andere centrale opslag van bewijs | permanent |
| X-2 | Beoordeling van antwoorden door een AI-model, of een AI-samenvatting van de synthese | permanent |
| X-3 | Scores, badges, streaks of een ranglijst | permanent |
| X-4 | Inloggen met een HAN-account, SCORM- of LTI-pakket | permanent |
| X-5 | Een framework met bouwstap (React, Vue) of een xAPI-standaard | permanent |
| X-6 | Een live klasoverzicht voor de docent, ook via QR-code of tikcode per student | permanent |
| X-7 | Een aparte docent-app of docentsite met eigen inhoud | permanent |
| X-8 | Peer-feedback via chat, gedeeld bord of server; adaptieve leerpaden met eigen module | permanent |
| X-9 | Herinneringen of planning per e-mail of melding | permanent |
| X-10 | Video van derden ingebed in de site | permanent |
| X-11 | Een tweede werkboek naast de site, of het werkboek en draaiboek als losse bronnen | permanent |
| X-12 | Een kant-en-klaar synthesediagram waarin de student de juiste verbanden invult | permanent |
| X-13 | De gewogen score, HCI en VTI uit het TOM³-scoreformulier | permanent |
| X-14 | Een kwaliteitsoordeel, vervanging van de beroepsproducten of fraudebestendig bewijs | permanent |
| X-15 | A3-vak 2 tot en met 8, de diagnose, quick win, big win en de leeruitkomsten LUK 2 (overig), LUK 3 en LUK 4 | buiten scope; uitbreiding volgt een eigen LRD met dezelfde opzet |
| X-16 | Een tweede TOM-model als alternatief voor TOM³ | permanent voor deze e-learning |

---

## 9. Aannames die bevestiging vragen

Concept-waarden, niet vastgesteld. Ze staan hier zodat ze in één ronde kunnen worden beslist. Een aanname ontslaat een regel niet van haar criterium.

- **A-1** — De TOM³-uitwerking van Westmoreland BV is de enige TOM-bron, maar heeft geen openbare publicatie (domein westmoreland.nl geparkeerd bij zoeken op 30 september 2026). Publicatiegegevens en toestemming voor vermelding moeten bij Westmoreland worden opgevraagd. Tot dan geldt BR-3 („ongepubliceerd document"). Raakt BR-3, LB-11, LI-3.
- **A-2** — De koppeltabel bij de beoordelingscriteria zet BC1 bij opdracht 1, 2 en 3, terwijl de beschrijving van opdracht 1 en 2 alleen LUK 1 noemt. Deze blueprint gaat uit van BC1 voor alles wat met analyse te maken heeft. Raakt AP-9, §4.3.
- **A-3** — De drempels 80 %, 70 %, 1,25 × richttijd, ≤ 2 opzoekmomenten en ≤ 10 min zijn startdoelen; de pilot kalibreert ze. Raakt AP-2 t/m AP-8.
- **A-4** — Reactietijd van controles (≤ 1 s, BW-1, LB-2) is een ontworpen waarde en niet uit een bron afgeleid.
- **A-5** — De pauzeband ≥ 2 uur tot < 2 dagen (TP-7) vult een hiaat: het LRD noemt „tot een dag" en „twee tot dertien dagen" en laat 1 tot 2 dagen open.
- **A-6** — Sommige browsers wissen opslag van een site die een week niet is bezocht. TP-9 en DS-2 zijn de mitigatie; de exacte termijn per browser is niet vastgesteld.
- **A-7** — De begintijden van het rooster zijn bij het schrijven onbekend; DM-10 laat de docent ze invullen.
- **A-8** — De DOI's of links van Cepeda e.a. (2006), Mislevy e.a. (2003), Roediger & Karpicke (2006) en het IIRC-framework (2021) zijn in het LRD als „controleren" gemarkeerd. BR-6 controleert ze bij elke publicatie.
- **A-9** — De JavaScript van de site valt onder CC BY-SA 4.0, hoewel Creative Commons zijn licenties voor software afraadt. Bewust geaccepteerd; niet apart uitgezocht (LI-4).
- **A-10** — Standaarden (WCAG 2.1 niveau AA, SHA-256, APA 7e editie, CC BY-SA 4.0) zijn overgenomen uit het LRD en in deze blueprint niet opnieuw tegen de primaire bron gecontroleerd.
- **A-11** — Het werkboek van week 5 bevat 15 taken, maar slechts 3 „Klaar als"-regels en 6 „Waarom"-regels, terwijl TK-2 beide bij 100 % van de taken eist. De ontbrekende regels moeten door de auteur worden geschreven en goedgekeurd (raakt TK-2, BW-12, QA-3).

---

## 10. Bronnen

Volledige APA-vermeldingen staan in het LRD, Bijlage A. Hier alleen de bronnen waarop regels in deze blueprint steunen.

- Anderson, L. W. & Krathwohl, D. R. (Red.). (2001). *A taxonomy for learning, teaching, and assessing*. Longman. (§4.1)
- Biggs, J. & Tang, C. (2011). *Teaching for quality learning at university* (4e ed.). Open University Press. (§2)
- Bureau Tromp. (2023, 9 februari). *Wat is de A3 verbetermethode?* [Video]. YouTube. https://www.youtube.com/watch?v=hVYtuPjMeYg (MD-16)
- MIT OpenCourseWare. (2014, 6 maart). *Ses. 3-4: A3 thinking* [Video]. YouTube. https://www.youtube.com/watch?v=z1KloN7Ub0M (MD-16)
- Cepeda, N. J., e.a. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin, 132*(3), 354–380. (TP-1–TP-9)
- Hattie, J. & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. (§2)
- Mayer, R. E. (2004). Should there be a three-strikes rule against pure discovery learning? *American Psychologist, 59*(1), 14–19. (VB-2, VB-4)
- Mislevy, R. J., Almond, R. G. & Lukas, J. F. (2003). *A brief introduction to evidence-centered design* (RR-03-16). ETS. (§2, EV)
- Roediger, H. L., III & Karpicke, J. D. (2006). Test-enhanced learning. *Psychological Science, 17*(3), 249–255. (TP-2)
- Westmoreland BV. (z.d.). *Architectuur- en implementatieblauwdruk van het TOM³-model* [Ongepubliceerd document]. (LB-11)
- Interne bronnen: leeruitkomsten en opdrachtomschrijvingen C-cluster; `WK5/Werkboek_A3-start_week5.html`; `WK5/Draaiboek_woensdag_week5.html`; `docs/LRD-ELEARNING-A3.html`.

---

## Bijlage A — Kruisverwijzing LRD → blueprint

Regels zijn hier hergroepeerd en gesplitst tot één verplichting per regel. Elke LRD-eis staat hieronder; „—" betekent dat er geen regel aan hangt, met reden.

### Functionele requirements

| LRD | Blueprint |
|---|---|
| FR-01 | SI-1, SI-3 |
| FR-02 | ST-1, ST-2, PR-2 |
| FR-03 | TK-1 |
| FR-04 | TK-2 |
| FR-05 | TK-3, TK-4, TK-5 |
| FR-06 | TK-6, TK-7 |
| FR-07 | BW-1, BW-2 |
| FR-08 | BW-3, BW-4 |
| FR-09 | BW-12, BW-13 |
| FR-10 | LB-2 |
| FR-11 | LB-3, LB-4 |
| FR-12 | LB-5, LB-6 |
| FR-13 | LB-7 |
| FR-14 | LB-8 |
| FR-15 | LB-9 |
| FR-16 | LB-10, LB-11, LB-12 |
| FR-17 | LB-13 |
| FR-18 | LB-14 |
| FR-19 | LB-15 |
| FR-20 | RC-5, RC-6 |
| FR-21 | DS-1, DS-2, DS-3 |
| FR-22 | DS-5, DS-6, DS-7 |
| FR-23 | DS-8 |
| FR-24 | DS-9 |
| FR-25 | QA-1 |
| FR-26 | ST-6 |
| FR-27 | MD-14, MD-16 |
| FR-28 | TK-10, TK-11, TK-12 |
| FR-29 | DM-1, DM-2 |
| FR-30 | DM-3 |
| FR-31 | DM-4, DM-5, DM-6 |
| FR-32 | DM-7 |
| FR-33 | DM-8 |
| FR-34 | DM-9 |
| FR-35 | DS-11 |
| FR-36 | PR-3, PR-4 |
| FR-37 | DM-11 |
| FR-38 | TK-8, TK-9 |
| FR-39 | TK-13, TK-14 |
| FR-40 | ST-3, ST-4, ST-5 |
| FR-41 | LB-16, LB-17 |
| FR-42 | WS-1, WS-3, WS-4, WS-5, WS-6, WS-7, WS-8 |
| FR-43 | — (in het LRD vervallen, samengevoegd met FR-42) |
| FR-44 | LB-1 |
| FR-45 | DM-12 |
| FR-46 | VB-1 |
| FR-47 | VB-2 |
| FR-48 | VB-3, VB-10 |
| FR-49 | VB-4 |
| FR-50 | VB-5, VB-6 |
| FR-51 | VB-7 |
| FR-52 | VB-8, WS-2 |
| FR-53 | BR-1, BR-2, BR-3 |
| FR-54 | BR-4, BR-5 |
| FR-55 | MD-1 |
| FR-56 | MD-2 |
| FR-57 | MD-4, MD-5, MD-6, MD-7 |
| FR-58 | MD-8, MD-9, MD-10, MD-11, MD-13 |
| FR-59 | DM-13 |
| FR-60 | SI-2, SI-3 |
| FR-61 | TK-15, TK-16, TK-17 |
| FR-62 | TP-1, TP-2, TP-3, TP-4, TP-5 |
| FR-63 | TP-6, TP-7, TP-8 |
| FR-64 | TP-9 |
| FR-65 | TP-10, DM-14 |
| FR-66 | ST-7 |
| FR-67 | TP-11 |

### Non-functionele requirements

| LRD | Blueprint |
|---|---|
| NFR-01 | SI-4 |
| NFR-02 | PR-1, PR-2, WS-9, DS-10 |
| NFR-03 | TG-1, TG-2, TG-3, TG-4, TG-5, MD-5, MD-9 |
| NFR-04 | PF-1 |
| NFR-05 | PF-2, DS-12 |
| NFR-06 | PF-3, PF-4, DM-15 |
| NFR-07 | PF-5, TK-14 |
| NFR-08 | QA-4 |
| NFR-09 | QA-2, QA-3, BW-8 |
| NFR-10 | DS-4, DL-4 |
| NFR-11 | QA-5 |
| NFR-12 | LI-1, LI-2, LI-3 |
| NFR-13 | QA-6 |
| NFR-14 | DM-16 |
| NFR-15 | DM-17 |
| NFR-16 | MD-4, MD-5, MD-6, MD-12, MD-13 |
| NFR-17 | BR-1, BR-6 |
| NFR-18 | SI-5, SI-6, SI-7, LI-4, LI-5 |

### Overige LRD-onderdelen

| LRD | Blueprint |
|---|---|
| Deel 1 (context, twee gebruiksvormen) | §1, §3 |
| Deel 2 (kaders) | §2 |
| Deel 3 (leeruitkomsten, dekking) | §4 |
| Deel 4 (doelgroep, voorkennis) | ST-1, TK-3, QA-4, QA-5 |
| Deel 5 (PAMS, KISS) | §2, §8 |
| Deel 6.1 (bewijsonderdelen EV-01–EV-11) | §6.7, ongewijzigde ID's |
| Deel 6.2–6.5 (record, controles, dossier, grens) | §3, §5, §6.5, §6.6, §6.8 |
| Deel 6.6 (leerroute) | TK-18 |
| Deel 6.1 en 6.3 (statusregel, controlesoorten, disclaimer bij Compleet) | BW-5, BW-6, BW-7, BW-9, BW-10, BW-11 |
| Deel 6.2 (bewijsrecord) | RC-1, RC-2, RC-3, RC-4 |
| Deel 6.7 en 8.2 (programma van woensdag, begintijden) | DM-10, DM-18 |
| Deel 6.9 en risico „vierde invulplaatje" (taak 9.4 zelfstandig, 20 min) | VB-9 |
| Deel 6.10 en 8.4 (tekst ≤ 300 woorden, fictieve bronkaarten) | MD-3, MD-15, MD-16 |
| Deel 12 (risico's: pilotbanner, klembord bij de Wissel, herinnering) | SI-8, WS-10, WS-11 |
| Deel 10 (deliverables 5, 6, 7) | DL-1, DL-2, DL-3 |
| Deel 6.7 (docentmodus) | §6.16 |
| Deel 6.8 (Wissel) | §6.9 |
| Deel 6.9 (verbanden) | §6.10 |
| Deel 6.10 (media) | §6.12 |
| Deel 6.11 (tussenpozen) | §6.11 |
| Deel 8 (programma, verdieping, media, terugblik) | §4.2; inhoud blijft bron in het LRD |
| Deel 9 (toetsing) | §3 („Wat het bewijs is"), X-14, DS-8 |
| Deel 10 (deliverables) | §7.4 |
| Deel 11 (AC-01–AC-44) | Bijlage B |
| Deel 12 (risico's) | — (risicolijst blijft in het LRD; mitigaties zijn regels hierboven) |
| Deel 13 (roadmap) | — (bouwvolgorde hoort in het bouwplan) |
| Besluitenregister (tot LRD 0.12 Bijlage A, B1–B60) | — (staat in `docs/ADR-ELEARNING-A3.md`; vervangen besluiten blijven daar staan; alle besluiten zijn in B58 bevestigd) |
| Bijlage B (bronnen, tot LRD 0.12) | §10; sinds LRD 0.13 heet die bijlage Bijlage A |

## Bijlage B — Acceptatiecriteria (LRD Deel 11) → verificatie

De acceptatiecriteria van het LRD zijn hier de verificatie van regels, geen aparte eisen.

| AC | Regels |
|---|---|
| AC-01 | PR-1, SI-1 |
| AC-02 | QA-3, BW-12 |
| AC-03 | AP-1 |
| AC-04 | DS-8 |
| AC-05 | QA-2 |
| AC-06 | TG-1, TG-2 |
| AC-07 | PF-1 |
| AC-08 | AP-2 |
| AC-09 | AP-3 |
| AC-10 | AP-5 |
| AC-11 | ST-6 |
| AC-12 | QA-1 |
| AC-13 | AP-9 |
| AC-14 | AP-4 |
| AC-15 | DM-16 |
| AC-16 | PR-3, PR-4 |
| AC-17 | DM-9 |
| AC-18 | DM-11 |
| AC-19 | TK-8, TK-9 |
| AC-20 | TK-5, TK-13 |
| AC-21 | ST-3, ST-5 |
| AC-22 | LB-16, TK-11 |
| AC-23 | WS-5, WS-7 |
| AC-24 | WS-6 |
| AC-25 | LB-1, DM-11, DM-12 |
| AC-26 | VB-3, VB-5, VB-6, VB-7 |
| AC-27 | VB-2, VB-4 |
| AC-28 | AP-6 |
| AC-29 | BR-1, BR-2, BR-5 |
| AC-30 | MD-1, MD-2 |
| AC-31 | MD-4, MD-5, MD-6, MD-12 |
| AC-32 | MD-9, MD-10 |
| AC-33 | DM-13 |
| AC-34 | AP-7 |
| AC-35 | SI-2, SI-3 |
| AC-36 | SI-6, SI-7 |
| AC-37 | TK-15, TK-16, TK-17 |
| AC-38 | TP-2, TP-3 |
| AC-39 | TP-6, TP-7, TP-8 |
| AC-40 | TP-9 |
| AC-41 | TP-10, DM-14 |
| AC-42 | AP-8 |
| AC-43 | ST-7 |
| AC-44 | TP-11 |
