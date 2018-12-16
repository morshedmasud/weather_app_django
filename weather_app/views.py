from django.shortcuts import render, redirect
import requests
from .models import Weather
from .forms import WeatherForm
from django.contrib import messages


def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=034ebcf9d43d63940f9fc34b7a95a8af"
    if request.method == "POST":
        response = requests.get(url.format(request.POST.get('city_name')))

        if response.status_code != 200:
            messages.error(request, "'{}' this city maybe not valid!! try another..".format(request.POST.get('city_name')))
            return redirect('index')

        data = WeatherForm(request.POST)
        data.save()

    cities = Weather.objects.all()[::-1]
    weather_data = []
    count = 1
    for city in cities:
        if count == 5:
            break
        r = requests.get(url.format(city)).json()
        city_weather ={
            'city': r['name'],
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'].capitalize(),
            'icon': r['weather'][0]['icon']
        }
        weather_data.append(city_weather)
        count += 1

    form = WeatherForm()
    context = {
        "weather_data": weather_data,
        "form": form
    }

    return render(request, 'weather/index.html', context)

