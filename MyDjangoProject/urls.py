from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^ileaflog/', include('ileaflog.urls', namespace="ileaflog")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    (r'^admin/', include(admin.site.urls)),
)