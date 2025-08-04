import re
import shutil

def fonksiyon_var_mi(kod, fonksiyon_adi):
    desen = rf'def {fonksiyon_adi}\(.*?\):\n(?:\s+.+\n)+'
    return re.search(desen, kod) is not None

def onar(dosya_yolu, yedek_yolu, kritik_fonksiyonlar):
    with open(dosya_yolu, 'r') as f:
        mevcut_kod = f.read()

    eksik_fonksiyonlar = []
    for fonk in kritik_fonksiyonlar:
        if not fonksiyon_var_mi(mevcut_kod, fonk):
            eksik_fonksiyonlar.append(fonk)

    if eksik_fonksiyonlar:
        # Dosyayı yedekten geri yükle
        shutil.copy(yedek_yolu, dosya_yolu)
        print(f"🛠️ Onarım yapıldı. Eksik fonksiyonlar: {', '.join(eksik_fonksiyonlar)}")
        return True
    else:
        print("✅ Tüm kritik fonksiyonlar yerinde. Onarım gerekmedi.")
        return False
