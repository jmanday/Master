# appRestaurants/urls.py
from django.conf.urls import url
from appRestaurants import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^home/$', views.home, name='home'),
  url(r'^searchRestaurant/$', views.searchRestaurant, name='searchRestaurant'),
  url(r'^listRestaurants/$', views.listRestaurants, name='listRestaurants'),
  url(r'^addRestaurant/$', views.addRestaurant, name='addRestaurant'),
  url(r'^deleteRestaurant/$', views.deleteRestaurant, name='deleteRestaurant'),
  url(r'^profile/$', views.profile, name='profile')
]
