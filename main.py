#https://krakendev.online | https://youtu.be/AxGPkmmanQI

from pynput.keyboard import Key,Controller      #<--pip install pynput if you didn't installed yet
import time                                     # <--daha önceden indirmediyseniz komut istemine pip install pynput yazıp indirin 
keyboard = Controller()

time.sleep(4)                                   #<--timer before the script start to work | çalıştırdıktan kaç saniye sonra başlayacağı değer
for char in "":                                 #<--add your text here |metni buraya girin
    if char == " ":
        time.sleep(0.2)                         #<--time between spaces
    else:                                       #<--boşluklar arası zaman
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.14)                        #<--time between key presses
                                                #<--basılan tuşlar arası geçen süre

