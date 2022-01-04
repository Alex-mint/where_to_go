from django.contrib import admin

from places.models import Place, Image


#@admin.register(Place)
class ImageInline(admin.TabularInline):
    model = Image
    fields = ['place', 'image', 'number']

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

# class BookInline(admin.TabularInline):
#     model = Book
#
# class AuthorAdmin(admin.ModelAdmin):
#     inlines = [
#         BookInline,
#     ]
