#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Esta biblioteca envolve todas as funções disponíveis, todos os imports necessários, todas as funções de prompt

#### Libraries
# Standard library
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib	
import numpy as np
import network3
import numpy as np
import mnist_loader 
import scipy.misc as smp

# Third-party libraries
from network3 import Network
from network3 import ConvPoolLayer, FullyConnectedLayer, SoftmaxLayer
from scipy.misc import imsave
from network3 import ReLU
from six.moves import cPickle
training_data, validation_data, test_data = mnist_loader.load_data_wrapper() 


#functions(funcional)_______ REDE

def image_to_array(img_name):

	img=mpimg.imread(img_name)
	#imgplot = plt.imshow(img) #to transform again into image
	#plt.show() #show the image
	print(img)
		

def image_show(r):
# escolher o numero da imagem desejado
	a = training_data[r][0] 
	m = np.asmatrix(a) #transformar a matriz
	#print(m)
	K=np.zeros((28,28),dtype=np.uint8)
	for x in range (784):#tamanho de a
	    K[x//28,x%28]=m[x]*255 #// divisao de inteiros    #% resto da divisao
	    #255=256 niveis de cinza (todos os 1 são 255) -- 1 é muito baixo e considerado praticamente preto.
	    #// linha
		#% coluna
		#pegamos cada linha de m e colocamos como uma coluna.
	img = smp.toimage(K)# Create a PIL image
	img.show() # View in default viewer
	#plt.savefig('myfig')
	smp.imsave(str(r) + '.png', img)#saves the image
	

def show_correct_number(num):
# escolher o numero da imagem desejado
	a = training_data[num][1]
	i=0
	while i < len(a):
		if a[i][0]==1:
			return i
		i=i+1

def carrega_rede(filename):
	new_net_name = network3.load(filename)
	#carrega_rede(filename)
#def salva_rede(net_name):
	#net_name.save(filename)


class CTS:
	def cria_rede_padrao(self):
		self.mini_batch_size = 10
		self.net_name = Network([FullyConnectedLayer(n_in=784, n_out=100),SoftmaxLayer(n_in=100, n_out=10)], self.mini_batch_size)
		
	def treina_rede(self):
		self.epochs = input("Number of Epochs:")
		#mini_batch_size = 10
		#net_name = Network([FullyConnectedLayer(n_in=784, n_out=100),SoftmaxLayer(n_in=100, n_out=10)], mini_batch_size)
		training_data, validation_data, test_data = network3.load_data_shared()
		self.net_name.SGD(training_data, self.epochs, self.mini_batch_size, 0.1, validation_data, test_data)
		#net_name.save(filename)
	def salva_rede(self,filename):
		self.net_name.save(filename)




#functions(funcional)_______ DATABASE
class CTS_banco:

	def cria_banco(self):
		self.banco = []
		print(self.banco)
	def insere_imagem_banco(self,banco,tipo):
		self.rimage= raw_input("Name of the image:")
		self.mat = matplotlib.image.imread(self.rimage)
		self.pixels=np.zeros((784,1),dtype=np.uint8)
		for x in range (28):#tamanho de a
			for y in range (28):#tamanho de a
				self.pixels[y+x*28]=self.mat[x][y]*255
				#print(self.mat[x][y])
				#print(self.pixels[y+x*28])

		self.discover=np.zeros((10,1))


		if tipo ==0:
			self.discover[0, 0]=1
		if tipo ==1:
			self.discover[1, 0]=1
		if tipo ==2:
			self.discover[2, 0]=1
		if tipo ==3:
			self.discover[3, 0]=1
		if tipo ==4:
			self.discover[4, 0]=1
		if tipo ==5:
			self.discover[5, 0]=1
		if tipo ==6:
			self.discover[6, 0]=1
		if tipo ==7:
			self.discover[7, 0]=1
		if tipo ==8:
			self.discover[8, 0]=1
		if tipo ==9:
			self.discover[9, 0]=1
		else:
			print("Tree out of range")	
		self.cmplist=[self.pixels,self.discover]

		img = smp.toimage(self.mat)# Create a PIL image
		img.show()
		#return self.banco,self.cmplist
		self.banco.append(self.cmplist)
		print("banco=", self.banco)

	def salva_banco(self,databasename):
		#databasename = raw_input("Name your database:")
		opens = open(databasename, 'wb')
		cPickle.dump(self.banco,opens, protocol=cPickle.HIGHEST_PROTOCOL)
		opens.close()
	def apaga_imagem_banco(self,indice):
		#imagem = raw_input("Image you want to delete:")
		del self.banco[indice]

	def size(self):
		return(len(self.banco))

	

def carrega_banco(databasename):
	loads = open(databasename, 'rb')
	temp =cPickle.load(loads)#temp variavel temporaria
	loads.close()
	return temp
	
	

def mostra_imagem_banco(images):
	b = banco[images][0] 
	n = np.asmatrix(a) #transformar a matriz
	#print(m)
	P=np.zeros((28,28),dtype=np.uint8)
	for x in range (784):#tamanho de a
	    P[x//28,x%28]=n[x]*255 #// divisao de inteiros    #% resto da divisao
	    #255=256 niveis de cinza (todos os 1 são 255) -- 1 é muito baixo e considerado praticamente preto.
	    #// linha
		#% coluna
		#pegamos cada linha de m e colocamos como uma coluna.
	img = smp.toimage(P)# Create a PIL image
	img.show()

def reclassifica_imagem_banco():
	pass


#Functions of the program______REDE
def pimage_to_array():
	img_name = input('enter the name of the image:')
	image_to_array(img_name)


def pimage_show():
	r = input('Enter the number of the image you want: ')
	image_show(r)


def pshow_correct_number():
	num = raw_input('Enter the number of the image you want: ')
	show_correct_number(num)
	print(show_correct_number(num))

def pcarrega_rede():
	filename= raw_input ('Enter the name of the file that will load your network:')
	carrega_rede(filename)

	



#Functions of the program______DATABASE

def pcarrega_banco():
	databasename= raw_input ('Enter the name of the file that will load your database:')
	carrega_banco(databasename)
	
#def papaga_imagem_banco():
	#apaga_imagem_banco(imagem)

def function():
	pass
def function():
	pass
def function():
	pass


