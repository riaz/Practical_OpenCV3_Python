import cv2
import glob
import math
import numpy as np

img = cv2.imread("../resources/images/car2.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#img = cv2.Canny(img, 100, 200)

#kernel = np.ones((3,3),np.uint8)
img = cv2.GaussianBlur(img,(5,5),0)

img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
cv2.imshow("Hello", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
