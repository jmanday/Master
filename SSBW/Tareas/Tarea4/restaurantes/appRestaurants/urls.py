# appRestaurants/urls.py
from django.conf.urls import url
from appRestaurants import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^home/$', views.home, name='home'),
  url(r'^searchRestaurant/$', views.searchRestaurant, name='searchRestaurant'),
  url(r'^listRestaurants/$', views.listRestaurants, name='listRestaurants'),
  url(r'^addRestaurants/$', views.addRestaurant, name='addRestaurant'),
  url(r'^profile/$', views.profile, name='profile')
]
