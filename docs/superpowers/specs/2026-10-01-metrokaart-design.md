# Ontwerp: metrokaart van het leerblok

**Status:** ontwerp, ter review
**Datum:** 1 oktober 2026
**Product:** hybride e-learning A3 (repository `hanbedrijfskunde/a3-learning`), alle studentpagina's
**Na akkoord:** vastleggen in LRD 0.19 (FR-72, AC-48), ADR (B110), BLUEPRINT (SX-4 aangepast, SX-18, SX-19, Bijlage A en B) en DESIGN (§6 Metrokaart); daarna bouwen in de worktree `metrokaart` van a3-learning.

## 1. Doel

De student ziet bovenaan elke pagina waar hij of zij is in het leerblok, zoals een reiziger op een metrokaart: één lijn per leerblok in een eigen kleur, een halte per taak, en een markering „hier”. De kaart laat ook zien waar het spoor zich splitst (een keuze of een duo dat elk iets anders doet) en waar het weer samenkomt. Begin en eind van een lijn zijn overstappunten naar het vorige en het volgende leerblok.

Purpose: de student ziet in één oogopslag wat er nog komt en hoe ver het blok is. Autonomy: elke halte is een link, er is geen slot (TK-1), en de kaart toont dat er verschillende routes zijn. Mastery: de afgelegde weg is gevuld. KISS: de kaart vervangt de segmentbalk van de taakkop, zodat er één voortgangsbeeld is in plaats van twee.

## 2. Besluiten uit het gesprek

| Vraag | Keuze van de auteur | Afgewezen |
|---|---|---|
| Wat is een halte | Een taak; alleen de huidige taak klapt open in vier stap-haltes (waarom, stof, oefenen, toepassen) | alleen taken (stappen dan nergens op de kaart); elke stap een halte (12 tot 24 haltes, te lang op 360 px) |
| Splitsingen | Route A/B in 3.2; duo met twee artikelen in de oefening van 4.2; de verdieping als zijtak; tekst/video/spel in de stap stof van de mediataak | — |
| Andere pagina's | Start, Dossier en Bronnen tonen de lijn van het leerblok waar de student het laatst werkte; bij een eerste bezoek lijn 1 met de student vóór het beginpunt | het hele netwerk van vier lijnen; geen kaart buiten de leerblokken (dan niet „iedere pagina”) |
| Klikbaar | Ja: elke halte en elk overstappunt is een link | alleen oriëntatie |
| Lijnkleuren | Vier eigen metrokleuren als tokens: 1 magenta `#E50056`, 2 blauw `#0063B2`, 3 groen `#00804A`, 4 oranje `#C2410C` | tinten van magenta (lijnen niet uit elkaar te houden, lichte tinten halen 3:1 niet) |
| Segmentbalk (SX-4) | De metrokaart vervangt hem; het tekstalternatief „Taak 2 van 3, stap 3 van 4” gaat over op de kaart; de stappenrij met namen blijft | beide houden (dubbele informatie op een klein scherm) |
| Tikvlak op smalle schermen | Een strook per halte: volle hoogte van de kaart, breedte tot de buren (≥ 24 × 24 px, WCAG 2.5.8), geen overlap | 44 × 44 px per halte (past niet: 11 × 44 = 484 px op 328 px); de stap-haltes weglaten op mobiel (nog 8 haltes, ≈ 41 px, past nog steeds niet); de lijn op twee regels (meer hoogte, ingewikkelder tekenwerk) |
| Techniek | Eén inline SVG, getekend uit de leerblokdata en de opslag | HTML en CSS met lijnstukken (splitsen en samenkomen breekbaar); een vaste SVG per leerblok (loopt achter als een taak verandert, zoals bij B102) |

## 3. Wat de kaart toont

```
 ⦿━━━━━●━━━━━●━━┳━ A ━●━┳━━●━━━━━●━━━━━●━━━━━⦿══ 3
 Vorige keer 3.1   3.2 ┗━ B ━●━┛  4.1   4.2   4.3   Afsluiten
                             ▲ hier
```

**Lijn.** Eén horizontale lijn van 6 px in de kleur van het leerblok (`--lijn-N`).

**Haltes.** Een taak is een cirkel op de lijn, met daaronder het taaknummer. De stand komt uit `stapStand` (`js/voortgang.js`), die nu de segmentbalk voedt:

| Stand | Beeld | Tekst voor schermlezers |
|---|---|---|
| afgerond (klaar gezet) | cirkel gevuld in de lijnkleur | „afgerond” |
| huidige taak | witte cirkel, zwarte ring van 3 px, label „hier” eronder | „hier” (`aria-current="step"`) |
| open | witte cirkel met rand in de lijnkleur | „open” |

**De huidige taak klapt open.** In plaats van één halte staan er vier kleinere stap-haltes: Waarom, Stof, Oefenen, Toepassen. Ze hebben dezelfde standen, en de stap die de student ziet heeft de ring. De overige taken blijven één halte.

**Splitsingen.** Een taak met een splitsing staat op de kaart als een vork: het spoor splitst vóór de halte in parallelle takken, elk met een eigen halte, en komt erna weer samen. De tak die de student koos is vol getekend, de andere gestippeld. Zolang er nog niets gekozen is, zijn alle takken vol.

| Plek | Takken | Gekozen tak komt uit |
|---|---|---|
| Taak 3.2, stap oefenen en toepassen | A · databank / B · AI-tool | veld `route` van de toepassing, anders van de oefening |
| Taak 4.2, stap oefenen | Artikel 1 / Artikel 2 | veld `artikel` van de oefening |
| Mediataak van het leerblok (`blok.media.taak`), stap stof | Tekst / Video / Spel | `media:route:N` (tekst als niets bewaard is, MD-2) |
| Verdieping (`verdieping.na`) | zijtak met één halte „Verdieping”, gestippeld spoor | gedaan als `verdieping:N` gezet is; dan vol |

Is een taak met splitsing ingeklapt, dan staan de takken op taakniveau (3.2 A/B, 4.2 Artikel 1/2). Klapt ze open, dan liggen de stap-haltes uit de kolom „Plek” op de takken en de andere stappen op de hoofdlijn. Bij de mediataak splitst alleen de stap stof in drie. Dat is de enige splitsing die alleen bij de opengeklapte taak in beeld komt; ingeklapt is de mediataak een gewone halte. De verdieping buigt af na de halte van haar taak en sluit weer aan vóór de volgende halte (of vóór „Afsluiten” als het de laatste taak is). Ze is geen halte op de hoofdlijn, omdat ze optioneel is (TK-13, TK-14).

**Overstappunten.** Begin en eind van de lijn zijn een witte cirkel van 18 px met een zwarte rand van 4 px, de vorm van een overstappunt op een metrokaart. Aan het begin staat „Vorige keer” met een stompje van lijn N−1; bij leerblok 1 is dat „Start” zonder stompje. Aan het eind staat „Afsluiten” met een stompje van lijn N+1; bij leerblok 4 staat er „Dossier” zonder stompje. De stompjes zijn decoratief (geen link, `aria-hidden`): de overstap staat in de toegankelijke naam van het overstappunt („Afsluiten, overstap naar leerblok 3”), en het afsluitscherm heeft de knop „Door naar leerblok N+1” al. Een eigen tikvlak per stompje zou de stroken op 360 px onder 24 px duwen. Het eindpunt is gevuld als het leerblok is afgerond (TK-16); het beginpunt is gevuld zodra de student in het leerblok een taak heeft gestart.

**Labels.** Taaknummers staan onder de haltes, in 13 px (SX-10). Takken krijgen een kort label (A, B, Art. 1, Art. 2, T, V, S) met de volledige naam in de toegankelijke naam. De labels van de overstappunten staan boven de lijn (links en rechts uitgelijnd), alle andere eronder, zodat ze elkaar niet raken. Past de kaart niet, dan houden alleen „hier” en de overstappunten een label en verliezen de andere haltes het hunne (zie §6).

## 4. Gedrag

**Plaats.** Onder de kop en het hoofdmenu, boven `main`, in een `nav` met `aria-label="Waar je bent in leerblok N"`. Hij staat op de studentpagina's index, leerblok-1 t/m 4, dossier en bronnen, en niet op docentmodus, verificatie en controlelab (SX geldt daar niet). Hij scrolt mee met de pagina en is niet vastgezet: de vaste taakkop blijft het enige vaste element bovenin.

**Welk leerblok.** Op `leerblok-N.html` is dat leerblok N. Op de andere pagina's is het het leerblok met de jongste `positie:N.bijgewerkt`. Is er geen positie, dan is het leerblok 1 en staat „hier” bij het beginpunt „Start”.

**Waar „hier” staat.** Op een leerblokpagina volgt de ring het adres (`#taak-x.y/stap`): in het overzicht staat hij op het beginpunt, in een taak op de stap, en bij `#afsluiten` op het eindpunt. Op de andere pagina's staat hij op de taak uit `positie:N`. De kaart luistert naar de bestaande adreswissel en tekent opnieuw. Er komt geen tweede router.

**Links.** Een taakhalte gaat naar `leerblok-N.html#taak-x.y`, een stap-halte naar `#taak-x.y/<stap>`, een tak naar de taak (de keuze zelf maakt de student in de taak), de verdieping naar `#taak-<na>` (waar ze verschijnt), het beginpunt naar `leerblok-N.html` (overzicht met „Vorige keer”), en het eindpunt naar `#afsluiten`. Bij leerblok 4 gaat het eindpunt naar `dossier.html`.

**Segmentbalk.** `segmenten` in de taakkop van `js/leerblok.js` vervalt. De kaart neemt het `aria-label` over (`segmentLabel`, SX-4). De stappenrij met namen en de knop „← Leerblok N” blijven.

## 5. Architectuur

Hetzelfde patroon als `voortgang.js` en `leerblok.js`: de logica zonder DOM is apart te testen.

| Eenheid | Rol | Hangt af van |
|---|---|---|
| `js/metro-model.js` | `metroModel({ blok, store, adres })` geeft een lijst haltes, takken en overstappunten met stand, label, toegankelijke naam en href. Geen DOM, geen maten. Ook `laatsteLeerblok(store)`. | `voortgang.js` (`stapStand`), `afgerond.js`, `media.js` (alleen `leesRoute`, of de sleutel overnemen als `media.js` te zwaar is voor de startpagina) |
| `js/metro.js` | `tekenMetro(model, breedte)` maakt de SVG met `<a>`-elementen. Kiest de opmaak (labels weg bij te weinig ruimte). `plaatsMetro()` zoekt de plek, laadt de data en tekent opnieuw bij `hashchange` en `resize`. | `metro-model.js`, `dom.js` (`h`) |
| `data/leerblok-N.json` | Nieuw optioneel veld per taak: `"spoor": { "stappen": ["oefenen", "toepassen"], "veld": "route", "takken": [{ "waarde": "A · databank", "kort": "A" }, …] }`. De verdieping en de mediataak staan al in de data. | content-check valideert het veld |
| `css/site.css` | Tokens `--lijn-1` … `--lijn-4` in `:root`; opmaak `.metro`. | — |

Leerblokpagina's laden de leerblokdata al. Index, dossier en bronnen laden voor de kaart alleen `data/leerblok-N.json` van het laatste leerblok. De gewichtscontrole telt dat mee. Op leerblokpagina's komt er ongeveer 8 kB bron bij, op index, dossier en bronnen hoogstens de grootte van één leerblokbestand (bronnen: nu 63,6 kB). Alle pagina's blijven ruim binnen 300 kB gzip.

**Foutgevallen.** Zonder opslag (`kiesOpslag` valt terug op geheugen) toont de kaart de lijn zonder stand, met „hier” op het adres. Laadt de data niet, dan komt er geen kaart en blijft de pagina gewoon werken. Een onbekende waarde in een keuzeveld betekent: nog niets gekozen.

## 6. Kleine schermen en toegankelijkheid

- Op 360 px (328 px tekenbreedte) past de kaart zonder horizontaal scrollen. Het grootste geval is leerblok 3 met zes taken, waarvan één opengeklapt, plus de verdieping: twee overstappunten, vijf haltes en vier stap-haltes. De afstand tussen haltes schaalt mee. Wordt hij kleiner dan 28 px, dan vervallen de labels behalve die van „hier” en de overstappunten.
- Elke halte heeft als tikvlak een strook: de volle hoogte van de kaart (≥ 44 px) en de breedte tot halverwege de buren. Takken in dezelfde kolom delen de strook in de hoogte. Elk tikvlak is minstens 24 × 24 px (WCAG 2.5.8), en tikvlakken overlappen niet. Elf haltes van 44 × 44 px passen niet op 328 px (leerblok 3 met een opengeklapte taak), dus de kaart wijkt hier af van de 44 × 44 uit DESIGN §4; besluit van de auteur, vastgelegd in B110. De verdieping heeft een eigen smalle kolom tussen haar taak en de volgende, met de halte onder de lijn, zodat ook haar tikvlak een eigen strook is.
- De SVG heeft `role="list"`, elke halte is een `<a>` met `role="listitem"` en een naam als „Taak 3.2, Route B, open”. De huidige halte heeft `aria-current="step"`. Daaronder staat een tekstregel voor wie de SVG niet ziet: „Leerblok 2 · taak 3 van 5 · stap 2 van 4”.
- De focus is zichtbaar met de focusrand van 4 px uit de site. De volgorde bij tabben volgt de lijn van links naar rechts, takken van boven naar beneden.
- Contrast: elke lijnkleur heeft ≥ 3:1 tegen wit (WCAG 1.4.11). Berekend: magenta 4,70, blauw 6,13, groen 5,02, oranje 5,18. De contrastcontrole krijgt de vier tokens erbij.
- Kleur is nooit de enige drager: de stand staat ook in de vorm (gevuld, ring, rand) en in de toegankelijke naam (TG-4). Het leerbloknummer staat in de tekstregel.
- Beweging: alleen het vullen van een halte (200 ms), niet bij `prefers-reduced-motion` (SX-9). Geen harde schaduw (SX-7); de haltes zijn klikbaar, maar een schaduw op een lijn van 6 px is onleesbaar.
- Afdrukken: de kaart staat niet op papier (`print.css`), want werkboek en dossier hebben hun eigen kop.

## 7. Testen

- **Model** (`tests/metro.test.mjs`): voor elk leerblok het juiste aantal taakhaltes; bij het adres van een taak vier stap-haltes en `hier` op de goede stap; route B gekozen in 3.2 geeft tak B vol en tak A gestippeld; niets gekozen geeft beide vol; 4.2 met artikel 2; de mediataak met video; verdieping gedaan en niet gedaan, ook als de verdieping na de laatste taak komt; beginpunt „Start” bij leerblok 1 en „Vorige keer” bij 2–4; eindpunt „Dossier” bij leerblok 4; `laatsteLeerblok` kiest de jongste positie, en zonder positie leerblok 1.
- **Tekening**: op 360 px geen element buiten de viewBox, tikvlakken ≥ 24 × 24 px, kaart ≥ 44 px hoog, tikvlakken zonder overlap; toegankelijke naam en `aria-current`; geen schaduw.
- **Pagina's**: de kaart staat op de zeven studentpagina's en niet op docent, verificatie en controlelab; de segmentbalk is weg; het `aria-label` van SX-4 staat op de kaart.
- **Bestaande controles**: content-check accepteert `spoor` alleen met bestaande stappen en een veld met `opties` die de takken dekken; de contrastcontrole met de vier lijnkleuren; de gewichtscontrole met de extra data op index, dossier en bronnen.

## 8. Buiten scope

- Een netwerkkaart van alle vier lijnen. Wie wil overstappen, gebruikt de overstappunten of het menu Leerblokken.
- De kaart in de docentmodus. Daar zijn onderdelen van het draaiboek de eenheid, geen leerblokken.
- Animatie van een „rijdende” markering tussen haltes.
- Een kaart op de startpagina in plaats van de vier leerblokregels met segmenten (DESIGN §5.2). Die blijven: ze tonen de resultaten per leerblok, de kaart toont de weg.
