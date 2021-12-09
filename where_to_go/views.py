from django.http import HttpResponse, Http404
from django.http.response import JsonResponse
from django.shortcuts import render, get_list_or_404
from django.template import loader
from places.models import Place, Image

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
def get_place_json(place):
    images = get_list_or_404(Image, place=place)
    place_json = {
        "title": place.title,
        'img': [item.image.url for item in images],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
    return place_json

def index(request):
    return render(request, 'index.html', {'places_geojson': places_geojson})



def places(request, post_id):
    try:
        place = Place.objects.get(pk=post_id)
    except Place.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    return JsonResponse(get_place_json(place), safe=False,
                        json_dumps_params={'ensure_ascii': False, 'indent': 2})

