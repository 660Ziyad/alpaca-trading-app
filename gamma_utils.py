import cv2
import pytesseract
import re

def extract_gamma_strikes(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)

    strikes = re.findall(r'\d{4,5}', text)
    return list(set(strikes))
