---
name: beoordeel-elearning
description: Gebruik wanneer een gebouwde e-learning of leermodule (zoals de hybride e-learning A3 in de repository a3-learning, of elke andere online module) beoordeeld, doorgelicht of geaudit moet worden, niet alleen het ontwerp. Triggers zijn "beoordeel de e-learning", "audit de site", "voldoet de module aan de kritische succesfactoren", "hoe goed is wat we gebouwd hebben", "kwaliteitscheck voor de pilot", of een herbeoordeling na een bouwfase. Combineert de PAMS+KISS-toetsing van beoordeel-onderwijsontwerp met de KSF-audit uit docs/ksfs-e-learning.md (alignment, retrieval, spreiding, feedback, multimedia, toegankelijkheid, AI en privacy). Gebruik dit in plaats van beoordeel-onderwijsontwerp alleen, zodra er iets werkends te doorlopen is.
---

# Beoordeel e-learning

Beoordeelt een **gebouwde** e-learning met twee meetlatten in één rapport:

1. **PAMS + KISS**: de vaste criteria van de auteur, beschreven in de skill
   `beoordeel-onderwijsontwerp`. Ze meten wat team en student ervaren.
2. **De KSF-audit**: 9 domeinen (A t/m I) met de kritische succesfactoren uit
   [docs/ksfs-e-learning.md](../../../docs/ksfs-e-learning.md). Ze meten of de module de
   best onderbouwde leerstrategieën inzet en aan de randvoorwaarden voldoet.

Ze overlappen weinig. PAMS+KISS kan hoog scoren op een module die geen enkele oefenvraag
spreidt, en de KSF-audit kan hoog scoren op een module waar niemand iets te kiezen heeft.
Daarom staan de scores naast elkaar en worden ze **nooit opgeteld of gemiddeld**.

Het oordeel is een **voorstel** aan de ontwerper. Elke score heeft bewijs met een vindplaats,
elke zwakte een concrete verbetering.

## Waarom niet gewoon beoordeel-onderwijsontwerp?

Die skill toetst een ontwerp op papier. Bij een gebouwde site zijn er dingen die alleen te
zien zijn door hem te gebruiken: een controle die een goed antwoord afkeurt, een video zonder
ondertitel, een pagina die op 360 px scrolt. En het blueprint toetst of de site *doet wat de
spec zegt*. Deze skill vraagt of de spec zelf tot een goede module leidt. Beide vragen zijn
nodig; ze vervangen elkaar niet.

## Werkwijze

### 0. Stel vast wat er is

Lees eerst de voortgangslijst in `docs/BUILDPLAN-ELEARNING-A3.md` en `git log` van de
repository. Beoordeel alleen wat gebouwd is. Wat nog niet gebouwd is (bijvoorbeeld media
uit fase 13), krijgt de status **nog niet gebouwd** en telt niet mee in een totaal, zodat de
beoordeling van een volgende fase eerlijk vergelijkbaar blijft. Noteer de fase en de
commit waarop je beoordeelt: de beoordeling hoort bij die stand, net als het verslag bij een
LRD-versie hoort.

Lees daarna het pakket: `docs/LRD-ELEARNING-A3.html` (doel, leeruitkomsten), het BLUEPRINT
(toetsbare regels), het ADR (welke keuzes bewust zijn) en eventuele eerdere beoordelingen in
`docs/`. Een bewuste, beredeneerde keuze in het ADR (bijvoorbeeld geen AI-beoordeling)
drukt een score niet; je noemt hem bij de spanningen.

### 1. Verzamel bewijs aan het echte product

Documenten lezen is niet genoeg: de KSF-audit zelf noemt de walkthrough als student de
belangrijkste bron voor multimedia, navigatie en toegankelijkheid. Zie
[references/bewijs-verzamelen.md](references/bewijs-verzamelen.md) voor de commando's en de
walkthrough. Kort: draai de testpoort van de repository, doorloop de **gepubliceerde** site
met Playwright als student (op 360 px en 1280 px, en met alleen het toetsenbord), en lees de
datafiles in `data/` voor de inhoud.

Houd bij elk bewijsstuk vast **wie het heeft vastgesteld**: een geautomatiseerde test, een
Playwright-doorloop door de beoordelaar, of een mens. Het BUILDPLAN vervangt op veel plekken
de menselijke tester door Playwright; dat is geldig bewijs voor een functie, maar geen bewijs
dat een student het begrijpt (dat is AP-3). Zet dat onderscheid in de verantwoording.

### 2. Scoor PAMS + KISS

Volg de skill `beoordeel-onderwijsontwerp` en lees
[criteria.md](../beoordeel-onderwijsontwerp/criteria.md): dezelfde matrix, dezelfde schaal
(0–3), dezelfde regels voor n.v.t. en bewuste keuzes. Geen eigen criteria erbij, want dan
zijn de scores niet meer naast eerdere beoordelingen te leggen. Twee aanpassingen voor een
gebouwde module:

- Het pakket is nu de **site plus de docentmodus plus de bijbehorende documenten**. „Team"
  is het projectteam dat de student in de werkweek heeft; de e-learning zelf is individueel.
  Werken studenten alleen individueel, dan scoor je het teamniveau op wat de site voor het
  team doet (de Wissel, het dossier per team, docentmodus), en je noemt de keuze.
- KISS · Docent gaat over de docentmodus en de docentgids: kan een collega deel 1 draaien met
  alleen de docentmodus (AP-4)?

### 3. Scoor de KSF-audit

Werk de 9 domeinen af met de criteria in
[references/kwaliteitsfactoren.md](references/kwaliteitsfactoren.md). Daar staat per
criterium wat je aan de gebouwde site kijkt en hoe. Schaal per criterium:

| Score | Label | Betekenis |
|---|---|---|
| 0 | Onvoldoende | Afwezig, of aanwezig maar werkt tegen het leerdoel |
| 1 | Basis | Aanwezig maar inconsistent, of alleen op onderdelen |
| 2 | Goed | Consistent aanwezig in de hele module, met bewijs |
| 3 | Excellent | Goed, plus onderbouwd met data of evaluatie en aantoonbaar verbeterd |

Een 3 kan dus pas na de pilot en een doorlopen verbetercyclus. Verwacht vóór fase 15 geen
3'en; een 2 is dan het plafond, en dat is geen tekortkoming.

Elk criterium heeft een prioriteit (**E** essentieel, **A** aanvullend) en een laag
(**I** input/ontwerp, **P** proces/uitvoering, **O** opbrengst). Beslisregel uit het
onderzoek: de module *voldoet* als alle E-criteria minimaal 2 halen en het gemiddelde over
alle gescoorde criteria ≥ 1,8 is. Vijf punten zijn **knock-out**: A2, D1, D4, G1 t/m G4 en
I1. Scoort een knock-out lager dan 2, dan voldoet de module niet, ook niet bij een hoog
gemiddelde.

**Rapporteer I, P en O apart en nooit als één totaal.** Een site vóór de pilot heeft alleen
een I-score. P en O zijn dan **niet te beoordelen** (geen 0): er zijn nog geen studenten
geweest, geen feedbacktermijnen en geen leerresultaten. Zeg dat expliciet, met de datum
waarop het wel kan (fase 15). Een 0 voor „geen data" zou een ontwerp straffen voor iets wat
niet aan het ontwerp ligt.

Studentevaluaties en tevredenheid zijn procesindicatoren. Behandel ze nooit als bewijs van
leerwinst (H5). Dat is de vraag waar dit onderzoek het meest voor waarschuwt, en de fout die
het snelst gemaakt wordt bij een pilot.

**Checklistdenken vermijden.** Rubrics meten aanwezigheid, niet kwaliteit. Bij elk criterium
schrijf je één zin over *hoe goed* het is, niet alleen dát het er is: een oefenvraag die
alleen reproductie vraagt is aanwezig maar scoort bij D3 laag. Weeg feedbackkwaliteit (D4) en
ICAP (C1) zwaarder dan formele aanwezigheid.

### 4. Kies de drie verbeteringen

Uit beide meetlatten samen: de drie die de meeste punten opleveren tegen de minste moeite,
met de cellen of criteria die vooruitgaan (van → naar) en de moeite (klein, middel, groot)
zoals in `beoordeel-onderwijsontwerp`. Zoek de gemeenschappelijke oorzaak. Wat een
knock-out onder 2 houdt, gaat altijd voor.

### 5. Schrijf het rapport

Acht delen, in deze volgorde. Elk deel is er altijd, ook als de inhoud „niet van toepassing"
is.

1. **Oordeel in het kort**: 3 zinnen. Stand (fase en commit), PAMS+KISS-totaal in de vorm
   „17/42 (40 %)", KSF-uitkomst (voldoet / voldoet niet, met de reden), de ene oorzaak die
   het meest verklaart.
2. **Scorematrix PAMS+KISS**: in de vorm van `beoordeel-onderwijsontwerp`.
3. **KSF-scorekaart**: één tabel per domein met ID · score · prio · laag · bewijs met
   vindplaats · wie het vaststelde. Daaronder de drie deelscores I / P / O en de knock-outs.
4. **Per criterium (PAMS+KISS)**: zoals in `beoordeel-onderwijsontwerp` (wat werkt, met
   bewijs, dan **Zwak:** met de verbetering).
5. **Spanningen**: waar criteria botsen en welke kant het ontwerp kiest. Typische botsingen:
   keuzevrijheid (Autonomy) tegen alignment (A2); eenvoud (KISS) tegen gespreide ophaaloefening
   (D2); een alleen-lokaal dossier zonder server (privacy) tegen learning analytics (H2).
   Bewuste exclusies uit het BLUEPRINT (§8) noem je hier, zodat de lezer ziet dat het geen
   vergissing is.
6. **Top 3 verbeteringen**.
7. **Niet slopen**: wat sterk is en een herziening moet overleven.
8. **Verantwoording**: wat niet te beoordelen was en waarom, per bewijsstuk wie het
   vaststelde (test, beoordelaar met Playwright, mens), dat de scores van één beoordelaar
   komen (de kalibratieronde uit het onderzoek ontbreekt dus), en bij een vorige beoordeling
   de oude en nieuwe scores naast elkaar. Vermeld ook welke criteria uit het onderzoek je
   liet vervallen omdat het product ze bewust niet heeft, met verwijzing naar het BLUEPRINT.

Sla het rapport op als `docs/beoordeling-elearning-a3-<stand>.html` (bijvoorbeeld
`-fase12`), in de opzet van `docs/beoordeling-lrd-elearning-a3.html`, met de HAN-huisstijl
en de printstijl uit CLAUDE.md. Geef de gebruiker in het gesprek de korte versie (delen 1 en 6).
Laat de Nederlandse tekst vóór oplevering langs de skills `redigeer-nederlandse-tekst` en
`schrap-ai-taal` gaan.

## Grenzen

- Je scoort de module, niet de studenten, en je beoordeelt niet de betrouwbaarheid van
  het onderzoek zelf. Het onderzoek waarschuwt zelf dat effectgroottes gemiddelden met grote
  spreiding zijn; gebruik ze als richting.
- Juridische criteria (G, I4, I5) zijn een technische toets, geen juridisch oordeel.
  Zeg dat in de verantwoording en verwijs naar de juridische afdeling voor de definitieve
  lezing (het onderzoek noemt dat zelf bij de EAA en het Bdto).
- Verandert het BLUEPRINT of het onderzoek, dan hoort deze skill mee te veranderen: de
  criteria staan in `references/kwaliteitsfactoren.md`, niet in de tekst hierboven.
