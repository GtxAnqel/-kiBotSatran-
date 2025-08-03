import ast
import os

SAVUNMACI_DOSYA = "savunmaci.py"
HEDEF_BACKUP = "savunmaci_hacklenmis.py"

class KodSaldirgan:
    def __init__(self, hedef_dosya):
        self.dosya = hedef_dosya
        self.kod = self.kodu_oku()
        self.agac = ast.parse(self.kod)

    def kodu_oku(self):
        with open(self.dosya, "r", encoding="utf-8") as f:
            return f.read()

    def fonksiyonlara_mudahale_et(self):
        yeni_satirlar = []
        satirlar = self.kod.split("\n")

        icinde_mudahale_yapilacak = []
        for node in ast.walk(self.agac):
            if isinstance(node, ast.FunctionDef):
                if "kritik" in node.name.lower() or "sifre" in node.name.lower():
                    icinde_mudahale_yapilacak.append(node.lineno)

        for i, satir in enumerate(satirlar, start=1):
            yeni_satirlar.append(satir)
            if i in icinde_mudahale_yapilacak:
                yeni_satirlar.append("    raise Exception('💥 Bu fonksiyon sabote edildi!')")

        return "\n".join(yeni_satirlar)

    def hackle_ve_kaydet(self):
        yeni_kod = self.fonksiyonlara_mudahale_et()
        with open(HEDEF_BACKUP, "w", encoding="utf-8") as f:
            f.write(yeni_kod)
        print(f"🔧 Saldırı tamamlandı. Yeni dosya: {HEDEF_BACKUP}")

# --- KULLANIM ---
if __name__ == "__main__":
    if not os.path.exists(SAVUNMACI_DOSYA):
        print("❌ Hedef dosya bulunamadı.")
    else:
        saldirgan = KodSaldirgan(SAVUNMACI_DOSYA)
        saldirgan.hackle_ve_kaydet()
