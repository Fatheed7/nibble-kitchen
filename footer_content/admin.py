from django.contrib import admin
from .models import Returns, Postage, Privacy

@admin.register(Returns)
class QuillPostAdmin(admin.ModelAdmin):
    list_display = ['name']
    pass

@admin.register(Postage)
class QuillPostAdmin(admin.ModelAdmin):
    list_display = ['name']
    pass


@admin.register(Privacy)
class QuillPostAdmin(admin.ModelAdmin):
    list_display = ['name']
    pass
