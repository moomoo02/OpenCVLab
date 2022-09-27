from ast import While
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    #Lines: cv2.line(image, start, end, color, thickness)
    img = cv2.line(frame, (0,0), (width, height), (255,0,0), 10)
    img = cv2.line(frame, (width,0), (0, height), (255,0,0), 10)

    #Rectangle: cv2.rectangle(frame, top-left, bottom-right, color, thickness)
    img = cv2.rectangle(frame, (100,100), (200,200), (128,128,128), 5)

    #Circle: cv2.circle(frame, center-position, radius, color, thickness(-1 to fill))
    img = cv2.circle(frame, (300,300), 60, (0,0,255), -1)

    cv2.imshow('frame', frame)

    #Breaks out when q is pressed
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()