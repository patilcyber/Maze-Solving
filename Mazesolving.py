# Coded By: Sourav Singh.

import cv2
import numpy as np

# Read the image.
img = cv2.imread("maze00.jpg")
# Converting image to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Converting grayscale image to the binary image.
ret, original_binary_img = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

# Finding the length and breadth of the image.
x = len(original_binary_img)
y = len(original_binary_img[0])

g=10
if x>200:
	g=20
# Drawing the line on the starting point and ending point.
cv2.line(original_binary_img, (0,2),(0,17),(255,255,255),2)
cv2.line(original_binary_img, (x-17,y-1),(y-1,y-1),(255,255,255),2)

# Converting the image into the inverse binary image.	
ret, thresh = cv2.threshold(original_binary_img, 127, 255, cv2.THRESH_BINARY_INV) 

# Drawing contours in the image (First to find the contours across the border then to draw the contour across the image, just by changing the value different from 10 you can solve the different type of maze). 
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
dc = cv2.drawContours(thresh, contours, 0, (255, 255, 255), 10)
dc = cv2.drawContours(dc, contours, 1, (0,0,0) , 10)

# Converting the contoured image into the binary image again.
ret, thresh = cv2.threshold(dc, 240, 255, cv2.THRESH_BINARY)

ke = 25
kernel = np.ones((ke, ke), np.uint8)

# Doing dilation in the binary image so that white colour dilute into the maze. 
dilation = cv2.dilate(thresh, kernel, iterations=1)

# Erosion spread the black part over the maze got after the dilation.
erosion = cv2.erode(dilation, kernel, iterations=1)

# Here we are making the difference in both the images dilation and erosion to get the path part in the maze.
diff = cv2.absdiff(dilation, erosion)

# Converting the colour to  show the maze path with black colour
ret, thresh2 = cv2.threshold(diff, 127, 255, cv2.THRESH_BINARY_INV)

# Showing the solved maze image.
cv2.imshow('Image', thresh2)
cv2.waitKey(0)
# res = cv2.resize(diff, dsize=(100,100), interpolation=cv2.INTER_CUBIC)
