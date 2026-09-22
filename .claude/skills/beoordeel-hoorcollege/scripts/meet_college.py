#!/usr/bin/env python3
"""
Meet een hoorcollegedeck tegen de script-gates uit het LRD (Deel 6.2).

Het deck volgt het deckcontract (LRD 6.1): één HTML-bestand met
<section class="slide" data-part data-title>, per dia een <div class="notes">,
opdrachtblokken <div class="socratic"> met een <span class="clock"> en een
data-vorm, en data-attributen voor leeruitkomsten (data-lo), modeldia's
(data-model / data-houdbaarheid / data-bronjaar), casus (data-casus="nl"),
ophaalcheck (data-check), huiswerk (data-huiswerk), doorkijk (data-doorkijk),
pauze (data-eind), tijdbudget (data-minuten) en begrippenlijst (data-begrippen).

Gebruik:  python3 .claude/skills/beoordeel-hoorcollege/scripts/meet_college.py <deck.html>\n              [--json pad] [--schermen map] [--jaar 2026] [--zonder-render]

De drempels zijn die van LRD 6.2 — startdoelen uit de beoordeling van het
voorbeeldcollege, te kalibreren op de eerste eigen meting (roadmap stap 6).
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

from bs4 import BeautifulSoup

# --------------------------------------------------------------------------
# drempels (LRD 6.2)
# --------------------------------------------------------------------------

LEERUITKOMSTEN = [f"LO{i}" for i in range(1, 8)]
OORDELEN = {"blijft", "verschuift", "afscheid"}
D3_GEMIDDELD, D3_MAX = 110, 170
D4_MOMENTEN, D4_AANDEEL, D4_GAT, D4_VORMEN, D4_MIN, D4_MAX = 10, 0.35, 4, 4, 15 * 60, 20 * 60
D5_BRON_JAREN = 3
S4_MINUTEN = 90
S5_NOTITIES = 3000
S3_KLEIN_MAX, S3_GROOT_MIN = 30, 28   # % woorden < 14 pt, % woorden ≥ 18 pt
PX_NAAR_PT = 0.75                    # 1280 px = 13,33 inch = een standaarddia

# --------------------------------------------------------------------------
# klok: "60 seconden", "2 minuten", "3 min", "45 sec", "0,5 min"
# --------------------------------------------------------------------------

_KLOK = re.compile(r"(\d+(?:[.,]\d+)?)\s*(seconden|seconde|sec|s|minuten|minuut|min|m)\b", re.I)


def klok_seconden(tekst: str) -> float | None:
    m = _KLOK.search(tekst)
    if not m:
        return None
    getal = float(m.group(1).replace(",", "."))
    return getal * 60 if m.group(2).lower().startswith("m") else getal


# --------------------------------------------------------------------------
# het deck
# --------------------------------------------------------------------------

@dataclass
class Moment:
    seconden: float
    vorm: str | None


@dataclass
class Dia:
    nummer: int
    titel: str
    deel: str
    woorden: int
    notitie_woorden: int
    momenten: list[Moment] = field(default_factory=list)
    lo: set[str] = field(default_factory=set)
    attrs: dict[str, str] = field(default_factory=dict)
    verborgen: bool = False      # pptx: niet geprojecteerd; telt niet mee in D3/D4

    def heeft(self, attr: str) -> bool:
        return f"data-{attr}" in self.attrs


@dataclass
class Deck:
    dias: list[Dia]


@dataclass
class Gate:
    code: str
    ok: bool
    waarde: str
    drempel: str
    gemeten: bool = True


def _woorden(tekst: str) -> int:
    return len(tekst.split())


def lees_deck(html: str) -> Deck:
    soup = BeautifulSoup(html, "lxml")
    dias: list[Dia] = []
    for i, sec in enumerate(soup.select("section.slide"), 1):
        notities = sec.select("div.notes")
        notitie_woorden = sum(_woorden(n.get_text(" ")) for n in notities)
        for n in notities:
            n.decompose()
        momenten = []
        for blok in sec.select(".socratic"):
            klok = blok.select_one(".clock")
            seconden = klok_seconden(klok.get_text(" ")) if klok else None
            if seconden is not None:
                momenten.append(Moment(seconden, blok.get("data-vorm")))
        dias.append(Dia(
            nummer=i,
            titel=sec.get("data-title", ""),
            deel=sec.get("data-part", ""),
            woorden=_woorden(sec.get_text(" ")),
            notitie_woorden=notitie_woorden,
            momenten=momenten,
            lo={el["data-lo"] for el in sec.select("[data-lo]")},
            attrs={k: v for k, v in sec.attrs.items() if k.startswith("data-")},
        ))
    return Deck(dias)


# --------------------------------------------------------------------------
# pptx-route: zelfde Deck, ander bestand. Geen deckcontract mogelijk, dus
# alleen D3, S3 en S5 zijn meetbaar; de rest meldt het script als niet gemeten.
# --------------------------------------------------------------------------

_A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
_P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
_VOETTEKST = {"sldNum", "ftr", "dt"}


def _pptx_dias(z):
    import re
    namen = [n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)]
    return sorted(namen, key=lambda n: int(re.search(r"(\d+)\.xml", n).group(1)))


def _smartart_tekst(z, dianaam: str) -> str:
    """SmartArt staat niet in de dia-XML maar in ppt/diagrams/dataN.xml, bereikbaar
    via de rels van de dia. Wie alleen de dia leest, mist die tekst — en dat kostte de
    beoordeling van 28 aug 2026 eerst een heel criterium."""
    import posixpath
    import re
    from xml.etree import ElementTree as ET
    rels = f"ppt/slides/_rels/{dianaam.split('/')[-1]}.rels"
    if rels not in z.namelist():
        return ""
    doelen = re.findall(r'Target="([^"]+diagrams/data\d+\.xml)"', z.read(rels).decode("utf8", "ignore"))
    stukken = []
    for doel in doelen:
        pad = posixpath.normpath(posixpath.join("ppt/slides", doel))
        if pad in z.namelist():
            stukken.append(" ".join(t.text.strip() for t in ET.fromstring(z.read(pad)).iter(_A + "t") if t.text and t.text.strip()))
    return " ".join(stukken)


def lees_pptx_tekst(pad: Path, nummer: int) -> str:
    """Alle getoonde tekst van één dia (vormen én SmartArt), zonder voettekstvelden."""
    import zipfile
    from xml.etree import ElementTree as ET
    z = zipfile.ZipFile(pad)
    naam = _pptx_dias(z)[nummer - 1]
    root = ET.fromstring(z.read(naam))
    delen = []
    for sp in root.iter(_P + "sp"):
        ph = sp.find(f"{_P}nvSpPr/{_P}nvPr/{_P}ph")
        if ph is not None and ph.get("type") in _VOETTEKST:
            continue
        delen.append(" ".join(t.text.strip() for t in sp.iter(_A + "t") if t.text and t.text.strip()))
    delen.append(_smartart_tekst(z, naam))
    return " ".join(d for d in delen if d)


def lees_pptx(pad: Path) -> Deck:
    import re
    import zipfile
    from xml.etree import ElementTree as ET
    z = zipfile.ZipFile(pad)
    notities = {int(re.search(r"(\d+)\.xml", n).group(1)): n
                for n in z.namelist() if re.match(r"ppt/notesSlides/notesSlide\d+\.xml$", n)}
    dias: list[Dia] = []
    for i, naam in enumerate(_pptx_dias(z), 1):
        xml = z.read(naam)
        root = ET.fromstring(xml)
        woorden, titel = 0, ""
        for sp in root.iter(_P + "sp"):
            ph = sp.find(f"{_P}nvSpPr/{_P}nvPr/{_P}ph")
            soort = ph.get("type", "body") if ph is not None else "body"
            if soort in _VOETTEKST:
                continue
            tekst = " ".join(t.text.strip() for t in sp.iter(_A + "t") if t.text and t.text.strip())
            if soort in ("title", "ctrTitle") and not titel:
                titel = tekst
            woorden += _woorden(tekst)
        woorden += _woorden(_smartart_tekst(z, naam))
        if not titel:
            titel = next((t.text.strip() for t in root.iter(_A + "t") if t.text and t.text.strip()), "")
        nw = 0
        if i in notities:
            nroot = ET.fromstring(z.read(notities[i]))
            for sp in nroot.iter(_P + "sp"):
                ph = sp.find(f"{_P}nvSpPr/{_P}nvPr/{_P}ph")
                if ph is not None and ph.get("type") in _VOETTEKST:
                    continue
                nw += _woorden(" ".join(t.text or "" for t in sp.iter(_A + "t")))
        dias.append(Dia(nummer=i, titel=titel, deel="", woorden=woorden, notitie_woorden=nw,
                        verborgen=bool(re.search(rb'<p:sld[^>]*\sshow="0"', xml))))
    return Deck(dias)


def _pptx_naar_pdf(pad: Path, werkmap: Path) -> Path:
    """Kopie zonder verborgen dia's-vlag, geconverteerd met LibreOffice; zo houdt
    de pdf dezelfde nummering als het deck."""
    import re
    import shutil
    import subprocess
    import zipfile
    werkmap = Path(werkmap)
    werkmap.mkdir(parents=True, exist_ok=True)
    kopie = werkmap / "deck.pptx"
    with zipfile.ZipFile(pad) as bron, zipfile.ZipFile(kopie, "w", zipfile.ZIP_DEFLATED) as doel:
        for item in bron.infolist():
            data = bron.read(item.filename)
            if re.match(r"ppt/slides/slide\d+\.xml$", item.filename):
                data = re.sub(rb'(<p:sld\b[^>]*?)\sshow="0"', rb"\1", data)
            doel.writestr(item, data)
    soffice = shutil.which("soffice") or "/Applications/LibreOffice.app/Contents/MacOS/soffice"
    subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", str(werkmap), str(kopie)],
                   check=True, capture_output=True, timeout=300)
    return werkmap / "deck.pdf"


def meet_lettergroottes_pptx(pad: Path, werkmap: Path) -> dict[str, float]:
    """Zoals meet_lettergroottes, maar uit de pdf: daar staan de groottes al in punten
    (de dia is 13,33 inch breed, net als het HTML-deck)."""
    import fitz
    pdf = _pptx_naar_pdf(pad, werkmap)
    verborgen = {d.nummer for d in lees_pptx(pad).dias if d.verborgen}
    b = {"klein": 0, "midden": 0, "groot": 0}
    doc = fitz.open(pdf)
    for i, pagina in enumerate(doc, 1):
        if i in verborgen:
            continue
        for blok in pagina.get_text("dict")["blocks"]:
            for regel in blok.get("lines", []):
                for span in regel["spans"]:
                    w = _woorden(span["text"])
                    pt = span["size"]
                    b["klein" if pt < 14 else "midden" if pt < 18 else "groot"] += w
    totaal = sum(b.values()) or 1
    return {"<14": round(100 * b["klein"] / totaal, 1),
            "14-18": round(100 * b["midden"] / totaal, 1),
            ">=18": round(100 * b["groot"] / totaal, 1)}


def maak_schermen_pptx(pad: Path, map_: Path) -> list[Path]:
    import fitz
    map_ = Path(map_)
    pdf = _pptx_naar_pdf(pad, map_)
    paden = []
    for i, pagina in enumerate(fitz.open(pdf), 1):
        doel = map_ / f"dia-{i:02d}.png"
        pagina.get_pixmap(dpi=96).save(doel)
        paden.append(doel)
    return paden


def lees_modellen(pad: Path) -> list[str]:
    """De paragraafnummers (niveau 2) uit inhoudsopgave.json — één modeldia per stuk.
    Geen bestand (ander vak, ander project): lege lijst, en D5-n wordt niet gemeten."""
    if not Path(pad).exists():
        return []
    data = json.loads(Path(pad).read_text(encoding="utf-8"))
    return [h["nummer"] for h in data["hoofdstukken"] if h["niveau"] == 2]


def langste_gat(dias: list[Dia]) -> int:
    """Langste reeks opeenvolgende dia's zonder getimed moment."""
    langste = huidig = 0
    for d in (x for x in dias if not x.verborgen):
        huidig = 0 if d.momenten else huidig + 1
        langste = max(langste, huidig)
    return langste


# --------------------------------------------------------------------------
# de gates
# --------------------------------------------------------------------------

def gate_d1(deck: Deck) -> Gate:
    if not any(d.lo for d in deck.dias):
        return Gate("D1", False, "leeruitkomsten niet gemarkeerd (data-lo); gate niet gemeten", "7/7 op dia 1 = slotdia", gemeten=False)
    eerste, laatste = deck.dias[0].lo, deck.dias[-1].lo
    verwacht = set(LEERUITKOMSTEN)
    ok = eerste == verwacht and laatste == verwacht
    return Gate("D1", ok, f"{len(eerste & verwacht)}/7" + ("" if eerste == laatste else " · slotdia wijkt af"), "7/7 op dia 1 = slotdia")


def gate_d3(deck: Deck) -> Gate:
    getoond = [d for d in deck.dias if not d.verborgen] or deck.dias
    gem = sum(d.woorden for d in getoond) / len(getoond)
    zwaarste = max(getoond, key=lambda d: d.woorden)
    ok = gem <= D3_GEMIDDELD and zwaarste.woorden <= D3_MAX
    return Gate("D3", ok, f"gem. {gem:.0f} w/dia · max {zwaarste.woorden} (dia {zwaarste.nummer})", f"≤{D3_GEMIDDELD} gem. · ≤{D3_MAX} max")


def gate_d4(deck: Deck) -> Gate:
    momenten = [m for d in deck.dias for m in d.momenten]
    if not momenten:
        return Gate("D4", False, "geen opdrachtblokken met klok (.socratic/.clock); gate niet gemeten",
                    f"≥{D4_MOMENTEN} · ≥{D4_AANDEEL:.0%} · gat ≤{D4_GAT} · ≥{D4_VORMEN} vormen · {D4_MIN // 60}–{D4_MAX // 60} min", gemeten=False)
    dias_met = sum(1 for d in deck.dias if d.momenten)
    aandeel = dias_met / len(deck.dias)
    gat = langste_gat(deck.dias)
    vormen = {m.vorm for m in momenten if m.vorm}
    vormen_gemarkeerd = bool(vormen)
    totaal = sum(m.seconden for m in momenten)
    ok = (len(momenten) >= D4_MOMENTEN and aandeel >= D4_AANDEEL and gat <= D4_GAT
          and (len(vormen) >= D4_VORMEN or not vormen_gemarkeerd) and D4_MIN <= totaal <= D4_MAX)
    vormtekst = f"{len(vormen)} vormen" if vormen_gemarkeerd else "vormen niet gemarkeerd (data-vorm)"
    waarde = (f"{len(momenten)} momenten · {aandeel:.0%} dia's · gat {gat} · "
              f"{vormtekst} · {totaal / 60:g} min")
    return Gate("D4", ok, waarde, f"≥{D4_MOMENTEN} · ≥{D4_AANDEEL:.0%} · gat ≤{D4_GAT} · ≥{D4_VORMEN} vormen · {D4_MIN // 60}–{D4_MAX // 60} min")


def gate_d5n(deck: Deck, modellen: list[str], jaar: int) -> Gate:
    per_model = {d.attrs.get("data-model"): d for d in deck.dias if d.heeft("model")}
    if not modellen:
        return Gate("D5n", False, "geen modellenlijst (inhoudsopgave.json); gate niet gemeten",
                    "modeldia per syllabusbron · bron ≤ 3 jaar · NL-casus", gemeten=False)
    if not per_model:
        # geen enkele modeldia: een deck zonder deckcontract of van een ander vak —
        # dan is "alle modellen ontbreken" ruis, geen bevinding
        return Gate("D5n", False, "geen modeldia's (data-model); gate niet gemeten",
                    f"{len(modellen)}/{len(modellen)} met oordeel · bron ≥ {jaar - D5_BRON_JAREN} · NL-casus", gemeten=False)
    fouten = []
    for m in modellen:
        d = per_model.get(m)
        if d is None:
            fouten.append(f"{m} ontbreekt")
            continue
        if d.attrs.get("data-houdbaarheid") not in OORDELEN:
            fouten.append(f"{m} zonder oordeel")
        try:
            if int(d.attrs.get("data-bronjaar", "0")) < jaar - D5_BRON_JAREN:
                fouten.append(f"{m} bron {d.attrs.get('data-bronjaar')}")
        except ValueError:
            fouten.append(f"{m} bronjaar onleesbaar")
    nl = any(d.attrs.get("data-casus") == "nl" for d in deck.dias)
    if not nl:
        fouten.append("geen NL-casus")
    goed = len(modellen) - sum(1 for f in fouten if f.split()[0] in modellen)
    waarde = f"{goed}/{len(modellen)} modellen · NL-casus: {'ja' if nl else 'nee'}"
    if fouten:
        waarde += " · " + ", ".join(fouten)
    return Gate("D5n", not fouten, waarde, f"{len(modellen)}/{len(modellen)} met oordeel · bron ≥ {jaar - D5_BRON_JAREN} · NL-casus")


def gate_d7(deck: Deck) -> Gate:
    if not any(d.heeft("check") or d.heeft("huiswerk") or d.heeft("doorkijk") for d in deck.dias):
        return Gate("D7", False, "afsluiting niet gemarkeerd (data-check/huiswerk/doorkijk); gate niet gemeten",
                    "ophaalcheck, huiswerk en doorkijk op de laatste drie dia's", gemeten=False)
    staart = deck.dias[-3:]
    delen = {"ophaalcheck": any(d.heeft("check") for d in staart),
             "huiswerk": any(d.heeft("huiswerk") for d in staart),
             "doorkijk": any(d.heeft("doorkijk") for d in staart)}
    ok = all(delen.values())
    waarde = " · ".join(f"{k}: {'ja' if v else 'nee'}" for k, v in delen.items())
    return Gate("D7", ok, waarde, "ophaalcheck, huiswerk en doorkijk op de laatste drie dia's")


def gate_s4(deck: Deck) -> Gate:
    if not any(d.heeft("minuten") or d.heeft("eind") for d in deck.dias):
        return Gate("S4", False, "tijdbudget en pauze niet gemarkeerd (data-minuten/data-eind); gate niet gemeten",
                    f"pauzedia met eindtijd · blokken = {S4_MINUTEN} min", gemeten=False)
    pauzes = [d for d in deck.dias if d.deel.lower() == "pauze"]
    eind = next((d.attrs["data-eind"] for d in pauzes if d.heeft("eind")), None)
    minuten = sum(float(d.attrs["data-minuten"]) for d in deck.dias if d.heeft("minuten"))
    ok = eind is not None and minuten == S4_MINUTEN
    return Gate("S4", ok, f"pauze {eind or 'zonder eindtijd'} · blokken {minuten:g}/{S4_MINUTEN} min", f"pauzedia met eindtijd · blokken = {S4_MINUTEN} min")


def gate_s5(deck: Deck) -> Gate:
    totaal = sum(d.notitie_woorden for d in deck.dias)
    zonder = [d.nummer for d in deck.dias if d.notitie_woorden == 0]
    begrippen = any(d.heeft("begrippen") for d in deck.dias)
    # zonder markering kan het script niet zien of er een begrippenlijst is; dat ziet de reviewer
    ok = totaal >= S5_NOTITIES and not zonder
    waarde = f"notities {totaal:,} w".replace(",", ".")
    if zonder:
        waarde += f" · {len(zonder)} dia's zonder notitie ({', '.join(map(str, zonder))})"
    waarde += f" · begrippenlijst: {'ja' if begrippen else 'niet gemarkeerd (data-begrippen) — reviewer beslist'}"
    return Gate("S5", ok, waarde, f"≥{S5_NOTITIES:,} w · elke dia · begrippenlijst".replace(",", "."))


# --------------------------------------------------------------------------
# S3: lettergroottes uit een render (Playwright/Chromium)
# --------------------------------------------------------------------------

_JS_LETTERGROOTTES = """
() => {
  const b = {klein: 0, midden: 0, groot: 0};
  const buiten = el => el.closest('.notes, .foot, #bar, #notes, #grid, #help, #toast, #hlbadge');
  const svgSchaal = svg => {
    // preserveAspectRatio staat standaard op 'meet': de tekening past in het kleinste
    // van beide, en wordt in de andere richting gecentreerd. Rekenen met de breedte
    // alleen overschat de letters van een tekening die op zijn hoogte wordt ingepast —
    // op dia 5 van week 3 scheelde dat een factor twee (11,7 pt gemeten, 6,6 pt echt).
    const vb = svg.viewBox && svg.viewBox.baseVal, r = svg.getBoundingClientRect();
    if (!vb || !vb.width || !vb.height || !r.width || !r.height) return 1;
    const pas = (svg.getAttribute('preserveAspectRatio') || '').trim();
    if (pas.startsWith('none')) return r.width / vb.width;
    const k = Math.min(r.width / vb.width, r.height / vb.height);
    return pas.includes('slice') ? Math.max(r.width / vb.width, r.height / vb.height) : k;
  };
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = w.nextNode())) {
    const t = n.textContent.trim(); if (!t) continue;
    const el = n.parentElement;
    if (!el || !el.closest('section.slide') || buiten(el)) continue;
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    let px = parseFloat(cs.fontSize);
    const svg = el.closest('svg'); if (svg) px *= svgSchaal(svg);
    const pt = px * %s, aantal = t.split(/\\s+/).length;
    if (pt < 14) b.klein += aantal; else if (pt < 18) b.midden += aantal; else b.groot += aantal;
  }
  return b;
}
""" % PX_NAAR_PT

_CSS_ALLES_ZICHTBAAR = """
  .slide{display:flex !important}
  #deck{transform:translate(-50%,-50%) scale(1) !important}
  #bar,#notes,#grid,#help,#toast,#hlbadge{display:none !important}
"""


def meet_lettergroottes(pad: Path) -> dict[str, float]:
    """Percentage woorden onder 14 pt, tussen 14 en 18 pt, en op 18 pt of meer,
    gemeten op het gerenderde deck bij 1280 × 720 met schaal 1 (1 px = 0,75 pt).
    Tekst in een tekening telt mee met de schaalfactor van die tekening."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        pagina = browser.new_page(viewport={"width": 1280, "height": 720})
        pagina.goto(Path(pad).resolve().as_uri())
        pagina.add_style_tag(content=_CSS_ALLES_ZICHTBAAR)
        b = pagina.evaluate(_JS_LETTERGROOTTES)
        browser.close()
    totaal = sum(b.values()) or 1
    return {"<14": round(100 * b["klein"] / totaal, 1),
            "14-18": round(100 * b["midden"] / totaal, 1),
            ">=18": round(100 * b["groot"] / totaal, 1)}


def maak_schermen(pad: Path, map_: Path) -> list[Path]:
    """Rendert elke dia apart naar <map>/dia-NN.png op 1280 × 720, schaal 1 — wat er
    geprojecteerd wordt, zonder bedieningsbalk, notities of overzicht."""
    from playwright.sync_api import sync_playwright
    map_ = Path(map_)
    map_.mkdir(parents=True, exist_ok=True)
    paden: list[Path] = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        pagina = browser.new_page(viewport={"width": 1280, "height": 720})
        pagina.goto(Path(pad).resolve().as_uri())
        pagina.add_style_tag(content="""
          #deck{transform:translate(-50%,-50%) scale(1) !important}
          #bar,#notes,#grid,#help,#toast,#hlbadge,#prog{display:none !important}
          .slide{display:none !important} .slide.meet-aan{display:flex !important}""")
        n = pagina.evaluate("document.querySelectorAll('section.slide').length")
        for i in range(n):
            pagina.evaluate("""i => {
              document.querySelectorAll('section.slide').forEach((s, k) => s.classList.toggle('meet-aan', k === i));
            }""", i)
            doel = map_ / f"dia-{i + 1:02d}.png"
            pagina.locator("#deck").screenshot(path=str(doel))
            paden.append(doel)
        browser.close()
    return paden


def gate_s3(buckets: dict[str, float] | None) -> Gate:
    if buckets is None:
        return Gate("S3", False, "geen render; gate niet gemeten", f"<14pt ≤{S3_KLEIN_MAX}% · ≥18pt ≥{S3_GROOT_MIN}%", gemeten=False)
    ok = buckets["<14"] <= S3_KLEIN_MAX and buckets[">=18"] >= S3_GROOT_MIN
    waarde = f"<14pt: {buckets['<14']:g}% · 14–18pt: {buckets['14-18']:g}% · ≥18pt: {buckets['>=18']:g}%"
    return Gate("S3", ok, waarde, f"<14pt ≤{S3_KLEIN_MAX}% · ≥18pt ≥{S3_GROOT_MIN}%")


def meet(deck: Deck, modellen: list[str], jaar: int, lettergroottes: dict[str, float] | None = None) -> list[Gate]:
    return [gate_d1(deck), gate_d3(deck), gate_d4(deck), gate_d5n(deck, modellen, jaar),
            gate_d7(deck), gate_s3(lettergroottes), gate_s4(deck), gate_s5(deck)]


# --------------------------------------------------------------------------
# rapport
# --------------------------------------------------------------------------

def rapport(gates: list[Gate]) -> str:
    def status(g):
        return "----" if not g.gemeten else "PASS" if g.ok else "FAIL"
    regels = [f"{g.code:<4} {status(g)}  {g.waarde}  [{g.drempel}]" for g in gates]
    gemeten = [g for g in gates if g.gemeten]
    rood = sum(1 for g in gemeten if not g.ok)
    slot = (f"→ {rood} van {len(gemeten)} harde gates rood; geen oplevering." if rood
            else f"→ alle {len(gemeten)} harde gates groen; gereed voor de reviewer.")
    if len(gemeten) < len(gates):
        n = len(gates) - len(gemeten)
        slot += f" ({n} gate{'s' if n != 1 else ''} niet gemeten: " + ", ".join(g.code for g in gates if not g.gemeten) + ")"
    return "\n".join(regels + [slot])


def main(argv: list[str] | None = None) -> int:
    hier = Path(__file__).resolve().parents[4]   # …/IM
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("deck", type=Path)
    ap.add_argument("--json", type=Path, help="pad voor de meting (standaard meting-<datum>.json naast het deck)")
    ap.add_argument("--jaar", type=int, default=dt.date.today().year)
    ap.add_argument("--inhoudsopgave", type=Path, default=hier / "8481-informatiemanagement" / "inhoudsopgave.json")
    ap.add_argument("--zonder-render", action="store_true", help="sla de S3-meting (browser) over")
    ap.add_argument("--schermen", type=Path, help="map voor een PNG per dia (dia-NN.png)")
    a = ap.parse_args(argv)
    pptx = a.deck.suffix.lower() == ".pptx"
    werkmap = (a.schermen or a.deck.parent / "meting-werk")
    deck = lees_pptx(a.deck) if pptx else lees_deck(a.deck.read_text(encoding="utf-8"))
    lettergroottes = None
    if not a.zonder_render:
        try:
            lettergroottes = meet_lettergroottes_pptx(a.deck, werkmap) if pptx else meet_lettergroottes(a.deck)
        except Exception as e:  # geen browser/LibreOffice: meld het, meet de rest
            print(f"S3 niet gemeten — render mislukt: {str(e).splitlines()[0][:120]}", file=sys.stderr)
    gates = meet(deck, lees_modellen(a.inhoudsopgave), a.jaar, lettergroottes)
    print(rapport(gates))
    if a.schermen:
        try:
            paden = maak_schermen_pptx(a.deck, a.schermen) if pptx else maak_schermen(a.deck, a.schermen)
            print(f"{len(paden)} schermafbeeldingen in {a.schermen}/")
        except Exception as e:
            print(f"schermafbeeldingen mislukt: {str(e).splitlines()[0][:120]}", file=sys.stderr)
    uit = a.json or a.deck.with_name(f"meting-{dt.date.today():%Y-%m-%d}.json")
    uit.write_text(json.dumps({"deck": a.deck.name, "datum": dt.date.today().isoformat(),
                               "dias": len(deck.dias), "gates": [asdict(g) for g in gates]},
                              ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"meting geschreven: {uit.name}")
    return 1 if any(g.gemeten and not g.ok for g in gates) else 0


if __name__ == "__main__":
    sys.exit(main())
