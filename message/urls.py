from django.conf.urls import url
import views

app_name = 'message'
urlpatterns = [
    url(r'^$', views.message_list, name='message_list'),
    url(r'^addmessage/$', views.message_add, name='message_add'),
    url(r'^deletemessage/(?P<msgid>\d+)/$', views.message_delete, name='message_delete'),
    url(r'^editmessage/(?P<msgid>\d+)/$', views.message_edit, name='message_edit'),
    url(r'^selectmap/$', views.select_map, name='select_map'),
]
