from django.conf.urls import url
import views

app_name = 'speaker'
urlpatterns = [
    url(r'^selectspeaker/$', views.select_speaker, name='select_speaker'),
    url(r'^record/$', views.record, name='record'),
    url(r'^voicelist/$', views.voice_list, name='voice_list'),
    url(r'^addvoice/$', views.voice_add, name='voice_add'),
    url(r'^deletevoice/(?P<vid>\d+)/$', views.voice_delete, name='voice_delete'),
    url(r'^savelist/$', views.save_list, name='save_list'),
    url(r'^deletelist/$', views.delete_list, name='delete_list'),
    url(r'^sendvoice/$', views.send_voice, name='send_voice'),
]
