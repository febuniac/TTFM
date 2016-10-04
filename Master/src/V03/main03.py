# http://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/

## Main
# cd /Users/mauricioalouan/Dropbox/MLAgro/V03/
# source activate opencv

#########################################################
############## Imports
import numpy as np
import argparse
import cv2
import json
import time
import settings
import ttMLlib as tt

#########################################################
############## Variables
imagelocation = "/Users/mauricioalouan/Dropbox/MLAgro/V03/Area"
imagename = "Area.jpg"
Params_HSquareX = 80
Params_HSquareY = 80
Params_ScreenRes = (1280, 720)
Params_WindowSizeW = Params_ScreenRes[0]
Params_WindowSizeH = Params_ScreenRes[1]
Params_FileToSavePoints = "Points.json"
Params_FileToLoadPoints = Params_FileToSavePoints

ActiveWindowX1 = 1
ActiveWindowY1 = 1
ActiveWindowX2 = Params_WindowSizeW
ActiveWindowY2 = Params_WindowSizeH

GlobalImgWriterCounter = 50

############## Global ML Variables:
settings.init()
#GRede = []
#GRedePointer = 0
#GBDI = []
#GBDIPointer = 0
#GPoints = []
#GPointsPointer = 0

Points = []

def ScaledNamedWindow(WinName,screen_res,img):
	scale_width = screen_res[0] / img.shape[1]
	scale_height = screen_res[1] / img.shape[0]
	scale = min(scale_width, scale_height)
	window_width = int(img.shape[1] * scale)
	window_height = int(img.shape[0] * scale)
	cv2.namedWindow(WinName, cv2.WINDOW_NORMAL)
	cv2.resizeWindow(WinName, window_width, window_height)

#########################################################
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
MouseX = 1
MouseY = 1
GMouseX = 1
GMouseY = 1

#cropping = False
cropping = True
Gvw = None
GGravando = 0

#########################################################
############## Program Functions
def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global cropping, image, imageActive, imageClone, Points, Params_HSquareX, Params_HSquareY, ActiveWindowX1, ActiveWindowX2, ActiveWindowY1, ActiveWindowY2
 
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONUP:
		MouseX = x
		MouseY = y
		GMouseX = x + ActiveWindowX1 - 1
		GMouseY = y + ActiveWindowY1 - 1
		Points.append((GMouseX, GMouseY))
		print(Points)
		#cropping = not cropping

		# draw a rectangle around the region of interest
		if cropping:
			print("CROPPING")
			cv2.rectangle(image, (GMouseX-Params_HSquareX, GMouseY-Params_HSquareY), (GMouseX+Params_HSquareX, GMouseY+Params_HSquareY), (0, 255, 0), 2)
			cv2.rectangle(imageActive, (MouseX-Params_HSquareX, MouseY-Params_HSquareY), (MouseX+Params_HSquareX, MouseY+Params_HSquareY), (0, 255, 0), 2)
			imageActive = image[ActiveWindowY1:ActiveWindowY2, ActiveWindowX1:ActiveWindowX2]
			cv2.imshow("image", imageActive)
		else:
			## Not used anymore...
			print("NOT CROPPING")
			imageActive = imageClone[(ActiveWindowY1):(ActiveWindowY2), ActiveWindowX1:ActiveWindowX2].copy()
			cv2.imshow("image", imageActive)

def savePoints(data, filename):
	global Points
	# Saves Points
	data = {"Points": Points}
	f = open(filename, "w")
	json.dump(data, f)
	f.close()

def loadPointsFromFile(filename):
	global Points
	f = open(filename, "r")
	d = json.load(f)
	print(d)
	Points = d['Points']
	print(Points)
	f.close()

def showPoints():
	global image, imageActive, imageClone
	image = imageClone.copy()	
	for point in Points:
		cv2.rectangle(image, (point[0]-Params_HSquareX,point[1]-Params_HSquareY), (point[0]+Params_HSquareX,point[1]+Params_HSquareY), (0, 255, 0), 2)
	imageActive = image[ActiveWindowY1:ActiveWindowY2, ActiveWindowX1:ActiveWindowX2]
	cv2.imshow("image", imageActive)

def showPointsWithDelay():
	global image, imageActive, imageClone, GGravando
	image = imageClone.copy()	
	for point in Points:
		cv2.rectangle(image, (point[0]-Params_HSquareX,point[1]-Params_HSquareY), (point[0]+Params_HSquareX,point[1]+Params_HSquareY), (0, 255, 0), 2)
		imageActive = image[ActiveWindowY1:ActiveWindowY2, ActiveWindowX1:ActiveWindowX2]
		cv2.imshow("image", imageActive)
		#GravaTelaJpg()
		if GGravando == 1:
			print "gravando"
			GravaTelaNoVideo()
		key = cv2.waitKey(100) & 0xFF

def GravaTelaJpg():
	global imageActive, GlobalImgWriterCounter
	cv2.imwrite("Image" + str(GlobalImgWriterCounter) + ".jpg", imageActive)
	GlobalImgWriterCounter = GlobalImgWriterCounter + 1

def GravaTelaNoVideo():
	global Gvw, imagemAtiva
	cv.WriteFrame(Gvw, imagemAtiva)


def IniciaGravadorDeVideo():
	global Gvw, GGravando
	print "Iniciando Gravador"
	vfilename = "vid1.avi"
	vfourcc = 'XVID'
	vfps = 4
	vframeSize = (Params_WindowSizeW,Params_WindowSizeH)
	Gvw = cv2.VideoWriter(vfilename, -1, vfps, vframeSize,1)
	GGravando = 1
	print "Iniciado"


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=False, help="Path to the image")
args = vars(ap.parse_args())
if args["image"] == None:
	args["image"] = imagelocation + "/" + imagename

# load the image, clone it, and setup the mouse callback function
image = cv2.imread(args["image"])
imageClone = image.copy()
imageActive = image[ActiveWindowY1:ActiveWindowY2, ActiveWindowX1:ActiveWindowX2]
cv2.namedWindow("image")
cv2.resizeWindow("image", Params_WindowSizeW, Params_WindowSizeH)
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setMouseCallback("image", click_and_crop)
 
# keep looping until the 'q' key is pressed
cv2.imshow("image", imageActive)
while True:
	# display the image and wait for a keypress
	key = cv2.waitKey(1) & 0xFF
	#cv2.imshow("image", imageActive)
 
	# if the 'ESC' key is pressed, Quit
	if key == 27:
		quit()

	# if the 'z' key is pressed, undo
	if key == ord("z"):
		Points.pop()
		showPoints()
 
	# if the 's' key is pressed, save points
	elif key == ord("s"):
		savePoints(Points, Params_FileToSavePoints)
		break

	# if the 'l' key is pressed, load points
	elif key == ord("l"):
		loadPointsFromFile(Params_FileToLoadPoints)
		showPoints()

	# if the 'p' key is pressed, load points with delay
	elif key == ord("p"):
		loadPointsFromFile(Params_FileToLoadPoints)
		showPointsWithDelay()

	# if the 'g' key is pressed, GravaTela como JPG
	elif key == ord("g"):
		GravaTelaJpg()

	# if the 'v' key is pressed, GravaVideo
	elif key == ord("v"):
		print "video not working"
		#IniciaGravadorDeVideo()
		#showPointsWithDelay()
		#Gvw.release()

	elif key == 0:
		ActiveWindowY1 = ActiveWindowY1 - Params_WindowSizeH
		ActiveWindowY2 = ActiveWindowY2 - Params_WindowSizeH
		imageActive = image[(ActiveWindowY1):(ActiveWindowY2), ActiveWindowX1:ActiveWindowX2].copy()
		cv2.imshow("image", imageActive)
		print "up"
	elif key == 1:
		ActiveWindowY1 = ActiveWindowY1 + Params_WindowSizeH
		ActiveWindowY2 = ActiveWindowY2 + Params_WindowSizeH
		imageActive = image[(ActiveWindowY1):(ActiveWindowY2), ActiveWindowX1:ActiveWindowX2].copy()
		cv2.imshow("image", imageActive)
		print "down"
	elif key == 2:
		ActiveWindowX1 = ActiveWindowX1 - Params_WindowSizeW
		ActiveWindowX2 = ActiveWindowX2 - Params_WindowSizeW
		imageActive = image[(ActiveWindowY1):(ActiveWindowY2), ActiveWindowX1:ActiveWindowX2].copy()
		cv2.imshow("image", imageActive)
		print "left"
	elif key == 3:
		ActiveWindowX1 = ActiveWindowX1 + Params_WindowSizeW
		ActiveWindowX2 = ActiveWindowX2 + Params_WindowSizeW
		imageActive = image[(ActiveWindowY1):(ActiveWindowY2), ActiveWindowX1:ActiveWindowX2].copy()
		cv2.imshow("image", imageActive)
		print "right"

	elif key == ord("k"):
		while True:
			xxx = raw_input(":")
			if xxx == 'k':
				break
			else:
				tt.ProcessaComandos(xxx)
			#break

	elif key != 255:
		print(key)
	else:		
		pass

# if there are two reference points, then crop the region of interest
# from teh image and display it
if 1 == 2:
	roi = imageClone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
	cv2.imshow("ROI", roi)
	cv2.waitKey(0)
 
# close all open windows
cv2.destroyAllWindows()




## Keys
# ESC	quit
# z		undo last point (actually delete last point)
# s		save points
# l		load points
# p		play points
# g		grava tela em jpg


