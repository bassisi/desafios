from typing import List, Tuple
import pandas as pd
import emoji
from collections import Counter

def extract_emojis(text):
    # Extrae todos los emojis de un texto dado
    return [char for char in text if char in emoji.EMOJI_DATA]

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Leer el archivo JSON completo en memoria
    df = pd.read_json(file_path, lines=True)  
    # Asegurarse de que la columna 'content' es de tipo string
    df['content'] = df['content'].astype(str)  
    
    # Extraer emojis de todos los tweets y combinarlos en una lista
    all_emojis = df['content'].apply(extract_emojis).sum()  
    
    # Contador para almacenar la frecuencia de los emojis
    emoji_counter = Counter(all_emojis)  
    
    # Devolver los 10 emojis más comunes con sus conteos
    return emoji_counter.most_common(10)  
