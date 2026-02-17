"""
Módulo para interpretações astrológicas com múltiplas APIs
Sistema de fallback: Gemini → OpenAI → Estático
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
    
    # Configurar Gemini
    if GEMINI_DISPONIVEL and "GEMINI_API_KEY" in st.secrets:
        try:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            apis_config['gemini'] = True
        except:
            pass
    
    # Configurar OpenAI
    if OPENAI_DISPONIVEL and "OPENAI_API_KEY" in st.secrets:
        apis_config['openai'] = True
    
    return apis_config


@st.cache_data(ttl=86400)  # Cache de 24h
def gerar_horoscopo(signo, data):
    """
    Gera horóscopo usando APIs com fallback automático
    """
    prompt = f"""Gere um horóscopo para {signo} para o dia {data.strftime('%d/%m/%Y')}.

Estruture em 3 seções curtas:
- ❤️ Amor e Relacionamentos
- 💼 Trabalho e Finanças  
- 🧘 Saúde e Bem-estar

Tom: acolhedor, místico e positivo. Máximo 150 palavras no total."""
    
    apis = configurar_apis()
    
    # Tentar Gemini primeiro
    if apis['gemini']:
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            st.warning(f"⚠️ Gemini indisponível, tentando OpenAI...")
    
    # Fallback para OpenAI
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
        except Exception as e:
            st.warning(f"⚠️ OpenAI indisponível: {str(e)}")
    
    # Fallback estático
    return gerar_horoscopo_estatico(signo, data)


@st.cache_data(ttl=3600)
def analisar_compatibilidade(signo1, signo2, tipo_relacao):
    """
    Analisa compatibilidade usando APIs com fallback
    """
    prompt = f"""Analise a compatibilidade astrológica entre {signo1} e {signo2} 
em um relacionamento {tipo_relacao}.

Inclua:
- Dinâmica geral da relação
- Pontos de harmonia
- Possíveis desafios
- Dicas para melhorar a conexão

Máximo 200 palavras, tom positivo e construtivo."""
    
    apis = configurar_apis()
    
    # Tentar Gemini primeiro
    if apis['gemini']:
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            return response.text
        except:
            pass
    
    # Fallback para OpenAI
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
    """
    Interpreta mapa astral usando APIs com fallback
    """
    sol = posicoes_planetas['Sol']['signo']
    lua = posicoes_planetas['Lua']['signo']
    
    prompt = f"""Faça uma interpretação astrológica básica para:
- Sol em {sol}
- Lua em {lua}

Foque em: personalidade essencial e mundo emocional.
Máximo 100 palavras, tom acolhedor."""
    
    apis = configurar_apis()
    
    # Tentar Gemini primeiro
    if apis['gemini']:
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            return response.text
        except:
            pass
    
    # Fallback para OpenAI
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
    return f"""**Sol em {sol}**: Representa sua essência, identidade e forma de expressar vitalidade no mundo.

**Lua em {lua}**: Revela seu mundo emocional, necessidades afetivas e como você processa sentimentos."""


# ===== FUNÇÕES DE FALLBACK ESTÁTICO =====

def gerar_horoscopo_estatico(signo, data):
    """Versão estática de backup"""
    horoscopos = {
        "Áries": """❤️ **Amor e Relacionamentos**
Momento favorável para expressar sentimentos com sinceridade. Sua paixão está em alta.

💼 **Trabalho e Finanças**
Energia competitiva favorece novos projetos. Confie em sua coragem para decisões importantes.

🧘 **Saúde e Bem-estar**
Canalize energia em atividades físicas. Cuidado com impulsividade.""",
        
        "Touro": """❤️ **Amor e Relacionamentos**
Estabilidade emocional ao alcance. Demonstre afeto através de gestos práticos.

💼 **Trabalho e Finanças**
Persistência traz resultados concretos. Evite decisões financeiras apressadas.

🧘 **Saúde e Bem-estar**
Contato com natureza e alimentação balanceada são essenciais.""",
        
        "Gêmeos": """❤️ **Amor e Relacionamentos**
Comunicação fluida favorece novas conexões. Versatilidade atrai pessoas interessantes.

💼 **Trabalho e Finanças**
Criatividade em destaque. Explore ideias, mas foque em finalizar projetos.

🧘 **Saúde e Bem-estar**
Exercite a mente com leituras. Meditação organiza pensamentos.""",
        
        "Câncer": """❤️ **Amor e Relacionamentos**
Sensibilidade aguçada. Cultive vínculos profundos e acolha quem precisa.

💼 **Trabalho e Finanças**
Confie na intuição. Trabalhos em equipe fluem melhor hoje.

🧘 **Saúde e Bem-estar**
Cuide das emoções. Momentos em casa recarregam energias.""",
        
        "Leão": """❤️ **Amor e Relacionamentos**
Magnetismo em alta. Demonstre carinho de forma generosa e criativa.

💼 **Trabalho e Finanças**
Criatividade e liderança são reconhecidas. Assuma o protagonismo.

🧘 **Saúde e Bem-estar**
Atividades que façam você brilhar. Cuide da autoestima.""",
        
        "Virgem": """❤️ **Amor e Relacionamentos**
Atos práticos valem mais que palavras. Organize momentos especiais.

💼 **Trabalho e Finanças**
Organização e detalhes fazem diferença. Dia produtivo para análises.

🧘 **Saúde e Bem-estar**
Rotinas saudáveis. Seu corpo responde bem à disciplina.""",
        
        "Libra": """❤️ **Amor e Relacionamentos**
Harmonia favorece relacionamentos. Busque diálogos equilibrados.

💼 **Trabalho e Finanças**
Diplomacia é sua força. Negociações e parcerias prosperam.

🧘 **Saúde e Bem-estar**
Equilíbrio mente-corpo. Yoga ou meditação são benéficos.""",
        
        "Escorpião": """❤️ **Amor e Relacionamentos**
Intensidade emocional marca vínculos. Permita-se ser vulnerável.

💼 **Trabalho e Finanças**
Determinação leva longe. Investigações profundas trazem resultados.

🧘 **Saúde e Bem-estar**
Transforme emoções em ações positivas. Atividades físicas liberam tensões.""",
        
        "Sagitário": """❤️ **Amor e Relacionamentos**
Aventura anima relacionamentos. Compartilhe experiências novas.

💼 **Trabalho e Finanças**
Otimismo abre portas. Explore oportunidades com visão ampla.

🧘 **Saúde e Bem-estar**
Movimento e liberdade essenciais. Atividades ao ar livre renovam energias.""",
        
        "Capricórnio": """❤️ **Amor e Relacionamentos**
Comprometimento fortalece laços. Demonstre lealdade de forma prática.

💼 **Trabalho e Finanças**
Ambição e disciplina recompensadas. Planeje a longo prazo.

🧘 **Saúde e Bem-estar**
Não negligencie descanso. Equilíbrio trabalho-relaxamento é fundamental.""",
        
        "Aquário": """❤️ **Amor e Relacionamentos**
Originalidade atrai pessoas interessantes. Valorize amizades autênticas.

💼 **Trabalho e Finanças**
Ideias inovadoras em destaque. Colabore em projetos transformadores.

🧘 **Saúde e Bem-estar**
Liberdade é essencial. Explore atividades que expressem unicidade.""",
        
        "Peixes": """❤️ **Amor e Relacionamentos**
Compaixão profunda vínculos. Esteja presente emocionalmente.

💼 **Trabalho e Finanças**
Criatividade e intuição guiam decisões. Confie em sua sensibilidade.

🧘 **Saúde e Bem-estar**
Práticas espirituais nutrem alma. Meditação, música e água trazem paz."""
    }
    
    return horoscopos.get(signo, "Horóscopo temporariamente indisponível.")


def analisar_compatibilidade_estatica(signo1, signo2, tipo_relacao):
    """Versão estática de backup"""
    elementos = {
        "Áries": "Fogo", "Leão": "Fogo", "Sagitário": "Fogo",
        "Touro": "Terra", "Virgem": "Terra", "Capricórnio": "Terra",
        "Gêmeos": "Ar", "Libra": "Ar", "Aquário": "Ar",
        "Câncer": "Água", "Escorpião": "Água", "Peixes": "Água"
    }
    
    elem1 = elementos.get(signo1)
    elem2 = elementos.get(signo2)
    
    return f"""**Dinâmica {tipo_relacao}**

A combinação entre {signo1} ({elem1}) e {signo2} ({elem2}) apresenta dinâmicas únicas.

**Pontos de Harmonia:**
• Complementaridade de energias
• Potencial para crescimento mútuo
• Oportunidades de aprendizado conjunto

**Possíveis Desafios:**
• Diferenças de ritmo e temperamento
• Necessidade de comunicação clara
• Respeito ao espaço individual

**Dicas:**
• Pratiquem escuta ativa
• Valorizem as diferenças
• Mantenham diálogo aberto"""
