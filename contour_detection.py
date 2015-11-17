## contour detection.
## credits adrian rosebrock - pyimage search blog

import cv2
import numpy as np


image = cv2.imread('pass1.jpg')
image.shape  ##[h,w,3]


ratio = image.shape[0] / 500.0
new_width=int(image.shape[1]/ratio)
original = image.copy()

resized=cv2.resize(image,(new_width,500))
cv2.imwrite('resized_pass1.jpg',resized)

# convert the image to grayscale, blur it, and find edges
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
cv2.imwrite('grayed_pass1.jpg',gray)

gray = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imwrite('blurred_pass1.jpg',gray)
edged = cv2.Canny(gray, 75, 200)
cv2.imwrite('edged_pass1.jpg',edged)


## at this stage try other images as well..
## contour:

(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]


# loop over the contours
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) == 4:
        screenCnt = approx
	break

##draw
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
cv2.imwrite("Outline_pass1.jpg", image)
