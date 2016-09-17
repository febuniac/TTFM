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
#filename = input('Enter the name of the image you will save: ')
def image_show(r):
# escolher o numero da imagem desejado
    a = training_data[r][0] 
    m = np.asmatrix(a) #transformar a matriz
    print(m)
    O=np.zeros((28,28),dtype=np.uint8)
    for x in range (784):#tamanho de a
        O[x//28,x%28]=m[x]*255 #// divisao de inteiros    #% resto da divisao
    img = smp.toimage(O)# Create a PIL image
    img.show() # View in default viewer
    #plt.savefig('myfig')
    smp.imsave(str(r) + '.png', img)#saves the image
image_show(r)

#// linha
#% coluna
#pegamos cada linha de m e colocamos como uma coluna.

#http://stackoverflow.com/questions/434583/what-is-the-fastest-way-to-draw-an-image-from-discrete-pixel-values-in-python