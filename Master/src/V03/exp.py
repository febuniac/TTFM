import numpy as np
import argparse
import cv2
import json
import time
import cPickle
import settings as ss
imagelocation = "/Users/mauricioalouan/Dropbox/MLAgro/V03/Area"
imagename = "Area.jpg"
Params_HSquareX = 80
Params_HSquareY = 80
Params_ScreenRes = (1280, 720)
Params_WindowSizeW = Params_ScreenRes[0]
Params_WindowSizeH = Params_ScreenRes[1]
Params_FileToSavePoints = "Points.json"
Params_FileToLoadPoints = Params_FileToSavePoints

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=False, help="Path to the image")
_StoreAction(option_strings=['-i', '--image'], dest='image', nargs=None, const=None, default=None, type=None, choices=None, help='Path to the image', metavar=None)
args = vars(ap.parse_args())

if args["image"] == None:
	args["image"] = imagelocation + "/" + imagename

image = cv2.imread(args["image"])
imageClone = image.copy()
cv2.imshow("image",image)
#(B, G, R) = cv2.split(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



blurred = cv2.medianBlur(gray, 7)
canny = cv2.Canny(image, 30, 150)
cv2.imshow("Canny", canny)
