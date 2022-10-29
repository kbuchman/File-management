from PIL import Image as im
from pytesseract import image_to_string, pytesseract

# path to disc files with tesseract
pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
TESSDATA_PREFIX = 'C:/Program Files/Tesseract-OCR'

def get_text_from_image(file_path, language):
    output = image_to_string(im.open(file_path).convert("RGB"), lang=language)
    return output

if __name__ == '__main__':
    print(get_text_from_image('test.png', 'pol'))