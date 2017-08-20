import numpy as np
import tensorflow as tf
from tensorflow.contrib import layers, rnn


class DaggerNetwork(object):
    def __init__(self, state_dim, action_cnt):
        self.states = tf.placeholder(tf.float32, [None, state_dim])

        actor_h1 = layers.relu(self.states, 4)
        self.action_scores = layers.linear(actor_h1, action_cnt)
        self.action_probs = tf.nn.softmax(self.action_scores,
                                          name='action_probs')

        self.trainable_vars = tf.get_collection(
            tf.GraphKeys.TRAINABLE_VARIABLES, tf.get_variable_scope().name)
