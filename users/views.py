from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login
from panel.views import index
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms import UserAddForm,UserEditForm
from .models import UserProfile


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

                return render(request, 'login.html', {
                    'error': 'your account is disabled , contact support .',
                }, content_type='application/xhtml+xml')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {
                'error': 'your username or password is invalid, try again.',
            }, content_type='application/xhtml+xml')


def logout_user(request):
    logout(request)
    return redirect('/')


def user_lists(request):
    id = request.GET.get('delete', None)

    if id:
        user = User.objects.get(id=id)
        if request.user == user:
            UserProfile.objects.get(user_id=id).delete()
            return HttpResponseRedirect(reverse('users:logout'))

    users_profile = UserProfile.objects.all()
    context = {'users': users_profile}
    return render(request, 'users.html', context)


def handle_uploaded_file(image):
    import StringIO
    from PIL import Image
    image_file = StringIO.StringIO(image.read())
    image = Image.open(image_file)
    w, h = image.size
    image = image.resize((w/2, h/2), Image.ANTIALIAS)

    image_file = StringIO.StringIO()
    image.save(image_file, 'JPEG', quality=90)
    return image


def user_add(request):
    if request.method == "POST":
        pic = ""
        if 'picture' in request.FILES:
            pic = request.FILES['picture']
        if 'id' in request.POST:
            form = UserEditForm(request.POST, request.FILES)
            if form.is_valid():
                uploaded_form = form.cleaned_data
                firstname = uploaded_form['firstname']
                lastname = uploaded_form['lastname']
                email = uploaded_form['email']
                password = uploaded_form['password1']
                id = uploaded_form['id']
                user = User.objects.get(id=id)
                user.first_name = firstname
                user.last_name = lastname
                user.email = email
                user.set_password(password)
                userpf = UserProfile.objects.get(user_id=id)
                userpf.picture = pic
                user.save()
                userpf.save()
            else:
                context = {'form': form}
                return render(request, 'add_user.html', context)
        else:
            form = UserAddForm(request.POST, request.FILES)
            if form.is_valid():
                uploaded_form = form.cleaned_data
                username = uploaded_form['username']
                firstname = uploaded_form['firstname']
                lastname = uploaded_form['lastname']
                email = uploaded_form['email']
                password = uploaded_form['password1']
                pic = ""
                if 'picture' in request.FILES:
                    pic = request.FILES['picture']

                user = User.objects.create_user(username=username,
                                            first_name=firstname, last_name=lastname, email=email, password=password)
                user.save()
                userprofile = UserProfile(picture=pic, user=user)
                userprofile.save()
            else:
                context = {'form': form}
                return render(request, 'add_user.html', context)
        return HttpResponseRedirect(reverse('users:user_lists'))
    else:
        id = request.GET.get('edit', None)
        data = None
        form = UserAddForm(initial=data)
        if id:
            usp = UserProfile.objects.get(user_id=id)
            if request.user != usp.user:
                 return HttpResponseRedirect(reverse('users:user_lists'))
            data = {'firstname': usp.user.first_name,
                    'lastname': usp.user.last_name, 'email': usp.user.email,'picture':usp.picture,'id':id}
            form = UserEditForm(initial=data)
        context = {'form': form,'id':id}
        return render(request, 'add_user.html', context)


def responce_image(address):
    try:
        image_data = open(address, "rb").read()
        return HttpResponse(image_data, content_type="image/png")
    except IOError:
        return address


def getProfilePicture(request):
    userp = None
    try:
        userp = UserProfile.objects.get(user_id=request.user.id)
    except:
        userp = None
    if userp == None:
        res = responce_image("static/dist/img/404_user.png")
    else:
        res = responce_image("users/static/users/picture/{username}.jpg".format(username=userp.user.username))
    return HttpResponse(res)
