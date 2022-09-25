import cv2

img = cv2.imread('assets/elgato.jpeg', 0)

#-1, grb
# 0, grayscale
# 1, unchanged

cv2.imshow('Image',img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
