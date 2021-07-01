#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 下午1:41

import pytesseract
from PIL import Image

if __name__ == '__main__':
    pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'
    # text = pytesseract.image_to_string(Image.open('https://sit.miaocode.com/core/account/captcha?r=0.7553891298591418'))
    text = pytesseract.image_to_string(Image.open('/Users/lensaclrtn/Downloads/111.jpeg'))

    print(text)
