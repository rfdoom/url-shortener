from webbrowser import get
from django.shortcuts import render, redirect
from django.forms import ValidationError
import requests
from models import URL
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

API_KEY = 'e99aae469de9eacb0c20ad6735ff7dbc4b1fb'


def home(request):
    return render(request, 'home.html')

@csrf_exempt
def encode(request):
    if request.method == 'post':
        try:
            url = request.POST['url-input']
            get_short_url = f'https://cutt.ly/api/api.php?key={API_KEY}&short={url}'
            data = requests.get(get_short_url).json(['url'])
            if data['status'] == 7:
                new_instance = URL()
                new_instance.longURL = url
                new_instance.nickname = request.POST['nickname-input']
                new_instance.shortURL = data['shortLink']
                new_instance.save()
            else:
                status = data['status']
                return f'ERROR STATUS: {status}'
        except ValidationError as e:
            return redirect('error')
    return render(request, 'encode.html')

def decode(request):
    return render(request, 'decode.html')