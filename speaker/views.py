from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from .models import Voice,SavedMessage
from .forms import AddVoiceForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from map.models import Building,Floor,Map
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import redis

# Create your views here.


def voice_list(request):
    voices = Voice.objects.all()
    return render(request, "voice_list.html", {'voices': voices})


def voice_add(request):
    form = AddVoiceForm()
    if request.method == 'GET':
        return render(request, "add_voice.html", {'form': form})
    if request.method == 'POST':
        form = AddVoiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('speaker:voice_list'))
        else:
            return render(request, "add_voice.html", {'form': form})


def voice_delete(request,vid):
    get_object_or_404(Voice, id=vid).delete()
    return HttpResponseRedirect(reverse('speaker:voice_list'))


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
    voices = Voice.objects.all
    saved_message = SavedMessage.objects.all()
    return render(request, 'select_speaker.html', {"building": building, "floors":floors, "maps":maps,"map":map,"voices":voices,"saved_messages":saved_message})


def record(request):
    return render(request, 'record.html', {})


@csrf_exempt
def save_list(request):
    list = request.POST['jsonlist']
    name = request.POST['listname']
    scheck = SavedMessage.objects.filter(name=name)
    if scheck:
        scheck[0].jsonlist = list
        scheck[0].save()
    else:
        s = SavedMessage(name=name, jsonlist=list)
        s.save();
    return HttpResponse("done")


@csrf_exempt
def delete_list(request):
    listname = request.POST['listname']
    SavedMessage.objects.filter(name=listname).delete()
    return HttpResponse("done")



@csrf_exempt
def send_voice(request):
    voicename = request.POST['voicename']
    maclist = request.POST['maclist']
    print voicename,maclist
    jsonList = json.loads(maclist)
    maclist = []
    for item in jsonList:
        maclist.append(item["mac"])
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set("voicename", voicename)
    r.lpush('maclist', *maclist)
    return HttpResponse("done")


def find_speaker(request):
    if request.method == "GET":
        with open(settings.BASE_DIR + "/jsonlist.json", "r+") as f:
            jsonlist = json.loads(f.read())
        maps = Map.objects.all()
        assigned = []
        for map in maps:
            markerjson =json.loads(map.markers)
            notes = markerjson
            for note in notes:
                mac = note['note'].split("</br>")[1]
                assigned.append(mac)
        maclist = []
        for mac in jsonlist:
            if mac not in assigned:
                maclist.append(mac)
        return render(request, 'find_speaker.html', {"maclist": maclist})
    else:
        pass
