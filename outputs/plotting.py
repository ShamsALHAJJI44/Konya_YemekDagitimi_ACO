import matplotlib.pyplot as plt

def yol_gorsellestir(yol, koordinatlar, kaydet=False, dosya_yolu=None):
    plt.figure(figsize=(10, 8))
    for i in range(len(yol) - 1):
        sehir1, (lat1, lon1) = koordinatlar[yol[i]]
        sehir2, (lat2, lon2) = koordinatlar[yol[i + 1]]
        plt.plot([lon1, lon2], [lat1, lat2], 'k--', alpha=0.6)
        plt.scatter(lon1, lat1, color='red', s=40)
        plt.text(lon1 + 0.01, lat1 + 0.01, sehir1, fontsize=9, color='blue')
    son_sehir, (son_lat, son_lon) = koordinatlar[yol[-1]]
    plt.scatter(son_lon, son_lat, color='red', s=40)
    plt.text(son_lon + 0.01, son_lat + 0.01, son_sehir, fontsize=9, color='blue')
    plt.title("Konya Yurt Dağıtım Rotası")
    plt.xlabel("Boylam")
    plt.ylabel("Enlem")
    plt.grid(True)

    if kaydet and dosya_yolu:
        plt.savefig(dosya_yolu, dpi=300)
        print(f"✅ Yol grafiği kaydedildi: {dosya_yolu}")
    else:
        plt.show()

def plot_convergence(best_distances, kaydet=False, dosya_yolu=None):
    plt.figure(figsize=(8, 6))
    plt.plot(best_distances, marker='o', color='green')
    plt.title("ACO - En İyi Mesafenin İterasyonlara Göre Değişimi")
    plt.xlabel("İterasyon")
    plt.ylabel("En Kısa Mesafe (km)")
    plt.grid(True)

    if kaydet and dosya_yolu:
        plt.savefig(dosya_yolu, dpi=300)
        print(f"✅ Yakınsama grafiği kaydedildi: {dosya_yolu}")
    else:
        plt.show()