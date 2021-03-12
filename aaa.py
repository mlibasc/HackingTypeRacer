import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open('pic1.png')

text = pytesseract.image_to_string(img, config='')
print(text)