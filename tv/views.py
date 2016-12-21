from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from map.models import Building, Floor, Map
from django.views.decorators.csrf import csrf_exempt
from .models import SavedMessage,Message
from .forms import AddMessageForm
from django.views.decorators.csrf import csrf_exempt
import redis
import json


def message_list(request):
    messages = Message.objects.all()
    return render(request, "tv_message_list.html", {'messages': messages})


def tv_message_add(request):
    form = AddMessageForm()
    if request.method == 'GET':
        return render(request, "add_tv_message.html", {'form': form})
    if request.method == 'POST':
        form = AddMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tv:message_list'))
        else:
            return render(request, "add_tv_message.html", {'form': form})


def tv_message_edit(request,mid):
    msg = get_object_or_404(Message, id=mid)
    if request.method == 'GET':

        data = {"name":msg.name,"showtime":msg.showtime,"context": msg.context}
        form = AddMessageForm(initial=data)
        return render(request, 'tv_message_edit.html', {"form": form,'msg':msg})
    else:
        form = AddMessageForm(request.POST or None, instance=msg)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tv:message_list'))
        else:
            return render(request, 'tv_message_edit.html', {"form": form,'msg':msg})


def tv_message_delete(request,mid):
    get_object_or_404(Message, id=mid).delete()
    return HttpResponseRedirect(reverse('tv:message_list'))



def select_tv(request):
    building = Building.objects.all()
    if len(building):
        b1 = building[0]
        floors = Floor.objects.filter(building=b1)
        if len(floors):
            f1 = floors[0]
            maps = Map.objects.filter(floor=f1)
            if len(maps):
                map = maps[0]
    messages = Message.objects.all()
    saved_message = SavedMessage.objects.all()
    return render(request, 'select_tv.html', {"building": building, "floors": floors, "maps": maps, "map": map,"saved_messages":saved_message,"messages":messages})


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
def send_message(request):
    list = request.POST['maclist']
    message_id = request.POST['messageid']
    msg = Message.objects.get(id=message_id)
    jsonstr={}
    jsonstr["showtime"]=msg.showtime
    jsonstr["text"]=msg.context
    jsonstr=json.dumps(jsonstr, ensure_ascii=False)
    print str
    jsonList = json.loads(list)
    maclist=[]
    for item in jsonList:
        maclist.append(item["mac"])
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set("tvMessage",jsonstr)
    r.lpush('maclist', *maclist)
    print maclist
    return HttpResponse("done")