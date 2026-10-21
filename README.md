# 💡 Nestors idétavla

En liten webbapp där man samlar idéer (kundidéer, paket och produkter) och flyttar dem mellan kolumnerna **Idé**, **Pågår** och **Klart**. Byggd i Python med [Streamlit](https://streamlit.io).

## Kör i GitHub Codespaces (inget att installera)

1. Klicka på den gröna knappen **Code** här ovanför.
2. Välj fliken **Codespaces** och klicka på **Create codespace on main**.
3. Vänta någon minut. Allt installeras och appen startar av sig själv.
4. Appen öppnas i en flik (port 8501). Gör den inte det: öppna fliken **Ports** längst ner och klicka på jordgloben vid 8501.

Vill du starta appen själv skriver du i terminalen:

```bash
streamlit run app.py
```

## Filerna

| Fil | Vad den gör |
|---|---|
| `app.py` | Gränssnittet, det du ser i webbläsaren |
| `tavla.py` | Logiken: lägga till, flytta, ta bort, spara |
| `test_tavla.py` | Tester för logiken (kör med `pytest -v`) |
| `ideer.json` | Skapas automatiskt och sparar dina idéer |

Testerna körs automatiskt med GitHub Actions varje gång något ändras.

Obs: `ideer.json` sparas bara i ditt codespace och laddas inte upp till GitHub.
