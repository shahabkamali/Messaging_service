from django.conf.urls import url
import views

app_name = 'tv'
urlpatterns = [
    url(r'^$', views.message_list, name='message_list'),
    url(r'^addtvmessage/$', views.tv_message_add, name='tv_message_add'),
    url(r'^edittvmessage/(?P<mid>\d+)/$', views.tv_message_edit, name='tv_message_edit'),
    url(r'^deletetvmessage/(?P<mid>\d+)/$', views.tv_message_delete, name='tv_message_delete'),
    url(r'^edittvmessage/$', views.tv_message_edit, name='tv_message_edit'),
    url(r'^sendmessage/$', views.send_message, name='send_message'),
    url(r'^selecttv/$', views.select_tv, name='select_tv'),
    url(r'^savelist/$', views.save_list, name='save_list')
]
