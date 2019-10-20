#!/usr/bin/python3
import shutil
from PIL import Image
import pytesseract


def getCaptcha(session, url):

    response = session.get(url, timeout=3, stream=True)
    with open('captcha.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

    img = Image.open("captcha.png")
    text = pytesseract.image_to_string(img)

    return text
