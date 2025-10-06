# TensorFlow and Keras: Deploying custom models

**Training Course Used**: https://www.youtube.com/watch?v=BVqj1R71508

<br /> 

<div align="center">
  <h3>🟩 CHAPTER 1: Introduction 🟩</h3>
</div>



<div style="height: 4px; background-color: black; width: 100%; border-radius: 2px;"></div>


🔹 **Script 1**: HelloTensorFlow

A simple TensorFlow computation. We first disables eager execution so that TensorFlow builds a static computational graph instead of executing operations immediately, this was done as my very old laptop seems to give errors when using the current TensorFlow update. A constant tensor containing the string “Hello, TensorFlow!” is then defined, and a session is created to run the graph. Within the session, the tensor is evaluated and its value retrieved. Finally, the result is printed showing “Hello, TensorFlow!” in the console.

🔹 **Script 2**: WorkingWithTensors

A placeholder *x* is created to act as a variable input that will receive values later when the graph is run. The operation square_op is defined to compute the square of each element in *x*. Inside a session, the graph is executed using sess.run, and actual input values [1, 2, 3] are supplied through a feed_dict. TensorFlow then computes and returns the squared results [1, 4, 9], which are printed to the console.

🔹 **Script 3**: TFOperations

Two constant tensors a and b are defined with the values 2 and 3. An addition operation add_op is then created using TensorFlow’s built-in tf.add() function, which symbolically represents the sum of the two tensors within the computation graph. A TensorFlow session is opened to execute this graph, and sess.run(add_op) evaluates the operation, returning the result of 5.

🔹 **Script 4**: TFKeras

This script defines and compiles a simple feedforward neural network using Keras, TensorFlow’s high-level deep learning API. It creates a Sequential model - meaning layers are stacked linearly - starting with an input layer expecting 784 features. The first hidden layer has 64 neurons with a ReLU activation function, introducing non-linearity, and the output layer has 10 neurons with a softmax activation, producing a probability distribution over 10 possible classes. The model is then compiled using the Adam optimizer for efficient gradient-based learning, sparse categorical cross-entropy as the loss function (suitable for integer class labels), and accuracy as the evaluation metric during training and testing.



<div align="center">
  <h3>🟩 CHAPTER 2: Tensors and Operations 🟩</h3>
</div>

🔹 **Script 1**: TFOperations2A

This script demonstrates a wide range of basic TensorFlow operations on tensors. It begins by performing arithmetic operations such as addition, subtraction, element-wise multiplication, and division on two 2 by 2 tensors. It then applies mathematical functions including squaring, square roots, exponentials, and natural logarithms. Next, it performs reduction operations to compute sums, means, and maximum values, followed by matrix operations such as matrix multiplication, transposition, and inversion. The script also showcases tensor indexing and slicing, extracting specific elements and columns, and finally illustrates broadcasting, where a smaller tensor is automatically expanded to match the shape of another during addition.

🔹 **Script 2**: TFOperations2B

This script demonstrates how TensorFlow handles different types of tensors and operations. It first defines constant tensors tensor_a, tensor_b, and constant_tensor, which hold fixed numerical values. 

It then creates a variable tensor initialized with random values drawn from a normal distribution; this variable can be updated, as shown by reassigning it new random values using .assign(). 

The script also defines a tensor x to illustrate computation. TensorFlow computes the element-wise square of x and prints the resulting tensor. Overall, it showcases the distinction between constants (unchangeable), variables (modifiable), and computed tensors in TensorFlow.

🔹 **Script 3**: GraphSessions

Two constant tensors a and b are defined, and a matrix multiplication operation c = tf.matmul(a, b) is added to the computation graph. The line print(tf.compat.v1.get_default_graph().as_graph_def()) displays the graph’s internal structure, showing the defined operations. A TensorBoard writer is then created to save the graph definition to a “logs” directory, allowing it to be visualized in TensorBoard. Finally, a TensorFlow session runs the graph, computes the matrix product, and prints the resulting 2 by 2 matrix.

🔹 **Script 4**: GraphSessions2

This script manually builds and executes a simple TensorFlow computation graph. It first creates a new graph and defines two constant tensors, a and b, with values 2 and 3, along with an addition operation c = tf.add(a, b) inside that graph. Then, a TensorFlow session is opened to execute the graph. Within the session, sess.run(c) evaluates the addition operation, computes the result 5, and prints it to the console.

🔹 **Script 5**: BNNs

🔹 **Script 6**: LossFunctions&Optimizers

🔹 **Script 7**: ActivationFunctions

<div align="center">
  <h3>🟩 CHAPTER 3: Custom models with Keras 🟩</h3>
</div>

<div align="center">
  <h3>🟩 CHAPTER 4: Deploying models 🟩</h3>
</div>

