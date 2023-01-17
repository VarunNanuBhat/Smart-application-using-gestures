import serial
#import time
import pyautogui
import os
#import subprocess
from os import path
a=0
os.system('say "Opening 2048 Game"')
os.system('open -a "2048 Game"' )
while True:
    ser = serial.Serial("/dev/tty.HC-05-SPPDev")
    ser.flushInput()
    ser_bytes = ser.readline()
    decoded_bytes = int(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
    c=str(decoded_bytes)
    if(c=='500006'):
        continue
    if(c=='501006'):
        pyautogui.press('a')
        os.system('say "Left"')
    if(c=='511006'):
        pyautogui.press('d')
        os.system('say "Right"')
    if(c=='510006'):
        pyautogui.press('w')
        os.system('say "Up"')
    if(c=='500106'):
        pyautogui.press('s')
        os.system('say "Down"')
    if(c=='501106'):
        pyautogui.press('r')
        os.system('say "New game"')
    if(c=='511106'):
        #os.system('wmctrl -c "Firefox"')
        os.system('pkill "2048 Game"')
        os.system('say "Closing 2048 Game"')
        break