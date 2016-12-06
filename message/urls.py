from django.conf.urls import url
import views

app_name = 'message'
urlpatterns = [
    url(r'^$', views.message_list, name='message_list'),
    url(r'^addmessage/$', views.message_add, name='message_add'),
    url(r'^deletemessage/(?P<msgid>\d+)/$', views.message_delete, name='message_delete'),
    url(r'^editmessage/(?P<msgid>\d+)/$', views.message_edit, name='message_edit'),
    url(r'^selectmap/$', views.select_map, name='select_map'),
    url(r'^getfloors/(?P<b_id>\d+)/$', views.get_floors, name='get_floors'),
    url(r'^getmaps/(?P<m_id>\d+)/$', views.get_maps, name='get_maps'),
    url(r'^getmapaddress/(?P<mapid>\d+)/$', views.get_map_address, name='get_map_address'),
    url(r'^sendmessage/$', views.send_message, name='send_message'),
    url(r'^savelist/$', views.save_list, name='save_list'),
    url(r'^deletelist/$', views.delete_list, name='delete_list'),
]
