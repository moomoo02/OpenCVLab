import cv2

img = cv2.imread('assets/elgato.jpeg', 1)
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
#-1, grb
# 0, grayscale
# 1, unchanged

cv2.imshow('Image',img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
