"""
Módulo de integração com Gemini API para interpretações astrológicas
"""
import google.generativeai as genai
import streamlit as st

# Configurar API do Gemini
def configurar_gemini():
    """Configura a API do Gemini"""
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        return True
    except Exception as e:
        st.error(f"Erro ao configurar Gemini: {e}")
        return False


@st.cache_data(ttl=86400)  # Cache de 24 horas
def gerar_horoscopo(signo, data):
    """Gera horóscopo diário para um signo específico"""
    try:
        if not configurar_gemini():
            return "Erro: API não configurada."
        
        model = genai.GenerativeModel('gemini-pro')
        
        prompt = f"""Gere um horóscopo para {signo} para o dia {data.strftime('%d/%m/%Y')}.

Estruture em 3 seções curtas:
- ❤️ Amor e Relacionamentos
- 💼 Trabalho e Finanças  
- 🧘 Saúde e Bem-estar

Tom: acolhedor, místico e positivo. Máximo 150 palavras no total."""
        
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"Erro ao gerar horóscopo: {str(e)}"


@st.cache_data(ttl=3600)
def analisar_compatibilidade(signo1, signo2, tipo_relacao):
    """Analisa compatibilidade astrológica entre dois signos"""
    try:
        if not configurar_gemini():
            return "Erro: API não configurada."
        
        model = genai.GenerativeModel('gemini-pro')
        
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


@st.cache_data(ttl=3600)
def interpretar_mapa_basico(posicoes_planetas):
    """Gera interpretação básica de um mapa astral"""
    try:
        if not configurar_gemini():
            return "Erro: API não configurada."
        
        model = genai.GenerativeModel('gemini-pro')
        
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
