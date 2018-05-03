from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$', views.post_list, name='post_list'),
    url(r'^detail/(?P<detail_pk>\d+)/$', views.post_detail, name='post_detail'),
]