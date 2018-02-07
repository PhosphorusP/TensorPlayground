import tensorflow as tf
a = tf.constant(int(input("input a:")))
b = tf.constant(int(input("input b:")))
result = tf.add(a,b)
sess = tf.Session()
print(sess.run(result))