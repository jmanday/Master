from django.db import models
from mongoengine import *

connect('dbRestaurants')

# Esquema para la BD de pruebas de mongoDB

class location(EmbeddedDocument):
    lat      = FloatField()
    lon      = FloatField()

class address(EmbeddedDocument):
    city     = StringField()
    street   = StringField()
    zipcode  = StringField()
    coord    = EmbeddedDocumentField(location)

class restaurantes(Document):
    name             = StringField(required=True, max_length=80)
    id_restaurant    = StringField()
    image            = ImageField()
    address          = EmbeddedDocumentField(address)              # en la misma colleccion
