import torch
import torchvision.transforms.functional as fn
import os
from PIL import Image

# Konstante

dir_path = os.path.dirname(os.path.realpath(__file__))
real_directory = dir_path + '/testing/image_2/'
simulator_directory = dir_path + '/simulator/dataA/dataA/CameraRGB/'
real_results = dir_path + '/real_results/'
simulator_results = dir_path + '/simulator_results/'
crop_size = 256
resize_size = 0
step_print = 20
every_nth = 4


# Funkcija za obradu slika
def preprocess(img, crop_size, resize_size):
    if (crop_size):
        img = fn.center_crop(img, output_size=[crop_size, crop_size])

    if (resize_size):
        img = fn.resize(img, size=[resize_size, resize_size])

    return img


# Stvarne slike
k = 0
for image in os.listdir(real_directory):

    img = Image.open(real_directory + str(image))
    img = preprocess(img, crop_size, resize_size)
    img.save(real_results + str(k) + '.png')
    k += 1
    if (k % step_print == 0):
        print(f"{k} done...")

# Simulator slike
k = 0
for image in os.listdir(simulator_directory):

    if (k % every_nth == 0):
        img = Image.open(simulator_directory + str(image))
        img = preprocess(img, crop_size, resize_size)
        img.save(simulator_results + str(k) + '.png')
    k += 1
    if (k % step_print == 0):
        print(f"{k} done...")
