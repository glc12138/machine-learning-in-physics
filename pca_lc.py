import numpy as np
#import matplotlib.pyplot as plt
#from sklearn.decomposition import PCA
import numpy as np
import tensorflow as tf
import sys

def normalize(X):
    means = np.mean(X, axis=0)
    tmp = np.subtract(X, means)
    return tmp, means


def pca_lca(k1):
    n_components = 3
    
    Xn, means = normalize(k1)

    xtf = tf.placeholder(tf.float32, shape=[k1.shape[0], k1.shape[1]])
    s, u, v = tf.svd(xtf)
    ucut = tf.slice(u, [0, 0], [u.shape[0], n_components])
    s = tf.diag(s)
    scut = tf.slice(s, [0, 0], [n_components,s.shape[1]])
    R = tf.matmul(ucut, scut)
    with tf.Session() as sess:
            Rn = sess.run(R, feed_dict = {
                    xtf: Xn
#                    xtf: k1
                })

##                return Rn[:,:2]
    return Rn
