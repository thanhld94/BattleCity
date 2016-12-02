import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# preparing training and test data
import numpy as np
from numpy import genfromtxt

# each state of the game is represent as a vector of 18 features
# and this will be the size of the input vector
numberOfFeatures = 18
# 5 actions: up/down/left/right/shoot
numberOfActions = 5
# neural network model statistic
nodesLayer1 = 500
nodesLayer2 = 500
nodesLayer3 = 500


# Setting up the model
# creating the model for the neural network
# 3 hidden layer with an output layer with each node represent a possible action
# including move up/down/left/right and shoot
def neural_network_model(data):
  hidden_1_layer = {'weights':tf.Variable(tf.random_normal([numberOfFeatures, nodesLayer1])), 
                    'biases':tf.Variable(tf.random_normal([nodesLayer1]))}
  hidden_2_layer = {'weights':tf.Variable(tf.random_normal([nodesLayer1, nodesLayer2])), 
                      'biases':tf.Variable(tf.random_normal([nodesLayer2]))}
  hidden_3_layer = {'weights':tf.Variable(tf.random_normal([nodesLayer2, nodesLayer3])), 
                      'biases':tf.Variable(tf.random_normal([nodesLayer3]))}
  output_layer = {'weights':tf.Variable(tf.random_normal([nodesLayer3, numberOfActions])), 
                    'biases':tf.Variable(tf.random_normal([numberOfActions])),}
  l1 = tf.add(tf.matmul(data,hidden_1_layer['weights']), hidden_1_layer['biases'])
  l1 = tf.nn.relu(l1)
  l2 = tf.add(tf.matmul(l1,hidden_2_layer['weights']), hidden_2_layer['biases'])
  l2 = tf.nn.relu(l2)
  l3 = tf.add(tf.matmul(l2,hidden_3_layer['weights']), hidden_3_layer['biases'])
  l3 = tf.nn.relu(l3)
  output = tf.matmul(l3,output_layer['weights']) + output_layer['biases']
  return output

class DeepNet:
  
  def __init__(self, dataInFile, dataOutFile):
    self.train_in = []
    self.train_out = []
    self.test_in = []
    self.test_out = []
    self.loadDataFromFiles(dataInFile, dataOutFile)
    self.setupVariables()
    self.model = neural_network_model(self.x)
    self.sess = tf.Session()
    self.sess.run(tf.initialize_all_variables())

  def loadDataFromFiles(self, datain, dataout):
    # load data from files
    data_in = genfromtxt(datain, delimiter=' ', dtype='int32')
    raw_out = genfromtxt(dataout, delimiter=' ', dtype='int32')
    data_out = []
    # reformating the output
    for i in range(len(raw_out)):
      temp = [0,0,0,0,0]
      temp[raw_out[i]] = 1;
      data_out.append(temp)
    # separate in and out data
    self.train_in = data_in[:9000]
    self.train_out = data_out[:9000]
    self.test_in = data_in[9001:]
    self.test_out = data_out[9001:]


  def setupVariables(self):
    # placehodlers for data
    self.x = tf.placeholder('float', [None, numberOfFeatures])
    self.y_ = tf.placeholder('float')

  # Training the model
  def train(self, numberOfTrainingRecords):
    # Setting up
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(self.model, self.y_))
    optimizer = tf.train.AdamOptimizer().minimize(cost)
    with tf.Session() as sess:
      sess.run(tf.initialize_all_variables())
      # Iterate through each record in the training data
      for idx in range(min(len(self.train_in), numberOfTrainingRecords)):
        # Setting up the record and expected vector
        record = np.reshape(self.train_in[idx], (1, numberOfFeatures))
        expected = []
        expected.append(self.train_out[idx])
        # Training
        _, epoch_loss = sess.run([optimizer, cost], feed_dict={self.x: record, self.y_: expected})
      # Evaluating the agent
      correct_prediction = tf.equal(tf.argmax(self.model, 1), tf.argmax(self.y_, 1))
      accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))
      print('Accuracy:', accuracy.eval({self.x: self.test_in, self.y_:self.test_out}))

  # Give prediction to a state
  def predict(self, record):
    data = []
    data.append(record)
    evaluation = self.sess.run(self.model, feed_dict={self.x: data})[0]
    # chosing the value with the highest value
    answer = 0
    for i in range(len(evaluation)):
      if evaluation[i] > evaluation[answer]:
        answer = i
    return answer
    
# Example
#
#  myNN = DeepNet("../training_data/sorted_data.in", "../training_data/sorted_data.out")
#
#  myNN.train(10000)
#  print(myNN.predict([0, 0, 0, 300, 4, 300, 1, 300, 6, 300, 6, 0, 0, 0, 0, 0, 1, 1]))
#
#
