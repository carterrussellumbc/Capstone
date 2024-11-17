import os
import pathlib
from mongo import Mongo
from helpers import Helpers
from model import ImageClassifier


''' write csv of labelled URLs '''
mongo = Mongo()
helpers = Helpers()
classifier = ImageClassifier()

classifier.train_model(0.15, 96024, "C:\\Users\\Carter\\git\\Capstone\\data", 5, 15, 'product_classifier.keras')

# classes = ['apples', 'bananas', 'avocados', 'red-bell-peppers', 'oranges']
# filepath_to_image = f"{os.getcwd()}\\test_images\\peaches.jpg"
# helpers.classify_product(classes, filepath_to_image, 'product_classifier.keras')

# df = helpers.constructDataFrame(classes)

# filepath = "C:\\Users\\Carter\\Downloads\\20241115-131221_capstone.csv"
# helpers.download_images(filepath)
# product_item_data_dir = pathlib.Path("C:\\Users\\Carter\\git\\Capstone\\data")

''' print list of unique categories in MongoDB '''
# key_list = mongo.getDistinct()
# for i in key_list:
#     if i.isascii():
#         print(i)
