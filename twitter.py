import serial
#import time
import pyautogui
import os
#import subprocess
from os import path
a=0
os.system('say "Opening Twitter"')
os.system('open -a "Twitter"')
pyautogui.moveTo(523,201)
pyautogui.hotkey('command','1')
while True:
    ser = serial.Serial("/dev/tty.HC-05-SPPDev")
    ser.flushInput()
    ser_bytes = ser.readline()
    decoded_bytes = int(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
    c=str(decoded_bytes)
    if(c=='500006'):
        continue
    if(c=='501006'):
        pyautogui.press('down')
        os.system('say "Next post"')
    if(c=='500106'):
        pyautogui.hotkey('command','l')
        os.system('say "Liked"')
    if(c=='511006'):
        pyautogui.press('up')
        os.system('say "Previous post"')
    if(c=='511106'):
        os.system('pkill "Twitter"')
        os.system('say "Closing Twitter"')
        break