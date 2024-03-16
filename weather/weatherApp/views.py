import urllib.parse
from django.shortcuts import render
import json
import urllib.request
from dotenv import load_dotenv
import os

load_dotenv()
# Create your views here.

api = os.getenv("API_KEY")

def index(request):
    if request.method == "POST":
        city = request.POST["city"]
        url = 'http://api.openweathermap.org/data/2.5/weather?q='+ city + '&units=metric&appid=' + str(api)

        encoded_url = urllib.parse.quote(url, safe=':/?&=') # to remove the spaces from the user 
        source = urllib.request.urlopen(encoded_url).read()
        
        list_data = json.loads(source)

        data = {
            "name":str(list_data['name']), 
            "country_code": str(list_data['sys']['country']),
            "coordinate": str(list_data['coord']['lon']) + ', '
            + str(list_data['coord']['lat']),

            "temp": str(list_data['main']['temp']) + ' °C',
            "pressure": str(list_data['main']['pressure']),
            "humidity": str(list_data['main']['humidity']),
            'main': str(list_data['weather'][0]['main']),
            'description': str(list_data['weather'][0]['description']),
            'icon': list_data['weather'][0]['icon'],
            'base': list_data['base'],
        }
        print(data)
    else:
        data={}

    return render(request, "main/index.html", data)