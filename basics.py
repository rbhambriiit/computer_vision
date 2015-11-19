
import cv2


image = cv2.imread('pass1.jpg')
image.shape  ##[h,w,3]

original = image.copy()

resized=cv2.resize(image,(new_width,new_height))
cv2.imwrite('resized_pass1.jpg',resized)

# convert the image to grayscale, blur it, and find edges
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
cv2.imwrite('grayed_pass1.jpg',gray)

gray = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imwrite('blurred_pass1.jpg',gray)
edged = cv2.Canny(gray, 75, 200)
cv2.imwrite('edged_pass1.jpg',edged)

'''
## at this stage - ready to try other cool things for images: recognition, visualisation, draw shapes, extract regions, find contours,....

This can require what we learnt so far:
## list modification - images can be represented as a list of pixels with each pixel containtig data.
    you can modify these values to perform image operation, lets say convert a grayscale image to binary or take negative of an image

mylist=[1,3,-6,-10,4]
newlist=[]
>>> for iter in mylist:
	if iter > 0:
		newlist.append(1)
	else:
		newlist.append(0)

>>> newlist
[1, 1, 0, 0, 1]

'''
