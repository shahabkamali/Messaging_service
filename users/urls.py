from django.conf.urls import url
import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




app_name = 'users'
urlpatterns = [
    url(r'^useradd/', views.user_add, name='user_add'),
    url(r'^userlists/', views.user_lists, name="user_lists"),
    url(r'^login/', views.login_user, name='login_user'),
    url(r'^logout/', views.logout_user, name='logout'),
    url(r'^changepassword/', views.change_password, name='change_password'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

