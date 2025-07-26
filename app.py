import streamlit as st
import pandas as pd

# Ostrzeżenie startowe
if "accepted_risk" not in st.session_state:
    st.session_state.accepted_risk = False

if not st.session_state.accepted_risk:
    st.warning("⚠️ Hazard może wiązać się z utratą pieniędzy oraz skrajnymi doświadczeniami emocjonalnymi.\n\n"
               "Twórca aplikacji nie zapewnia wygranej na podstawie typów z algorytmów.")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("✅ Akceptuję ryzyko"):
            st.session_state.accepted_risk = True
            st.rerun()
    with col2:
        if st.button("❌ Wychodzę"):
            st.stop()

# Główna aplikacja po akceptacji
st.title("AnalizerPL")

# Przykładowe dropdowny
dyscypliny = ["Piłka nożna", "Koszykówka"]
kraje = ["Polska", "Niemcy"]
ligi = {
    "Polska": ["Ekstraklasa", "I liga", "II liga"],
    "Niemcy": ["Bundesliga", "2. Bundesliga"]
}

dyscyplina = st.selectbox("Wybierz dyscyplinę", dyscypliny)
kraj = st.selectbox("Wybierz kraj", kraje)
liga = st.selectbox("Wybierz ligę", ligi[kraj])

# Po wybraniu ligi – wpisz drużyny
team1 = st.text_input("Drużyna 1")
team2 = st.text_input("Drużyna 2")
