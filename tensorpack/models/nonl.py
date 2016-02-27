#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# File: nonl.py
# Author: Yuxin Wu <ppwwyyxx@gmail.com>

import tensorflow as tf
from copy import copy

from ._common import *

__all__ = ['Maxout', 'prelu']

@layer_register()
def Maxout(x, num_unit):
    input_shape = x.get_shape().as_list()
    assert len(input_shape) == 4
    ch = input_shape[3]
    assert ch % num_unit == 0
    x = tf.reshape(x, [-1, input_shape[1], input_shape[2], ch / 3, 3])
    return tf.reduce_max(x, 4, name='output')

def PReLU(x, init=tf.constant_initializer(0.001)):
    alpha = tf.get_variable('alpha', [], initializer=init)
    return ((1 + alpha) * x + (1 - alpha) * tf.abs(x)) * 0.5
