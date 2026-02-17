"""
Módulo para conversão de cidades em coordenadas (geocoding)
"""
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import streamlit as st

# Cache para evitar múltiplas requisições
@st.cache_data(ttl=86400)  # Cache de 24h
def buscar_coordenadas(cidade, pais="Brasil"):
    """
    Busca latitude e longitude de uma cidade
    
    Args:
        cidade (str): Nome da cidade
        pais (str): País (padrão: Brasil)
    
    Returns:
        tuple: (latitude, longitude, nome_completo) ou (None, None, None) se não encontrar
    """
    try:
        # Criar geolocator (user_agent é obrigatório)
        geolocator = Nominatim(user_agent="astro-vision-app", timeout=10)
        
        # Buscar localização
        location = geolocator.geocode(f"{cidade}, {pais}")
        
        if location:
            return (
                round(location.latitude, 4),
                round(location.longitude, 4),
                location.address
            )
        else:
            return None, None, None
    
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        st.warning(f"⚠️ Erro ao buscar localização: {str(e)}")
        return None, None, None
    except Exception as e:
        st.error(f"Erro inesperado: {str(e)}")
        return None, None, None


def sugerir_cidades_brasil():
    """
    Retorna lista de cidades brasileiras principais com coordenadas
    """
    return {
        "Porto Alegre, RS": (-30.0346, -51.2177),
        "São Paulo, SP": (-23.5505, -46.6333),
        "Rio de Janeiro, RJ": (-22.9068, -43.1729),
        "Brasília, DF": (-15.7939, -47.8828),
        "Salvador, BA": (-12.9714, -38.5014),
        "Fortaleza, CE": (-3.7172, -38.5433),
        "Belo Horizonte, MG": (-19.9167, -43.9345),
        "Manaus, AM": (-3.1190, -60.0217),
        "Curitiba, PR": (-25.4284, -49.2733),
        "Recife, PE": (-8.0476, -34.8770),
        "Goiânia, GO": (-16.6869, -49.2648),
        "Belém, PA": (-1.4558, -48.5039),
        "Guarulhos, SP": (-23.4538, -46.5333),
        "Campinas, SP": (-22.9099, -47.0626),
        "São Luís, MA": (-2.5307, -44.3068),
        "Maceió, AL": (-9.6498, -35.7089),
        "Natal, RN": (-5.7945, -35.2110),
        "Campo Grande, MS": (-20.4428, -54.6464),
        "João Pessoa, PB": (-7.1195, -34.8450),
        "Teresina, PI": (-5.0919, -42.8034),
        "Florianópolis, SC": (-27.5954, -48.5480),
        "Vitória, ES": (-20.3155, -40.3128),
        "Cuiabá, MT": (-15.6014, -56.0979)
    }
