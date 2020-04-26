from processes import scraper
from processes import image_handler



def run():
  scraper.Main().scrape()
  image_handler.Main().download_images()
  image_handler.Main().combine_images()
  # combine_images()
  # zip_files()
  # send_zip_via_email()

run()