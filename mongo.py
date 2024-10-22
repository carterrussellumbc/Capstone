from pymongo import MongoClient


class Mongo:

    def __init__(self):
        self.uri = "mongodb://localhost:27017/"
        self.coll = 'products'

    def createClient(self):
        return MongoClient(self.uri)

    def getColl(self):
        client = self.createClient()
        db = client.off
        return db[self.coll]

    def getProduct(self, productName):
        coll = self.getColl()
        product = coll.find({"categories_hierarchy": f"en:{productName}"})
        return product, productName

    def getDistinct(self):
        key_list = []
        coll = self.getColl()
        for i in coll.find().distinct("categories_hierarchy"):
            if i:  # Quick way to deal with NoneType
                if i.isascii():  # Get rid of a majority of non-english products inside the en: category
                    if i.startswith('en:'):
                        key_list.append(i)
        return key_list
