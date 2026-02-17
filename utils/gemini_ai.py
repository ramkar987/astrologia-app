"""
Módulo para interpretações astrológicas
Versão com respostas estáticas (sem necessidade de API externa)
"""
import streamlit as st
from datetime import datetime

# Flag para testar com API depois
USAR_API = False  # Mude para True quando resolver a API key


def gerar_horoscopo(signo, data):
    """
    Gera horóscopo diário para um signo específico
    """
    horoscopos = {
        "Áries": """❤️ **Amor e Relacionamentos**
Momento favorável para expressar seus sentimentos com sinceridade. As estrelas sugerem conversas importantes com quem você ama.

💼 **Trabalho e Finanças**
Sua energia competitiva está em alta. Ótimo dia para iniciar projetos e tomar a liderança em situações desafiadoras.

🧘 **Saúde e Bem-estar**
Canalize seu excesso de energia em atividades físicas. Cuidado com impulsividade e estresse.""",

        "Touro": """❤️ **Amor e Relacionamentos**
A estabilidade emocional que você busca está ao seu alcance. Valorize momentos de qualidade com pessoas especiais.

💼 **Trabalho e Finanças**
Persistência e paciência trarão resultados concretos. Evite decisões apressadas, especialmente financeiras.

🧘 **Saúde e Bem-estar**
Priorize o contato com a natureza e alimentação balanceada. Seu corpo pede cuidado e atenção.""",

        "Gêmeos": """❤️ **Amor e Relacionamentos**
Comunicação fluida favorece novas conexões. Sua versatilidade atrai pessoas interessantes para sua vida.

💼 **Trabalho e Finanças**
Sua criatividade está em destaque. Explore múltiplas ideias, mas foque em finalizar o que começou.

🧘 **Saúde e Bem-estar**
Exercite sua mente com leituras e aprendizado. Evite dispersão e cultive momentos de silêncio.""",

        "Câncer": """❤️ **Amor e Relacionamentos**
Sua sensibilidade está aguçada. Cultive vínculos afetivos profundos e acolha quem precisa de você.

💼 **Trabalho e Finanças**
Confie em sua intuição para tomar decisões. Trabalhos em equipe tendem a fluir melhor hoje.

🧘 **Saúde e Bem-estar**
Cuide de suas emoções. Momentos em família ou em casa ajudam a recarregar energias.""",

        "Leão": """❤️ **Amor e Relacionamentos**
Seu magnetismo está em alta. Aproveite para fortalecer laços e demonstrar seu carinho de forma generosa.

💼 **Trabalho e Finanças**
Sua criatividade e liderança são reconhecidas. Assuma o protagonismo e inspire outros.

🧘 **Saúde e Bem-estar**
Pratique atividades que façam você brilhar. Cuide da autoestima e celebre suas conquistas.""",

        "Virgem": """❤️ **Amor e Relacionamentos**
Atos práticos de amor valem mais que palavras. Demonstre afeto através de gestos cuidadosos.

💼 **Trabalho e Finanças**
Sua organização e atenção aos detalhes fazem a diferença. Dia produtivo para tarefas minuciosas.

🧘 **Saúde e Bem-estar**
Estabeleça rotinas saudáveis. Seu corpo responde bem à disciplina e cuidados regulares.""",

        "Libra": """❤️ **Amor e Relacionamentos**
Harmonia e equilíbrio favorecem seus relacionamentos. Busque diálogos equilibrados e evite conflitos.

💼 **Trabalho e Finanças**
Sua diplomacia é sua maior força. Negociações e parcerias tendem a prosperar.

🧘 **Saúde e Bem-estar**
Busque equilíbrio entre mente e corpo. Práticas como yoga ou meditação são benéficas.""",

        "Escorpião": """❤️ **Amor e Relacionamentos**
Intensidade emocional marca seus vínculos. Permita-se ser vulnerável com quem confia.

💼 **Trabalho e Finanças**
Sua determinação leva você longe. Investigações e trabalhos profundos trazem resultados.

🧘 **Saúde e Bem-estar**
Transforme emoções intensas em ações positivas. Atividades físicas ajudam a liberar tensões.""",

        "Sagitário": """❤️ **Amor e Relacionamentos**
Aventura e espontaneidade animam seus relacionamentos. Compartilhe experiências novas com quem ama.

💼 **Trabalho e Finanças**
Seu otimismo abre portas. Explore novas oportunidades e confie em sua visão ampla.

🧘 **Saúde e Bem-estar**
Movimento e liberdade são essenciais. Pratique atividades ao ar livre e expanda horizontes.""",

        "Capricórnio": """❤️ **Amor e Relacionamentos**
Responsabilidade e comprometimento fortalecem laços. Demonstre sua lealdade de forma prática.

💼 **Trabalho e Finanças**
Sua ambição e disciplina são recompensadas. Planeje a longo prazo e seja paciente com resultados.

🧘 **Saúde e Bem-estar**
Não negligencie descanso. Equilíbrio entre trabalho e relaxamento é fundamental.""",

        "Aquário": """❤️ **Amor e Relacionamentos**
Originalidade atrai pessoas interessantes. Valorize amizades e conexões autênticas.

💼 **Trabalho e Finanças**
Ideias inovadoras estão em destaque. Colabore em projetos que promovam mudanças positivas.

🧘 **Saúde e Bem-estar**
Liberdade e individualidade são essenciais. Explore atividades que expressem sua unicidade.""",

        "Peixes": """❤️ **Amor e Relacionamentos**
Compaixão e empatia profundam seus vínculos. Esteja presente emocionalmente para quem precisa.

💼 **Trabalho e Finanças**
Criatividade e intuição guiam suas decisões. Confie em sua sensibilidade para resolver problemas.

🧘 **Saúde e Bem-estar**
Práticas espirituais e artísticas nutrem sua alma. Cuide de seu mundo interior."""
    }
    
    return horoscopos.get(signo, "Horóscopo temporariamente indisponível.")


def analisar_compatibilidade(signo1, signo2, tipo_relacao):
    """
    Analisa compatibilidade entre dois signos
    """
    # Determinar elementos
    elementos = {
        "Áries": "Fogo", "Leão": "Fogo", "Sagitário": "Fogo",
        "Touro": "Terra", "Virgem": "Terra", "Capricórnio": "Terra",
        "Gêmeos": "Ar", "Libra": "Ar", "Aquário": "Ar",
        "Câncer": "Água", "Escorpião": "Água", "Peixes": "Água"
    }
    
    elem1 = elementos.get(signo1, "Desconhecido")
    elem2 = elementos.get(signo2, "Desconhecido")
    
    # Análise baseada em elementos
    if elem1 == elem2:
        dinamica = f"Ambos compartilham o elemento {elem1}, criando uma compreensão natural e sintonia imediata. Vocês falam a mesma língua emocional."
        harmonia = "Valores e temperamentos similares facilitam a convivência"
        desafios = "Excesso de similaridade pode gerar estagnação ou falta de desafios construtivos"
        
    elif (elem1 in ["Fogo", "Ar"] and elem2 in ["Fogo", "Ar"]) or \
         (elem1 in ["Terra", "Água"] and elem2 in ["Terra", "Água"]):
        dinamica = f"{elem1} e {elem2} são elementos compatíveis que se complementam naturalmente, criando equilíbrio e crescimento mútuo."
        harmonia = "Diferenças complementares que enriquecem a relação"
        desafios = "Ritmos distintos requerem ajustes e paciência"
        
    else:
        dinamica = f"A combinação entre {elem1} e {elem2} traz desafios interessantes, mas também grandes oportunidades de crescimento e aprendizado."
        harmonia = "Perspectivas diferentes ampliam horizontes"
        desafios = "Temperamentos contrastantes exigem esforço e compreensão"
    
    return f"""**Dinâmica {tipo_relacao}**

{dinamica}

**Pontos de Harmonia:**
- {harmonia}
- Potencial para equilíbrio através do respeito mútuo
- Oportunidade de evoluir juntos

**Possíveis Desafios:**
- {desafios}
- Necessidade de comunicação clara e aberta
- Respeito às diferenças individuais

**Dicas para Fortalecer a Conexão:**
- Pratique escuta ativa e empatia
- Celebrem as diferenças como fonte de aprendizado
- Estabeleçam momentos de qualidade juntos
- Mantenham diálogo aberto sobre expectativas"""


def interpretar_mapa_basico(posicoes_planetas):
    """
    Interpretação básica do mapa astral
    """
    sol = posicoes_planetas.get('Sol', {}).get('signo', 'desconhecido')
    lua = posicoes_planetas.get('Lua', {}).get('signo', 'desconhecido')
    mercurio = posicoes_planetas.get('Mercúrio', {}).get('signo', 'desconhecido')
    
    return f"""**Sol em {sol}**: Representa sua essência, identidade central e forma de expressar vitalidade no mundo. É sua luz que brilha naturalmente.

**Lua em {lua}**: Revela seu mundo emocional, necessidades afetivas e como você processa sentimentos. É seu porto seguro interior.

**Mercúrio em {mercurio}**: Mostra seu estilo de comunicação, forma de pensar e processar informações. É como sua mente opera."""
