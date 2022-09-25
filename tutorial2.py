import cv2
import random

img = cv2.imread("assets/elgato.jpeg", -1)

for i in range(400):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imshow('Image', img)
cv2.waitKey(10000)
cv2.destroyAllWindows()