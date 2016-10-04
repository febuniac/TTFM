# http://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/

## Main
# cd /Users/mauricioalouan/Dropbox/MLAgro/V03/
# cd /Users/mauricioalouan/Dropbox/ProjetoTT/V03/
# source activate opencv
# python main04.py

#########################################################
############## Imports
import numpy as np
import argparse
import cv2
import json
import time
import settings as ss
import ttMLlib as tt

#########################################################

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
	global cropping
 
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONUP:
		MouseX = x
		MouseY = y
		GMouseX = x + ss.ActiveWindowX1 - 1
		GMouseY = y + ss.ActiveWindowY1 - 1

		ss.Points.append((GMouseX, GMouseY, ss.Point_Shp, ss.Point_Rad, ss.Point_Lay))
		print(ss.Points)
		#cropping = not cropping

		# draw a rectangle around the region of interest
		if cropping:
			print("CROPPING")
			cv2.rectangle(ss.image, (GMouseX-ss.Point_Rad, GMouseY-ss.Point_Rad), (GMouseX+ss.Point_Rad, GMouseY+ss.Point_Rad), ss.Lay_col[ss.Point_Lay], 2)
			cv2.rectangle(ss.imageActive, (MouseX-ss.Point_Rad, MouseY-ss.Point_Rad), (MouseX+ss.Point_Rad, MouseY+ss.Point_Rad), ss.Lay_col[ss.Point_Lay], 2)
			ss.imageActive = ss.image[ss.ActiveWindowY1:ss.ActiveWindowY2, ss.ActiveWindowX1:ss.ActiveWindowX2]
			cv2.imshow("image", ss.imageActive)
		else:
			## Not used anymore...
			print("NOT CROPPING")
			ss.imageActive = ss.imageClone[(ss.ActiveWindowY1):(ss.ActiveWindowY2), ss.ActiveWindowX1:ss.ActiveWindowX2].copy()
			cv2.imshow("image", ss.imageActive)


def showPoints():
	ss.image = ss.imageClone.copy()	
	for point in ss.Points:
		if len(point) ==2:
			cv2.rectangle(ss.image, (point[0]-ss.Point_Rad,point[1]-ss.Point_Rad), (point[0]+ss.Point_Rad,point[1]+ss.Point_Rad), (0, 255, 0), 2)
		else:
			cv2.rectangle(ss.image, (point[0]-point[3],point[1]-point[3]), (point[0]+point[3],point[1]+point[3]), ss.Lay_col[point[4]], 2)
		
	ss.imageActive = ss.image[ss.ActiveWindowY1:ss.ActiveWindowY2, ss.ActiveWindowX1:ss.ActiveWindowX2]
	cv2.imshow("image", ss.imageActive)

def showPointsWithDelay():
	global GGravando
	ss.image = ss.imageClone.copy()
	for point in ss.Points:
		cv2.rectangle(ss.image, (point[0]-ss.Point_Rad,point[1]-ss.Point_Rad), (point[0]+ss.Point_Rad,point[1]+ss.Point_Rad), (0, 255, 0), 2)
		ss.imageActive = ss.image[ss.ActiveWindowY1:ss.ActiveWindowY2, ss.ActiveWindowX1:ss.ActiveWindowX2]
		cv2.imshow("image", ss.imageActive)
		#GravaTelaJpg()
		if GGravando == 1:
			print "gravando"
			GravaTelaNoVideo()
		key = cv2.waitKey(100) & 0xFF

def GravaTelaJpg():
	cv2.imwrite("Image" + str(ss.GlobalImgWriterCounter) + ".jpg", ss.imageActive)
	ss.GlobalImgWriterCounter = ss.GlobalImgWriterCounter + 1

def GravaTelaNoVideo():
	# Not working on mac (can test on windows)
	#global Gvw, imagemAtiva
	#cv.WriteFrame(Gvw, imagemAtiva)
	pass


def IniciaGravadorDeVideo():
	global Gvw, GGravando
	print "Iniciando Gravador"
	vfilename = "vid1.avi"
	vfourcc = 'XVID'
	vfps = 4
	vframeSize = (ss.Params_WindowSizeW,ss.Params_WindowSizeH)
	Gvw = cv2.VideoWriter(vfilename, -1, vfps, vframeSize,1)
	GGravando = 1
	print "Iniciado"


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=False, help="Path to the image")
args = vars(ap.parse_args())
if args["image"] == None:
	args["image"] = ss.imagelocation + "/" + ss.imagename

# load the image, clone it, and setup the mouse callback function
ss.image = cv2.imread(args["image"])
ss.imageClone = ss.image.copy()
ss.imageActive = ss.image[ss.ActiveWindowY1:ss.ActiveWindowY2, ss.ActiveWindowX1:ss.ActiveWindowX2]
cv2.namedWindow("image")
cv2.resizeWindow("image", ss.Params_WindowSizeW, ss.Params_WindowSizeH)
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setMouseCallback("image", click_and_crop)
 
# keep looping until the 'q' key is pressed
cv2.imshow("image", ss.imageActive)
while True:
	# display the image and wait for a keypress
	key = cv2.waitKey(1) & 0xFF
	#cv2.imshow("image", imageActive)
 
	# if the 'ESC' key is pressed, Quit
	if key == 27:
		quit()

	# if the 'z' key is pressed, undo
	if key == ord("z"):
		ss.Points.pop()
		showPoints()
 
	# if the 's' key is pressed, save points
	elif key == ord("s"):
		tt.savePoints(ss.Points, ss.Params_FileToSavePoints)

	# if the 'l' key is pressed, load points
	elif key == ord("l"):
		ss.Points = tt.loadPointsFromFile(ss.Params_FileToLoadPoints)
		print("##### mm #####")
		print(ss.Points)
		showPoints()

	# if the 'p' key is pressed, load points with delay
	elif key == ord("p"):
		ss.Points = tt.loadPointsFromFile(ss.Params_FileToLoadPoints)
		print("##### mm #####")
		print(ss.Points)
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
		ss.ActiveWindowY1 = ss.ActiveWindowY1 - ss.Params_WindowSizeH
		ss.ActiveWindowY2 = ss.ActiveWindowY2 - ss.Params_WindowSizeH
		ss.imageActive = ss.image[(ss.ActiveWindowY1):(ss.ActiveWindowY2), ss.ActiveWindowX1:ss.ActiveWindowX2].copy()
		cv2.imshow("image", ss.imageActive)
		print "up"
	elif key == 1:
		ss.ActiveWindowY1 = ss.ActiveWindowY1 + ss.Params_WindowSizeH
		ss.ActiveWindowY2 = ss.ActiveWindowY2 + ss.Params_WindowSizeH
		ss.imageActive = ss.image[(ss.ActiveWindowY1):(ss.ActiveWindowY2), ss.ActiveWindowX1:ss.ActiveWindowX2].copy()
		cv2.imshow("image", ss.imageActive)
		print "down"
	elif key == 2:
		ss.ActiveWindowX1 = ss.ActiveWindowX1 - ss.Params_WindowSizeW
		ss.ActiveWindowX2 = ss.ActiveWindowX2 - ss.Params_WindowSizeW
		ss.imageActive = ss.image[(ss.ActiveWindowY1):(ss.ActiveWindowY2), ss.ActiveWindowX1:ss.ActiveWindowX2].copy()
		cv2.imshow("image", ss.imageActive)
		print "left"
	elif key == 3:
		ss.ActiveWindowX1 = ss.ActiveWindowX1 + ss.Params_WindowSizeW
		ss.ActiveWindowX2 = ss.ActiveWindowX2 + ss.Params_WindowSizeW
		ss.imageActive = ss.image[(ss.ActiveWindowY1):(ss.ActiveWindowY2), ss.ActiveWindowX1:ss.ActiveWindowX2].copy()
		cv2.imshow("image", ss.imageActive)
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
	roi = ss.imageClone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
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


