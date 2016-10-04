# USAGE
# python counting_coins.py --image ../images/coins.png
# python counting_coins.py --image area/area.jpg

# Import the necessary packages
from __future__ import print_function
import numpy as np
import argparse
import cv2

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())

# Load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow("Image", image)

# The first thing we are going to do is apply edge detection to
# the image to reveal the outlines of the coins
#edged = cv2.Canny(blurred, 30, 150)
#cv2.imshow("Edges", edged)

# Find contours in the edged image.
# NOTE: The cv2.findContours method is DESTRUCTIVE to the image
# you pass in. If you intend on reusing your edged image, be
# sure to copy it before calling cv2.findContours
# (_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
circles = []
bla = cv2.HoughCircles( blurred[0:1000,0:1000], cv2.HOUGH_GRADIENT, 1, 50, 200, 100,minRadius= 50,maxRadius= 130 );
print(bla)

# How many contours did we find?
print("I count {} coins in this image".format(len(bla)))
if 1==1:
	quit()

# Let's highlight the coins in the original image by drawing a
# green circle around them
coins = image.copy()
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