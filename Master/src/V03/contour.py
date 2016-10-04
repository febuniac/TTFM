# USAGE
# python counting_coins.py --image ../images/coins.png
# python counting_coins.py --image area/area.jpg

# Import the necessary packages
from __future__ import print_function
import numpy as np
import argparse
import cv2

# Construct the argument parser and parse the arguments

# Load the image, convert it to grayscale, and blur it slightly
image = cv2.imread("imgs/im001.jpg")
image = image[20:140,20:140,:]

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
gblurred = cv2.medianBlur(gray, 7)
#cv2.imshow("Image", image)
#cv2.imshow("Image", blurred)

(B, G, R) = cv2.split(image)
zeros = np.zeros(image.shape[:2], dtype = "uint8")
GG = cv2.merge([zeros, G, zeros])
BB = cv2.merge([B, zeros, zeros])
RR = cv2.merge([zeros, zeros, R])
gb7 = cv2.medianBlur(GG, 7)
gb9 = cv2.medianBlur(GG, 9)
gb11 = cv2.medianBlur(GG, 11)

bb7 = cv2.medianBlur(BB, 7)
bb9 = cv2.medianBlur(BB, 9)
bb11 = cv2.medianBlur(BB, 11)

rb7 = cv2.medianBlur(RR, 7)
rb9 = cv2.medianBlur(RR, 9)
rb11 = cv2.medianBlur(RR, 11)

gcombo = np.hstack([GG,gb7,gb9,gb11])
bcombo = np.hstack([BB,bb7,bb9,bb11])
rcombo = np.hstack([RR,rb7,rb9,rb11])

rmin = np.min(R[0:5,0:5])
rmax = np.max(R[0:5,0:5])
print(rmin)
print(rmax)

combo = np.vstack([gcombo,bcombo,rcombo])
cv2.imshow("i",combo)


# The first thing we are going to do is apply edge detection to
# the image to reveal the outlines of the coins
edged = cv2.Canny(gb9, 180, 220)
cv2.imshow("Edges", edged)



# Find contours in the edged image.
# NOTE: The cv2.findContours method is DESTRUCTIVE to the image
# you pass in. If you intend on reusing your edged image, be
# sure to copy it before calling cv2.findContours
# (_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
circles = []
(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cv2.HoughCircles( blurred, cv2.HOUGH_GRADIENT, 1, 50, 200, 100,minRadius= 50,maxRadius= 130 );
print(cnts)

# How many contours did we find?
#print("I count {} coins in this image".format(len(cnts)))
if 1==2:
	quit()

# Let's highlight the coins in the original image by drawing a
# green circle around them
coins = image.copy()
if not cnts:
	cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
	cv2.imshow("Coins", coins)
	cv2.waitKey(0)

# Now, let's loop over each contour
for (i, c) in enumerate(cnts):
	# We can compute the 'bounding box' for each contour, which is
	# the rectangle that encloses the contour
	(x, y, w, h) = cv2.boundingRect(c)

	# Now that we have the contour, let's extract it using array
	# slices
	print("Coin #{}".format(i + 1))
	coin = image[y:y + h, x:x + w]
	cv2.imshow("Coin", coin)

	# Just for fun, let's construct a mask for the coin by finding
	# The minumum enclosing circle of the contour
	mask = np.zeros(image.shape[:2], dtype = "uint8")
	((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
	cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
	mask = mask[y:y + h, x:x + w]
	cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask = mask))
	cv2.waitKey(0)