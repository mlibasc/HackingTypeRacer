import cv2 
import pytesseract
import re
import pyautogui
from pynput.keyboard import Key, Controller
import time 
from PIL import Image

#########################Set this to the first 3 rows
#height = 70
#width = 1070    left = 15, right = 1085
height = 35
width = 1070

left = 15
right = left + width
top = 55 
bottom = top + 35

i = 0
text = ""

while(len(text) < 950):
    screenShot = pyautogui.screenshot()

    #--------------------Screenshot Processing--------------------#
    temp = 'pic' + str(i)
    screenShot.save(r'C:/Users/Mei.li/Documents/Programs/Extra/HackingTypeRacer/'+temp+'.png')
    screenShot = Image.open(temp+'.png')

    if(i == 0):
        referencePic = screenShot.crop((left,top,right,bottom))
    elif(i == 1):
        newTop = top + 78
        referencePic = screenShot.crop((left,newTop,right,newTop+height))
    elif(i == 2):
        newTop = top + 155
        referencePic = screenShot.crop((left,newTop,right,newTop+height))
    elif(i == 3):
        newTop = top + 228
        referencePic = screenShot.crop((left,newTop,right,newTop+height))
    elif(i == 4):
        newTop = top + 150
        referencePic = screenShot.crop((left,newTop,right,newTop+height))
    elif(i == 5):
        referencePic = screenShot.crop((left,newTop,right,newTop+height))
    elif(i == 6):
        referencePic = screenShot.crop((left,newTop,right,newTop+height))

    referencePic = referencePic.save(r'C:/Users/Mei.li/Documents/Programs/Extra/HackingTypeRacer/'+temp+'.png')
    print("saved new img")
    #--------------------------------------------------------------#

    #--------------------Image Processing--------------------------#
    keyboard = Controller()
    time.sleep(2)

    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    img = cv2.imread(temp+'.png')

    text = pytesseract.image_to_string(img)
    text = text.lower()
    output = text.split()
    #----------------------------------------------------------------#

    #-------------------------------Typing---------------------------#
    for line in output:
        for letter in line:
            keyboard.press(letter)
            keyboard.release(letter)  
            time.sleep(0.1)
    #----------------------------------------------------------------#
    i = i+1
    if(i == 7):
        i == 0