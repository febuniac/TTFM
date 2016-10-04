lambdaVec = 0.9

P1 = Points[0:5]
P2 = Points[5:10]
P3 = Points[10:15]

P1 = np.asarray(P1)
P2 = np.asarray(P2)
P3 = np.asarray(P3)
	
def DistEVetIL(P1):
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

D1, V1 = DistEVetIL(P1)
D2, V2 = DistEVetIL(P2)
D2, V3 = DistEVetIL(P3)

DF = np.vstack((D1,D2,D3))
DStat = (np.nanmean(DF), np.nanmin(DF), np.nanmax(DF))
VF = np.vstack((V1,V2,v3))
VStat = (np.nanmean(VF), np.nanmin(VF), np.nanmax(VF))

def DistPLs(ponto,linha):
	x3,y3 = ponto
	[[x1,x2],[y1,y2]] = linha
	u = ((x3-x1)*(x2-x1)+(y3-y1)*(y2-y1))/float((x2-x1)**2+(y2-y1)**2)
	d = ((y2-y1)*x3 - (x2-x1)*y3 + x2*y1 -y2*x1)/np.sqrt((x2-x1)**2+(y2-y1)**2)
	x = x1 + u*(x2-x1)
	y = y1 + u*(y2-y1)
	return u,d, (x,y)


## Para passar pra funcao
ponto = P2[1]
linha = P1[1:3]
u,d,p = DistPLs(ponto,linha)

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





