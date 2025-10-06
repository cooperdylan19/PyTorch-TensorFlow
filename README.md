TensorFlow and Keras: Deploying custom models

**Training Course Used**: https://www.youtube.com/watch?v=BVqj1R71508


### CHAPTER 1: Introduction

**Script 1**: HelloTensorFlow

A simple TensorFlow computation. We first disables eager execution so that TensorFlow builds a static computational graph instead of executing operations immediately, this was done as my very old laptop seems to give errors when using the current TensorFlow update. A constant tensor containing the string “Hello, TensorFlow!” is then defined, and a session is created to run the graph. Within the session, the tensor is evaluated and its value retrieved. Finally, the result is printed showing “Hello, TensorFlow!” in the console.

**Script 2**: WorkingWithTensors

A placeholder *x* is created to act as a variable input that will receive values later when the graph is run. The operation square_op is defined to compute the square of each element in *x*. Inside a session, the graph is executed using sess.run, and actual input values [1, 2, 3] are supplied through a feed_dict. TensorFlow then computes and returns the squared results [1, 4, 9], which are printed to the console.

**Script 3**: TFOperations

Two constant tensors a and b are defined with the values 2 and 3. An addition operation add_op is then created using TensorFlow’s built-in tf.add() function, which symbolically represents the sum of the two tensors within the computation graph. A TensorFlow session is opened to execute this graph, and sess.run(add_op) evaluates the operation, returning the result of 5.

**Script 4**: TFKeras

This script defines and compiles a simple feedforward neural network using Keras, TensorFlow’s high-level deep learning API. It creates a Sequential model - meaning layers are stacked linearly - starting with an input layer expecting 784 features. The first hidden layer has 64 neurons with a ReLU activation function, introducing non-linearity, and the output layer has 10 neurons with a softmax activation, producing a probability distribution over 10 possible classes. The model is then compiled using the Adam optimizer for efficient gradient-based learning, sparse categorical cross-entropy as the loss function (suitable for integer class labels), and accuracy as the evaluation metric during training and testing.



### CHAPTER 2: Tensors and Operations

