from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    appid = "ce9a769fe69bd36df32f6627d9923114"
    api_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save() 
    form = CityForm()
    cities = City.objects.all()
    all_cities = []
    try:
        if len(cities) > 0 :   
            for city in cities:
                res = requests.get(api_url.format(city)).json()
                city_info = {
                    'city' : city.name,
                        'temp_min' : res["main"]["temp_min"],
                        'temp_now' : res["main"]["temp"],
                        'temp_max' : res["main"]["temp_max"],
                        'icon' : res ["weather"][0]["icon"],
                        'pressure' : res ["main"]["pressure"],
                        'description' : res ["weather"][0]["description"],
                        'wind_speed' : res['wind']['speed'],
                }
                all_cities.append(city_info)    
    except KeyError:
            print('ошибка ключа')
            while True:
                cities = City.objects.all().delete()     
    finally:            
                context = {'all_info': all_cities, 'form': form}
                return render(request, 'index.html', context)