import traceback
from dotenv import load_dotenv
from processes import scraper
from processes import image_handler
from processes import database_handler
load_dotenv()

def run():
    print("Welcome to the automated IG post creator")
    ask_for_input()
    url = input()
    while url != 'exit':
        try:
            print("Scraping")
            scraper.Main().scrape(url)
            ##########################
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
            ask_for_input()
            url = input()
            continue
        except:
            traceback.print_exc()
            print(f"Error during script. Please check with the developer")
    print("Exiting")

def ask_for_input():
    print("Please enter the url you wish to scrape")
    print("If you don't wish to scrape anymore, type *exit*")

# run()
