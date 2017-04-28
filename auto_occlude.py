import numpy as np
import cv2
import random
import os

IMG_SIZE = 64
MAX_SIZE = 25
MIN_SIZE = 15
# Remember to modify this!
ROOT_DIR = ""

def random_occlude(name):
	img = cv2.imread(name, 3)
	cv2.namedWindow('image', cv2.WINDOW_NORMAL)
	cv2.imshow('image', img)


	width = random.randrange(MIN_SIZE, MAX_SIZE)
	height = random.randrange(MIN_SIZE, MAX_SIZE)

	x = random.randrange(1, IMG_SIZE-MAX_SIZE)
	y = random.randrange(1, IMG_SIZE-MAX_SIZE)

	# Python: cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
	occlude = cv2.rectangle(img, (x, y), (x + width, y + height), 0, -1)

	cv2.imshow('image', occlude)
	cv2.imwrite('occluded-'+name, occlude)


def auto_occlude():
	for subdir, dirs, files in os.walk(ROOT_DIR):
		for file in files:
			print(file)
			random_occlude(file)

auto_occlude()

