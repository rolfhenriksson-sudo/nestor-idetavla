"""Nestors idétavla – webbgränssnittet.

Starta med:  streamlit run app.py
All logik ligger i tavla.py, här finns bara det man ser på skärmen.
"""
import streamlit as st

import tavla

FIL = "ideer.json"  # här sparas idéerna mellan omstarter

st.set_page_config(page_title="Nestors idétavla", layout="wide")
st.title("💡 Nestors idétavla")

ideer = tavla.ladda(FIL)


def uppdatera(nya_ideer):
    """Sparar ändringen och ritar om sidan."""
    tavla.spara(nya_ideer, FIL)
    st.rerun()


# --- Formulär för att lägga till en idé ---
with st.form("ny_ide", clear_on_submit=True):
    st.subheader("Lägg till en idé")
    titel = st.text_input("Titel")
    beskrivning = st.text_area("Kort beskrivning")
    typ = st.selectbox("Typ", tavla.TYPER)
    if st.form_submit_button("Lägg till"):
        if titel.strip():
            uppdatera(tavla.ny_ide(ideer, titel, beskrivning, typ))
        else:
            st.warning("Skriv en titel först.")

# --- Själva tavlan med tre kolumner ---
for kolumn, ruta in zip(tavla.KOLUMNER, st.columns(len(tavla.KOLUMNER))):
    with ruta:
        st.header(kolumn)
        for ide in tavla.i_kolumn(ideer, kolumn):
            with st.container(border=True):
                st.markdown(f"**{ide['titel']}**  \n_{ide['typ']}_")
                if ide["beskrivning"]:
                    st.write(ide["beskrivning"])
                vanster, hoger, radera = st.columns(3)
                # Knapparna behöver unika nycklar, därför används idéns id
                if vanster.button("⬅️", key=f"v{ide['id']}", disabled=kolumn == tavla.KOLUMNER[0]):
                    uppdatera(tavla.flytta(ideer, ide["id"], -1))
                if hoger.button("➡️", key=f"h{ide['id']}", disabled=kolumn == tavla.KOLUMNER[-1]):
                    uppdatera(tavla.flytta(ideer, ide["id"], 1))
                if radera.button("🗑️", key=f"r{ide['id']}"):
                    uppdatera(tavla.ta_bort(ideer, ide["id"]))
