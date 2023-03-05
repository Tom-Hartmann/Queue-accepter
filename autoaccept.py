from tkinter import *
import os
import time
import pyautogui
import json
pyautogui.FAILSAFE = FALSE

jsonpener = open('config.json', 'r').read()
obj = json.loads(jsonpener)

# Main function


def img():
    if toggle_button.config('text')[-1] == 'ON':
        print("Searching for a game")
        imglocation = pyautogui.locateCenterOnScreen(
            'accept.png', confidence=0.7)
        if imglocation != None:
            toggle_button.config(text='OFF')
            CurrenPostion = pyautogui.position()
            # pyautogui.moveTo(imglocation,duration=0)
            pyautogui.click(imglocation)
            pyautogui.moveTo(CurrenPostion, duration=0)
            print("gl")
            # sleeping to not stay on while in champ select/ingame | tempfix
            time.sleep(10)
            print("Slept 10 seconds")
    dodgelocation = pyautogui.locateCenterOnScreen(
        'notaccept.png', confidence=0.7)
    if dodgelocation != None:
        toggle_button.config(text='ON')
        print("Someone didn't accept!")
    root.after(2000, img)
    balancelocation = pyautogui.locateCenterOnScreen(
        'balance.png', confidence=0.7)
    if toggle_button.config('text')[-1] == 'OFF' and balancelocation != None:
        if automode_button.config('text')[-1] == 'Automode ON':
            toggle_button.config(text='ON')
            ban_button.config(text='BAN ON')
            lockin_button.config(text='Lock ON')
            print('ON')
    banphase = pyautogui.locateCenterOnScreen('ban.png', confidence=0.9)
    cancerchampbannen = pyautogui.locateCenterOnScreen(
        'ban2.png', confidence=0.7)
    searchbar = pyautogui.locateCenterOnScreen('search.png', confidence=0.9)
    frame = pyautogui.locateCenterOnScreen('frame.png', confidence=0.7)
    confirmban = pyautogui.locateCenterOnScreen(
        'confirmban.png', confidence=0.7)  # Der bann muss durch!
    if toggle_button.config('text')[-1] == 'OFF' and banphase != None:
        if ban_button.config('text')[-1] == 'BAN ON':
            print('BAN PHASE!')
            pyautogui.click(searchbar)
            # pyautogui.hotkey('ctrl','a')
            # pyautogui.hotkey('return')
            pyautogui.write(obj['banchamp'])
            time.sleep(0.5)
            print('Trying to click the frame')
            print(frame)
            xlst = list(frame)
            del xlst[1]
            lst = list(frame)
            del lst[0]
            print(xlst, lst)
            # Thanks to gianpi#1307 für helping me with this part.
            ycords = int(''.join(str(i) for i in lst))
            ycords += 60
            pyautogui.moveTo(frame)
            x, y = pyautogui.position()
            x, y = pyautogui.position()
            pyautogui.click(y=ycords, x=x)
            pyautogui.click(cancerchampbannen, duration=0)
            time.sleep(2)
            print('Checking for ban confirmation.')
            pyautogui.click(confirmban, duration=0)
            ban_button.config(text='BAN OFF')
    lockinimg = pyautogui.locateCenterOnScreen('lockin.png', confidence=0.7)
    if toggle_button.config('text')[-1] == 'OFF' and lockin_button != None:
        if lockin_button.config('text')[-1] == 'Lock ON':
            if lockinimg != None:
                pyautogui.click(lockinimg, duration=0)
                lockin_button.config(text='Lock OFF')

# Get Language


def Lang():
    path = os.getcwd()
    os.chdir(os.path.join(path, "Languages"))
    path = os.getcwd()

    text = obj['Language']
    os.chdir(os.path.join(path, text))

# Button on/off


def Simpletoggle():
    if toggle_button.config('text')[-1] == 'ON':
        toggle_button.config(text='OFF')
        print("OFF")
    else:
        toggle_button.config(text='ON')
        print("ON")

# Button Automode on/off


def Autotoggle():
    if automode_button.config('text')[-1] == 'Automode ON':
        automode_button.config(text='Automode OFF')
        print('Automode OFF')
    else:
        automode_button.config(text='Automode ON')
        print('Automode ON')

# Button Lock in on/off


def Lockin():
    if lockin_button.config('text')[-1] == 'Lock ON':
        lockin_button.config(text='Lock OFF')
        print('Lock OFF')
    else:
        lockin_button.config(text='Lock ON')
        print('Lock ON')

# Button Ban on/off


def BanChamp():
    if ban_button.config('text')[-1] == 'BAN ON':
        ban_button.config(text='BAN OFF')
        print('BAN OFF')
    else:
        ban_button.config(text='BAN ON')
        print('BAN ON')


# Window
root = Tk()
root.title("Queue Accepter")
root.iconbitmap("icon.ico")
root['background'] = 'black'
Hauteur = 0
Largeur = 250
(H, L, c) = (Hauteur, Largeur, "white")
Dessin = Canvas(root, height=H, width=L, bg=c)
Dessin.pack()

# Button
toggle_button = Button(text='OFF', bg='black', fg='white',
                       width=12, command=Simpletoggle)
do = toggle_button['text']
toggle_button.pack(pady=5)

# Automode
automode_button = Button(text='Automode off', bg='black',
                         fg='white', width=12, command=Autotoggle)
do = automode_button['text']
automode_button.pack(pady=5)

# Lock in
lockin_button = Button(text='Lock OFF', bg='black',
                       fg='white', width=12, command=Lockin)
do = lockin_button['text']
lockin_button.pack(pady=5)

# BanChamp
ban_button = Button(text='BAN OFF', bg='black',
                    fg='white', width=12, command=BanChamp)
do = ban_button['text']
ban_button.pack(pady=5)

Lang()
# Loop
root.after(2000, img)
root.mainloop()
