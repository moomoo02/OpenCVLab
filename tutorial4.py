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


    img = cv2.rectangle(frame, (100,100), (200,200), (128,128,128), 5)
    cv2.imshow('frame', frame)

    #Breaks out when q is pressed
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()