import tensorflow as tf

tf.compat.v1.disable_eager_execution()

a = tf.constant(2)
b = tf.constant(3) #define tensor flow constnats

add_op = tf.add(a, b) # define addition tf operator


with tf.compat.v1.Session() as sess: #start tensorflow session

    result = sess.run(add_op)

    print("Result:", result) # 2 + 3 == 5