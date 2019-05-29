from PIL import Image
import image_label
import uuid
import get_images
import captcha_setting

count = 100

for i in range(count):
  uid = uuid.uuid1()
  get_images.get_9f_captcha(i, uid)

image_label.captcha_label(True, True)