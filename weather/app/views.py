from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

appid = "ce9a769fe69bd36df32f6627d9923114"
api_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid



def index(request):
    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save() 
        form = CityForm()

    try:  
        all_cities = []
        cities = City.objects.all()
        for city in cities:
            res = requests.get(api_url.format(city)).json()

            city_info = {
                'city' : city.name,   
                    'temp_now' : res["main"]["feels_like"],
                    'icon' : res ["weather"][0]["icon"],
                    'pressure' : res ["main"]["pressure"],
                    'description' : res ["weather"][0]["description"],
                    'wind_speed' : res['wind']['speed'],
                }
            all_cities.append(city_info)   
    finally: 
        cities = City.objects.all().delete()           
        context = {'all_info': all_cities, 'form': form}
        return render(request, 'index.html', context)

             

            