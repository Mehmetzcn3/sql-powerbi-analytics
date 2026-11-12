import pandas as pd
import json
import random
from datetime import datetime, timedelta

#Müsteriler icin excel dosyası
musteriler = []
isimler = ["mEhMet", "AHMET", "ayşe", "fAtma", "Kaan", "ZEYNEP"]
sehirler = [" izmir", "İSTANBUL ", "ankara", "  Bursa", "antalya"]
tarih_formatlari = ["%d.%m.%Y", "%Y/%m/%d", "%d-%b-%Y"] # Farklı tarih formatları

for i in range(1, 101):
    tarih = datetime.now() - timedelta(days=random.randint(100, 1000))
    formatli_tarih = tarih.strftime(random.choice(tarih_formatlari)) # Tarihler çorba
    
    
    maas_tipi = random.choice([" TL", "$", "₺", ""])
    maas = f"{random.randint(20, 90)}000{maas_tipi}" 
    
    musteriler.append({
        "MusteriID": i,
        "AdSoyad": random.choice(isimler) + " " + random.choice(isimler),
        "Sehir": random.choice(sehirler),
        "KayitTarihi": formatli_tarih, # SQL'de CONVERT / TRY_CAST ile temizlenecek
        "AylikGelir": maas # SQL'de REPLACE ve SUBSTRING ile temizlenecek
    })

df_musteri = pd.DataFrame(musteriler)
df_musteri.to_excel("musteriler_kirli.xlsx", index=False)


# urunler - json
urunler = []
kategoriler = ["Laptop", "Telefon", "Aksesuar"]
markalar = ["Asus", "Apple", "Samsung", "Logitech"]

for i in range(1, 21):
    urunler.append({
        "UrunID": i,
        "UrunAdi": f"Urun_{i}",
        "Ozellikler": { # İç içe (nested) JSON yapısı. SQL'de JSON_VALUE ile parçalanacak.
            "Kategori": random.choice(kategoriler),
            "Marka": random.choice(markalar),
            "Fiyat": random.randint(500, 50000)
        }
    })

with open('urunler_api.json', 'w', encoding='utf-8') as f:
    json.dump(urunler, f, ensure_ascii=False, indent=4)


# 3. csv 
siparisler = []
for i in range(1, 301):
    siparisler.append({
        "SiparisID": 1000 + i,
        "MusteriID": random.randint(1, 100),
        "UrunID": random.randint(1, 20),
        "SiparisTarihi": (datetime.now() - timedelta(days=random.randint(1, 100))).strftime("%Y-%m-%d"),
        "Adet": random.randint(1, 5)
    })

df_siparis = pd.DataFrame(siparisler)
df_siparis.to_csv("siparisler_temiz.csv", index=False)

print("Harika! 'musteriler_kirli.xlsx', 'urunler_api.json' ve 'siparisler_temiz.csv' dosyaları oluşturuldu.")