from dotenv import load_dotenv
import os
import requests
from db.supabase import create_supabase_client
# from models.weather import WeatherModel

load_dotenv()

WEATHER_SERVICE_API_KEY=os.getenv("WEATHER_SERVICE_API_KEY")

class WeatherController:
    # baseUrl = 'http://api.weatherapi.com/v1/current.json'
    # params = {
    #         'q': 'Harare',
    #         'key': WEATHER_SERVICE_API_KEY
    #     }
    # supabase = create_supabase_client()

    def getWeatherFromAPI(cities):
        weatherData = []
        for city in cities:
            baseUrl = 'http://api.weatherapi.com/v1/current.json'
            params = {
                    'q': city,
                    'key': WEATHER_SERVICE_API_KEY
                }            
            response = requests.get(baseUrl, params)            
            try:
                data = {}
                response = requests.get(baseUrl, params)
                print(response.json())
                data['LocationName']=response.json()['location']['name']
                data['LocationLat']=response.json()['location']['lat']
                data['LocationLong']=response.json()['location']['lon']
                data['WindSpeed']=response.json()['current']['wind_kph']
                data['Temp']=response.json()['current']['temp_c']  
                weatherData.append(data)              
            except Exception as e:
                print('Exception ' ,e)
                return e
        return weatherData
        
    def insertIntoWeatherTable(self):
        pass
