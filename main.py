
import os
from data.coordinates import load_yurt_coordinates
from core.matrix_utils import mesafe_matrisi_olustur
from core.ant_algorithm import run_aco
from config import ACO_CONFIG
from outputs.plotting import yol_gorsellestir, plot_convergence
import numpy as np

# Veriyi yükle
data_path = os.path.join("/content/drive/MyDrive/Colab_Notebooks/Konya_YemekDagitimi_ACO/data", "konya_yurtlar.csv")
sehir_koordinatlari = load_yurt_coordinates(data_path)

# Sadece koordinatları listeye dönüştür
koordinatlar = [v[1] for v in sehir_koordinatlari.values()]

# Mesafe matrisini oluştur
mesafe = mesafe_matrisi_olustur(koordinatlar)

# ACO algoritmasını çalıştır
en_iyi_yol, en_iyi_mesafe, iterasyon_iyileri = run_aco(
    mesafe,
    karinca_sayisi=ACO_CONFIG["karinca_sayisi"],
    iterasyon_sayisi=ACO_CONFIG["iterasyon_sayisi"],
    alpha=ACO_CONFIG["alpha"],
    beta=ACO_CONFIG["beta"],
    buharlasma_orani=ACO_CONFIG["buharlasma_orani"],
    feromon_katkisi=ACO_CONFIG["feromon_katkisi"]
)

# Sonuçları yazdır
print("\n🚚 En iyi rota:")
for i in en_iyi_yol:
    print(f"  ➤ {sehir_koordinatlari[i][0]}")
print(f"\n📏 Toplam mesafe: {en_iyi_mesafe:.2f} km")

# Sonuç dosyasına kaydet
output_dir = "/content/drive/MyDrive/Colab_Notebooks/Konya_YemekDagitimi_ACO/outputs"
os.makedirs(output_dir, exist_ok=True)

# .txt dosyasına kaydet
with open(os.path.join(output_dir, "sonuc.txt"), "w") as out:
    out.write(f"En iyi yol: {en_iyi_yol}\nToplam mesafe: {en_iyi_mesafe:.2f} km\n")

# Görselleri kaydet
rota_dosya = os.path.join(output_dir, "rota.png")
yakinsama_dosya = os.path.join(output_dir, "yakinsama.png")

yol_gorsellestir(en_iyi_yol, sehir_koordinatlari, kaydet=True, dosya_yolu=rota_dosya)
plot_convergence(iterasyon_iyileri, kaydet=True, dosya_yolu=yakinsama_dosya)

print("\n✅ Çıktılar kaydedildi:")
print(f"📁 Rota grafiği: {rota_dosya}")
print(f"📉 Yakınsama grafiği: {yakinsama_dosya}")
print(f"🧾 Sonuç dosyası: {os.path.join(output_dir, 'sonuc.txt')}")
