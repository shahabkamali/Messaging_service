from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from panel.views import index
from django.contrib.auth import logout
from .forms import UserAddForm

# Create your views here.


def login_user(request):
    if request.method == "GET":

        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                # Return a 'disabled account' error message
                return render(request, 'login.html', {
                    'errror': 'your account is disabled , contact support .',
                }, content_type='application/xhtml+xml')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {
                'errror': 'your username or password is invalid, try again.',
            }, content_type='application/xhtml+xml')


def logout_user(request):
    logout(request)
    return redirect('/')


def user_lists(request):
    return render(request, 'users.html')


def user_add(request):
    if request.method == "POST":
        print "in post"
    else:
        print "in get"
        form = UserAddForm()
        print type(form)
        print "1",form.firstname
        context = {'form': form}
    return render(request, 'add_user.html', context)