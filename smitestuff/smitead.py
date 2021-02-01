import pyautogui
from pyautogui import *
from time import sleep
import random
import pydirectinput
import subprocess
import win32gui
import win32api
import win32


##variables
sideclick = (1771, 340)
img = 0
img2 = 0
mousex = 0
mousey = 0

# PASSIVE functions
def click(variable):
    pyautogui.moveTo(variable)
    sleep(.03)
    pyautogui.click()
def imgscan(imgname, con, gray):
    global img
    img = pyautogui.locateOnScreen(imgname + '.png', confidence=con, grayscale=gray)
def imgscanclick(imgname, con, gray):
    imgscan(imgname, con, gray)
    click(img)
def dualimgscan(imgname, con, gray, imgname2, con2, gray2):
    global img
    global img2
    img = pyautogui.locateOnScreen(imgname + '.png', confidence=con, grayscale=gray)
    img2 = pyautogui.locateOnScreen(imgname2 + '.png', confidence=con2, grayscale=gray2)
def loopscan(imgname, con, gray):
    while True:
        imgscan(imgname, con, gray)
        if img != None:
            break
def dualloopscanrange(imgname, con, gray,imgname2, con2, gray2):
    for i in range(12):
        sleep(1)
        dualimgscan(imgname, con, gray, imgname2, con2, gray2)
        if img or img2 != None:
            break
def dualloopscan(imgname, con, gray,imgname2, con2, gray2):
    while True:
        dualimgscan(imgname, con, gray, imgname2, con2, gray2)
        if img or img2 != None:
            break
def loopscanclick(imgname, con, gray):
    while True:
        imgscan(imgname, con, gray)
        if img != None:
            click(img)
            break
def relaunch():
    os.system('wmic process where name="Smite.exe" delete')
    sleep(2)
    subprocess.call(r"C:\Program Files (x86)\Steam\Steam.exe -applaunch 386360")
    sleep(70)

def ad():
    dualloopscanrange('earn', .8, False, 'earnglow', .8, False)
    if img != None:
        click(img)
    elif img2 != None:
        click(img2)
    elif img == None and img2 == None:
        relaunch()
        return
    sleep(.1)
    loopscanclick('watch', .8, True)
    sleep(1)
    dualloopscan('collection', .8, False, 'directunlock', .8, False)
    if img2 != None:
        click(sideclick)
        loopscanclick('exit', .8, False)
    elif img != None and img2 == None:
        loopscanclick('exit', .8, False)
    sleep(.1)

while True:
    ad()

