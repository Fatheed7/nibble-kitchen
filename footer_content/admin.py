from django.contrib import admin
from .models import Returns, Postage, Privacy, About


@admin.register(Returns)
@admin.register(Postage)
@admin.register(Privacy)
@admin.register(About)
class QuillPostAdmin(admin.ModelAdmin):
    list_display = ['name']
    pass
