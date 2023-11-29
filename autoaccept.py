import os
import json5
import time
import pyautogui
import threading
import asyncio
import logging
from tkinter import *
from pyscreeze import ImageNotFoundException

ImageNotFoundException(True)

logging.basicConfig(level=logging.DEBUG)

# pyautogui.FAILSAFE = False

with open("config.json5", "r") as json_file:
    obj = json5.load(json_file)

# Get Language
def Lang():
    path = os.getcwd()
    os.chdir(os.path.join(path, "Languages"))
    path = os.getcwd()

    text = obj["Language"]
    os.chdir(os.path.join(path, text))

def on_close():
    root.destroy()

def locateImage(image, confidence=0.7, click=False):
    try: 
        location = pyautogui.locateCenterOnScreen(image, confidence=confidence)
        if location:
            if click:
                pyautogui.click(location)
            return True
        return False
    except Exception as e:
        print(f"An error occured: {e}")
        return False
    
async def main_function():
    while True:
        await asyncio.sleep(0.1)
        if (
            toggle_button.config("text")[-1] == "OFF"
            and (locateImage("social.png")  or locateImage("balance.png") or locateImage("navigation_bar.png") or locateImage("balance1.png"))
            and automode_button.config("text")[-1] == "Automode ON"
        ):
            toggle_button.config(text="ON")
            if obj["AutoBan"] == "True":
                ban_button.config(text="BAN ON")
                logging.debug("AutoBan ON")
            if obj["AutoLock"] == "True":
                lockin_button.config(text="Lock ON")
                logging.debug("AutoLock ON")
        if locateImage("banphase.png", confidence=0.5):
            toggle_button.config("text")[-1] == "OFF"
        if locateImage("frame.png"):
            toggle_button.config("text")[-1] == "OFF"
        if toggle_button.config("text")[-1] == "ON" and locateImage(
            "accept.png", confidence=0.9
        ):
            current_position = pyautogui.position()
            locateImage("accept.png",click=True)
            pyautogui.moveTo(current_position, duration=0)
            toggle_button.config(text="OFF")
            logging.debug("Game accepted")
            time.sleep(10)
        if locateImage("ban.png", confidence=0.5) and toggle_button.config("text")[-1] == "ON":
            toggle_button.config(text="OFF")
        if locateImage("notaccept.png") and automode_button.config("text")[-1] == "Automode ON":
            toggle_button.config(text="ON")
            logging.debug("Someone didn't accept!")
        if (
            locateImage("ban.png", confidence=0.9)
            and toggle_button.config("text")[-1] == "OFF"
            and ban_button.config("text")[-1] == "BAN ON"
        ):
            logging.debug("Setting local variable to True")
            logging.debug("BAN PHASE!")
            frame_location = pyautogui.locateImageCenterOnScreen("frame.png", confidence=0.5)
            locateImage("search.png", confidence=0.7,click=True)
            pyautogui.hotkey("ctrl", "a")
            pyautogui.hotkey("delete")
            pyautogui.write(obj["banchamp"])
            time.sleep(0.5)
            xvar, yvar = frame_location[0], frame_location[1] + 60
            print(xvar,yvar)
            pyautogui.click(x=xvar,y=yvar)
            locateImage("ban2.png",click=True)
            pyautogui.click()
            time.sleep(1)
            ban_button.config(text="BAN OFF")
            logging.debug("Now setting localvariable_to_true")
            if locateImage("confirmban.png", 0.8):
                logging.debug("Found Confirm Ban")
                locateImage("confirmban.png", 0.7,click=True)
                logging.debug("Clicked confirm ban")
        if locateImage("confirmban.png", 0.8):
            logging.debug("Found Confirm Ban")
            locateImage("confirmban.png", 0.7,click=True)
            logging.debug("Clicked confirm ban")
        if (
            toggle_button.config("text")[-1] == "OFF"
            and lockin_button.config("text")[-1] == "Lock ON"
        ):
            if locateImage("lockin.png",click=True):
                lockin_button.config(text="Lock OFF")
        if locateImage("confirmban.png", 0.8):
            locateImage("confirmban.png", 0.7,click=True)
            logging.debug("Found Confirm Ban")
        if auto_decline.config("text")[-1] == "DECLINE ON":
#            if locateImage("declineswap.png"):    
                if locateImage("declineswap.png",click=True):
                    logging.debug("Declinded swap!")
time.sleep(0.1)
def start_thread(target_function):
    thread = threading.Thread(target=target_function)
    thread.daemon = True
    thread.start()

def start_asyncio_coroutine(target_function):
    def run_coroutine_in_thread():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(target_function())
        loop.close()

    thread = threading.Thread(target=run_coroutine_in_thread)
    thread.daemon = True
    thread.start()

def Simpletoggle():
    if toggle_button.config("text")[-1] == "ON":
        toggle_button.config(text="OFF")
        logging.debug("OFF")
    else:
        toggle_button.config(text="ON")
        logging.debug("ON")

def Autotoggle():
    if automode_button.config("text")[-1] == "Automode ON":
        automode_button.config(text="Automode OFF")
        logging.debug("Automode OFF")
    else:
        automode_button.config(text="Automode ON")
        logging.debug("Automode ON")

def Lockin():
    if lockin_button.config("text")[-1] == "Lock ON":
        lockin_button.config(text="Lock OFF")
        logging.debug("Lock OFF")
    else:
        lockin_button.config(text="Lock ON")
        logging.debug("Lock ON")

def BanChamp():
    if ban_button.config("text")[-1] == "BAN ON":
        ban_button.config(text="BAN OFF")
        logging.debug("BAN OFF")
    else:
        ban_button.config(text="BAN ON")
        logging.debug("BAN ON")

def AutoDecline():
    if auto_decline.config("text")[-1] == "DECLINE ON":
        auto_decline.config(text="DECLINE OFF")
        logging.debug("DECLINE OFF")
    else:
        auto_decline.config(text="DECLINE ON")
        logging.debug("DECLINE ON")

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
    new_position = "+{}+{}".format(root.winfo_x() + deltax, root.winfo_y() + deltay)
    root.geometry(new_position)

# Create main window
root = Tk()
root.geometry("250x210")
root.configure(bg="black")

# Remove default title bar
root.overrideredirect(1)

# Create custom title bar frame
title_bar = Frame(root, bg="black", relief="raised", bd=2, height=30)
title_bar.pack(fill=X, side=TOP)

# Create title label
title = Label(title_bar, text="Queue Accepter", bg="black", fg="white")
title.pack(side=LEFT, padx=5)

# Create close button
close_button = Button(
    title_bar, text="X", bg="black", fg="white", relief=FLAT, command=on_close
)
close_button.pack(side=RIGHT)

# Bind the functions to the title_bar frame
title_bar.bind("<ButtonPress-1>", start_move)
title_bar.bind("<ButtonRelease-1>", stop_move)
title_bar.bind("<B1-Motion>", on_motion)

# Button
toggle_button = Button(
    root,
    text="OFF",
    bg="black",
    fg="white",
    width=12,
    command=lambda: start_thread(Simpletoggle),
)
toggle_button.pack(pady=5)

# Automode
automode_button = Button(
    root,
    text="Automode off",
    bg="black",
    fg="white",
    width=12,
    command=lambda: start_thread(Autotoggle),
)
automode_button.pack(pady=5)

# Lock in
lockin_button = Button(
    root,
    text="Lock OFF",
    bg="black",
    fg="white",
    width=12,
    command=lambda: start_thread(Lockin),
)
lockin_button.pack(pady=5)

# BanChamp
ban_button = Button(
    root,
    text="BAN OFF",
    bg="black",
    fg="white",
    width=12,
    command=lambda: start_thread(BanChamp),
)
ban_button.pack(pady=5)

#Auto decline for Aram
auto_decline = Button(
    root,
    text="DECLINE OFF",
    bg="black",
    fg="white",
    width=12,
    command=lambda: start_thread(AutoDecline),
)
auto_decline.pack(pady=5)

# Getting languages
Lang()

# Starting img thread
start_asyncio_coroutine(main_function)
# Run the main loop
root.mainloop()