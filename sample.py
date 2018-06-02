import tensorflow as tf
x=tf.constant([[1,2,3,4],
                [7,8,9,10]])
y=tf.reshape(x, [2,-1,2])
with tf.Session() as sess:
    print(x.eval())
    print(y.eval())
    print(x.shape)