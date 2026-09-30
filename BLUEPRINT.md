# BLUEPRINT — Hybride e-learning A3 met automatisch bewijs

> Afgeleid van `docs/lrd-elearning-a3.html` (LRD versie 0.12, 30 september 2026). Dit document beschrijft de doelsituatie van het product: geen bouwvolgorde, geen fasering, geen voortgang. Bouwvolgorde en voortgang staan in het bouwplan (`BUILDPLAN.md`). Pedagogische onderbouwing en risico's blijven in het LRD; het besluitenregister (B1–B59) staat in `docs/adr-elearning-a3.md`; regels hier verwijzen daar niet naartoe maar zijn zelfstandig toetsbaar. Bijlage A koppelt elke LRD-eis aan de regels hieronder.

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

Doeldekking: de 13 onderdelen leveren 5 gedekt, 7 deels en 2 buiten scope (de laatste twee rijen gelden als één rij per groep). Regel BW-13 toont deze tabel aan de student met de eigen status.

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
| <a id="si-5"></a>SI-5 | De repository moet alleen de site (HTML, CSS, JavaScript, datafiles, media), een README met verwijzing naar de docentgids, een `.nojekyll`-bestand, een `LICENSE`-bestand, de workflow en de tests bevatten. | Should | 0 bestanden buiten deze 8 categorieën | Inspectie |
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
| <a id="tk-17"></a>TK-17 | De site moet de student altijd laten doorgaan zonder een leerblok af te ronden. | Must | 0 blokkades bij een leerblok dat niet is afgerond | Test |
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
| <a id="ds-2"></a>DS-3-pre | — (nummer vervalt; zie DS-2 hieronder) | — | — | — |
