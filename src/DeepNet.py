import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot = True)

# each state of the game is represent as a vector of 18 features
# and this will be the size of the input vector
numberOfFeatures = 18

# 5 actions: up/down/left/right/shoot
numberOfActions = 5

# neural network model statistic
nodesLayer1 = 500
nodesLayer2 = 500
nodesLayer3 = 500

# placehodlers for data
x = tf.placeholder('float', [None, numberOfFeatures])
y = tf.placeholder('float')

# creating the model for the neural network
# 3 hidden layer with an output layer with each node represent a possible action
# including move up/down/left/right and shoot
def neural_network_model(data):
  # Setting up the model
  hidden_1_layer = {'weights':tf.Variable(tf.random_normal([numberOfFeatures, nodesLayer1])), 
                      'biases':tf.Variable(tf.random_normal([nodesLayer1]))}
  hidden_2_layer = {'weights':tf.Variable(tf.random_normal([nodesLayer1, nodesLayer2])), 
                      'biases':tf.Variable(tf.random_normal([nodesLayer2]))}
  hidden_3_layer = {'weights':tf.Variable(tf.random_normal([nodesLayer2, nodesLayer3])), 
                      'biases':tf.Variable(tf.random_normal([nodesLayer3]))}
  output_layer = {'weights':tf.Variable(tf.random_normal([nodesLayer3, numberOfActions])), 
                    'biases':tf.Variable(tf.random_normal([numberOfActions])),}
  # Calculating the output
  l1 = tf.add(tf.matmul(data,hidden_1_layer['weights']), hidden_1_layer['biases'])
  l1 = tf.nn.relu(l1)
  l2 = tf.add(tf.matmul(l1,hidden_2_layer['weights']), hidden_2_layer['biases'])
  l2 = tf.nn.relu(l2)
  l3 = tf.add(tf.matmul(l2,hidden_3_layer['weights']), hidden_3_layer['biases'])
  l3 = tf.nn.relu(l3)
  output = tf.matmul(l3,output_layer['weights']) + output_layer['biases']
  return output

#TODO Processing the input data (convert the csv file to the correct type)
#TODO write the training
