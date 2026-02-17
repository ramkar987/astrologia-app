import google.generativeai as genai
import os

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def gerar_horoscopo(signo, data):
    """Gera horóscopo diário com Gemini"""
    model = genai.GenerativeModel('gemini-2.0-flash-lite')  # Modelo mais barato
    
    prompt = f"""Gere um horóscopo para {signo} em {data.strftime('%d/%m/%Y')}.
    Inclua: amor, trabalho, saúde. Máximo 150 palavras. Tom acolhedor e místico."""
    
    response = model.generate_content(prompt)
    return response.text

def interpretar_mapa(posicoes_planetas):
    """Interpretação básica do mapa com Gemini"""
    model = genai.GenerativeModel('gemini-2.0-flash-lite')
    
    planetas_texto = "\n".join([f"{p}: {d['signo']} {d['grau']}°" 
                                 for p, d in posicoes_planetas.items()])
    
    prompt = f"""Interprete este mapa astral de forma concisa (200 palavras):
    {planetas_texto}
    
    Foque em: personalidade, vocação e desafios principais."""
    
    response = model.generate_content(prompt)
    return response.text
