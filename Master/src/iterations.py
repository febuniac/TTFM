import network3
from network3 import Network
from network3 import ConvPoolLayer, FullyConnectedLayer, SoftmaxLayer
class CTS:
	def __init__(self):
		self.mini_batch_size = 10
		self.net_name = Network([FullyConnectedLayer(n_in=784, n_out=100),SoftmaxLayer(n_in=100, n_out=10)], self.mini_batch_size)
	
	def train(self):
		#mini_batch_size = 10
		#net_name = Network([FullyConnectedLayer(n_in=784, n_out=100),SoftmaxLayer(n_in=100, n_out=10)], mini_batch_size)
		training_data, validation_data, test_data = network3.load_data_shared()
		self.net_name.SGD(training_data, 1, self.mini_batch_size, 0.1, validation_data, test_data)
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
	cts.load(filename)
	while x>0:
		cts.train()
		cts.save(filename)
		x-=1
		if x==0:
			break
