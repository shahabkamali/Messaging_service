from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

def tv(request) :
    if not request.user.is_authenticated():
        return redirect('/login')
    return render(request, 'tv_preset.html')

def text(request) :
    if not request.user.is_authenticated():
        return redirect('/login')
    return render(request, 'text_preset.html')