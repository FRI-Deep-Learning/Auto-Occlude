import numpy as np
import cv2

img = cv2.imread('image.jpg', 3)


cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image.jpg', img)
x = cv2.waitKey(0)
if x == 27:
    cv2.destroyAllWindows()

