import subprocess

def calistir_ve_kontrol(etiket, dosya):
    print(f"\n▶️ {etiket} çalıştırılıyor...")
    try:
        sonuc = subprocess.run(
            ["python", dosya],
            capture_output=True,
            text=True,
            timeout=10
        )
        print(sonuc.stdout)
        if sonuc.stderr:
            print("⚠️ Hata:", sonuc.stderr.strip())
            return False
        return True
    except Exception as e:
        print("❌ Çalıştırma hatası:", e)
        return False

if __name__ == "__main__":
    print("🏟️ Kod Arenası Başlatıldı")

    adim1 = calistir_ve_kontrol("1️⃣ Savunmacı", "savunmaci.py")
    adim2 = calistir_ve_kontrol("2️⃣ Saldırgan", "saldirgan.py")
    adim3 = calistir_ve_kontrol("3️⃣ Sabotajlı Dosya", "savunmaci_hacklenmis.py")

    print("\n📢 Sonuç:")
    if not adim3:
        print("💀 Saldırgan kazandı! Kod çöktü.")
    elif adim1 and adim2 and adim3:
        print("🛡️ Savunmacı ayakta! Saldırı başarısız.")
    else:
        print("🤷 Durum belirsiz. Kodlar eksik çalıştı.")
