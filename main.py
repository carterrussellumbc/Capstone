from mongo import Mongo
from helpers import Helpers
import polars as pl

mongo = Mongo()
helpers = Helpers()
product_name_list = ['bananas', 'apples', 'peaches']
df = helpers.constructDataFrame(product_name_list)
# helpers.writeToCSV(df)

# key_list = mongo.getDistinct()
# for i in key_list:
#     if i.isascii():
#         print(i)
