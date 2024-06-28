from typing import List, Tuple
from datetime import datetime
import pandas as pd

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Leer el archivo en trozos
    chunk_size = 10000
    chunks = pd.read_json(file_path, lines=True, chunksize=chunk_size)
    
    # Diccionario para contar tweets por fecha y usuario
    tweet_counts = {}
    
    for chunk in chunks:
        # Convertir la columna "date" a fecha sin tiempo
        chunk["date"] = pd.to_datetime(chunk["date"]).dt.date
        
        # Extraer el valor de la clave "username" en la columna "user"        
        chunk["username"] = chunk["user"].apply(lambda x: x["username"] if isinstance(x, dict) else None)
        
        # Contar tweets por fecha y usuario en el chunk actual
        for date, group in chunk.groupby("date"):
            if date not in tweet_counts:
                tweet_counts[date] = {}
            for username, count in group["username"].value_counts().items():
                if username not in tweet_counts[date]:
                    tweet_counts[date][username] = 0
                tweet_counts[date][username] += count

    # Encontrar las top 10 fechas con más tweets
    top_dates = sorted(tweet_counts.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]
    
    # Encontrar el usuario con más tweets por cada una de las top 10 fechas
    result = []
    for date, username_counts in top_dates:
        top_username = max(username_counts.items(), key=lambda x: x[1])[0]
        result.append((date, top_username))
    
    return result