import requests
import json
import base64
import time
import os
from PIL import Image
import image_label
import uuid
import captcha_setting

def get_9f_captcha (i, uuid):
  res = requests.post(
    'https://wx.9fbank.com/apiUrl/api/security/picVerifyUUidH5?time=1558436489355',
    data={'uuid': uuid}
  ) # 9fu验证码接口
  # print(res.text)
  data = json.loads(res.text)['data']
  img = base64.b64decode(data['verifyCode'])
  now = str(int(time.time()))
  if not os.path.exists(captcha_setting.DATA_PATH):
    os.makedirs(captcha_setting.DATA_PATH)
  img_path = captcha_setting.DATA_PATH + str(i) + '_' + now  + '.png'
  file = open(img_path, 'wb') 
  file.write(img)  
  file.close()
  return img_path
