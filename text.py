import cv2 
import pytesseract
import re
import pyautogui
from pynput.keyboard import Key, Controller
import time 
from PIL import Image

t0 = time.time()
t1 = time.time()
total = t1-t0

#########################Set this to the first 3 rows
top1 = 300
left1 = 60
right1 = 1000
bottom1 = 400
top2 = bottom1
left2 = left1
bottom2 = 120
right2 = right1
i = 1

timer = 30
while(total < timer):
    screenShot = pyautogui.screenshot()

    #--------------------Screenshot Processing--------------------#
    temp = 'pic' + str(i)
    screenShot.save(r'C:\Users\Mei_8\Documents\OTT\\'+temp+'.png')
    screenShot = Image.open(temp+'.png')

    if(i == 1):
        referencePic = screenShot.crop((left1,top1,right1,bottom1))
    else:
        referencePic = screenShot.crop((left2,top2,right2,bottom2))

    referencePic = referencePic.save(r'C:\Users\Mei_8\Documents\OTT\\'+temp+'.png')
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
            time.sleep(0.2)
        t1 = time.time()
        total = t1-t0
        print(total)
        if(total > timer): 
            quit()
    #----------------------------------------------------------------#
    if(i == 1):
        i = 2
    if(i == 2):
        i = 1
