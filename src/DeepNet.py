import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# generating numpy data
import numpy as np
from numpy import genfromtxt
my_data = genfromtxt('../training_data/sorted_data.csv', delimiter=',', dtype='int32')

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

# Training the model
def train_neural_network(prediction):
  # Setting up
  cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(prediction,y) )
  optimizer = tf.train.AdamOptimizer().minimize(cost)
  with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    # iterate through each record in the training data
    for idx in range(1000):
      # setting up the record and expected vector
      record = np.reshape(np.array(my_data[idx][:numberOfFeatures]), (1, numberOfFeatures))
      expected = [[0,0,0,0,0]]
      expected[0][my_data[idx][numberOfFeatures] - 1] = 1
      # training
      _, epoch_loss = sess.run([optimizer, cost], feed_dict={x: record, y: expected})
      #print('Record', idx, 'completed out of', len(my_data), 'loss:', epoch_loss)

model = neural_network_model(x)
train_neural_network(model)
