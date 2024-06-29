from typing import List, Tuple
import pandas as pd
import re
from collections import Counter

# Precompilado del patrón de mención
mention_pattern = re.compile(r'@\w+')

def extract_mentions(text):
    return mention_pattern.findall(text)

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Tamaño de fragmento más grande para menos iteraciones
    chunk_size = 50000
    # Contador de frecuencias de mención
    mention_counter = Counter()

    # Procesar archivo en trozos
    for chunk in pd.read_json(file_path, lines=True, chunksize=chunk_size):
        content = chunk['content'].astype(str)  # Seteando el contenido para que sea de tipo string
        for text in content:
            mentions = extract_mentions(text)  # Extracción de menciones del contenido
            mention_counter.update(mentions)  # Actualización del contador con menciones extraídas

    return mention_counter.most_common(10)  # Devolución de las 10 menciones más comunes con sus recuentos