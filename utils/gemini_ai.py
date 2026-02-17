"""
Módulo para interpretações astrológicas com múltiplas APIs
Sistema de fallback automático e silencioso
"""
import streamlit as st
from datetime import datetime

# Tentar importar as bibliotecas
try:
    import google.generativeai as genai
    GEMINI_DISPONIVEL = True
except ImportError:
    GEMINI_DISPONIVEL = False

try:
    from openai import OpenAI
    OPENAI_DISPONIVEL = True
except ImportError:
    OPENAI_DISPONIVEL = False


def configurar_apis():
    """Configura as APIs disponíveis"""
    apis_config = {
        'gemini': False,
        'openai': False
    }
    
    if GEMINI_DISPONIVEL and "GEMINI_API_KEY" in st.secrets:
        try:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            apis_config['gemini'] = True
        except:
            pass
    
    if OPENAI_DISPONIVEL and "OPENAI_API_KEY" in st.secrets:
        apis_config['openai'] = True
    
    return apis_config


@st.cache_data(ttl=86400)
def gerar_horoscopo(signo, data):
    """Gera horóscopo usando APIs com fallback automático"""
    prompt = f"""Gere um horóscopo para {signo} para o dia {data.strftime('%d/%m/%Y')}.

Estruture em 3 seções curtas:
- ❤️ Amor e Relacionamentos
- 💼 Trabalho e Finanças  
- 🧘 Saúde e Bem-estar

Tom: acolhedor, místico e positivo. Máximo 150 palavras no total."""
    
    apis = configurar_apis()
    
    # Tentar Gemini
    if apis['gemini']:
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            return response.text
        except:
            pass  # Falha silenciosa
    
    # Tentar OpenAI
    if apis['openai']:
        try:
            client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um astrólogo experiente e acolhedor."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300,
                temperature=0.7
            )
            return response.choices[0].message.content
        except:
            pass  # Falha silenciosa
    
    # Fallback estático (sempre funciona)
    return gerar_horoscopo_estatico(signo, data)


@st.cache_data(ttl=3600)
def analisar_compatibilidade(signo1, signo2, tipo_relacao):
    """Analisa compatibilidade usando APIs com fallback"""
    prompt = f"""Analise a compatibilidade astrológica entre {signo1} e {signo2} 
em um relacionamento {tipo_relacao}.

Inclua:
- Dinâmica geral da relação
- Pontos de harmonia
- Possíveis desafios
- Dicas para melhorar a conexão

Máximo 200 palavras, tom positivo e construtivo."""
    
    apis = configurar_apis()
    
    # Tentar Gemini
    if apis['gemini']:
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            return response.text
        except:
            pass
    
    # Tentar OpenAI
    if apis['openai']:
        try:
            client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um astrólogo especialista em relacionamentos."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=400,
                temperature=0.7
            )
            return response.choices[0].message.content
        except:
            pass
    
    # Fallback estático
    return analisar_compatibilidade_estatica(signo1, signo2, tipo_relacao)


@st.cache_data(ttl=3600)
def interpretar_mapa_basico(posicoes_planetas):
    """Interpreta mapa astral usando APIs com fallback"""
    sol = posicoes_planetas['Sol']['signo']
    lua = posicoes_planetas['Lua']['signo']
    
    prompt = f"""Faça uma interpretação astrológica básica para:
- Sol em {sol}
- Lua em {lua}

Foque em: personalidade essencial e mundo emocional.
Máximo 100 palavras, tom acolhedor."""
    
    apis = configurar_apis()
    
    # Tentar Gemini
    if apis['gemini']:
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            return response.text
        except:
            pass
    
    # Tentar OpenAI
    if apis['openai']:
        try:
            client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um astrólogo especialista em mapas natais."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200,
                temperature=0.7
            )
            return response.choices[0].message.content
        except:
            pass
    
    # Fallback estático
    return f"""**Sol em {sol}**: Representa sua essência central, identidade e forma de expressar vitalidade no mundo. É sua luz que brilha naturalmente.

**Lua em {lua}**: Revela seu mundo emocional interior, necessidades afetivas e como você processa sentimentos. É seu porto seguro interior."""


# ===== FUNÇÕES DE FALLBACK ESTÁTICO =====

def gerar_horoscopo_estatico(signo, data):
    """Versão estática de alta qualidade"""
    horoscopos = {
        "Áries": """❤️ **Amor e Relacionamentos**
Momento favorável para expressar sentimentos com sinceridade. Sua paixão está em alta.

💼 **Trabalho e Finanças**
Energia competitiva favorece novos projetos. Confie em sua coragem para decisões importantes.

🧘 **Saúde e Bem-estar**
Canalize energia em atividades físicas. Cuidado com impulsividade.""",
        
        # ... (restante dos signos como antes)
    }
    
    return horoscopos.get(signo, "Horóscopo temporariamente indisponível.")


def analisar_compatibilidade_estatica(signo1, signo2, tipo_relacao):
    """Análise estática de compatibilidade"""
    elementos = {
        "Áries": "Fogo", "Leão": "Fogo", "Sagitário": "Fogo",
        "Touro": "Terra", "Virgem": "Terra", "Capricórnio": "Terra",
        "Gêmeos": "Ar", "Libra": "Ar", "Aquário": "Ar",
        "Câncer": "Água", "Escorpião": "Água", "Peixes": "Água"
    }
    
    elem1 = elementos.get(signo1)
    elem2 = elementos.get(signo2)
    
    if elem1 == elem2:
        dinamica = f"Ambos compartilham o elemento {elem1}, criando compreensão natural e sintonia imediata."
        harmonia = "Valores similares facilitam convivência"
        desafios = "Excesso de similaridade pode gerar estagnação"
    elif (elem1 in ["Fogo", "Ar"] and elem2 in ["Fogo", "Ar"]) or \
         (elem1 in ["Terra", "Água"] and elem2 in ["Terra", "Água"]):
        dinamica = f"{elem1} e {elem2} são elementos compatíveis que se complementam naturalmente."
        harmonia = "Diferenças complementares enriquecem a relação"
        desafios = "Ritmos distintos requerem ajustes"
    else:
        dinamica = f"A combinação entre {elem1} e {elem2} traz desafios interessantes e oportunidades de crescimento."
        harmonia = "Perspectivas diferentes ampliam horizontes"
        desafios = "Temperamentos contrastantes exigem esforço"
    
    return f"""**Dinâmica {tipo_relacao}**

{dinamica}

**Pontos de Harmonia:**
• {harmonia}
• Potencial para equilíbrio através do respeito mútuo
• Oportunidade de evoluir juntos

**Possíveis Desafios:**
• {desafios}
• Necessidade de comunicação clara
• Respeito às diferenças individuais

**Dicas para Fortalecer a Conexão:**
• Pratiquem escuta ativa e empatia
• Valorizem as diferenças como aprendizado
• Mantenham diálogo aberto sobre expectativas"""
