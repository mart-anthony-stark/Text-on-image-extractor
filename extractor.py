import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"D:\tesseract\Tesseract-OCR\tesseract.exe"

img = Image.open("text-custom-font.png")
text = pytesseract.image_to_string(img)
print(text)
