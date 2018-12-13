from django.shortcuts import render
import requests


def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=034ebcf9d43d63940f9fc34b7a95a8af"
    city = "dhaka"

    r = requests.get(url.format(city)).json()

    city_weather ={
        'city': r['name'],
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'].capitalize(),
        'icon': r['weather'][0]['icon']
    }

    context = {
        "city_weather": city_weather,
    }

    return render(request, 'weather/index.html', context)

