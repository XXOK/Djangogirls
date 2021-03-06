from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$', views.post_list, name='post_list'),
    url(r'^detail/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^detail/(?P<pk>\d+)/edit$', views.post_edit, name='post_edit'),
    url(r'^maps/$', views.map_detail, name='map_detail'),
    url(r'^maps/new/$', views.map_new, name='map_new'),
]