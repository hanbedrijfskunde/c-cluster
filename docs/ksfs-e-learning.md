# Kritische succesfactoren voor e-learningmodules en een auditinstrument voor het hbo

De belangrijkste succesfactor van een e-learningmodule is niet de techniek of het medium. Het gaat erom dat een module (1) uitgelijnd is op heldere leerdoelen, (2) studenten actief laat ophalen, oefenen en toepassen met informatieve feedback, en (3) de cognitieve belasting laag houdt via goed multimedia-ontwerp. Toegankelijkheid, begeleiding (teaching presence) en een verbetercyclus op basis van data zijn daarbij voorwaardelijk. Bestaande rubrics zoals Quality Matters en OSCQR dekken alignment, navigatie en toegankelijkheid goed af. Ze toetsen nauwelijks of een module de best onderbouwde leerstrategieën (retrieval practice, spacing, uitgewerkte voorbeelden) daadwerkelijk inzet, en ze zeggen weinig over generatieve AI. Een eigen auditinstrument voor de HAN kan daarom het best QM/OSCQR als basis nemen en drie lagen toevoegen: evidence-based leerstrategieën, AI-gebruik en -integriteit, en een expliciete scheiding tussen ontwerp, uitvoering en opbrengst.

## TL;DR

- **Kern-KSF's met het sterkste bewijs:** constructive alignment, retrieval practice en spaced practice, informatieve feedback, multimedia-ontwerp volgens Mayer en cognitive load theory, en zichtbare docentsturing (teaching presence). Technologie en ondersteuning zijn randvoorwaarden: ze hangen samen met tevredenheid en acceptatie, minder met leerwinst.
- **Auditinstrument:** 9 domeinen (A–I) met ongeveer 45 toetsbare criteria, elk gelabeld als *essentieel* of *aanvullend*. Scoring gebeurt op een 4-puntsschaal (onvoldoende / basis / goed / excellent). Bewijs komt uit documentanalyse, een walkthrough als student, LMS-data en studentevaluaties, apart gerapporteerd voor input, proces en output.
- **Positie:** gebruik QM (7e editie) of OSCQR als "hygiëne-laag". Voeg criteria toe voor leerstrategieën, AI-guardrails en privacy/AI-verordening. Behandel de audit als ontwikkelgesprek in lijn met NVAO-standaard 2 en 3, niet als afvinklijst: compliance is geen bewijs van leereffectiviteit.

## Key Findings

### Overzicht van de KSF's en de sterkte van het bewijs

| # | Kritische succesfactor | Kern van het bewijs | Sterkte van bewijs |
|---|---|---|---|
| 1 | **Constructive alignment** (doelen, activiteiten en toetsing sluiten op elkaar aan) | Biggs; kern van QM ("alignment"-standaarden), OSCQR, NVAO-standaarden 1–3 | Consensus in kaders; empirisch indirect onderbouwd |
| 2 | **Retrieval practice (oefentoetsen)** | Adesope et al. (2017): 272 vergelijkingen, 15.427 deelnemers; g ≈ 0,51 t.o.v. herlezen, hoger t.o.v. andere controlecondities; klas- en labeffecten vergelijkbaar (0,67 vs 0,62)\[1\]\[2\]\[3\] | Sterk empirisch |
| 3 | **Spaced practice (spreiding)** | Cepeda et al. (2006): 839 metingen in 317 experimenten uit 184 artikelen;\[4\] Latimier et al. (2021): gespreide vs. geblokte retrieval g = 0,74\[5\] | Sterk empirisch |
| 4 | **Informatieve feedback** | Wisniewski, Zierer & Hattie (2020): 435 studies, 994 effecten, >61.000 lerenden; gemiddeld d = 0,48, sterke heterogeniteit; high-information feedback veel effectiever dan lof of cijfers\[6\]\[7\]\[8\] | Sterk empirisch (maar sterk afhankelijk van type) |
| 5 | **Multimedia-ontwerp / cognitieve belasting** (coherentie, signalering, segmentering, contiguïteit) | Mayer (2017) mediane effecten o.a. coherentie d = 0,70, signalering 0,46, segmentering 0,70; onafhankelijke meta-analyses lager: signalering d = 0,38 (Alpizar, Adesope & Wong, 2020, *ETR&D*) en segmentering d = 0,36 (Rey et al., 2019, *Educational Psychology Review*; 56 onderzoeken, 88 vergelijkingen); Cromley & Chen (2025): 591 effecten uit Mayers eigen werk, gemiddeld g = 0,37, dalend over de jaren | Sterk empirisch, met kleinere effecten dan vaak geciteerd |
| 6 | **Actieve/constructieve verwerking** (ICAP; Merrill's First Principles) | Chi & Wylie (2014): hypothese I > C > A > P; latere toetsing in technologie-rijk hoger onderwijs bevestigde de rangorde niet eenduidig\[9\]\[10\] | Plausibel en breed gedragen; beperkt direct bewijs |
| 7 | **Teaching presence en begeleiding** (CoI) | Martin et al. (2022), meta-analyse van 19 studies: teaching presence–werkelijk leren r = 0,353; cognitive presence r = 0,250; social presence r = 0,199; sterkere verbanden met *ervaren* leren en tevredenheid\[11\] | Matig empirisch (correlationeel, veel zelfrapportage) |
| 8 | **Bruikbaarheid, techniek en ondersteuning** | Selim (2007): vier CSF-categorieën (docent, student, IT-infrastructuur, universitaire ondersteuning); Sun et al. (2008): computerangst, docentattitude, flexibiliteit, cursuskwaliteit, ervaren nut, gebruiksgemak en diversiteit in toetsing voorspellen tevredenheid\[12\]\[13\]\[14\]\[15\] | Matig empirisch (acceptatie/tevredenheid, niet leerwinst) |
| 9 | **Toegankelijkheid en inclusie** | Wettelijk verplicht (Bdto/WCAG 2.1 AA); UDL 3.0 (CAST, juli 2024); QM 8.3–8.5\[16\]\[17\]\[18\] | Wettelijke norm + consensus; leereffect UDL beperkt onderzocht |
| 10 | **Evaluatie en datagedreven verbetering** | OSCQR-standaard 50; E-xcellence; NVAO-standaard 6 (kwaliteitszorg); DeLone & McLean ("net benefits")\[19\]\[20\] | Consensus in kaders |
| 11 | **Verantwoord AI-gebruik (guardrails, integriteit)** | Bastani et al. (2025, PNAS): ongeremde GPT verbetert oefenprestatie maar schaadt leren zodra toegang wegvalt; tutor met guardrails mitigeert dit. Kestin et al. (2025, Sci Rep, N = 194): zorgvuldig ontworpen AI-tutor gaf hogere leerwinst dan actief-leren-college in minder tijd\[21\]\[22\]\[23\]\[24\] | Opkomend; enkele sterke RCT's, context-specifiek |

### Wat de data betekenen

- **Het medium is niet de factor.** De meta-analyse van Means, Toyama, Murphy & Bakia (2013, *Teachers College Record* 115(3); 50 effecten uit 45 studies) vond een gemiddeld effect van +0,20 over alle 50 contrasten in het voordeel van online condities. Het voordeel kwam vooral uit blended-opzetten (g+ = +0,35 t.o.v. face-to-face); de 27 volledig online contrasten waren niet significant. Blended-opzetten bevatten ook vaak meer leertijd en extra didactiek. Een auditinstrument moet dus het ontwerp beoordelen, niet de vraag "online of niet".
- **Tevredenheid is geen leerwinst.** De klassieke CSF-studies (Selim, Sun et al.) en veel CoI-onderzoek meten acceptatie, tevredenheid of *ervaren* leren. In Martin et al. (2022) correleert cognitive presence sterk met ervaren leren (r = 0,663), maar zwak met werkelijk leren (r = 0,250).\[11\] Studentevaluaties zijn daarom nuttig als procesindicator, maar mogen niet als outcome-bewijs gelden.
- **De grootste winst zit in wat rubrics nauwelijks toetsen.** Retrieval practice, spacing en informatieve feedback hebben het robuustste bewijs. QM en OSCQR vragen wel naar "variatie in toetsing" en "zelftoetsen" (OSCQR 47), maar niet of oefenmomenten gespreid, cumulatief en met uitgewerkte feedback zijn ingericht.\[25\]
- **AI is een ontwerpvariabele, geen neutraal hulpmiddel.** Dezelfde technologie kan leren versterken (Kestin) of ondermijnen (Bastani), afhankelijk van guardrails.\[22\]\[24\] Het auditcriterium is dus niet "wordt AI gebruikt?", maar "dwingt het ontwerp denkwerk af en is het leerdoel beschermd?".

## Details

### 1. Onderbouwing per cluster van succesfactoren

**Didactisch ontwerp en alignment.** Constructive alignment (Biggs) is de ruggengraat van vrijwel elk kwaliteitskader. In QM zijn de alignment-standaarden (leerdoelen, toetsing, materialen, activiteiten, technologie) als essentieel gemarkeerd.\[26\] Merrill's First Principles zijn probleemgericht werken, activeren van voorkennis, demonstreren, toepassen en integreren. Ze vertalen dit naar een ontwerpvolgorde die goed past bij hbo-bedrijfskunde (casusgestuurd). Voor de Nederlandse context sluit dit direct aan op het NVAO-beoordelingskader 2024 (Staatscourant 2024, 6405; door NVAO toegepast vanaf 1 april 2024).\[27\]\[28\] Standaard 2 luidt: "Het programma, de onderwijsleeromgeving en de kwaliteit van het docententeam maken het voor de instromende studenten mogelijk de beoogde leerresultaten te realiseren."\[19\] Een module-audit levert zo direct bewijs voor opleidingsaccreditatie.

**Cognitieve belasting en multimedia.** Mayer (2017) rapporteert mediane effecten voor principes die extrinsieke belasting verminderen: coherentie d = 0,70, signalering 0,46, redundantie 0,87, ruimtelijke contiguïteit 0,79 en temporele contiguïteit 1,30. Voor het managen van essentiële belasting: segmentering 0,70, pre-training 0,46 en modaliteit 0,72.\[29\] Onafhankelijke meta-analyses vinden kleinere maar reële effecten: signalering d = 0,38 (Alpizar, Adesope & Wong, 2020) en segmentering d = 0,36 (Rey et al., 2019). De meta-analyse van Cromley & Chen (2025) over Mayers eigen corpus (92 artikelen, 181 studies, 591 effecten) komt uit op gemiddeld g = 0,37, met een lichte daling per publicatiejaar.\[30\]\[31\] Conclusie: de principes zijn betrouwbaar als ontwerpregels, maar verwacht geen wonderen. Grenscondities zoals het expertise-reversal-effect betekenen dat gevorderde studenten minder baat hebben bij sterke sturing.

**Oefenen, ophalen en spreiden.** Adesope et al. (2017) is de referentie-meta-analyse voor practice testing. De effectgrootte t.o.v. herlezen (g ≈ 0,51) is volgens de auteurs de meest realistische schatting voor de onderwijspraktijk.\[3\] De effecten gelden over alle onderwijsniveaus, en klas- en labstudies verschillen weinig.\[2\]\[3\] Spreiding versterkt dit: Latimier et al. (2021) vinden voor gespreide versus geblokte retrieval g = 0,74.\[5\] Het Cepeda-corpus laat zien dat het optimale interval meegroeit met de gewenste retentieduur.\[32\] Belangrijke kanttekening: het testing-effect kan afnemen bij zeer complexe leerstof (Van Gog & Sweller, 2015).\[2\] Voor bedrijfskundige transfer-taken moeten oefenvragen dus ook toepassing vragen, niet alleen reproductie.

**Feedback.** Wisniewski et al. (2020) corrigeren de hoge effecten uit eerdere Hattie-syntheses (0,70–0,79) naar d = 0,48.\[33\]\[34\] Ze laten vooral zien dat het *informatiegehalte* doorslaggevend is: feedback met taak-, proces- en zelfregulatie-informatie werkt veel beter dan "goed gedaan" of een cijfer.\[6\]\[33\] Het Hattie & Timperley-model (feed up / feed back / feed forward op taak-, proces- en zelfregulatieniveau) is daarom het logische auditkader.

**Activering en interactie.** ICAP (Chi & Wylie, 2014) is een bruikbare taal om opdrachten te classificeren: passief (kijken), actief (markeren, klikken), constructief (zelf genereren, uitleggen) en interactief (co-constructie).\[35\]\[36\] Het directe bewijs voor de strikte rangorde in online hoger onderwijs is gemengd.\[9\] Gebruik ICAP daarom als diagnose-instrument ("hoeveel van de leertijd is minstens constructief?"), niet als harde norm.

**Begeleiding en sociale aanwezigheid.** In het CoI-model is teaching presence (ontwerp, facilitatie, directe instructie) de presence met het sterkste verband met werkelijk leren (r = 0,353 in Martin et al., 2022).\[11\] Voor asynchrone zelfstudiemodules betekent dit: ook zonder live docent moet zichtbaar zijn wie de module stuurt, wanneer er gereageerd wordt en waar studenten terechtkunnen.

**Succesmodellen en randvoorwaarden.** Selim (2007, *Computers & Education* 49(2)) onderscheidt vier CSF-categorieën: docent, student, informatietechnologie en universitaire ondersteuning.\[13\]\[37\] Sun et al. (2008, *Computers & Education* 50(4)) toetsten een model met zes dimensies (lerende, docent, cursus, technologie, ontwerp, omgeving). Kritisch voor tevredenheid bleken computerangst, docentattitude, flexibiliteit, cursuskwaliteit, ervaren nut, ervaren gebruiksgemak en diversiteit in toetsing.\[12\]\[15\] Het DeLone & McLean-model (systeem-, informatie- en servicekwaliteit → gebruik/tevredenheid → netto-opbrengst) geeft hier een logische structuur voor: ontwerp- en systeemkwaliteit zijn input, gebruik en tevredenheid zijn proces, en leerresultaat is output.

**Toegankelijkheid: wat is juridisch écht verplicht?** Er circuleert veel verwarring rond de Europese Toegankelijkheidswet (EAA, van toepassing sinds 28 juni 2025).\[38\] Voor bekostigde hogescholen zoals de HAN geldt de verplichting primair via het Besluit digitale toegankelijkheid overheid: websites en apps (inclusief leeromgevingen) moeten voldoen aan WCAG 2.1 niveau A en AA (via EN 301 549), met een gepubliceerde toegankelijkheidsverklaring.\[18\]\[39\] BNNVARA Kassa (24 januari 2026) stelt: "Maar in Nederland vallen onderwijs en zorg buiten deze wet." Tweede Kamerlid Don Ceder (ChristenUnie) diende in november 2024 een motie in om de EAA ook voor onderwijs en zorg te laten gelden. De EAA raakt de HAN vooral indirect: commerciële leveranciers van LMS'en, e-books en tools moeten wél voldoen, en dat is een inkoopcriterium.\[40\] Commerciële adviesbureaus spreken elkaar hierover tegen: Proper Access schrijft "valt jouw instelling onder de EAA? Kort antwoord: waarschijnlijk wel", terwijl Cardan op dezelfde vraag antwoordt: "Het antwoord is: nee!" Behandel WCAG 2.1 AA daarom als wettelijke ondergrens en WCAG 2.2 AA als best practice. ETSI/CEN/CENELEC hebben in september 2026 EN 301 549 V4.1.1 gepubliceerd, gebaseerd op WCAG 2.2. Volgens een secundaire bron (sitebrunch, 7 september 2026, met verwijzing naar AccessibleEU) blijft WCAG 2.1 AA de toepasselijke norm totdat V4.1.1 in het Publicatieblad van de EU is aangehaald. Daarnaast vraagt NVAO-standaard 2 expliciet dat "de inrichting van de leeromgeving (...) de toegankelijkheid en studeerbaarheid van het onderwijs [bevordert], mede voor studenten met een functiebeperking".\[41\] UDL 3.0 (CAST, 30 juli 2024) verschuift het doel van "expert learners" naar "learner agency" en legt meer nadruk op identiteit, belonging en systemische barrières.\[42\]\[43\] UDL is een ontwerpkader. Het leereffect is minder hard onderzocht dan WCAG-conformiteit, dus scoor het als aanvullend.

**Generatieve AI.** Twee RCT's markeren de bandbreedte:
- Bastani et al. (2025, PNAS) gaven scholieren een standaard GPT-4-interface of een "GPT Tutor" met leerbeschermende prompts.\[22\] Beide verbeterden de prestatie tijdens het oefenen (+48% resp. +127%).\[44\] Toen de toegang wegviel, presteerden GPT Base-gebruikers slechter dan de controlegroep. Dat negatieve effect werd door de guardrails (hints in plaats van antwoorden) grotendeels opgevangen.\[23\]\[45\]
- Kestin et al. (2025, *Scientific Reports*; N = 194, Harvard-natuurkunde) lieten een tutor zien die volgens actief-leren-principes was ontworpen.\[24\] De mediane posttest-score was 4,5 tegen 3,5 in het actief-leren-college (pretest 2,75), in minder tijd.\[46\]

Beide studies zijn context-specifiek (wiskunde op de middelbare school; gestructureerde natuurkunde) en niet zonder meer te generaliseren naar open bedrijfskundige vraagstukken.

**Regelgeving AI.** De AI-verordening (EU 2024/1689) classificeert in Bijlage III punt 3 AI-systemen als hoog-risico wanneer ze leerresultaten evalueren (ook om het leerproces te sturen), het onderwijsniveau bepalen, toelating regelen of verboden gedrag tijdens toetsen detecteren (proctoring).\[47\] Via de Digital Omnibus on AI zijn de data aangepast:
- Voorlopig akkoord op 7 mei 2026.\[48\]\[49\]
- Door de Raad definitief goedgekeurd op 29 juni 2026.\[50\]
- Gepubliceerd als Verordening (EU) 2026/1744 op 24 juli 2026, in werking sinds 27 juli 2026.\[51\]

De hoog-risicoverplichtingen voor zelfstandige Bijlage III-systemen gelden nu vanaf **2 december 2027**, in plaats van 2 augustus 2026.\[52\]\[53\] De verplichtingen zelf zijn niet afgezwakt, waaronder de fundamental rights impact assessment (FRIA) voor bepaalde gebruiksverantwoordelijken.\[48\]\[54\] Voor een module betekent dit: een AI-tutor die alleen hints geeft valt doorgaans niet onder hoog-risico, maar AI die cijfers geeft, feedback koppelt aan beoordeling of proctoring uitvoert wel. Dat moet in de audit zichtbaar worden. Parallel geldt de AVG voor learning analytics: doelbinding, dataminimalisatie, transparantie naar studenten en een DPIA bij grootschalige of risicovolle verwerking.

### 2. Structuur van het auditinstrument

**Scoringsschaal (voor alle criteria):**

| Score | Label | Betekenis |
|---|---|---|
| 0 | Onvoldoende | Niet aanwezig, of aanwezig maar werkt tegen het leerdoel |
| 1 | Basis | Aanwezig maar inconsistent, of alleen op onderdelen |
| 2 | Goed | Consistent aanwezig in de hele module; aantoonbaar in bewijs |
| 3 | Excellent | Goed, plús onderbouwd met data of evaluatie en aantoonbaar verbeterd |

**Beslisregel (naar analogie van QM):** een module "voldoet" als alle essentiële criteria (E) minimaal score 2 halen en het gemiddelde over alle criteria ≥ 1,8 is. Aanvullende criteria (A) sturen de ontwikkelagenda. QM hanteert iets vergelijkbaars: alle 22 essentiële standaarden (3 punten) moeten gehaald zijn en minimaal 86 van de 101 punten (85%).\[26\]

**Laag-label per criterium:** I = input/ontwerp, P = proces/uitvoering, O = output/opbrengst.

#### Domein A – Didactisch ontwerp en alignment

| ID | Criterium (toetsbaar) | Waar kijkt de auditor naar? | Prio | Laag | Bron |
|---|---|---|---|---|---|
| A1 | Zijn de leerdoelen van de module geformuleerd als observeerbaar, meetbaar gedrag, op het juiste (hbo-)niveau? | Moduleoverzicht, studiehandleiding; werkwoorden (Bloom), niveau t.o.v. leeruitkomsten van de opleiding | E | I | QM 2.1–2.2; NVAO std. 1 |
| A2 | Is voor elk leerdoel aantoonbaar welke activiteit(en) en welke toets(en) eraan bijdragen? | Alignmentmatrix (leerdoel × activiteit × toets); ontbreekt die, dan reconstrueert de auditor hem | E | I | Biggs; QM alignment-standaarden |
| A3 | Is de moduleopbouw probleem- of taakgericht (authentieke bedrijfskundige casus als ankerpunt)? | Opbouw van de units; aanwezigheid van casus/probleem vóór theorie | A | I | Merrill (task-centered) |
| A4 | Wordt voorkennis expliciet geactiveerd of gediagnosticeerd aan het begin? | Voortoets, instapvragen, "wat weet je al"-activiteit | A | I | Merrill (activation); QM 1.7 |
| A5 | Is de verwachte studielast per onderdeel vermeld en realistisch (steekproef)? | Tijdsindicaties; vergelijking met LMS-tijdsdata of studentfeedback | E | I/P | NVAO std. 2 (studeerbaarheid); OSCQR |
| A6 | Zijn start, doel, structuur en verwachtingen direct duidelijk bij binnenkomst? | Welkomst-/startpagina, "begin hier", overzicht | E | I | QM 1.1–1.2; OSCQR 1 |

#### Domein B – Inhoud en multimedia

| ID | Criterium | Waar kijkt de auditor naar? | Prio | Laag | Bron |
|---|---|---|---|---|---|
| B1 | Is de inhoud actueel, correct en relevant voor het beroepenveld (herkomst en datum zichtbaar)? | Bronvermelding, publicatiedatum, vakinhoudelijke check door peer | E | I | QM 4; E-xcellence |
| B2 | Bevatten video's en pagina's geen decoratieve, afleidende elementen (achtergrondmuziek, irrelevante plaatjes, "leuke weetjes")? | Steekproef van ≥ 3 video's en ≥ 5 pagina's | E | I | Mayer: coherentie |
| B3 | Worden kernbegrippen en structuur gesignaleerd (koppen, markering, visuele cues)? | Opmaak van pagina's en slides | A | I | Mayer: signalering |
| B4 | Zijn video's gesegmenteerd (richtlijn ≤ ca. 6–10 min per concept) en door de student te pauzeren of navigeren? | Videolengtes, hoofdstukmarkeringen | E | I | Mayer: segmentering; CLT |
| B5 | Staan tekst en bijbehorende afbeelding of uitleg bij elkaar, en wordt gesproken uitleg niet letterlijk als tekst herhaald? | Diagrammen met labels; narratie vs. schermtekst | A | I | Mayer: contiguïteit, redundantie |
| B6 | Worden bij nieuwe, complexe procedures uitgewerkte voorbeelden gebruikt, afgebouwd naar zelfstandige opgaven? | Worked examples → faded examples → oefenopgaven | A | I | CLT (worked-example-effect) |
| B7 | Is de licentie of het auteursrecht van materiaal van derden in orde? | Licentievermelding, open licenties | E | I | QM 4.4 (7e ed.) |

#### Domein C – Activering en interactie

| ID | Criterium | Waar kijkt de auditor naar? | Prio | Laag | Bron |
|---|---|---|---|---|---|
| C1 | Is minimaal de helft van de geplande leertijd constructief of interactief (studenten genereren iets: uitleg, analyse, ontwerp)? | ICAP-codering van alle activiteiten, gewogen naar tijd | E | I | ICAP; QM 5.1 |
| C2 | Volgt na elke instructie-eenheid een toepassingsopdracht met feedback? | Ritme instructie → toepassing | E | I | Merrill (application) |
| C3 | Zijn er geplande momenten voor student-student-interactie (peer feedback, discussie, groepsopdracht) die inhoudelijk nodig zijn? | Forum-/peeropdrachten; zijn ze functioneel of alleen "post één bericht"? | A | I/P | CoI social presence; OSCQR 42 |
| C4 | Wordt de student gevraagd de leerstof te integreren of naar de eigen (werk)praktijk te vertalen (reflectie, transfer)? | Reflectie- en transferopdrachten | A | I | Merrill (integration) |
| C5 | Is de interactie in de praktijk ook daadwerkelijk ontstaan (deelname, diepgang)? | Forumdata, steekproef posts | A | P | CoI |

#### Domein D – Toetsing, oefenen en feedback

| ID | Criterium | Waar kijkt de auditor naar? | Prio | Laag | Bron |
|---|---|---|---|---|---|
| D1 | Bevat elke unit laagdrempelige oefentoetsen (retrieval practice) die studenten meerdere keren kunnen maken? | Quizzen, zelftoetsen, flashcards in het LMS | E | I | Adesope et al. 2017; OSCQR 47 |
| D2 | Komen eerdere leerstofonderdelen gespreid terug (cumulatieve of interleaved oefenvragen in latere units)? | Vraagbanken; komt stof uit week 1 terug in week 3+? | E | I | Cepeda 2006; Latimier 2021 |
| D3 | Gaan oefenvragen verder dan reproductie (toepassing/transfer bij bedrijfskundige casuïstiek)? | Vraagtypen, niveau t.o.v. leerdoel | E | I | Adesope (transfer); Van Gog & Sweller |
| D4 | Geeft de feedback taak- én procesinformatie (waarom fout, hoe verder = feed forward), niet alleen goed/fout of een score? | Feedbackteksten bij quizvragen; steekproef docentfeedback | E | I/P | Hattie & Timperley 2007; Wisniewski et al. 2020 |
| D5 | Zijn beoordelingscriteria (rubric, voorbeelden van goed werk) vooraf beschikbaar en gekoppeld aan de leerdoelen? | Rubrics, exemplars | E | I | QM 3.3; OSCQR 46; NVAO std. 3 |
| D6 | Is de summatieve toets valide (dekt de leerdoelen), betrouwbaar en voorzien van een toetsmatrijs? | Toetsmatrijs, beoordelingsmodel, tweede beoordelaar | E | I | NVAO std. 3; toetsbeleid |
| D7 | Wordt feedback tijdig gegeven (termijn gecommuniceerd en gehaald)? | Aangekondigde termijn vs. LMS-tijdstempels | E | P | QM 3.5; Sun et al. 2008 |
| D8 | Is de toets bestand tegen ongeautoriseerd AI-gebruik, of is AI-gebruik juist bewust toegestaan en geëxpliciteerd per opdracht? | Opdrachtontwerp (proces, mondelinge component, eigen data), AI-richtlijn per opdracht | E | I | QM 3.6 (7e ed., integriteit) |

#### Domein E – Begeleiding en sociale aanwezigheid

| ID | Criterium | Waar kijkt de auditor naar? | Prio | Laag | Bron |
|---|---|---|---|---|---|
| E1 | Is duidelijk wie de docent of begeleider is, hoe en wanneer die bereikbaar is en binnen welke termijn er gereageerd wordt? | Contactpagina, communicatieafspraken | E | I | QM 1.3, 1.8, 5.3; CoI teaching presence |
| E2 | Is de docent zichtbaar aanwezig tijdens de uitvoering (aankondigingen, samenvattingen, reactie op misconcepties)? | Aankondigingen, forumreacties, video-updates | E | P | CoI teaching presence (Martin et al. 2022) |
| E3 | Zijn er signalen en acties voor studenten die achterblijven (nudges, check-ins)? | Intelligent agents/release conditions in Brightspace, opvolging | A | P | Drop-out-onderzoek; learning analytics |
| E4 | Is er een laagdrempelige plek voor vragen (Q&A-forum, spreekuur) en wordt die gebruikt? | Forum, gebruiksdata | A | I/P | OSCQR interactie |

#### Domein F – Navigatie, gebruiksvriendelijkheid en techniek

| ID | Criterium | Waar kijkt de auditor naar? | Prio | Laag | Bron |
|---|---|---|---|---|---|
| F1 | Is de navigatie consistent en logisch, en kan een student elk onderdeel binnen 3 klikken vinden? | Walkthrough als student (taakgerichte test) | E | I | QM 8.1; Sun et al. (gebruiksgemak) |
| F2 | Werken alle links, embeds en tools (geen dode links, geen ontbrekende rechten)? | Linkchecker, walkthrough | E | I | QM 6; OSCQR tech |
| F3 | Zijn technische vereisten en ondersteuning (helpdesk) vermeld? | Startinformatie | E | I | QM 1.5, 7.1 |
| F4 | Is de module bruikbaar op mobiel en laptop (responsive, geen afhankelijkheid van één apparaat)? | Test op smartphone | A | I | OSCQR design |
| F5 | Is het aantal verschillende externe tools beperkt en functioneel verantwoord? | Toolinventaris vs. leerdoel | A | I | QM 6.1; Selim (IT) |

#### Domein G – Toegankelijkheid en inclusie

| ID | Criterium | Waar kijkt de auditor naar? | Prio | Laag | Bron |
|---|---|---|---|---|---|
| G1 | Hebben alle video's correcte ondertiteling (niet alleen automatisch, maar gecontroleerd) en waar nodig een transcript? | Steekproef video's | E | I | WCAG 2.1/2.2 AA; QM 8.5 |
| G2 | Hebben informatieve afbeeldingen alt-tekst en zijn decoratieve afbeeldingen als zodanig gemarkeerd? | Toegankelijkheidscheck (Brightspace Accessibility Checker, WAVE/axe) | E | I | WCAG; QM 8.4 |
| G3 | Zijn documenten (PDF/Word/PPT) toegankelijk: koppenstructuur, leesvolgorde, voldoende contrast? | Steekproef documenten, contrastcheck | E | I | WCAG; QM 8.3 |
| G4 | Is de module volledig met toetsenbord te bedienen, inclusief quizzen en interactieve elementen (H5P e.d.)? | Toetsenbordtest | E | I | WCAG 2.1 AA (Bdto) |
| G5 | Biedt de module keuze in representatie of expressie (bv. tekst én audio; keuze in opdrachtvorm) waar dat het leerdoel niet ondermijnt? | Alternatieven per onderdeel | A | I | UDL 3.0 |
| G6 | Zijn voorbeelden en casussen divers en vrij van stereotypering? | Inhoudsanalyse casussen | A | I | UDL 3.0 (richtlijn 7.4 e.a.); QM 7e ed. |
| G7 | Voldoen ingekochte tools en content aantoonbaar aan WCAG/EN 301 549 (conformiteitsverklaring of VPAT van de leverancier)? | Leveranciersdocumentatie | A | I | Bdto; EAA (leveranciers) |

#### Domein H – Evaluatie, data en continue verbetering

| ID | Criterium | Waar kijkt de auditor naar? | Prio | Laag | Bron |
|---|---|---|---|---|---|
| H1 | Kunnen studenten tijdens en na de module gestructureerd feedback geven over ontwerp, inhoud en techniek? | Tussentijdse "how's it going"-peiling, eindevaluatie | E | P | OSCQR 50 |
| H2 | Worden LMS-data (voortgang, uitval per onderdeel, quizitem-analyse, tijdsbesteding) periodiek geanalyseerd? | Analyse-rapport, itemanalyse | E | P | Learning analytics; E-xcellence |
| H3 | Is er een gedocumenteerde verbetercyclus: welke wijzigingen zijn doorgevoerd op basis van evaluatie of data? | Logboek of versiebeheer van de module | E | P | NVAO std. 6; PDCA |
| H4 | Wordt leeropbrengst gemeten tegen de leerdoelen (toetsresultaten per leerdoel, pre/post of vergelijking met eerdere cohorten)? | Resultaatanalyse per leerdoel | E | O | NVAO std. 4; DeLone & McLean "net benefits" |
| H5 | Wordt onderscheid gemaakt tussen tevredenheid, ervaren leren en werkelijk leren in de rapportage? | Evaluatierapport | A | O | Martin et al. 2022 |

#### Domein I – AI-gebruik, privacy en integriteit

| ID | Criterium | Waar kijkt de auditor naar? | Prio | Laag | Bron |
|---|---|---|---|---|---|
| I1 | Is per opdracht expliciet vermeld of en hoe generatieve AI gebruikt mag worden, inclusief verantwoording (bijv. AI-logboek of verantwoordingsparagraaf)? | Opdrachtomschrijvingen; aansluiting bij HAN-/opleidingsbeleid | E | I | QM 3.6; toetsbeleid |
| I2 | Als er een AI-tutor of -assistent in de module zit: is die zo ingericht dat hij hints en vragen geeft in plaats van eindantwoorden (guardrails), en is dat getest? | Systeemprompt/configuratie, testprotocol met voorbeeld-dialogen | E | I | Bastani et al. 2025; Kestin et al. 2025 |
| I3 | Is de AI-feedback inhoudelijk gecontroleerd op juistheid (steekproef) en is voor studenten duidelijk dat het AI-output betreft? | Steekproef van ≥ 20 AI-feedbackitems; transparantiemelding | E | P | AI-verordening (transparantie); Bastani (foutpercentages GPT) |
| I4 | Wordt AI níet autonoom ingezet voor beoordeling, niveaubepaling of proctoring, of, als dat wel zo is, is het behandeld als hoog-risicosysteem (menselijk toezicht, documentatie, FRIA vóór 2 december 2027)? | Toepassingsinventaris; juridische toets | E | I | AI-verordening Bijlage III punt 3; Verordening (EU) 2026/1744 |
| I5 | Is voor learning analytics en AI-tools vastgelegd welke persoonsgegevens worden verwerkt, met welk doel, en is een verwerkersovereenkomst/DPIA aanwezig waar nodig? | Privacydocumentatie, verwerkersovereenkomst, DPIA | E | I | AVG art. 5, 28, 35 |
| I6 | Worden studenten geïnformeerd over welke data over hen worden verzameld en hoe die worden gebruikt (inclusief nudges)? | Privacyverklaring in de module | E | I | AVG transparantie |
| I7 | Oefenen studenten met kritisch AI-gebruik als leerdoel (bijv. AI-output beoordelen of verbeteren), waar passend bij de opleiding? | Opdrachten gericht op AI-geletterdheid | A | I | AI-verordening art. 4 (AI-geletterdheid) |

### 3. Praktische uitvoering van de audit

**Vier bewijsbronnen, gekoppeld aan de drie lagen:**

| Methode | Wat levert het op | Vooral voor | Tijdsindicatie per module |
|---|---|---|---|
| **Documentanalyse** (studiehandleiding, alignmentmatrix, toetsmatrijs, rubrics, privacy-/AI-documentatie) | Ontwerpintentie en alignment | Input (A, D, I) | 1–2 uur |
| **Walkthrough als student** (in een studentenview, inclusief quizzen maken, mobiel en toetsenbord testen, toegankelijkheidscheckers) | Werkelijke gebruikerservaring, cognitieve belasting, toegankelijkheid | Input (B, C, F, G) | 2–3 uur |
| **Data-analyse** (Brightspace-voortgang, uitval per onderdeel, quizitem-analyse, feedbacktermijnen, forumactiviteit) | Of het ontwerp in de praktijk werkt | Proces (C5, D7, E2, H2) | 1–2 uur |
| **Studentevaluaties + kort panelgesprek of focusgroep** (5–8 studenten) | Ervaren studielast, duidelijkheid, begeleiding | Proces; ervaren opbrengst | 1–2 uur |
| **Resultaatanalyse** (toetsresultaten per leerdoel, cohortvergelijking) | Leeropbrengst | Output (H4) | 1 uur |

**Aanbevolen werkwijze (vier stappen):**
1. **Zelfevaluatie** door de moduleeigenaar met hetzelfde instrument (zoals bij OSCQR en E-xcellence, die met een self-assessment of quickscan starten).\[55\]\[56\]
2. **Peer-audit** door twee reviewers: één vakdidacticus en één collega van buiten de module. Minimaal één reviewer heeft toetsexpertise; hier ligt een natuurlijke rol voor de toetscommissie bij domein D en I.
3. **Kalibratiegesprek:** reviewers vergelijken scores per criterium. Bij verschil ≥ 2 punten volgt een discussie en worden bewijsstukken vastgelegd.
4. **Ontwikkelrapport** met maximaal 5 prioritaire verbeteracties, en een herbeoordeling na één uitvoering. Excellent (3) is alleen haalbaar na een doorlopen verbetercyclus.

**Input – proces – output expliciet scheiden.** Rapporteer drie deelscores in plaats van één totaalscore:
- *Ontwerpkwaliteit (I):* kan deze module in principe goed werken?
- *Uitvoeringskwaliteit (P):* wordt het ontwerp zo uitgevoerd en gebruikt als bedoeld (docentaanwezigheid, feedbacktermijnen, gebruik van oefentoetsen)?
- *Opbrengst (O):* halen studenten de leerdoelen, en beter dan eerdere cohorten of een vergelijkbare module?

Een module met hoge I- maar lage P-score heeft een implementatieprobleem, geen ontwerpprobleem. Een module met hoge I en P maar lage O is een signaal dat het ontwerp of de toets niet valide is. Dat onderscheid is de kern van een audit die tot verbetering leidt.

### 4. Vergelijking van bestaande rubrics

| Kader | Niveau / doel | Omvang en scoring | Sterk in | Mist of zwak in |
|---|---|---|---|---|
| **Quality Matters HE Rubric, 7e ed. (juli 2023)** | Cursusontwerp; peer review met certificering | 8 General Standards, 44 Specific Review Standards, 101 punten; 22 essentiële standaarden; certificering bij alle essentiële + ≥ 86 punten (85%)\[26\] | Alignment; oriëntatie; toegankelijkheid (7e ed. splitst tekst-, beeld- en AV-toegankelijkheid in aparte standaarden 8.3–8.5); nieuwe standaard 3.6 over academische integriteit; inclusief en "welcoming" ontwerp\[57\]\[58\]\[59\] | Alleen ontwerp (input), niet uitvoering of opbrengst; geen expliciete eisen aan spreiding of retrieval; AI alleen indirect via integriteit; licentie- en betaalmodel; Amerikaanse context |
| **OSCQR (SUNY; ook OLC Quality Scorecard voor cursusontwerp)** | Formatieve "review & refresh", expliciet niet-evaluatief\[60\]\[61\] | 6 categorieën, 50 standaarden; open gelicentieerd, aanpasbaar\[60\]\[62\] | Brede dekking incl. technologie en toegankelijkheid; zelftoetsen (47), gradebook (49), studentfeedback (50); gratis en aanpasbaar\[25\]\[62\] | Weinig differentiatie in prioriteit; ook hier weinig over spacing, feedbackkwaliteit of AI; ontwerpgericht |
| **E-xcellence (EADTU), 3e ed. 2016** | Programma en instelling (strategie, curriculum, cursusontwerp, levering, studenten- en staf-ondersteuning) | 35 benchmarks met indicatoren; quickscan + externe review; label\[56\]\[63\] | Europese context; koppelt aan instellingsbeleid en kwaliteitszorg; bruikbaar naast NVAO | Te grof voor module-audit; dateert van vóór generatieve AI; geen leerpsychologische detailcriteria |
| **NVAO-beoordelingskader 2024** | Opleidingsaccreditatie | 4 standaarden (+2 voor instellingen zonder ITK); oordeel voldoet / voldoet ten dele / voldoet niet\[19\]\[64\] | Wettelijk kader; toegankelijkheid en studeerbaarheid expliciet in standaard 2; validiteit en betrouwbaarheid toetsing in standaard 3\[19\] | Niet specifiek voor e-learning; geen moduleniveau |
| **ISO/IEC 40180 / ISO 21001** | Procesmatig kwaliteitsmanagement voor leren en onderwijs | Referentiekader of managementsysteem | Borging van processen, verantwoordelijkheden en verbetercyclus | Geen inhoudelijke didactische criteria; beperkt bruikbaar voor één module |

**Hoe een eigen instrument hierop voortbouwt:**
1. **Neem QM of OSCQR over als basislaag** voor oriëntatie, navigatie, techniek en toegankelijkheid (domeinen A, F, G). Dat voorkomt dubbel werk en maakt benchmarking mogelijk. OSCQR ligt voor de hand omdat het open gelicentieerd en aanpasbaar is.\[61\]\[62\]
2. **Voeg een evidence-based-leerstrategielaag toe** (D1–D4, B4–B6, C1). Hier zit de grootste gemiste winst in bestaande rubrics.
3. **Voeg een AI- en regelgevingslaag toe** (domein I), afgestemd op het HAN-toetsbeleid, de AVG en de AI-verordening.
4. **Voeg proces- en outcome-criteria toe** (E2, D7, H2–H5), zodat de audit meer meet dan ontwerpcompliance.
5. **Koppel elk domein aan NVAO-standaarden**, zodat auditresultaten direct bruikbaar zijn als bewijs in opleidingsbeoordelingen: A ↔ std. 1–2, D/I ↔ std. 3, H4 ↔ std. 4, H1–H3 ↔ std. 6.

## Recommendations

1. **Start met een pilot op 3–4 modules** binnen HBO Bedrijfskunde, bij voorkeur één Data Science-module, één AI-module, één Algemene Economie-module en één van een collega. Laat de moduleeigenaren eerst zelf scoren en voer daarna de peer-audit uit. Gebruik de pilot om de criteria te kalibreren: welke criteria leveren consequent verschillende scores op tussen reviewers?
2. **Maak vijf criteria "knock-out"** voor elke module: A2 (alignment), D1 (oefentoetsen), D4 (informatieve feedback), G1–G4 (toegankelijkheid, wettelijk) en I1 (AI-regels per opdracht). Deze hebben het sterkste bewijs of de hardste juridische basis.
3. **Betrek de toetscommissie structureel bij domein D en I.** Criteria D6, D8, I1 en I4 raken direct de borging van toetskwaliteit en de AI-verordening. Inventariseer vóór december 2027 welke AI-toepassingen in toetsing onder Bijlage III kunnen vallen.
4. **Bouw retrieval en spacing in als standaardsjabloon in Brightspace:** per unit een herhaalbare quiz met feedback per antwoordoptie, plus cumulatieve vragen uit eerdere units. Dit is goedkoop en heeft het sterkste bewijs.
5. **Ontwerp AI-tutors met guardrails** (hints, wedervragen, geen eindantwoorden, gevoed met docentmateriaal) en test ze vóór inzet met een protocol van voorbeeld-dialogen (I2–I3). Gebruik open, generieke chatbots niet als vervanging voor oefening.
6. **Rapporteer altijd drie deelscores (I/P/O)** en nooit alleen een totaalscore. Leg per criterium het bewijsstuk vast, zodat audits herhaalbaar zijn.
7. **Breder toepasbaar:** domeinen A–D, F en H zijn één-op-één bruikbaar in corporate learning en L&D. Vervang daar NVAO door de eigen leerdoel- en impactmetingen (bijv. Kirkpatrick-niveau 3–4 als output) en bekijk voor private aanbieders of de EAA wél direct van toepassing is.

## Caveats

- **Checklist-denken.** Rubrics meten vooral aanwezigheid, niet kwaliteit of effect. Een module kan alle QM-standaarden halen en toch vooral passieve consumptie opleveren. Laat reviewers bij elk criterium een kwalitatieve toelichting geven, en weeg ICAP-codering en feedbackkwaliteit zwaarder dan formele aanwezigheid.
- **Compliance ≠ leereffectiviteit.** Criteria in domein F en G (navigatie, WCAG) zijn noodzakelijk maar niet voldoende. Alleen domein H4 meet werkelijk leren, en dat vereist valide toetsen per leerdoel en bij voorkeur vergelijking tussen cohorten.
- **Effectgroottes zijn gemiddelden met grote spreiding.** De feedback-meta-analyse laat grote heterogeniteit zien.\[6\] Mayers effecten zijn in onafhankelijke replicaties kleiner, en het testing-effect kan afnemen bij zeer complexe leerstof.\[2\] Gebruik de getallen als richting, niet als belofte.
- **Veel CSF- en CoI-onderzoek is correlationeel en gebaseerd op zelfrapportage** (tevredenheid, ervaren leren). Studentevaluaties zijn daarom procesindicatoren, geen bewijs van leeropbrengst.
- **AI-bewijs is jong en context-specifiek.** Twee sterke RCT's (Bastani; Kestin) betreffen wiskunde en gestructureerde natuurkunde.\[22\]\[24\] Voor open, ill-structured bedrijfskundige vraagstukken is het bewijs nog dun.\[65\] Herzie domein I jaarlijks.
- **Juridische verwarring.** Commerciële bronnen spreken elkaar tegen over de reikwijdte van de EAA voor onderwijs. Voor bekostigde hogescholen is WCAG 2.1 AA via het Bdto de harde eis.\[39\]\[66\] Laat de juridische afdeling bevestigen hoe de HAN dit interpreteert. Ook de AI-verordening kent nu een uitgestelde, maar niet afgezwakte, planning (2 december 2027).\[54\]
- **Auditlast.** Een volledige audit kost realistisch 6–10 uur per module. Gebruik een quickscan (alleen essentiële criteria) voor periodieke checks en de volledige audit bij herontwerp of bij signalen uit data en evaluaties.
- **Interbeoordelaarsbetrouwbaarheid** van het eigen instrument is nog niet vastgesteld. Plan bij de pilot een kalibratieronde en pas vage criteria aan.

## Sources

1. [EFFECT SIZES AND META-ANALYSES - RetrievalPractice.org](https://pdf.retrievalpractice.org/MetaAnalysisGuide.pdf)
2. [Does research on ‘retrieval practice’ translate into classroom…](https://educationendowmentfoundation.org.uk/news/does-research-on-retrieval-practice-translate-into-classroom-practice)
3. [(PDF) Rethinking the Use of Tests: A Meta-Analysis of Practice Testing](https://www.researchgate.net/publication/315706448_Rethinking_the_Use_of_Tests_A_Meta-Analysis_of_Practice_Testing)
4. [Distributed practice in verbal recall tasks: A review and quantitative synthesis.](https://bibbase.org/network/publication/cepeda-pashler-vul-wixted-rohrer-distributedpracticeinverbalrecalltasksareviewandquantitativesynthesis-2006)
5. [META-ANALYSIS A Meta-Analytic Review of the Benefit of Spacing](http://www.lscp.net/persons/ramus/docs/EPR20.pdf)
6. [Wisniewski et al. (2020)](<https://www.gbl.uzh.ch/quartz/references/Wisniewski-et-al.-(2020)>)
7. [Feedback's Impact on Student Learning](https://www.scribd.com/document/757436810/The-Power-of-Feedback-Revisited)
8. [“Good job” teaches nothing — task feedback does](https://www.caadria2025.org/real-learning-gains-aren-from-pat/)
9. [\[PDF\] The ICAP Framework: Linking Cognitive Engagement to Active Learning Outcomes](https://www.semanticscholar.org/paper/The-ICAP-Framework:-Linking-Cognitive-Engagement-to-Chi-Wylie/9f30b9a4796209ea5ae872ff8959247ebeb15742)
10. [94 Applying the ICAP Framework to Improve Classroom Learning](https://www.unh.edu/teaching-learning-resource-hub/sites/default/files/media/2023-05/itow-applying-the-icap-framework-to-improve-classroom-learning-chi-boucher.pdf)
11. [ERIC - EJ1340511 - A Meta-Analysis on the Community of Inquiry Presences and Learning Outcomes in Online and Blended Learning Environments, Online Learning, 2022-Mar](https://eric.ed.gov/?id=EJ1340511)
12. [Google Scholar](https://scholar.google.com/scholar_lookup?hl=en&volume=50&publication_year=2008&pages=1183-1202&journal=Computers+&+Education=&issue=4&author=PC+Sun&author=RJ+Tsai&author=G+Finger&author=YY+Chen&author=D+Yeh&title=What+drives+a+successful+e-Learning?+An+empirical+investigation+of+the+critical+factors+influencing+learner+satisfaction)
13. [(PDF) E-learning critical success factors: An exploratory investigation of student perceptions](https://researchgate.net/publication/247834942_E-learning_critical_success_factors_An_exploratory_investigation_of_student_perceptions)
14. [(PDF) Critical Success Factors for the of Acceptance and Use of an LMS - The Case of e-CLASS](https://www.researchgate.net/publication/304020823_Critical_Success_Factors_for_the_of_Acceptance_and_Use_of_an_LMS_-_The_Case_of_e-CLASS)
15. [(PDF) INVESTIGATING KEY FACTORS FOR SUCCESSFUL E-LEARNING IMPLEMENTATION](https://www.researchgate.net/publication/333966711_INVESTIGATING_KEY_FACTORS_FOR_SUCCESSFUL_E-LEARNING_IMPLEMENTATION)
16. [QM Higher Education Rubric, Seventh Edition](https://www.qualitymatters.org/sites/default/files/PDFs/StandardsfromtheQMHigherEducationRubric.pdf)
17. [CAST Releases Universal Design for Learning Guidelines 3.0 - AVID Open Access](https://avidopenaccess.org/resource/cast-releases-universal-design-for-learning-guidelines-3-0/)
18. [Wat is verplicht?](https://www.digitoegankelijk.nl/wetgeving/wat-is-verplicht)
19. <https://www.nvao.net/files/attachments/.11273/Beoordelingskader_accreditatiestelsel_hoger_onderwijs_Nederland.pdf>
20. [OSCQR](https://oscqr.suny.edu/standard50/)
21. [AI tutoring outperforms in-class active learning: an RCT introducing a novel research-based design in an authentic educational setting](https://www.semanticscholar.org/paper/AI-tutoring-outperforms-in-class-active-learning:-a-Kestin-Miller/23c1bcb0c0450d79abbe0a1c2a9b4a3b60b6fe03)
22. [Generative AI without guardrails can harm learning: Evidence from high school mathematics](https://www.pnas.org/doi/10.1073/pnas.2422633122)
23. [Bastani Et Al 2025 Generative Ai Without Guardrails Can Harm Learning Evidence From High School Mathematics](https://www.scribd.com/document/1021930370/Bastani-Et-Al-2025-Generative-Ai-Without-Guardrails-Can-Harm-Learning-Evidence-From-High-School-Mathematics)
24. [A Harvard Randomized Controlled Trial Found AI Tutors Produced More Than Double the Learning Gains. Here Is What That Study Actually Shows.](https://impactaieducation.substack.com/p/a-harvard-randomized-controlled-trial)
25. [3.0 Core](https://oscqr.suny.edu/category/3-0-core/)
26. [The QM Rubric: Standards for Excellence](https://educationaldevelopment.uams.edu/qualitymatters/qm-rubric)
27. [Nr. 6405 4 maart 2024](https://zoek.officielebekendmakingen.nl/stcrt-2024-6405.pdf)
28. [NVAO Nederland presenteert nieuw accreditatiekader voor het hoger onderwijs](https://www.nvao.net/nl/nieuws/2024/3/nvao-nederland-presenteert-nieuw-accreditatiekader-voor-het-hoger-onderwijs)
29. [Using multimedia for e‐learning - Mayer - 2017 - Journal of Computer Assisted Learning - Wiley Online Library](https://onlinelibrary.wiley.com/doi/abs/10.1111/jcal.12197)
30. [A meta-analysis of Richard Mayer's multimedia learning research: Searching for boundary conditions of design principles across multiple media types - Illinois Experts](https://experts.illinois.edu/en/publications/a-meta-analysis-of-richard-mayers-multimedia-learning-research-se/)
31. [A meta-analysis of Richard Mayer's multimedia learning research: Searching for boundary conditions of design principles across multiple media types - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1747938X25000673)
32. [Distributed Practice in Verbal Recall](https://www.scribd.com/document/887830028/Cepeda-Distributed-Practice)
33. [The Power of Feedback Revisited: A Meta-Analysis of Educational Feedback Research — audio lecture](https://ennepo.ai/lecture/99ccdfa2-ff67-4399-b7e1-1fed4b81d7cb)
34. [www.frontiersin.org](https://www.frontiersin.org/articles/10.3389/fpsyg.2019.03087/pdf)
35. [The ICAP Framework: Linking Cognitive Engagement to Active Learning Outcomes](https://www.researchgate.net/publication/267629491_The_ICAP_Framework_Linking_Cognitive_Engagement_to_Active_Learning_Outcomes)
36. [Exploring the Design and Impact of Interactive Worked Examples for Learners with Varying Prior Knowledge](https://arxiv.org/pdf/2602.16806)
37. [A Systematic Review of the Challenges of e-Learning ...](https://files.eric.ed.gov/fulltext/EJ1414666.pdf)
38. [EU Toegankelijkheidsrichtlijn: een gelijk speelveld creëren voor iedereen - Europa decentraal](https://europadecentraal.nl/nieuws/eu-toegankelijkheidsrichtlijn-een-gelijk-speelveld-creeren-voor-iedereen/)
39. [Voor wie is digitale toegankelijkheid verplicht? - Proper Access](https://www.properaccess.nl/blog/voor-wie-is-digitale-toegankelijkheid-verplicht/)
40. [Moeten onderwijsinstellingen voldoen aan de European Accessibility Act?](https://www.cardan.com/blog/moeten-onderwijsinstellingen-voldoen-aan-de-european-accessibility-act)
41. [wetten.nl - Regeling - Beoordelingskader accreditatiestelsel hoger onderwijs Nederland - BWBR0049436](https://wetten.overheid.nl/BWBR0049436/2024-03-04/0)
42. [What to Know About the UDL Guidelines 3.0 Update](https://www.novakeducation.com/blog/what-to-know-about-the-udl-guidelines-3.0-update)
43. [Reflections from AHEAD 2025: The UDL Guidelines 3.0](https://otl.du.edu/reflections-from-ahead-2025-the-udl-guidelines-3-0/)
44. [Generative AI without guardrails can harm learning: Evidence from high school mathematics](https://www.researchgate.net/publication/393011815_Generative_AI_without_guardrails_can_harm_learning_Evidence_from_high_school_mathematics)
45. [Generative AI without guardrails can harm learning: Evidence from high school mathematics - ADS](https://ui.adsabs.harvard.edu/abs/2025PNAS..12222633B/abstract)
46. [Harvard Tested a Custom AI Physics Tutor - and Learning Gains Doubled in 49 Minutes - Gadget Review](https://www.gadgetreview.com/harvard-tested-a-custom-ai-physics-tutor-and-learning-gains-doubled-in-49-minutes)
47. [High-level summary of the AI Act](https://artificialintelligenceact.eu/high-level-summary/)
48. [The EU AI Act and assessment: December 2027 is not a snooze button](https://uniwise.eu/resources/blog/the-eu-ai-act-and-assessment-december-2027-is-not-a-snooze-button)
49. [EU agrees Digital Omnibus deal to simplify AI rules](https://www.whitecase.com/insight-alert/eu-agrees-digital-omnibus-deal-simplify-ai-rules)
50. [EU Council Formally Adopts AI Omnibus Amending EU AI Act, 29 June 2026](https://www.licentium.io/post/eu-council-formally-adopts-ai-omnibus-amending-eu-ai-act-29-june-2026)
51. [EU AI Omnibus enters into force, amending the AI Act](https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act)
52. [Digital Omnibus: What Changed in the EU AI Act](https://www.trail-ml.com/blog/eu-ai-act-digital-omnibus-changes)
53. [AI Act: the Digital Omnibus postpones high-risk rules and adds new prohibitions](https://www.noze.it/en/insights/ai-act-digital-omnibus-2026/)
54. [Digital Omnibus on AI: Regulation (EU) 2026/1744 Is Published in the Official Journal](https://www.nicfab.eu/en/posts/digital-omnibus-ai-official-journal/)
55. [Certification](https://oscqr.suny.edu/certification/)
56. [Excellence rome - v03 2016](https://www.slideshare.net/EbbaOssiann/excellence-rome-v03-2016)
57. [Quality Matters Releases 7th Edition Rubric](https://doit.umbc.edu/itnm/post/136682/)
58. [Quality Matters Rubric 7th Edition: What’s New? « Ecampus Course Development and Training](https://blogs.oregonstate.edu/inspire/2023/07/10/quality-matters-rubric-7th-edition-whats-new/)
59. [QM 7th Edition Update Highlights:](https://www.montgomerycollege.edu/_documents/offices/eass/qm-7th-edition.pdf)
60. [The SUNY Online Course Quality Review Rubric (OSCQR)](https://acadtech.siena.edu/the-suny-online-course-quality-review-rubric-oscqr/)
61. [OSCQR](https://oscqr.suny.edu/)
62. [The OSCQR Rubric - Office of Curriculum, Assessment and Teaching Transformation - University at Buffalo](https://www.buffalo.edu/catt/teach/develop/evaluate/evaluating-course-design/oscqr-rubric.html)
63. [News - E-xcellencelabel - EADTU](https://e-xcellencelabel.eadtu.eu/news)
64. [NVAO NEDERLAND UITVOERINGSREGELS ACCREDITATIESTELSEL HOGER ONDERWIJS](https://www.nvao.net/files/attachments/.13163/Uitvoeringsregels_Accreditatiestelsel_Hoger_Onderwijs_Nederland_september_2025.pdf)
65. [Review of Kestin et al.’s June 2025 Harvard Study on AI Tutoring](https://etcjournal.com/2025/11/10/review-of-kestin-et-al-s-june-2025-harvard-study-on-ai-tutoring/)
66. [Digitale toegankelijkheid in het onderwijs](https://www.properaccess.nl/onderwijs-digitale-toegankelijkheid/)
