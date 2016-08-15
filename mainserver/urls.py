from django.conf.urls import include, url
from django.contrib import admin
from panel import views as panelviews
urlpatterns = [
    # Examples:
    #url(r'^$', 'panel.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^', include(admin.site.urls)),

    url(r'^$', 'panel.views.index'),
    url(r'^logout', 'panel.views.logout_user'),
    url(r'^login', 'panel.views.login_user'),
    url(r'^map', 'panel.map.show_page'),
    url(r'^text-preset', 'panel.preset.text'),
    url(r'^tv-preset', 'panel.preset.tv'),
    url(r'^userlists', panelviews.user_lists),
    url(r'^useradd', panelviews.user_add),
    url(r'^hardwares', panelviews.hardware),
    url(r'^addhardware', panelviews.add_hardware),
    url(r'^messages', panelviews.message),
    url(r'^addmessage', panelviews.add_message)
]
