from typing import List, Tuple
import pandas as pd
import emoji
from collections import Counter

def extract_emojis(text):
    """
    Extrae todos los emojis de un texto dado.

    Parámetros:
    text (str): El texto de entrada del cual se deben extraer los emojis.

    Retorna:
    List[str]: Una lista de emojis encontrados en el texto.
    """
    # Extrae todos los emojis de un texto dado
    return [char for char in text if char in emoji.EMOJI_DATA]

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Identifica los 10 emojis más usados y sus respectivos conteos, optimizando para el uso de memoria.

    Parámetros:
    file_path (str): La ruta al archivo JSON que contiene los datos de los tweets.

    Retorna:
    List[Tuple[str, int]]: Una lista de tuplas donde cada tupla contiene un emoji y su conteo.
    """
    # Leer el archivo en trozos
    chunk_size = 10000
    chunks = pd.read_json(file_path, lines=True, chunksize=chunk_size)
    
    # Contador para almacenar la frecuencia de los emojis
    emoji_counter = Counter()
    
    for chunk in chunks:
        # Asegurarse de que la columna "content" es de tipo string
        chunk["content"] = chunk["content"].astype(str)
        for content in chunk["content"]:
            # Extraer emojis del contenido del tweet
            emojis = extract_emojis(content)
            # Actualizar el contador con los emojis extraídos
            emoji_counter.update(emojis)
    
    # Devolver los 10 emojis más comunes con sus conteos
    return emoji_counter.most_common(10)