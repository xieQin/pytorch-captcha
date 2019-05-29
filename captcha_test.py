# -*- coding: UTF-8 -*-
import numpy as np
import torch
from torch.autograd import Variable
import captcha_setting
import my_dataset
from captcha_cnn_model import CNN
import one_hot_encoding

def main():
    cnn = CNN()
    cnn.eval()
    cnn.load_state_dict(torch.load('model.pkl'))
    print("load cnn net.")

    test_dataloader = my_dataset.get_test_data_loader()

    correct = 0
    total = 0
    wrong_letter = []
    total_letter = {}
    for i in captcha_setting.ALPHABET:
        total_letter[i] = {
            'times': 0,
            'success': 0,
            'fail': 0
        }
    for i in captcha_setting.NUMBER:
        total_letter[i] = {
            'times': 0,
            'success': 0,
            'fail': 0
        }
    for i, (images, labels) in enumerate(test_dataloader):
        image = images
        vimage = Variable(image)
        predict_label = cnn(vimage)

        c = captcha_setting.ALL_CHAR_SET[np.argmax(predict_label[0, 0:captcha_setting.ALL_CHAR_SET_LEN].data.numpy())]

        predict_label = '%s' % (c)
        print('predict_label: ' + predict_label)
        true_label = one_hot_encoding.decode(labels.numpy()[0])
        total += labels.size(0)
        print('true_label: ' + true_label)
        total_letter[true_label]['times'] += 1
        if(predict_label == true_label):
            total_letter[true_label]['success'] += 1
            correct += 1
        else:
            total_letter[true_label]['fail'] += 1
            wrong_letter.append(true_label)
        if(total%200==0):
            print('Test Accuracy of the model on the %d test images: %f %%' % (total, 100 * correct / total))
    print('Test Accuracy of the model on the %d test images: %f %%' % (total, 100 * correct / total))
    print(wrong_letter)
    for i in total_letter:
        print('%s, success: %d fail: %d' % (i, total_letter[i]['success'], total_letter[i]['fail']))
    # print(total_letter)

if __name__ == '__main__':
    main()


