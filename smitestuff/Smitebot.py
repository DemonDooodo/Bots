import pyautogui
from pyautogui import *
from time import sleep
import random
import pydirectinput
import subprocess
class SMITERROR(Exception):
    pass


##variables
godname = 'persephone'
godlist = ['horus', 'fenrir', 'bellona', 'olorun', 'nike', 'mercury', 'persephone', 'heimdallr', 'osiris', 'hades', 'mulan']
godlistchoose = random.choice(godlist)
sideclick = (1771, 340)
playagainclick = (957, 54)
searchclick = (663, 193)
clearclick = (797, 191)
img = 0
img2 = 0
botchoose = ['medium', 'hard']
problem = 'vvgr'
rock = 'ver'
retreat = 'vrr'
nice = 'vvgn'
omw = 'vvve'
defend = 'vsdd'
group = 'vvvg'
vgs = [problem, rock, retreat, nice, omw, defend, group]
b = 0
mousex = 0
mousey = 0
gamemode = "conquest"

# PASSIVE functions
def click(variable):
    pyautogui.moveTo(variable)
    sleep(.04)
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
def smitecheck():
    imgscan('smite', .8, False)
    if img != None:
        return True
    elif img == None:
        return False
def randommouse():
    global mousex
    global mousey
    mousex = random.randint(100,1920)
    mousey = random.randint(100,1080)
    pyautogui.moveTo(mousex, mousey)
def singlekeypress(key, time):
    pyautogui.keyDown(key)
    sleep(time)
    pyautogui.keyUp(key)
def clicktype(name):
    click(clearclick)
    sleep(.01)
    click(searchclick)
    pyautogui.typewrite(name)
def champloop():
    clicktype(godlistchoose)
    sleep(.1)
    dualloopscan(godlistchoose, .9, False, godlistchoose+'2', .9, True)
    if img2 != None:
        champloop()
        return
    elif img != None and img2 == None:
        click(img)

# ACTIVE functions
def champselect():
    clicktype(godname)
    sleep(.1)
    dualloopscan(godname, .9, False, godname+'2', .9, True)
    if img2 != None:
        champloop()
        return
    elif img != None and img2 == None:
        click(img)

def conqselect():
    loopscanclick('play', .8, True)
    loopscanclick('coop', .8, True)
    loopscanclick(gamemode, .8, True)
    loopscanclick('hard', .9, True) #loopscanclick(random.choice(botchoose), .9, True)
    loopscanclick('play2', .8, True)

def antiafk():
    while True:
        if smitecheck() is True:
            for i in range(4):
                sleep(10)
                dualimgscan('smite', .8, False, 'close', .8, False)
                if img2 != None:
                    sleep(.5)
                    click(img2)
                    sleep(1)
                    click(playagainclick)
                    return
                elif img != None and img2 == None:
                    sleep(.5)
                    click(playagainclick)
                    return
            raise SMITERROR
        else:
            pydirectinput.moveTo(randommouse())
            singlekeypress('w', 20)
            sleep(.2)
            singlekeypress('s', 7)
            sleep(.2)
            pyautogui.press(' ')
            sleep(1.2)
            singlekeypress('b', .1)
            sleep(25)
            pyautogui.typewrite(random.choice(vgs), interval=.25)

def acceptfunc():
    while True:
        imgscan('boosters', .9, False)
        if img != None:
            break
        elif img == None:
            imgscan('accept', .9, False)
            if img != None:
                click(img)

def lobby():
    global b
    champselect()
    sleep(.5)
    loopscanclick('lockin', .8, False)
    sleep(.5)
    imgscanclick('boosters', .9, False)
    sleep(.5)
    imgscanclick('battlepoints', .9, False)
    sleep(.5)
    imgscanclick('activate', .8, False)
    sleep(.2)
    click(sideclick)
    while True:
        if smitecheck() is True:
            return
        else:
            imgscan('relic', .8, True)
            if img != None:
                b += 1
                return

def lobbyaccept():
    global b
    while True:
        acceptfunc()
        lobby()
        if b > 0:
            b = 0
            break

def lobbyacceptafk():
    while True:
        lobbyaccept()
        antiafk()

def runbot():
    conqselect()
    lobbyacceptafk()

runbot()