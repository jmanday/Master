"""restaurantes URL Configuration"""

from django.conf.urls import include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/restaurantes/home'

urlpatterns = [
  url(r'^restaurantes/', include('appRestaurants.urls')),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^accounts/', include('registration.backends.simple.urls')),
]
