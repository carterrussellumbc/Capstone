from mongo import Mongo
import tensorflow as tf
import pandas as pd
import datetime
import requests
import pathlib
import polars as pl
from PIL import Image
import numpy as np


class Helpers:

    def __init__(self):
        self.mongo = Mongo()

    def constructDataFrame(self, product_name_list):
        data = []
        base_url = "https://images.openfoodfacts.org/images/products/"
        for itemName in product_name_list:
            product, product_name = self.mongo.getProduct(itemName)
            for itemDoc in product:
                code = itemDoc['code']
                if len(code) == 13:
                    constructed_code = f"{code[:3]}/{code[3:6]}/{code[6:9]}/{code[9:]}/1.jpg"
                    url = base_url + constructed_code
                    temp_list = [url, product_name]
                    data.append(temp_list)
        df = pl.DataFrame(data, schema=["image_url", "classification"], orient="row")
        return df

    def writeToCSV(self, df):
        df.write_csv(f"C:\\Users\\Carter\\Downloads\\{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}_capstone.csv", separator=",")

    def process_path(filepath):
        label = tf.strings.split(filepath, os.sep)[-2]
        return tf.io.read_file(filepath), label
    def download_images(self, filepath):
        df = pd.read_csv(filepath)
        image_num = 0
        for index, row in df.iterrows():
            image_url = row[0]
            classification = row[1]
            image = requests.get(image_url)
            if image.status_code == 404:  # Filter out bad requests
                continue
            pathlib.Path(f"C:\\Users\\Carter\\git\\Capstone\\data\\{classification}").mkdir(parents=True, exist_ok=True)
            with open(
                    f"C:\\Users\\Carter\\git\\Capstone\\data\\{classification}\\{classification}_image_{image_num}.jpg",
                    "wb") as handler:
                handler.write(image.content)
                image_num += 1

    def classify_product(self, classes, filepath_to_image):
        image = Image.open(filepath_to_image)
        image_dims = (400, 400)
        image = image.resize(image_dims)
        image = tf.convert_to_tensor(image)
        image = (np.expand_dims(image, 0))
        model = tf.keras.models.load_model('product_classifier.keras')
        single_image_prediction = model.predict(image)
        class_pos = np.argmax(single_image_prediction[0])
        print(classes[class_pos])

