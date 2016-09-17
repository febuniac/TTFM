import mnist_loader 
training_data, validation_data, test_data = mnist_loader.load_data_wrapper() 
import json
import random
import sys

# Third-party libraries
import numpy as np
import network2
from network2 import Network


net = network2.Network([784, 100, 10], cost=network2.CrossEntropyCost)
net.large_weight_initializer()
net.SGD(training_data, 1, 10, 0.5, lmbda=5.0,evaluation_data=validation_data,monitor_evaluation_accuracy=True)
net.save(filename="nouggx")

