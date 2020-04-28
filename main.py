from dotenv import load_dotenv
load_dotenv()

from processes import scraper
from processes import image_handler


def run():
  print("Starting fashion_scraper")
  print("========================")
  print("Running command: scrape")
  scraper.Main().scrape()
  print("Command scrape ran successfully")
  print("========================")
  print("Running command: download_images")
  image_handler.Main().download_images()
  print("Command download_images ran successfully")
  print("========================")
  print("Running command: combine_images")
  image_handler.Main().combine_images()
  print("Command combine_images ran successfully")
  print("========================")
  print("Running command: zip_files")
  # zip_files()
  # send_zip_via_email()

run()