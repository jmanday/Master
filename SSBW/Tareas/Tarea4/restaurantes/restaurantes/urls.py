"""restaurantes URL Configuration"""

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
  url(r'^restaurantes/', include('appRestaurants.urls')),
  url(r'^admin/', include(admin.site.urls)),
  #url(r'^rango/', include('rango.urls')),
  #url(r'^accounts/', include('registration.backends.simple.urls')),
]
