from django.contrib import admin
from django.utils.safestring import mark_safe

from places.models import Place, Image


#@admin.register(Place)
class ImageInline(admin.TabularInline):
    model = Image
    fields = ['place', 'image', 'get_preview', 'number']
    readonly_fields = ["get_preview"]

    def get_preview(self, place):
        return mark_safe(f'<img src="{place.image.url}" width="auto" height="200px" />'
    )

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


