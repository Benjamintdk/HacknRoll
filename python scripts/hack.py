#this module trains the neural networks needed for the image retrieval system(top 5) and the shoe type.

from tensorflow import keras
from sklearn.metrics import pairwise
from matplotlib import pyplot as plt
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
import numpy as np
import tensorflow as tf
import os
import cv2

class Model:
    def __init__(self, lr, epochs, batch_size):
        self.lr = lr
        self.epochs = epochs
        self.batch_size = batch_size
    def trained_MLP(self, x, y, lr, epochs, batch_size):
        if x.size != 100:
            x = np.reshape(100)
        model = keras.models.Sequential([
        keras.layers.Dense(100, activation='relu'),
        keras.layers.Dense(20, activation='relu'),
        keras.layers.Dense(5, activation='softmax')
        ])
        model.compile(optimizer=keras.optimizers.Adam(self.lr),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
        model.fit(x, y, epochs=self.epochs, batch_size=self.batch_size)
        return model
    def trained_MobNet(self, x, y, lr, epochs, batch_size):
        base_model = keras.applications.mobilenet_v2.MobileNetV2(input_shape=None, alpha=1.0, include_top=False, weights='imagenet', input_tensor=None, pooling=None)
        base_model.trainable = True
        for layer in base_model.layers[:1250]:
          layer.trainable=False
        ## Adds additional layers on top of the pre-trained model for fine-tuning
        model = tf.keras.Sequential([
        base_model,
        tf.keras.layers.Conv2D(32, 3, activation='relu'),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(20, activation='relu'),
        tf.keras.layers.Dense(2, activation='')
        ])

        model.compile(optimizer=tf.keras.optimizers.Adam(0.0005),
                    loss='binary_crossentropy',
                    metrics=['accuracy'])
        model.fit(x, y, epochs=self.epochs, batch_size=self.batch_size)
        return model
