from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin
from places.models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ['place', 'image', 'get_preview']
    readonly_fields = ["get_preview"]

    def get_preview(self, place):
        return format_html(
            f'<img src="{place.image.url}" width="auto" height="200px" />'
    )

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Image)

