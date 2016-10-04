import numpy as np
import argparse
import cv2
import json
import time
import cPickle
import settings as ss
import os

#import network2
#import network3


##############################
def Ajuda():
	print("### Funcoes de Redes: \n \
	CarregaRede   -   CriaRede   -   SalvaRede   -   CriaRedePadrao   -   TreinaRede \n \
	### Funcoes de Banco de Imagens (BDI): \n \
	CarregaBDI  |  CriaBDI  |  SalvaBDI  |  InsereImagemBDI  |  ApagaImagemBDI  |  MostraImagemBDI  |  ReclassificaImagemBDI \n \
	MarcaLinha  |  ArmazenaLinhaBDI  |  GravaImagensdePontos  |  GravaImagensdePontosJPG  |  ProcessaPontos5p3 \
	SetSqSize \
	")

##############################
def ProcessaComandos(c):
	#global ss.GRede, ss.GRedePointer, ss.GBDI, ss.GBDIPointer, ss.GPoints, ss.GPointsPointer
	c = c.lower()
	if c == 'ajuda':
		print(settings.GPointsPointer)
		Ajuda()
	elif c == 'x':
		quit()
	elif c == 'carregarede':
		pCarregaRede()
	elif c == 'criarede':
		pCriaRede()
	elif c == 'salvarede':
		pSalvaRede()
	elif c == 'criaredepadrao':
		pCriaRedePadrao()
	elif c == 'treinarede':
		pTreinaRede()

	elif c == 'carregabdis':
		pCarregaBDIs()
	elif c == 'carregabdi':
		pCarregaBDI()
	elif c == 'criabdi':
		pCriaBDI()
	elif c == 'salvabdis':
		pSalvaBDIs()

	elif c == 'exp':
		image = cv2.cvtColor(ss.imageClone, cv2.COLOR_BGR2GRAY)
		image = cv2.GaussianBlur(image, (5, 5), 0)
		cv2.imshow("Blurred", image)
		canny = cv2.Canny(image, 30, 150)
		cv2.imshow("Canny", canny)
		cv2.waitKey(0)
		#pSalvaBDIs()


	elif c == 'salvabdi':
		pSalvaBDI()

	elif c == 'insereimagembdi':
		pInsereImagemBDI()
	elif c == 'apagaimagembdi':
		pApagaImagemBDI()
	elif c == 'mostraimagembdi':
		pMostraImagemBDI()
	elif c == 'reclassificaimagembdi':
		pReclassificaImagemBDI()

	elif c == 'marcalinha':
		pMarcaLinha()
	elif c == 'armazenalinhabdi':
		pArmazenaLinhaBDI()
	elif c == 'gravaimagensdepontos':
		pGravaImagensdePontos()
	elif c == 'gravaimagensdepontosjpg':
		pGravaImagensdePontosJPG()
		
	elif c == 'processapontos5p3':
		pProcessaPontos5p3()

	elif c == 'setsqsize':
		pSetSqSize()

	elif c == 'nl':
		pNextLayer()
	elif c == 'nextlayer':
		pNextLayer()
	elif c == 'pl':
		pPrevLayer()
	elif c == 'prevlayer':
		pPrevLayer()
	elif c == 'rangedetect':
		pRangeDetect()
	elif c == "chutaproxponto":
		pChutaProxPonto()
	elif c == "achaproxponto":
		pAchaProxPonto()

	elif c == 'teste':
		pTeste()
	else:
		Ajuda()

##############################
def pCarregaRede():
	print("not ready yet")
def pCriaRede():
	print("not ready yet")
def pSalvaRede():
	print("not ready yet")
def pCriaRedePadrao():
	print("not ready yet")
def pTreinaRede():
	print("not ready yet")

def pCarregaBDIs():
	CarregaBDIs()

def pCarregaBDI():
	print("not ready yet")
def pCriaBDI():
	print("Novo BDI")
	return CriaBDI()

def pSalvaBDIs():
	SalvaBDIs()

def pSalvaBDI():
	print("not ready yet")
def pInsereImagemBDI():
	print("not ready yet")
def pApagaImagemBDI():
	print("not ready yet")
def pMostraImagemBDI():
	print("not ready yet")
def pReclassificaImagemBDI():
	print("not ready yet")

def pMarcaLinha():
	print("not ready yet")

def pTeste():
	print(ss.BDIC001)

def pArmazenaLinhaBDI():
	x = ChecaSeNum(raw_input("Tipo de mascara (0-10):"),99)
	if x == 99:
		print("Not a number")
	else:
		pArmazenaLinhaBDI(x)

def pGravaImagensdePontos():
	x = raw_input("Funcao usa pontos salvos em " + ss.Params_FileToLoadPoints + ". Digite OK para continuar")
	if x.lower() == "ok":
		x = raw_input("Funcao usa Bancos de Imagem. Carregue os bancos antes de usar. Digite OK para continuar")
		if x.lower() == "ok":
			GravaImagensdePontos()

def pGravaImagensdePontosJPG():
	x = raw_input("Grava primeira imagem com numero " + str(ss.GlobalImgWriterCounter) + "? Ou digite numero")
	if x.lower() == "ok":
		GravaImagensdePontosJPG(ss.GlobalImgWriterCounter)
	elif ChecaSeNum(x,-1)>0:
		GravaImagensdePontosJPG(int(x))

def pProcessaPontos5p3():
	ProcessaPontos5p3()

def pSetSqSize():
	x = raw_input("Square Size:")
	if ChecaSeNum(x,-1)>0:
		SetSqSize(x)

def pNextLayer():
	NextLayer()

def pPrevLayer():
	PrevLayer()

def pRangeDetect():
	RangeDetect()

def pChutaProxPonto():
	ChutaProxPonto(ss.Points[-2],ss.Points[-1])

def pAchaProxPonto():
	AchaProxPonto(ss.Points[-2],ss.Points[-1])


##############################
def CarregaRede():
	print("not ready yet")
def CriaRede():
	print("not ready yet")
def SalvaRede():
	print("not ready yet")
def CriaRedePadrao():
	print("not ready yet")
def TreinaRede():
	print("not ready yet")

def CarregaBDIs():
	ss.BDIC001 = cPickle.load(open(ss.cBDIC001, "rb"))
	ss.BDIB001 = cPickle.load(open(ss.cBDIB001, "rb"))
	ss.BDIG001 = cPickle.load(open(ss.cBDIG001, "rb"))
	ss.BDIR001 = cPickle.load(open(ss.cBDIR001, "rb"))
	ss.BDIM001 = cPickle.load(open(ss.cBDIM001, "rb"))
	
def CarregaBDI():
	print("not ready yet")
def CriaBDI():
	print("Novo BDI")
	return []

def SalvaBDIs():
	f = open(ss.cBDIC001, 'wb')
	cPickle.dump(ss.BDIC001, f, protocol=cPickle.HIGHEST_PROTOCOL)
	f.close()

	f = open(ss.cBDIB001, 'wb')
	cPickle.dump(ss.BDIB001, f, protocol=cPickle.HIGHEST_PROTOCOL)
	f.close()

	f = open(ss.cBDIG001, 'wb')
	cPickle.dump(ss.BDIG001, f, protocol=cPickle.HIGHEST_PROTOCOL)
	f.close()

	f = open(ss.cBDIR001, 'wb')
	cPickle.dump(ss.BDIR001, f, protocol=cPickle.HIGHEST_PROTOCOL)
	f.close()

	f = open(ss.cBDIM001, 'wb')
	cPickle.dump(ss.BDIM001, f, protocol=cPickle.HIGHEST_PROTOCOL)
	f.close()

def SalvaBDI(n):
	f = open('BDI'+str(n).zfill(3)+'.pkl', 'wb')
	cPickle.dump(ss.GBDI[n], f, protocol=cPickle.HIGHEST_PROTOCOL)
	f.close()
	print("May work")

def InsereImagemBDI(im,classif,n):
	## Nao esta em uso
	c = classificaParaBDI(classif)
	GBDI[GBDIPointer].append(im, c)		

def ApagaImagemBDI():
	print("not ready yet")
def MostraImagemBDI():
	print("not ready yet")
def ReclassificaImagemBDI():
	print("not ready yet")

def MarcaLinha():
	print("not ready yet")

def ArmazenaLinhaBDI():
	pass

def GravaImagensdePontos():
	# 1. Carrega pontos salvos
	print("1. Carrega Pontos salvos")
	Points = loadPointsFromFile(ss.Params_FileToLoadPoints)
	print("2. Para cada ponto, cropa imagem")
	i = 0
	for [x,y] in Points:
		# 2. Para cada ponto, cropa imagem
		ic1 = ss.imageClone[(y-ss.Params_HSquareY):(y+ss.Params_HSquareY),(x-ss.Params_HSquareX):(x+ss.Params_HSquareX)]
		# 3. transforma cada imagem em {cor, r,g,b, c}
		ib1,ig1,ir1 = cv2.split(ic1)
		im1 = cv2.cvtColor(ic1, cv2.COLOR_BGR2GRAY)			
		# 4. Adiciona cada imagem ao BDI apropriado
		c = classificaParaBDI(1)
		ss.BDIC001.append([ic1,c])
		ss.BDIB001.append([ib1,c])
		ss.BDIG001.append([ig1,c])
		ss.BDIR001.append([ir1,c])
		ss.BDIM001.append([im1,c])
		i = i+1
	print(str(i) + " imagens gravadas")

def GravaImagensdePontosJPG(imn):
	# 1. Carrega pontos salvos
	print("1. Carrega Pontos salvos")
	Points = loadPointsFromFile(ss.Params_FileToLoadPoints)
	print("2. Para cada ponto, cropa imagem")
	i = 0
	for [x,y,z1,z2,z3] in Points:
		# 2. Para cada ponto, cropa imagem
		ic1 = ss.imageClone[(y-ss.Params_HSquareY):(y+ss.Params_HSquareY),(x-ss.Params_HSquareX):(x+ss.Params_HSquareX)]
		# 3. transforma cada imagem em {cor, r,g,b, c}
		cv2.imwrite(os.path.join('imgs', 'im' + str(imn+i).zfill(3) + '.jpg'), ic1)		
		i = i+1
	print(str(i) + " imagens gravadas na pasta - imgs")



def ProcessaPontos5p3():
	# 1. Carrega pontos salvos
	print("1. Carrega Pontos salvos")
	Points = loadPointsFromFile(ss.Params_FileToLoadPoints5p3)
	## Calcula Distancias Minimas, Medias e Maximas e Direcao

	P1 = Points[0:5]
	P2 = Points[5:10]
	P3 = Points[10:15]

	P1 = np.asarray(P1)
	P2 = np.asarray(P2)
	P3 = np.asarray(P3)

	D1, V1 = DistEVetIL(P1)
	D2, V2 = DistEVetIL(P2)
	D2, V3 = DistEVetIL(P3)

	DF = np.vstack((D1,D2,D3))
	DStat = (np.nanmean(DF), np.nanmin(DF), np.nanmax(DF))
	VF = np.vstack((V1,V2,V3))
	VStat = (np.nanmean(VF), np.nanmin(VF), np.nanmax(VF))

	Us1,Ds1,Ps1 = DistPL(P2,P1)
	Us2,Ds2,Ps2 = DistPL(P2,P3)


def SetSqSize(x):
	ss.Point_Rad = int(x)

def NextLayer():
	if ss.Point_Lay == 9:
		ss.Point_Lay = 0
	else:
		ss.Point_Lay = ss.Point_Lay + 1

def PrevLayer():
	if ss.Point_Lay == 0:
		ss.Point_Lay = 9
	else:
		ss.Point_Lay = ss.Point_Lay - 1

def RangeDetect():
	r = []
	for p in ss.Points:
		print(p)
		if p[4] > len(r)-1:
			l = len(r)-1
			while (l<p[4]):
				r.append(0)
				print(r)
				l = len(r)-1
			r[p[4]] = RangeDetectPt(p)
		else:
			r[p[4]] = CombineRange(r[p[4]],RangeDetectPt(p))
	saveRange(r,"Range.json")


##############################

def MascaraParaLinha(n):
	if n == 0:
		return(20,120)

##############################

def ChecaSeNum(x,y):
    try: 
        int(x)
        return int(x)
    except ValueError:
        return y

def Distancias(xy1, xy2):
	d0 = np.subtract(xy1[0], xy2[0])
	d1 = np.subtract(xy1[1], xy2[1])
	return np.sqrt(d0**2+d1**2)


def DistEVetIL(P1):		## P1 eh uma lista de pontos (x,y) na mesma linha
	for i in range(5):
		P1z = P1 - P1[i]
		d = np.absolute(np.asarray(range(5))-i)
		d = np.divide(np.sqrt(np.dot(P1z,P1z.T).diagonal()),d)
		if i==0:
			D=d
			v = None
		else:
			D=np.vstack((D,d))
			v=np.divide((P1[i]-P1[i-1]),d[i-1])
			if i==1:
				V=v
			else:
				V=np.vstack((V,v))
	return(D,V)


def DistPLs(ponto,linha):
	x3,y3 = ponto
	[[x1,x2],[y1,y2]] = linha
	u = ((x3-x1)*(x2-x1)+(y3-y1)*(y2-y1))/float((x2-x1)**2+(y2-y1)**2)
	d = ((y2-y1)*x3 - (x2-x1)*y3 + x2*y1 -y2*x1)/np.sqrt((x2-x1)**2+(y2-y1)**2)
	x = x1 + u*(x2-x1)
	y = y1 + u*(y2-y1)
	return u,d, (x,y)


def DistPL(pontos,linhas):
	zp = len(pontos)
	zl = len(linhas)
	for i in range(1,(zp-1)):
		ponto = pontos[i]
		linha = linhas[(i-1):(i+1)]
		u,d,p = DistPLs(ponto,linha)
		if i==1:
			U=u
			D=d
			P=p
		else:
			U=np.vstack((U,u))
			D=np.vstack((D,d))
			P=np.vstack((P,p))
	return U,D,P

def RangeDetectPt(point):
	im = ss.imageClone[(point[0]-point[3]):(point[0]+point[3]),(point[1]-point[3]):(point[1]+point[3])]
	return RangeDetectIm(im)

def RangeDetectIm(im, scala=.90):
	# scala not working
	bl = im[:,:,0].min()
	bu = im[:,:,0].max()
	gl = im[:,:,1].min()
	gu = im[:,:,1].max()
	rl = im[:,:,2].min()
	ru = im[:,:,2].max()
	return ([bl,gl,rl],[bu,gu,ru])

def CombineRange(a,b):
	return ([min(a[0][0],b[0][0]),min(a[0][1],b[0][1]),min(a[0][2],b[0][2])],[max(a[1][0],b[1][0]),max(a[1][1],b[1][1]),max(a[1][2],b[1][2])])


##############################
def savePoints(Points, filename):
	# Saves Points
	data = {"Points": Points}
	f = open(filename, "w")
	json.dump(data, f)
	f.close()

def loadPointsFromFile(filename):
	Points = []
	f = open(filename, "r")
	d = json.load(f)
	#print("##### tt ##### d:")
	#print(d)
	Points = d['Points']
	print("##### tt ##### Points:")
	print(Points)
	f.close()
	return Points

def classificaParaBDI(n):
	c = np.zeros((10,1), dtype=np.int)
	c[n]=1
	return c

def saveRange(Range, filename):
	# Saves Points
	print(Range)
	data = {"Range": Range}
	f = open(filename, "w")
	f.write(repr(Range))
	#json.dump(data, f)
	f.close()

def ChutaProxPonto(p1,p2):
	l = len(p1)
	x1 = p1[0]
	y1 = p1[1]
	x2 = p2[0]
	y2 = p2[1]
	if l == 2:
		p3 = ((x2+(x2-x1)),(y2+(y2-y1)))
	else:
		p3 = ((x2+(x2-x1)),(y2+(y2-y1)),p2[2],p2[3],p2[4])
	print(p1,p2,p3)
	return p3

def AchaProxPonto(p1,p2):
	p3 = ChutaProxPonto(p1,p2)
	print("Chute:")
	print(p3)
	c = AchaCentroPorHC(p3,r=90)
	print("Centro Por HC:")
	print(c)
	(x,y,s,r,l) = p3
	p3 = (x,y,s,r,1)
	(x,y,s,r,l) = c
	c = (x,y,s,r,2)
	AddDrawPoint(p3)
	AddDrawPoint(c)

def AchaCentroPorNN(p1,r):
	x0 = p1[0]-r
	x1 = p1[0]+r
	y0 = p1[1]-r
	y1 = p1[1]+r
	c = np.zeros((2*r+1),(2*r+1))
	for xi in range(x0,(x1+1)):
		for yi in range(y0,(y1+1)):
			c = ClassificaNota(ImagemComCentro(xi,yi,r))
	return p3

def AchaCentroPorHC(pc,r=90):
	xc = pc[0]
	yc = pc[1]
	im = ImagemComCentro(xc,yc,r)
	xoff,yoff = FindWithCascadeFromColorIm(im)
	x=xc+xoff
	y=yc+yoff
	l = len(pc)
	if l == 2:
		p3 = (x,y)
	else:
		p3 = (x,y,pc[2],pc[3],pc[4])
	print(p3)
	return p3

def ImagemComCentro(x,y,r):
	cv2.imshow("HCReg", ss.imageClone[(y-r):(y+r),(x-r):(x+r),:])
	return ss.imageClone[(y-r):(y+r),(x-r):(x+r),:]
	
def LoadCascade():
	# Create the haar cascade
	ss.CascadeDetector = cv2.CascadeClassifier(ss.cascPath)
	ss.cascLoaded = 1

def FindWithCascadeFromColorIm(im):
	f=0
	(h, w) = im.shape[:2]
	if ss.cascLoaded == 0:
		print("Loading Cascade")
		LoadCascade()
	gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	objs = ss.CascadeDetector.detectMultiScale(gray, scaleFactor=1.1,
	minNeighbors=2, minSize=(120, 120), maxSize =(200,200))
	l = len(objs)
	print "Found {0} objs!".format(l)


	if l == 0:
		pass
	if l == 1:
		f=1
		for (x, y, w, h) in objs:
			xc = x+w/2-w
			yc = y+h/2-h
			dc = np.sqrt(xc**2+yc**2)
	if l>1:
		## Acha Ponto Mais Perto Do Centro
		f=1
		dc=1000000
		xc=0
		yc=0
		pts=[]
		for (x, y, w, h) in objs:
			xi = x+w/2-w
			yi = y+h/2-h
			di = np.sqrt(xi**2+yi**2)
			if dc==1000000:
				xc=xi
				yc=yi
				dc=di
			elif di<dc:
				xc=xi
				yc=yi
				dc=di
	print("Melhor Dist C: | x, y")
	print(str(dc) + "   |   " + str(xc) + ", " + str(yc))
	return (xc,yc)

def AddPoint(p):
	ss.Points.append(p)

def DrawPoint(p):
	(x,y,s,r,l) = p
	cv2.rectangle(ss.image, (x-r, y-r), (x+r, y+r), ss.Lay_col[l], 2)
	cv2.rectangle(ss.imageActive, (x-r, y-r), (x+r, y+r), ss.Lay_col[l], 2)
	ss.imageActive = ss.image[ss.ActiveWindowY1:ss.ActiveWindowY2, ss.ActiveWindowX1:ss.ActiveWindowX2]
	cv2.imshow("image", ss.imageActive)

def AddDrawPoint(p):
	AddPoint(p)
	DrawPoint(p)


