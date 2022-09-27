import numpy as np
import cv2

img = cv2.imread('assets/chessboard.png')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
