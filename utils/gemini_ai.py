"""
Módulo de integração com Gemini API para interpretações astrológicas
"""
try:
    import google.generativeai as genai
    GEMINI_DISPONIVEL = True
except ImportError:
    GEMINI_DISPONIVEL = False
    
import streamlit as st
from datetime import datetime


def configurar_gemini():
    """Configura a API do Gemini se disponível"""
    if GEMINI_DISPONIVEL:
        try:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            return True
        except Exception as e:
            st.error(f"Erro ao configurar Gemini: {e}")
            return False
    return False


def gerar_horoscopo(signo, data):
    """
    Gera horóscopo diário para um signo específico
    """
    if not GEMINI_DISPONIVEL:
        return """⚠️ **Modo de demonstração**
        
❤️ **Amor e Relacionamentos**: As energias planetárias favorecem conexões profundas hoje.

💼 **Trabalho e Finanças**: Momento propício para planejamento e organização de projetos.

🧘 **Saúde e Bem-estar**: Priorize o autocuidado e momentos de descanso.

_Para previsões personalizadas, aguarde a configuração completa da API._"""
    
    try:
        if not configurar_gemini():
            return "Erro: API não configurada corretamente."
        
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""Gere um horóscopo para {signo} para o dia {data.strftime('%d/%m/%Y')}.

Estruture em 3 seções curtas:
- ❤️ Amor e Relacionamentos
- 💼 Trabalho e Finanças  
- 🧘 Saúde e Bem-estar

Tom: acolhedor, místico e positivo. Máximo 150 palavras no total."""
        
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"Erro ao gerar horóscopo: {str(e)}\n\nVerifique se a API key está configurada corretamente."


def interpretar_mapa_basico(posicoes_planetas):
    """
    Gera interpretação básica de um mapa astral
    """
    if not GEMINI_DISPONIVEL:
        sol = posicoes_planetas.get('Sol', {}).get('signo', 'desconhecido')
        lua = posicoes_planetas.get('Lua', {}).get('signo', 'desconhecido')
        return f"""**Sol em {sol}**: Representa sua essência, identidade e forma de expressar sua vitalidade.

**Lua em {lua}**: Revela seu mundo emocional, necessidades afetivas e como você processa sentimentos.

_Interpretação completa disponível em breve._"""
    
    try:
        if not configurar_gemini():
            return "Erro: API não configurada."
        
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


def analisar_compatibilidade(signo1, signo2, tipo_relacao):
    """
    Analisa compatibilidade astrológica entre dois signos
    """
    if not GEMINI_DISPONIVEL:
        return f"""**{signo1} × {signo2}**

A compatibilidade entre {signo1} e {signo2} em um relacionamento {tipo_relacao} apresenta dinâmicas interessantes.

Cada combinação astrológica traz seus desafios e oportunidades de crescimento. A chave está na comunicação aberta e respeito às diferenças.

_Análise completa disponível em breve._"""
    
    try:
        if not configurar_gemini():
            return "Erro: API não configurada."
        
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

