from django.shortcuts import render

def home(request):
    import requests
    import json

    news_api_request = requests.get(
        "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=85c2c37ef98c429dacc40f42669a1674"
        )
    api = json.loads(news_api_request.content)
    return render(request,'home.html', {"api":api})

# Create your views here.
