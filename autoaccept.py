import os
import time
import json
import pyautogui
import threading
from tkinter import *

pyautogui.FAILSAFE = False

with open('config.json', 'r') as json_file:
    obj = json.loads(json_file.read())

# Get Language


def Lang():
    path = os.getcwd()
    os.chdir(os.path.join(path, "Languages"))
    path = os.getcwd()

    text = obj['Language']
    os.chdir(os.path.join(path, text))


def on_close():
    root.destroy()


def locate(image, confidence=0.7):
    location = pyautogui.locateCenterOnScreen(image, confidence=confidence)
    if location is not None:
        return True
    return False


def locate_and_click(image, confidence=0.7):
    location = pyautogui.locateCenterOnScreen(image, confidence=confidence)
    if location is not None:
        pyautogui.click(location)
        return True
    return False


localvaribable = False


def img():
    while True:
        if toggle_button.config('text')[-1] == 'OFF' and locate('balance.png'):
            if automode_button.config('text')[-1] == 'Automode ON':
                toggle_button.config(text='ON')
                if obj['AutoBan'] == "True":
                    ban_button.config(text='BAN ON')
                if obj['AutoBan'] == "True":
                    lockin_button.config(text='Lock ON')
                print('ON')
        if toggle_button.config('text')[-1] == 'ON':
            if locate_and_click('accept.png'):
                toggle_button.config(text='OFF')
                print("Game accepted")
                time.sleep(10)
                print("Slept 10 seconds")
        if locate('notaccept.png'):
            toggle_button.config(text='ON')
            print("Someone didn't accept!")
        if toggle_button.config('text')[-1] == 'OFF':
            if locate('ban.png'):
               localvaribable == True  # and locate('ban.png', confidence=0.9):
               if ban_button.config('text')[-1] == 'BAN ON':
                    if localvaribable == True:
                        print('BAN PHASE!')
                        locate_and_click('search.png', confidence=0.9)
                        pyautogui.write(obj['banchamp'])
                        time.sleep(0.5)
                        frame_location = locate('frame.png')
                        pyautogui.moveTo(frame_location)
                        x, y = pyautogui.position()
                        pyautogui.click(y=y + 60, x=x)
                        locate_and_click('ban2.png')
                        time.sleep(1)
                        locate_and_click('confirmban.png')
                        ban_button.config(text='BAN OFF')
                        localvaribable == False
            if toggle_button.config('text')[-1] == 'OFF' and lockin_button != None:
                if lockin_button.config('text')[-1] == 'Lock ON':
                    if locate_and_click('lockin.png'):
                        lockin_button.config(text='Lock OFF')


time.sleep(1)


def start_thread(target_function):
    thread = threading.Thread(target=target_function)
    thread.daemon = True
    thread.start()


def Simpletoggle():
    if toggle_button.config('text')[-1] == 'ON':
        toggle_button.config(text='OFF')
        print("OFF")
    else:
        toggle_button.config(text='ON')
        print("ON")


def Autotoggle():
    if automode_button.config('text')[-1] == 'Automode ON':
        automode_button.config(text='Automode OFF')
        print('Automode OFF')
    else:
        automode_button.config(text='Automode ON')
        print('Automode ON')


def Lockin():
    if lockin_button.config('text')[-1] == 'Lock ON':
        lockin_button.config(text='Lock OFF')
        print('Lock OFF')
    else:
        lockin_button.config(text='Lock ON')
        print('Lock ON')


def BanChamp():
    if ban_button.config('text')[-1] == 'BAN ON':
        ban_button.config(text='BAN OFF')
        print('BAN OFF')
    else:
        ban_button.config(text='BAN ON')
        print('BAN ON')


def start_move(event):
    global x, y
    x = event.x
    y = event.y


def stop_move(event):
    global x, y
    x = None
    y = None


def on_motion(event):
    global x, y
    deltax = event.x - x
    deltay = event.y - y
    new_position = "+{}+{}".format(root.winfo_x() +
                                   deltax, root.winfo_y() + deltay)
    root.geometry(new_position)


# Create main window
root = Tk()
root.geometry("250x180")
root.configure(bg='black')

# Remove default title bar
root.overrideredirect(1)

# Create custom title bar frame
title_bar = Frame(root, bg='black', relief='raised', bd=2, height=30)
title_bar.pack(fill=X, side=TOP)

# Create title label
title = Label(title_bar, text="Queue Accepter", bg='black', fg='white')
title.pack(side=LEFT, padx=5)

# Create close button
close_button = Button(title_bar, text="X", bg='black',
                      fg='white', relief=FLAT, command=on_close)
close_button.pack(side=RIGHT)

# Bind the functions to the title_bar frame
title_bar.bind("<ButtonPress-1>", start_move)
title_bar.bind("<ButtonRelease-1>", stop_move)
title_bar.bind("<B1-Motion>", on_motion)

# Button
toggle_button = Button(root, text='OFF', bg='black', fg='white',
                       width=12, command=lambda: start_thread(Simpletoggle))
toggle_button.pack(pady=5)

# Automode
automode_button = Button(root, text='Automode off', bg='black',
                         fg='white', width=12, command=lambda: start_thread(Autotoggle))
automode_button.pack(pady=5)

# Lock in
lockin_button = Button(root, text='Lock OFF', bg='black',
                       fg='white', width=12, command=lambda: start_thread(Lockin))
lockin_button.pack(pady=5)

# BanChamp
ban_button = Button(root, text='BAN OFF', bg='black', fg='white',
                    width=12, command=lambda: start_thread(BanChamp))
ban_button.pack(pady=5)

# Getting languages
Lang()

# Starting img thread
start_thread(img)

# Run the main loop
root.mainloop()
