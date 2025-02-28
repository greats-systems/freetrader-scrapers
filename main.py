from fastapi import FastAPI
from controllers.gmbscraper import GMBScraper
from controllers.weather import WeatherController
# from models.weather import WeatherModel
from db.supabase import create_supabase_client

app = FastAPI()
supabase = create_supabase_client()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get('/scrape')
async def scrapeData():
    GMBScraper.scrape()

@app.get('/weather')
async def getWeatherFromAPI():
    data = WeatherController.getWeatherFromAPI()
    return data

@app.post('/weather/create')
async def insertIntoWeatherTable():
    weatherAPIData = WeatherController.getWeatherFromAPI()
    # print(x)
    supabase.from_("WeatherTest").insert({
        "LocationName" : weatherAPIData["LocationName"], 
        "LocationLat" : weatherAPIData["LocationLat"], 
        "LocationLong" : weatherAPIData["LocationLong"], 
        "WindSpeed" : weatherAPIData["WindSpeed"], 
        "Temp" : weatherAPIData["Temp"]}).execute()
    