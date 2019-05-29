import os
from PIL import Image

def resize (DATA_PATH):
  image_file_paths = [os.path.join(DATA_PATH, image_file) for image_file in os.listdir(DATA_PATH)]
  for image in image_file_paths:
    im = Image.open(image)
    if (im.size != (160,60)):
      im = im.resize((160, 60))
      im.save(image)