import json
import traceback
import pymongo
from slugify import slugify


class Main:
    def __init__(self):
        self.client = pymongo.MongoClient('db', username='root', password='password')

    def check_for_duplicates(self):
        non_duplicated_data = []
        with open('items.json') as json_file:
            data = json.load(json_file)
            for index, item_data in enumerate(data):
                item_data_normalized = self.normalize_data(item_data)
                obj_id = self.client.fashion_scrapper.images.find_one(item_data_normalized)
                if obj_id is None:  # Is new object
                    non_duplicated_data.append(item_data_normalized)
                else:
                    continue
        return non_duplicated_data

    def update_db(self, data):
        try:
            self.client.fashion_scrapper.images.insert_many(data)
        except:
          traceback.print_exc()

    def normalize_data(self, data):
        normalized_image = {
            'image_url': data['url'],
            'description': slugify(data['desc']),
            'description_raw': data['desc'],
            'value': data['value_raw']
        }
        return normalized_image
    
    def clean_data(self):
        self.client.fashion_scrapper.images.drop()
