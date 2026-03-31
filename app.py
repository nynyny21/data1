import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(layout="wide")

st.markdown("""
<style>
.block-container { 
    max-width: 100% !important; 
    padding-left: 1rem !important; 
    padding-right: 1rem !important; 
    padding-top: 0.8rem !important; 
}
iframe { 
    width: 100% !important; 
    margin-top: 0 !important; 
    margin-bottom: 0.6rem !important; 
}
</style>
""", unsafe_allow_html=True)

st.title("Summary Datarate N5")

# File ada di root repo
base_path = Path(".")

# Urutan manual sesuai kebutuhan
ordered_files = [
    "Ant_0.6m_4Msps_1W.html",
    "Ant_0.6m_8Msps_1W.htmll",
    "Ant_0.6m_4Msps_3W.html",
    "Ant_0.6m_8Msps_3W.html",
    "Ant_0.98m_4Msps_3W.html",
    "Ant_0.98m_8Msps_3W.html",
]

# Filter hanya file yang benar-benar ada
available_files = [
    f for f in ordered_files if (base_path / f).exists()
]

if not available_files:
    st.error("Tidak ada file HTML ditemukan.")
else:
    selected_file = st.selectbox(
        "Select antenna configuration",
        available_files
    )

    file_path = base_path / selected_file
    html = file_path.read_text(encoding="utf-8")

    components.html(
        html,
        height=600,
        scrolling=True
    )
