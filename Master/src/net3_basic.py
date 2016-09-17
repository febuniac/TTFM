import network3
from network3 import Network
from network3 import ConvPoolLayer, FullyConnectedLayer, SoftmaxLayer
training_data, validation_data, test_data = network3.load_data_shared()
mini_batch_size = 10
net = Network([FullyConnectedLayer(n_in=784, n_out=100),SoftmaxLayer(n_in=100, n_out=10)], mini_batch_size)
net.SGD(training_data, 10, mini_batch_size, 0.1, validation_data, test_data)
#net.save(filename="nouggxy")
347.728 bytes (348 KB on disk)
31.755.164 bytes (31,8 MB on disk)	
#a single hidden layer, containing 100 hidden neurons. 
#We'll train for 60epochs
#Using a learning rate of n=0.1
#A mini-batch size of 10
#No regularization.
#97.84  percent (best)




#This is the classification accuracy on the test_data, evaluated at
#the training epoch where we get the best classification accuracy on 
#the validation_data. Using the validation data to decide when to evaluate 
#the test accuracy helps avoid overfitting to the test data 

347.773 bytes (348 KB on disk)
31.761.019 bytes (31,8 MB on disk)