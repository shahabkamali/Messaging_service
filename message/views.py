from django.shortcuts import render

# Create your views here.


def message_add(request):
    form = AddMapForm()
    if request.method == 'GET':
        return render(request, "add_message.html", {'form': form})