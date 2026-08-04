import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Dashboards Expedição – NDI",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Remove paddings/menu padrão do Streamlit para o dashboard ocupar a tela toda
st.markdown(
    """
    <style>
        .block-container { padding-top: 0.6rem; padding-bottom: 0rem; padding-left: 1rem; padding-right: 1rem; }
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

BASE_DIR = Path(__file__).parent / "dashboards"

DASHBOARDS = {
    "principal": {"label": "📊 Resultado Operacional", "file": "dashprincipal.html", "height": 1700},
    "comparativo": {"label": "📈 Comparativo 2025 x 2026", "file": "dashcomparativo.html", "height": 1900},
}

# Permite abrir direto no dashboard certo por link, ex: https://seu-app.streamlit.app/?dash=comparativo
query_dash = st.query_params.get("dash", "principal")
if query_dash not in DASHBOARDS:
    query_dash = "principal"

st.sidebar.title("📦 Dashboards NDI")
chaves = list(DASHBOARDS.keys())
escolha = st.sidebar.radio(
    "Selecione o dashboard:",
    options=chaves,
    format_func=lambda k: DASHBOARDS[k]["label"],
    index=chaves.index(query_dash),
)

# Mantém a URL sincronizada com a escolha (facilita compartilhar o link certo)
st.query_params["dash"] = escolha

st.sidebar.markdown("---")
st.sidebar.caption(
    "Os dados de cada dashboard continuam vindo direto da planilha do Google Sheets "
    "e o histórico de meses é sincronizado com a aba HistoricoDash, exatamente como antes."
)

cfg = DASHBOARDS[escolha]
html_path = BASE_DIR / cfg["file"]
html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=cfg["height"], scrolling=True)
