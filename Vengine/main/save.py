import tensorflow as tf

def save(sess, path):
    with sess.graph.as_default():
        saver = tf.train.Saver()
        saver.save(sess, path, meta_graph_suffix='meta', write_meta_graph=True)