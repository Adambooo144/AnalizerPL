import streamlit as st

st.set_page_config(page_title="AnalizerPL", layout="centered")

if "accepted_risk" not in st.session_state:
    st.session_state.accepted_risk = False

# Jeśli nie zaakceptowano ryzyka
if not st.session_state.accepted_risk:
    with st.container():
        st.warning("⚠️ Hazard może wiązać się z utratą pieniędzy oraz skrajnymi doświadczeniami emocjonalnymi. "
                   "Twórca aplikacji nie zapewnia wygranej na podstawie typów z algorytmów.")
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("✅ Akceptuję ryzyko"):
                st.session_state.accepted_risk = True
        with col2:
            if st.button("❌ Wychodzę"):
                st.stop()

# Jeśli zaakceptowano ryzyko – pokazujemy resztę
else:
    st.title("AnalizerPL")

    dyscyplina = st.selectbox("Wybierz dyscyplinę", ["Piłka nożna"])
    kraj = st.selectbox("Wybierz kraj", ["Polska"])
    liga = st.selectbox("Wybierz ligę", ["Ekstraklasa", "I liga", "II liga"])

    druzyna1 = st.text_input("Drużyna 1")
    druzyna2 = st.text_input("Drużyna 2")

    if druzyna1 and druzyna2:
        st.markdown(f"🔍 Wybrano mecz: **{druzyna1} vs {druzyna2}**")
