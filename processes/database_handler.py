import pymongo
import json
import os
from slugify import slugify


class Main:
    """
      "image": {
        "_id": "value_set_by_pymong",
        "image_url": "url"
        "description": "text_without_spaces_and_special_characters",
        "value": "value"
      }
    """

    def __init__(self):
        self.username = os.getenv('DB_USERNAME')
        self.password = os.getenv('DB_PASSWORD')
        self.db_url = f"mongodb+srv://{self.username}:{self.password}@clio-qab7o.mongodb.net/"
        self.client = pymongo.MongoClient(self.db_url)

    def check_for_duplicates(self):
        non_duplicated_data = []
        with open(os.getenv('JSON_FILE_PATH')) as json_file:
            data = json.load(json_file)
            for index, item_data in enumerate(data):
                item_data_normalized = self.normalize_data(item_data)
                obj_id = self.client.fashion_scrapper.images.find_one(
                    item_data_normalized)
                if obj_id is None:  # Is new object
                    non_duplicated_data.append(item_data_normalized)
                else:
                    continue
        return non_duplicated_data

    def update_db(self, data):
        pass

    def normalize_data(self, data):
        normalized_image = {
            'image_url': data['url'],
            'description': slugify(data['desc']),
            'value': data['value_raw']
        }
        return normalized_image
