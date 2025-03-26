# IG Post Automator - Fashion Version

<img src="https://raw.githubusercontent.com/Mancini-Rafael/ig-post-creator/master/resources/imgs/instagram_icon.png" align="right"
     alt="IG logo" width="120" height="120">

Python based scrapper that given an url:
- Parses the URL for images
- Extract images in high quality
- Process images and applies visual elements in order to speed up generation of IG posts for fashion publisher

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


## Setup
- Run the command ```./bin/docker_setup.sh```

## Usage
- Inside a command line, run ```docker-compose run --rm --service-ports scrapper bash```
- Run the command ```pipenv sync``` 
- To scrape, run ```pipenv run python main.py```
