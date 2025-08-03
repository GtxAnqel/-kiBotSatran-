import os
import time
from sistem.sahne_yazici import yaz, sahne
from colorama import init

init(autoreset=True)

def bekle(saniye=2):
    time.sleep(saniye)
    os.system('clear' if os.name == 'posix' else 'cls')

def baslat_giris_animasyonu():
    yaz("\n\n// Kod Arenası'na Hoş Geldiniz //", hiz=0.05)
    bekle(1)
    yaz("~ Hazırlıklar tamamlanıyor...", hiz=0.03)
    bekle(1)
    yaz("~ Takımlar kodlarını yükledi...", hiz=0.03)
    bekle(1)
    yaz("\n⚔️  KOD SAVAŞI BAŞLIYOR ⚔️\n", hiz=0.06)
    bekle(2)
    bekle()
    os.system('clear' if os.name == 'posix' else 'cls')

def yukle_takimlar():
    from takimlar.kodkalkani import Takim as KodKalkani
    from takimlar.zer0byte import Takim as Zer0Byte
    return KodKalkani(), Zer0Byte()

def baslat_savas(takimA, takimB):
    sahne(f"{takimA.isim} açılış saldırısını başlattı...")
    takimA.saldir(takimB)
    bekle()

    sahne(f"{takimB.isim} hızlıca karşılık veriyor!")
    takimB.saldir(takimA)
    bekle()

    sahne(f"{takimA.isim} savunma sistemlerini yükseltiyor...")
    takimA.savun()
    bekle()

    sahne(f"{takimB.isim} exploit paketleriyle yüklendi!")
    takimB.saldir(takimA)
    bekle()

    sahne("⚖️  Sonuçlar hesaplanıyor...")
    puanA = takimA.durum()
    puanB = takimB.durum()

    print("\n🏁 Savaş Sonucu:")
    print(f"{takimA.isim}: {puanA} puan")
    print(f"{takimB.isim}: {puanB} puan")

    if puanA > puanB:
        print(f"🏆 {takimA.isim} kazandı!")
    elif puanB > puanA:
        print(f"🏆 {takimB.isim} kazandı!")
    else:
        print("🤝 Berabere!")

if __name__ == "__main__":
    baslat_giris_animasyonu()
    takimA, takimB = yukle_takimlar()
    baslat_savas(takimA, takimB)
