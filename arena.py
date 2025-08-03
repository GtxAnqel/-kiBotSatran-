import time
from sistem.sahne_yazici import sahne, yaz, temizle
from sistem.saldiri_motoru import sabotaj_et
import importlib.util
import sys
import traceback

def dinamik_import(dosya_yolu, modul_adi):
    spec = importlib.util.spec_from_file_location(modul_adi, dosya_yolu)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def intro():
    temizle()
    yaz("//..//", hiz=0.05, renk="\033[90m")
    time.sleep(0.5)
    yaz("KOD SAVAŞI BAŞLIYOR...\n", hiz=0.08, renk="\033[92m")
    time.sleep(1)

def calistir_fonksiyon(modul, fonk_adi):
    try:
        fonk = getattr(modul, fonk_adi)
        fonk()
        return True
    except Exception as e:
        sahne([
            f"💥 Hata! Fonksiyon '{fonk_adi}' çalıştırılamadı.",
            f"Sebep: {str(e)}",
        ], renk="\033[91m", bekle=2)
        return False

def savas():
    takimlar = [
        ("KodKalkanı", "takimlar/kodkalkani.py"),
        ("Zer0Byte", "takimlar/zer0byte.py")
    ]

    importlib.invalidate_caches()

    for round_num in range(1, 4):
        temizle()
        sahne([f"🔥 Raund {round_num} Başlıyor!"], renk="\033[93m", bekle=1)

        # Takım A saldırıyor, Takım B savunuyor
        sabotaj_et(takimlar[1][1], "saldir")
        modA = dinamik_import(takimlar[0][1], "kodkalkani")
        modB = dinamik_import(takimlar[1][1], "zer0byte")

        sahne([f"{takimlar[0][0]} saldırıyor..."], renk="\033[92m", bekle=1)
        if not calistir_fonksiyon(modA, "saldir"):
            sahne([f"🏆 {takimlar[1][0]} kazandı!"], renk="\033[91m", bekle=3)
            return

        sahne([f"{takimlar[1][0]} savunuyor..."], renk="\033[94m", bekle=1)
        if not calistir_fonksiyon(modB, "savun"):
            sahne([f"🏆 {takimlar[0][0]} kazandı!"], renk="\033[92m", bekle=3)
            return

        # Takım B saldırıyor, Takım A savunuyor
        sabotaj_et(takimlar[0][1], "saldir")
        modA = dinamik_import(takimlar[0][1], "kodkalkani")
        modB = dinamik_import(takimlar[1][1], "zer0byte")

        sahne([f"{takimlar[1][0]} saldırıyor..."], renk="\033[92m", bekle=1)
        if not calistir_fonksiyon(modB, "saldir"):
            sahne([f"🏆 {takimlar[0][0]} kazandı!"], renk="\033[91m", bekle=3)
            return

        sahne([f"{takimlar[0][0]} savunuyor..."], renk="\033[94m", bekle=1)
        if not calistir_fonksiyon(modA, "savun"):
            sahne([f"🏆 {takimlar[1][0]} kazandı!"], renk="\033[92m", bekle=3)
            return

    sahne(["🏁 Savaş berabere bitti!"], renk="\033[96m", bekle=3)

if __name__ == "__main__":
    intro()
    savas()
