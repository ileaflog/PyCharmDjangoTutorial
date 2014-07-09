from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^ileaflog/', include('ileaflog.urls', namespace="ileaflog")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^doac/', include('doac.urls', namespace="doac")),
    (r'^admin/', include(admin.site.urls)),
)

#
# For 'doac', see https://github.com/Rediker-Software/doac/blob/master/doac/views.py
#