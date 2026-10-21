"""Tester för logiken i tavla.py. Kör med: pytest -v"""
import pytest

import tavla


def test_ny_ide_hamnar_i_ide_kolumnen():
    ideer = tavla.ny_ide([], "Offertkalkylator", "För byggfirmor", "Produkt")
    assert len(ideer) == 1
    assert ideer[0]["status"] == "Idé"


def test_tom_titel_ger_fel():
    with pytest.raises(ValueError):
        tavla.ny_ide([], "  ", "", "Paket")


def test_flytta_hoger_och_vanster():
    ideer = tavla.ny_ide([], "Test", "", "Kundidé")
    id_ = ideer[0]["id"]
    ideer = tavla.flytta(ideer, id_, 1)
    assert ideer[0]["status"] == "Pågår"
    ideer = tavla.flytta(ideer, id_, -1)
    assert ideer[0]["status"] == "Idé"


def test_flytta_stannar_vid_kanten():
    ideer = tavla.ny_ide([], "Test", "", "Kundidé")
    id_ = ideer[0]["id"]
    ideer = tavla.flytta(ideer, id_, -1)
    assert ideer[0]["status"] == "Idé"
    for _ in range(5):
        ideer = tavla.flytta(ideer, id_, 1)
    assert ideer[0]["status"] == "Klart"


def test_ta_bort():
    ideer = tavla.ny_ide([], "A", "", "Paket")
    ideer = tavla.ny_ide(ideer, "B", "", "Paket")
    ideer = tavla.ta_bort(ideer, ideer[0]["id"])
    assert [i["titel"] for i in ideer] == ["B"]


def test_spara_och_ladda(tmp_path):
    fil = tmp_path / "ideer.json"
    assert tavla.ladda(fil) == []
    ideer = tavla.ny_ide([], "Åäö-idé", "Svenska tecken", "Produkt")
    tavla.spara(ideer, fil)
    assert tavla.ladda(fil) == ideer
