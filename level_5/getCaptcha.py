#!/usr/bin/python3
from PIL import Image
import pytesseract
import shutil
import numpy as np


def getCaptcha(session, url):

    response = session.get(url, timeout=3, stream=True)
    with open('captcha.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

    im = Image.open('captcha.png')
    im = im.convert('RGBA')

    data = np.array(im)   # "data" is a height x width x 4 numpy array
    # Temporarily unpack the bands for readability
    red, green, blue, alpha = data.T

    # Replace black with grey.. (leaves alpha values alone...)
    black_areas = (red == 0) & (blue == 0) & (green == 0)
    data[..., :-1][black_areas.T] = (125, 125, 125)  # Transpose back needed

    im2 = Image.fromarray(data)
    im2.save('clean-captcha.png')
    im = Image.open('clean-captcha.png')
    text = pytesseract.image_to_string(im)
    return text
