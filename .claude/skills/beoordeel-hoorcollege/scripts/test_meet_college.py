"""
Tests voor meet-college.py — de acht script-gates uit het LRD (Deel 6.2).

Het voorbeelddeck ijkdeck.html is het ijkpunt: de beoordeling van 28 augustus
2026 mat daar 14 getimede momenten (17,5 minuten), gemiddeld 110 woorden per
dia en een langste gat van 4 dia's. Het script moet die cijfers reproduceren
(roadmap stap 1: binnen 2%).

Dat bestand ligt hier naast de scripts en staat bewust stil. Het is de kopie van
introductie-bedrijfskunde.html waar de beoordelaar op 28 augustus naar keek, en
het hoort alleen te veranderen als iemand die beoordeling overdoet. Richt deze
fixture niet op een deck dat nog bewerkt wordt: dan toetsen deze tests niet meer
het meetscript maar het deck, en gaan ze rood bij elke redactieronde. Zo ging het
eerder mis, toen de fixture naar weken/week-01/college.html wees; dat deck is
sinds 28 augustus zeven dia's verder gewerkt en telt 60 woorden meer.
"""
from pathlib import Path

import pytest

import meet_college as mc

HIER = Path(__file__).resolve().parent
IM = HIER.parents[3]
VOORBEELD = HIER / "ijkdeck.html"


@pytest.fixture(scope="module")
def voorbeeld():
    return mc.lees_deck(VOORBEELD.read_text(encoding="utf-8"))


# ---------- klok ----------

@pytest.mark.parametrize("tekst,seconden", [
    ("60 seconden", 60), ("90 seconden", 90), ("2 minuten", 120),
    ("3 min", 180), ("45 sec", 45), ("0,5 min", 30), ("1 minuut", 60),
])
def test_klok_tekst_naar_seconden(tekst, seconden):
    assert mc.klok_seconden(tekst) == seconden


def test_klok_zonder_getal_is_none():
    assert mc.klok_seconden("even denken") is None


# ---------- het voorbeelddeck als ijkpunt ----------

def test_voorbeelddeck_heeft_32_dias(voorbeeld):
    assert len(voorbeeld.dias) == 32


def test_voorbeelddeck_telt_14_momenten_van_17_5_minuten(voorbeeld):
    momenten = [m for d in voorbeeld.dias for m in d.momenten]
    assert len(momenten) == 14
    assert sum(m.seconden for m in momenten) == 17.5 * 60


def test_voorbeelddeck_momenten_op_13_dias(voorbeeld):
    assert sum(1 for d in voorbeeld.dias if d.momenten) == 13


def test_voorbeelddeck_zoals_beoordeeld_gemiddeld_110_woorden_en_gat_4(voorbeeld):
    # De beoordeling van 28 aug 2026 mat 31 dia's; op 1 sep is dia 3 "Wie staat hier"
    # toegevoegd. Zonder die dia moet het script de beoordeling reproduceren.
    zoals_beoordeeld = [d for d in voorbeeld.dias if d.titel != "Wie staat hier"]
    assert len(zoals_beoordeeld) == 31
    gem = sum(d.woorden for d in zoals_beoordeeld) / 31
    assert gem == pytest.approx(110, rel=0.02)
    assert mc.langste_gat(zoals_beoordeeld) == 4


def test_voorbeelddeck_nu_gemiddeld_107_woorden_en_gat_5(voorbeeld):
    gem = sum(d.woorden for d in voorbeeld.dias) / len(voorbeeld.dias)
    assert gem == pytest.approx(107, abs=1)
    assert mc.langste_gat(voorbeeld.dias) == 5


def test_voorbeelddeck_twee_dias_boven_170_woorden(voorbeeld):
    # de beoordeling noemde dia 21 en 23; door de ingevoegde dia 3 zijn dat nu 22 en 24
    assert [d.nummer for d in voorbeeld.dias if d.woorden > 170] == [22, 24]


def test_notities_tellen_niet_mee_als_diatekst(voorbeeld):
    # dia 1 (titel) heeft een notitie; de diatekst moet die niet bevatten
    titel = voorbeeld.dias[0]
    assert titel.notitie_woorden > 0
    assert titel.woorden < titel.notitie_woorden


# ==========================================================================
# de gates — met kleine decks die precies één ding doen
# ==========================================================================

def dia(body="", *, deel="Deel", titel="t", notitie="n", attrs="", klas="slide"):
    return (f'<section class="{klas}" data-part="{deel}" data-title="{titel}" {attrs}>'
            f'{body}<div class="notes">{notitie}</div></section>')


def deck(*secties):
    return mc.lees_deck("<html><body>" + "".join(secties) + "</body></html>")


LO7 = "".join(f'<li data-lo="LO{i}">u{i}</li>' for i in range(1, 8))
LO6 = "".join(f'<li data-lo="LO{i}">u{i}</li>' for i in range(1, 7))


def moment(sec="60 seconden", vorm="tweetal"):
    return (f'<div class="socratic" data-vorm="{vorm}"><p class="lbl">x '
            f'<span class="clock">{sec}</span></p><p class="qq">?</p></div>')


# ---------- D1 leeruitkomsten ----------

def test_d1_slaagt_als_dia1_en_slotdia_dezelfde_zeven_uitkomsten_dragen():
    g = mc.gate_d1(deck(dia(LO7), dia(), dia(LO7)))
    assert g.ok and g.waarde == "7/7"


def test_d1_faalt_bij_zes_uitkomsten():
    assert not mc.gate_d1(deck(dia(LO6), dia(LO6))).ok


def test_d1_faalt_als_slotdia_afwijkt_van_dia1():
    assert not mc.gate_d1(deck(dia(LO7), dia(LO6))).ok


# ---------- D3 woorden ----------

def test_d3_slaagt_onder_110_gemiddeld_en_170_maximaal():
    assert mc.gate_d3(deck(dia("w " * 100), dia("w " * 120))).ok


def test_d3_faalt_bij_een_dia_boven_170():
    assert not mc.gate_d3(deck(dia("w " * 10), dia("w " * 171))).ok


def test_d3_faalt_bij_gemiddeld_boven_110():
    assert not mc.gate_d3(deck(dia("w " * 120), dia("w " * 120))).ok


# ---------- D4 activering ----------

def _tien_momenten_deck():
    # 10 momenten van 1,5 min = 15 min op 10 van 20 dia's, vier vormen, gat ≤ 4
    vormen = ["tweetal", "handen", "schrijven", "stemmen"]
    secties = []
    for i in range(20):
        secties.append(dia(moment("90 seconden", vormen[(i // 2) % 4]) if i % 2 == 0 else ""))
    return deck(*secties)


def test_d4_slaagt_bij_tien_momenten_vier_vormen_binnen_de_tijd():
    g = mc.gate_d4(_tien_momenten_deck())
    assert g.ok, g.waarde


def test_d4_faalt_bij_negen_momenten():
    d = _tien_momenten_deck()
    d.dias[0].momenten.clear()
    assert not mc.gate_d4(d).ok


def test_d4_faalt_bij_gat_van_vijf():
    assert not mc.gate_d4(deck(*([dia(moment())] * 10 + [dia()] * 5 + [dia(moment())]))).ok


def test_d4_faalt_bij_minder_dan_vier_werkvormen():
    assert not mc.gate_d4(deck(*[dia(moment("90 seconden", "tweetal"))] * 10)).ok


def test_d4_faalt_boven_twintig_minuten():
    assert not mc.gate_d4(deck(*[dia(moment("3 min", v)) for v in "abcdefghij"])).ok


def test_d4_voorbeelddeck_meldt_gat_5_en_geen_vormen(voorbeeld):
    g = mc.gate_d4(voorbeeld)
    assert not g.ok
    assert "gat 5" in g.waarde and "vormen niet gemarkeerd" in g.waarde


# ---------- D5-nieuw houdbaarheid ----------

MODELLEN = ["1.1", "1.2"]


def modeldia(nummer, oordeel="blijft", jaar=2026):
    return dia("m", attrs=f'data-model="{nummer}" data-houdbaarheid="{oordeel}" data-bronjaar="{jaar}"')


def test_d5n_slaagt_als_elk_model_een_oordeel_en_verse_bron_heeft():
    d = deck(modeldia("1.1"), modeldia("1.2", "verschuift"), dia("c", attrs='data-casus="nl"'))
    assert mc.gate_d5n(d, MODELLEN, jaar=2026).ok


def test_d5n_faalt_als_een_model_ontbreekt():
    d = deck(modeldia("1.1"), dia("c", attrs='data-casus="nl"'))
    g = mc.gate_d5n(d, MODELLEN, jaar=2026)
    assert not g.ok and "1.2" in g.waarde


def test_d5n_faalt_bij_bron_ouder_dan_drie_jaar():
    d = deck(modeldia("1.1", jaar=2022), modeldia("1.2"), dia("c", attrs='data-casus="nl"'))
    assert not mc.gate_d5n(d, MODELLEN, jaar=2026).ok


def test_d5n_faalt_zonder_nederlandse_casus():
    assert not mc.gate_d5n(deck(modeldia("1.1"), modeldia("1.2")), MODELLEN, jaar=2026).ok


def test_d5n_faalt_bij_onbekend_oordeel():
    d = deck(modeldia("1.1", "misschien"), modeldia("1.2"), dia("c", attrs='data-casus="nl"'))
    assert not mc.gate_d5n(d, MODELLEN, jaar=2026).ok


def test_modellen_uit_inhoudsopgave_zijn_de_veertien_paragrafen():
    pad = IM / "8481-informatiemanagement" / "inhoudsopgave.json"
    if not pad.exists():
        pytest.skip("geen inhoudsopgave.json in dit project (ander vak)")
    assert mc.lees_modellen(pad) == ["1.1", "1.2", "1.3", "1.4", "1.5", "2.1", "2.2", "2.3",
                                     "3.1", "3.2", "3.3", "4.1", "4.2", "4.3"]


# ---------- D7 afsluiting ----------

def test_d7_slaagt_met_check_huiswerk_en_doorkijk_op_de_laatste_drie_dias():
    d = deck(dia(), dia(attrs='data-check="mc"'), dia(attrs='data-huiswerk="H1"'), dia(attrs='data-doorkijk="werkcollege"'))
    assert mc.gate_d7(d).ok


def test_d7_faalt_zonder_ophaalcheck():
    d = deck(dia(), dia(attrs='data-huiswerk="H1"'), dia(attrs='data-doorkijk="werkcollege"'))
    assert not mc.gate_d7(d).ok


def test_d7_faalt_als_de_check_niet_bij_de_laatste_drie_staat():
    d = deck(dia(attrs='data-check="mc"'), dia(), dia(), dia(attrs='data-huiswerk="H1" data-doorkijk="w"'))
    assert not mc.gate_d7(d).ok


# ---------- S4 tempo ----------

def test_s4_slaagt_met_pauzedia_met_eindtijd_en_blokken_die_tot_90_optellen():
    d = deck(dia(attrs='data-minuten="40"'), dia(deel="Pauze", attrs='data-eind="10:45"', klas="slide part-slide"),
             dia(attrs='data-minuten="50"'))
    assert mc.gate_s4(d).ok


def test_s4_faalt_als_blokken_niet_tot_90_optellen():
    d = deck(dia(attrs='data-minuten="40"'), dia(deel="Pauze", attrs='data-eind="10:45"'), dia(attrs='data-minuten="40"'))
    assert not mc.gate_s4(d).ok


def test_s4_faalt_zonder_eindtijd_op_de_pauzedia():
    d = deck(dia(attrs='data-minuten="40"'), dia(deel="Pauze"), dia(attrs='data-minuten="50"'))
    assert not mc.gate_s4(d).ok


# ---------- S5 studeerbaarheid ----------

def test_s5_slaagt_bij_3000_notitiewoorden_op_elke_dia_en_een_begrippenlijst():
    d = deck(dia(notitie="n " * 1500), dia(notitie="n " * 1500, attrs='data-begrippen="1"'))
    assert mc.gate_s5(d).ok


def test_s5_faalt_als_een_dia_geen_notitie_heeft():
    d = deck(dia(notitie="n " * 3000), dia(notitie="", attrs='data-begrippen="1"'))
    g = mc.gate_s5(d)
    assert not g.ok and "zonder notitie" in g.waarde


def test_s5_faalt_onder_3000_woorden():
    assert not mc.gate_s5(deck(dia(notitie="n " * 100, attrs='data-begrippen="1"'))).ok


# ---------- rapport ----------

def test_rapport_drukt_per_gate_pass_of_fail_en_telt_rood():
    gates = [mc.Gate("D1", True, "7/7", "7/7"), mc.Gate("D4", False, "9 momenten", "≥10")]
    tekst = mc.rapport(gates)
    assert "D1   PASS  7/7" in tekst and "D4   FAIL  9 momenten" in tekst
    assert "1 van 2 harde gates rood" in tekst


def test_rapport_meldt_geen_oplevering_bij_rood_en_gereed_bij_groen():
    assert "geen oplevering" in mc.rapport([mc.Gate("D1", False, "6/7", "7/7")])
    assert "gereed" in mc.rapport([mc.Gate("D1", True, "7/7", "7/7")])


# ---------- S3 leesbaarheid (render) ----------

def test_s3_gate_op_buckets():
    assert mc.gate_s3({"<14": 27, "14-18": 45, ">=18": 28}).ok
    assert not mc.gate_s3({"<14": 31, "14-18": 41, ">=18": 28}).ok      # te veel klein
    assert not mc.gate_s3({"<14": 20, "14-18": 60, ">=18": 20}).ok      # te weinig groot


@pytest.mark.render
def test_s3_render_voorbeelddeck_reproduceert_de_beoordeling():
    # Beoordeling 28 aug 2026: 27% onder 14 pt, 45% 14–18 pt, 28% op 18 pt of meer.
    # Die drie getallen zijn gemeten met de oude schaalformule, die alleen naar de
    # breedte van een tekening keek. Sinds 16 sep 2026 rekent het script met de schaal
    # die de browser echt toepast (preserveAspectRatio 'meet': de kleinste van breedte
    # en hoogte). Hetzelfde bestand komt daarmee op 30,5 / 42,0 / 27,5 uit: de letters
    # in een tekening die op zijn hoogte wordt ingepast, tellen nu op hun echte maat.
    # Het bestand is niet veranderd; het meetinstrument wel.
    b = mc.meet_lettergroottes(VOORBEELD)
    assert b["<14"] == pytest.approx(30.5, abs=3)
    assert b["14-18"] == pytest.approx(42, abs=3)
    assert b[">=18"] == pytest.approx(27.5, abs=3)
    assert b["<14"] + b["14-18"] + b[">=18"] == pytest.approx(100, abs=0.5)


# ---------- rapport zonder render, en de CLI ----------

def test_rapport_telt_een_niet_gemeten_gate_niet_als_rood():
    gates = [mc.Gate("D1", True, "7/7", "7/7"), mc.gate_s3(None)]
    tekst = mc.rapport(gates)
    assert "S3   ----" in tekst
    assert "alle 1 harde gates groen" in tekst and "1 gate niet gemeten: S3" in tekst


def test_cli_schrijft_meting_json_en_geeft_exit_1_bij_rood(tmp_path):
    import subprocess, sys, json
    uit = tmp_path / "meting.json"
    r = subprocess.run([sys.executable, str(HIER / "meet_college.py"), str(VOORBEELD),
                        "--zonder-render", "--json", str(uit)], capture_output=True, text=True)
    assert r.returncode == 1                      # het voorbeelddeck volgt het contract niet
    assert "D4   FAIL" in r.stdout and "S3   ----" in r.stdout
    data = json.loads(uit.read_text(encoding="utf-8"))
    assert data["dias"] == 32 and {g["code"] for g in data["gates"]} >= {"D1", "D3", "D4", "D5n", "D7", "S3", "S4", "S5"}


# ---------- schermafbeeldingen per dia ----------

@pytest.mark.render
def test_schermen_schrijft_een_png_per_dia_met_dianummer(tmp_path):
    paden = mc.maak_schermen(VOORBEELD, tmp_path / "schermen")
    assert len(paden) == 32
    assert paden[0].name == "dia-01.png" and paden[-1].name == "dia-32.png"
    assert all(p.exists() and p.stat().st_size > 1000 for p in paden)


@pytest.mark.render
def test_cli_schermen_optie_rendert_de_dias(tmp_path):
    import subprocess, sys
    r = subprocess.run([sys.executable, str(HIER / "meet_college.py"), str(VOORBEELD),
                        "--zonder-render", "--json", str(tmp_path / "m.json"), "--schermen", str(tmp_path / "s")],
                       capture_output=True, text=True)
    assert "32 schermafbeeldingen" in r.stdout
    assert (tmp_path / "s" / "dia-17.png").exists()


# ---------- D5-n bij een deck zonder modeldia's ----------

def test_d5n_zonder_enige_modeldia_is_niet_gemeten_in_plaats_van_fail():
    # een deck van een ander vak, of zonder deckcontract: geen ruis over ontbrekende IM-modellen
    g = mc.gate_d5n(deck(dia("a"), dia("b")), MODELLEN, jaar=2026)
    assert not g.gemeten
    assert "geen modeldia" in g.waarde


def test_d5n_met_een_modeldia_maar_niet_alle_blijft_fail():
    g = mc.gate_d5n(deck(modeldia("1.1"), dia("c", attrs='data-casus="nl"')), MODELLEN, jaar=2026)
    assert g.gemeten and not g.ok


# ---------- contractloze decks: markering ontbreekt ≠ element ontbreekt ----------

def test_d1_zonder_enige_data_lo_is_niet_gemeten():
    g = mc.gate_d1(deck(dia("a"), dia("b")))
    assert not g.gemeten and "niet gemarkeerd" in g.waarde


def test_d7_zonder_enige_markering_is_niet_gemeten():
    assert not mc.gate_d7(deck(dia("a"), dia("b"), dia("c"))).gemeten


def test_s4_zonder_minuten_en_eindtijd_is_niet_gemeten():
    assert not mc.gate_s4(deck(dia("a"), dia(deel="Pauze"), dia("c"))).gemeten


def test_s5_zonder_data_begrippen_meet_alleen_woorden_en_notities():
    g = mc.gate_s5(deck(dia(notitie="n " * 1500), dia(notitie="n " * 1500)))
    assert g.gemeten and g.ok and "begrippenlijst: niet gemarkeerd" in g.waarde


def test_d4_zonder_enige_data_vorm_faalt_niet_op_werkvormen():
    d = deck(*[dia(f'<div class="socratic"><p class="lbl">x <span class="clock">90 seconden</span></p></div>')
               if i % 2 == 0 else dia() for i in range(20)])
    g = mc.gate_d4(d)
    assert g.ok and "vormen niet gemarkeerd" in g.waarde


def test_voorbeelddeck_zonder_contract_heeft_alleen_college_fails(voorbeeld):
    gates = mc.meet(voorbeeld, ["1.1"], jaar=2026)
    rood = {g.code for g in gates if g.gemeten and not g.ok}
    niet = {g.code for g in gates if not g.gemeten}
    assert rood == {"D3", "D4"}                       # dia 22 > 170 woorden; gat 5
    assert {"D1", "D5n", "D7", "S4", "S3"} <= niet     # S3 omdat er geen render is meegegeven


# ---------- PPTX-route: zelfde gates, ander bestand ----------

PPTX = IM / "weken" / "week-01" / "parallel" / "bedrijfskundig-denken-erik.pptx"


@pytest.fixture(scope="module")
def pptx_deck():
    return mc.lees_pptx(PPTX)


def test_pptx_levert_een_deck_met_53_dias_en_notities(pptx_deck):
    assert len(pptx_deck.dias) == 53
    assert pptx_deck.dias[0].titel.lower().startswith("theosm01")
    assert sum(d.notitie_woorden for d in pptx_deck.dias) > 2000
    assert pptx_deck.dias[2].woorden == 20          # dia 3: de tweetalopdracht, zonder het dianummer
    assert [d.nummer for d in pptx_deck.dias if d.verborgen] == [15, 29, 32]


def test_pptx_dianummer_in_voettekst_telt_niet_als_woord(pptx_deck):
    # dia 27 bevat alleen het dianummer; dat is voettekst, geen inhoud
    assert pptx_deck.dias[26].woorden == 0


def test_pptx_heeft_geen_getimede_momenten_en_geen_contract(pptx_deck):
    assert all(not d.momenten for d in pptx_deck.dias)
    gates = mc.meet(pptx_deck, ["1.1"], jaar=2026)
    assert not next(g for g in gates if g.code == "D4").gemeten   # geen .socratic → niet gemarkeerd


@pytest.mark.render
def test_pptx_lettergroottes_uit_pdf_zijn_echte_punten(tmp_path):
    b = mc.meet_lettergroottes_pptx(PPTX, tmp_path)
    assert b["<14"] + b["14-18"] + b[">=18"] == pytest.approx(100, abs=0.5)
    assert (tmp_path / "deck.pdf").exists()


@pytest.mark.render
def test_pptx_schermen_via_pdf(tmp_path):
    paden = mc.maak_schermen_pptx(PPTX, tmp_path / "s")
    assert len(paden) == 53 and paden[52].name == "dia-53.png"


# ---------- een project zonder inhoudsopgave.json (ander vak) ----------

def test_modellen_zonder_inhoudsopgave_is_lege_lijst(tmp_path):
    assert mc.lees_modellen(tmp_path / "bestaat-niet.json") == []


def test_d5n_zonder_modellenlijst_is_niet_gemeten():
    g = mc.gate_d5n(deck(modeldia("1.1")), [], jaar=2026)
    assert not g.gemeten and "geen modellenlijst" in g.waarde


# ---------- SmartArt: tekst in ppt/diagrams/, niet in de dia-XML ----------

def test_pptx_telt_smartart_tekst_mee(pptx_deck):
    # dia 18 is een SmartArt-diagram met beroepsproduct, Edumundo en de digitale kennistoets;
    # de beoordeling van 28 aug 2026 miste die tekst eerst om dezelfde reden
    assert pptx_deck.dias[17].woorden > 20
    assert pptx_deck.dias[16].woorden > 4          # dia 17: de vier chevrons


def test_pptx_smartart_tekst_zit_in_de_titel_of_tekst(pptx_deck):
    assert "kennistoets" in mc.lees_pptx_tekst(PPTX, 18).lower()
