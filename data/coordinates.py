import pandas as pd
import os

# CSV dosyasından yurt koordinatlarını oku
def load_yurt_coordinates(csv_path):
    df = pd.read_csv(csv_path)
    sehir_koordinatlari = {}
    for i, row in df.iterrows():
        sehir_koordinatlari[i] = (row["name"], (row["lat"], row["lng"]))
    return sehir_koordinatlari
