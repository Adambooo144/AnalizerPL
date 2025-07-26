import streamlit as st

st.set_page_config(page_title="AnalizerPL", layout="centered")

# Inicjalizacja stanu sesji
if "accepted" not in st.session_state:
    st.session_state.accepted = False

# Komunikat ostrzegawczy
st.warning("⚠️ Hazard może wiązać się z utratą pieniędzy oraz skrajnymi doświadczeniami emocjonalnymi.\n\nTwórca aplikacji nie zapewnia wygranej na podstawie typów z algorytmów.")

# Przyciski
col1, col2 = st.columns(2)
with col1:
    if st.button("✅ Akceptuję ryzyko"):
        st.session_state.accepted = True
with col2:
    if st.button("❌ Wychodzę"):
        st.stop()

# Główna część aplikacji – tylko po akceptacji
if st.session_state.accepted:
    st.title("AnalizerPL")

    dyscyplina = st.selectbox("Wybierz dyscyplinę", ["Piłka nożna"])
    kraj = st.selectbox("Wybierz kraj", ["Polska"])
    liga = st.selectbox("Wybierz ligę", ["Ekstraklasa", "I liga", "II liga"])
    druzyna1 = st.text_input("Drużyna 1")
    druzyna2 = st.text_input("Drużyna 2")
