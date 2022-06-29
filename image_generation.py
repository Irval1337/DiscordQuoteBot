import imgkit
import base64
from io import BytesIO
import io
import urllib.request
from PIL import Image
import sys, os

class Image_generation:
    def __init__(self, crop_w, wkhtmltoimage_path):
        self.crop_w = crop_w
        self.wkhtmltoimage_path = wkhtmltoimage_path

    def generate(self, username, message, date, color, avatar_img):
        s = ""
        with open('index.html') as f:
            s = f.read()
        s = s.replace("date_string", date)
        s = s.replace("message_string", message)
        s = s.replace("username_string", username)
        s = s.replace("rgb(46, 204, 113)", color)

        img = Image.open(BytesIO(avatar_img))
        img = img.resize((80,80))
        imgByteArr = io.BytesIO()
        img.save(imgByteArr, format="PNG")
        imgByteArr = imgByteArr.getvalue()
        img_str = base64.b64encode(imgByteArr)
        s = s.replace("avatar_base64", img_str.decode("UTF-8"))

        options = {
            'crop-w': self.crop_w,
        }

        config = imgkit.config(wkhtmltoimage=self.wkhtmltoimage_path)
        
        return imgkit.from_string(s, False, options=options, config=config)
