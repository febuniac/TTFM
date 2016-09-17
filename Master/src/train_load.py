import network3
from network3 import Network
from network3 import ConvPoolLayer, FullyConnectedLayer, SoftmaxLayer
#training_data, validation_data, test_data = network3.load_data_shared()

def load (filename):
	new_net_name = network3.load(filename)

if __name__=="__main__":
	filename= input ('Enter the name of the file that will load your network:')
	load(filename)


	

#net_name = Network([FullyConnectedLayer(n_in=784, n_out=100),SoftmaxLayer(n_in=100, n_out=10)], mini_batch_size)
#net_name.SGD(training_data, z, mini_batch_size, n, validation_data, test_data)
#net_name.save(filename ="bloop")