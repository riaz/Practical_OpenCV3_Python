import cv2
import glob
import math
import numpy as np

image = cv2.imread("../resources/images/plate.jpg")
image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# img = cv2.Canny(img, 100, 200)

# kernel = np.ones((3,3),np.uint8)

# applying gaussain blur
img = cv2.GaussianBlur(img, (5, 5), 0)

# since the number plate has numbers and the plate is aligned horizontally, we can sobel filter in vertical direction
img = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)

# thresholding
_, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

morph = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
cv2.morphologyEx(img, cv2.MORPH_CLOSE, morph, img)

img = cv2.GaussianBlur(img, (5, 5), 0)

_, contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(len(contours))

cv2.create

for cnt in contours:
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    image = cv2.drawContours(image, [box], 0, (0, 0, 255), 2)

cv2.imshow("Hello", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
