import cv2
import random

img = cv2.imread("assets/elgato.jpeg", 1)

print(img.shape)

tag = img[500:700, 600:900]

img[100:300, 650:950] = tag

cv2.imshow('Image', img)
cv2.waitKey(10000)
cv2.destroyAllWindows()