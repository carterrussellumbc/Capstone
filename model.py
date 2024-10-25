import pathlib
import numpy as np
import tensorflow as tf


class ImageClassifier:

    def __init__(self):
        self.batch_size = 32
        self.img_height = 400
        self.img_width = 400
        self.product_item_data_dir = pathlib.Path("C:\\Users\\Carter\\git\\Capstone\\data")

    def train_model(self):
        train_ds = tf.keras.utils.image_dataset_from_directory(
          self.product_item_data_dir,
          validation_split=0.2,
          subset="training",
          seed=123,
          image_size=(self.img_height, self.img_width),
          batch_size=self.batch_size)

        val_ds = tf.keras.utils.image_dataset_from_directory(
          self.product_item_data_dir,
          validation_split=0.2,
          subset="validation",
          seed=123,
          image_size=(self.img_height, self.img_width),
          batch_size=self.batch_size)

        num_classes = 3

        model = tf.keras.Sequential([
          tf.keras.layers.Rescaling(1./255),
          tf.keras.layers.Conv2D(32, 3, activation='relu'),
          tf.keras.layers.MaxPooling2D(),
          tf.keras.layers.Conv2D(32, 3, activation='relu'),
          tf.keras.layers.MaxPooling2D(),
          tf.keras.layers.Conv2D(32, 3, activation='relu'),
          tf.keras.layers.MaxPooling2D(),
          tf.keras.layers.Flatten(),
          tf.keras.layers.Dense(128, activation='relu'),
          tf.keras.layers.Dense(num_classes)
        ])

        model.compile(
          optimizer='adam',
          loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
          metrics=['accuracy'])

        model.fit(
          train_ds,
          validation_data=val_ds,
          epochs=5
        )

        model.save('product_classifier.keras')
