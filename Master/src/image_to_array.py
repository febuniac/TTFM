import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

r = input('Enter the name of the image you want: ')

def image_to_array(r):
	img=mpimg.imread(r)
	#imgplot = plt.imshow(img) #to transform again into image
	#plt.show() #show the image
	print(img)
image_to_array(r)





#img.shape
#http://matplotlib.org/users/image_tutorial.html