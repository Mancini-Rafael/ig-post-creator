import traceback
from dotenv import load_dotenv
from processes import scraper
from processes import image_handler
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
            print("Downloading new images")
            image_handler.Main().download_images()
            ##########################
            print("Generating posts")
            image_handler.Main().combine_images()
            #########################
            print("All Done. Check resources/results folder for new generated posts")
            print("**ATTENTION** Running the command will clear all the generated posts inside resources/results")
            ask_for_input()
            url = input()
            continue
        except:
            traceback.print_exc()
            exit()
    print("Exiting")
    exit()

def log_error(msg):
    print(f"Error during script {msg}. Please check with the developer")

def ask_for_input():
    print("Please enter the url you wish to scrape")
    print("If you don't wish to scrape anymore, type *exit*")

run()
