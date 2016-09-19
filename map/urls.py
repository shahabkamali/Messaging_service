from django.conf.urls import url
import views

app_name = 'map'
urlpatterns = [
    url(r'^addmap/', views.map_add, name='map_add'),
    url(r'^$', views.map_list,name='map_list'),
    url(r'^addbuilding/$', views.building_add, name='building_add'),
    url(r'^addfloor/$', views.floor_add, name='floor_add'),
    url(r'^mapdelete/$', views.map_delete, name='map_delete'),
    url(r'^editmap/(?P<mapid>\d+)/$', views.edit_map ,name='edit_map'),
]
