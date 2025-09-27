import tensorflow as tf

tf.compat.v1.disable_eager_execution()

# check version
#print("TensorFlow version: ", tf.__version__) # 2.16.2

tensor = tf.constant("Hello, TensorFlow!")

with tf.compat.v1.Session() as sess:

    result = sess.run(tensor)

    print(result.decode())

