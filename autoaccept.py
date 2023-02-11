from tkinter import *
import os
import time
import pyautogui
pyautogui.FAILSAFE = FALSE
#Main function
def img():
    if toggle_button.config('text')[-1] == 'ON' :
        print ("Searching for a game")
        imglocation = pyautogui.locateCenterOnScreen('accept.png', confidence=0.7)
        if imglocation != None:
            toggle_button.config(text='OFF')
            CurrenPostion = pyautogui.position()
            pyautogui.moveTo(imglocation,duration=0)
            pyautogui.click()
            pyautogui.moveTo(CurrenPostion,duration=0)
            print ("gl")
            time.sleep(10)
            print ("Slept 10 seconds")
    imglocation2 = pyautogui.locateCenterOnScreen('notaccept.png', confidence=0.7)
    if imglocation2 != None :
        toggle_button.config(text='ON')
        print("Someone didn't accept!")
    root.after(300,img)
    imglocation3 = pyautogui.locateCenterOnScreen('balance.png', confidence=0.7)
    if toggle_button.config('text')[-1] == 'OFF' and imglocation3 != None:
        if automode_button.config('text')[-1] == 'Automode ON':
            toggle_button.config(text='ON')
            print ('ON')

#Get Language
def Lang():
    path = os.getcwd()
    os.chdir(os.path.join(path,"Languages"))
    path = os.getcwd()

    f_in = open("Options.txt","r",encoding="utf-8")
    text= f_in.readline()
    f_in.close()
    text=text[10:]
    text=text.strip()

    os.chdir(os.path.join(path,text))
    
#Button on/off
def Simpletoggle():
    if toggle_button.config('text')[-1] == 'ON':
        toggle_button.config(text='OFF')
        print("OFF")
    else:
        toggle_button.config(text='ON')
        print("ON")

#Button Automode on/off
def SimpleToggle2():
    if automode_button.config('text')[-1] == 'Automode ON':
        automode_button.config(text='Automode OFF')
        print('Automode OFF')
    else:
        automode_button.config(text='Automode ON')
        print('Automode ON')

#Window
root = Tk()
root.title("Queue Accepter")
root.iconbitmap("icon.ico")
Hauteur = 0
Largeur = 250
(H,L,c) = (Hauteur,Largeur,"white")
Dessin = Canvas(root,height=H,width=L,bg=c)
Dessin.pack()

#Button
toggle_button = Button(text='OFF', width=10, command=Simpletoggle)
do = toggle_button['text']
toggle_button.pack(pady=10)

#Automode
automode_button = Button(text='Automode off', width=12, command=SimpleToggle2)
do = automode_button['text']
automode_button.pack(pady=5)

Lang()
#Loop
root.after(2000,img)
root.mainloop()
