from django.http import HttpResponse, Http404
from django.http.response import JsonResponse
from django.shortcuts import render, get_list_or_404
from django.template import loader
from places.models import Place, Image
from django.urls import reverse


def all_places(request, post_id):
    try:
        place = Place.objects.get(pk=post_id)
    except Place.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
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
                        "detailsUrl": reverse(all_places, args=[place.id])#"https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
                    }
                }
            ]
        }
        places_with_description.append(description)
    return render(request, 'index.html', {'places_geojson': places_with_description})

