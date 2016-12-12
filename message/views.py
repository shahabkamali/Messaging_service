from django.shortcuts import render
from .models import Message,SavedMessage
from .forms import AddMessageForm
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.shortcuts import get_object_or_404
from map.models import Building,Floor,Map
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import redis
import json
# Create your views here.


def message_list(request):
    msgs = Message.objects.all()
    return render(request, "message_list.html", {'msgs': msgs})


def message_add(request):
    form = AddMessageForm()
    if request.method == 'GET':
        return render(request, "add_message.html", {'form': form})
    if request.method == 'POST':
        form = AddMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('message:message_list'))
        else:
            return render(request, "add_message.html", { 'form': form})


def message_delete(request,msgid):
    get_object_or_404(Message,id=msgid).delete()
    return HttpResponseRedirect(reverse('message:message_list'))


def message_edit(request,msgid):
    msg = get_object_or_404(Message, id=msgid)
    if request.method == 'GET':

        data = {"name":msg.name,"text": msg.text, "r": msg.r, "g": msg.g, "b": msg.b, "font": msg.font,
                "effect": msg.effect, "x": msg.x, "y": msg.y, "showtime": msg.showtime,"brightness":msg.brightness}

        form = AddMessageForm(initial=data)
        return render(request, 'message_edit.html', {"form": form,'msg':msg})
    else:
        form = AddMessageForm(request.POST or None, instance=msg)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('message:message_list'))
        else:
            return render(request, 'message_edit.html', {"form": form,'msg':msg})


def select_map(request):
    building = Building.objects.all()
    if len(building):
        b1 = building[0]
        floors = Floor.objects.filter(building=b1)
        if len(floors):
            f1 = floors[0]
            maps = Map.objects.filter(floor=f1)
            if len(maps):
                map =maps[0]
    messages = Message.objects.all
    saved_message = SavedMessage.objects.all()
    return render(request, 'select_map.html', {"building": building, "floors":floors, "maps":maps,"map":map,"messages":messages,"saved_messages":saved_message})


def get_floors(request,b_id):
    b = Building.objects.get(id=b_id)
    floors = Floor.objects.filter(building=b)
    floors_serialized = serializers.serialize('json', floors)
    return JsonResponse(floors_serialized, safe=False)


def get_maps(request,m_id):
    f = Floor.objects.get(id=m_id)
    maps = Map.objects.filter(floor=f)
    maps_serialized = serializers.serialize('json', maps)
    return JsonResponse(maps_serialized, safe=False)


def get_map_address(request,mapid):
    m = Map.objects.filter(id=mapid)
    map_serialized = serializers.serialize('json', m)
    return JsonResponse(map_serialized, safe=False)

@csrf_exempt
def save_list(request):
    list = request.POST['jsonlist']
    name = request.POST['listname']
    scheck = SavedMessage.objects.filter(name=name)
    if scheck:
        scheck[0].jsonlist = list
        scheck[0].save()
    else:
        s = SavedMessage(name=name,jsonlist=list)
        s.save();
    return HttpResponse("done")


@csrf_exempt
def delete_list(request):
    listname = request.POST['listname']
    SavedMessage.objects.filter(name=listname).delete()
    return HttpResponse("done")



@csrf_exempt
def send_message(request):
    list = request.POST['maclist']
    message_id = request.POST['messageid']
    msg = Message.objects.get(id=message_id)
    str = "{brace_open}\"text\":\"{msg_text}\",\"font\":\"{msg_font}.bdf\",\"x\":{x},\"y\":{y}," \
          "\"r\":{r},\"g\":{g},\"b\":{b},\"effect\":{effect},\"brightness\":" \
          "{brightness},\"showtime\":{showtime}{brace_close}".format(msg_text=msg.text, msg_font=msg.font,
                                                         x=msg.x, y=msg.y, r=msg.r,g=msg.g, b=msg.b,
                                                         effect=msg.effect, brightness=msg.brightness,
                                                         showtime=msg.showtime,brace_open="{", brace_close="}")
    jsonList = json.loads(list)
    maclist=[]
    for item in jsonList:
        maclist.append(item["mac"])
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set("jsonMessage",str)
    r.lpush('maclist', *maclist)
    print maclist
    return HttpResponse("done")

