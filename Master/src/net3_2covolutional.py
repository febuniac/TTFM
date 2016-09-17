import network3
from network3 import Network
from network3 import ConvPoolLayer, FullyConnectedLayer, SoftmaxLayer
training_data, validation_data, test_data = network3.load_data_shared()
mini_batch_size = 10
net = Network([
        ConvPoolLayer(image_shape=(mini_batch_size, 1, 28, 28), 
                      filter_shape=(20, 1, 5, 5), 
                      poolsize=(2, 2)),
        ConvPoolLayer(image_shape=(mini_batch_size, 20, 12, 12), 
                      filter_shape=(40, 20, 5, 5), 
                      poolsize=(2, 2)),
        FullyConnectedLayer(n_in=40*4*4, n_out=100),
        SoftmaxLayer(n_in=100, n_out=10)], mini_batch_size)
net.SGD(training_data, 60, mini_batch_size, 0.1, 
            validation_data, test_data)


#what does it even mean to apply a second convolutional-pooling layer? 
#In fact, you can think of the second convolutional-pooling layer as having as input 12×12
# "images", whose "pixels" represent the presence (or absence) of particular localized features 
#in the original input image. So you can think of this layer as having as input a version of the 
#original input image. That version is abstracted and condensed, but still has a lot of spatial structure, 
#and so it makes sense to use a second convolutional-pooling layer.




#The output from the previous layer involves 20separate feature maps, and so there are 20×12×12
#inputs to the second convolutional-pooling layer. It's as though we've got 20 separate images input 
#to the convolutional-pooling layer, not a single image, as was the case for the first convolutional-pooling layer.
#How should neurons in the second convolutional-pooling layer respond to these multiple input images? In fact, we'll 
#allow each neuron in this layer to learn from all 20×5×5 input neurons in its local receptive field. More informally:
#the feature detectors in the second convolutional-pooling layer have access to all the features from the previous layer,
#but only within their particular local receptive field