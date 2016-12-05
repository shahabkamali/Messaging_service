from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from .models import Building, Floor, Map
from django.views.decorators.csrf import csrf_exempt
from .forms import AddFloorForm, AddMapForm,EditMapForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core import serializers


def map_add(request):
    floorform = AddFloorForm()
    form = AddMapForm()
    if request.method == 'GET':

        return render(request, "add_map.html", {'floorform': floorform, 'mapform':form})
    if request.method == 'POST':
        if 'editmap' in request.POST:
            map = Map.objects.get(id=request.POST['editmap'])
            map.mapname = request.POST['mapname']
            map.floor = Floor.objects.get(id=request.POST['floor'])
            map.picture = request.FILES['picture']
            map.save()
            return HttpResponseRedirect(reverse('map:map_list'))
        form = AddMapForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('map:map_list'))
        else:
            return render(request,"add_map.html",{'floorform': floorform,'mapform':form})


@csrf_exempt
def floor_add(request):
        if request.method == 'POST':
            form = AddFloorForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('done')
            return HttpResponseNotFound('fail')


def map_list(request):
    maps = Map.objects.all()
    return render(request, 'map_list.html',{'maps':maps})


@csrf_exempt
def building_add(request):
    if request.method == "POST":
        if request.POST['name'] != '':
            b = Building(name=request.POST['name'])
            b.save()
        return HttpResponse("Done")


def map_delete(request):
    id = request.GET.get('delete', None)
    if id:
        Map.objects.get(id=id).delete()
        return HttpResponseRedirect(reverse('map:map_list'))


def edit_map(request,mapid):
    m = get_object_or_404(Map, pk=mapid)
    data = {'mapname':m.mapname,'picture':m.picture}
    formget=EditMapForm(initial=data)
    if request.method == 'GET':
        return render(request, 'map_edit.html',{'form':formget,'map':m})
    else:
       form = EditMapForm(request.POST,request.FILES,instance=m)
       if form.is_valid():
            uploaded_form = form.cleaned_data
            mapname = uploaded_form['mapname']
            picture=request.FILES['picture']
            m.mapname=mapname
            m.picture=picture
            m.save()
            return HttpResponseRedirect(reverse('map:map_list'))
       else:
           return render(request, 'map_edit.html',{'form':form,'map':m})


def markers(request,mapid):
    m = Map.objects.get(id=mapid)
    return render(request, 'markers.html',{'map':m})


@csrf_exempt
def save_markers(request,mapid):
    m = get_object_or_404(Map, pk=mapid)
    m.markers =request.POST['json']
    m.save()
    return HttpResponse("Done")


def get_markers(request,mapid):
    m = get_object_or_404(Map, pk=mapid)
    #markers_serialized = serializers.serialize('json', m.markers)
    return JsonResponse(m.markers,safe=False)



