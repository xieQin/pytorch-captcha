import os
from PIL import Image
import time
import captcha_setting

THRESHOLD = 136
LUT = [0]*THRESHOLD + [1]*(256 - THRESHOLD)

def capt_process(capt, lable, is_crop):
  """
  图像预处理：将验证码图片转为二值型图片，按字符切割

  :require Image: from PIL import Image
  :require LUT: A lookup table, 包含256个值

  :param capt: 验证码Image对象
  :return capt_per_char_list: 一个数组包含四个元素，每个元素是一张包含单个字符的二值型图片
  """
  capt_gray = capt.convert("L")
  capt_bw = capt_gray.point(LUT, "1")
  capt_per_char_list = []
  for i in range(4):
    x = i * 40
    y = 5
    capt_per_char = capt_bw.crop((x, y, x + 40, y + 55))
    capt_per_char_list.append(capt_per_char)
  # print(capt_per_char_list)
  suffix = str(int(time.time() * 1e3))
  img_path = captcha_setting.SVAE_PATH + lable + '_' + suffix + '.png'
  # capt_bw.save(img_path)
  img = delete_line(capt_bw)
  if(is_crop):
    return crop(img, lable)
  else:
    img.save(img_path)
    return img_path

def crop(capt_bw, lable):
  capt_per_char_list = []
  img_path_list = []
  for i in range(4):
    x = i * 40
    y = 5
    capt_per_char = capt_bw.crop((x, y, x + 40, y + 55))
    capt_per_char_list.append(capt_per_char)
    suffix = str(int(time.time() * 1e3))
    capt_per_char_list[i].save(captcha_setting.SVAE_PATH + lable[i] + '_' + suffix + '.png')
    img_path_list.append(captcha_setting.SVAE_PATH + lable[i] + '_' + suffix + '.png')
  return img_path_list

def process ():
  image_file_paths = [os.path.join(captcha_setting.DATA_PATH, image_file) for image_file in os.listdir(captcha_setting.DATA_PATH)]
  for image in image_file_paths:
    lable = image.split('/')[2].split('_')[0]
    im = Image.open(image)
    delete_line(im, image, captcha_setting.SVAE_PATH)
    capt_process(im, captcha_setting.SVAE_PATH, lable)
    os.remove(image)

def delete_line(image):
  data = image
  (w,h) = data.size
  #data.getpixel((x,y))获取目标像素点颜色。
  #data.putpixel((x,y),255)更改像素点颜色，255代表颜色。
  for x in range(0, w):
    for y in range(0, h):
      # data.putpixel((10,10),0)
      # data.putpixel((42, 35),0)

      if x <= 18 and y >= 41:
        data.putpixel((x,y),255)
      if x in range(28, 35) and y in range(39, 42):
        data.putpixel((x,y),255)
      if x in range(42, 117) and y in range(36, 39):
        data.putpixel((x,y),255)
      if x in range(117, 131) and y in range(39, 42):
        data.putpixel((x,y),255)
      if x in range(123, 142) and y in range(42, 45):
        data.putpixel((x,y),255)
      if x >= 142 and y >= 41:
        data.putpixel((x,y),255)
  # data.save(img_path, "png")
  return data

# process('images/data/')