from webbrowser import get
from django import shortcuts
from django.shortcuts import render, redirect
from django.forms import ValidationError
import requests
from .models import URL
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

API_KEY = 'e99aae469de9eacb0c20ad6735ff7dbc4b1fb'
ONE_SIMPLE_API_KEY = 'lZNWLMwKTe41DQsBzMr5rocfFfhCFVhAQ1oIUr1R'


def home(request):
    return render(request, 'home.html')

@csrf_exempt
def encode(request):
    if request.method == 'POST':
        try:
            url = request.POST['url-input']
            get_short_url = f'https://cutt.ly/api/api.php?key={API_KEY}&output=json&short={url}'
            data = requests.get(get_short_url).json()
            print('URL:', url, 'shortURL:', get_short_url, 'data:', data)
            if data['url']['status'] == 7:
                new_instance = URL()
                new_instance.longURL = url
                new_instance.nickname = request.POST['nickname-input']
                new_instance.shortURL = data['url']['shortLink']
                new_instance.save()
                return render(request, 'encode.html', {'data':data})
            else:
                status = data['url']['status']
                print(f'ERROR STATUS: {status}')
                return redirect('error', {'error': status})
        except ValidationError as e:
            return redirect('error')
    return render(request, 'encode.html')

@csrf_exempt
def decode(request):
    if request.method == 'POST':
        url = request.POST['decode-input']
        get_long_url = f'https://onesimpleapi.com/api/unshorten?token={ONE_SIMPLE_API_KEY}&url={url}'
        print(get_long_url)
        return render(request, 'decode.html', {'data': get_long_url})
    return render(request, 'decode.html')

def error(request):
    return render(request, 'error.html')