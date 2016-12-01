import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# preparing training and test data
import numpy as np
from numpy import genfromtxt

# load data from files
data_in = genfromtxt('../training_data/sorted_data.in', delimiter=' ', dtype='int32')
raw_out = genfromtxt('../training_data/sorted_data.out', delimiter=' ', dtype='int32')

data_out = []
# reformating the output
for i in range(len(raw_out)):
  temp = [0,0,0,0,0]
  temp[raw_out[i]] = 1;
  data_out.append(temp)

# separate in and out data
train_in = data_in[:9000]
train_out = data_out[:9000]
test_in = data_in[9001:]
test_out = data_out[9001:]

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
y_ = tf.placeholder('float')

# Setting up the model
# creating the model for the neural network
# 3 hidden layer with an output layer with each node represent a possible action
# including move up/down/left/right and shoot
hidden_1_layer = {'weights':tf.Variable(tf.random_normal([numberOfFeatures, nodesLayer1])), 
                    'biases':tf.Variable(tf.random_normal([nodesLayer1]))}
hidden_2_layer = {'weights':tf.Variable(tf.random_normal([nodesLayer1, nodesLayer2])), 
                    'biases':tf.Variable(tf.random_normal([nodesLayer2]))}
hidden_3_layer = {'weights':tf.Variable(tf.random_normal([nodesLayer2, nodesLayer3])), 
                    'biases':tf.Variable(tf.random_normal([nodesLayer3]))}
output_layer = {'weights':tf.Variable(tf.random_normal([nodesLayer3, numberOfActions])), 
                  'biases':tf.Variable(tf.random_normal([numberOfActions])),}

# Calculating the output
def neural_network_model(data):
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
  cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(prediction, y_))
  optimizer = tf.train.AdamOptimizer().minimize(cost)
  with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    # Iterate through each record in the training data
    for idx in range(len(train_in)):
      # Setting up the record and expected vector
      record = np.reshape(train_in[idx], (1, numberOfFeatures))
      expected = []
      expected.append(train_out[idx])
      # Training
      _, epoch_loss = sess.run([optimizer, cost], feed_dict={x: record, y_: expected})
    # Evaluating the agent
    correct_prediction = tf.equal(tf.argmax(prediction, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))
    print('Accuracy:', accuracy.eval({x: test_in, y_:test_out}))

model = neural_network_model(x)
train_neural_network(model)
