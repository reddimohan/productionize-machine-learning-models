import os
import yaml

import tensorflow as tf
from keras.models import load_model


def init():
    """
    create global variables, so that you can load this variable inside api/module file
    """
    global classifier
    global graph

    # One time Model Loading to global variable, so that we dont have to load them again
    classifier = load_model('models/cat_dog_clf_model.h5')

    graph = tf.get_default_graph()
