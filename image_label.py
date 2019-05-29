import os
from PIL import Image
import time
import image_process
import captcha_setting

def captcha_label (is_crop, is_recog):
  image_file_paths = [os.path.join(captcha_setting.DATA_PATH, image_file) for image_file in os.listdir(captcha_setting.DATA_PATH)]
  for image in image_file_paths:
    img_captcha_label(image, is_crop, is_recog)
    os.remove(image)

def img_captcha_label (image, is_crop, is_recog):
  im = Image.open(image)
  text = '0123'
  if (is_recog):
    im.show()
    text = input("请输入验证码中的字符：")
    text = text.upper()
  suffix = str(int(time.time() * 1e3))
  if (im.size != (160,60)):
    im = im.resize((160, 60))
  if not os.path.exists(captcha_setting.TEMP_PATH):
    os.makedirs(captcha_setting.TEMP_PATH)
  im.save(captcha_setting.TEMP_PATH + text + "_" + suffix + ".png")
  if not os.path.exists(captcha_setting.SVAE_PATH):
    os.makedirs(captcha_setting.SVAE_PATH)
  # image_process.delete_line(im, image, SVAE_PATH)
  return image_process.capt_process(im, text, is_crop)
  # os.remove(image)
