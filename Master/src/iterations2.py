import network3
from network3 import Network
from network3 import ConvPoolLayer, FullyConnectedLayer, SoftmaxLayer
from network3 import ReLU
class CTS:
	def __init__(self):
		self.mini_batch_size = 10
		self.net_name = Network([
		ConvPoolLayer(image_shape=(self.mini_batch_size, 1, 28, 28), 
		              filter_shape=(20, 1, 5, 5), 
		              poolsize=(2, 2), 
		              activation_fn=ReLU),
		ConvPoolLayer(image_shape=(self.mini_batch_size, 20, 12, 12), 
		              filter_shape=(40, 20, 5, 5), 
		              poolsize=(2, 2), 
		              activation_fn=ReLU),
		FullyConnectedLayer(
		    n_in=40*4*4, n_out=1000, activation_fn=ReLU, p_dropout=0.5),
		FullyConnectedLayer(
		    n_in=1000, n_out=1000, activation_fn=ReLU, p_dropout=0.5),
		SoftmaxLayer(n_in=1000, n_out=10, p_dropout=0.5)], 
		self.mini_batch_size)
	

	def train(self):
		#mini_batch_size = 10
		#net_name = Network([FullyConnectedLayer(n_in=784, n_out=100),SoftmaxLayer(n_in=100, n_out=10)], mini_batch_size)
		training_data, validation_data, test_data = network3.load_data_shared()
		expanded_training_data, _, _ = network3.load_data_shared("../data/mnist_expanded.pkl.gz")
		self.net_name.SGD(expanded_training_data, 1, self.mini_batch_size, 0.03, 
	    validation_data, test_data)
		#net_name.save(filename)
	def save(self,filename):
		self.net_name.save(filename)
	
	def load (self,filename):
		new_net_name = network3.load(filename)


if __name__=="__main__":
	filename= input ('Enter the name of the file that will save your network:')
	cts =CTS()
	cts.train()
	cts.save(filename)
	x= input ('number of iterations:')
	while x>0:
		cts.load(filename)
		cts.train()
		cts.save(filename)
		x-=1
		if x==0:
			break
