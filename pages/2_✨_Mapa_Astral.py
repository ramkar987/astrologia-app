import streamlit as st
from datetime import datetime, time
from utils.astro_calc import calcular_mapa
from utils.geocoding import buscar_coordenadas, sugerir_cidades_brasil

st.set_page_config(page_title="Mapa Astral", page_icon="✨", layout="wide")

st.title("✨ Mapa Astral Natal")
st.markdown("### Descubra as posições planetárias no momento do seu nascimento")

# Armazenar dados no session_state
if 'latitude' not in st.session_state:
    st.session_state.latitude = -30.0346
if 'longitude' not in st.session_state:
    st.session_state.longitude = -51.2177

with st.form("dados_nascimento"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📅 Data de Nascimento")
        data_nasc = st.date_input("Selecione a data:", value=datetime(1990, 1, 1),
                                   min_value=datetime(1900, 1, 1), max_value=datetime.now())
        hora_nasc = st.time_input("Hora de nascimento:", value=time(12, 0))
    
    with col2:
        st.markdown("#### 📍 Local de Nascimento")
        
        # Opção: buscar automaticamente ou inserir manualmente
        modo = st.radio("Como deseja informar?", 
                       ["🔍 Buscar cidade", "✍️ Inserir coordenadas manualmente"],
                       horizontal=True)
        
        if modo == "🔍 Buscar cidade":
            cidade = st.text_input("Digite a cidade:", placeholder="Ex: Porto Alegre, RS")
            
            # Botão para buscar coordenadas (fora do form)
            if cidade:
                st.caption("📍 As coordenadas serão calculadas automaticamente ao processar")
            
            # Valores temporários (serão atualizados)
            latitude = st.session_state.latitude
            longitude = st.session_state.longitude
            
        else:
            cidade = st.text_input("Cidade (referência):", placeholder="Ex: Porto Alegre")
            col_lat, col_lon = st.columns(2)
            with col_lat:
                latitude = st.number_input("Latitude:", value=st.session_state.latitude, format="%.4f")
            with col_lon:
                longitude = st.number_input("Longitude:", value=st.session_state.longitude, format="%.4f")
            
            st.caption("💡 Dica: Pesquise 'latitude longitude [sua cidade]' no Google")
    
    calcular_btn = st.form_submit_button("🌙 Calcular Mapa Astral", type="primary", use_container_width=True)

# Processamento
if calcular_btn:
    if not cidade:
        st.error("⚠️ Por favor, preencha a cidade de nascimento")
    else:
        # Se modo busca automática, buscar coordenadas
        if modo == "🔍 Buscar cidade":
            with st.spinner(f"🔍 Buscando coordenadas de {cidade}..."):
                lat_encontrada, lon_encontrada, endereco_completo = buscar_coordenadas(cidade)
                
                if lat_encontrada and lon_encontrada:
                    latitude = lat_encontrada
                    longitude = lon_encontrada
                    st.session_state.latitude = latitude
                    st.session_state.longitude = longitude
                    st.success(f"📍 Localização encontrada: {endereco_completo}")
                else:
                    st.error("⚠️ Não foi possível encontrar a cidade. Tente incluir o estado (ex: 'Porto Alegre, RS') ou use coordenadas manuais.")
                    st.stop()
        
        with st.spinner("🔮 Calculando posições planetárias..."):
            try:
                posicoes = calcular_mapa(data_nasc, hora_nasc, latitude, longitude)
                
                st.success(f"✅ Mapa calculado para {data_nasc.strftime('%d/%m/%Y')} às {hora_nasc.strftime('%H:%M')} em {cidade}")
                st.caption(f"📍 Coordenadas: {latitude}, {longitude}")
                
                st.markdown("---")
                st.markdown("## 🌟 Posições Planetárias")
                
                col_a, col_b = st.columns(2)
                planetas_lista = list(posicoes.items())
                metade = len(planetas_lista) // 2
                
                with col_a:
                    for planeta, dados in planetas_lista[:metade]:
                        st.markdown(f"**{planeta}** em {dados['signo']}")
                        st.caption(f"{dados['grau']:.2f}° | Longitude: {dados['longitude']:.2f}°")
                        st.markdown("---")
                
                with col_b:
                    for planeta, dados in planetas_lista[metade:]:
                        st.markdown(f"**{planeta}** em {dados['signo']}")
                        st.caption(f"{dados['grau']:.2f}° | Longitude: {dados['longitude']:.2f}°")
                        st.markdown("---")
                
                st.markdown("---")
                st.markdown("## 💬 Interpretação Básica (Gratuita)")
                
                interpretacao = f"""
**Sol em {posicoes['Sol']['signo']}**: Representa sua essência, identidade e forma de brilhar no mundo.

**Lua em {posicoes['Lua']['signo']}**: Revela seu mundo emocional, necessidades afetivas e como você processa sentimentos.

**Mercúrio em {posicoes['Mercúrio']['signo']}**: Mostra seu estilo de comunicação e forma de pensar.
                """
                st.info(interpretacao)
                
                st.warning("💎 **Premium**: Interpretação completa com todos os planetas + Casas + Ascendente + Aspectos + Relatório PDF - R$ 19,90/mês")
                
            except Exception as e:
                st.error(f"⚠️ Erro ao calcular mapa: {str(e)}")

# Cidades sugeridas (expandable)
with st.expander("🏙️ Ver coordenadas de cidades principais"):
    cidades_sugeridas = sugerir_cidades_brasil()
    
    cols = st.columns(3)
    for idx, (cidade_nome, coords) in enumerate(cidades_sugeridas.items()):
        with cols[idx % 3]:
            st.markdown(f"**{cidade_nome}**")
            st.caption(f"Lat: {coords[0]}, Lon: {coords[1]}")

st.divider()
st.markdown("### ℹ️ Sobre o Mapa Astral")
st.markdown("""
O mapa astral mostra as posições planetárias no momento exato do seu nascimento.

**Elementos principais:**
- **Planetas**: Energias e funções psicológicas
- **Signos**: Como as energias se expressam
- **Casas**: Áreas da vida afetadas (Premium)
- **Aspectos**: Relações entre planetas (Premium)
""")
