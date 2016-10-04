# https://realpython.com/blog/python/face-recognition-with-python/
# cd /Users/mauricioalouan/Dropbox/MLAgro/V03/
# source activate opencv

from sys import argv
import cv2

# Get user supplied values
#imagePath = argv[1]
#cascPath = sys.argv[2]

imagelocation = "/Users/mauricioalouan/Dropbox/MLAgro/V03/pessoas/"
imagename = "im6.jpg"
cascPath = "/Users/mauricioalouan/Dropbox/MLAgro/V03/haar/haarcascade_frontalface_alt.xml"

#imagelocation = "/Users/mauricioalouan/Dropbox/MLAgro/V03/area/"
#imagename = "area.jpg"
#cascPath = "/Users/mauricioalouan/Dropbox/MLAgro/V03/haar/laranja20-01.xml"


imagePath = imagelocation + "/" + imagename


# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
cv2.imshow("Faces found" ,image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

detector = cv2.CascadeClassifier(cascPath)
faces = detector.detectMultiScale(gray, scaleFactor=1.1,
	minNeighbors=2, minSize=(10, 10), maxSize =(100,100))

#detector = cv2.CascadeClassifier(cascPath)
#faces = detector.detectMultiScale(gray, scaleFactor=1.5,
#	minNeighbors=2, minSize=(120, 120), maxSize =(200,200))


print "Found {0} faces!".format(len(faces))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found" ,image)
cv2.waitKey(0)