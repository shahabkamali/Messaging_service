from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from map.models import Building,Floor,Map
# Create your views here.

def select_speaker(request):
    building = Building.objects.all()
    if len(building):
        b1 = building[0]
        floors = Floor.objects.filter(building=b1)
        if len(floors):
            f1 = floors[0]
            maps = Map.objects.filter(floor=f1)
            if len(maps):
                map =maps[0]
    return render(request, 'select_speaker.html', {"building": building, "floors":floors, "maps":maps,"map":map})

