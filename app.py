import streamlit as st
import os

from data.coordinates import load_yurt_coordinates
from core.matrix_utils import mesafe_matrisi_olustur
from core.ant_algorithm import run_aco
from outputs.plotting import yol_gorsellestir, plot_convergence
from config import ACO_CONFIG, ORS_API_KEY

# ===============================
# Sayfa Ayarları
# ===============================
st.set_page_config(
    page_title="Konya Yemek Dağıtımı - ACO",
    layout="centered"
)

st.title("🍽️ Konya Yurtlar İçin Yemek Dağıtımı")
st.subheader("Ant Colony Optimization (ACO)")

# ===============================
# Parametreler (Sidebar)
# ===============================
st.sidebar.header("⚙️ ACO Parametreleri")

karinca_sayisi = st.sidebar.slider(
    "Karınca Sayısı",
    5, 50, ACO_CONFIG["karinca_sayisi"]
)

iterasyon_sayisi = st.sidebar.slider(
    "İterasyon Sayısı",
    10, 100, ACO_CONFIG["iterasyon_sayisi"]
)

alpha = st.sidebar.slider(
    "Alpha (Feromon Etkisi)",
    0.1, 5.0, float(ACO_CONFIG["alpha"])
)

beta = st.sidebar.slider(
    "Beta (Mesafe Etkisi)",
    0.1, 5.0, float(ACO_CONFIG["beta"])
)

# ===============================
# Çalıştır Butonu
# ===============================
if st.button("🚀 Algoritmayı Çalıştır"):
    st.info("Algoritma çalışıyor, lütfen bekleyin...")

    # Veri yükle
    data_path = os.path.join("data", "konya_yurtlar.csv")
    sehir_koordinatlari = load_yurt_coordinates(data_path)
    koordinatlar = [v[1] for v in sehir_koordinatlari.values()]

    # Mesafe matrisi
    mesafe = mesafe_matrisi_olustur(
    koordinatlar,
    yontem="ors",
    api_key=ORS_API_KEY
)


    # ACO çalıştır
    en_iyi_yol, en_iyi_mesafe, iterasyon_iyileri = run_aco(
        mesafe,
        karinca_sayisi=karinca_sayisi,
        iterasyon_sayisi=iterasyon_sayisi,
        alpha=alpha,
        beta=beta,
        buharlasma_orani=ACO_CONFIG["buharlasma_orani"],
        feromon_katkisi=ACO_CONFIG["feromon_katkisi"]
    )

    # km'ye çevir
    en_iyi_mesafe_km = en_iyi_mesafe / 1000

    st.success(f"✅ En kısa toplam mesafe: {en_iyi_mesafe_km:.2f} km")

    # Output klasörü
    os.makedirs("outputs", exist_ok=True)

    rota_path = "outputs/rota.png"
    yakin_path = "outputs/yakinsama.png"

    yol_gorsellestir(
        en_iyi_yol,
        sehir_koordinatlari,
        kaydet=True,
        dosya_yolu=rota_path
    )

    plot_convergence(
        iterasyon_iyileri,
        kaydet=True,
        dosya_yolu=yakin_path
    )

    # Görseller
    st.image(rota_path, caption="📍 En Kısa Rota")
    st.image(yakin_path, caption="📉 Yakınsama Grafiği")
