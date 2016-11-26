from django.conf.urls import url
import views

app_name = 'message'
urlpatterns = [
    url(r'^addmessage/', views.message_add, name='message_add'),
]
