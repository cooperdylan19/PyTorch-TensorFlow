import tensorflow as tf

tf.compat.v1.disable_eager_execution()

x = tf.compat.v1.placeholder(tf.float32, shape=(None,))

square_op = tf.square(x)

with tf.compat.v1.Session() as sess:

    result = sess.run(square_op, feed_dict={x: [1,2,3]})

    print(result) # 1, 4, 9 