import random

from django.shortcuts import render
from random import choice


# Create your views here.

def settings_gen(request):
    return render(request, 'generator/index.html')


def generate_password(request):
    signs = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        signs.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        signs.extend('1234567890')
    if request.GET.get('other_signs'):
        signs.extend('!@#$%^&*()_-+=')
    result_password = ''
    password_length = int(request.GET.get('length'))
    for i in range(password_length):
        result_password += random.choice(signs)

    return render(request, 'generator/generated_password.html', {'result_password': result_password})


def about(request):
    return render(request, 'generator/about.html')
