import streamlit as st
import pandas as pd

# Wczytaj plik krajów
df_kraje = pd.read_csv("kraje.csv", encoding="utf-8")

# Wyciągnij listę nazw do selectboxa
lista_krajow = df_kraje["nazwa_kraju"].tolist()

# Wczytaj plik dyscyplin
df_dyscypliny = pd.read_csv("dyscypliny.csv", encoding="utf-8")

# Wyciągnij listę nazw do selectboxa
lista_dyscyplin = df_dyscypliny["nazwa_dyscypliny"].tolist()

st.set_page_config(page_title="AnalizerPL", layout="centered")

if "accepted_risk" not in st.session_state:
    st.session_state.accepted_risk = False

# Ekran ostrzegawczy
if not st.session_state.accepted_risk:
    with st.container():
        st.warning("⚠️ Hazard może wiązać się z utratą pieniędzy oraz skrajnymi doświadczeniami emocjonalnymi. "
                   "Twórca aplikacji nie zapewnia wygranej na podstawie typów z algorytmów.")
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("✅ Akceptuję ryzyko"):
                st.session_state.accepted_risk = True
                st.rerun()
        with col2:
            if st.button("❌ Wychodzę"):
                st.stop()

# Właściwa aplikacja
else:
    st.title("AnalizerPL")

    dyscyplina = st.selectbox("Wybierz dyscyplinę", lista_dyscyplin)
    kraj = st.selectbox("Wybierz kraj", lista_krajow)

    # Domyślnie pusta lista
    lista_lig = []

    # Jeśli wybrano Polskę, pokaż dostępne ligi
    if kraj == "Polska":
        lista_lig = ["Ekstraklasa", "I liga", "II liga"]

    # Jeśli są dostępne ligi, pokaż selectbox
    if lista_lig:
        liga = st.selectbox("Wybierz ligę", lista_lig)
    else:
        liga = None  # żeby dalej nie wywalało błędu

    druzyna1 = st.text_input("Drużyna 1")
    druzyna2 = st.text_input("Drużyna 2")

    analiza = st.button("🔎 Analizuj")

    if analiza:
        if druzyna1.strip() and druzyna2.strip():
            st.success(f"Analiza meczu: **{druzyna1.strip()}** vs **{druzyna2.strip()}** "
                       f"({liga if liga else 'Brak ligi'}, {kraj}) – wkrótce zostanie uruchomiona.")
        else:
            st.error("⚠️ Uzupełnij obie drużyny, aby przeprowadzić analizę.")
