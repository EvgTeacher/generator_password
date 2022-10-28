from django.shortcuts import render
from django.http import HttpResponse
import string
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    paswd = ''
    lenght = int(request.GET.get('lenght', 10))
    if request.GET.get('uppercase') and request.GET.get('lowercase') and request.GET.get('number'):
        for i in range(lenght):
            paswd += random.choice(string.ascii_letters+'0123456789')
    elif request.GET.get('uppercase') and request.GET.get('number'):
        for i in range(lenght):
            paswd += random.choice(string.ascii_uppercase +'0123456789')
    elif request.GET.get('lowercase') and request.GET.get('number'):
        for i in range(lenght):
            paswd += random.choice(string.ascii_lowercase +'0123456789')
    elif request.GET.get('uppercase') and request.GET.get('lowercase'):
        for i in range(lenght):
            paswd += random.choice(string.ascii_letters)
    elif request.GET.get('uppercase'):
        for i in range(lenght):
            paswd += random.choice(string.ascii_uppercase)
    elif request.GET.get('lowercase'):
        for i in range(lenght):
            paswd += random.choice(string.ascii_lowercase)
    elif request.GET.get('number'):
        for i in range(lenght):
            paswd += random.choice('0123456789')
    else:
        for i in range(lenght):
            paswd += random.choice('0123456789')

    return render(request, 'generator/password.html', {'password': paswd})


def test(request):
    return render(request, 'generator/test.html')
