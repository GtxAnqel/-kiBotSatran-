import ast
import shutil
import os

class KodSavunucu:
    def __init__(self, dosya_adi):
        self.dosya = dosya_adi
        self.kod = self.kodu_oku()
        self.fonksiyonlar = self.fonksiyonlari_bul()

    def kodu_oku(self):
        with open(self.dosya, "r", encoding="utf-8") as f:
            return f.read()

    def fonksiyonlari_bul(self):
        agac = ast.parse(self.kod)
        return [node.name for node in ast.walk(agac) if isinstance(node, ast.FunctionDef)]

    def kritik_fonksiyonlari_goster(self):
        print("💡 Kritik Fonksiyonlar:")
        for f in self.fonksiyonlar:
            if "kritik" in f.lower() or "sifre" in f.lower() or "veri" in f.lower():
                print(f"🔴 {f} (Yüksek Risk)")
            else:
                print(f"🟢 {f}")

    def yedekle(self):
        hedef = self.dosya.replace(".py", "_backup.py")
        shutil.copy(self.dosya, hedef)
        print(f"📁 Dosya yedeklendi: {hedef}")

# --- KULLANIM ---
if __name__ == "__main__":
    dosya = __file__
    koruyucu = KodSavunucu(dosya)
    koruyucu.kritik_fonksiyonlari_goster()
    koruyucu.yedekle()
