import subprocess
import sys
import time
import itertools
import os
from colorama import init, Fore, Style

init(autoreset=True)

def print_slow(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def loading_animation(duration=3, symbols="//..//", speed=0.15):
    end_time = time.time() + duration
    for c in itertools.cycle(symbols):
        if time.time() > end_time:
            break
        print(f"\r{c} Yükleniyor...", end="", flush=True)
        time.sleep(speed)
    print("\r" + " " * 20, end="\r")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def sahne(text, color=Fore.WHITE, delay=0.04, bekle=2):
    clear_screen()
    print(color + Style.BRIGHT, end="")
    print_slow(text, delay)
    time.sleep(bekle)
    print(Style.RESET_ALL, end="")

def calistir_ve_kontrol(etiket, dosya):
    print(Fore.CYAN + f"\n▶️ {etiket} çalıştırılıyor..." + Style.RESET_ALL)
    try:
        sonuc = subprocess.run(
            ["python3", dosya],
            capture_output=True,
            text=True,
            timeout=15
        )
        if sonuc.stdout.strip():
            print(sonuc.stdout.strip())
        if sonuc.stderr.strip():
            print(Fore.RED + "⚠️ Hata: " + sonuc.stderr.strip() + Style.RESET_ALL)
            return False
        return True
    except Exception as e:
        print(Fore.RED + "❌ Çalıştırma hatası: " + str(e) + Style.RESET_ALL)
        return False

if __name__ == "__main__":
    clear_screen()
    print(Fore.MAGENTA + Style.BRIGHT + "K O D   S A V A Ş I   B A Ş L I Y O R\n" + Style.RESET_ALL)
    loading_animation(3)

    sahne("🛡️ Savunmacılar zırhlarını kuşanıyor...", Fore.GREEN)
    adim1 = calistir_ve_kontrol("Savunmacı", "savunmaci.py")

    sahne("👹 Saldırganlar exploit yapıyor...", Fore.RED)
    time.sleep(2)

    sahne("⚔️ Savunmacılar güzel savunuyor ama zorlanıyor...", Fore.YELLOW)
    time.sleep(2)

    sahne("🔥 Saldırgan sinsice sabotajını yerleştiriyor...", Fore.RED)
    adim2 = calistir_ve_kontrol("Saldırgan", "saldirgan.py")

    sahne("💥 Arenada son koz: sabotajlı kod sahnede!", Fore.MAGENTA)
    adim3 = calistir_ve_kontrol("Sabotajlı Dosya", "savunmaci_hacklenmis.py")

    clear_screen()
    print(Fore.CYAN + "\n📢 Sonuçlar:\n" + Style.RESET_ALL)
    if not adim3:
        sahne("💀 Saldırgan zafer kazandı! Savunmacı çöktü...", Fore.RED)
    elif adim1 and adim2 and adim3:
        sahne("🛡️ Savunmacı ayakta kaldı! Saldırı başarısız oldu.", Fore.GREEN)
    else:
        sahne("🤷 Durum belirsiz. Kodlar tam olarak çalışmadı.", Fore.YELLOW)
