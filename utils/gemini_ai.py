"""
Módulo de integração com Gemini API para interpretações astrológicas
"""
import google.generativeai as genai
import streamlit as st
from datetime import datetime

# Configurar API do Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

@st.cache_data(ttl=86400)  # Cache de 24 horas
def gerar_horoscopo(signo, data):
    """
    Gera horóscopo diário para um signo específico
    
    Args:
        signo (str): Nome do signo (ex: 'Áries', 'Touro')
        data (datetime.date): Data da previsão
    
    Returns:
        str: Texto do horóscopo gerado
    """
    try:
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
        prompt = f"""Gere um horóscopo para {signo} para o dia {data.strftime('%d/%m/%Y')}.

Estruture em 3 seções curtas:
- ❤️ Amor e Relacionamentos
- 💼 Trabalho e Finanças  
- 🧘 Saúde e Bem-estar

Tom: acolhedor, místico e positivo. Máximo 150 palavras no total."""
        
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"Erro ao gerar horóscopo: {str(e)}\n\nVerifique se a API key do Gemini está configurada corretamente."


@st.cache_data(ttl=3600)  # Cache de 1 hora
def interpretar_mapa_basico(posicoes_planetas):
    """
    Gera interpretação básica de um mapa astral
    
    Args:
        posicoes_planetas (dict): Dicionário com posições dos planetas
    
    Returns:
        str: Interpretação textual
    """
    try:
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
    
    except Exception as e:
        return f"Erro ao interpretar mapa: {str(e)}"


@st.cache_data(ttl=3600)
def analisar_compatibilidade(signo1, signo2, tipo_relacao):
    """
    Analisa compatibilidade astrológica entre dois signos
    
    Args:
        signo1 (str): Primeiro signo
        signo2 (str): Segundo signo
        tipo_relacao (str): Tipo de relacionamento (Romântico, Amizade, Profissional)
    
    Returns:
        str: Análise de compatibilidade
    """
    try:
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
    
    except Exception as e:
        return f"Erro ao analisar compatibilidade: {str(e)}"
