from django.conf.urls import url
import views

app_name = 'speaker'
urlpatterns = [
    url(r'^selectspeaker/$', views.select_speaker, name='select_speaker'),
]
