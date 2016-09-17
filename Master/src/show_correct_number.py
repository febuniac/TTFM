import network3
import numpy as np
from network3 import Network
import mnist_loader 
from network3 import ConvPoolLayer, FullyConnectedLayer, SoftmaxLayer
#training_data, validation_data, test_data = network3.load_data_shared()
training_data, validation_data, test_data = mnist_loader.load_data_wrapper() 
import scipy.misc as smp
#import matplotlib.pyplot as plt
from scipy.misc import imsave

r = input('Enter the  number of the image you want: ')
def show_correct_number(r):
# escolher o numero da imagem desejado
	a = training_data[r][1]
	i=0
	while i < len(a):
		if a[i][0]==1:
			return i
		i=i+1
print(show_correct_number(r))


	#while x in range (a):#tamanho de a
		#x-=1
		#if x==1:
			#print position


#testlist = [1,2,3,5,3,1,2,1,6]
#for item in testlist:
    #if item == 1:
        #print position


        #for i in xrange(len(testlist)):
  #if testlist[i] == 1:
    #print i





    #m = np.asmatrix(a)
	#lookingFor = 1
	#i = 0
	#index = 0
	#try:
	 # while i < len(m):
	 #   index = a.index(lookingFor,i)
	 #   i = index + 1
	 #   print index
	#except ValueError: #testlist.index() cannot find lookingFor
	 # pass
