"""
Módulo de cálculos astrológicos usando Swiss Ephemeris
"""
import swisseph as swe
from datetime import datetime

def calcular_mapa(data_nasc, hora_nasc, latitude, longitude):
    """
    Calcula as posições planetárias para um mapa astral natal
    
    Args:
        data_nasc (datetime.date): Data de nascimento
        hora_nasc (datetime.time): Hora de nascimento
        latitude (float): Latitude do local de nascimento
        longitude (float): Longitude do local de nascimento
    
    Returns:
        dict: Dicionário com posições planetárias
    """
    # Converter data e hora para Julian Day
    ano = data_nasc.year
    mes = data_nasc.month
    dia = data_nasc.day
    hora_decimal = hora_nasc.hour + hora_nasc.minute / 60.0 + hora_nasc.second / 3600.0
    
    # Calcular Julian Day
    jd = swe.julday(ano, mes, dia, hora_decimal)
    
    # Definir planetas para calcular
    planetas = {
        'Sol': swe.SUN,
        'Lua': swe.MOON,
        'Mercúrio': swe.MERCURY,
        'Vênus': swe.VENUS,
        'Marte': swe.MARS,
        'Júpiter': swe.JUPITER,
        'Saturno': swe.SATURN
    }
    
    # Nomes dos signos
    signos = [
        'Áries', 'Touro', 'Gêmeos', 'Câncer', 
        'Leão', 'Virgem', 'Libra', 'Escorpião',
        'Sagitário', 'Capricórnio', 'Aquário', 'Peixes'
    ]
    
    # Calcular posições
    posicoes = {}
    
    for nome_planeta, id_planeta in planetas.items():
        try:
            # Calcular posição (retorna tupla com longitude, latitude, distância, etc)
            resultado = swe.calc_ut(jd, id_planeta)
            longitude_ecliptica = resultado[0][0]  # Longitude eclíptica em graus
            
            # Determinar signo (cada signo tem 30 graus)
            signo_idx = int(longitude_ecliptica / 30)
            grau_no_signo = longitude_ecliptica % 30
            
            posicoes[nome_planeta] = {
                'signo': signos[signo_idx],
                'grau': round(grau_no_signo, 2),
                'longitude': round(longitude_ecliptica, 2)
            }
        
        except Exception as e:
            posicoes[nome_planeta] = {
                'signo': 'Erro',
                'grau': 0.0,
                'longitude': 0.0,
                'erro': str(e)
            }
    
    return posicoes


def calcular_ascendente(data_nasc, hora_nasc, latitude, longitude):
    """
    Calcula o Ascendente (versão futura para Premium)
    
    Args:
        data_nasc (datetime.date): Data de nascimento
        hora_nasc (datetime.time): Hora de nascimento
        latitude (float): Latitude
        longitude (float): Longitude
    
    Returns:
        dict: Signo e grau do Ascendente
    """
    # Placeholder para funcionalidade Premium
    # Implementar usando swe.houses()
    pass
