from django.db import models
from django_quill.fields import QuillField

class Refunds(models.Model):
    class Meta:
        verbose_name_plural = "Refunds & Returns"

    content = QuillField()

class Postage(models.Model):
    class Meta:
        verbose_name_plural = "Postage and Packaging"
        
    content = QuillField()

class Privacy(models.Model):
    class Meta:
        verbose_name_plural = "Privacy Policy"
        
    content = QuillField()

