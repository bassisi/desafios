from typing import List, Tuple
from datetime import datetime
import pandas as pd

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Leer el archivo completo en memoria
    df = pd.read_json(file_path, lines=True)
    
    # Convertir la columna "date" a fecha sin tiempo
    df["date"] = pd.to_datetime(df["date"]).dt.date
    
    # Extraer el valor de la clave "username" en la columna "user"  
    df["username"] = df["user"].apply(lambda x: x["username"] if isinstance(x, dict) else None)
    
    # Contar tweets por fecha y usuario
    tweet_counts = df.groupby(["date", "username"]).size().reset_index(name="count")
    
    # Encontrar las top 10 fechas con más tweets
    top_dates = tweet_counts.groupby("date")["count"].sum().nlargest(10).index
    
    # Encontrar el usuario con más tweets por cada una de las top 10 fechas
    result = []
    for date in top_dates:
        top_username = tweet_counts[tweet_counts["date"] == date].sort_values(by="count", ascending=False).iloc[0]["username"]
        result.append((date, top_username))
    
    return result