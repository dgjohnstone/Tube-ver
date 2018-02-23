from django.conf.urls import url
from . import views     


urlpatterns = [
    url(r'^dashboard$', views.dashboard), 
    url(r'^new$', views.newVideo),
    url(r'^create$', views.create),
    url(r'^show/(?P<id>\d+)$',views.show),
    url(r'^delete/(?P<id>\d+)$',views.delete),
    url(r'^update/(?P<id>\d+)$', views.update),
    url(r'^change/(?P<id>\d+)$', views.change),
  ]