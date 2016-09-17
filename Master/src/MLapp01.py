#imports
#definicoes
#classes
#import ttmllib as tt

def pcarregarede():
	x = raw_input('nome da rede')
	y = raw_input('nome da rede b')
	z = raw_input('nome da rede c')
	carregarede(x,y,z)

def carregarede(x,y,z):
	print('aaaa' +x+y+z)

while True:
	x= raw_input (':')
	print(x)
	if x =='carregarede':
		pcarregarede()
		#tt.pcarregarede()


