import streamlit as st
from utils.gemini_ai import analisar_compatibilidade

st.set_page_config(page_title="Compatibilidade", page_icon="💕", layout="wide")

st.title("💕 Análise de Compatibilidade")
st.markdown("### Descubra a sintonia astrológica entre você e outra pessoa")

signos = ["Áries", "Touro", "Gêmeos", "Câncer", "Leão", "Virgem",
          "Libra", "Escorpião", "Sagitário", "Capricórnio", "Aquário", "Peixes"]

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 👤 Primeira Pessoa")
    signo1 = st.selectbox("Signo Solar:", signos, key="signo1")
    nome1 = st.text_input("Nome (opcional):", placeholder="Ex: Maria", key="nome1")

with col2:
    st.markdown("#### 💫 Segunda Pessoa")
    signo2 = st.selectbox("Signo Solar:", signos, key="signo2", index=6)
    nome2 = st.text_input("Nome (opcional):", placeholder="Ex: João", key="nome2")

tipo_relacao = st.radio("Tipo de relacionamento:", ["Romântico 💖", "Amizade 🤝", "Profissional 💼"], horizontal=True)

analisar_btn = st.button("🔮 Analisar Compatibilidade", type="primary", use_container_width=True)

if analisar_btn:
    if signo1 == signo2:
        st.warning("⚠️ Ambos os signos são iguais. A análise será sobre a dinâmica entre pessoas do mesmo signo.")
    
    with st.spinner("✨ Analisando a sintonia astrológica..."):
        try:
            tipo = tipo_relacao.split()[0]
            nome_exibicao1 = nome1 if nome1 else signo1
            nome_exibicao2 = nome2 if nome2 else signo2
            
            resultado = analisar_compatibilidade(signo1, signo2, tipo)
            
            st.markdown("---")
            st.markdown(f"## 💫 Compatibilidade: {nome_exibicao1} × {nome_exibicao2}")
            
            elementos = {
                "Áries": "Fogo", "Leão": "Fogo", "Sagitário": "Fogo",
                "Touro": "Terra", "Virgem": "Terra", "Capricórnio": "Terra",
                "Gêmeos": "Ar", "Libra": "Ar", "Aquário": "Ar",
                "Câncer": "Água", "Escorpião": "Água", "Peixes": "Água"
            }
            
            elem1 = elementos[signo1]
            elem2 = elementos[signo2]
            
            if elem1 == elem2:
                score = 85
                cor = "🟢"
            elif (elem1 in ["Fogo", "Ar"] and elem2 in ["Fogo", "Ar"]) or \
                 (elem1 in ["Terra", "Água"] and elem2 in ["Terra", "Água"]):
                score = 75
                cor = "🟡"
            else:
                score = 60
                cor = "🟠"
            
            col_score, col_elementos = st.columns([1, 2])
            
            with col_score:
                st.metric("Score de Compatibilidade", f"{score}%")
                st.markdown(f"{cor} **{'Excelente' if score >= 80 else 'Boa' if score >= 70 else 'Moderada'}**")
            
            with col_elementos:
                st.markdown(f"**{signo1}** ({elem1}) × **{signo2}** ({elem2})")
                st.progress(score / 100)
            
            st.markdown("---")
            st.markdown("### 📝 Análise Detalhada")
            st.info(resultado)
            
            st.markdown("---")
            col_pos, col_des = st.columns(2)
            
            with col_pos:
                st.markdown("#### ✅ Pontos Fortes")
                st.success("- Complementaridade de energias\n- Respeito mútuo\n- Crescimento conjunto")
            
            with col_des:
                st.markdown("#### ⚠️ Desafios")
                st.warning("- Diferenças de ritmo\n- Necessidade de comunicação\n- Espaço individual")
            
            st.divider()
            st.warning("💎 **Sinastria Completa no Premium** - R$ 19,90/mês")
            
        except Exception as e:
            st.error(f"⚠️ Erro ao analisar: {str(e)}")

st.divider()
st.markdown("### 📚 Sobre Compatibilidade Astrológica")
st.markdown("""
**Versão Gratuita**: Compatibilidade básica entre signos solares

**Versão Premium**: Sinastria completa com todos os planetas
""")
