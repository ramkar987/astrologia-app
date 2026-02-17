import streamlit as st

st.set_page_config(
    page_title="Astro Vision",
    page_icon="🌙",
    layout="wide"
)

st.title("🌙 Astro Vision - Seu Portal Astrológico")
st.markdown("### Descubra os segredos do seu mapa astral")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### 🔮 Horóscopo Diário")
    st.write("Previsões personalizadas para hoje")
    
with col2:
    st.markdown("#### ✨ Mapa Astral")
    st.write("Calcule seu mapa natal completo")
    
with col3:
    st.markdown("#### 💕 Compatibilidade")
    st.write("Descubra a sintonia entre signos")

st.divider()

# CTA para premium
st.info("💎 **Premium**: Interpretações completas, relatórios PDF e consultas ilimitadas - R$ 19,90/mês")
