# IG Post Automator

<img src="https://raw.githubusercontent.com/Mancini-Rafael/ig-post-creator/master/resources/imgs/instagram_icon.png" align="right"
     alt="IG logo" width="120" height="120">

Instagram Post automator is a python script tool that allows a user to automate the process of generating a IG story post by scraping a website.

* Ignores products that are unavailable
* Support to MongoDB tracking of generated IG stories (*pending*)

# Requirements
- Docker
- DockerCompose

## How It Works

1. IGPA asks for a URL to scrape for image objects and description info
2. The valid image objects are stored in a items.json file
3. The images scraped are checked against a remote DB for duplicity
3. The valid images are downloaded
4. The valid images are combined in the IG story format
5. The created images are updated in the DB to prevent re-run


## Usage
1 - Inside a command line, run ```docker-compose run --rm --service-ports scrapper pipenv run python -i main.py```
2 - In the python terminal, type ```scrape("url")```, replacing url with the url of choice, and
    after the response finishes parsing, type ```process()```
3 - If you ever wish to clean the database, run command 1, and then run ```clear()```
