import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

r = input('Enter the name of the image you want: ')

def array_to_image(r):
	img=mpimg.imread(r)
	imgplot = plt.imshow(img)
	plt.show()
array_to_image(r)
#img.shape
#http://matplotlib.org/users/image_tutorial.html