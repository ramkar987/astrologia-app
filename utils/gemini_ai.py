import google.generativeai as genai
import streamlit as st
from datetime import datetime

# Configurar API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

@st.cache_data(ttl=86400)  # Cache de 24h
def gerar_horoscopo(signo, data):
    """Gera horóscopo diário com Gemini"""
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    prompt = f"""Gere um horóscopo para {signo} para o dia {data.strftime('%d/%m/%Y')}.

Estruture em 3 seções curtas:
- ❤️ Amor e Relacionamentos
- 💼 Trabalho e Finanças  
- 🧘 Saúde e Bem-estar

Tom: acolhedor, místico e positivo. Máximo 150 palavras no total."""
    
    response = model.generate_content(prompt)
    return response.text

@st.cache_data(ttl=3600)  # Cache de 1h
def interpretar_mapa_basico(posicoes_planetas):
    """Interpretação básica do mapa com Gemini"""
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    sol = posicoes_planetas['Sol']['signo']
    lua = posicoes_planetas['Lua']['signo']
    
    prompt = f"""Faça uma interpretação astrológica básica para:
- Sol em {sol}
- Lua em {lua}

Foque em: personalidade essencial e mundo emocional.
Máximo 100 palavras, tom acolhedor."""
    
    response = model.generate_content(prompt)
    return response.text

@st.cache_data(ttl=3600)
def analisar_compatibilidade(signo1, signo2, tipo_relacao):
    """Analisa compatibilidade entre dois signos"""
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    prompt = f"""Analise a compatibilidade astrológica entre {signo1} e {signo2} 
em um relacionamento {tipo_relacao}.

Inclua:
- Dinâmica geral da relação
- Pontos de harmonia
- Possíveis desafios
- Dicas para melhorar a conexão

Máximo 200 palavras, tom positivo e construtivo."""
    
    response = model.generate_content(prompt)
    return response.text
