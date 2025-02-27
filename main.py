from fastapi import FastAPI
from gmbscraper import GMBScraper

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get('/scrape')
async def scrapeData():
    GMBScraper.scrape()