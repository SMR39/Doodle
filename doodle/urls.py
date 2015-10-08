from django.conf.urls import patterns, url

from doodle import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       #url(r'^(?P<meeting_id>\d+)/$', views.list, name='list'),
                       url(r'^(?P<meeting_id>\d+)/$', views.details, name='details'),
                       url(r'^(?P<meeting_id>\d+)/results/$', views.results, name='results'),
                       url(r'^(?P<meeting_id>\d+)/room/$', views.room, name='room'),
                       url(r'^(?P<meeting_id>\d+)/room/roomdetail/$', views.roomdetail, name='roomdetail'),
                       url(r'^(?P<meeting_id>\d+)/room/roomselect/$', views.roomselect, name='roomselect'),
                       url(r'^(?P<meeting_id>\d+)/room/chooseroom/$', views.chooseroom, name='chooseroom'),
                       )