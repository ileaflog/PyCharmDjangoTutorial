from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    (r'^$', 'polls.views.index'),
    (r'^(?P<poll_id>\d+)/$', 'polls.views.detail'),
    (r'^(?P<poll_id>\d+)/results/$', 'MyDjangoApp.polls.views.results'),
    (r'^(?P<poll_id>\d+)/vote/$', 'MyDjangoApp.polls.views.vote'),
)
