import os
from mongo import Mongo
from helpers import Helpers
from model import ImageClassifier


''' write csv of labelled URLs '''
mongo = Mongo()
helpers = Helpers()
classifier = ImageClassifier()

# classifier.train_model()

classes = ['apples', 'bananas', 'peaches']
filepath_to_image = f"{os.getcwd()}\\test_images\\Apple.jpg"
helpers.classify_product(classes, filepath_to_image)
















# product_name_list = ['bananas', 'apples','peaches']
# df = helpers.constructDataFrame(product_name_list)
# helpers.writeToCSV(df)
# filepath = "C:\\Users\\Carter\\Downloads\\20241025-134633_capstone.csv"
# helpers.download_images(filepath)
# product_item_data_dir = pathlib.Path("C:\\Users\\Carter\\git\\Capstone\\data")

''' print list of unique categories in MongoDB '''
# key_list = mongo.getDistinct()
# for i in key_list:
#     if i.isascii():
#         print(i)
