from typing import List, Tuple
import pandas as pd
import re
from collections import Counter

# Precompila el patrón de mención
mention_pattern = re.compile(r'@\w+')

def extract_mentions(text):
    """
    Extrae todas las menciones (palabras que comienzan con @) del texto dado.
    
    Parámetros:
    text (str): El texto de entrada del que se deben extraer las menciones.
    
    Retorna:
    list: Una lista de menciones encontradas en el texto.
    """
    return mention_pattern.findall(text)

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Identifica los 10 usuarios más mencionados en un conjunto de datos de Twitter, optimizando para el uso de memoria.
    
    Parámetros:
    file_path (str): La ruta al archivo JSON que contiene los datos de los tweets.
    
    Retorna:
    list: Una lista de tuplas donde cada tupla contiene un nombre de usuario y la cuenta de menciones.
    """
    # Tamaño de fragmento más pequeño para un menor uso de memoria
    chunk_size = 10000 
    # Contador de frecuencias de mención
    mention_counter = Counter()  

    # Procesar archivo en trozos
    for chunk in pd.read_json(file_path, lines=True, chunksize=chunk_size):
        content = chunk['content'].astype(str)  # Seteando el contenido para que sea de tipo string
        for text in content:
            mentions = extract_mentions(text)  # Extracción de menciones del contenido
            mention_counter.update(mentions)  # Actualización del contador con menciones extraídas

    return mention_counter.most_common(10)  # Devolución de las 10 menciones más comunes con sus recuentos