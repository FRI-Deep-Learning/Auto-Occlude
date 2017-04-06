import numpy as np
import cv2
import random

IMG_SIZE = 64
MAX_SIZE = 25
MIN_SIZE = 15

name = 'small.jpg'

img = cv2.imread('small.jpg', 3)
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


x = cv2.waitKey(0)
if x == 27:
    cv2.destroyAllWindows()
