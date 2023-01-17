import serial
#import time
import pyautogui
import os
#import subprocess
from os import path
a=0
os.system('say "Opening latest News"')
os.system('open -a "feedly"')
pyautogui.moveTo(883,371)
while True:
    ser = serial.Serial("/dev/tty.HC-05-SPPDev")
    ser.flushInput()
    ser_bytes = ser.readline()
    decoded_bytes = int(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
    c=str(decoded_bytes)
    if(c=='500006'):
        continue
    if(c=='501006'):
        pyautogui.scroll(-10)
        os.system('say "Scrolling Up"')
    if(c=='511006'):
        pyautogui.scroll(10)
        os.system('say "Scrolling Down"')
    if(c=='511106'):
        os.system('pkill "feedly"')
        os.system('say "Closing News"')
        break