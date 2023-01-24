from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def search_page(request):
    zipcode = 37027
    url = f'https://www.weather-daily.com/wp-json/weather/by_postal_code/{zipcode}'
    response = requests.get(url)
    context = {
        "data": response.json()
    }
    return  HttpResponse(response.json())
    # return render(request, 'weather/search_page.html', context)