import time
import pyautogui as pa


haha = "aham não por nada chavinho os guri te pega na curva"
haha = haha.split()


pa.click(x=961, y=1058)
pa.click(x=15, y=21)
pa.click(x=374, y=297)
pa.click(x=864, y=990)

for x in haha:
    pa.write(x)
    pa.press('ENTER')