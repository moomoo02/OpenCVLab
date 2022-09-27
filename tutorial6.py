from sqlite3 import converters
import numpy as np
import cv2
import random 

img = cv2.imread('assets/chessboard.png')
img = cv2.resize(img, (0,0), fx=1, fy=1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.goodFeaturesToTrack(source image, number of corners, minimum quality, euclidian distance)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners) #convert to integers

for corner in corners:
    x,y = corner.ravel() #[[1,2], [3,4]] -> [1,2,3,4]
    cv2.circle(img, (x,y), 5, (60,255,200), 3)

for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0,255,size = 3)))
        cv2.line(img, corner1, corner2, color,1)
cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
