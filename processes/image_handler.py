import os
import json
import sys
import shutil
import requests
import numpy
import math
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from slugify import slugify


class Main:
    def __init__(self):
        pass

    def download_images(self, data):
        """
          Will loop through the sent data object and download
          all images to a imgs folder. Each image will be named
          after the json list index.
        """
        self.check_file_folder_presence()
        for index, item_data in enumerate(data):
            request = requests.get(f"https://{item_data['image_url']}")
            print(f"Downloaded {item_data['description']}")
            img_data = request.content
            path = "tmp/imgs/{index}.jpg".format(index=index)
            with open(path, 'wb') as handler:
                handler.write(img_data)
            self.resize_img_to_aspect_ratio(path)

    def generate_insta_posts(self, data):
        """
          Will look in the data object and merge the jpegs for each ad,
          and add the template text
        """
        for index, item_data in enumerate(data):
            # Find image with the same index -> Content
            path = f"tmp/imgs/{index}.jpg"
            content = Image.open(path)
            # Draw info on banners -> Top / Bottom
            top_banner = self.draw_top_banner(item_data['description_raw'])
            bottom_banner = self.draw_bottom_banner(item_data['value'])
            # Combine images
            new_image = Image.new(mode='RGB', size=(1080, 1920), color='white')
            top_banner_coord = (0, 0)
            content_coord = (0, int((1920 - content.size[1])/2))
            bottom_banner_coord = (0, 1920 - bottom_banner.size[1])
            new_image.paste(content, content_coord)
            new_image.paste(top_banner, top_banner_coord)
            new_image.paste(bottom_banner, bottom_banner_coord)
            image_name = item_data['description']
            print(f'Finished {image_name}')
            new_image.save(f'resources/results/{image_name}.jpg')

    def generate_sale_posts(self, data):
        """
          Will look in the data object and merge the jpegs for each ad,
          and add the template image
        """
        for index, item_data in enumerate(data):
            # Find image with the same index -> Content
            path = f"tmp/imgs/{index}.jpg"
            bg = Image.open(path).convert('RGB')
            fg = Image.open("resources/imgs/sale_banner.png").convert('RGBA')
            fg_resized = fg.resize((300,300))
            coords = (780, 0)
            bg.paste(fg_resized,box=coords,mask=fg_resized)
            image_name = item_data['description']
            bg.save(f'resources/results/{image_name}_sale.jpg')
            print(f'Finished {image_name}')

    def draw_top_banner(self, text):
        raw_img = Image.open("resources/imgs/top_banner.jpg")
        font = ImageFont.truetype("resources/fonts/OpenSans-Bold.ttf", 64)
        img = raw_img.resize((1080, 411))
        color = (0, 0, 0)
        draw = ImageDraw.Draw(img)
        orig_width, orig_height = img.size[0], img.size[1]
        text_grouped = self.split_text_in_threes(text)
        for idx, piece in enumerate(text_grouped):
            text_width, text_height = draw.textsize(piece.upper(), font=font)
            draw.text(((orig_width - text_width)/2, (((orig_height - len(text_grouped)*100) -
                                                      text_height)/2) + ((idx + 1) * 80)), piece.upper(), color, font=font)
        return img

    def draw_bottom_banner(self, text):
        raw_img = Image.open("resources/imgs/bottom_banner.jpg")
        font = ImageFont.truetype("resources/fonts/OpenSans-Light.ttf", 64)
        img = raw_img.resize((1080, 411))
        orig_width, orig_height = img.size[0], img.size[1]
        draw = ImageDraw.Draw(img)

        text_width, text_height = draw.textsize(text, font=font)
        draw.text(((orig_width-text_width)/2, ((orig_height -
                                                text_height)/2) - 110), text, (250, 250, 250), font=font)

        text_width, text_height = draw.textsize(
            'em até 12x sem juros', font=font)
        draw.text(((orig_width-text_width)/2, ((orig_height-text_height) /
                                               2) - 20), 'em até 12x sem juros', (0, 0, 0), font=font)
        return img

    # HELPER METHODS

    def resize_img_to_aspect_ratio(self, path):
        raw_image = Image.open(path)
        orig_width, orig_height = raw_image.size[0], raw_image.size[1]
        print("Previous size", (orig_width, orig_height))
        aspect = orig_height / orig_width
        new_size = (1080, math.ceil(aspect*1080))
        print("New size", new_size)
        content = raw_image.resize(new_size)
        content.save(path)

    def split_text_in_threes(self, text):
        words = text.split()
        grouped_words = [self.clean(' '.join(words[i: i + 3])) for i in range(0, len(words), 3)]
        return grouped_words
    
    def clean(self, text):
        return text.replace("Dolce&Gabbana", "D&G")

    def check_file_folder_presence(self):
        """
          Will check if the items.json file and the imgs folder are present
          and that the imgs folder is empty
        """
        print("Checking file and folder structure")
        if os.path.exists("tmp/imgs"):
            print("Images folder present. Will delete contents to proceed and proceed")
            shutil.rmtree('tmp/imgs')
        if os.path.exists("resources/results"):
            print("Results folder present. Will delete contents to proceed and proceed")
            shutil.rmtree('resources/results')
        os.mkdir("tmp/imgs")
        os.mkdir("resources/results")
