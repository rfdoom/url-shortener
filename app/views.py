from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def encode(request):
    return render(request, 'encode.html')

def decode(request):
    return render(request, 'decode.html')