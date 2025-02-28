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
    data = []
    cities = ['Harare', 'Bulawayo', 'Gweru']
    data.append(WeatherController.getWeatherFromAPI(cities))
    return data

@app.post('/weather/create')
async def insertIntoWeatherTable():
    data = []
    cities = ['Harare', 'Bulawayo', 'Gweru']
    data.append(WeatherController.getWeatherFromAPI(cities))
    for cityData in data[0]:
        # print(cityData)
        try:
            supabase.from_("WeatherTest").insert({
                "LocationName" : cityData["LocationName"], 
                "LocationLat" : cityData["LocationLat"], 
                "LocationLong" : cityData["LocationLong"], 
                "WindSpeed" : cityData["WindSpeed"], 
                "Temp" : cityData["Temp"]}).execute()            
        except Exception as e:
            print(e)
    return data[0]
    