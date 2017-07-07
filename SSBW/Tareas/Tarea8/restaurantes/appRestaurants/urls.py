# appRestaurants/urls.py
from django.conf.urls import url
from appRestaurants import views
from django.views.decorators.csrf import csrf_exempt

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()


urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^home/$', views.home, name='home'),
  url(r'^searchRestaurant/$', views.searchRestaurant, name='searchRestaurant'),
  url(r'^listRestaurants/$', views.listRestaurants, name='listRestaurants'),
  url(r'^addRestaurant/$', views.addRestaurant, name='addRestaurant'),
  url(r'^deleteRestaurant/$', views.deleteRestaurant, name='deleteRestaurant'),
  url(r'^getRestaurant/$', views.getRestaurant, name='getRestaurant'),
  url(r'^modifyDatasRestaurant/$', views.modifyDatasRestaurant, name='modifyDatasRestaurant'),
  url(r'^profile/$', views.profile, name='profile'),
  url(r'^obtain-auth-token/$', csrf_exempt(obtain_auth_token))
]
