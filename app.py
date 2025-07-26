import streamlit as st
import pandas as pd

# Wczytaj plik dyscyplin
df_dyscypliny = pd.read_csv("dyscypliny.csv")

# Wyciągnij listę nazw do selectboxa
lista_dyscyplin = df_dyscypliny["discipline_name"].tolist()

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
                st.rerun() # ← tu jest magia
        with col2:
            if st.button("❌ Wychodzę"):
                st.stop()


# Właściwa aplikacja
else:
    st.title("AnalizerPL")

    dyscyplina = st.selectbox("Wybierz dyscyplinę", lista_dyscyplin)
    kraj = st.selectbox("Wybierz kraj", df_kraje["kraj"])
    liga = st.selectbox("Wybierz ligę", ["Ekstraklasa", "I liga", "II liga"])

    druzyna1 = st.text_input("Drużyna 1")
    druzyna2 = st.text_input("Drużyna 2")

    # Przycisk jest zawsze widoczny
    analiza = st.button("🔎 Analizuj")

    # Ale działa dopiero po wpisaniu drużyn
    if analiza:
        if druzyna1.strip() and druzyna2.strip():
            st.success(f"Analiza meczu: **{druzyna1.strip()}** vs **{druzyna2.strip()}** "
                       f"({liga}, {kraj}) – wkrótce zostanie uruchomiona.")
        else:
            st.error("⚠️ Uzupełnij obie drużyny, aby przeprowadzić analizę.")

