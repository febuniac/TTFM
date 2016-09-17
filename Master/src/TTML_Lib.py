#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Esta biblioteca envolve todas as funções disponíveis, todos os imports necessários, todas as funções de prompt
#### Libraries
# Standard library
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
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
training_data, validation_data, test_data = mnist_loader.load_data_wrapper() 





#functions(funcional)


def image_to_array(img_name):

	img=mpimg.imread(img_name)
	#imgplot = plt.imshow(img) #to transform again into image
	#plt.show() #show the image
	print(img)
	return image_to_array(img_name)
		
	

def pimage_to_array():
	img_name = input('enter the name of the image:')
	image_to_array(img_name)


def image_show(r):
# escolher o numero da imagem desejado
	a = training_data[r][0] 
	m = np.asmatrix(a) #transformar a matriz
	print(m)
	K=np.zeros((28,28),dtype=np.uint8)
	for x in range (784):#tamanho de a
	    K[x//28,x%28]=m[x]*255 #// divisao de inteiros    #% resto da divisao
	    #255=256 niveis de cinza (todos os 1 são 255) -- 1 é muito baixo e considerado praticamente preto.
	    #// linha
		#% coluna
		#pegamos cada linha de m e colocamos como uma coluna.
	img = smp.toimage(O)# Create a PIL image
	img.show() # View in default viewer
	#plt.savefig('myfig')
	smp.imsave(str(r) + '.png', img)#saves the image
	


def pimage_show():
	r = input('Enter the number of the image you want: ')
	image_show(r)

while True:
	x= raw_input (':')
	print(x)
	if x =='carregarede':
		pcarregarede()
		#tt.pcarregarede()
	if x =='imgvetor':
		pimage_to_array()	
	if x=='mostraimagem':
		pimage_show()

def show_correct_number(r):
# escolher o numero da imagem desejado
	a = training_data[r][1]
	i=0
	while i < len(a):
		if a[i][0]==1:
			return i
		i=i+1
print(show_correct_number(r))


class CTS:
	def __init__(self):
		self.mini_batch_size = 10
		self.net_name = Network([FullyConnectedLayer(n_in=784, n_out=100),SoftmaxLayer(n_in=100, n_out=10)], self.mini_batch_size)
	
	def train_net3(self):
		#mini_batch_size = 10
		#net_name = Network([FullyConnectedLayer(n_in=784, n_out=100),SoftmaxLayer(n_in=100, n_out=10)], mini_batch_size)
		training_data, validation_data, test_data = network3.load_data_shared()
		self.net_name.SGD(training_data, 10, self.mini_batch_size, 0.1, validation_data, test_data)
		#net_name.save(filename)
	def save_net3(self,filename):
		self.net_name.save(filename)

if __name__=="__main__":
	filename= input ('Enter the name of the file that will save your network:')
	cts = CTS()
	cts.train_net3()
	cts.save_net3(filename)

