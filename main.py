import traceback
import time
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
    print("Generating posts")
    image_handler.Main().combine_images(data)
    #########################
    print("Updating databases")
    database_handler.Main().update_db(data)
    ##########################
    print("All Done. Check tmp/results folder for new generated posts")
    print("**ATTENTION** Running the command will clear all the generated posts inside tmp/results")

def scrape(url):
    print("Welcome to the automated IG post creator")
    print("Scraping")
    scraper.Main().scrape(url)
    time.sleep(10)
    print("Scraped")

def clear():
    database_handler.Main().clean_data()