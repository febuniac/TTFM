#imports
#definicoes
#classes
#import ttmllib as tt
import TTML_Lib
from TTML_Lib import *



cts = None
cts_banco = None

#Loop for the working of the program	
while True:
	x= raw_input (':')
	print(x)
	if x =='carregarede':
		pcarrega_rede()
		#tt.pcarregarede()
	if x =='salvarede':
		if cts is not None:
			filename= input ('Enter the name of the file that will save your network:')
			cts.salva_rede(filename)
	if x =='criaredepadrao':
		if cts is None:
			cts = CTS()
			cts.cria_rede_padrao()
	#if x =='criarede':
		#pcria_rede_padrao()
	if x =='treinarede':
		if cts is not None:
			cts.treina_rede()
	if x =='imgvetor':
		pimage_to_array()	
	if x =='mostraimagem':
		pimage_show()
	if x =='mostranumero':
		pshow_correct_number()


	if x =='criabanco':
		if cts_banco is None:
			cts_banco = CTS_banco()
			banco=cts_banco.cria_banco()
	if x =='salvabanco':
		if cts_banco is not None:
			databasename = raw_input("Name your database:")
			cts_banco.salva_banco(databasename)
	if x =='insereimagembanco':
		if cts_banco is not None:
			cts_banco.insere_imagem_banco(banco)
			print(banco)
	if x =='carregabanco':
		pcarrega_banco()
		#print(xdatabasename)
	if x =='apagaimagembanco':
		if cts_banco is not None:
			print(cts_banco.size())
			indice = input("Index you want to delete:")
			cts_banco.apaga_imagem_banco(indice)
	if x=='mostraimagembanco':
		pshow_correct_number()




#def pcarregarede():
	#x = raw_input('nome da rede')
	#y = raw_input('nome da rede b')
	#z = raw_input('nome da rede c')
	#carregarede(x,y,z)

#def carregarede(x,y,z):
	#print('aaaa' +x+y+z)

#while True:
#	x= raw_input (':')
#	print(x)
#	if x =='carregarede':
	#	pcarregarede()
		#tt.pcarregarede()


