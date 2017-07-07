from mongoengine import *
import datetime

connect('test')

# Esquema para la BD de pruebas de mongoDB

class addr(EmbeddedDocument):
    building = StringField()
    street   = StringField()
    city     = StringField()   # insertado
    zipcode  = IntField()
    coord    = GeoPointField() # OJO, al BD de test estan a reves
                               # [long, lat] en vez de [lat, long]

class likes(EmbeddedDocument):
    grade = StringField(max_length=1)
    score = IntField()
    date  = DateTimeField()

class restaurants(Document):
    name             = StringField(required=True, max_length=80)
    restaurant_id    = IntField()
    cuisine          = StringField()
    borough          = StringField()
    address          = EmbeddedDocumentField(addr)              # en la misma colleccion
    grades           = ListField(EmbeddedDocumentField(likes))


# Inserta un nuevo restaurante en la base de datos
dir = addr(street="Hermosa, 5 ", city="Granada", zipcode=18010, coord=[37.1766872, -3.5965171])  # asi estan bien
r = restaurants(name="Casa Julio", cuisine="Granaina", borough="Centro", address=dir)
r.save()

# Consulta, los tres primeros
for r in restaurants.objects[:3]:
    print (r.name, r.address.coord, r.grades[0].date)

# Consulta, los tres primeros
res = restaurants.objects.filter(cuisine="Granaina")
for r in res:
    print (r.name)

# Hacer mas consultas, probar las de geolocalizacion
# ...
