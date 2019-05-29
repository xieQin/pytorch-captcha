# -*- coding: UTF-8 -*-
import numpy as np
import torch
import os
from torch.autograd import Variable
import captcha_setting
from PIL import Image
import one_hot_encoding as ohe
from torch.utils.data import DataLoader,Dataset
import torchvision.transforms as transforms
from captcha_cnn_model import CNN
import image_label

class mydataset(Dataset):
    def __init__(self, path, transform=None):
        self.train_image_file_path = path
        self.transform = transform

    def __len__(self):
        return 1

    def __getitem__(self, idx):
        image_root = self.train_image_file_path
        image_name = image_root.split(os.path.sep)[-1]
        image = Image.open(image_root)
        if self.transform is not None:
            image = self.transform(image)
        label = ohe.encode(image_name.split('_')[0]) # 为了方便，在生成图片的时候，图片文件的命名格式 "4个数字或者数字_时间戳.PNG", 4个字母或者即是图片的验证码的值，字母大写,同时对该值做 one-hot 处理
        return image, label

transform = transforms.Compose([
    # transforms.ColorJitter(),
    transforms.Grayscale(),
    transforms.ToTensor(),
    # transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def get_recog_data_loader(image_path):
    dataset = mydataset(image_path, transform=transform)
    return DataLoader(dataset, batch_size=1, shuffle=True)

def cnn_recog(image_path):
    cnn = CNN()
    cnn.eval()
    cnn.load_state_dict(torch.load('./model.pkl'))
    print("load cnn net.")

    recog_dataloader = get_recog_data_loader(image_path)
    print(image_path)
    #vis = Visdom()
    for i, (images, labels) in enumerate(recog_dataloader):
        image = images
        vimage = Variable(image)
        predict_label = cnn(vimage)

        c = captcha_setting.ALL_CHAR_SET[np.argmax(predict_label[0, 0:captcha_setting.ALL_CHAR_SET_LEN].data.numpy())]

        c = '%s' % (c)
        return c

DATA_PATH = 'dataset/test/'
SVAE_PATH = 'dataset/crop/'
TEMP_PATH = 'dataset/temp/'å

def recog(img_path):
    recog_lable = ['*', '*', '*', '*']
    img_path_list = image_label.img_captcha_label(img_path, True, False)
    for crop_image in img_path_list:
        c = cnn_recog(crop_image)
        i = int(crop_image.split('/')[2].split('_')[0])
        print('%s' % (c))
        recog_lable[i] = c
        os.remove(crop_image)
    return ''.join(recog_lable)

# print(recog('dataset/test/97V5_1559106051034.png'))

