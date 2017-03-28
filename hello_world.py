import tensorflow as tf
Const = tf.constant('Hello, world')
sess = tf.Session()
print(sess.run(Const))