from ast import While
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8) #Black Image
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

    #Split into 4 parts
    image[:height//2, :width//2] = smaller_frame #Top left
    image[height//2:, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180) #Bottom left
    image[:height//2, width//2:] = smaller_frame #Top right
    image[height//2:, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180) #Bottom right

    cv2.imshow('image', image) 

    #cv2.imshow('frame', frame)

    #Breaks out when q is pressed
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()