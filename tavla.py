"""Logiken för Nestors idétavla.

Här finns bara "rena" funktioner: de tar emot en lista med idéer och
returnerar en ny lista. Inget UI här, så allt går lätt att testa.
"""
import json
import uuid
from pathlib import Path

# Tavlans tre kolumner, i ordning från vänster till höger
KOLUMNER = ["Idé", "Pågår", "Klart"]

# Vilka sorters idéer man kan lägga in
TYPER = ["Kundidé", "Paket", "Produkt"]


def ny_ide(ideer, titel, beskrivning, typ):
    """Lägger till en ny idé i första kolumnen och returnerar en ny lista."""
    titel = titel.strip()
    if not titel:
        raise ValueError("Titel får inte vara tom")
    if typ not in TYPER:
        raise ValueError(f"Okänd typ: {typ}")
    ide = {
        "id": uuid.uuid4().hex[:8],  # kort unikt id
        "titel": titel,
        "beskrivning": beskrivning.strip(),
        "typ": typ,
        "status": KOLUMNER[0],
    }
    return ideer + [ide]


def flytta(ideer, ide_id, steg):
    """Flyttar en idé steg kolumner (-1 = vänster, +1 = höger).

    Idén stannar kvar vid kanten om den inte kan flyttas längre.
    """
    resultat = []
    for ide in ideer:
        if ide["id"] == ide_id:
            index = KOLUMNER.index(ide["status"]) + steg
            index = max(0, min(index, len(KOLUMNER) - 1))
            ide = {**ide, "status": KOLUMNER[index]}
        resultat.append(ide)
    return resultat


def ta_bort(ideer, ide_id):
    """Returnerar listan utan idén med det angivna id:t."""
    return [ide for ide in ideer if ide["id"] != ide_id]


def i_kolumn(ideer, kolumn):
    """Returnerar alla idéer som ligger i en viss kolumn."""
    return [ide for ide in ideer if ide["status"] == kolumn]


def ladda(fil):
    """Läser idéerna från en JSON-fil. Finns ingen fil blir listan tom."""
    fil = Path(fil)
    if not fil.exists():
        return []
    return json.loads(fil.read_text(encoding="utf-8"))


def spara(ideer, fil):
    """Sparar idéerna i en JSON-fil (läsbar, med svenska tecken)."""
    Path(fil).write_text(
        json.dumps(ideer, ensure_ascii=False, indent=2), encoding="utf-8"
    )
