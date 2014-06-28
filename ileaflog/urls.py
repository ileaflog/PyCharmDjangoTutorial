__author__ = 'remillet'
from django.conf.urls import patterns, url

from ileaflog import views

urlpatterns = patterns('',
    (r'^$', 'ileaflog.views.index'),
    (r'^oauth/inat', 'ileaflog.views.oauth'),
#    (r'^(?P<poll_id>\d+)/$', 'polls.views.detail'),
#    (r'^(?P<poll_id>\d+)/results/$', 'MyDjangoApp.polls.views.results'),
#    (r'^(?P<poll_id>\d+)/vote/$', 'MyDjangoApp.polls.views.vote'),
)
