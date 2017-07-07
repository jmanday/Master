from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.core.files.base import ContentFile
import requests
import json
from appRestaurants.models import restaurantes
from appRestaurants.models import address
from appRestaurants.models import location
from appRestaurants.forms import AddRestaurant
from django.contrib.auth.decorators import login_required
import gridfs
import base64

# Create your views here.

@login_required
def index(request):
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'app/login.html', context)


@login_required
def home(request):
    context = {}
    return render(request,'app/home.html', context)


@login_required
def addRestaurant(request):
    req_map = 'http://maps.googleapis.com/maps/api/geocode/json?address='
    if request.method == 'POST':
        form = AddRestaurant(request.POST, request.FILES)
        if form.is_valid():
            form_id = form.cleaned_data['id_restaurant']
            form_name = form.cleaned_data['name']
            form_street = form.cleaned_data['direc']
            form_zipcode = form.cleaned_data['zipcode']
            form_city = form.cleaned_data['city']
            form_image = request.FILES['image']

            name = form_name
            name = form_name.replace(' ', '+')
            req_map = req_map + name

            req = requests.get(req_map)
            jsonList = []
            jsonList.append(json.loads(req.text))
            glat = (jsonList[0]["results"][0]["geometry"]["location"]["lat"])
            glng = (jsonList[0]["results"][0]["geometry"]["location"]["lng"])
            instanceLocation = location(lat = glat, lon = glng)
            instanceAddress = address(city = form_city, street = form_street, zipcode = form_zipcode, coord = instanceLocation)
            instanceRestaurant = restaurantes(name = form_name, id_restaurant = form_id, image = form_image, address = instanceAddress)
            instanceRestaurant.save()

            return HttpResponseRedirect('/restaurantes/home')
    else:
        form = AddRestaurant()

    return render(request, 'app/addRestaurant.html', {'form': form})


@login_required
def searchRestaurant(request):
    if request.method == 'POST':
        context = {}
        idRestaurant = request.POST.get('searched_id')
        rest = restaurantes.objects(id_restaurant = idRestaurant)

        for d in rest:
            context["name"] = d.name
            context["id_restaurant"] = d.id_restaurant
            context["street"] = d.address.street
            context["city"] = d.address.city
            context["zipcode"] = d.address.zipcode
            context["image"] = d.image
            if (d.image):
                context["image"] = base64.b64encode(d.image.read())

        return render(request,'app/getRestaurant.html', {'data': context})
    else:
        return HttpResponseRedirect('/restaurantes/searchRestaurant/')

@login_required
def listRestaurants(request):
    contex = {
        "rests" : restaurantes.objects, # todos los restaurantes
    }

    return render(request, 'app/listRestaurants.html', {'data': contex["rests"]})


@login_required
def deleteRestaurant(request):
    if request.method == 'POST':
        context = {}
        idRestaurant = request.POST.get('searched_id')
        rest = restaurantes.objects(id_restaurant = idRestaurant)
        rest.delete()

    return HttpResponseRedirect('/restaurantes/home/')


def profile(request):
    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username)
        jsonList = []
        jsonList.append(json.loads(req.text))
        userData = {}
        for data in jsonList:
            userData['name'] = data['name']
            userData['blog'] = data['blog']
            userData['email'] = data['email']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['avatar_url'] = data['avatar_url']
            userData['followers'] = data['followers']
            userData['following'] = data['following']
        parsedData.append(userData)
    return render(request, 'app/profile.html', {'data': parsedData})
