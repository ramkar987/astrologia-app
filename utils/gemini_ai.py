"""
Astrologia com Groq API (GRATUITO - 14.400 requests/dia!)
Compatible com OpenAI SDK
"""
import streamlit as st
from openai import OpenAI
from datetime import datetime

@st.cache_data(ttl=86400)  # Cache 24h
def gerar_horoscopo(signo, data):
    """Gera horóscopo diário"""
    client = OpenAI(
        api_key=st.secrets["GROQ_API_KEY"],
        base_url="https://api.groq.com/openai/v1"
    )
    
    prompt = f"""Gere horóscopo para {signo} - {data.strftime('%d/%m/%Y')}

**Estrutura obrigatória:**
- ❤️ **Amor e Relacionamentos**
- 💼 **Trabalho e Finanças**
- 🧘 **Saúde e Bem-estar**

Místico, acolhedor, positivo. Máximo 120 palavras."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # Grátis e excelente
        messages=[{"role": "user", "content": prompt}],
        max_tokens=250,
        temperature=0.8
    )
    
    return response.choices[0].message.content

@st.cache_data(ttl=3600)
def analisar_compatibilidade(signo1, signo2, tipo_relacao):
    """Análise de compatibilidade"""
    client = OpenAI(
        api_key=st.secrets["GROQ_API_KEY"],
        base_url="https://api.groq.com/openai/v1"
    )
    
    prompt = f"""Compatibilidade astrológica: {signo1} x {signo2}
Tipo: {tipo_relacao}

**Estrutura:**
- Dinâmica geral
- Pontos de harmonia
- Possíveis desafios
- Dicas práticas

Positivo e construtivo. Máximo 150 palavras."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.7
    )
    
    return response.choices[0].message.content

@st.cache_data(ttl=3600)
def interpretar_mapa_basico(posicoes_planetas):
    """Interpretação básica mapa astral"""
    client = OpenAI(
        api_key=st.secrets["GROQ_API_KEY"],
        base_url="https://api.groq.com/openai/v1"
    )
    
    sol = posicoes_planetas.get('Sol', {}).get('signo', 'desconhecido')
    lua = posicoes_planetas.get('Lua', {}).get('signo', 'desconhecido')
    
    prompt = f"""Interpretação astrológica básica:

**Sol em {sol}**: Essência/identidade
**Lua em {lua}**: Emoções/necessidades

Acolhedor, 80 palavras máximo."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.7
    )
    
    return response.choices[0].message.content
