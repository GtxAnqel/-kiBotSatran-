import re

def sabotaj_et(dosya_yolu, hedef_fonksiyon):
    with open(dosya_yolu, 'r') as f:
        kod = f.read()

    # Hedef fonksiyonu bulmak için regex
    desen = rf'def {hedef_fonksiyon}\(.*?\):\n(?:\s+.+\n)+'
    yeni_kod, degisiklik_sayisi = re.subn(desen, '', kod)

    if degisiklik_sayisi > 0:
        with open(dosya_yolu, 'w') as f:
            f.write(yeni_kod)
        print(f"💣 Saldırı başarılı: '{hedef_fonksiyon}' fonksiyonu silindi.")
        return True
    else:
        print(f"🛡️ '{hedef_fonksiyon}' fonksiyonu bulunamadı veya zaten silinmiş.")
        return False
