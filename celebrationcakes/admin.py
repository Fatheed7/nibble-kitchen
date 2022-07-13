from django.contrib import admin
from .models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image', 'image_url', 'caption')


admin.site.register(Gallery, GalleryAdmin)
