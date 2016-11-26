from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required(login_url='/users/login/')
def index(request):
    return render(request, 'dashboard.html')



def hardware(request):
    return render(request, 'hardware.html')


def add_hardware(request):
    return render(request, 'add_hardware.html')


def message(request):
    return render(request, 'messages.html')


def add_message(request):
    return render(request, 'add_message.html')


def send_message(request):
    return render(request, 'send_message.html')

def map_list(request):
    return render(request, 'map_list.html')