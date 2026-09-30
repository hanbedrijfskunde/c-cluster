# KSF-criteria voor een gebouwde e-learning

Afgeleid uit [docs/ksfs-e-learning.md](../../../../docs/ksfs-e-learning.md) (domeinen A t/m I,
ID's ongewijzigd, zodat scores naar het onderzoek terug te herleiden zijn). Dit bestand
voegt toe wat het onderzoek niet kan weten: **waar je het aan de gebouwde site ziet**. De
regel-ID's (TK-2, BW-1, MD-5, …) verwijzen naar `docs/BLUEPRINT-ELEARNING-A3.md`. Zijn
ze daar hernummerd, volg dan het blueprint; de kolom „Kijk in de site" is een aanwijzing, geen
bewijs. **Een regel die het blueprint claimt is nog geen score: de score volgt uit wat je zelf
in het product ziet.**

Prio: **E** essentieel, **A** aanvullend. Laag: **I** input, **P** proces, **O** opbrengst.
Knock-out (moet ≥ 2): **A2, D1, D4, G1–G4, I1**. Schaal en beslisregel staan in
[SKILL.md](../SKILL.md).

## Zo gebruik je de kolom „Kijk in de site"

Eerst de waarneming, dan pas de score. Schrijf bij elk criterium op *wat je zag* en *waar*
(pagina, taaknummer, bestand, regel). Kun je het niet zien omdat het (nog) niet gebouwd is,
zet dan „nog niet gebouwd". Kun je het niet zien omdat het pas met studenten meetbaar is,
zet dan „niet te beoordelen vóór de pilot". Geen van beide is een 0.

## Domein A — Didactisch ontwerp en alignment

| ID | Criterium | Prio | Laag | Kijk in de site |
|---|---|---|---|---|
| A1 | Leerdoelen observeerbaar en op hbo-niveau | E | I | Leeruitkomsten in `data/luk.json` en LRD §4.1: werkwoorden, niveau ten opzichte van de LUK van het C-cluster |
| A2 | Per leerdoel: activiteit én toets (alignmentmatrix) | E | I | `data/luk.json` (dekking §4.3), BW-12, BW-13 en `content-check`: heeft elk bewijsonderdeel een LUK-koppeling, en oefent de taak dat wat het bewijsonderdeel toetst? Zoek een LUK-onderdeel dat wel „gedekt" heet maar waar geen taak voor oefent |
| A3 | Probleem- of taakgericht opgebouwd (casus vóór theorie) | A | I | Volgorde in `leerblok-N.html`: eigen vraagstuk en oefencasus vóór de uitlegtekst? (TK-3, MD-3) |
| A4 | Voorkennis geactiveerd of gediagnosticeerd | A | I | Startpagina en begin van elk leerblok; de terugblik vanaf leerblok 2 (TP-1 t/m TP-3); mogelijkheid om over te slaan wie het al kan (TK-5) |
| A5 | Studielast vermeld en realistisch | E | I/P | Richttijd per taak en per leerblok (PF-5: 45 min). Klopt de som? Loop een blok door met een timer. Realistisch blijkt pas uit AP-2, dus dat deel is P |
| A6 | Start, doel, structuur en verwachtingen direct duidelijk | E | I | `index.html`: is in één scherm te zien wat je gaat doen, hoelang en waarom (LB-1, ST-1)? |

## Domein B — Inhoud en multimedia

| ID | Criterium | Prio | Laag | Kijk in de site |
|---|---|---|---|---|
| B1 | Inhoud actueel, correct, herkomst zichtbaar | E | I | `bronnen.html` en BR-1 t/m BR-6: bronnen met jaar en werkende link; laat een vakinhoudelijke peer een steekproef van 3 taken lezen |
| B2 | Geen decoratieve of afleidende elementen | E | I | Steekproef van alle video's (nu 2 of meer) en 5 pagina's: muziek, sfeerbeelden, „leuke weetjes"? |
| B3 | Kernbegrippen gesignaleerd (koppen, markering) | A | I | Opmaak per taak: nummer, „waarom", tijd en „klaar als" zichtbaar (TK-2), Engelse vaktermen uitgelegd (QA-5) |
| B4 | Video's gesegmenteerd (≈ ≤ 6–10 min per concept), pauzeerbaar | E | I | MD-4: ≤ 3 min per video, met bedieningsknoppen, geen autoplay (MD-6) |
| B5 | Tekst en beeld bij elkaar; narratie niet letterlijk als tekst herhaald | A | I | Video's met ondertitel en het transcript naast elkaar: herhaalt de schermtekst de spraak woord voor woord? |
| B6 | Uitgewerkte voorbeelden die afbouwen naar zelfstandig werk | A | I | Oefencasus met modelantwoord → toepassing op het eigen vraagstuk (TK-3, TK-4): is er afbouw, of springt het van voorbeeld naar volledig zelf? |
| B7 | Licentie en auteursrecht van derden in orde | E | I | LI-1 t/m LI-5; `lits/` mag niet in de repository staan; kijktips zijn gewone links (MD-14, MD-16) |

## Domein C — Activering en interactie

| ID | Criterium | Prio | Laag | Kijk in de site |
|---|---|---|---|---|
| C1 | ≥ 50 % van de leertijd constructief of interactief (ICAP) | E | I | Codeer **elke** taak van de vier leerblokken als passief (lezen/kijken), actief (klikken, markeren), constructief (zelf schrijven, ontwerpen) of interactief (Wissel, peerfeedback). Weeg met de richttijd. Laat de tabel in het rapport zien; ICAP is een diagnose, geen harde norm |
| C2 | Na elke instructie-eenheid een toepassing met feedback | E | I | Ritme van vijf stappen (TK-18): volgt na elke uitleg een taak, en geeft de site daarop een reactie (BW-1, BW-2)? |
| C3 | Geplande student-studentinteractie die inhoudelijk nodig is | A | I/P | De Wissel en de feedbacklog (WS-1 t/m WS-11, LB-14): is het echt nodig om iets van een ander te krijgen, of kan het overgeslagen worden zonder gevolg (EV-09)? |
| C4 | Integratie en transfer naar de eigen praktijk | A | I | Verbanden-kaart, synthese en reflectie (VB, EV-10, EV-11); het eigen vraagstuk als anker |
| C5 | Interactie is daadwerkelijk ontstaan | A | P | Alleen na de pilot: hoeveel Wissel-uitwisselingen, hoe diep? |

## Domein D — Toetsing, oefenen en feedback

| ID | Criterium | Prio | Laag | Kijk in de site |
|---|---|---|---|---|
| D1 | Laagdrempelige oefentoetsen, herhaalbaar | E | I | Oefenversie per taak, herhaalbaar (TK-6: ≥ 10×), zonder gevolgen voor de status (TK-4). Ophaalmoment vóór de meenemen-kaart (TP-2) telt ook. Probeer het zelf drie keer: verandert de oefening, of is het dezelfde vraag? |
| D2 | Stof komt gespreid terug | E | I | Terugblik en „werken met tussenpozen" (TP-1 t/m TP-11): komt week-1-stof terug in leerblok 3 en 4, of alleen in het volgende leerblok? Testprofielen met pauzes van 1 uur, 1 dag, 5 dagen en 14 dagen (TP-7) |
| D3 | Oefenvragen gaan verder dan reproductie | E | I | Transfervraag (TP-4), stelling (LB-8), „wat laat dit model niet zien" (EV-11). Tel per oefenvraag of hij herhalen of toepassen vraagt; alleen kennisvragen scoren laag |
| D4 | Feedback geeft taak- én procesinformatie (feed forward), niet alleen goed/fout of score | E | I/P | Meldingen van de controles: één zin per niet-ok-controle over wat ontbreekt (BW-2, BW-9) is *taak*-informatie. Zegt de melding ook *hoe verder* (proces) en wijst BW-7 naar het modelantwoord? Let op: soort C telt alleen woorden (BW-11), dus de site beoordeelt de kwaliteit van een reden niet. De site zegt dat zelf (BW-6). Scoor of de student zonder docent weet wat de volgende stap is. Neem 10 meldingen letterlijk in het rapport op |
| D5 | Beoordelingscriteria en voorbeelden vooraf beschikbaar | E | I | „Klaar als" bij elke taak (TK-2; let op: `bron: concept-auteur` telt pas mee na akkoord van de auteur) en modelantwoorden |
| D6 | Summatieve toets valide en betrouwbaar | E | I | Een deel valt bewust buiten de site: X-14 (geen kwaliteitsoordeel, geen vervanging van de beroepsproducten). Beoordeel alleen of het dossier (EV-01 t/m EV-11) de LUK-onderdelen dekt die het claimt; anders n.v.t. (bewust, X-14) |
| D7 | Feedback tijdig | E | P | Site: binnen 1 s (BW-1). Docentfeedback op het dossier: pas na de pilot |
| D8 | Bestand tegen ongeautoriseerd AI-gebruik, of AI-gebruik expliciet toegestaan | E | I | De bewijsstukken zijn eigen-vraagstuk-gebonden en de site controleert alleen structuur. Zegt de site wat een student met AI mag doen (zie I1)? Kan iemand een Compleet-status krijgen met door AI gegenereerde tekst, en is dat eerlijk gemeld (BW-6: „Of het goed is, bespreek je met je coach")? |

## Domein E — Begeleiding en sociale aanwezigheid

| ID | Criterium | Prio | Laag | Kijk in de site |
|---|---|---|---|---|
| E1 | Duidelijk wie begeleidt, hoe en wanneer bereikbaar | E | I | Coachrol op de site; in het werkcollege de docent zelf. De site zegt nergens „stuur een mail": is dat een keuze (X-9)? Wijst de site naar de coach als de controle vastloopt? |
| E2 | Docent zichtbaar aanwezig tijdens uitvoering | E | P | Docentmodus: stapkaart, docentkaart met „als het anders loopt" (DM-3, DM-7); of dat in de zaal gebeurt blijkt pas in de pilot |
| E3 | Signalen en acties voor wie achterblijft | A | P | Herinnering bij ≥ 7 dagen dezelfde status (WS-11); de aanbevolen week en dag zonder slot (TP-10). Geen mail en geen dashboard (X-6, X-9): dat is een bewuste keuze |
| E4 | Laagdrempelige plek voor vragen | A | I/P | „Vragen aan je coach" in de site, de feedbacklog, of alleen de zaal? |

## Domein F — Navigatie, gebruiksvriendelijkheid en techniek

| ID | Criterium | Prio | Laag | Kijk in de site |
|---|---|---|---|---|
| F1 | Consistente navigatie; elk onderdeel binnen 3 klikken | E | I | Klik vanaf `index.html` naar elke pagina en taak en tel (SI-3: ≤ 2 klikken naar een pagina) |
| F2 | Alle links, embeds en tools werken | E | I | `node tools/link-check.mjs`, BR-6 op DOI's, walkthrough van de gepubliceerde site zonder consolefout |
| F3 | Technische vereisten en ondersteuning vermeld | E | I | README, studentintroductie (DL-2), melding bij geblokkeerde opslag (DS-12), en bij ontbrekende `crypto.subtle` (geen https) |
| F4 | Bruikbaar op mobiel en laptop | A | I | Playwright op 360 px: 0 px horizontale scroll (PF-1), alle velden invulbaar |
| F5 | Weinig externe tools, functioneel | A | I | PR-1: 0 verzoeken naar andere domeinen; het antwoord is per constructie goed. Beloon dat, maar scoor het niet hoger dan het is |

## Domein G — Toegankelijkheid en inclusie

| ID | Criterium | Prio | Laag | Kijk in de site |
|---|---|---|---|---|
| G1 | Video's met gecontroleerde ondertiteling en transcript | E | I | MD-5: WebVTT en transcript bij **elke** video. Lees de ondertitels tegen de spraak. Een computerstem met een ondertitel uit dezelfde tekst is technisch in orde; een conceptvideo (fase 12) noem je zo |
| G2 | Alt-tekst voor informatieve afbeeldingen; decoratieve gemarkeerd | E | I | axe of Lighthouse op alle pagina's, plus steekproef van de diagrammen |
| G3 | Documenten toegankelijk (koppen, leesvolgorde, contrast) | E | I | De afdrukbare pagina's en pdf's van het dossier; docentgids; contrast (TG-3: ≥ 4,5:1) |
| G4 | Volledig met toetsenbord te bedienen, ook spellen | E | I | TG-2 (leerblok 1 zonder muis), MD-9 (spellen zonder muis), zichtbare focus. Doe het zelf, alleen met Tab, Enter en spatie |
| G5 | Keuze in representatie of expressie | A | I | Drie routes per leerblok (MD-1, MD-2, MD-12: alles ook met alleen tekst). Bestaan ze allemaal al? |
| G6 | Voorbeelden divers en vrij van stereotypering | A | I | Inhoudsanalyse van de casussen en fictieve bronkaarten (MD-15) |
| G7 | Ingekochte tools voldoen aan WCAG | A | I | Geen ingekochte tools: n.v.t. (PR-1, X-4, X-5) |

De wet: WCAG 2.1 AA is de wettelijke ondergrens, 2.2 AA is best practice (TG-1 vraagt 2.1
AA). Een Lighthouse-score is een hulpmiddel, geen conformiteitsverklaring: een schermlezer-
doorloop (TG-5) en de toetsenbordproef blijven nodig.

## Domein H — Evaluatie, data en verbetering

| ID | Criterium | Prio | Laag | Kijk in de site |
|---|---|---|---|---|
| H1 | Studenten geven gestructureerd feedback op ontwerp en techniek | E | P | Pilot: vraag na afloop (AP-3, AP-7); tussentijds moment in de site? |
| H2 | LMS-data periodiek geanalyseerd | E | P | Er is bewust geen server, LRS of analytics (X-1, PR-1). **N.v.t. (bewust)**: alleen als de tijdnotities van de docent (AP-2) en de terugblik-logs (TP-8) zijn bedoeld als vervanging en dat in het ADR staat. Noem het verlies aan inzicht bij de spanningen |
| H3 | Gedocumenteerde verbetercyclus | E | P | Het ADR (B1, B2, …) en het BUILDPLAN met bevindingen per fase. Loop 3 recente besluiten na: volgen ze uit bewijs, of uit smaak? |
| H4 | Leeropbrengst gemeten tegen de leerdoelen | E | O | Niet te beoordelen vóór de pilot. Vraag: kán het na de pilot? Zijn er vooraf een nulmeting en een vergelijking? Het dossier zegt expliciet geen kwaliteitsoordeel (X-14) |
| H5 | Onderscheid tevredenheid, ervaren en werkelijk leren | A | O | Kijk in de pilotvragen (AP-3, AP-7): meten ze ervaring, en is daar niets meer van gemaakt? |

## Domein I — AI, privacy en integriteit

De site bevat geen AI (X-2). De criteria I2, I3 en I4 zijn dan per constructie n.v.t.: zeg dat
met verwijzing naar X-2 en zet het in de verantwoording, niet als een score.

| ID | Criterium | Prio | Laag | Kijk in de site |
|---|---|---|---|---|
| I1 | Per opdracht vermeld of en hoe AI gebruikt mag worden, met verantwoording | E | I | **Knock-out en het meest waarschijnlijke gat.** Zoek in de studentintroductie, op de startpagina en per taak. Een site zonder AI zegt daarmee nog niet wat studenten met AI mogen doen bij hun eigen tekst. Ontbreekt het, dan is dit een 0 of 1, ook al is de site zelf AI-vrij |
| I2 | AI-tutor met guardrails, getest | E | I | N.v.t. (X-2) |
| I3 | AI-feedback gecontroleerd en als AI herkenbaar | E | P | N.v.t. (X-2) |
| I4 | Geen autonome AI voor beoordeling of proctoring | E | I | Voldaan per constructie (X-2, X-14). Scoor 2, niet 3 |
| I5 | Persoonsgegevens en doel vastgelegd; DPIA of verwerkersovereenkomst waar nodig | E | I | PR-1 t/m PR-4, privacytekst ≤ 100 woorden (ST-2), netwerktrace zonder verzoeken (PR-2). Alles blijft in de browser van de student; is dat ook vastgelegd voor de docent die dossiers inleest? (DS-9, DS-10) |
| I6 | Studenten weten welke data over hen worden verzameld | E | I | Privacytekst op `index.html` en bij de Wissel (WS-10, ≤ 60 woorden): zeggen ze het juiste, en is het leesbaar voor een eerstejaars? |
| I7 | Kritisch AI-gebruik als leerdoel | A | I | Bewuste keuze van de opleiding; is dit een LUK van deze e-learning of niet? Noem het, scoor het alleen als het een doel is |

## Van criterium naar oordeel

- Bij elk criterium één zin over kwaliteit, niet alleen aanwezigheid.
- Twijfel tussen twee scores: kies de lagere en zet de reden erbij. Een score die alleen
  op het blueprint leunt (de regel bestaat, maar je hebt het niet zelf gezien) krijgt een `*`.
- Een criterium dat het product bewust niet heeft (X-n in het BLUEPRINT §8, met reden in het
  ADR) krijgt „n.v.t. (bewust, X-n)" en valt uit het gemiddelde. Alleen als ook het doel
  achter het criterium ergens anders wordt gehaald. Anders is het een gewone lage score
  met een bewuste keuze in de spanningen.
- NVAO-koppeling voor wie het rapport als bewijs voor de opleiding wil gebruiken: A ↔ std.
  1–2, D en I ↔ std. 3, H4 ↔ std. 4, H1–H3 ↔ std. 6 (het onderzoek noemt deze koppeling).
