from mongo import Mongo
import polars as pl
import datetime


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
        df = pl.DataFrame(data, schema=["image_url", "product_name"], orient="row")
        return df

    def writeToCSV(self, df):
        df.write_csv(f"C:\\Users\\Carter\\Downloads\\{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}_capstone.csv", separator=",")

