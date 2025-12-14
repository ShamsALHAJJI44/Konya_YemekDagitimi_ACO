import numpy as np
import requests

def mesafe_matrisi_olustur(koordinatlar, yontem="ors", api_key=None):
    if yontem != "ors":
        raise ValueError("Şu anda sadece ORS yöntemi destekleniyor")

    if api_key is None:
        raise ValueError("ORS API anahtarı gerekli")

    n = len(koordinatlar)
    mesafe = np.zeros((n, n))

    url = "https://api.openrouteservice.org/v2/matrix/driving-car"

    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json"
    }

    # ORS expects [lon, lat]
    locations = [[lon, lat] for lat, lon in koordinatlar]

    body = {
        "locations": locations,
        "metrics": ["distance"],
        "units": "km"
    }

    response = requests.post(url, json=body, headers=headers)

    if response.status_code != 200:
        raise RuntimeError(f"ORS Hatası: {response.text}")

    distances = response.json()["distances"]

    for i in range(n):
        for j in range(n):
            if i == j:
                mesafe[i][j] = np.inf
            else:
                mesafe[i][j] = distances[i][j]

    return mesafe

def hesapla_cekicilik(mesafe):
    cekicilik = np.zeros_like(mesafe, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        cekicilik = 1.0 / mesafe
        cekicilik[np.isinf(mesafe)] = 0.0
        cekicilik[np.isnan(cekicilik)] = 0.0
    return cekicilik
