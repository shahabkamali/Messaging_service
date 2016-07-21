from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    #url(r'^$', 'panel.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^', include(admin.site.urls)),

    url(r'^$', 'panel.views.index'),
    url(r'^logout', 'panel.views.logout_user'),
    url(r'^login', 'panel.views.login_user'),
    url(r'^map', 'panel.map.show_page'),
]
