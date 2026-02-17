import swisseph as swe
from datetime import datetime

def calcular_mapa(data_nasc, hora_nasc, lat, lon):
    """Calcula posições planetárias"""
    # Converter data para Julian Day
    ano, mes, dia = data_nasc.year, data_nasc.month, data_nasc.day
    hora_decimal = hora_nasc.hour + hora_nasc.minute/60
    
    jd = swe.julday(ano, mes, dia, hora_decimal)
    
    planetas = {
        'Sol': swe.SUN,
        'Lua': swe.MOON,
        'Mercúrio': swe.MERCURY,
        'Vênus': swe.VENUS,
        'Marte': swe.MARS,
        'Júpiter': swe.JUPITER,
        'Saturno': swe.SATURN
    }
    
    posicoes = {}
    signos = ['Áries', 'Touro', 'Gêmeos', 'Câncer', 'Leão', 'Virgem',
              'Libra', 'Escorpião', 'Sagitário', 'Capricórnio', 'Aquário', 'Peixes']
    
    for nome, id_planeta in planetas.items():
        pos = swe.calc_ut(jd, id_planeta)[0][0]  # Longitude eclíptica
        signo_idx = int(pos / 30)
        grau = pos % 30
        posicoes[nome] = {
            'signo': signos[signo_idx],
            'grau': round(grau, 2),
            'longitude': round(pos, 2)
        }
    
    return posicoes
