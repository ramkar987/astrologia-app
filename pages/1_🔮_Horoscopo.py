import streamlit as st
from datetime import datetime
import sys
sys.path.append('..')
from utils.gemini_ai import gerar_horoscopo

st.set_page_config(page_title="Horóscopo Diário", page_icon="🔮", layout="wide")

st.title("🔮 Horóscopo Diário")
st.markdown("### Descubra o que os astros reservam para você hoje")

# Signos e seus emojis
signos = {
    "Áries": "♈",
    "Touro": "♉",
    "Gêmeos": "♊",
    "Câncer": "♋",
    "Leão": "♌",
    "Virgem": "♍",
    "Libra": "♎",
    "Escorpião": "♏",
    "Sagitário": "♐",
    "Capricórnio": "♑",
    "Aquário": "♒",
    "Peixes": "♓"
}

# Seleção de signo
col1, col2 = st.columns([2, 3])

with col1:
    signo_selecionado = st.selectbox(
        "Escolha seu signo:",
        options=list(signos.keys()),
        index=0
    )
    
    data_horoscopo = st.date_input(
        "Data:",
        value=datetime.now(),
        max_value=datetime.now()
    )
    
    gerar_btn = st.button("✨ Gerar Horóscopo", type="primary", use_container_width=True)

with col2:
    st.markdown(f"### {signos[signo_selecionado]} {signo_selecionado}")
    
    if gerar_btn:
        with st.spinner("🌙 Consultando os astros..."):
            try:
                horoscopo = gerar_horoscopo(signo_selecionado, data_horoscopo)
                
                st.markdown("#### 💫 Sua Previsão")
                st.info(horoscopo)
                
                # Botão para compartilhar (simulado)
                st.markdown("---")
                st.success("💡 **Dica**: Volte amanhã para sua nova previsão!")
                
            except Exception as e:
                st.error(f"⚠️ Erro ao gerar horóscopo: {str(e)}")
                st.info("Verifique se a API key do Gemini está configurada corretamente em `.streamlit/secrets.toml`")

# Informações adicionais
st.divider()

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown("#### 🌟 Elemento")
    elementos = {
        "Áries": "Fogo", "Touro": "Terra", "Gêmeos": "Ar", "Câncer": "Água",
        "Leão": "Fogo", "Virgem": "Terra", "Libra": "Ar", "Escorpião": "Água",
        "Sagitário": "Fogo", "Capricórnio": "Terra", "Aquário": "Ar", "Peixes": "Água"
    }
    st.write(elementos[signo_selecionado])

with col_b:
    st.markdown("#### 🪐 Regente")
    regentes = {
        "Áries": "Marte", "Touro": "Vênus", "Gêmeos": "Mercúrio", "Câncer": "Lua",
        "Leão": "Sol", "Virgem": "Mercúrio", "Libra": "Vênus", "Escorpião": "Plutão",
        "Sagitário": "Júpiter", "Capricórnio": "Saturno", "Aquário": "Urano", "Peixes": "Netuno"
    }
    st.write(regentes[signo_selecionado])

with col_c:
    st.markdown("#### ⚡ Qualidade")
    qualidades = {
        "Áries": "Cardinal", "Touro": "Fixo", "Gêmeos": "Mutável", "Câncer": "Cardinal",
        "Leão": "Fixo", "Virgem": "Mutável", "Libra": "Cardinal", "Escorpião": "Fixo",
        "Sagitário": "Mutável", "Capricórnio": "Cardinal", "Aquário": "Fixo", "Peixes": "Mutável"
    }
    st.write(qualidades[signo_selecionado])

# CTA Premium
st.divider()
st.warning("💎 **Premium**: Horóscopo semanal e mensal + análises personalizadas - R$ 19,90/mês")
