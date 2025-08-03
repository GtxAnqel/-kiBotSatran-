import time
import os
from colorama import Fore, Style, init

init(autoreset=True)

def temizle():
    os.system("cls" if os.name == "nt" else "clear")

def yaz(metin, hiz=0.01, renk=Fore.WHITE):
    for harf in metin:
        print(renk + harf, end="", flush=True)
        time.sleep(hiz)
    print()

def sahne(metinler, hiz=0.03, renk=Fore.CYAN, bekle=2):
    temizle()
    for satir in metinler:
        yaz(satir, hiz, renk)
    time.sleep(bekle)
