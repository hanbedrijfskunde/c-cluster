# Bewijs verzamelen aan de gebouwde site

De site staat in een aparte repository. Lokaal: `/Users/witoldtenhove/Documents/HAN/a3-learning`
(kloon van `hanbedrijfskunde/a3-learning`). Gepubliceerd: `https://hanbedrijfskunde.github.io/a3-learning/`.
Controleer eerst of de lokale kloon dezelfde commit heeft als de gepubliceerde stand
(`git -C … log -1`, en de workflow-run op GitHub), en beoordeel de **gepubliceerde** site: dat
is wat studenten zien.

## 1. De testpoort draaien (5 minuten)

Vanuit de map van de repository, in deze volgorde:

```
node --test                     # zonder mapargument: met tests/ faalt het op Node 22+
node tools/content-check.mjs
node tools/link-check.mjs
```

Noteer het aantal tests en of er waarschuwingen zijn. Waarschuwingen in `content-check` over
`concept-auteur` betekenen tekst die de auteur nog niet heeft goedgekeurd; die telt bij
D5 en A2 niet als bevestigd. Groene tests bewijzen dat de site doet wat de spec zegt, niet dat
de spec een goede module oplevert; ze zijn dus bewijs voor F2 en QA-criteria, niet voor
D of C.

## 2. De walkthrough als student

Doe dit zelf met Playwright, op de gepubliceerde URL, en werk **alle leerblokken die bestaan**
door, niet alleen leerblok 1. Een student zonder eigen vraagstuk en een student mét worden
beide gedaan (dat is de terugvaloptie uit Autonomy). Leg per stap vast wat je zag.

1. Startpagina: alias, teamnummer, vraagstuk, waarom-zin, of „nog geen scherp vraagstuk".
   Hoe lang duurt het voordat je aan het eigenlijke leren begint (A6, Purpose)?
2. Per taak: waarom, tijd, „klaar als", oefenversie, modelantwoord, toepassing. Tik bewust
   een zwak antwoord en daarna een goed antwoord. **Keurt de controle een goed antwoord af, of
   laat hij een zwak antwoord door?** Dat is de belangrijkste testbaarheid van D4 en van de
   grondslag van de bewijsstatus. Neem minstens drie zwakke en drie goede invoeren op en
   noteer de letterlijke melding.
3. Herlaad, sluit af, exporteer het dossier, wis alles, importeer (DS-1 t/m DS-6).
4. Zet de tijdstempels in `localStorage` op 1 uur, 1 dag, 5 dagen en 14 dagen terug en open
   leerblok 2 (TP-7): ziet de student steeds de juiste terugblik?
5. Media: speel elke video en elk spel. Lees de ondertitel tegen de spraak, controleer het
   transcript, druk op Tab door het spel.
6. Docentmodus: draai deel 1 door met alleen de docentmodus en tel de momenten waarop je iets
   buiten de docentmodus moet opzoeken (AP-4).

Meet daarbij, op zowel 1280 px als 360 px:

- consolefouten (`browser_console_messages`), 0 verwacht;
- netwerkverzoeken naar andere domeinen (`browser_network_requests`), 0 verwacht (PR-1);
- horizontale scroll op 360 px;
- alleen-toetsenbord: kun je alle velden bereiken en de opslag activeren, en is de focus
  zichtbaar?
- pagina-gewicht en tijd tot bruikbaar.

Voor de toegankelijkheid: Lighthouse (`lighthouse_audit`) of axe per pagina, plus de proef met
het toetsenbord. Automatische tools vangen slechts een deel van de problemen; een score
van 100 is geen conformiteit.

## 3. Inhoud lezen

Lees `data/leerblok-1.json` t/m `-4.json`, `data/luk.json`, `data/terugblik.json`, de
bronnenbestanden, en de docentbestanden. Zoek daar:

- **ICAP-verdeling** (C1): tel de richttijd per activiteitstype.
- **Alignment** (A2): neem één LUK-onderdeel uit `luk.json` dat „gedekt" heet en volg het naar
  een taak, een controle en een modelantwoord. Werkt de keten?
- **Concept- en ontbrekende teksten**: velden met `bron: concept-auteur`, lege „waarom" of
  „klaar als", placeholders, verwijzingen naar iets wat er niet is (KISS · Student).
- **Vraagniveau** (D3): reproductie of toepassing?

## 4. Bewijs dat pas na de pilot komt

Zet in de verantwoording per criterium welke gegevens nog moeten komen en wie ze verzamelt:
tijdnotities van de docent (AP-2), de nabevraging (AP-3, AP-7), de terugblik-logs (AP-8), de
lezing van EV-11 (AP-6), het gesprek met 5–8 studenten. Zonder die gegevens blijven
P en O „niet te beoordelen".

## Wie stelde het vast

Zet achter elk bewijsstuk een van drie labels en gebruik ze in de scorekaart:

- **T**: geautomatiseerde test van de repository (bouwer);
- **B**: waarneming van de beoordelaar (Playwright of handmatig);
- **M**: gedaan door een mens die de site niet bouwde (student, collega, docent).

Een criterium dat alleen T-bewijs heeft, krijgt een `*`. Voor toegankelijkheid en
begrijpelijkheid weegt M zwaarder dan T; het BUILDPLAN zegt zelf op meerdere plekken dat de
menselijke tester door Playwright is vervangen.
