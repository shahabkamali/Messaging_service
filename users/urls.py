from django.conf.urls import url
import views

app_name = 'users'
urlpatterns = [
    url(r'^useradd/', views.user_add, name='user_add'),
    url(r'^userlists/', views.user_lists, name="user_lists"),
    url(r'^login/', views.login_user, name='login_user'),
    url(r'^logout/', views.logout_user, name='logout'),
    url(r'^profilepicture/', views.getProfilePicture, name='getProfilePicture'),
]
