# -*- coding: UTF-8 -*-
import os
# 验证码中的字符
# string.digits + string.ascii_uppercase
NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

ALL_CHAR_SET = NUMBER + ALPHABET
ALL_CHAR_SET_LEN = len(ALL_CHAR_SET)
MAX_CAPTCHA = 4

# 网络设置
EPOCHS = 30
BATCH_SIZE = 10

# 图像大小
IMAGE_HEIGHT = 55
IMAGE_WIDTH = 40

DATA_PATH = 'images/data/'
SVAE_PATH = 'images/test/'
TRAIN_PATH = 'images/test/'
TEMP_PATH = 'images/temp/'
TEST_PATH = 'images/test/'