from django.http import HttpResponse, Http404
from django.http.response import JsonResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.template import loader
from places.models import Place, Image
from django.urls import reverse


def get_place(request, post_id):
    place = get_object_or_404(Place, pk=post_id)
    images = get_list_or_404(Image, place=place)
    place_json = {
        "title": place.title,
        'imgs': [item.image.url for item in images],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
    return JsonResponse(place_json, safe=False,
                        json_dumps_params={'ensure_ascii': False, 'indent': 2})


def index(request):
    places = Place.objects.all()
    places_with_description = []
    for place in places:
        description = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [place.lng, place.lat]
                    },
                    "properties": {
                        "title": place.title,
                        "placeId": place.id,
                        "detailsUrl": reverse(get_place, args=[place.id])
                    }
                }
            ]
        }
        places_with_description.append(description)
    return render(request, 'index.html', {'places_geojson': places_with_description})

