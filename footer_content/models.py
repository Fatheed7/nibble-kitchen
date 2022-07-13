from django.db import models
from django_quill.fields import QuillField


class Returns(models.Model):
    class Meta:
        verbose_name_plural = "Refunds & Returns"

    name = models.CharField(max_length=255, null=True)
    content = QuillField()


class Postage(models.Model):
    class Meta:
        verbose_name_plural = "Postage and Packaging"

    name = models.CharField(max_length=255, null=True)
    content = QuillField()


class Privacy(models.Model):
    class Meta:
        verbose_name_plural = "Privacy Policy"

    name = models.CharField(max_length=255, null=True)
    content = QuillField()


class About(models.Model):
    class Meta:
        verbose_name_plural = "About Us"

    name = models.CharField(max_length=255, null=True)
    content = QuillField()
