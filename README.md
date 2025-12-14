# 🍽️ Konya Yurtlar İçin Yemek Dağıtımı  
## Ant Colony Optimization (ACO) ile En Kısa Rota Bulma

Bu projede Konya ilinde bulunan **öğrenci yurtlarına yemek dağıtımı** yapan
bir aracın, tüm yurtları ziyaret edecek şekilde **en kısa toplam mesafeyi**
katetmesi amaçlanmıştır.

Problem, Gezgin Satıcı Problemi (TSP) kapsamında ele alınmış ve
**Ant Colony Optimization (ACO)** algoritması kullanılarak çözülmüştür.

---

## 📌 Proje Kapsamı

- Dağıtım noktaları: Konya ilindeki **20 öğrenci yurdu**
- Kullanılan veriler: Gerçek coğrafi koordinatlar
- Amaç: En kısa yemek dağıtım rotasının belirlenmesi
- Çözüm yöntemi: Ant Colony Optimization (ACO)

---

## 🌍 Mesafe Hesabı ve API Kullanımı

Noktalar arasındaki mesafeler, **OpenRouteService Matrix API** kullanılarak
hesaplanmıştır.

- API, iki nokta arasındaki **gerçek sürüş mesafesini (driving distance)**
  metre cinsinden döndürmektedir.
- Elde edilen mesafe matrisi ACO algoritmasına girdi olarak verilmiştir.
- Nihai sonuçlar kullanıcıya **kilometre (km)** cinsinden sunulmuştur.

Google Maps API ücretli olduğu için, benzer işlevselliğe sahip
ücretsiz bir alternatif tercih edilmiştir.

---

## 🐜 Ant Colony Optimization (ACO)

ACO algoritması, karıncaların feromon izlerini takip ederek
en kısa yolu bulma prensibine dayanan sezgisel bir optimizasyon yöntemidir.

Bu projede ACO algoritması aşağıdaki parametreler ile uygulanmıştır:
- Karınca sayısı
- İterasyon sayısı
- Alpha (feromon etkisi)
- Beta (mesafe etkisi)
- Buharlaşma oranı

---

## 🖥️ Streamlit Arayüzü

Proje, **Streamlit** kullanılarak geliştirilen bir grafik arayüz ile
çalıştırılabilmektedir.

Streamlit arayüzü sayesinde:
- Kullanıcı ACO parametrelerini dinamik olarak değiştirebilir
- Algoritma tek bir buton ile çalıştırılabilir
- En kısa rota ve yakınsama grafiği görsel olarak sunulur

---

## ▶️ Projenin Çalıştırılması

### 1️⃣ Gerekli kütüphanelerin kurulması
```bash
pip install -r requirements.txt


###2️⃣ Streamlit uygulamasının başlatılması
streamlit run app.py


📊 Çıktılar

Rota Görselleştirmesi: En kısa dağıtım rotası

Yakınsama Grafiği: İterasyonlara göre çözüm kalitesinin iyileşmesi

Sonuç Dosyası: Toplam mesafe bilgisi (km)

🔐 Güvenlik Notu

API anahtarı güvenlik nedeniyle GitHub reposunda paylaşılmamıştır.
