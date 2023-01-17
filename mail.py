import serial
#import time
import pyautogui
import os
#import subprocess
from os import path
a=0
os.system('say "Opening Mail"')
os.system('open -a "Mail"')
pyautogui.moveTo(131,255)
        #time.sleep(3)
while True:
    ser = serial.Serial("/dev/tty.HC-05-SPPDev")
    ser.flushInput()
    ser_bytes = ser.readline()
    decoded_bytes = int(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
    c=str(decoded_bytes)
    if(c=='500006'):
        continue
    if(c=='510006'):
        pyautogui.moveTo(131,255)
    if(c=='501006'):
        pyautogui.moveTo(845,249)
    if(c=='511006'):
        pyautogui.press('down')
        os.system('say "Moving Down"')
    if(c=='501106'):
        pyautogui.press('up')
        os.system('say "Moving Up"')
    if(c=='500106'):
        pyautogui.scroll(-5)
        os.system('say "Scrolling down"')
    if(c=='510106'):
        pyautogui.scroll(5)
        os.system('say "Scrolling Up"')
    if(c=='511106'):
        os.system('pkill "Mail"')
        os.system('say "Closing Mail Application"')
        break