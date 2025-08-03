import os

def sabotaj_et(dosya_yolu, fonksiyon_adi="saldir"):
    """
    Verilen Python dosyasında belirtilen fonksiyonun içine
    sabotaj kodu enjekte eder.
    """

    if not os.path.exists(dosya_yolu):
        print(f"Dosya bulunamadı: {dosya_yolu}")
        return False

    with open(dosya_yolu, "r", encoding="utf-8") as f:
        satirlar = f.readlines()

    yeni_satirlar = []
    sabotaj_kod = [
        "    raise Exception('💥 Bu fonksiyon sabote edildi!')\n"
    ]

    fonksiyon_bulundu = False
    indent_boyutu = None

    for i, satir in enumerate(satirlar):
        yeni_satirlar.append(satir)
        if satir.strip().startswith(f"def {fonksiyon_adi}"):
            fonksiyon_bulundu = True
            # Girintiyi ölç
            indent_boyutu = len(satir) - len(satir.lstrip())
            # Sabotaj kodunu ekle
            for sabotaj_satir in sabotaj_kod:
                yeni_satirlar.append(" " * (indent_boyutu + 4) + sabotaj_satir.strip() + "\n")
            # Sonraki satırları atlamak için döngü kırılabilir ama biz devam ediyoruz

    if not fonksiyon_bulundu:
        print(f"Fonksiyon bulunamadı: {fonksiyon_adi}()")
        return False

    # Dosyayı yaz
    with open(dosya_yolu, "w", encoding="utf-8") as f:
        f.writelines(yeni_satirlar)

    print(f"⚠️ Sabotaj yapıldı: {dosya_yolu} içindeki {fonksiyon_adi} fonksiyonu")
    return True
