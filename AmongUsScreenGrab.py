#Athanasios Tsivgas - Amoung Us Auto Muter (screen grab end)
#this code essentially grabs certian pixels on the screen and color matches them to figure out if the user is in the meeting screen or not (while in the meeting screen it will unmute everyone)
from PIL import Image, ImageGrab
import time
import pynput
from pynput.keyboard import Key, Controller
timer = 1
status = "none"
keyboard = Controller()
while(timer!=0):
    time.sleep(1)
    screen = ImageGrab.grab();
    pix1 = str(screen.getpixel((228,56))) #vote = (143, 151, 164)
    pix2 = str(screen.getpixel((1656,982))) #vote = (143, 151, 164)
    pix3 = str(screen.getpixel((226,1011))) #vote = (143, 151, 164)
    pix4 = str(screen.getpixel((283,222))) #vote = (238, 244, 251)
    pix5 = str(screen.getpixel((912,340))) #vote = (170, 200, 229)
    colorCheck = 0
    if(pix1=="(143, 151, 164)"):
        colorCheck+=1

    if(pix2=="(143, 151, 164)"):
        colorCheck+=1

    if(pix3=="(143, 151, 164)"):
        colorCheck+=1

    if(pix4=="(238, 244, 251)"):
        colorCheck+=1

    if(pix5=="(170, 200, 229)"):
        colorCheck+=1
#keybindings for def (right now its set to ctrl l), essentially how it works is the client deffens and the AmoungUsMuter.py will see that the client deffened and mute everyone
#then when out of a meeting the client will undeffen and the AmoungUsMuter.py will un mute everyone
#this is done with deffen so that the client user can mute durring meetings if they want without the program muting everyone else
#so change your discord keybind for deffen to ctrl l and it will work fine or change the keybind here in the code
    if(colorCheck>2 and status!="meeting"):
        status = "meeting"
        keyboard.press(Key.ctrl)
        keyboard.press('l')
        keyboard.release('l')
        keyboard.release(Key.ctrl)
        print("MEETING " + str(colorCheck))
    elif(colorCheck<2 and status=="meeting"):
        status = "none"
        keyboard.press(Key.ctrl)
        keyboard.press('l')
        keyboard.release('l')
        keyboard.release(Key.ctrl)
        print("No Meeting ")
    else:
        print("No Meeting else " + str(colorCheck))
