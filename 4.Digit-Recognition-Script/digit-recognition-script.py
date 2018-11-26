# Source code adapted from:
# - https://www.digitalocean.com/community/tutorials/how-to-build-a-neural-network-to-recognize-handwritten-digits-with-tensorflow
import tensorflow as tf
import numpy as np 
import PIL
# from PIL import Image

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True) # y labels are oh-encoded

# Find out size of the dataset
n_train = mnist.train.num_examples           # 55,000
n_validation = mnist.validation.num_examples # 5000
n_test = mnist.test.num_examples             # 10,000

# Store the no. of units each layer
n_input = 784                               # input layer (28x28 pixels)
n_hidden1 = 512                             # 1st hidden layer
n_hidden2 = 256                             # 2nd hidden layer
n_hidden3 = 128                             # 3rd hidden layer
n_output = 10                               # output layer (0-9 digits)

# Hyperparameters remain constant
learning_rate = 1e-4
n_iterations = 1000
batch_size = 128
dropout = 0.5

# Defining 3 tensors as placeholders
X = tf.placeholder("float", [None, n_input])
Y = tf.placeholder("float", [None, n_output])
keep_prob = tf.placeholder(tf.float32) 

# 
weights = {
    'w1': tf.Variable(tf.truncated_normal([n_input, n_hidden1], stddev=0.1)),
    'w2': tf.Variable(tf.truncated_normal([n_hidden1, n_hidden2], stddev=0.1)),
    'w3': tf.Variable(tf.truncated_normal([n_hidden2, n_hidden3], stddev=0.1)),
    'out': tf.Variable(tf.truncated_normal([n_hidden3, n_output], stddev=0.1)),
}

# Constant values are used to ensure 
# the tensors activate in the initial stage
biases = {
    'b1': tf.Variable(tf.constant(0.1, shape=[n_hidden1])),
    'b2': tf.Variable(tf.constant(0.1, shape=[n_hidden2])),
    'b3': tf.Variable(tf.constant(0.1, shape=[n_hidden3])),
    'out': tf.Variable(tf.constant(0.1, shape=[n_output]))
}

# Set up layers of the network
layer_1 = tf.add(tf.matmul(X, weights['w1']), biases['b1'])
layer_2 = tf.add(tf.matmul(layer_1, weights['w2']), biases['b2'])
layer_3 = tf.add(tf.matmul(layer_2, weights['w3']), biases['b3'])
layer_drop = tf.nn.dropout(layer_3, keep_prob)
output_layer = tf.matmul(layer_3, weights['out']) + biases['out']


# Using the Adam optimizer 
# gradient descend optimization algorithm
# to find the local minimum of a function
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=Y, logits=output_layer))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

# Define the method of evaluating the accuracy
correct_pred = tf.equal(tf.argmax(output_layer, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# Feed the network with training examples
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# Help to reduce loss as learning progresses
for i in range(n_iterations):
    batch_x, batch_y = mnist.train.next_batch(batch_size)
    sess.run(train_step, feed_dict={X: batch_x, Y: batch_y, keep_prob:dropout})

    # print loss and accuracy (per minibatch)
    if i%100==0:
        minibatch_loss, minibatch_accuracy = sess.run([cross_entropy, accuracy], feed_dict={X: batch_x, Y: batch_y, keep_prob:1.0})
        print("Iteration", str(i), "\t| Loss =", str(minibatch_loss), "\t| Accuracy =", str(minibatch_accuracy))


# Run session on MNIST test images
test_accuracy = sess.run(accuracy, feed_dict={X: mnist.test.images, Y: mnist.test.labels, keep_prob:1.0})
print("\nAccuracy on test set:", test_accuracy)

# Resize the image from the non-resized
# folder to a 28x28 pixel image and
# save it to a new folder
# _nonresized_img = PIL.Image.open("numbers/non_resized/number9.png")
# _nonresized_img = _nonresized_img.resize((28, 28), PIL.Image.ANTIALIAS)
# _nonresized_img.save("numbers/resized/resizenumber9.png")

# Load the test image of the handwritten digit
# saved as a 28x28 pixel image
_resized_img = np.invert(PIL.Image.open("numbers/resized/resizenumber6.png").convert('L')).ravel()

# Feeding the image loaded for testing
prediction = sess.run(tf.argmax(output_layer,1), feed_dict={X: [_resized_img]})
# img_accuracy = sess.run(accuracy, feed_dict={X: _resized_img, Y: _resized_img, keep_prob:1.0})
print ("Prediction for test image:", np.squeeze(prediction))
# print ("nAccuracy on handwritten image:", img_accuracy)