from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

def index(request):
    if not request.user.is_authenticated():
        return redirect('/login')
    return render(request, 'dashboard.html')


def logout_user(request):
    logout(request)
    return redirect('/login')

def login_user(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                # Return a 'disabled account' error message
                return render(request, 'panel/login.html', {
                    'errror': 'your account is disabled , contact support .',
                }, content_type='application/xhtml+xml')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'panel/login.html', {
                'errror': 'your username or password is invalid, try again.',
            }, content_type='application/xhtml+xml')

