import streamlit as st
from datetime import datetime, time
import sys
import streamlit as st
from datetime import datetime, time
from utils.astro_calc import calcular_mapa  # ✅ Import direto
from utils.gemini_ai import interpretar_mapa_basico



st.set_page_config(page_title="Mapa Astral", page_icon="✨", layout="wide")

st.title("✨ Mapa Astral Natal")
st.markdown("### Descubra as posições planetárias no momento do seu nascimento")

# Formulário de dados
with st.form("dados_nascimento"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📅 Data de Nascimento")
        data_nasc = st.date_input(
            "Selecione a data:",
            value=datetime(1990, 1, 1),
            min_value=datetime(1900, 1, 1),
            max_value=datetime.now()
        )
        
        hora_nasc = st.time_input(
            "Hora de nascimento:",
            value=time(12, 0)
        )
    
    with col2:
        st.markdown("#### 📍 Local de Nascimento")
        cidade = st.text_input("Cidade:", placeholder="Ex: Porto Alegre")
        
        col_lat, col_lon = st.columns(2)
        with col_lat:
            latitude = st.number_input("Latitude:", value=-30.03, format="%.4f")
        with col_lon:
            longitude = st.number_input("Longitude:", value=-51.23, format="%.4f")
        
        st.caption("💡 Dica: Pesquise 'latitude longitude [sua cidade]' no Google")
    
    calcular_btn = st.form_submit_button("🌙 Calcular Mapa Astral", type="primary", use_container_width=True)

# Processamento
if calcular_btn:
    if not cidade:
        st.error("⚠️ Por favor, preencha a cidade de nascimento")
    else:
        with st.spinner("🔮 Calculando posições planetárias..."):
            try:
                # Calcular posições
                posicoes = calcular_mapa(data_nasc, hora_nasc, latitude, longitude)
                
                st.success(f"✅ Mapa calculado para {data_nasc.strftime('%d/%m/%Y')} às {hora_nasc.strftime('%H:%M')} em {cidade}")
                
                # Exibir posições
                st.markdown("---")
                st.markdown("## 🌟 Posições Planetárias")
                
                # Criar tabela de planetas
                col_a, col_b = st.columns(2)
                
                planetas_lista = list(posicoes.items())
                metade = len(planetas_lista) // 2
                
                with col_a:
                    for planeta, dados in planetas_lista[:metade]:
                        with st.container():
                            st.markdown(f"**{planeta}** em {dados['signo']}")
                            st.caption(f"{dados['grau']:.2f}° | Longitude: {dados['longitude']:.2f}°")
                            st.markdown("---")
                
                with col_b:
                    for planeta, dados in planetas_lista[metade:]:
                        with st.container():
                            st.markdown(f"**{planeta}** em {dados['signo']}")
                            st.caption(f"{dados['grau']:.2f}° | Longitude: {dados['longitude']:.2f}°")
                            st.markdown("---")
                
                # Interpretação básica (versão gratuita limitada)
                st.markdown("---")
                st.markdown("## 💬 Interpretação Básica (Gratuita)")
                
                interpretacao_basica = f"""
                **Sol em {posicoes['Sol']['signo']}**: Representa sua essência e identidade.
                
                **Lua em {posicoes['Lua']['signo']}**: Suas emoções e mundo interior.
                
                **Ascendente**: Para calcular o ascendente com precisão, considere a versão Premium.
                """
                
                st.info(interpretacao_basica)
                
                # CTA Premium
                st.warning("💎 **Desbloqueie Interpretação Completa no Premium:**\n- Análise detalhada de todos os planetas\n- Casas astrológicas\n- Aspectos planetários\n- Relatório em PDF\n\n**R$ 19,90/mês**")
                
            except Exception as e:
                st.error(f"⚠️ Erro ao calcular mapa: {str(e)}")
                st.info("Verifique se os dados estão corretos e se a biblioteca pyswisseph está instalada.")

# Informações extras
st.divider()
st.markdown("### ℹ️ Sobre o Mapa Astral")
st.markdown("""
O mapa astral é uma fotografia do céu no momento exato do seu nascimento. 
Ele mostra onde cada planeta estava posicionado e como eles se relacionam entre si.

**Principais elementos:**
- **Planetas**: Representam energias e funções psicológicas
- **Signos**: Mostram como essas energias se expressam
- **Casas**: Indicam áreas da vida afetadas
- **Aspectos**: Relações angulares entre planetas
""")
