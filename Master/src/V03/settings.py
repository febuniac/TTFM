# settings.py
image = []
imageClone = []
imageActive = []


GRede = []
GRedePointer = 0
GBDI = []
GBDIPointer = 0
GPoints = []
GPointsPointer = 0
Points = []

CurrentMode= ""

BDIC001 = []
BDIB001 = []
BDIG001 = []
BDIR001 = []
BDIM001 = []

cBDIC001 = "BDIC001.pkl"
cBDIB001 = "BDIB001.pkl"
cBDIG001 = "BDIG001.pkl"
cBDIR001 = "BDIR001.pkl"
cBDIM001 = "BDIM001.pkl"

imagelocation = "/Users/mauricioalouan/Dropbox/MLAgro/V03/Area"
imagename = "Area.jpg"

## Haar Cascade
cascLoaded = 0
cascPath = "/Users/mauricioalouan/Dropbox/MLAgro/V03/haar/laranja20-01.xml"

## Points
Point_Shp = 's'	# for square, c)ircle
Point_Rad = 80
Point_Lay = 0

Lay_col=[(0, 255, 0),(255, 0, 0),(0, 0, 255),(255, 255, 0),
		(0, 255, 255),(255, 0, 255),(0, 125, 125),(125, 125, 0),
		(125, 0, 125),(0, 125, 0)]

Params_ScreenRes = (1280, 720)
Params_WindowSizeW = Params_ScreenRes[0]
Params_WindowSizeH = Params_ScreenRes[1]
Params_FileToSavePoints = "Points.json"
Params_FileToLoadPoints = Params_FileToSavePoints
Params_FileToLoadPoints5p3 = "Points5p3.json"

ActiveWindowX1 = 1
ActiveWindowY1 = 1
ActiveWindowX2 = Params_WindowSizeW
ActiveWindowY2 = Params_WindowSizeH

GlobalImgWriterCounter = 50

## To Exclude:
Params_HSquareX = 80
Params_HSquareY = 80
