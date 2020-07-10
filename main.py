import traceback
import os
import time
import zipfile
from dotenv import load_dotenv
from processes import scraper
from processes import image_handler
from processes import database_handler
load_dotenv()

def process():
    print("Checking for duplicates")
    data = database_handler.Main().check_for_duplicates()
    ##########################
    print("Downloading new images")
    image_handler.Main().download_images(data)
    ##########################
    print("Generating insta-posts")
    image_handler.Main().generate_insta_posts(data)
    ##########################
    print("Generating sale posts")
    image_handler.Main().generate_sale_posts(data)
    #########################
    print("Updating databases")
    database_handler.Main().update_db(data)
    ##########################
    print("All Done. Check tmp/results folder for new generated posts")
    print("**ATTENTION** Running the command again will clear all the generated posts inside tmp/results")

def scrape(url):
    print("Welcome to the automated IG post creator")
    print("Scraping")
    scraper.Main().scrape(url)
    print("Scraped")
    print("Processing")
    process()
    zip_result()

def clear():
    print("Cleaning Database")
    database_handler.Main().clean_data()
    print("Database cleaned")

def leave():
    print("Bye Bye")
    raise SystemExit(0)

def zip_result():
    timestring = time.strftime("%Y%m%d-%H%M%S")
    zipf = zipfile.ZipFile(f"result_{timestring}.zip", 'w', zipfile.ZIP_DEFLATED)
    path="resources/results/"
    for root, _, files in os.walk(path):
        for file in files:
            zipf.write(os.path.join(root, file))
    zipf.close()

def main():
    print("Please enter the *url* to scrape or *clear* to start fresh or *exit* to leave")
    url = input()
    if url == "clear":
        clear()
        main()
    if url == "exit":
        leave()
    scrape(url)
    leave()

if __name__ == "__main__":
    main()