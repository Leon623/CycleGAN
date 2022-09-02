import torch
import torchvision.transforms.functional as fn
import os
from PIL import Image

# Konstante
dir_path = os.path.dirname(os.path.realpath(__file__))
real_directory = dir_path + '/new_real/test/'
simulator_directory = dir_path + '/CarlaSimulatorScenes/Carla-Object-Detection-Dataset/combined/'
real_results = dir_path + '/final/real_results/'
simulator_results = dir_path + '/final/simulator_results/'


# Funkcija za obradu slika
def preprocess_image(img, crop_size, resize_size):
    if (crop_size):
        img = fn.center_crop(img, output_size=[crop_size, crop_size])

    if (resize_size):
        img = fn.resize(img, size=[resize_size, resize_size])

    return img


def preprocess_data(source_directory, results_directory, crop_size, resize_size, step_print, every_nth):
    k = 0
    for image in os.listdir(source_directory):

        if (k % every_nth == 0):
            img = Image.open(source_directory + str(image))
            img = preprocess_image(img, crop_size, resize_size)
            img.save(results_directory + str(k) + '.png')
        k += 1
        if (k % step_print == 0):
            print(f"{k} done...")


if __name__ == "__main__":
    preprocess_data(source_directory=real_directory, results_directory=real_results, crop_size=720, resize_size=256,
                    step_print=100, every_nth=4)

    preprocess_data(source_directory=simulator_directory, results_directory=simulator_results, crop_size=380,
                    resize_size=256,
                    step_print=100, every_nth=2)
