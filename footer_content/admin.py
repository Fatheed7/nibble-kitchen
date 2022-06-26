from django.contrib import admin
from .models import Refunds, Postage, Privacy

@admin.register(Refunds)
class QuillPostAdmin(admin.ModelAdmin):
    pass
