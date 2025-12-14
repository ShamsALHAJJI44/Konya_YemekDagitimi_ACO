import numpy as np
import random
from core.matrix_utils import hesapla_cekicilik

def olasilik_hesapla(mevcut, ziyaret_edilmemisler, feromon, cekicilik, alpha, beta):
    toplam = 0
    olasiliklar = {}
    for j in ziyaret_edilmemisler:
        deger = (feromon[mevcut][j] ** alpha) * (cekicilik[mevcut][j] ** beta)
        olasiliklar[j] = deger
        toplam += deger
    for j in olasiliklar:
        olasiliklar[j] /= toplam if toplam > 0 else 1
    return olasiliklar

def rulet_tekerlegi_secimi(olasilik_dict):
    r = random.random()
    toplam = 0
    for sehir, olasilik in olasilik_dict.items():
        toplam += olasilik
        if r <= toplam:
            return sehir

def karinca_gezi(baslangic, mesafe, feromon, alpha=1, beta=2):
    n = len(mesafe)
    yol = [baslangic]
    toplam_uzunluk = 0
    cekicilik = hesapla_cekicilik(mesafe)
    while len(yol) < n:
        mevcut = yol[-1]
        ziyaret_edilmemisler = list(set(range(n)) - set(yol))
        olasiliklar = olasilik_hesapla(mevcut, ziyaret_edilmemisler, feromon, cekicilik, alpha, beta)
        secilen = rulet_tekerlegi_secimi(olasiliklar)
        yol.append(secilen)
        toplam_uzunluk += mesafe[mevcut][secilen]
    toplam_uzunluk += mesafe[yol[-1]][yol[0]]  # geri dönüş mesafesi
    yol.append(yol[0])  # başlangıç noktasına dön
    return yol, toplam_uzunluk

def feromon_guncelle(feromon, yollar, buharlasma_orani=0.5, Q=1.0):
    yeni_feromon = (1 - buharlasma_orani) * feromon
    for yol, uzunluk in yollar:
        for i in range(len(yol) - 1):
            a, b = yol[i], yol[i + 1]
            katkı = Q / (uzunluk + 1e-6)  # sıfıra bölünme hatasını önlemek için
            yeni_feromon[a][b] += katkı
            yeni_feromon[b][a] += katkı
    return yeni_feromon

def run_aco(mesafe, karinca_sayisi=10, iterasyon_sayisi=50, alpha=1, beta=3,
            buharlasma_orani=0.5, feromon_katkisi=1):
    sehir_sayisi = len(mesafe)
    feromon = np.ones_like(mesafe) * 0.1
    en_iyi_yol = None
    en_kisa_mesafe = float("inf")
    iterasyon_en_iyiler = []
    for it in range(iterasyon_sayisi):
        yollar = []
        for _ in range(karinca_sayisi):
            yol, uzunluk = karinca_gezi(0, mesafe, feromon, alpha, beta)
            yollar.append((yol, uzunluk))
            if uzunluk < en_kisa_mesafe:
                en_kisa_mesafe = uzunluk
                en_iyi_yol = yol
        feromon = feromon_guncelle(feromon, yollar, buharlasma_orani, feromon_katkisi)
        iterasyon_en_iyiler.append(en_kisa_mesafe)
        print(f"🔁 İterasyon {it+1}: En kısa mesafe = {en_kisa_mesafe:.2f} km")
    return en_iyi_yol, en_kisa_mesafe, iterasyon_en_iyiler