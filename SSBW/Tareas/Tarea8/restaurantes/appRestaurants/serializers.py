from rest_framework_mongoengine import serializers
from rest_framework_mongoengine import viewsets

from .models import restaurantes

class restaurantesSerializer(serializers.DocumentSerializer):

   class Meta:
       model = restaurantes
       fields = ('name', 'id_restaurant', 'image', 'address')


class restaurantesViewSet(viewsets.ModelViewSet):
   lookup_field = 'id_restaurant'
   serializer_class = restaurantesSerializer

   def get_queryset(self):
       return restaurantes.objects.all()
