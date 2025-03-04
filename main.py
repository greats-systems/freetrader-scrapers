from fastapi import FastAPI
from controllers.gmbscraper import GMBScraper
from controllers.weather import WeatherController
from db.supabase import create_supabase_client

app = FastAPI()
supabase = create_supabase_client()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get('/scrape')
async def scrapeData():
    GMBScraper.scrape()

@app.get('/weather/open-weather')
async def getWeatherFromAPI():
    data = []
    cities = ['Harare', 'Bulawayo', 'Gweru', 'Mutare', 'Masvingo', 'Hwange', 'Victoria Falls', 'Kariba', 'Kwekwe', 'Gwanda', 'Beitbridge']
    data.append(WeatherController.getWeatherFromAPI(cities))
    return data[0]

@app.get('/weather/supabase')
async def getWeatherFromSupabase():
    result = supabase.table("WeatherTest").select('*').order(column='id').execute()
    return result.data

@app.get('/weather/supabase/insert')
async def insertIntoWeatherTable():
    data = []
    # cities = ['Harare', 'Bulawayo', 'Gweru', 'Mutare', 'Masvingo', 'Hwange', 'Victoria Falls', 'Kariba', 'Kwekwe', 'Gwanda', 'Beitbridge']
    # data.append(WeatherController.getWeatherFromAPI(cities))
    data.append(WeatherController.getWeatherFromAPI())
    for cityData in data:
        try:
            supabase.from_("WeatherTest").insert({
                "LocationName" : cityData["LocationName"], 
                "LocationLat" : cityData["LocationLat"], 
                "LocationLong" : cityData["LocationLong"], 
                "WindSpeed" : cityData["WindSpeed"], 
                "Temp" : cityData["Temp"]}).execute()            
        except Exception as e:
            print(e)
    return 'Weather data has been added successfully!'
    