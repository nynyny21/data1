import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(layout="wide")

st.markdown("""
<style>
.block-container { max-width: 100% !important; padding-left: 1rem !important; padding-right: 1rem !important; padding-top: 0.8rem !important; }
h3 { margin: 0.2rem 0 0.2rem 0 !important; }
iframe { width: 100% !important; margin-top: 0 !important; margin-bottom: 0.6rem !important; }
</style>
""", unsafe_allow_html=True)

st.title("Summary Datarate N5")

base_path = Path("reports")

html_files = [
    "Ant_0.6m_4Msps_1W.html",
    "Ant_0.6m_8Msps_1W.html",
    "Ant_0.6m_4Msps_3W.html",
    "Ant_0.6m_8Msps_3W.html",
    "Ant_0.98m_4Msps_3W.html",
    "Ant_0.98m_8Msps_3W.html",
]

for f in html_files:
    file_path = base_path / f
    if file_path.exists():
        html = file_path.read_text(encoding="utf-8")

        
        components.html(html, height=600, scrolling=True)

        # kalau masih mau pemisah tipis:
        st.markdown("<hr style='margin:0.1rem 0; border:0; border-top:1px solid #ddd;'>", unsafe_allow_html=True)
    else:
        st.error(f"File tidak ditemukan: {file_path}")