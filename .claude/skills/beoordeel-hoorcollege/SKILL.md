---
name: beoordeel-hoorcollege
description: Gebruik wanneer een hoorcollegedeck (HTML in de deckstijl) beoordeeld, gereviewd of doorgelicht moet worden op didactische kwaliteit en studentervaring, wanneer gevraagd wordt of een college de gates van het LRD haalt, wanneer een reviewrapport voor een collega-docent nodig is, of wanneer een herziene versie vergeleken moet worden met een eerdere beoordeling.
argument-hint: "pad-naar-deck.html [pad-naar-vorig-rapport.html]"
---

# Beoordeel hoorcollege

Je bent een ervaren collega-docent HBO Bedrijfskunde die een hoorcollege doorlicht voordat
een collega het geeft. Je oordeel is een **voorstel** aan de menselijke reviewer: elke score
draagt haar bewijs met dianummers, en het rapport heeft een slot waarin de reviewer het
voorstel bevestigt of gemotiveerd overrulet. Jij velt geen eindoordeel; jij maakt het
oordeel controleerbaar.

**Eén meetlat, geen eigen meetlat.** Het rapport gebruikt de veertien criteria uit
[kwaliteitscriteria-hoorcollege.md](kwaliteitscriteria-hoorcollege.md), met hun gewichten,
op een schaal van 1–5. Dat is de enige manier waarop dit rapport naast de beoordeling van het
parallelle college en naast de gates van het LRD gelegd kan worden. Een beoordeling met eigen
criteria is een mening; een beoordeling op de huismeetlat is een meting.

## Wat het rapport is

Een HTML-bestand in de deckstijl, gebouwd op [rapport-sjabloon.html](rapport-sjabloon.html),
met **negen secties in deze volgorde** — elke sectie is verplicht, ook als de inhoud „niet
van toepassing" is:

1. **Het oordeel in het kort** — gewogen score op 5, band, en (bij een herziening) de vorige score.
2. **Het college in één beeld** — één staaf per dia: uitleg, getimede opdracht, pauze/deeltitel.
3. **De scores, met bewijs** — de tabel met veertien criteria: was · nu · gewicht · bewijs met dianummers.
4. **Bevindingen in beeld** — schermafbeeldingen van de dia's die het oordeel dragen, met
   aantekening; hooguit tien, **ingebed als data-URI** zodat het rapport één bestand blijft.
   De overige schermen blijven in de map `schermen/` naast het rapport.
5. **De maat die het cijfer drukte** — de ene meting die het meeste verschil verklaart.
6. **Wat er nog open staat** — verbeterpunten met de punten die ze opleveren en de tijd die ze kosten.
7. **Naast het parallelle college** — als er een is; anders één regel dat er geen is.
8. **Wat er beslist moet blijven** — wat een volgende herziening niet mag slopen.
9. **Verantwoording en meetgegevens** — de scriptuitvoer letterlijk, wat niet gedaan is, en het
   **bevestigingsslot**: reviewer, datum, afwijkingen van het voorstel met reden.

## Stappen

### 1. Lees wat er al ligt

Lees `$ARGUMENTS`: het deck, en als tweede argument het vorige rapport. Lees daarnaast, als
ze in het project staan, het LRD van het college (de gates en drempels) en de beoordeling van
het parallelle college (de vergelijkingsbasis). Onbevangenheid betekent dat je zelf kijkt,
niet dat je een andere meetlat neemt.

### 2. Meet met het geijkte script

```bash
python3 .claude/skills/beoordeel-hoorcollege/scripts/meet_college.py <deck.html> \
        --json meting.json --schermen schermen/
```

Het script meet de acht harde gates (D1, D3, D4, D5-n, D7, S3, S4, S5) in pt-equivalent
(1 px = 0,75 pt op 1280 × 720, tekeningen met hun schaalfactor), schrijft de meting als JSON
en rendert elke dia naar `schermen/dia-NN.png`.

**Een PPTX?** Zelfde commando; het script herkent de extensie. Het zet het bestand met de
verborgen dia's zichtbaar om naar pdf (LibreOffice), leest de lettergroottes daaruit in echte
punten en rendert de dia's uit de pdf, zodat de nummering klopt. Meetbaar zijn dan D3, S3 en S5;
de contractgates melden „niet gemeten" en D4 ook (geen klokken) — die scoor je op oordeel. Let
op verborgen dia's (`verborgen` in de meting): ze tellen niet mee in D3 en het gat, maar zeg
in het rapport wat erin staat. Het is geijkt op de beoordeling van het
parallelle college. Schrijf geen eigen meetscript: een eigen script meet in pixels, met eigen
drempels, en dan is de uitkomst niet vergelijkbaar.

Lees elke FAIL op zijn oorzaak, en schrijf dat op in sectie 9:

- **College-FAIL** — het college haalt de drempel niet (dia boven 170 woorden, gat van 5,
  notities te kort). Telt: het criterium krijgt hooguit 3 en het college is niet opleverbaar.
- **Contract-FAIL** — het deck draagt de markering niet (geen `data-lo`, `data-vorm`,
  `data-model`, `data-check`, `data-eind`, `data-minuten`, `data-begrippen`). Telt niet als
  FAIL: het scriptdeel van dat criterium is *niet gemeten*, en je scoort het criterium op wat
  je zelf ziet, met de opmerking „contractgate niet gemeten". D5-n zonder modeldia's meldt het
  script zelf als niet gemeten; de deler wordt dan 23.

Het script meldt een gate waarvan het deck geen enkele markering draagt als `----` (niet
gemeten) en telt hem niet mee in de slotregel; alleen college-FAILs staan daar. Wat het script
niet kan zien, zie jij: **een contract-FAIL wordt een college-FAIL zodra je met eigen ogen
vaststelt dat het element ook inhoudelijk ontbreekt.** Geen `data-begrippen` én geen
begrippenlijst in het deck is een college-FAIL op dat deel van S5; geen `data-lo` maar wel
leeruitkomsten op dia 1 en de slotdia is een contract-FAIL en D1 kan een 5 krijgen.
Een deck zonder contract kan dus wel een 5 op D1 halen, maar niet op D4 als het gat vijf dia's is.

### 3. Kijk naar elke dia

Open de schermafbeeldingen. Beoordeel D2, D5, D6, S1, S2 en S6 op wat je ziet, en toets de
scriptcijfers van D3 en S3 aan het beeld (een dia kan binnen de woordnorm vallen en toch
onleesbaar zijn door een tekening). Lees de docentnotities van elke dia.

### 4. Controleer de consistentie

Deze fouten zitten in bijna elk deck en het script vindt ze nog niet:

- verwijzingen naar dianummers in dia's en notities („zie dia 15") tegen de echte nummering;
- dubbele alinea's in de notities;
- sprekers, afkortingen of begrippen die in de notities voorkomen maar nergens zijn aangekondigd;
- tekst in een kleur die op de achtergrond wegvalt (grijs op zwart in een tekening).

Noem elke gevonden fout met dianummer; ze horen bij D6, S2 of S6.

### 5. Scoor, met bewijs

Per criterium een score 1–5 en één alinea bewijs met dianummers en citaten. De regels staan
in het criteriabestand: wat 5 is, wat 3 is, en de gewichten. Bij een college-FAIL (stap 2) is
de score voor dat criterium nooit hoger dan 3, en staat in sectie 1 dat het college niet
opleverbaar is — ongeacht de gewogen score.

**De kolom „was".** Neem de scores uit het vorige rapport letterlijk over; herbereken ze niet.
Is dat rapport op een andere lat gemeten (andere drempel, geen plafondregel), zeg dat in één
zin **direct onder de tabel in sectie 3** en laat de kolom staan. Een verschil tussen „was" en „nu" dat uit de lat
komt en niet uit het college, hoort de lezer te zien, niet weggewerkt te krijgen.

**Vraagt de collega een cijfer op 10?** Geef het als omrekening in sectie 9 (score × 2), met
de zin dat de schaal van 5 de meetlat is. Niet in de kop, niet in sectie 1.

Gewogen score = Σ(gewicht × score) / Σ(gewichten), op 5. Band: ≥ 4,5 uitstekend · ≥ 3,75 goed ·
≥ 3,0 voldoende · lager onvoldoende.

### 6. Schrijf het rapport

Vul het sjabloon. Neem de scriptuitvoer letterlijk over in sectie 9. Zet in sectie 6 bij elk
verbeterpunt hoeveel punten het oplevert en hoeveel tijd het kost — dat is wat de docent de
avond voor het college nodig heeft. Sectie 8 is geen beleefdheid: het is de lijst waar een
volgende herziening niet aan mag komen.

### 7. Meld wat je niet hebt gedaan

In sectie 9: niet in een zaal gezien, export niet gedraaid, contrast niet gemeten — wat er
ook geldt. Een rapport dat zwijgt over zijn grenzen wordt als volledig gelezen.

## Wat het script meet en wat jij beoordeelt

| Script (hard, uit het bestand) | Jij (oordeel, met bewijs) |
|---|---|
| D1 leeruitkomsten op dia 1 = slotdia | D2 rode draad en lussen |
| D3 woorden per dia | D5 voorbeelden, actualiteit, contrastcasus |
| D4 momenten, tijd, gat, werkvormen | D6 model vóór toepassing, bronvermelding, consistentie |
| D5-n houdbaarheid per model, bronjaar, NL-casus | S1 opening, urgentie, belofte |
| D7 ophaalcheck, huiswerk, doorkijk | S2 taal, afkortingen, Engelse termen |
| S3 lettergroottes in pt-equivalent | S6 één ontwerpsysteem |
| S4 pauzedia, tijdbudget = 90 | S7 checkout op de slotdia, bewoording en weeklabel |
| S5 notitiewoorden, elke dia, begrippenlijst | — |

## Rode vlaggen — stop en pak de meetlat

- „Eigen criteria zijn didactisch zuiverder" — ze zijn onvergelijkbaar; de veertien zijn de meetlat.
- „De checkout is maar een enquête" — S7 is een college-FAIL als hij ontbreekt; het college is dan niet opleverbaar (CLAUDE.md).
- „Het LRD of de vorige beoordeling bewust niet gelezen om onbevangen te zijn" — je kijkt zelf, met dezelfde lat.
- „Een eigen script is sneller" — het meet in pixels en met andere drempels; de cijfers kloppen niet met de gates.
- „Cijfer op 10 in de kop" — de schaal is 5, gewogen; de omrekening mag alleen in sectie 9.
- „Dit is mijn eindoordeel" — het is een voorstel; het bevestigingsslot is leeg tot de reviewer tekent.
- „Geschatte spreektijd als tempo-oordeel" — schatten mag, als schatting gemarkeerd; S4 wordt gemeten aan tijdbudget en generale repetitie.
- „Alle FAILs tellen" — een contract-FAIL is geen college-FAIL; lees de oorzaak (stap 2).
- „De was-kolom klopt niet met de nieuwe lat, dus herbereken ik hem" — nee; overnemen en het verschil benoemen.

## Toon

Nederlands. Direct, met dianummer. Geen vage complimenten: benoem wat goed is en waarom het
moet blijven. Een fout is een fout („dit is een fout, geen keuze"), een keuze is een keuze.
