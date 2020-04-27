import os
import json
import sys
import shutil
import requests

class Main:
  def __init__(self):
    pass

  def download_images(self):
    """
      Will loop through a item.json file in the project
      root and download all images to a imgs folder.
      Each image will be named after the json list index.
    """
    self.check_file_folder_presence()
    with open('items.json') as json_file:
      data = json.load(json_file)
      for index, item_data in enumerate(data):
        img_data = requests.get(f"https://{item_data['url']}").content        
        # with open("tmp/imgs/{index}.jpg".format(index = index), 'wb') as handler:
        #   handler.write(img_data)

  def combine_images(self):
    """
      Will look in the items.json file and merge the jpegs for each ad,
      and add the template text
    """


  def check_file_folder_presence(self):
    """
      Will check if the items.json file and the imgs folder are present
      and that the imgs folder is empty
    """

    print("Checking file and folder structure")
    if os.path.exists("tmp/imgs") and not(os.path.isdir("tmp/imgs")):
      print("Images file present instead of folder")
      # Remove imgs file
    elif os.path.exists("tmp/imgs") and os.path.isdir("tmp/imgs"):
      print("Images folder present. Will delete contents to proceed and proceed")
      shutil.rmtree('tmp/imgs')
    elif not(os.path.exists("items.json")) or not(os.path.isfile("items.json")):
      sys.exit("Can't find the items.json file. It must be present to proceed")
    else:
      print("Images folder not present. Will create")
    os.mkdir("tmp/imgs")