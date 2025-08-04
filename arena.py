import time
import random
from sistem.sabotaj import sabotaj_et
from sistem.onar import onar
from sistem.sahne_yazici import sahne_yaz

# Takımlar
takimlar = {
    "zer0byte": {
        "dosya": "takimlar/zer0byte.py",
        "yedek": "yedekler/zer0byte_backup.py",
        "kritik": ["saldir", "savun"]
    },
    "kodkalkani": {
        "dosya": "takimlar/kodkalkani.py",
        "yedek": "yedekler/kodkalkani_backup.py",
        "kritik": ["saldir", "savun"]
    }
}

sahne_yaz("🎮 KOD SAVAŞI BAŞLIYOR...\n", hiz=0.07)
time.sleep(1)
print()

tur_sayisi = 5

for tur in range(1, tur_sayisi + 1):
    sahne_yaz(f"\n🌀 {tur}. TUR BAŞLIYOR...\n", hiz=0.06)
    time.sleep(1)

    # Saldıran ve savunan rastgele seçiliyor
    saldiran_adi, savunan_adi = random.sample(list(takimlar.keys()), 2)
    saldiran = takimlar[saldiran_adi]
    savunan = takimlar[savunan_adi]

    sahne_yaz(f"💥 {saldiran_adi.upper()} ekibi saldırıyor!", hiz=0.04)
    hedef_fonk = random.choice(savunan["kritik"])
    sahne_yaz(f"🎯 Hedef: {hedef_fonk} fonksiyonu", hiz=0.04)
    time.sleep(1)

    # Saldırı
    sabotaj_basarili = sabotaj_et(savunan["dosya"], hedef_fonk)

    # Savunma
    sahne_yaz(f"🛡️ {savunan_adi.upper()} savunma sistemini devreye sokuyor...", hiz=0.04)
    onarildi = onar(savunan["dosya"], savunan["yedek"], savunan["kritik"])
    time.sleep(1)

    # Sahne geçişi
    print("\n" + "="*40 + "\n")
    time.sleep(2)

sahne_yaz("\n🏁 Kod Savaşı Sona Erdi!", hiz=0.07)
