# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Wat dit is

Geen softwareproject maar een werkmap voor onderwijsontwerp: het C-cluster (HBO Bedrijfskunde, HAN), Praktijkopdracht 5, studiejaar 2026-27. Er is geen build, lint of testcommando. Uitvoer zijn zelfstandige HTML-documenten (werkboeken, draaiboeken, decks, LRD's), Markdown-ontwerpen en pdf's. Taal van alle documenten: Nederlands. Bij het hernoemen of verplaatsen van bestanden moeten verwijzingen in andere documenten mee (zoek met grep).

## Indeling

- `WK4/`, `WK5/`: lesmateriaal per onderwijsweek (werkboek, draaiboek, docentinstructie, slides, ontwerp-`.md`). `WK5/overzicht-weekprogramma.md` is het startpunt voor week 5; `WK5/ontwerp-woensdag-A3-start.md` is het ontwerp van dag 2.
- `docs/`: ontwerpdocumenten over meerdere weken heen (zie hieronder) en `overzicht-leeruitkomsten.*`, de samenvatting van de vijf LUK en de beoordelingscriteria (BC) van het C-cluster.
- `lits/`: literatuur en afbeeldingen van derden. Staat in `.gitignore` en wordt niet gepubliceerd; kopieer er geen tekst of afbeeldingen uit in documenten die openbaar kunnen worden.
- `.claude/skills/`: projectskills. Gebruik `beoordeel-onderwijsontwerp` voor toetsing van ontwerpen, `beoordeel-elearning` voor de gebouwde e-learning (PAMS+KISS plus de KSF-audit uit `docs/ksfs-e-learning.md`), `beoordeel-hoorcollege` en `ontwerp-dia` voor decks, en `redigeer-nederlandse-tekst` en `schrap-ai-taal` voordat Nederlandse tekst naar lezers gaat.

`.gitignore` sluit ook uit: `WK*/PhoneVentures*`, `WK*/*.pptx`, `*.docx`, `*.odt`, `*Copy.pdf` (materiaal van derden of van Brightspace) en `archief/`.

## LRD, ADR en BLUEPRINT van een product

Per product staan drie documenten altijd bij elkaar in `docs/` (plus BUILDPLAN en eventueel DESIGN), met bestandsnamen in hoofdletters (extensie klein): `LRD-<PRODUCT>.html`, `ADR-<PRODUCT>.md`, `BLUEPRINT-<PRODUCT>.md`. Nu bestaat dit voor de hybride e-learning A3 (`-ELEARNING-A3`); de site zelf komt in een aparte repository, `hanbedrijfskunde/a3-learning`. Elk document heeft één rol; zet niets in het verkeerde:

- **LRD** beschrijft het ontwerp (pedagogiek, eisen FR-/NFR-, acceptatiecriteria AC-, risico's, roadmap). Het versienummer staat in de kop; verhoog het bij elke ontwerpronde.
- **ADR** is het besluitenregister (B1, B2, …). Alleen onderaan toevoegen, nooit regels verwijderen; een vervangen besluit blijft staan met in de statuskolom het besluit dat het vervangt. Nummers zijn stabiel omdat andere documenten ernaar verwijzen.
- **BLUEPRINT** is de doelsituatie in genummerde, toetsbare regels (prefix per onderwerp, Must/Should/Could, criterium met getal en eenheid, verificatiemethode). Geen bouwvolgorde, fasering of voortgang erin; die horen in `BUILDPLAN-<PRODUCT>.md` (bestaat nog niet). Bijlage A koppelt LRD-eisen aan blueprintregels; werk die bij als een LRD-eis verandert. Gebruik hiervoor de skill `blueprint-and-buildplan`.
- **DESIGN** (`DESIGN-<PRODUCT>.md`, optioneel) is de ontwerprichtlijn voor de gebruikerskant: tokens, schermen, componenten, taal. Geen regel-ID's; het toetsbare deel staat als regels in het BLUEPRINT (voor de e-learning: SX-*), en bij verschil gaat het BLUEPRINT voor.

Ontwerpen worden getoetst aan de vaste criteria van de auteur: Purpose, Autonomy, Mastery, Social (PAMS) en KISS, waarbij KISS pas telt als het afgewezen alternatief genoemd is. Ruimte voor verschillen is een subcriterium van Autonomy. Het beoordelingsverslag staat in `docs/beoordeling-lrd-elearning-a3.html` en hoort bij een bepaalde LRD-versie.

## Stijl van de HTML-documenten

Zelfstandige bestanden met inline CSS, zonder externe scripts of lettertypen. HAN-huisstijl: accent `#E50056`, zwart en wit, dikke zwarte randen met harde schaduw. Nieuwe documenten volgen de opzet van een bestaand zusterdocument, bijvoorbeeld `docs/LRD-ELEARNING-A3.html` (houd de printstijl intact: werkboeken en draaiboeken worden ook als pdf gebruikt).
