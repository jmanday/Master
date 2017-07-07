from django import forms
from django.forms import ModelForm

class AddRestaurant(forms.Form):
    name = forms.CharField(label='Nombre', max_length=50)
    id_restaurant = forms.CharField(label='Identificador', max_length=8)
    direc = forms.CharField(label='Dirección', max_length=50)
    zipcode = forms.CharField(label='Código Postal', max_length=5)
    city = forms.CharField(label='Ciudad', max_length=15)
    image = forms.FileField(label='Imagen')
