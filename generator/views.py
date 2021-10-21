from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    password = ""
    characters = list('abcdefghijklmnopqrstuvwxyz')
    upperchar = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('123456789')
    special_char = list('!@#$%^&*()_+')
    length = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        characters.extend(upperchar)
    if request.GET.get('numbers'):
        characters.extend(numbers)
    if request.GET.get('specialchar'):
        characters.extend(special_char)
    for i in range(length):
        password+=random.choice(characters)
    return render(request, 'generator/password.html', {'password': password})

def about(request):
    return render(request, 'about/about.html')
