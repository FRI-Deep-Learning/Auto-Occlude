import os
import cv2


def get_image_tuples():
    images_dir = os.getcwd() + "\images"
    list_of_images = os.listdir(images_dir)

    return tuple(list_of_images)

