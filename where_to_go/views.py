from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from places.models import Place

moscow_legends = Place.objects.get(placeId='moscow_legends')
roofs24 = Place.objects.get(placeId='roofs24')
places_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [moscow_legends.lng, moscow_legends.lat]
            },
            "properties": {
                "title": "«Легенды Москвы",
                "placeId": "moscow_legends",
                "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [roofs24.lng, roofs24.lat]
            },
            "properties": {
                "title": "Крыши24.рф",
                "placeId": "roofs24",
                "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/roofs24.json"
            }
        }
    ]
}


def index(request):
    return render(request, 'index.html', {'places_geojson': places_geojson})

