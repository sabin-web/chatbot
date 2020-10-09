import json
import os

import urllib.request

def lambda_handler(event, context):
    
    city = event['currentIntent']['slots']['City']

    api_key = os.environ['APPID']
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    final_url = base_url +'q='+ city+ "&appid=" + api_key 
    
    weather_result = json.load(urllib.request.urlopen(final_url))
    temp = str(round(weather_result['main']['feels_like'] - 273.15,2))
    message=weather_result['weather'][0]['description']
    humidity = weather_result['main']['humidity']
    wind = weather_result['wind']['speed']
    temperature = f'The temperature feels like {temp} °C in {city}.It is {message}.The humidity is {humidity}%.The wind speed is {wind} km/h.'
    
    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "SSML",
              "content": temperature
            },
        }
    }
    return response
